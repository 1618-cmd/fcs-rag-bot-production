# Quick Reference Guide

Quick access to key information for the production project.

---

## Project Details

- **Project Name**: Vena RAG Bot - Production
- **Jira Project Key**: FRBP
- **Status**: Phase 1 Development
- **Location**: `C:\Users\Miles\Desktop\Projects\Vena\Vena RAG Bot Production`

---

## Key Decisions Summary

### Technology Stack
- **LLM**: OpenAI GPT-4o ✅
- **Embeddings**: OpenAI text-embedding-3-small ✅
- **Vector DB**: ChromaDB (dev) → Pinecone (prod)
- **Backend**: FastAPI ✅
- **Frontend**: Streamlit (Phase 1) → React (Phase 2)
- **Database**: PostgreSQL
- **Cache**: Redis
- **Hosting**: Railway (recommended)

### Architecture
- **RAG Pipeline**: Semantic search + LLM synthesis
- **Chunking**: 500 tokens, 50 overlap
- **Retrieval**: Top 3-5 documents
- **Response**: Always include citations

---

## Phase 1 Requirements (Months 1-2)

### Must-Have Features
1. Knowledge Query & Response (UR-001)
2. VenaQL Code Explanation (UR-002)
3. Simple Code Generation (UR-003)
4. Web Interface (UR-006)
5. Basic Analytics (FR-007)

### Success Criteria
- 85% accuracy on Q&A
- 90% syntax validity
- < 3 seconds response time
- > 4.0/5.0 satisfaction

---

## Important Files

### Documentation
- `PROJECT_CONTEXT.md` - **READ THIS FIRST** - All context and decisions
- `MIGRATION_GUIDE.md` - How to migrate from POC
- `README.md` - Quick start guide
- `QUICK_REFERENCE.md` - This file

### Source Code
- `src/config.py` - Configuration
- `src/ingestion.py` - Document ingestion
- `src/retrieval.py` - RAG pipeline
- `src/app.py` - Streamlit UI (POC)

### Configuration
- `.env.example` - Environment variables template
- `requirements.txt` - Python dependencies

---

## Common Tasks

### Set Up Development Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your keys
```

### Ingest Knowledge Base
```bash
python -m src.ingestion
```

### Run Streamlit UI
```bash
streamlit run src/app.py
```

### Run FastAPI Backend
```bash
uvicorn src.api.main:app --reload
```

---

## Jira Queries

### All Work Items
```jql
project = "FRBP"
```

### TO DO Items
```jql
project = "FRBP" AND status = "TO DO"
```

### IN PROGRESS
```jql
project = "FRBP" AND status = "IN PROGRESS"
```

### Unassigned
```jql
project = "FRBP" AND assignee is EMPTY
```

---

## Team Contacts

- **ML Engineer**: Miles Waite
- **Vena SME**: Martin Bruwer
- **Jira**: FRBP project

---

## Budget Summary

- **Development**: £68,000 - £106,000
- **Annual Operating**: £6,600 - £30,500

---

## Compliance Checklist

- [ ] GDPR DPIA completed
- [ ] Data Processing Agreements signed
- [ ] Audit logging configured
- [ ] Security review completed
- [ ] Data retention policies set

---

## Next Steps

1. ✅ Review PROJECT_CONTEXT.md
2. ✅ Set up development environment
3. ⏳ Migrate code from POC
4. ⏳ Set up infrastructure
5. ⏳ Begin Phase 1 development

---

*For detailed information, see PROJECT_CONTEXT.md*

