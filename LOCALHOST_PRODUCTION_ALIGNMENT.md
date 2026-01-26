# Localhost vs Production Alignment Checklist

## Critical Settings That MUST Match

### ✅ Verified Settings (Current Localhost)
- **QDRANT_COLLECTION_NAME**: `fcs-rag-bot-prod` ✅
- **TOP_K_RESULTS**: `20` ✅
- **TEMPERATURE**: `0.1` ✅
- **MAX_TOKENS**: `2000` ✅
- **OPENAI_MODEL**: `gpt-4o` ✅
- **EMBEDDING_MODEL**: `text-embedding-3-small` ✅
- **LLM_PROVIDER**: `openai` ✅

### ⚠️ Environment-Specific (Should Differ)
- **ENVIRONMENT**: 
  - Localhost: `development` ✅
  - Production: `production` ✅
- **DEBUG**: 
  - Localhost: `true` (optional)
  - Production: `false` ✅
- **LOG_LEVEL**: 
  - Localhost: `DEBUG` (optional)
  - Production: `INFO` ✅

## Code Differences to Verify

### 1. Query Expansion
- **Status**: Implemented in `backend/src/core/rag.py`
- **Method**: `_expand_query()` (async)
- **Usage**: Called in `retrieve()` method
- **Action**: Verify both environments use query expansion

### 2. Prompt Template
- **File**: `backend/src/core/rag.py` (SYSTEM_PROMPT)
- **Status**: Single source of truth ✅
- **Action**: No changes needed

### 3. CORS Configuration
- **File**: `backend/src/api/main.py`
- **Logic**: Adds localhost origins if `ENVIRONMENT=development` or `DEBUG=true`
- **Action**: Verify production doesn't include localhost origins

## Production Environment Variables Checklist

Ensure production has these set:

```env
# Critical - Must Match Localhost
QDRANT_COLLECTION_NAME=fcs-rag-bot-prod
TOP_K_RESULTS=20
TEMPERATURE=0.1
MAX_TOKENS=2000
OPENAI_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small
LLM_PROVIDER=openai

# Environment-Specific (Different from Localhost)
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
```

## Verification Steps

1. ✅ Check localhost config (done)
2. ⏳ Verify production config matches
3. ⏳ Test same query on both environments
4. ⏳ Compare response structure and quality
5. ⏳ Verify query expansion is working in both

## Known Differences (Expected)

1. **CORS Origins**: Production only allows `https://www.fcs-alex.com`, localhost allows both
2. **Logging**: Production uses INFO level, localhost can use DEBUG
3. **Database/Redis**: Production uses Railway services, localhost uses local services

## Action Items

- [x] Fixed default QDRANT_COLLECTION_NAME in config.py to match template
- [x] Created verification script: `scripts/verify_localhost_production_alignment.py`
- [ ] Verify production `.env` has all critical settings matching
- [ ] Test query expansion in both environments
- [ ] Run same test query on both and compare responses
- [ ] Document any remaining differences

## How to Verify Alignment

Run the verification script:
```bash
python scripts/verify_localhost_production_alignment.py
```

This will check:
- ✅ QDRANT_COLLECTION_NAME matches
- ✅ TOP_K_RESULTS matches
- ✅ TEMPERATURE matches
- ✅ MAX_TOKENS matches
- ✅ Model names match
- ✅ LLM provider matches
