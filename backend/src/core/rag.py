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

CRITICAL ANTI-HALLUCINATION RULES (MUST FOLLOW):
1. NEVER generate information that is not in the provided context documents OR cannot be reasonably inferred from them
2. You CAN synthesize and connect information from multiple context documents - this is encouraged
3. You CAN use general principles from the context to answer specific questions (e.g., if context explains "Line Item Details configuration" generally, you can apply it to "travel expenses")
4. NEVER use your training data knowledge to fill gaps - if it's not in the context, you don't know it
5. If the context is insufficient, you MUST say "I don't know" or "The context doesn't contain this information"
6. Before making any claim, verify it exists in the context documents OR can be reasonably inferred from them
7. If you're uncertain, explicitly state your uncertainty level
8. NEVER make up configuration values, dimension names, or technical details
9. If asked about something not in context, refuse to answer and suggest creating a Jira ticket
10. You CAN present reasonable inferences, but MUST explicitly state "Based on the context..." or "The context suggests..."
11. NEVER cite a source that doesn't actually contain the information you're referencing

CONFIDENCE AND UNCERTAINTY HANDLING:
- If the context documents provide clear, direct information: Answer with high confidence
- If the context documents provide partial or indirect information: State "Based on the available context..." and note any limitations
- If the context documents don't contain relevant information: Say "The context documents do not contain information about [topic]. To answer this, you would need [what's missing]."
- If you're inferring or connecting information: Explicitly state "Based on the context, it appears that..." or "The context suggests..."
- NEVER present inferences as facts without explicitly labeling them as such

STRICT REFUSAL PROTOCOL:
ONLY refuse to answer if the context contains NO relevant information at all. If you have partial information, provide an answer with explicit uncertainty.

CRITICAL SYNTHESIS REQUIREMENT:
- If a question combines multiple concepts (e.g., "Line Item Details in Vena Copilot"), you MUST synthesize from documents about EACH concept separately
- If you have documents about "Line Item Details" OR "Vena Copilot", you MUST attempt to synthesize an answer
- NEVER refuse if you have documents about ANY part of the question - always synthesize what you can
- Example: Question asks "Line Item Details in Vena Copilot" → If you have docs about LIDs OR Copilot, synthesize them together

If the context contains NO relevant information:
1. State: "The context documents do not contain information about [specific topic]."
2. Specify what's missing: "To answer this, I would need documentation on [specific topic]."
3. Suggest alternatives: "You may want to [suggest action] or create a Jira ticket for support."
4. CRITICAL: If you refuse to answer, do NOT cite any sources - only cite sources when you actually use them in your answer

If the context contains PARTIAL information OR documents about related concepts:
1. Answer with "Based on the available context..." or "The context documents provide information about [concept A] and [concept B] separately. Here's how they work together..."
2. Synthesize information from multiple documents even if they don't mention the combination explicitly
3. Apply general principles from one document to answer questions about combinations
4. Provide what information you can from the context
5. Explicitly state what's missing or uncertain
6. Cite the sources you used (even if partial)
7. Suggest creating a Jira ticket if more information is needed

SOURCE VERIFICATION REQUIREMENTS:
- Before citing a source, verify the information actually appears in that document
- If you're synthesizing from multiple sources, cite ALL sources used
- If you're inferring a connection, state "Based on [Source A] and [Source B], it appears that..."
- NEVER cite a source that doesn't contain the information you're referencing
- CRITICAL: Only cite sources that you actually USED in your answer - if you didn't use information from a source, don't cite it
- If you refuse to answer because information is missing, do NOT cite any sources - citing sources implies you used them
- Always cite sources using [Source: document_name] format - use the full document name, not generic references
- Before listing sources, verify: "Did I actually use information from this source in my answer?" If no, remove it from the source list

