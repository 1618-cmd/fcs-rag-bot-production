# FCS RAG Bot - High-Level Architecture

## Overview
A production-ready RAG (Retrieval Augmented Generation) system for Vena technical support, featuring a modern Next.js frontend and Python FastAPI backend with Qdrant Cloud vector database.

---

## Architecture Layers

### 1. Frontend Layer (Next.js)
**Technology:** Next.js 15, React 19, TypeScript, Tailwind CSS

**Purpose:** User interface for interacting with the RAG bot

**Key Components:**
- Chat interface with Claude-style UI
- Markdown rendering with syntax highlighting
- Conversation history management
- Real-time API communication

**High-Level Summary:**
- Provides a clean, modern chat interface where users can ask questions
- Handles user input, displays responses, and manages conversation state
- Communicates with backend via REST API calls
- Stores conversation history locally in browser

---

### 2. Backend API Layer (FastAPI)
**Technology:** FastAPI, Python 3.12+, Uvicorn ASGI server

**Purpose:** RESTful API server that processes RAG queries

**Key Components:**
- `/api/query` endpoint - Main RAG query handler
- `/api/health` endpoint - Health check
- CORS middleware for frontend communication
- Error handling and logging

**High-Level Summary:**
- Receives user questions from frontend via HTTP POST requests
- Validates input and routes to RAG pipeline
- Returns structured JSON responses with answers and sources
- Handles errors gracefully and tracks performance metrics

---

### 3. RAG Pipeline (LangChain)
**Technology:** LangChain 0.1.20, OpenAI API

**Purpose:** Core RAG logic - retrieval and generation

**Key Components:**
- `RAGPipeline` class - Main pipeline orchestrator
- Embedding generation (OpenAI)
- Vector search (Qdrant)
- LLM response generation (GPT-4o)

**High-Level Summary:**
- Orchestrates the entire RAG process from query to answer
- Converts queries to embeddings for semantic search
- Retrieves relevant document chunks from vector database
- Formats context and generates answers using GPT-4o
- Returns both the answer and source document references

---

### 4. Vector Database (Qdrant Cloud)
**Technology:** Qdrant Cloud (managed vector database)

**Purpose:** Stores and searches document embeddings

**Key Components:**
- Vector collection: `vena_rag_bot`
- Embedding storage (1536 dimensions for text-embedding-3-small)
- Metadata storage (source file names, chunk info)

**High-Level Summary:**
- Stores pre-computed embeddings of all document chunks
- Performs fast semantic similarity search
- Returns most relevant document chunks for any query
- Cloud-hosted for scalability and reliability

---

### 5. Document Ingestion Pipeline
**Technology:** LangChain document loaders, OpenAI embeddings

**Purpose:** Processes and indexes knowledge base documents

**Key Components:**
- Document loaders (Markdown, Text, PDF)
- Text chunking (RecursiveCharacterTextSplitter)
- Embedding generation
- Qdrant storage

**High-Level Summary:**
- Reads all documents from `knowledge_base/` directory
- Splits documents into manageable chunks (500 tokens each)
- Generates embeddings for each chunk using OpenAI
- Stores chunks and embeddings in Qdrant for later retrieval
- Run manually when knowledge base is updated

---

### 6. Knowledge Base
**Location:** `knowledge_base/` directory

**Purpose:** Source of truth for Vena documentation

**Formats:** Markdown (`.md`), Text (`.txt`), PDF (`.pdf`)

**High-Level Summary:**
- Contains all Vena technical documentation
- Includes guides, troubleshooting info, API references
- Organised in folders by topic/category
- Updated by adding new documents and re-running ingestion

---

## Data Flow - Query Process

### Step-by-Step Query Flow

#### Step 1: User Input
**High-Level Summary:**
- User types a question in the frontend chat interface
- Frontend captures the input and prepares it for submission

#### Step 2: API Request
**High-Level Summary:**
- Frontend sends HTTP POST request to `/api/query` endpoint
- Request includes the user's question in JSON format
- Backend receives and validates the request

