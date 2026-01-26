# LLM Provider Compatibility - Component Review Checklist

**Date:** January 2026  
**Purpose:** Review and update components to fully support multi-provider LLM compatibility

---

## Components to Review

### ✅ Already Updated
- [x] **RAG Pipeline** (`backend/src/core/rag.py`) - Supports per-query provider selection
- [x] **Query Endpoint** (`backend/src/api/routes/query.py`) - Accepts `llm_provider` parameter
- [x] **LLM Provider Service** (`backend/src/services/llm_provider.py`) - Compatibility layer implemented
- [x] **Configuration** (`backend/src/utils/config.py`) - Provider settings added
- [x] **Frontend API Client** (`frontend/lib/api.ts`) - Provider parameter added
- [x] **Frontend UI** (`frontend/components/Chat.tsx`) - Model selector added

---

## ⚠️ Components Needing Review/Update

### 1. **Cache Keys** (Priority: High)
**Location:** `backend/src/api/routes/query.py` (lines 204-207)

**Issue:** Cache keys don't include provider, which could cause:
- GPT-4o response cached, then returned for Claude query (wrong model)
- Claude response cached, then returned for GPT-4o query (wrong model)

**Current Code:**
```python
cache_key = question
if calc_script:
    cache_key = f"{calc_script.strip()}\n\n{question}"
```

**Recommended Fix:**
```python
# Include provider in cache key to avoid cross-provider cache hits
cache_key = f"{llm_provider or settings.llm_provider}:{question}"
if calc_script:
    cache_key = f"{llm_provider or settings.llm_provider}:{calc_script.strip()}\n\n{question}"
```

**Impact:** Prevents incorrect cached responses from different providers

---

### 2. **Query Logging** (Priority: Medium)
**Location:** `backend/src/services/query_logger.py`

**Issue:** Query logs don't track which provider/model was used, making analytics incomplete.

**Current:** No provider/model tracking in logs

**Recommended Fix:**
- Add `llm_provider` parameter to `log_query_async()`
- Add `model_name` parameter to `log_query_async()`
- Update `QueryLog` database model to include these fields (if not already present)
- Pass provider/model from query endpoint to logger

**Impact:** Better analytics, cost tracking per provider, performance comparison

---

### 3. **Error Handling** (Priority: Low)
**Location:** `backend/src/services/llm_provider.py`, `backend/src/core/rag.py`

**Issue:** Error messages might not be provider-specific

**Current:** Generic error messages

**Recommended:** 
- Add provider-specific error messages
- Handle Anthropic-specific errors (rate limits, API errors)
- Handle OpenAI-specific errors
- Provide helpful error messages to users

**Impact:** Better debugging and user experience

---

### 4. **Ingestion Pipeline** (Priority: Low - Likely OK)
**Location:** `backend/src/core/ingestion.py`

**Status:** ✅ **Likely OK** - Uses OpenAI embeddings (which is correct - Anthropic doesn't provide embeddings)

**Review Needed:**
- Verify embeddings still work correctly
- Check if any hardcoded model references exist
- Ensure ingestion doesn't depend on LLM provider

**Impact:** Minimal - embeddings are separate from LLM provider

---

### 5. **Hardcoded Model References** (Priority: Low)
**Location:** Various files

**Check for:**
- Any hardcoded `"gpt-4o"` or model names
- Configuration files that might need updates
- Documentation that references specific models

**Impact:** Maintainability and clarity

---

## Implementation Priority

1. **High Priority:**
   - ✅ Cache keys (prevents incorrect responses)

2. **Medium Priority:**
   - Query logging (analytics and cost tracking)

3. **Low Priority:**
   - Error handling improvements
   - Ingestion review
   - Hardcoded references cleanup

---

## Testing Checklist

After updates, test:
- [ ] Cache works correctly per provider (GPT-4o query doesn't return Claude response)
- [ ] Query logs include provider/model information
- [ ] Error messages are clear and provider-specific
- [ ] Switching providers works seamlessly
- [ ] Default provider works when no provider specified

---

## Notes

- The compatibility layer is working correctly
- Main issues are in supporting systems (caching, logging)
- No breaking changes expected
- All updates are backward compatible
