# RAG Bot Debugging Guide

This guide covers all the tools and techniques for debugging your RAG bot.

## Table of Contents
1. [Logging Configuration](#logging-configuration)
2. [Debug Scripts](#debug-scripts)
3. [Query Logging](#query-logging)
4. [Error Handling & Tracing](#error-handling--tracing)
5. [Common Debugging Scenarios](#common-debugging-scenarios)
6. [Testing Tools](#testing-tools)

---

## Logging Configuration

### Enable Debug Logging

Set the log level in your `.env` file:

```bash
# In backend/.env
LOG_LEVEL=DEBUG  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

Or set it when starting the server:

```bash
LOG_LEVEL=DEBUG python -m uvicorn src.api.main:app --reload
```

### View Logs

**Console Output:**
- All logs are printed to stdout/stderr
- Format: `YYYY-MM-DD HH:MM:SS - logger_name - LEVEL - message`

**File Logging (Optional):**
- Configure in `backend/src/utils/logging_config.py`
- Add file handler to write logs to disk

**Third-Party Library Logs:**
- By default, third-party libraries (httpx, openai, qdrant, langchain) are set to WARNING
- To see more detail, modify `backend/src/utils/logging_config.py`:

```python
logging.getLogger("openai").setLevel(logging.DEBUG)  # Show OpenAI API calls
logging.getLogger("qdrant_client").setLevel(logging.DEBUG)  # Show Qdrant queries
```

---

## Debug Scripts

### 1. Retrieval Debug Script

Test retrieval directly without the API:

```bash
cd backend
python debug_retrieval.py "Your question here"
```

**What it shows:**
- Pipeline initialization status
- Number of documents retrieved
- Preview of retrieved documents
- Full query response
- Whether response is a refusal

**Example:**
```bash
python debug_retrieval.py "How do I configure Line Item Details?"
```

**Output includes:**
- Retrieved document sources
- Document previews (first 150 chars)
- Response preview (first 500 chars)
- Refusal detection

---

## Query Logging

### View Query Logs

Query logs are stored in PostgreSQL. Access them via:

**1. Admin API (if implemented):**
```bash
GET /api/admin/queries
```

**2. Direct Database Query:**
```sql
SELECT 
    id,
    question,
    answer,
    sources,
    latency_ms,
    was_cached,
    was_refusal,
    refusal_reason,
    created_at
FROM query_logs
ORDER BY created_at DESC
LIMIT 100;
```

**3. Check Logs Script:**
Create `scripts/view_query_logs.py`:

```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv("backend/.env")

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT question, answer, latency_ms, was_refusal, created_at
        FROM query_logs
        ORDER BY created_at DESC
        LIMIT 20
    """))
    
    for row in result:
        print(f"[{row.created_at}] {row.question[:50]}...")
        print(f"  Refusal: {row.was_refusal}, Latency: {row.latency_ms}ms")
```

---

## Error Handling & Tracing

### Sentry Integration

If Sentry is configured, errors are automatically tracked:

**Check Sentry Dashboard:**
- Go to your Sentry project dashboard
- View errors, breadcrumbs, and stack traces
- See custom tags (query, user, etc.)

**Enable Sentry in `.env`:**
```bash
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
SENTRY_ENVIRONMENT=development  # or production
```

### Error Logging

Errors are logged with full tracebacks:

```python
# In backend/src/api/routes/query.py
logger.error(f"Error processing query: {e}", exc_info=True)
```

**View error logs:**
- Check console output (if LOG_LEVEL=DEBUG)
- Check Sentry dashboard
- Check application logs (if file logging enabled)

### Common Error Patterns

**1. "No documents retrieved":**
- Check Qdrant connection
- Verify collection exists
- Check embedding model
- Test with `debug_retrieval.py`

**2. "Tuple index out of range":**
- Usually means `query_async` returned unexpected format
- Check `backend/src/core/rag.py` query methods
- Verify documents list is not empty

**3. "Connection refused" (Qdrant):**
- Check `QDRANT_URL` and `QDRANT_API_KEY`
- Verify network connectivity
- Check Qdrant Cloud dashboard

**4. "Rate limit exceeded":**
- Check Redis connection
- Verify rate limiter configuration
- Check `RATE_LIMIT_QUERY_PER_MINUTE` setting

---

## Common Debugging Scenarios

### Scenario 1: Bot Refuses to Answer

**Symptoms:**
- Response says "context documents do not contain information"
- No sources cited

**Debug Steps:**

1. **Check retrieval:**
   ```bash
   python debug_retrieval.py "Your question"
   ```

2. **Verify documents exist:**
   - Check if documents were retrieved (should see list in debug output)
   - If no documents: check Qdrant collection, embeddings

3. **Check query similarity:**
   - Try rephrasing the question
   - Check if similar questions work
   - Verify knowledge base has relevant content

4. **Check prompt:**
   - Review `SYSTEM_PROMPT` in `backend/src/core/rag.py`
   - Verify synthesis rules are being followed
   - Check if question matches prompt expectations

### Scenario 2: Wrong Sources Cited

**Symptoms:**
- Bot cites sources that don't contain the information
- Sources don't match the answer

**Debug Steps:**

1. **Check retrieved documents:**
   ```bash
   python debug_retrieval.py "Your question"
   ```
   - Review which documents were retrieved
   - Check if they actually contain relevant info

2. **Check source extraction:**
   - Verify `pipeline.get_sources()` method
   - Check document metadata has 'source' field

3. **Review prompt:**
   - Check source verification rules in `SYSTEM_PROMPT`
   - Verify citation format

### Scenario 3: Slow Response Times

**Symptoms:**
- Queries take > 5 seconds
- High latency in query logs

**Debug Steps:**

1. **Check query logs:**
   ```sql
   SELECT latency_ms, was_cached, question
   FROM query_logs
   ORDER BY latency_ms DESC
   LIMIT 10;
   ```

2. **Check cache:**
   - Verify Redis is connected
   - Check if `was_cached=True` in logs
   - Test with `skip_cache=True` to see fresh query time

3. **Check LLM provider:**
   - OpenAI vs Anthropic latency
   - Network latency to API
   - Model selection (gpt-4o vs gpt-3.5-turbo)

4. **Check retrieval:**
   - Qdrant query time
   - Number of documents retrieved (top_k)
   - Embedding generation time

### Scenario 4: Cache Not Working

**Symptoms:**
- Same question returns different latency
- `was_cached=False` for repeated queries

**Debug Steps:**

1. **Check Redis connection:**
   ```python
   # Test Redis
   import redis
   r = redis.from_url(os.getenv("REDIS_URL"))
   r.ping()  # Should return True
   ```

2. **Check cache key:**
   - Verify cache key includes question + calc_script
   - Check if `skip_cache` is being set

3. **Check cache TTL:**
   - Verify `CACHE_TTL` setting (default: 86400 = 24 hours)
   - Check if cache is expiring too quickly

### Scenario 5: Vena API Integration Issues

**Symptoms:**
- Vena data not included in responses
- Errors when `vena_model_id` is provided

**Debug Steps:**

1. **Check Vena API credentials:**
   ```bash
   # In .env
   VENA_API_USER=your-user
   VENA_API_KEY=your-key
   VENA_TENANT_NAME=your-tenant
   ```

2. **Test Vena API directly:**
   ```bash
   python backend/test_vena_api_connection.py
   ```

3. **Check intent detection:**
   - Review `_detect_vena_intent()` in `backend/src/services/vena_api.py`
   - Verify question triggers Vena API call

4. **Check error logs:**
   - Look for Vena API errors in logs
   - Check if API client is enabled

---

## Testing Tools

### 1. Test Retrieval

```bash
cd backend
python debug_retrieval.py "Your test question"
```

### 2. Test Vena API

```bash
python backend/test_vena_api_connection.py
python backend/test_vena_integration.py
```

### 3. Test Error Scenarios

```bash
# Test with invalid question
python debug_retrieval.py ""

# Test with very long question
python debug_retrieval.py "A" * 10000
```

### 4. Load Testing

```bash
python scripts/load_test.py
```

### 5. Test Specific Retrieval Cases

```bash
# Test Error Code 1008 retrieval
python backend/test_error_1008_retrieval.py

# Test intercompany retrieval
python backend/test_intercompany_retrieval.py
```

---

## Quick Debug Checklist

When debugging an issue, follow this checklist:

- [ ] **Check logs:** Set `LOG_LEVEL=DEBUG` and review console output
- [ ] **Test retrieval:** Run `debug_retrieval.py` with the problematic question
- [ ] **Check query logs:** Review recent queries in database
- [ ] **Verify connections:** Qdrant, Redis, PostgreSQL, LLM API
- [ ] **Check environment:** Verify all `.env` variables are set correctly
- [ ] **Test cache:** Check if cache is working (Redis connection)
- [ ] **Review prompt:** Check if prompt rules are causing the issue
- [ ] **Check Sentry:** Review error tracking dashboard
- [ ] **Test with different providers:** Try OpenAI vs Anthropic
- [ ] **Check knowledge base:** Verify relevant documents exist

---

## Advanced Debugging

### Enable Verbose Logging for Specific Components

Modify `backend/src/utils/logging_config.py`:

```python
# Enable DEBUG for specific loggers
logging.getLogger("src.core.rag").setLevel(logging.DEBUG)
logging.getLogger("src.services.vena_api").setLevel(logging.DEBUG)
logging.getLogger("src.services.cache").setLevel(logging.DEBUG)
```

### Add Custom Debug Points

Add temporary debug logging in code:

```python
# In backend/src/core/rag.py
logger.debug(f"Retrieved {len(documents)} documents")
logger.debug(f"Document sources: {[d.metadata.get('source') for d in documents]}")
logger.debug(f"Response length: {len(response)} chars")
```

### Profile Query Performance

Add timing to identify bottlenecks:

```python
import time

start = time.time()
documents = pipeline.retrieve(question)
retrieval_time = time.time() - start

start = time.time()
response = pipeline.generate_response(question, documents)
generation_time = time.time() - start

logger.debug(f"Retrieval: {retrieval_time:.2f}s, Generation: {generation_time:.2f}s")
```

---

## Getting Help

If you're stuck:

1. **Check existing test files** for examples
2. **Review query logs** to see what's working
3. **Use debug scripts** to isolate the issue
4. **Check Sentry** for error details
5. **Review this guide** for common scenarios

For production issues, always check:
- Sentry dashboard for errors
- Query logs for patterns
- System health endpoints (`/api/health`)
