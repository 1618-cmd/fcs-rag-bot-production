# Render Performance Fixes

## Issues Found

1. **No Workers Configured** - Uvicorn was running with a single worker, meaning only one request could be processed at a time
2. **Blocking Operations** - RAG pipeline operations were synchronous, blocking the event loop
3. **No Timeout Settings** - No timeout configuration could cause hanging requests
4. **No Connection Pooling** - Qdrant client wasn't configured with timeouts

## Fixes Applied

### 1. Added Uvicorn Workers (`render.yaml`, `Procfile`, `railway.toml`)
```bash
--workers 4 --timeout-keep-alive 30
```
- **4 workers**: Allows handling 4 concurrent requests
- **30s keep-alive**: Prevents connection timeouts

### 2. Made RAG Pipeline Async (`backend/src/core/rag.py`)
- Added `retrieve_async()` and `generate_response_async()` methods
- Uses `asyncio.to_thread()` to run blocking operations in thread pool
- Updated `query_async()` to use async methods

### 3. Updated Query Endpoint (`backend/src/api/routes/query.py`)
- Changed to use `pipeline.query_async()` instead of synchronous `query()`
- Properly handles async operations without blocking

### 4. Added Qdrant Timeout (`backend/src/core/rag.py`)
- Set 30-second timeout on Qdrant client to prevent hanging

## Expected Performance Improvements

- **Concurrent Requests**: Can now handle 4 requests simultaneously (vs 1 before)
- **Non-blocking**: Async operations won't block the event loop
- **Better Resource Utilisation**: Multiple workers can process requests in parallel
- **Reduced Latency**: Better connection handling and timeouts

## Next Steps

1. **Commit and push changes to GitHub**
2. **Redeploy on Render** - Render will automatically detect the changes and redeploy
3. **Monitor performance** - Check Render logs and metrics after deployment
4. **Test response times** - Should see improvement in concurrent request handling

## Notes

- The 4 workers setting is optimal for Render Professional tier
- If you need more concurrent requests, you can increase workers (but monitor CPU/memory usage)
- The async changes maintain backward compatibility - synchronous methods still exist