#### Step 3: Query Embedding
**High-Level Summary:**
- Backend converts the text question into a numerical vector (embedding)
- Uses OpenAI's `text-embedding-3-small` model
- Embedding represents the semantic meaning of the question
- This allows matching questions to documents by meaning, not just keywords

#### Step 4: Vector Search
**High-Level Summary:**
- Embedding is sent to Qdrant vector database
- Qdrant performs similarity search across all stored document chunks
- Finds the top-k (default: 5) most semantically similar chunks
- Returns chunks ranked by relevance score

#### Step 5: Context Retrieval
**High-Level Summary:**
- Retrieved document chunks are extracted from Qdrant
- Each chunk includes its text content and metadata (source file name)
- Chunks are formatted into a structured context string
- Context is prepared for the LLM with clear source attribution

#### Step 6: Prompt Construction
**High-Level Summary:**
- System prompt is added (instructions for the AI assistant)
- User question and retrieved context are combined
- Full prompt includes: system instructions + context documents + user question
- Prompt is formatted according to GPT-4o's expected input structure

#### Step 7: LLM Generation
**High-Level Summary:**
- Complete prompt is sent to OpenAI GPT-4o model
- LLM generates a response based on the provided context
- Response is constrained to only use information from the context
- LLM includes source citations in its response

#### Step 8: Response Processing
**High-Level Summary:**
- Backend extracts the generated answer from LLM response
- Source document names are extracted from retrieved chunks
- Response is formatted into structured JSON
- Latency is calculated and included in response

#### Step 9: API Response
**High-Level Summary:**
- Backend returns JSON response with:
  - `answer`: The generated text response
  - `sources`: Array of source document names
  - `latency_ms`: Time taken to process the query
  - `model`: Model name used (gpt-4o)

#### Step 10: Frontend Display
**High-Level Summary:**
- Frontend receives the response
- Answer is rendered with markdown formatting
- Source citations are displayed as badges
- Message is added to conversation history
- User can continue the conversation

---

## Data Flow - Ingestion Process

### Step-by-Step Ingestion Flow

#### Step 1: Document Discovery
**High-Level Summary:**
- Ingestion script scans `knowledge_base/` directory
- Finds all supported file types (`.md`, `.txt`, `.pdf`)
- Recursively searches subdirectories
- Creates a list of all documents to process

#### Step 2: Document Loading
**High-Level Summary:**
- Each document is loaded using appropriate loader:
  - Markdown/Text: Direct text extraction
  - PDF: PDF parsing to extract text
- Documents are converted to LangChain `Document` objects
- Each document includes metadata (file path, file name)

#### Step 3: Text Chunking
**High-Level Summary:**
- Documents are split into smaller chunks (500 tokens each)
- Chunks overlap by 50 tokens to preserve context
- Uses `RecursiveCharacterTextSplitter` for intelligent splitting
- Preserves document structure (respects paragraphs, code blocks)
- Each chunk becomes a separate searchable unit

#### Step 4: Embedding Generation
**High-Level Summary:**
- Each chunk is converted to an embedding vector
- Uses OpenAI's `text-embedding-3-small` model
- Embedding is a 1536-dimensional numerical vector
- Embeddings capture semantic meaning of the text
- Processed in batches for efficiency

#### Step 5: Metadata Enrichment
**High-Level Summary:**
- Each chunk is enriched with metadata:
  - Source file path
  - Source file name
  - Chunk index (position in document)
  - Timestamp
- Metadata helps with source citation later

#### Step 6: Vector Storage
**High-Level Summary:**
- Chunks, embeddings, and metadata are sent to Qdrant Cloud
- Stored in a collection (default: `vena_rag_bot`)
- Each chunk becomes a searchable vector point
- Collection is created if it doesn't exist
- Existing chunks can be updated or replaced

#### Step 7: Indexing Completion
**High-Level Summary:**
- Qdrant indexes all vectors for fast similarity search
- Collection is ready for querying
- Summary statistics are logged (total chunks, files processed)
- Ingestion process completes