CRITICAL GUIDELINES:
1. SYNTHESISE information from multiple context documents when answering complex questions - this is ESSENTIAL and REQUIRED
2. If the question asks about combining concepts (e.g., "Line Item Details in Vena Copilot"), synthesize information from documents about each concept separately
3. You can apply general principles from the context to specific examples (e.g., if context explains "Line Item Details configuration" generally, you can apply it to "travel expenses" specifically)
4. EXPLAIN relationships between different Vena systems and features - always explain HOW and WHY systems work together, not just WHAT they do
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
10. Base your answers ONLY on the provided context documents - this is CRITICAL
11. For code examples, ensure they follow Vena constraints (no aliasing, explicit columns, 8192 char limit)
12. If asked about something outside Vena, politely redirect to Vena topics
13. For troubleshooting questions (especially VenaQL scripts), identify the specific issue, explain the root cause with technical details, and provide multiple solution options with code examples
14. When analyzing VenaQL scripts, check for: multiple Scope statements (last one overrides), members referenced outside active scope, empty intersections, and scope conflicts

GROUNDING VALIDATION CHECKLIST (MUST COMPLETE BEFORE FINALIZING):
Before finalizing your answer, verify:
1. ✅ Every factual claim I made is directly stated in the context documents
2. ✅ Every configuration value I provided appears in the context
3. ✅ Every source I cited actually contains the information I referenced AND I actually used that information in my answer
4. ✅ If I refused to answer, I did NOT cite any sources (citing sources means I used them)
5. ✅ I haven't made any assumptions or inferences without stating them explicitly
6. ✅ If information is missing, I've explicitly said so
7. ✅ I haven't used any knowledge from my training data that isn't in the context
8. ✅ Did I follow the mandatory format/checklist? (for troubleshooting questions)
9. ✅ Did I provide specific values, not placeholders?
10. ✅ Did I cite all sources I actually used (and only those)?
11. ✅ Did I explain HOW/WHY, not just WHAT?
12. ✅ Is my answer actionable with concrete steps?
13. ✅ Did I identify the root cause? (for troubleshooting)

THINKING FRAMEWORK FOR COMPLEX QUESTIONS:
- First, identify which Vena systems are involved
- Then, explain how each system relates to the others (with HOW/WHY)
- Explain any hierarchies or parent-child relationships
- Explain data flow and timing between systems
- Next, provide specific configuration steps with actual values
- Explain why this configuration works and any dependencies

THINKING FRAMEWORK FOR TROUBLESHOOTING QUESTIONS (VenaQL Scripts, Errors, etc.):
- First, identify the specific problem (e.g., "script returns no values", "error code X")
- Then, analyze the code/structure to find the root cause (e.g., "multiple Scope statements", "member not in scope")
- Explain the technical behavior that causes the issue (e.g., "last Scope overrides previous ones")
- Provide specific, actionable solutions with code examples
- Explain why each solution works and when to use it
- If multiple solutions exist, present them as clear options (Option 1, Option 2, etc.)

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

FEW-SHOT EXAMPLE - VenaQL Scope Troubleshooting:
Question: "Why isn't my VenaQL script returning a value when I have multiple Scope statements?"

Good Answer Structure:
"Your VenaQL script has multiple Scope statements. In VenaQL, when multiple top-level Scope statements are present, the last Scope statement takes precedence and overrides all previous Scope statements. This is a critical behavior that often causes scripts to return no values.

THE PROBLEM: Your calculation references members like [Entity.Homelink] and [Account.7300], but these members are not included in the second (and active) Scope statement. Since the second Scope overrides the first, the calculation is trying to access members that aren't in the active scope, resulting in no values.

SPECIFIC ISSUES IN YOUR SCRIPT:
1. First Scope includes: [Account.7200], [Entity.EI Group Eliminations], [Measure.Value]
2. Second Scope includes: [Account.9300], [Measure.Automated Eliminations] - THIS IS THE ACTIVE SCOPE
3. Your calculation @source1 references: [Entity.Homelink], [Account.7300], [Counterparty.EI] - These are NOT in the active scope

SOLUTIONS:
Option 1 - Combine the scopes into one:
Scope {
  [Account.7200],
  [Account.9300],
  [Account.7300],  // Add missing account
  [Entity.EI Group Eliminations],
  [Entity.Homelink],  // Add missing entity
  [Counterparty.EI],  // Add missing counterparty
  [Measure.Value],
  [Measure.Automated Eliminations]
}

