# FCS RAG Bot - TODO List (Organized by Epics)

**Last Updated:** January 2026  
**Project:** FCS RAG Bot Production (VRBP)

---

## 📋 Epic Overview

| Epic | Items | Priority | Status |
|------|-------|----------|--------|
| **EPIC-1: Prompt Versioning & Management** | 5 | 🔴 High | Not Started |
| **EPIC-2: Sentry Integration & Observability** | 4 | 🔴 High | Not Started |
| **EPIC-3: Prompt Context Injection & Templating** | 4 | 🔴 High | Not Started |
| **EPIC-4: Prompt Engineering & Optimization** | 3 | 🔴 High | Not Started |
| **EPIC-5: Enhanced Document Management** | 4 | 🔴 High | Not Started |
| **EPIC-6: Vena API Integration & Data Pulling** | 8 | 🔴 High | Not Started |
| **EPIC-7: LLM Provider Compatibility Fixes** | 7 | 🟡 Medium | Not Started |
| **EPIC-8: Infrastructure & Code Quality** | 8 | 🟡 Medium | Not Started |
| **EPIC-9: Testing & Quality Assurance** | 3 | 🟢 Low | Not Started |
| **EPIC-10: Documentation & Knowledge Base** | 4 | 🟢 Low | Not Started |
| **EPIC-11: Advanced Prompt Features** | 4 | 🟢 Low | Not Started |
| **EPIC-12: Monitoring & Analytics** | 4 | 🟢 Low | Not Started |
| **Total** | **56** | | |

---

## 🔴 High Priority Epics

---

### EPIC-1: Prompt Versioning & Management System

**Description:** Implement a comprehensive prompt versioning system to track, manage, and deploy prompt changes with rollback capabilities.

**Epic Key:** `VRBP-EPIC-1`  
**Priority:** High  
**Estimated Effort:** 2-3 weeks

#### Tasks:
- [ ] **VRBP-1.1** - Create prompt versioning database schema
  - Store prompt versions with metadata (version number, date, author, description)
  - Track which version is active/production
  - Support rollback to previous versions
- [ ] **VRBP-1.2** - Create prompt management service (`backend/src/services/prompt_manager.py`)
  - CRUD operations for prompts
  - Version comparison and diff functionality
  - A/B testing support (run multiple versions simultaneously)
- [ ] **VRBP-1.3** - Add prompt version tracking to query logs
  - Log which prompt version was used for each query
  - Enable analytics on prompt performance
- [ ] **VRBP-1.4** - Create admin API endpoints for prompt management
  - `GET /api/admin/prompts` - List all prompt versions
  - `POST /api/admin/prompts` - Create new prompt version
  - `PUT /api/admin/prompts/{version}/activate` - Activate a version
  - `GET /api/admin/prompts/{version}` - Get specific version
- [ ] **VRBP-1.5** - Add prompt version to configuration
  - Environment variable: `PROMPT_VERSION` (defaults to "latest")
  - Support per-tenant prompt versions (future)

**Acceptance Criteria:**
- Admins can create, view, and activate prompt versions
- Query logs include prompt version information
- System supports rollback to previous prompt versions
- A/B testing infrastructure is in place

---

### EPIC-2: Sentry Integration with Prompt Breadcrumbs

**Description:** Enhance Sentry error tracking with detailed prompt execution breadcrumbs and context for better debugging and monitoring.

**Epic Key:** `VRBP-EPIC-2`  
**Priority:** High  
**Estimated Effort:** 1 week

#### Tasks:
- [ ] **VRBP-2.1** - Add Sentry breadcrumbs for prompt execution
  - Log prompt version used
  - Log prompt template (truncated if too long)
  - Log context documents count and sources
  - Log LLM provider and model used
  - Log token counts (input/output)
- [ ] **VRBP-2.2** - Add custom Sentry tags for prompts
  - `prompt_version`
  - `prompt_type` (system/user)
  - `llm_provider`
  - `model_name`
- [ ] **VRBP-2.3** - Create prompt-specific Sentry context
  - Add prompt metadata to Sentry scope before LLM calls
  - Include prompt in error context when LLM errors occur
