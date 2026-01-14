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
SYSTEM_PROMPT = """You are a knowledgeable technical assistant specializing in the Vena financial consolidation platform. Your role is to help contractors and developers understand Vena concepts, write VenaQL code, and troubleshoot issues.

IMPORTANT GUIDELINES:
1. Base your answers ONLY on the provided context documents
2. Always cite your sources using [Source: document_name] format
3. If the context doesn't contain enough information, say so clearly
4. For code examples, ensure they follow Vena constraints (no aliasing, explicit columns, 8192 char limit)
5. Be concise but thorough
6. If asked about something outside Vena, politely redirect to Vena topics

CONTEXT DOCUMENTS:
{context}

Remember: Only use information from the context above. Cite your sources."""


USER_PROMPT = """Question: {question}

Please provide a helpful answer based on the context documents provided. Include source citations."""


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
        
        Args:
            documents: List of retrieved documents
            
        Returns:
            Formatted context string
        """
        context_parts = []
        
        for i, doc in enumerate(documents, 1):
            source = Path(doc.metadata.get("source", "unknown")).stem
            content = doc.page_content.strip()
            context_parts.append(f"[Document {i}: {source}]\n{content}\n")
        
        return "\n---\n".join(context_parts)
    
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
        
        Args:
            documents: List of documents
            
        Returns:
            List of unique source names
        """
        sources = []
        for doc in documents:
            source = Path(doc.metadata.get("source", "unknown")).stem
            if source not in sources:
                sources.append(source)
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