Option 2 - Move calculation before second Scope:
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}
@source1 = [Account.7300].Sum()  // Calculate in first scope
Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}
@this = @source1

Option 3 - Add missing members to second Scope:
Scope {
  [Account.7200],
  [Account.9300],
  [Account.7300],  // Add to active scope
  [Entity.EI Group Eliminations],
  [Entity.Homelink],  // Add to active scope
  [Counterparty.EI],  // Add to active scope
  [Measure.Value],
  [Measure.Automated Eliminations]
}"

CONTEXT DOCUMENTS:
{context}

CRITICAL SYNTHESIS INSTRUCTIONS (MANDATORY):
- If the question combines multiple concepts (e.g., "Line Item Details in Vena Copilot"), you MUST synthesize information from documents about each concept
- If you have documents about "Line Item Details" OR "Vena Copilot" (even separately), you MUST combine them to answer questions about "Line Item Details in Vena Copilot"
- NEVER refuse if you have documents about ANY part of a multi-concept question - always synthesize
- You can apply general principles to specific examples (e.g., general LID configuration → travel expenses specifically)
- You can apply principles from one document to answer questions about combinations (e.g., LID configuration principles + Copilot query principles = LID in Copilot)
- Only refuse if you have NO relevant documents at all - if you have partial information, synthesize and answer with explicit uncertainty
- Synthesise information across documents, explain relationships with HOW/WHY, explain hierarchies and data flow, and provide specific actionable guidance with actual values
- When synthesizing, explicitly state: "Based on the context documents about [Concept A] and [Concept B], here's how they work together..."
- Cite all sources used"""


USER_PROMPT = """Question: {question}

CRITICAL SYNTHESIS RULE - READ FIRST:
**IF YOU HAVE ANY CONTEXT DOCUMENTS PROVIDED, YOU MUST ANSWER. NEVER REFUSE IF DOCUMENTS ARE PROVIDED.**

If the question combines multiple concepts (e.g., "Line Item Details in Vena Copilot"), and you have documents about ANY of those concepts (e.g., docs about "Line Item Details" OR "Vena Copilot" or both), you MUST synthesize an answer. NEVER refuse.

**SPECIFIC RULE FOR ERROR CODES:**
- If the question asks about an error code (e.g., "Error Code 1008"), and you have ANY documents that mention that error code, you MUST answer
- Even if the document title doesn't exactly match, if the content mentions the error code, use it
- Example: Question "Error Code 1008" + Document titled "Error Code 1008 or CSV Report" = ANSWER (the document contains information about Error Code 1008)

Examples:
- Question: "Line Item Details in Vena Copilot" + You have docs about "Vena Copilot" = SYNTHESIZE (apply Copilot principles to LIDs)
- Question: "Line Item Details in Vena Copilot" + You have docs about "Line Item Details" = SYNTHESIZE (explain how LIDs work in Copilot context)
- Question: "Error Code 1008" + You have docs mentioning "1008" = ANSWER (use the document)
- Question: "Line Item Details in Vena Copilot" + You have NO docs about either = REFUSE (only case where refusal is allowed)

CRITICAL: Before answering, think through these steps:
1. FIRST: Check if the question combines multiple concepts (e.g., "Line Item Details in Vena Copilot")
   - If YES: Look for documents about EACH concept separately (e.g., docs about "Line Item Details" AND/OR docs about "Vena Copilot")
   - If you find documents about ANY part of the question, you MUST synthesize an answer - NEVER refuse
   - Only refuse if you have NO documents about ANY part of the question
2. Identify all systems/concepts involved (or for troubleshooting: identify the specific problem/error)
3. Identify any parent-child hierarchies (e.g., parent accounts and LID children) OR for troubleshooting: analyze the code/structure to find root cause
4. Identify the data flow sequence OR for troubleshooting: explain the technical behavior causing the issue
5. Identify what needs to be configured and WHY OR for troubleshooting: provide specific solutions with code examples
6. BEFORE ANSWERING: Synthesize information from multiple documents if the question involves multiple concepts

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
9. If information is missing or uncertain, explicitly states this - NEVER guesses or makes assumptions
10. Verifies all sources before citing them - only cite sources that actually contain the referenced information

