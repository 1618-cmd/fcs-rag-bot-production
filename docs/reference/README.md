# POC Code Reference

This directory contains the original POC code for reference.

## Files

- `config.py` - Original POC configuration (ChromaDB-based)
- `ingestion.py` - Original POC ingestion (ChromaDB)
- `retrieval.py` - Original POC RAG pipeline (ChromaDB)
- `app.py` - Original Streamlit UI (for reference only)

## Note

This code has been refactored and moved to the production structure:
- `config.py` → `backend/src/utils/config.py` (updated for Qdrant, Postgres, Redis)
- `ingestion.py` → `backend/src/core/ingestion.py` (updated for Qdrant)
- `retrieval.py` → `backend/src/core/rag.py` (updated for Qdrant)
- `app.py` → Will be replaced by FastAPI backend + Next.js frontend

Do not use this code directly - use the production code in `backend/src/`.

