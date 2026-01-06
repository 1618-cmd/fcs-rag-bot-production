# Backend - FastAPI Application

FastAPI backend for the Vena RAG Bot Production.

## 🚀 Quick Start

### 1. Set Up Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your API keys and configuration
# See ENV_SETUP.md for detailed instructions
```

### 2. Install Dependencies

```bash
# Create virtual environment (if not already created)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Verify Configuration

```bash
# Test that your .env is configured correctly
python -m src.utils.config
```

### 4. Ingest Knowledge Base (First Time)

```bash
# Make sure you have documents in knowledge_base/ folder
# Then run ingestion
python -m src.core.ingestion
```

### 5. Run FastAPI Server (After Step 3)

```bash
# Start the server
uvicorn src.api.main:app --reload

# Server will be available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

---

## 📁 Project Structure

```
backend/
├── src/
│   ├── api/              # FastAPI routes (to be created)
│   ├── core/             # Core RAG logic
│   │   ├── rag.py        # RAG pipeline
│   │   └── ingestion.py  # Document ingestion
│   ├── services/         # Business logic (to be created)
│   ├── models/           # Data models (to be created)
│   └── utils/            # Utilities
│       ├── config.py     # Configuration
│       └── logging_config.py  # Logging setup
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
├── .env.example          # Environment template
└── README.md             # This file
```

---

## 🔧 Configuration

See [ENV_SETUP.md](ENV_SETUP.md) for detailed environment setup instructions.

Required environment variables:
- `OPENAI_API_KEY` - OpenAI API key
- `QDRANT_URL` - Qdrant Cloud cluster URL
- `QDRANT_API_KEY` - Qdrant Cloud API key
- `QDRANT_COLLECTION_NAME` - Collection name (default: `vena_rag_bot_dev`)

Optional (for production):
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string

---

## 📚 Usage

### Ingest Knowledge Base

```bash
python -m src.core.ingestion
```

This will:
1. Load documents from `knowledge_base/` folder
2. Chunk them into smaller pieces
3. Generate embeddings
4. Store in Qdrant Cloud

### Test RAG Pipeline

```python
from src.core.rag import get_rag_pipeline

pipeline = get_rag_pipeline()
response, docs = pipeline.query("What is Vena?")
print(response)
print(f"Sources: {pipeline.get_sources(docs)}")
```

---

## 🧪 Testing

```bash
# Run tests (when created)
pytest

# Run with coverage
pytest --cov=src
```

---

## 📝 Development

### Code Style
- Follow PEP 8
- Use type hints
- Add docstrings to functions/classes

### Logging
```python
from src.utils.logging_config import get_logger

logger = get_logger(__name__)
logger.info("Your log message")
```

---

## 🚢 Deployment

See deployment documentation in `infrastructure/` folder.

---

## 📖 Documentation

- [Environment Setup](ENV_SETUP.md) - Detailed .env configuration
- [Project Structure](../../PROJECT_STRUCTURE.md) - Full project structure
- [Next Steps](../../NEXT_STEPS.md) - Development roadmap

---

## ❓ Troubleshooting

### "Configuration validation failed"
- Check `.env` file exists and has all required variables
- Run `python -m src.utils.config` to see specific errors

### "Vector store not initialized"
- Run ingestion: `python -m src.core.ingestion`
- Check Qdrant credentials in `.env`

### Import errors
- Make sure you're in the `backend/` directory
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`

---

## 📞 Support

For issues or questions, refer to:
- [PROJECT_CONTEXT.md](../../PROJECT_CONTEXT.md) - Full project context
- [QUICK_REFERENCE.md](../../QUICK_REFERENCE.md) - Quick reference guide
