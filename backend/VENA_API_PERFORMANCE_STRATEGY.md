# Vena API Integration Performance Strategy

## Overview

This document outlines performance optimisation strategies for integrating the Vena API into the RAG bot system. The primary objective is to enable live data retrieval from Vena tenants without compromising response times for general queries.

## Performance Challenges

Integrating external API calls introduces latency to the system. Vena API requests typically add between 500 milliseconds and 2 seconds to response times. This delay can significantly impact user experience, particularly for queries that do not require live tenant data.

## Performance Optimisation Strategies

### 1. Smart Detection

**Principle:** Only fetch data when explicitly required.

**Implementation:**
- Analyse user queries for keywords that indicate a need for live Vena data
- Trigger API calls only when keywords such as "from Vena", "hierarchy", "my tenant", or "dimensions" are detected
- Skip API calls for general knowledge questions, syntax queries, or troubleshooting that relies solely on documentation

**Benefits:**
- Eliminates unnecessary API calls for the majority of queries
- Reduces latency for queries that do not require live data
- Maintains fast response times for documentation-based questions

### 2. Caching

**Principle:** Store frequently accessed data to avoid repeated API calls.

**Implementation:**
- Cache hierarchy and dimension data with a time-to-live (TTL) of one hour
- Store cached data in Redis or in-memory cache
- First request fetches from the Vena API and stores the result
- Subsequent requests within the TTL period retrieve data from cache
- Implement cache invalidation when data may have changed

**Benefits:**
- Subsequent requests for the same hierarchy return instantly
- Reduces load on the Vena API
- Improves response times for repeated queries

**Considerations:**
- Cache expiry must balance data freshness with performance
- Cache invalidation strategy must account for potential data changes in Vena

### 3. Parallel Execution

**Principle:** Execute independent operations concurrently.

**Implementation:**
- Fetch Vena API data and knowledge base documents simultaneously
- Do not wait for Vena API response before initiating vector search
- Combine results when both operations complete

**Benefits:**
- No additional latency overhead compared to sequential execution
- Total response time equals the longer of the two operations, not their sum
- Maintains fast response times even when API calls are required

### 4. Asynchronous and Background Fetching

**Principle:** Defer non-critical data retrieval when possible.

**Implementation Options:**

**Option A: Background Fetching After Response**
- Return initial response using knowledge base data
- Fetch Vena data in the background
- Update response or cache for future use

**Option B: Pre-fetching on Startup**
- Load common hierarchies during system initialisation
- Store in cache for immediate access
- Refresh periodically in the background

**Option C: Explicit User Request**
- Fetch only when user explicitly requests live data
- Provide clear indication when live data is being used

**Benefits:**
- Immediate response to user queries
- Data available for subsequent requests
- User controls when live data is retrieved

### 5. Conditional Fetching

**Principle:** Apply intelligent rules to determine when API calls are necessary.

**Fetch When:**
- Question mentions specific dimensions (e.g., "Account hierarchy", "Entity structure")
- User explicitly requests live data (e.g., "from my tenant", "current structure")
- Script generation requires real account codes or dimension members
- Question context indicates need for tenant-specific information

**Skip When:**
- General knowledge question about Vena functionality
- Question about VenaQL syntax or best practices
- Troubleshooting question that can be answered from documentation
- No mention of hierarchies, dimensions, or tenant-specific data

**Benefits:**
- Minimises unnecessary API calls
- Maintains fast response times for appropriate queries
- Ensures live data is available when needed

## Recommended Approach: Hybrid Strategy

### Fast Path (No API Call)

**Use Cases:**
- General questions about Vena functionality
- Syntax and best practice queries
- Troubleshooting questions answerable from documentation
- Queries with no mention of live data or hierarchies

**Performance:** Immediate response using knowledge base only

### Smart Path (Cached API Call)

**Use Cases:**
- Questions requiring hierarchy or dimension data
- Script generation needing real account codes
- Queries mentioning specific dimensions

**Process:**
1. Check cache for requested hierarchy
2. If cache hit: return instantly
3. If cache miss: fetch from API, store in cache, then return

**Performance:** Instant for cached data, acceptable delay for first request

### Explicit Path (Always Fetch)

**Use Cases:**
- User explicitly requests latest data ("get latest", "refresh")
- User specifies "force update" or similar
- Critical operations requiring absolute data freshness

**Process:**
- Bypass cache
- Always fetch fresh data from Vena API
- Update cache with new data

**Performance:** Acceptable delay for guaranteed fresh data

## Performance Impact Analysis

### Without Optimisation

**Impact:**
- Every query requiring Vena data adds 500ms to 2 seconds latency
- User experience degrades noticeably
- Increased load on Vena API infrastructure

### With Optimisation

**Impact:**
- Cache hit: No additional latency (instant response)
- Cache miss: 500ms delay (first request only)
- Parallel execution: No overhead (runs concurrently with knowledge base search)
- Most queries: No API call required (fast path)

**Result:** Minimal performance impact for the majority of queries, with acceptable delays only when live data is explicitly required.

## Implementation Suggestion

### Query Flag Approach

Add an optional flag to query requests:

```
use_vena_data: bool = False (default: False)
```

**Fetch Vena Data When:**
- User explicitly sets flag to True
- Question contains hierarchy or dimension keywords
- User explicitly requests live data in the question text

**Result:**
- Most queries: No API call (fast response)
- Specific queries: Cached API call (acceptable delay)
- User maintains control over when live data is used

### Benefits of Flag Approach

- User control: Explicit opt-in for live data
- Backward compatible: Existing queries unaffected
- Performance: Default behaviour remains fast
- Flexibility: Can be combined with automatic detection

## Conclusion

By implementing a hybrid strategy combining smart detection, caching, parallel execution, and conditional fetching, the system can provide live Vena data when needed whilst maintaining fast response times for general queries. The recommended approach ensures that performance remains optimal for the majority of use cases, with live data available on demand.
