# Environment Setup Guide

## Quick Start

1. **Copy the example file:**
   ```bash
   cd backend
   cp .env.example .env
   ```

2. **Fill in your values** in `.env` (see sections below)

3. **Verify configuration:**
   ```bash
   python -m src.utils.config
   ```

---

## 🔄 Reusing POC API Keys

If you have a working POC, you can reuse your existing API keys:

### ✅ Can Reuse from POC:
- **OpenAI API Key** - Same key works for production
- **OpenAI Model Settings** - Same models (`gpt-4o`, `text-embedding-3-small`)

### ❌ Cannot Reuse:
- **ChromaDB** - POC used local ChromaDB (no API key needed)
- **Qdrant** - Production uses Qdrant Cloud (needs new credentials)

### Quick Migration:
1. Copy `OPENAI_API_KEY` from your POC `.env` file
2. Paste into `backend/.env`
3. Set up new Qdrant Cloud account (see Qdrant section below)

---

## Required Variables

### 🔴 Critical (Must Have)

#### OpenAI API Key
- **Variable**: `OPENAI_API_KEY`
- **Where to get**: https://platform.openai.com/api-keys
- **Format**: `sk-...`
- **Required for**: LLM responses and embeddings

#### Qdrant Cloud
- **Variables**: `QDRANT_URL`, `QDRANT_API_KEY`
- **Where to get**: https://cloud.qdrant.io/
  1. Sign up / Log in
  2. Create a cluster
  3. Get cluster URL and API key
- **Format**: 
  - URL: `https://your-cluster-id.qdrant.io`
  - API Key: `your-api-key-here`
- **Required for**: Vector database (document storage)

---

### 🟡 Important (For Production)

#### PostgreSQL Database
- **Variable**: `DATABASE_URL`
- **Where to get**: 
  - **Railway**: Provided automatically when you create Postgres service
  - **Local**: `postgresql://postgres:password@localhost:5432/vena_rag_bot`
- **Format**: `postgresql://user:password@host:port/database`
- **Required for**: Query logging and analytics

#### Redis Cache
- **Variable**: `REDIS_URL`
- **Where to get**:
  - **Railway**: Provided automatically when you create Redis service
  - **Local**: `redis://localhost:6379`
- **Format**: `redis://host:port` or `redis://user:password@host:port`
- **Required for**: Response caching

---

### 🟢 Optional (Have Defaults)

- `OPENAI_MODEL` - Default: `gpt-4o`
- `EMBEDDING_MODEL` - Default: `text-embedding-3-small`
- `QDRANT_COLLECTION_NAME` - Default: `vena_rag_bot_dev`
- `ENVIRONMENT` - Default: `development`
- `DEBUG` - Default: `false`
- `LOG_LEVEL` - Default: `INFO`
- `CACHE_TTL` - Default: `86400` (24 hours)

---

## Setup by Environment

### Local Development

```env
# Minimal setup for local dev
OPENAI_API_KEY=sk-your-key-here
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-key-here
QDRANT_COLLECTION_NAME=vena_rag_bot_dev

# Optional for local testing
DATABASE_URL=postgresql://postgres:password@localhost:5432/vena_rag_bot
REDIS_URL=redis://localhost:6379

ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
```

### Production (Railway)

```env
# Railway provides these automatically via environment variables
OPENAI_API_KEY=sk-your-key-here
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-key-here
QDRANT_COLLECTION_NAME=vena_rag_bot_prod

# Railway automatically sets these:
# DATABASE_URL (from Postgres service)
# REDIS_URL (from Redis service)

ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
```

---

## Step-by-Step Setup

### 1. OpenAI API Key

**Option A: Reuse from POC** (Recommended if you have one)
1. Open your POC `.env` file
2. Copy the `OPENAI_API_KEY` value
3. Paste into `backend/.env` as `OPENAI_API_KEY`
4. Done! ✅

**Option B: Create New Key**
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Paste into `.env` as `OPENAI_API_KEY`

**Cost**: Pay-as-you-go. GPT-4o is ~$2.50-5.00 per 1M input tokens.

---

### 2. Qdrant Cloud Setup

1. **Sign up**: https://cloud.qdrant.io/
2. **Create cluster**:
   - Click "Create Cluster"
   - Choose region (London recommended for UK)
   - Select plan (Starter is fine for Phase 1)
   - Create cluster
3. **Get credentials**:
   - Cluster URL: `https://your-cluster-id.qdrant.io`
   - API Key: Click "API Keys" → Create new key
4. **Add to `.env`**:
   ```
   QDRANT_URL=https://your-cluster-id.qdrant.io
   QDRANT_API_KEY=your-api-key-here
   ```

**Cost**: ~£50/month for starter plan (covers Phase 1 needs)

---

### 3. PostgreSQL (For Production)

#### Option A: Railway (Recommended)
1. Sign up: https://railway.app/
2. Create new project
3. Add Postgres service
4. Railway provides `DATABASE_URL` automatically
5. Copy to `.env` (or Railway sets it automatically)

#### Option B: Local (For Testing)
1. Install PostgreSQL locally
2. Create database: `createdb vena_rag_bot`
3. Set in `.env`: `DATABASE_URL=postgresql://postgres:password@localhost:5432/vena_rag_bot`

**Cost**: Railway ~£5-10/month, Local = free

---

### 4. Redis (For Caching)

#### Option A: Railway (Recommended)
1. In Railway project, add Redis service
2. Railway provides `REDIS_URL` automatically
3. Copy to `.env` (or Railway sets it automatically)

#### Option B: Local (For Testing)
1. Install Redis locally
2. Start Redis: `redis-server`
3. Set in `.env`: `REDIS_URL=redis://localhost:6379`

**Cost**: Railway included in plan, Local = free

---

## Verification

### Test Configuration

Run this to verify your setup:

```bash
cd backend
python -m src.utils.config
```

You should see:
```
✅ Configuration validated successfully!
   Environment: development
   Model: gpt-4o
   Embeddings: text-embedding-3-small
   Knowledge Base: C:\...\knowledge_base
   Qdrant: https://your-cluster.qdrant.io
   Database: Configured
   Redis: Configured
```

### Common Issues

**"OPENAI_API_KEY not configured"**
- Check the key starts with `sk-`
- Make sure there are no extra spaces
- Verify the key is active in OpenAI dashboard

**"QDRANT_URL not configured"**
- Check URL format: `https://cluster-id.qdrant.io`
- No trailing slash
- Verify cluster is active in Qdrant dashboard

**"DATABASE_URL not configured"**
- For development: Can be skipped (not required for local testing)
- For production: Must be set
- Check format: `postgresql://user:pass@host:port/db`

---

## Security Notes

1. **Never commit `.env`** - It's in `.gitignore`
2. **Use different keys for dev/prod** - Separate Qdrant collections
3. **Rotate keys regularly** - Especially API keys
4. **Use Railway secrets** - For production, use Railway's environment variables instead of `.env`

---

## Next Steps

Once `.env` is configured:

1. ✅ Verify: `python -m src.utils.config`
2. 📚 Ingest knowledge base: `python -m src.core.ingestion`
3. 🚀 Start building FastAPI backend (Step 3)

---

## Cost Summary

| Service | Cost (Monthly) |
|---------|----------------|
| OpenAI (usage) | ~£10-20 |
| Qdrant Cloud | ~£50 |
| Railway (Backend + Postgres + Redis) | ~£10-20 |
| **Total** | **~£70-90/month** |

*Note: Actual costs depend on usage. OpenAI is pay-as-you-go.*

