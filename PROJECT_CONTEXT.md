# Vena RAG Bot - Production Project Context

**Created:** January 6, 2026  
**Source:** POC Project (December 2024 - January 2026)  
**Purpose:** Production implementation of Vena RAG-Based Technical Support System

---

## Project Overview

This production project is based on a successful 2-3 week Proof of Concept (POC) that validated the core hypothesis: **A RAG system can accurately retrieve and synthesize answers to complex Vena technical questions from a curated knowledge base.**

### Key Success from POC
- ✅ Validated retrieval quality (≥80% relevance)
- ✅ Working prototype with Streamlit interface
- ✅ Core RAG pipeline functional
- ✅ Knowledge base ingestion working
- ✅ Go/No-Go decision: **GO** for Phase 1 production

---

## Business Context

### Problem Statement
- Contractors face 3-4 week onboarding period (or 12 weeks self-learning)
- 40-50% of senior resource time consumed by repetitive technical queries
- Technical knowledge exists as tribal knowledge
- Historical issue resolutions not systematically captured

### Solution
RAG-based AI assistant providing:
- Knowledge Q&A with source citations
- VenaQL code generation and explanation
- Issue diagnosis and troubleshooting (Phase 2)
- Automated documentation generation (Phase 2)

### Expected Benefits
- Reduction in contractor onboarding time (weeks → days)
- 60% decrease in interruptions to senior resources
- 80% self-service resolution rate
- Continuous knowledge base growth

---

## Technical Decisions Made

### Technology Stack (POC → Production)

| Component | POC Choice | Production Recommendation | Rationale |
|-----------|------------|---------------------------|-----------|
| **LLM** | OpenAI GPT-4o | OpenAI GPT-4o | Best quality/speed/cost balance |
| **Embeddings** | OpenAI text-embedding-3-small | OpenAI text-embedding-3-small | Cost-effective, high quality |
| **Vector DB** | ChromaDB (local) | Pinecone (production) / Weaviate (cost control) | Scalability, managed service |
| **Backend** | Python + FastAPI | Python + FastAPI | Async support, API documentation |
| **Frontend** | Streamlit | React (Phase 2) | Better UX, component reusability |
| **Hosting** | Local | Railway / Streamlit Cloud | Easy deployment, scaling |
| **Database** | N/A | PostgreSQL (Supabase/Railway) | User accounts, logs, metadata |
| **Cache** | N/A | Redis | Performance optimization |
| **Monitoring** | N/A | Sentry, PostHog | Error tracking, analytics |
| **Auth** | N/A | Clerk / Auth0 (Phase 2) | User authentication |

### Architecture Decisions

1. **RAG Pipeline**: Semantic search + LLM synthesis (validated in POC)
2. **Document Chunking**: 500 tokens with 50 token overlap
3. **Retrieval**: Top 3-5 most relevant documents
4. **Response Format**: Always include source citations
5. **Code Validation**: Custom Python validation engine for VenaQL

---

## Project Structure

### POC Structure (What We Built)
```
RAG Bot POC/
├── src/
│   ├── config.py          # Configuration settings
│   ├── ingestion.py       # Document ingestion pipeline
│   ├── retrieval.py      # RAG query pipeline
│   └── app.py             # Streamlit chat interface
├── knowledge_base/        # Vena documentation
│   ├── issue_resolutions/
│   ├── patterns/
│   ├── concepts/
│   └── troubleshooting/
├── data/                  # ChromaDB vector storage
└── requirements.txt
```

### Production Structure (Recommended)
```
Vena RAG Bot Production/
├── backend/
│   ├── src/
│   │   ├── api/           # FastAPI routes
│   │   ├── core/          # Core RAG logic
│   │   ├── services/      # Business logic
│   │   ├── models/        # Data models
│   │   └── utils/         # Utilities
│   ├── tests/
│   └── requirements.txt
├── frontend/              # React app (Phase 2)
├── knowledge_base/       # Vena documentation
├── infrastructure/        # Docker, deployment configs
├── docs/                  # Documentation
└── scripts/               # Deployment, migration scripts
```

---

## Key Documents from POC

### 1. Business Requirements Document (BRD)
- **Location**: `BRD_Complete.docx` / `BRD_Complete.md`
- **Version**: 1.1 (January 5, 2026)
- **Key Sections**:
  - User Requirements (UR-001 to UR-007)
  - Functional Requirements (FR-001 to FR-013)
  - Non-Functional Requirements (NFR-001 to NFR-008)
  - Compliance & Legal (Sections 18-20)
  - Security & Data Protection

### 2. POC Proposal
- **Location**: `POC_Proposal.md`
- **Key Outcomes**: Validated retrieval quality, working prototype

### 3. Production Architecture Decision
- **Location**: `Production_Architecture_Decision_Proposal.docx`
- **Key Decisions**: Technology stack, hosting, scaling strategy

### 4. Jira Project Structure
- **Project Key**: FRBP (FCS RAG Bot - Phase1)
- **Epics**: 5 Epics for Phase 1
- **Stories**: 23 Stories mapped to BRD requirements

---

## Phase 1 Requirements (Months 1-2)