---

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 15, React 19 | Modern web UI framework |
| **Styling** | Tailwind CSS 4.0 | Utility-first CSS framework |
| **Backend** | FastAPI | High-performance Python web framework |
| **Server** | Uvicorn | ASGI server for FastAPI |
| **RAG Framework** | LangChain 0.1.20 | RAG pipeline orchestration |
| **LLM** | OpenAI GPT-4o | Large language model for generation |
| **Embeddings** | OpenAI text-embedding-3-small | Text-to-vector conversion |
| **Vector DB** | Qdrant Cloud | Managed vector database |
| **Document Processing** | LangChain loaders, PyPDF | Document parsing and chunking |
| **Language** | Python 3.12+, TypeScript | Backend and frontend languages |

---

## Configuration Summary

### Environment Variables
- `OPENAI_API_KEY` - Authentication for OpenAI API
- `QDRANT_URL` - Qdrant Cloud cluster endpoint
- `QDRANT_API_KEY` - Qdrant authentication key
- `QDRANT_COLLECTION_NAME` - Vector collection name (default: `vena_rag_bot`)

### Key Settings
- **Chunk Size:** 500 tokens (balance between context and granularity)
- **Chunk Overlap:** 50 tokens (preserves context across boundaries)
- **Top-K Retrieval:** 5 documents (number of chunks retrieved per query)
- **Temperature:** 0.1 (low for consistent, factual responses)
- **Max Tokens:** 2000 (response length limit)

---

## Key Features

### 1. Semantic Search
**High-Level Summary:**
- Finds relevant documents by meaning, not just keyword matching
- Understands synonyms, context, and intent
- More accurate than traditional keyword search

### 2. Source Citations
**High-Level Summary:**
- Every answer includes source document references
- Users can verify information and explore further
- Builds trust and transparency

### 3. Conversation History
**High-Level Summary:**
- Maintains context across multiple questions
- Stores conversations in browser localStorage
- Allows users to revisit previous interactions

### 4. Markdown Support
**High-Level Summary:**
- Renders formatted text (bold, italic, lists, links)
- Syntax highlighting for code blocks
- Professional presentation of technical content

### 5. Error Handling
**High-Level Summary:**
- Graceful error messages for users
- Detailed logging for debugging
- Fallback behaviours when services are unavailable

### 6. Performance Monitoring
**High-Level Summary:**
- Tracks query latency
- Logs processing times
- Helps identify bottlenecks

---

## Deployment Architecture

### Frontend Deployment
**High-Level Summary:**
- Can be deployed to Vercel, Netlify, or any static hosting
- Builds to static files (with Next.js SSR if needed)
- Connects to backend API via environment variable

### Backend Deployment
**High-Level Summary:**
- Deployed as FastAPI application on Railway, Render, Heroku, or similar
- Runs Uvicorn ASGI server
- Requires Python 3.12+ runtime
- Needs access to OpenAI API and Qdrant Cloud

### Vector Database
**High-Level Summary:**
- Qdrant Cloud (managed service)
- No local deployment needed
- Scales automatically
- Accessible via API from anywhere

### Knowledge Base
**High-Level Summary:**
- Stored in repository or cloud storage
- Updated by committing new documents
- Re-ingestion required after updates

---

## Scalability Considerations

### Current Architecture
- **Stateless Backend:** Each request is independent
- **Cloud Vector DB:** Qdrant Cloud handles scaling
- **Stateless Frontend:** Can be cached and CDN-distributed
- **API Rate Limits:** OpenAI API has rate limits to consider

### Future Enhancements
- Caching layer (Redis) for common queries
- Database (PostgreSQL) for conversation persistence
- Multiple backend instances with load balancing
- Streaming responses for better UX
- Batch processing for ingestion

---

## Security Considerations

### API Keys
- Stored in environment variables (never in code)
- Backend validates keys on startup
- Frontend never sees backend API keys

### CORS
- Currently allows all origins (development)
- Should be restricted to frontend domain in production

