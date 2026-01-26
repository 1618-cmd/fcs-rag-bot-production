# How to View Questions Asked in Production

## Current Status

**Query logging to a database is NOT yet implemented.** Queries are only logged via Python logging (to stdout), which are visible in your deployment platform's logs.

---

## Option 1: View Render Logs (Immediate Solution)

Your backend is deployed on **Render**. You can view all queries in real-time:

### Steps:

1. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com/
   - Log in to your account

2. **Navigate to Your Service**
   - Find your `fcs-rag-bot-production` service
   - Click on it

3. **View Logs**
   - Click the **"Logs"** tab at the top
   - You'll see real-time application logs including:
     - `Processing query: {question}...` - Shows each query being processed
     - `Query completed in {latency}ms` - Shows response time
     - `Returning cached response` - Shows cache hits

4. **Search Logs**
   - Use the search box to filter for specific queries
   - Search for: `"Processing query"` to see all questions

### What You'll See:

```
INFO: Processing query: How do I configure Line Item Details in Vena Copilot?...
INFO: Query completed in 2345.67ms
INFO: Returning cached response (saved 2345ms)
```

---

## Option 2: Implement Database Query Logging (Recommended for Analytics)

To properly track and analyze queries, implement database logging.

### Benefits:
- ✅ Store all queries in a database
- ✅ Query/search historical questions
- ✅ Analyze popular questions, latency, sources
- ✅ Build an admin dashboard to view queries

### Implementation Plan:

**Step 1: Set up Database Models**
- Create `QueryLog` table in PostgreSQL
- Fields: `id`, `question`, `answer`, `sources`, `latency_ms`, `timestamp`, `user_id`

**Step 2: Create Logging Service**
- Create `backend/src/services/logging.py`
- Function: `log_query(question, answer, sources, latency)`

**Step 3: Integrate with API**
- In `backend/src/api/routes/query.py`
- After each query, call `log_query()` to save to database

**Step 4: Create Admin Endpoint**
- `GET /api/admin/queries` - List all queries with filters
- `GET /api/admin/queries/{id}` - Get specific query
- `GET /api/admin/analytics` - Get query statistics

**Step 5: Build Admin UI (Optional)**
- Add queries page to Admin tab
- Show table of recent queries
- Add filters (date range, search)

---

## Quick Comparison

| Method | Pros | Cons |
|--------|------|------|
| **Render Logs** | ✅ Available now<br>✅ Real-time<br>✅ No code changes | ❌ Can't search easily<br>❌ No analytics<br>❌ Logs expire |
| **Database Logging** | ✅ Searchable<br>✅ Analytics<br>✅ Permanent storage | ❌ Requires implementation<br>❌ Needs database |

---

## Recommendation

**For now**: Use **Render Logs** (Option 1) to view queries immediately.

**For later**: Implement **Database Logging** (Option 2) for proper analytics and historical tracking.

---

## Next Steps

If you want to implement database logging, I can:
1. Create the database models
2. Add the logging service
3. Integrate with the API
4. Create admin endpoints to view queries

Would you like me to implement database query logging now?