### Core Features
1. **Knowledge Query and Response (UR-001)**
   - Natural language queries
   - Source citations
   - Conversation context

2. **VenaQL Code Explanation (UR-002)**
   - Plain-English explanations
   - Component identification

3. **Simple VenaQL Code Generation (UR-003)**
   - Pattern-based generation
   - Syntax validation
   - Confidence scoring

4. **Web Interface (UR-006)**
   - Chat interface
   - Responsive design
   - 99% uptime during business hours

5. **Basic Analytics (FR-007)**
   - Query logging
   - Feedback collection
   - Usage metrics

### Success Criteria
- 85% accuracy on knowledge Q&A
- 90% syntax validity on generated code
- Average response time < 3 seconds
- User satisfaction score > 4.0/5.0

---

## Phase 2 Requirements (Months 3-4)

### Enhanced Features
1. **Issue Diagnosis Support (UR-004)**
2. **Documentation Generation (UR-005)**
3. **Advanced Code Generation**
4. **Vena Metadata Integration**
5. **Authentication & SSO**

---

## Compliance & Security Requirements

### GDPR Compliance (Section 18)
- Data Protection Impact Assessment (DPIA) required
- Data retention policies:
  - Query logs: 90 days
  - Audit logs: 7 years
  - User accounts: Active + 30 days
- Data Processing Agreements with third parties

### Audit Requirements (Section 19)
- All user queries logged
- All code generation requests logged
- Access reviews: Quarterly
- Configuration changes logged

### Security Requirements (Section 20)
- Data encrypted in transit (HTTPS/TLS)
- Data encrypted at rest
- Input validation and sanitization
- Security monitoring and alerting
- Penetration testing (Phase 2)

---

## Team & Resources

### Core Team
- **ML Engineer**: Full-time (4 months)
- **Vena SME**: 50% (4 months)
- **Technical Writer**: 50% (2 months)
- **Project Manager**: 25% (4 months)

### Stakeholders
- **Project Sponsor**: Budget approval, ROI
- **Senior Technical Team**: Knowledge contribution
- **Contractor Users**: Beta testing, feedback

---

## Budget Summary

### Development Costs
- ML Engineer: £40,000 - £60,000
- Vena SME: £15,000 - £25,000
- Technical Writer: £5,000 - £8,000
- Project Manager: £5,000 - £8,000
- **Total Development: £68,000 - £106,000**

### Annual Operating Costs
- LLM API: £4,000 - £20,000
- Vector database: £1,000 - £5,000
- Application hosting: £1,000 - £3,000
- Monitoring: £500 - £2,000
- **Total Annual: £6,600 - £30,500**

---

## Key Learnings from POC

### What Worked Well
1. ChromaDB was sufficient for POC (10-15 documents)
2. OpenAI GPT-4o provided excellent response quality
3. Streamlit enabled rapid UI development
4. Semantic search found relevant documents even with different terminology

### Challenges Encountered
1. Document chunking strategy needed refinement
2. Some edge cases in code generation
3. Response time optimization needed for production

### Recommendations for Production
1. Use managed vector database (Pinecone) for scalability
2. Implement caching layer (Redis) for common queries
3. Add monitoring from day one
4. Plan for authentication early (Phase 2)
5. Establish knowledge base curation process

---

## Migration Path: POC → Production

### Step 1: Code Migration
- [ ] Copy core RAG logic from POC
- [ ] Refactor for FastAPI backend
- [ ] Add proper error handling
- [ ] Add logging and monitoring

### Step 2: Infrastructure Setup
- [ ] Set up production hosting (Railway/Streamlit Cloud)
- [ ] Configure vector database (Pinecone)
- [ ] Set up PostgreSQL database
- [ ] Configure Redis cache
- [ ] Set up monitoring (Sentry, PostHog)

### Step 3: Knowledge Base Migration
- [ ] Migrate POC knowledge base (10-15 docs)
- [ ] Expand to 50-100 documents (Phase 1 target)
- [ ] Establish content curation process
- [ ] Set up version control for documents

### Step 4: Testing & Deployment
- [ ] Unit tests for core components
- [ ] Integration tests for RAG pipeline
- [ ] User acceptance testing (5 contractors)
- [ ] Performance testing
- [ ] Security testing

---

## Next Steps

1. **Review this context document** with the team
2. **Set up production project structure**
3. **Migrate code from POC**
4. **Set up Jira project for Phase 1** (if not already done)
5. **Begin Phase 1 implementation** (Months 1-2)

---

## Questions to Resolve

1. **Hosting**: Railway vs Streamlit Cloud vs other?
2. **Vector Database**: Pinecone vs Weaviate vs Qdrant Cloud?
3. **Authentication**: Clerk vs Auth0 vs custom?
4. **Frontend**: Keep Streamlit for Phase 1 or move to React?
5. **Knowledge Base**: How to structure for 100+ documents?

---

## Contact & References

- **Project Owner**: Miles Waite
- **Stakeholder**: Martin Bruwer
- **Jira Project**: FRBP (FCS RAG Bot - Phase1)
- **POC Location**: `C:\Users\Miles\Desktop\Projects\Vena\RAG Bot POC`

---

*This document captures all key context from the POC phase. Use it as a reference when building the production system.*