- [ ] **VRBP-2.4** - Add performance tracking for prompts
  - Track prompt execution time
  - Track token usage per prompt version
  - Track error rates per prompt version

**Acceptance Criteria:**
- All prompt executions create Sentry breadcrumbs
- Error reports include full prompt context
- Performance metrics are tracked per prompt version
- Custom tags enable filtering in Sentry dashboard

---

### EPIC-3: Prompt Context Injection & Templating System

**Description:** Implement dynamic prompt context injection and templating to support personalized, query-specific prompts.

**Epic Key:** `VRBP-EPIC-3`  
**Priority:** High  
**Estimated Effort:** 2-3 weeks

#### Tasks:
- [ ] **VRBP-3.1** - Create dynamic context injection service
  - Support variable injection (user context, tenant info, query metadata)
  - Support conditional prompt sections based on query type
  - Support few-shot example injection based on query similarity
- [ ] **VRBP-3.2** - Add context injection to RAG pipeline
  - Inject user role/tenant-specific instructions
  - Inject query type-specific guidelines (VenaQL vs general questions)
  - Inject recent conversation context
- [ ] **VRBP-3.3** - Create prompt template system
  - Support Jinja2-style templating for prompts
  - Allow dynamic sections based on query analysis
  - Support prompt composition (base + specialized sections)
- [ ] **VRBP-3.4** - Modularize prompts into reusable components
  - Break down monolithic prompts into smaller, reusable modules
  - Create prompt component library (anti-hallucination rules, VenaQL syntax rules, source citation guidelines, etc.)
  - Support component versioning and composition
  - Create component registry with metadata (purpose, usage, dependencies)
  - Enable mix-and-match prompt building from components
  - Support component inheritance and overrides
  - Add component testing and validation

**Acceptance Criteria:**
- Prompts can be dynamically customized based on user/tenant context
- Query type detection triggers appropriate prompt sections
- Template system supports complex prompt composition
- Few-shot examples are injected based on query similarity
- Prompts are modularized into reusable components
- Component library enables easy prompt assembly
- Components can be versioned and tested independently

---

### EPIC-4: Prompt Engineering & Optimization Framework

**Description:** Build tools and workflows for testing, analyzing, and optimizing prompts systematically.

**Epic Key:** `VRBP-EPIC-4`  
**Priority:** High  
**Estimated Effort:** 2-3 weeks

#### Tasks:
- [ ] **VRBP-4.1** - Create prompt testing framework
  - Test suite for prompt variations
  - Automated evaluation metrics (accuracy, relevance, hallucination rate)
  - A/B testing infrastructure
- [ ] **VRBP-4.2** - Add prompt analytics dashboard
  - Track prompt performance metrics
  - Compare versions side-by-side
  - Identify prompt weaknesses
- [ ] **VRBP-4.3** - Create prompt optimization workflow
  - Iterative improvement process
  - Version control for prompt experiments
  - Rollback capability

**Acceptance Criteria:**
- Automated test suite evaluates prompt variations
- Analytics dashboard shows prompt performance comparisons
- Optimization workflow supports iterative improvements
- A/B testing allows running multiple prompt versions simultaneously

---

### EPIC-5: Enhanced Document Management System

**Description:** Improve document management with versioning, enhanced metadata, search capabilities, and analytics.

**Epic Key:** `VRBP-EPIC-5`  
**Priority:** High  
**Estimated Effort:** 2 weeks

#### Tasks:
- [ ] **VRBP-5.1** - Add document versioning
  - Track document versions in database
  - Support document updates without full re-ingestion
  - Incremental ingestion (only changed documents)
- [ ] **VRBP-5.2** - Improve document metadata tracking
  - Store document source, author, last modified date
  - Track document approval status and workflow
  - Store document categories/tags
- [ ] **VRBP-5.3** - Add document search and filtering
  - Search documents by name, content, metadata
  - Filter by status, category, date range
  - Bulk operations (approve/reject multiple)