### Data Privacy
- Queries sent to OpenAI (check their privacy policy)
- Documents stored in Qdrant Cloud (check their security)
- No user authentication currently (add if needed)

---

## Maintenance

### Regular Tasks
1. **Update Knowledge Base:** Add new documents as needed
2. **Re-run Ingestion:** After knowledge base updates
3. **Monitor Performance:** Check latency and error rates
4. **Update Dependencies:** Keep packages current
5. **Review Logs:** Check for errors or issues

### Troubleshooting
- Check backend logs for API errors
- Verify Qdrant connection and collection exists
- Ensure OpenAI API key is valid and has credits
- Check frontend console for API call errors

---

## Next Steps & Improvements

### Priority Improvements (Quick Wins)

#### 1. Implement Redis Caching (High Impact, 2 hours)
**Current Status:** Redis is configured but not implemented

**What to Add:**
- Query response caching to avoid redundant OpenAI API calls
- Cache common queries for 24 hours (configurable TTL)
- Cache key based on query text hash
- Cache invalidation on knowledge base updates

**Benefits:**
- Faster response times for repeated queries
- Reduced OpenAI API costs
- Better user experience

**Implementation:**
- Create `backend/src/services/cache.py`
- Integrate with RAG pipeline in `backend/src/core/rag.py`
- Add cache hit/miss logging

---

#### 2. Upgrade LangChain Version (Medium Impact, 2 hours)
**Current Status:** Using LangChain 0.1.20 (outdated)

**What to Upgrade:**
- Upgrade to LangChain 0.3+ or latest stable version
- Update imports and API calls
- Test compatibility with existing code

**Benefits:**
- Access to newer features and improvements
- Better security patches
- Improved performance
- Better documentation and community support

**Risks:**
- May require code changes due to API differences
- Test thoroughly before deploying

---

#### 3. Add Streaming Responses (High Impact, 3 hours)
**Current Status:** Responses are returned all at once

**What to Add:**
- Server-Sent Events (SSE) or WebSocket support
- Stream LLM responses token-by-token
- Update frontend to handle streaming
- Show partial responses as they arrive

**Benefits:**
- Better perceived performance (users see responses immediately)
- More engaging user experience
- Industry standard for chat applications

**Implementation:**
- Add streaming endpoint in FastAPI
- Update frontend Chat component
- Handle streaming in React

---

#### 4. Optimise Render Performance (Medium Impact, 1 hour)
**Current Status:** Using Render free tier with cold starts

**Options:**
- **Option A:** Upgrade to Render Starter plan (£7/month) - Eliminates cold starts
- **Option B:** Set up keep-alive ping service (free) - Reduces cold starts
- **Option C:** Keep as-is if cold starts aren't a problem

**Benefits:**
- Faster first request after inactivity
- Better user experience
- More reliable service

---

### Medium Priority Improvements

#### 5. Implement PostgreSQL Database (Medium Impact, 3-4 hours)
**Current Status:** PostgreSQL is configured but not used

**What to Add:**
- Conversation persistence (store chat history in database)
- Query logging and analytics
- User session management
- Usage statistics and insights

**Benefits:**
- Persistent conversation history across devices
- Analytics on query patterns
- Better debugging and monitoring
- User management capabilities

**Implementation:**
- Set up database models (SQLAlchemy)
- Create migration scripts (Alembic)
- Add conversation storage endpoints
- Build analytics dashboard

---

#### 6. Add Hybrid Search (Medium Impact, 4-5 hours)
**Current Status:** Only semantic search (vector similarity)

**What to Add:**
- Combine semantic search with keyword/BM25 search
- Re-ranking of results (e.g., Cohere Rerank)
- Better handling of exact matches and synonyms

**Benefits:**
- More accurate search results
- Better handling of technical terms
- Improved relevance ranking

**Implementation:**
- Add keyword search capability
- Implement hybrid search algorithm
- Integrate re-ranking service

---

#### 7. Add Monitoring & Observability (Medium Impact, 2-3 hours)
**Current Status:** Basic logging only