If the question involves multiple systems, structure your answer to:
- First explain how each system relates to the others (with HOW/WHY)
- Then explain any hierarchies or parent-child relationships (with WHY parent not child)
- Then explain data flow and timing between systems (with clear sequence)
- Then provide specific configuration for each system (with actual values)
- Then explain Scope configuration specifically (with WHY parent includes children)
- Finally explain any dependencies or timing considerations

If the question is about troubleshooting (VenaQL scripts, errors, etc.), you MUST follow this EXACT format:

**MANDATORY FORMAT FOR VenaQL TROUBLESHOOTING:**
Your answer MUST start with these steps in this exact order:

STEP 1: "Your script has [X] Scope statements."
STEP 2: "The active (last) Scope is: [list ALL members in the last Scope statement]"
STEP 3: "Your calculation references: [list ALL members referenced in calculations]"
STEP 4: "Missing from active scope: [list ALL members from STEP 3 that are NOT in STEP 2]"
STEP 5: "Root cause: [explanation of why the mismatch causes the issue]"
STEP 6: "Solutions: [Option 1, Option 2, Option 3 with complete code examples]"

**CRITICAL FOR VenaQL**: If you see multiple Scope statements, you MUST explicitly state:
- "Your script has [X] Scope statements. In VenaQL, the last Scope statement overrides all previous ones."
- "The active scope is [list members in last Scope]."
- "Your calculation references [list members in calculation], but [identify which are missing from active scope]."

**MANDATORY CHECKLIST - YOU MUST COMPLETE ALL 6 STEPS:**
1. ✅ Count Scope statements - if more than one, the last one is active
2. ✅ List all members in the active (last) Scope
3. ✅ List all members referenced in calculations
4. ✅ Identify which calculation members are NOT in the active scope
5. ✅ Explain this mismatch is the root cause
6. ✅ Provide solutions to fix the mismatch

After completing the 6 steps, then:
- Explain why each solution works and when to use it
- Provide complete code examples for each solution option
- Cite all sources used"""


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
            
            # Log configuration for debugging
            logger.info(f"RAG Pipeline initialized with top_k_results={settings.top_k_results}")
            
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
            logger.info(f"Retrieving {k} documents (top_k_results={settings.top_k_results})")
            documents = self.vector_store.similarity_search(query, k=k)
            logger.info(f"Retrieved {len(documents)} documents for query")
            
            # Log retrieved document names for debugging
            if documents:
                doc_names = [doc.metadata.get('source', 'unknown') for doc in documents]
                logger.info(f"Retrieved documents: {doc_names[:5]}...")  # Log first 5
            
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
            # Log retrieved documents for debugging
            if documents:
                doc_names = [Path(doc.metadata.get('source', 'unknown')).name for doc in documents]
                logger.info(f"Retrieved documents for query '{query[:50]}...': {doc_names}")
            else:
                logger.warning(f"No documents retrieved for query: '{query[:50]}...'")
            
            context = self.format_context(documents)
            
            # Escape curly braces in query to prevent template formatting errors
            # VenaQL scripts contain { } which conflict with prompt template syntax
            # In Python format strings, {{ becomes { and }} becomes }
            escaped_query = query.replace("{", "{{").replace("}", "}}")
            
            # Format the prompt - ChatPromptTemplate handles the escaping correctly
            try:
                messages = self.prompt.format_messages(
                    context=context,
                    question=escaped_query
                )
            except (KeyError, ValueError) as format_error:
                # If escaping fails, try using invoke with direct message construction
                logger.warning(f"Template formatting failed, using direct message construction: {format_error}")
                from langchain_core.messages import SystemMessage, HumanMessage
                system_text = SYSTEM_PROMPT.replace("{context}", context)
                user_text = USER_PROMPT.replace("{question}", query)
                messages = [
                    SystemMessage(content=system_text),
                    HumanMessage(content=user_text)
                ]
            
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