- [ ] **VRBP-5.4** - Create document analytics
  - Track which documents are most frequently retrieved
  - Identify unused or outdated documents
  - Document quality metrics

**Acceptance Criteria:**
- Documents are versioned and can be updated incrementally
- Rich metadata is stored and searchable
- Admin can search, filter, and bulk manage documents
- Analytics identify document usage patterns and quality issues

---

### EPIC-6: Vena API Integration & Data Pulling

**Description:** Enhance Vena API integration to pull and synchronize tenant data (dimensions, hierarchies, intersections, model structure) with intelligent caching, real-time updates, and comprehensive error handling.

**Epic Key:** `VRBP-EPIC-6`  
**Priority:** High  
**Estimated Effort:** 3-4 weeks

#### Tasks:
- [ ] **VRBP-6.1** - Enhance Vena API client with additional endpoints
  - Implement model listing/discovery (if available)
  - Add support for dimension hierarchies endpoint
  - Add support for member relationships (parent/child)
  - Implement pagination for large datasets
  - Add rate limiting and request throttling
- [ ] **VRBP-6.2** - Create data synchronization service
  - Background job to periodically pull Vena tenant data
  - Incremental updates (only changed data)
  - Full sync capability for initial setup
  - Conflict resolution for concurrent updates
  - Sync status tracking and reporting
- [ ] **VRBP-6.3** - Implement intelligent caching for Vena API data
  - Cache dimensions, members, and hierarchies
  - Cache intersection data with TTL based on data type
  - Cache invalidation strategies (time-based, event-based)
  - Multi-level caching (memory + Redis)
  - Cache warming for frequently accessed data
- [ ] **VRBP-6.4** - Add model ID management system
  - Store model IDs per tenant/user
  - Model ID discovery and validation
  - Support for multiple models per tenant
  - Model metadata storage (name, description, last sync)
  - Admin UI for model ID management
- [ ] **VRBP-6.5** - Create data transformation and formatting service
  - Transform Vena API responses to RAG-friendly format
  - Format hierarchies for prompt injection
  - Structure dimension members for context
  - Aggregate intersection data for summaries
  - Handle large datasets with summarization
- [ ] **VRBP-6.6** - Enhance error handling and retry logic
  - Exponential backoff for rate limits
  - Retry strategies for transient failures
  - Circuit breaker pattern for API failures
  - Graceful degradation when API unavailable
  - Detailed error logging and alerting
- [ ] **VRBP-6.7** - Add real-time data update capabilities
  - Webhook support for Vena data changes (if available)
  - Polling mechanism for data updates
  - Event-driven cache invalidation
  - Real-time sync status dashboard
  - Notification system for sync failures
- [ ] **VRBP-6.8** - Create Vena API analytics and monitoring
  - Track API call frequency and costs
  - Monitor API response times
  - Track data freshness metrics
  - Alert on API errors or failures
  - Dashboard for Vena API health

**Acceptance Criteria:**
- Vena API client supports all necessary endpoints
- Data synchronization runs automatically and reliably
- Caching reduces API calls by 80%+
- Model IDs are managed per tenant/user
- Data is transformed and formatted for RAG context
- Error handling gracefully handles API failures
- Real-time updates keep data fresh
- Analytics provide visibility into API usage

**Dependencies:**
- Redis for caching
- Background job system (Celery or similar)
- Database for storing model IDs and sync status

---

## 🟡 Medium Priority Epics

---

### EPIC-7: LLM Provider Compatibility Fixes

**Description:** Fix compatibility issues and enhance support for multiple LLM providers (OpenAI, Anthropic) with proper caching, logging, and error handling.

**Epic Key:** `VRBP-EPIC-7`  
**Priority:** Medium  
**Estimated Effort:** 1-2 weeks

#### Tasks:
- [ ] **VRBP-7.1** - Update cache keys to include LLM provider
  - Location: `backend/src/api/routes/query.py` (lines 204-207)
  - Include provider in cache key: `f"{llm_provider}:{question}"`
  - Prevents cross-provider cache hits (GPT-4o response returned for Claude query)