**What to Add:**
- Error tracking (Sentry or similar)
- Performance monitoring (APM)
- Query analytics dashboard
- Alerting for errors or slow responses

**Benefits:**
- Better debugging capabilities
- Proactive issue detection
- Performance insights
- User behaviour analytics

---

### Advanced Improvements (Future Enhancements)

#### 8. Add Rate Limiting
- Prevent API abuse
- Fair usage policies
- Per-user rate limits

#### 9. Implement A/B Testing for Prompts
- Test different prompt variations
- Measure response quality
- Optimise system prompts

#### 10. Add Query Deduplication
- Detect similar queries
- Reuse previous responses
- Reduce redundant processing

#### 11. Batch Embedding Generation
- Process multiple queries together
- More efficient API usage
- Lower costs

#### 12. Connection Pooling
- Optimise database connections
- Better resource management
- Improved performance

#### 13. Add Authentication & Authorization
- User authentication
- Role-based access control
- API key management

#### 14. Implement File Watcher for Auto-Ingestion
- Monitor knowledge base directory
- Automatically ingest new documents
- Real-time updates

---

## Improvement Priority Matrix

| Priority | Improvement | Impact | Effort | Value |
|----------|------------|--------|--------|-----|
| **P0** | Redis Caching | High | Low (2h) | High |
| **P0** | Streaming Responses | High | Medium (3h) | High |
| **P1** | Upgrade LangChain | Medium | Low (2h) | Medium |
| **P1** | Render Optimisation | Medium | Low (1h) | Medium |
| **P2** | PostgreSQL Database | High | Medium (4h) | Medium |
| **P2** | Hybrid Search | Medium | High (5h) | Medium |
| **P2** | Monitoring | Medium | Medium (3h) | Medium |
| **P3** | Rate Limiting | Low | Low (2h) | Low |
| **P3** | A/B Testing | Low | High (4h) | Low |
| **P3** | Auto-Ingestion | Low | Medium (3h) | Low |

---

## Recommended Implementation Order

### Phase 1: Quick Wins (1 week)
1. Redis Caching
2. Streaming Responses
3. Upgrade LangChain
4. Render Optimisation

### Phase 2: Core Features (2-3 weeks)
5. PostgreSQL Database
6. Monitoring & Observability

### Phase 3: Advanced Features (1-2 months)
7. Hybrid Search
8. Rate Limiting
9. Auto-Ingestion

### Phase 4: Optimisation (Ongoing)
10. A/B Testing
11. Query Deduplication
12. Batch Processing
13. Connection Pooling

---

## Cost Considerations

### Current Monthly Costs (Estimated)
- **Vercel:** Free tier (or £20/month for Pro)
- **Render:** Free tier (or £7/month Starter to eliminate cold starts)
- **Qdrant Cloud:** Free tier (or ~£25/month for production)
- **OpenAI:** Pay-as-you-go (~£10-50/month depending on usage)
- **Total:** ~£15-100/month

### With Improvements
- **Redis:** Free (Railway) or ~£5/month (managed)
- **PostgreSQL:** Free (Railway) or ~£5/month (managed)
- **Monitoring:** Free tier (Sentry) or ~£10/month
- **Total:** ~£30-120/month

---

## Success Metrics

Track these metrics to measure improvement success:

1. **Performance:**
   - Average response time (target: < 3 seconds)
   - Cold start time (target: < 2 seconds with paid tier)
   - Cache hit rate (target: > 30%)

2. **Cost:**
   - OpenAI API costs per query
   - Total monthly infrastructure costs
   - Cost per user query

3. **User Experience:**
   - Time to first token (streaming)
   - User satisfaction scores
   - Query success rate

4. **Reliability:**
   - Uptime percentage (target: > 99.5%)
   - Error rate (target: < 1%)
   - Average queries per day

---

This architecture provides a robust, scalable foundation for a production RAG system with clear separation of concerns and well-defined data flows. The improvements outlined above will enhance performance, reliability, and user experience as the system scales.
