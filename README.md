# Vena RAG Bot - Production System

**Status:** Phase 1 Development  
**Based on:** Successful POC (December 2024 - January 2026)  
**Project Key:** FRBP (Jira)

---

## 🎯 Project Overview

Production implementation of the Vena RAG-Based Technical Support System. This system provides AI-powered technical support for contractors working on the Vena financial consolidation platform.

### Key Features (Phase 1)
- ✅ Knowledge Query and Response with source citations
- ✅ VenaQL Code Explanation
- ✅ Simple VenaQL Code Generation
- ✅ Web-based chat interface
- ✅ Basic usage analytics

---

## 📋 Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API key
- PostgreSQL database (for production)
- Vector database (Pinecone/Weaviate for production)

### Installation

```bash
# Clone or navigate to project
cd "Vena RAG Bot Production"

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Run Development Server

```bash
# Ingest knowledge base (first time)
python -m src.ingestion

# Run Streamlit interface (POC-style)
streamlit run src/app.py

# Or run FastAPI backend (production)
uvicorn src.api.main:app --reload
```

---

## 📁 Project Structure

```
Vena RAG Bot Production/
├── src/                    # Source code
│   ├── api/                # FastAPI routes (production)
│   ├── core/               # Core RAG logic
│   ├── services/           # Business logic
│   ├── models/             # Data models
│   ├── config.py           # Configuration
│   ├── ingestion.py        # Document ingestion
│   ├── retrieval.py        # RAG pipeline
│   └── app.py              # Streamlit UI (POC)
├── knowledge_base/         # Vena documentation
│   ├── issue_resolutions/
│   ├── patterns/
│   ├── concepts/
│   └── troubleshooting/
├── tests/                  # Test suite
├── docs/                   # Documentation
├── infrastructure/         # Deployment configs
├── PROJECT_CONTEXT.md      # Full project context
├── MIGRATION_GUIDE.md      # POC to Production guide
└── requirements.txt
```

---

## 🛠️ Tech Stack

- **LLM**: OpenAI GPT-4o
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector DB**: ChromaDB (dev) → Pinecone/Weaviate (prod)
- **Backend**: Python + FastAPI
- **Frontend**: Streamlit (Phase 1) → React (Phase 2)
- **Database**: PostgreSQL (Supabase/Railway)
- **Cache**: Redis
- **Monitoring**: Sentry, PostHog

---

## 📚 Documentation

- **[PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)** - Complete project context and decisions
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Guide to migrate from POC
- **[BRD_Complete.md](../RAG Bot POC/BRD_Complete.md)** - Business Requirements Document
- **[Production Architecture](../RAG Bot POC/Production_Architecture_Decision_Proposal.md)** - Architecture decisions

---

## 🚀 Development Workflow

1. **Review PROJECT_CONTEXT.md** - Understand all decisions made
2. **Set up environment** - Follow Quick Start above
3. **Migrate POC code** - See MIGRATION_GUIDE.md
4. **Set up infrastructure** - Database, vector DB, hosting
5. **Begin Phase 1 development** - Follow Jira project (FRBP)

---

## 📊 Success Criteria

### Phase 1 Targets
- 85% accuracy on knowledge Q&A
- 90% syntax validity on generated code
- Average response time < 3 seconds
- User satisfaction score > 4.0/5.0

---

## 👥 Team

- **ML Engineer**: Miles Waite
- **Vena SME**: Martin Bruwer
- **Project**: FRBP (Jira)

---

## 📝 License

Proprietary - Vena Solutions

---

*For complete project context, see [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)*