- [ ] **VRBP-6.2** - Add LLM provider/model tracking to query logs
  - Add `llm_provider` field to `QueryLog` model
  - Add `model_name` field to `QueryLog` model
  - Update `log_query_async()` to accept provider/model parameters
  - Pass provider/model from query endpoint to logger
- [ ] **VRBP-6.3** - Add provider-specific analytics
  - Cost tracking per provider
  - Performance comparison (latency, token usage)
  - Error rate comparison
- [ ] **VRBP-6.4** - Add provider-specific error handling
  - Anthropic-specific errors (rate limits, API errors)
  - OpenAI-specific errors
  - Better error messages for users
- [ ] **VRBP-6.5** - Add error recovery strategies
  - Automatic retry with exponential backoff
  - Fallback to alternative provider on failure
  - Graceful degradation

**Acceptance Criteria:**
- Cache keys prevent cross-provider cache hits
- Query logs track provider and model information
- Analytics compare provider performance and costs
- Error handling is provider-specific with recovery strategies

---

### EPIC-8: Infrastructure & Code Quality Improvements

**Description:** Review and improve infrastructure components, remove hardcoded references, and enhance code quality.

**Epic Key:** `VRBP-EPIC-8`  
**Priority:** Medium  
**Estimated Effort:** 1 week

#### Tasks:
- [ ] **VRBP-8.1** - Verify embeddings still work correctly
- [ ] **VRBP-8.2** - Check for hardcoded model references
- [ ] **VRBP-8.3** - Ensure ingestion doesn't depend on LLM provider
- [ ] **VRBP-8.4** - Add ingestion performance metrics
- [ ] **VRBP-8.5** - Search codebase for hardcoded model names
- [ ] **VRBP-8.6** - Replace with configuration-based references
- [ ] **VRBP-8.7** - Update documentation with model references
- [ ] **VRBP-8.8** - Evaluate and implement retrieval improvements (discussion)
  - **Option 1: Hybrid search (keyword + semantic)**
    - Combine semantic similarity with keyword matching (e.g., BM25)
    - Pros: Better for exact term matches; can surface documents that rank lower semantically
    - Cons: More complexity; requires tuning
  - **Option 2: Query rewriting with LLM**
    - Use the LLM to rewrite the query into multiple variations before retrieval
    - Pros: Can generate more specific queries that match document phrasing
    - Cons: Extra LLM call; adds latency
  - **Option 3: Reranking**
    - Retrieve more (e.g., 50), then rerank with a cross-encoder
    - Pros: Better final ordering
    - Cons: More compute; requires a reranker model
  - **Option 4: Adjust prompt strictness**
    - Allow synthesis when documents are related but not exact matches
    - Pros: More flexible answers
    - Cons: Risk of over-interpretation
  - **Option 5: Multiple retrieval strategies**
    - Run multiple queries (original, simplified, keyword-focused) and merge results
    - Pros: Broader coverage
    - Cons: More complexity and cost
  - **Current Status:** Query expansion implemented (top_k=20, keyword expansion)
  - **Issue:** Some queries (e.g., "troubleshoot VenaQL incorrect results") not retrieving relevant documents despite them existing in knowledge base

**Acceptance Criteria:**
- All embeddings work correctly with current setup
- No hardcoded model references exist
- Ingestion is provider-agnostic
- Performance metrics are tracked for ingestion
- Retrieval improvements evaluated and best option(s) selected for implementation

---

## 🟢 Low Priority Epics

---

### EPIC-8: Testing & Quality Assurance

**Description:** Create comprehensive testing framework for prompts and ensure quality through automated testing.

**Epic Key:** `VRBP-EPIC-8`  
**Priority:** Low  
**Estimated Effort:** 1-2 weeks

#### Tasks:
- [ ] **VRBP-8.1** - Create test cases for prompt variations
- [ ] **VRBP-8.2** - Automated prompt evaluation
- [ ] **VRBP-8.3** - Regression testing for prompt changes

**Acceptance Criteria:**
- Test suite covers prompt variations
- Automated evaluation runs on prompt changes
- Regression tests prevent prompt quality degradation

---

