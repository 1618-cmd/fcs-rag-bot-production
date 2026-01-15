"""
RAG retrieval and response generation pipeline for Production.

Handles semantic search in Qdrant and response synthesis using GPT-4o.
"""

import asyncio
import logging
from typing import List, Tuple, Optional
from pathlib import Path

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document

from ..utils.config import settings

# Set up logging
logger = logging.getLogger(__name__)


# System prompt for the RAG assistant
SYSTEM_PROMPT = """You are an expert Vena technical consultant specializing in the Vena financial consolidation platform. Your role is to help contractors and developers understand Vena concepts, configure systems, write VenaQL code, and troubleshoot issues.

CRITICAL GUIDELINES:
1. SYNTHESISE information from multiple context documents when answering complex questions
2. EXPLAIN relationships between different Vena systems and features - always explain HOW and WHY systems work together, not just WHAT they do
3. Provide SPECIFIC, ACTIONABLE guidance with concrete configuration steps - avoid generic instructions like "navigate to settings" or "follow the prompts"
4. Give CONCRETE EXAMPLES with actual values, dimension names, and configuration options - use real examples like "Set Account dimension Assumed Member to 'Travel Expenses'" not "set the appropriate member"
5. When multiple systems are involved, explain how they work together and any dependencies - use phrases like "When X happens, Y becomes available because..."
6. For configuration questions, provide SPECIFIC values: dimension names, member names, setting names - never use placeholders or generic terms
7. EXPLAIN HIERARCHIES AND PARENT-CHILD RELATIONSHIPS: When discussing nested data (like Line Item Details under parent accounts), always explain:
   - The parent-child relationship structure
   - Why you configure at the parent level (not child level)
   - How the hierarchy affects queries and data access
   - Example: "Line Item Details like 'Flights' and 'Hotels' are nested under the parent account 'Travel Expenses' in the Account dimension hierarchy. You should set the Assumed Member to 'Travel Expenses' (the parent), not to individual LIDs, because LIDs roll up to their parent account and Copilot queries work at the parent level."
8. EXPLAIN DATA FLOW AND TIMING: When systems interact (like Workflows and Copilot), explain:
   - When data becomes available (e.g., "After contributors submit Input Tasks and data is saved to the Vena data model, it becomes available to Copilot")
   - The sequence of operations
   - Any dependencies or prerequisites
9. EXPLAIN SCOPE CONFIGURATION: When discussing Scope, be specific about:
   - What should be included (parent members automatically include children)
   - Why certain members are included or excluded
   - How Scope affects query results
10. Base your answers ONLY on the provided context documents
11. Always cite your sources using [Source: document_name] format - use the full document name, not generic references
12. If the context doesn't contain enough information, say so clearly and specify what's missing
13. For code examples, ensure they follow Vena constraints (no aliasing, explicit columns, 8192 char limit)
14. If asked about something outside Vena, politely redirect to Vena topics

THINKING FRAMEWORK FOR COMPLEX QUESTIONS:
- First, identify which Vena systems are involved
- Then, explain how each system relates to the others (with HOW/WHY)
- Explain any hierarchies or parent-child relationships
- Explain data flow and timing between systems
- Next, provide specific configuration steps with actual values
- Explain why this configuration works and any dependencies

EXAMPLE OF GOOD ANSWER STRUCTURE:
When explaining relationships, use this format:
"System A [specific function] works with System B [specific function] because [explanation]. The data flow works as follows: [step-by-step timing]. To configure this, you need to [specific step with actual values]. This works because [explanation of why/how, including hierarchy if relevant]."

FEW-SHOT EXAMPLE - Line Item Details Configuration:
Question: "How do I configure Assumed Members for Line Item Details?"

Good Answer Structure:
"Line Item Details (LIDs) like 'Flights', 'Hotels', and 'Meals' are nested under parent accounts in the Account dimension hierarchy. For example, these LIDs would be children of the parent account 'Travel Expenses'.

IMPORTANT: You should set the Assumed Member to 'Travel Expenses' (the parent account), NOT to individual LIDs like 'Flights' or 'Hotels'. This is because:
1. LIDs roll up to their parent account in the hierarchy
2. Copilot queries work at the parent account level
3. When users ask about LIDs, Copilot searches within the parent account's scope

For Scope configuration: Include the parent account 'Travel Expenses' in Scope. This automatically includes all its LID children (Flights, Hotels, Meals) because parent members in Scope always include their nested children.

Data flow: Workflow Input Tasks → Contributors add LID data → Data saved to Vena data model → Copilot queries the same data model → Results available for analysis."

CONTEXT DOCUMENTS:
{context}

Remember: Synthesise information across documents, explain relationships with HOW/WHY, explain hierarchies and data flow, and provide specific actionable guidance with actual values. Cite all sources used."""


