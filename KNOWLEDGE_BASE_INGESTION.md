# Knowledge Base Ingestion - When & How

## 🎯 When to Ingest the Knowledge Base

### Option 1: Early (For Local Development) ✅ Recommended
**When**: After Step 2 (Environment Config) + Qdrant Cloud Setup

**Why**: 
- Test the RAG pipeline locally before building the API
- Verify ingestion works with Qdrant
- Catch any issues early
- Can test queries via Python scripts

**Prerequisites:**
- ✅ Step 2 complete (`.env` configured)
- ✅ Qdrant Cloud account created
- ✅ Qdrant collection created (or will be auto-created)
- ✅ Knowledge base documents ready in `knowledge_base/` folder

**Timeline**: After Step 2, before Step 3 (FastAPI)

---

### Option 2: After Backend Setup (For Integration Testing)
**When**: After Step 3 (FastAPI Backend) is complete

**Why**:
- Test the full stack: ingestion → API → queries
- Verify everything works together
- Can test via API endpoints

**Prerequisites:**
- ✅ Steps 2-3 complete
- ✅ FastAPI backend running
- ✅ Qdrant Cloud configured

**Timeline**: After Step 3, before Step 7 (Local Testing)

---

### Option 3: After Deployment (For Production)
**When**: After Step 9 (Deployment) - Production environment

**Why**:
- Production data separate from dev
- Can test in production environment
- Final verification before going live

**Prerequisites:**
- ✅ All steps complete
- ✅ Production environment deployed
- ✅ Production Qdrant collection ready

**Timeline**: Final step in Step 9 (Deployment)

---

## 📋 Recommended Approach

### For Development: **Option 1 (Early)**
Ingest early so you can:
1. Test ingestion code works
2. Verify Qdrant integration
3. Test RAG queries locally
4. Catch issues before building API

### For Production: **Option 3 (After Deployment)**
Ingest in production after:
1. Everything is deployed
2. Production Qdrant is ready
3. You're ready to go live

---

## 🔄 Typical Workflow

### Development Phase
```
Step 2: Environment Config
  ↓
[INGEST KNOWLEDGE BASE HERE] ← Early ingestion
  ↓
Step 3: FastAPI Backend
  ↓
Step 4-6: Services & Frontend
  ↓
Step 7: Local Testing (knowledge base already ingested)
```

### Production Phase
```
Step 8: Infrastructure Setup
  ↓
Step 9: Deployment
  ↓
[INGEST KNOWLEDGE BASE HERE] ← Production ingestion
  ↓
Test production system
  ↓
Go live!
```

---

## 📝 How to Ingest

### Method 1: Command Line (Recommended)
```bash
# From project root
cd backend
python -m src.core.ingestion
```

### Method 2: Python Script
```python
from backend.src.core.ingestion import ingest_knowledge_base

# Ingest to default collection
vector_store = ingest_knowledge_base()

# Or specify collection name
vector_store = ingest_knowledge_base(collection_name="vena_rag_bot_prod")
```

### Method 3: Via API (After backend is built)
```bash
POST /api/admin/ingest
```

---

## ⚠️ Important Notes

### 1. Separate Collections for Dev/Prod
- **Development**: Use collection name like `vena_rag_bot_dev`
- **Production**: Use collection name like `vena_rag_bot_prod`
- Set via `QDRANT_COLLECTION_NAME` in `.env`

### 2. Re-ingestion
- If you update documents, you need to re-ingest
- Old chunks remain in Qdrant (consider clearing collection first)
- Or use versioned collections (`vena_rag_bot_v1`, `vena_rag_bot_v2`)

### 3. Knowledge Base Location
- Documents should be in: `knowledge_base/` (project root)
- Supports: `.md` and `.txt` files
- Recursive: Loads from subdirectories

### 4. First-Time Setup
Before first ingestion:
1. Add documents to `knowledge_base/` folder
2. Organize in subfolders (optional):
   - `knowledge_base/issue_resolutions/`
   - `knowledge_base/patterns/`
   - `knowledge_base/concepts/`
   - `knowledge_base/troubleshooting/`

---

## ✅ Checklist Before Ingesting

- [ ] `.env` file configured with Qdrant credentials
- [ ] Qdrant Cloud account created
- [ ] `QDRANT_URL` set in `.env`
- [ ] `QDRANT_API_KEY` set in `.env`
- [ ] `QDRANT_COLLECTION_NAME` set (or will use default)
- [ ] Documents added to `knowledge_base/` folder
- [ ] Python dependencies installed (`pip install -r backend/requirements.txt`)
- [ ] Virtual environment activated

---

## 🚀 Quick Start (After Step 2)

Once you have your `.env` configured:

```bash
# 1. Navigate to backend
cd backend

# 2. Activate virtual environment (if using one)
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies (if not already done)
pip install -r requirements.txt

# 4. Run ingestion
python -m src.core.ingestion
```

You should see:
```
🚀 Vena RAG Bot - Knowledge Base Ingestion
==================================================
📂 Loading documents from: ...
   Found X documents
✂️  Chunking documents...
   Created Y chunks
🔢 Generating embeddings and storing in Qdrant...
✅ Vector store created/updated in Qdrant collection: vena_rag_bot
==================================================
✅ Ingestion complete!
   Documents: X
   Chunks: Y
==================================================
```

---

## 🔍 Verify Ingestion Worked

### Check Qdrant Dashboard
1. Log into Qdrant Cloud
2. Check your collection
3. Verify document count matches chunks created

### Test Query (After RAG pipeline is set up)
```python
from backend.src.core.rag import get_rag_pipeline

pipeline = get_rag_pipeline()
response, docs = pipeline.query("What is Vena?")
print(response)
print(f"Sources: {pipeline.get_sources(docs)}")
```

---

## 📊 Expected Results

For a typical knowledge base:
- **10-15 documents** (POC size): ~50-100 chunks
- **50-100 documents** (Phase 1 target): ~500-1000 chunks
- **Ingestion time**: ~1-5 minutes depending on size
- **Cost**: Minimal (Qdrant free tier covers small collections)

---

## ❓ FAQ

**Q: Can I ingest multiple times?**  
A: Yes, but it will add duplicate chunks. Consider clearing the collection first or using versioned collections.

**Q: What if ingestion fails?**  
A: Check:
- Qdrant credentials are correct
- Documents exist in `knowledge_base/`
- Network connection to Qdrant
- OpenAI API key is valid

**Q: How do I update the knowledge base?**  
A: Re-run ingestion. Consider clearing the collection first or using a new collection name.

**Q: Can I ingest from different sources?**  
A: Yes, modify `ingestion.py` to load from different paths or add new loaders.

---

*Recommendation: Ingest early (after Step 2) for local development, then re-ingest in production after deployment.*