### EPIC-9: Documentation & Knowledge Base Updates

**Description:** Update and enhance documentation for new systems and features.

**Epic Key:** `VRBP-EPIC-9`  
**Priority:** Low  
**Estimated Effort:** 1 week

#### Tasks:
- [ ] **VRBP-9.1** - Document prompt versioning system
- [ ] **VRBP-9.2** - Document Sentry breadcrumb structure
- [ ] **VRBP-9.3** - Document context injection system
- [ ] **VRBP-9.4** - Update API documentation

**Acceptance Criteria:**
- All new systems are fully documented
- API documentation is up-to-date
- Documentation includes examples and best practices

---

### EPIC-10: Advanced Prompt Features

**Description:** Implement advanced prompt features for enhanced personalization and context awareness.

**Epic Key:** `VRBP-EPIC-10`  
**Priority:** Low  
**Estimated Effort:** 2-3 weeks

#### Tasks:
- [ ] **VRBP-10.1** - Multi-turn conversation context in prompts
- [ ] **VRBP-10.2** - Dynamic few-shot example selection
- [ ] **VRBP-10.3** - Prompt templates for different query types
- [ ] **VRBP-10.4** - Prompt personalization per user/tenant

**Acceptance Criteria:**
- Prompts include conversation history
- Few-shot examples are dynamically selected
- Query types trigger appropriate prompt templates
- Prompts are personalized per user/tenant

---

### EPIC-11: Monitoring & Analytics Dashboards

**Description:** Build comprehensive monitoring and analytics dashboards for prompts, performance, and costs.

**Epic Key:** `VRBP-EPIC-11`  
**Priority:** Low  
**Estimated Effort:** 2 weeks

#### Tasks:
- [ ] **VRBP-11.1** - Prompt performance dashboards
- [ ] **VRBP-11.2** - Real-time prompt monitoring
- [ ] **VRBP-11.3** - Alerting for prompt degradation
- [ ] **VRBP-11.4** - Cost tracking per prompt version

**Acceptance Criteria:**
- Dashboards display prompt performance metrics
- Real-time monitoring shows current system state
- Alerts notify when prompt quality degrades
- Cost tracking shows spending per prompt version

---

## 🎯 Quick Wins (Can be done immediately)

These tasks can be completed quickly and provide immediate value:

1. **VRBP-QW-1** - Add prompt version to Sentry breadcrumbs (1-2 hours)
   - Simple addition to existing Sentry integration
   - High value for debugging

2. **VRBP-QW-2** - Update cache keys to include provider (30 min)
   - Critical bug fix
   - Prevents incorrect responses

3. **VRBP-QW-3** - Add provider/model to query logs (1 hour)
   - Extend existing logging
   - Enables analytics

4. **VRBP-QW-4** - Create prompt versioning database model (1 hour)
   - Foundation for future work
   - Can be done incrementally

---

## 📊 Epic Priority Matrix

| Epic | Impact | Effort | Priority | Dependencies |
|------|--------|--------|----------|--------------|
| EPIC-6 (Cache keys fix) | High | Low | 🔴 Do First | None |
| EPIC-1 (Prompt versioning) | High | Medium | 🔴 High | None |
| EPIC-2 (Sentry breadcrumbs) | Medium | Low | 🔴 High | EPIC-1 |
| EPIC-3 (Context injection) | High | High | 🔴 High | EPIC-1 |
| EPIC-4 (Prompt engineering) | High | High | 🔴 High | EPIC-1, EPIC-2 |
| EPIC-5 (Document management) | Medium | Medium | 🔴 High | None |
| EPIC-6 (Provider compatibility) | Medium | Low | 🟡 Medium | None |
| EPIC-7 (Infrastructure) | Low | Medium | 🟡 Medium | None |
| EPIC-8 (Testing) | Medium | Medium | 🟢 Low | EPIC-1, EPIC-4 |
| EPIC-9 (Documentation) | Low | Low | 🟢 Low | All epics |
| EPIC-10 (Advanced features) | Medium | High | 🟢 Low | EPIC-1, EPIC-3 |
| EPIC-11 (Monitoring) | Medium | Medium | 🟢 Low | EPIC-1, EPIC-2 |