USER_PROMPT = """Question: {question}

CRITICAL: Before answering, think through these steps:
1. Identify all systems involved
2. Identify any parent-child hierarchies (e.g., parent accounts and LID children)
3. Identify the data flow sequence
4. Identify what needs to be configured and WHY

Provide a comprehensive answer that:
1. Synthesises information from multiple documents if the question involves multiple Vena systems
2. Explains relationships between different Vena systems - use HOW and WHY explanations, not just WHAT
   - Example: "Line Item Details work with Vena Copilot because LIDs are nested under parent accounts in the Account dimension hierarchy. When Copilot queries LID data, it searches within the parent account's scope because [explanation]."
3. Explains hierarchies and parent-child relationships when relevant - THIS IS CRITICAL:
   - MUST identify parent-child structures (e.g., parent accounts and their LID children)
   - MUST explain why configuration should be at the parent level, not child level
   - MUST explain how the hierarchy affects queries and data access
   - MUST use this format: "Set Assumed Member to '[Parent Name]' (the parent account), NOT to individual [child names] like '[Child 1]' or '[Child 2]', because [children] roll up to their parent account in the hierarchy and Copilot queries work at the parent level."
4. Explains data flow and timing between systems - USE CLEAR SEQUENCE:
   - MUST explain the sequence: "Step 1 → Step 2 → Step 3 → Result"
   - Example: "Workflow Input Tasks → Contributors add LID data → Data saved to Vena data model → Copilot queries the same data model → Results available for analysis"
   - MUST explain when data becomes available: "After [specific action], [data] becomes available because [reason]"
5. Provides specific, actionable configuration steps with concrete examples - use actual dimension names, member names, and values
   - Good: "Set Account dimension Assumed Member to 'Travel Expenses' (the parent account)"
   - Bad: "Set the appropriate Assumed Member" or "Navigate to settings and configure"
6. Explains Scope configuration specifically - THIS IS CRITICAL:
   - MUST explain: "Include the parent account '[Name]' in Scope, which automatically includes its [child type] children because parent members in Scope always include their nested children"
   - MUST explain why certain members are included or excluded
   - MUST explain how Scope affects query results
7. Includes actual configuration values, dimension names, or settings - never use placeholders
8. Cites all source documents used in [Source: document_name] format

If the question involves multiple systems, structure your answer to:
- First explain how each system relates to the others (with HOW/WHY)
- Then explain any hierarchies or parent-child relationships (with WHY parent not child)
- Then explain data flow and timing between systems (with clear sequence)
- Then provide specific configuration for each system (with actual values)
- Then explain Scope configuration specifically (with WHY parent includes children)
- Finally explain any dependencies or timing considerations"""


