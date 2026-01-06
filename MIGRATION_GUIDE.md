# Migration Guide: POC → Production

This guide helps you migrate code, knowledge base, and infrastructure from the POC to the production system.

---

## Overview

**POC Location**: `C:\Users\Miles\Desktop\Projects\Vena\RAG Bot POC`  
**Production Location**: `C:\Users\Miles\Desktop\Projects\Vena\Vena RAG Bot Production`

---

## Step 1: Code Migration

### Copy Core Files

Copy these files from POC to Production:

```bash
# From POC directory
src/config.py          → Production/src/config.py
src/ingestion.py       → Production/src/ingestion.py
src/retrieval.py       → Production/src/retrieval.py
src/app.py             → Production/src/app.py (keep for reference)
requirements.txt       → Production/requirements.txt
.env.example          → Production/.env.example
```

### Refactor for Production

1. **Update config.py**
   - Add production database settings
   - Add Redis cache configuration
   - Add monitoring configuration
   - Add environment-specific settings

2. **Create FastAPI Backend**
   - Create `src/api/main.py` for FastAPI app
   - Create `src/api/routes/` for API endpoints
   - Move RAG logic to `src/core/rag.py`
   - Add authentication middleware

3. **Add Error Handling**
   - Add proper exception handling
   - Add logging (structured logging)
   - Add retry logic for API calls

---

## Step 2: Knowledge Base Migration

### Copy Knowledge Base

```bash
# Copy entire knowledge_base directory
knowledge_base/ → Production/knowledge_base/
```

### Expand Knowledge Base

POC had 10-15 documents. Phase 1 target is 50-100 documents:

- [ ] Document 20 historical issue resolutions
- [ ] Extract 25 code patterns
- [ ] Create 10 reference guides
- [ ] Compile Vena constraint reference
- [ ] Build schema dictionary (50 tables/slices)

### Re-ingest Documents

```bash
# In production environment
python -m src.ingestion
```

---

## Step 3: Infrastructure Setup

### Vector Database Migration

**From**: ChromaDB (local)  
**To**: Pinecone or Weaviate (managed)

1. **Set up Pinecone/Weaviate account**
2. **Update config.py** with new vector DB settings
3. **Update ingestion.py** to use new vector DB
4. **Re-ingest documents** to new vector DB
5. **Test retrieval** works correctly

### Database Setup

1. **Set up PostgreSQL** (Supabase or Railway)
2. **Create schema** for:
   - User accounts
   - Query logs
   - Feedback
   - Analytics
3. **Add database models** in `src/models/`
4. **Set up migrations** (Alembic)

### Cache Setup

1. **Set up Redis** (Railway or managed service)
2. **Add caching layer** for:
   - Common queries
   - Embeddings
   - API responses
3. **Update retrieval.py** to use cache

### Hosting Setup

1. **Choose hosting** (Railway recommended)
2. **Set up environment variables**
3. **Configure deployment pipeline**
4. **Set up monitoring** (Sentry, PostHog)

---

## Step 4: Testing

### Unit Tests

```bash
# Create test structure
tests/
├── unit/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_validation.py
└── integration/
    └── test_rag_pipeline.py
```

### Test Migration

1. **Run POC tests** to establish baseline
2. **Run production tests** to verify migration
3. **Compare results** - should be identical

---

## Step 5: Configuration

### Environment Variables

Update `.env` with production values:

```env
# OpenAI
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database (Pinecone)
PINECONE_API_KEY=your-key-here
PINECONE_ENVIRONMENT=us-east-1
PINECONE_INDEX=vena-rag-bot

# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# Redis
REDIS_URL=redis://host:6379

# Monitoring
SENTRY_DSN=your-sentry-dsn
POSTHOG_KEY=your-posthog-key
```

---

## Step 6: Deployment

### Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Knowledge base ingested
- [ ] Database schema created
- [ ] Monitoring set up
- [ ] Security review completed

### Deploy

1. **Deploy backend** to hosting platform
2. **Deploy frontend** (if separate)
3. **Run database migrations**
4. **Verify health checks**
5. **Test end-to-end**

---

## Rollback Plan

If issues occur:

1. **Keep POC running** as backup
2. **Database rollback** - restore from backup
3. **Code rollback** - revert to previous version
4. **Vector DB** - can re-ingest from knowledge base

---

## Validation

After migration, verify:

- [ ] All POC queries return same results
- [ ] Response times acceptable (< 3 seconds)
- [ ] Error handling works
- [ ] Monitoring captures metrics
- [ ] Knowledge base search works
- [ ] Code generation works

---

## Next Steps

1. Complete code migration
2. Set up infrastructure
3. Migrate knowledge base
4. Run tests
5. Deploy to staging
6. User acceptance testing
7. Deploy to production

---

*For questions, refer to PROJECT_CONTEXT.md or contact the team.*