---

## 📋 Implementation Notes

### Prompt Versioning Architecture
```
backend/src/services/
├── prompt_manager.py       # Prompt CRUD and versioning
├── prompt_context.py       # Context injection service
├── prompt_analytics.py    # Performance tracking
└── prompt_components.py   # Modular prompt components

backend/src/models/
├── prompt_version.py      # Database model for prompt versions
└── prompt_component.py    # Database model for prompt components

backend/src/api/routes/
└── admin/
    ├── prompts.py         # Admin endpoints for prompt management
    └── prompt_components.py  # Admin endpoints for component management
```

### Modular Prompt Component Structure
```python
# Example prompt component structure
class PromptComponent:
    id: str
    name: str  # e.g., "anti-hallucination-rules"
    version: str
    category: str  # e.g., "rules", "guidelines", "examples", "instructions"
    content: str  # The actual prompt text
    dependencies: List[str]  # Other component IDs this depends on
    metadata: Dict  # Purpose, usage notes, tags
    
# Example component library:
components = {
    "anti-hallucination-rules": {
        "content": "CRITICAL ANTI-HALLUCINATION RULES...",
        "category": "rules",
        "required": True
    },
    "venaql-syntax-rules": {
        "content": "CRITICAL VENAQL CALCULATION SCRIPT SYNTAX RULES...",
        "category": "rules",
        "required": False
    },
    "source-citation-guidelines": {
        "content": "SOURCE VERIFICATION REQUIREMENTS...",
        "category": "guidelines",
        "required": True
    },
    "venaql-troubleshooting-examples": {
        "content": "FEW-SHOT EXAMPLE - VenaQL Scope Troubleshooting...",
        "category": "examples",
        "required": False
    }
}

# Prompt composition:
final_prompt = compose_prompt([
    "anti-hallucination-rules",
    "source-citation-guidelines",
    "venaql-syntax-rules",  # Only if query is VenaQL-related
    "venaql-troubleshooting-examples"  # Only if query is troubleshooting
])
```

### Sentry Breadcrumb Structure
```python
# Example breadcrumb data
{
    "category": "prompt",
    "message": "Executing RAG query",
    "level": "info",
    "data": {
        "prompt_version": "v2.1.0",
        "llm_provider": "openai",
        "model": "gpt-4o",
        "context_docs_count": 5,
        "input_tokens": 1250,
        "output_tokens": 350
    }
}
```

### Document Management Schema
```python
# Enhanced document model
class Document:
    id: str
    name: str
    path: str
    version: int
    status: str  # pending, approved, archived
    category: str
    tags: List[str]
    metadata: Dict
    created_at: datetime
    updated_at: datetime
    approved_by: Optional[str]
    approved_at: Optional[datetime]
```

---

## 🔗 Related Documentation

- [LLM Provider Compatibility Review Checklist](docs/LLM_PROVIDER_REVIEW_CHECKLIST.md)
- [Jira Setup Guide](JIRA_SETUP.md)
- [Project Context](PROJECT_CONTEXT.md)

---

## 📝 Epic Creation Guide for Jira

### Suggested Epic Structure:
1. **Epic Name Format:** `[Feature Area]: [Brief Description]`
   - Example: `Prompt Management: Versioning & Management System`

2. **Epic Description Template:**
   ```
   [Brief description of what this epic delivers]
   
   **Business Value:** [Why this matters]
   **Success Criteria:** [How we'll know it's done]
   **Dependencies:** [Other epics or work]
   ```

3. **Epic Labels:**
   - `prompt-management`
   - `sentry-integration`
   - `document-management`
   - `llm-provider`
   - `infrastructure`
   - `testing`
   - `documentation`
   - `monitoring`

4. **Epic Priority:**
   - Use Jira priority field: High, Medium, Low
   - Match with 🔴 🟡 🟢 indicators

---

**Note:** This TODO list is organized by epics for Jira project management. Each epic contains related tasks that can be broken down into stories and subtasks in Jira.