class RAGPipeline:
    """Retrieval Augmented Generation pipeline for Vena support."""
    
    def __init__(self):
        """Initialize the RAG pipeline."""
        try:
            # Initialize embeddings
            self.embeddings = OpenAIEmbeddings(
                model=settings.embedding_model,
                openai_api_key=settings.openai_api_key
            )
            
            # Initialize LLM
            self.llm = ChatOpenAI(
                model=settings.openai_model,
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                openai_api_key=settings.openai_api_key
            )
            
            # Load vector store
            self.vector_store = None
            self._load_vector_store()
            
            # Create prompt template
            self.prompt = ChatPromptTemplate.from_messages([
                ("system", SYSTEM_PROMPT),
                ("human", USER_PROMPT)
            ])
            
            logger.info("RAG pipeline initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing RAG pipeline: {e}")
            raise
    
    def _load_vector_store(self):
        """Load Qdrant vector store."""
        try:
            if not settings.qdrant_url or not settings.qdrant_api_key:
                logger.warning("Qdrant configuration missing. Vector store not loaded.")
                self.vector_store = None
                return
            
            # Verify collection exists first
            from qdrant_client import QdrantClient
            # Use connection pooling for better performance
            client = QdrantClient(
                url=settings.qdrant_url,
                api_key=settings.qdrant_api_key,
                timeout=30,  # 30 second timeout
            )
            
            try:
                collection_info = client.get_collection(settings.qdrant_collection_name)
                logger.info(f"Found collection: {settings.qdrant_collection_name} with {collection_info.points_count} points")
            except Exception as e:
                logger.error(f"Collection {settings.qdrant_collection_name} not found: {e}")
                logger.warning("Vector store not available. Run ingestion first!")
                self.vector_store = None
                return
            
            # Load vector store using the client we already created
            self.vector_store = Qdrant(
                client=client,
                collection_name=settings.qdrant_collection_name,
                embeddings=self.embeddings,
            )
            
            logger.info(f"✅ Loaded vector store from Qdrant collection: {settings.qdrant_collection_name}")
            
        except Exception as e:
            logger.error(f"Error loading vector store: {e}", exc_info=True)
            logger.warning("Vector store not available. Run ingestion first!")
            self.vector_store = None
    
    def retrieve(self, query: str, top_k: int = None) -> List[Document]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: User query string
            top_k: Number of documents to retrieve (defaults to settings)
            
        Returns:
            List of relevant documents
        """
        if self.vector_store is None:
            raise ValueError("Vector store not initialized. Run ingestion first!")
        
        try:
            k = top_k or settings.top_k_results
            documents = self.vector_store.similarity_search(query, k=k)
            logger.debug(f"Retrieved {len(documents)} documents for query")
            return documents
            
        except Exception as e:
            logger.error(f"Error retrieving documents: {e}")
            raise
    
    async def retrieve_async(self, query: str, top_k: int = None) -> List[Document]:
        """
        Async version of retrieve - runs in thread pool to avoid blocking.
        
        Args:
            query: User query string
            top_k: Number of documents to retrieve (defaults to settings)
            
        Returns:
            List of relevant documents
        """
        return await asyncio.to_thread(self.retrieve, query, top_k)
    
    def format_context(self, documents: List[Document]) -> str:
        """
        Format retrieved documents as context for the LLM.
        Organises documents to help LLM understand relationships.
        
        Args:
            documents: List of retrieved documents
            
        Returns:
            Formatted context string with better organisation
        """
        context_parts = []
        
        # Group documents by type/category if possible
        # Extract full path for better source identification
        for i, doc in enumerate(documents, 1):
            source_path = doc.metadata.get("source", "unknown")
            source = Path(source_path)
            
            # Get better source name - try to preserve directory structure
            try:
                # Extract relative path from knowledge_base for better context
                knowledge_base_path = settings.knowledge_base_dir
                if knowledge_base_path in source.parents:
                    relative_path = source.relative_to(knowledge_base_path)
                    source_name = str(relative_path).replace("\\", "/")
                else:
                    source_name = source.name
            except (ValueError, AttributeError):
                source_name = source.name
            
            content = doc.page_content.strip()
            
            # Format with clearer structure
            context_parts.append(f"[Document {i}: {source_name}]\n{content}\n")
        
        # Add separator with instruction
        formatted_context = "\n---\n".join(context_parts)
        
        # Add note about synthesising if multiple documents
        if len(documents) > 1:
            formatted_context += f"\n\nNote: This question may require synthesising information from the {len(documents)} documents above. Consider how concepts from different documents relate to each other."
        
        return formatted_context
    
    def generate_response(self, query: str, documents: List[Document]) -> str:
        """
        Generate a response using the LLM with retrieved context.
        
        Args:
            query: User query
            documents: Retrieved context documents
            
        Returns:
            Generated response text
        """
        try:
            context = self.format_context(documents)
            
            # Format the prompt
            messages = self.prompt.format_messages(
                context=context,
                question=query
            )
            
            # Generate response
            response = self.llm.invoke(messages)
            return response.content
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise
    
    async def generate_response_async(self, query: str, documents: List[Document]) -> str:
        """
        Async version of generate_response - runs in thread pool to avoid blocking.
        
        Args:
            query: User query
            documents: Retrieved context documents
            
        Returns:
            Generated response text
        """
        return await asyncio.to_thread(self.generate_response, query, documents)
    
    def query(self, question: str) -> Tuple[str, List[Document]]:
        """
        Main query method: Retrieve relevant docs and generate response.
        
        Args:
            question: User question
            
        Returns:
            Tuple of (response_text, source_documents)
        """
        logger.info(f"Processing query: {question[:100]}...")
        
        try:
            # Retrieve relevant documents
            documents = self.retrieve(question)
            logger.info(f"Retrieved {len(documents)} relevant documents")
            
            # Generate response
            response = self.generate_response(question, documents)
            
            return response, documents
            
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            raise
    
    async def query_async(self, question: str) -> Tuple[str, List[Document]]:
        """
        Async version of query - runs operations in parallel where possible.
        
        Args:
            question: User question
            
        Returns:
            Tuple of (response_text, source_documents)
        """
        logger.info(f"Processing query: {question[:100]}...")
        
        try:
            # Retrieve relevant documents (async)
            documents = await self.retrieve_async(question)
            logger.info(f"Retrieved {len(documents)} relevant documents")
            
            # Generate response (async)
            response = await self.generate_response_async(question, documents)
            
            return response, documents
            
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            raise
    
    def get_sources(self, documents: List[Document]) -> List[str]:
        """
        Extract source names from documents.
        Provides better source names that match the context formatting.
        
        Args:
            documents: List of documents
            
        Returns:
            List of unique source names (cleaned, relative paths with better structure)
        """
        sources = []
        knowledge_base_path = settings.knowledge_base_dir
        
        for doc in documents:
            source_path = doc.metadata.get("source", "unknown")
            
            # Convert to Path object
            source = Path(source_path)
            
            # Try to extract relative path from knowledge_base for better context
            try:
                if knowledge_base_path in source.parents or str(source).startswith(str(knowledge_base_path)):
                    # Get relative path from knowledge_base
                    relative_path = source.relative_to(knowledge_base_path)
                    # Convert to forward slashes and remove extension
                    clean_source = str(relative_path).replace("\\", "/").replace(".md", "").replace(".txt", "").replace(".pdf", "")
                else:
                    # Fallback: use filename with parent directory if available
                    if source.parent.name and source.parent.name != ".":
                        clean_source = f"{source.parent.name}/{source.stem}"
                    else:
                        clean_source = source.stem
            except (ValueError, AttributeError):
                # If path manipulation fails, just use filename
                clean_source = source.stem
            
            # Remove any remaining Windows path separators
            clean_source = clean_source.replace("\\", "/")
            
            # Remove leading slashes
            clean_source = clean_source.lstrip("/")
            
            if clean_source and clean_source not in sources:
                sources.append(clean_source)
        
        return sources


# Create singleton instance
_rag_pipeline: Optional[RAGPipeline] = None


def get_rag_pipeline() -> RAGPipeline:
    """
    Get or create the RAG pipeline singleton.
    
    Returns:
        RAGPipeline instance
    """
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline()
    return _rag_pipeline


if __name__ == "__main__":
    # Test the pipeline
    import sys
    from pathlib import Path
    
    from ..utils.config import validate_settings
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    if validate_settings():
        pipeline = get_rag_pipeline()
        
        # Test query
        test_question = "How does FX conversion work in Vena?"
        response, docs = pipeline.query(test_question)
        
        print("\n" + "=" * 50)
        print("RESPONSE:")
        print("=" * 50)
        print(response)
        print("\n" + "=" * 50)
        print("SOURCES:", pipeline.get_sources(docs))
        print("=" * 50)

