# Processor Register
## FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Quarterly or when processors change  
**Next Review:** April 2026

---

## 1. Purpose

This register documents all third-party data processors used by the FCS RAG Bot system, in compliance with Article 28 of the GDPR. It tracks Data Processing Agreement (DPA) status, international transfer safeguards, and processor security assessments.

**Legal Requirement:** Article 28 GDPR requires that processors are bound by data processing agreements and that appropriate safeguards are in place for international transfers.

---

## 2. Processor Register

### 2.1 OpenAI

**Processor Details:**
- **Name:** OpenAI, L.L.C.
- **Location:** United States (San Francisco, California)
- **Website:** https://openai.com
- **Contact:** [OpenAI Support / DPA Contact]

**Data Processed:**
- User queries submitted to the RAG Bot
- Uploaded calculation scripts (VenaQL code)
- Generated responses (may contain user data)
- Query embeddings (derived from user queries)

**Processing Purpose:**
- Generate responses to user queries using GPT-4o language model
- Analyse and explain calculation scripts
- Create embeddings for semantic search

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (core service functionality)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check OpenAI account settings]
- **DPA Available:** Yes (OpenAI provides DPA for business customers)
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [Where DPA is stored/document reference]

**International Transfers:**
- **Transfer Location:** United States
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs)
- **SCCs Status:** [To be verified - Check if included in DPA]
- **Additional Safeguards:** Data Processing Agreement
- **Data Residency Options:** [Check if EU data residency available]

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest
- Access controls and authentication
- Security monitoring
- SOC 2 Type II certified
- Regular security assessments

**Risk Assessment:**
- **Risk Level:** Medium-High (US-based, processes user queries)
- **Mitigation:** DPA, SCCs, security certifications, data minimisation (send only necessary data)
- **Review Date:** [Date]

**Review Notes:**
- [Notes from DPA review]
- [Any concerns or issues identified]
- [Actions taken or required]

---

### 2.2 Qdrant Cloud

**Processor Details:**
- **Name:** Qdrant Cloud
- **Location:** European Union / United States (depending on cluster location)
- **Website:** https://cloud.qdrant.io
- **Contact:** [Qdrant Support / DPA Contact]
- **Cluster Location:** [EU/US - to be confirmed]

**Data Processed:**
- Document embeddings (from knowledge base documents - not personal data)
- Query embeddings (derived from user queries - indirect personal data)
- Vector search metadata

**Processing Purpose:**
- Store document embeddings for semantic search
- Store query embeddings for similarity matching
- Enable RAG (Retrieval-Augmented Generation) functionality

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (core service functionality)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check Qdrant Cloud account]
- **DPA Available:** [To be verified]
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [Where DPA is stored/document reference]

**International Transfers:**
- **Transfer Location:** [EU or US - depends on cluster]
- **Transfer Mechanism:** 
  - If EU cluster: No transfer (data stays in EU)
  - If US cluster: Standard Contractual Clauses (SCCs) required
- **SCCs Status:** [To be verified if US cluster]
- **Data Residency:** [Verify cluster location and data residency options]

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest
- Access controls (API key authentication)
- Security monitoring
- [Additional security measures to be verified]

**Risk Assessment:**
- **Risk Level:** 
  - EU cluster: Low-Medium
  - US cluster: Medium (if transfer occurs)
- **Mitigation:** DPA, SCCs (if US), data residency selection (prefer EU)
- **Review Date:** [Date]

**Review Notes:**
- [Notes from DPA review]
- [Cluster location confirmation]
- [Actions taken or required]

---

### 2.3 Render (Hosting Provider)

**Processor Details:**
- **Name:** Render, Inc.
- **Location:** United States
- **Website:** https://render.com
- **Contact:** [Render Support / DPA Contact]

**Data Processed:**
- All application data (user accounts, query logs)
- Database backups
- Application logs (may contain user queries, error messages)
- Infrastructure logs

**Processing Purpose:**
- Hosting backend application
- Database hosting (PostgreSQL)
- Application and infrastructure monitoring
- Backup storage

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (infrastructure hosting)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check Render terms of service]
- **DPA Available:** [To be verified - May be in terms of service]
- **DPA Signed:** [Yes/No/Pending - May be automatic via terms acceptance]
- **DPA Date:** [Date if applicable]
- **DPA Location:** [Terms of service / separate DPA]

**International Transfers:**
- **Transfer Location:** United States
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs)
- **SCCs Status:** [To be verified - Check if in terms of service]
- **Additional Safeguards:** Terms of service, security measures

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest (to be verified)
- Access controls
- Security monitoring
- [Additional security measures to be verified]

**Risk Assessment:**
- **Risk Level:** Medium (US-based, hosts all application data)
- **Mitigation:** DPA/SCCs, encryption, access controls, regular backups
- **Review Date:** [Date]

**Review Notes:**
- [Notes from terms review]
- [Verification of encryption at rest]
- [Actions taken or required]

---

### 2.4 Vercel (Frontend Hosting)

**Processor Details:**
- **Name:** Vercel, Inc.
- **Location:** United States
- **Website:** https://vercel.com
- **Contact:** [Vercel Support / DPA Contact]

**Data Processed:**
- Frontend application code
- Application logs (may contain user interactions)
- Analytics data (if enabled)
- Build and deployment logs

**Processing Purpose:**
- Hosting frontend application
- Application deployment and builds
- Logging and monitoring

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (infrastructure hosting)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check Vercel terms of service]
- **DPA Available:** [To be verified]
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if applicable]
- **DPA Location:** [Terms of service / separate DPA]

**International Transfers:**
- **Transfer Location:** United States
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs)
- **SCCs Status:** [To be verified]
- **Additional Safeguards:** Terms of service

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Security monitoring
- [Additional security measures to be verified]

**Risk Assessment:**
- **Risk Level:** Low-Medium (frontend hosting, limited personal data)
- **Mitigation:** DPA/SCCs, encryption, access controls
- **Review Date:** [Date]

**Review Notes:**
- [Notes from terms review]
- [Actions taken or required]

---

### 2.5 Sentry (Error Tracking)

**Processor Details:**
- **Name:** Functional Software, Inc. (Sentry)
- **Location:** United States
- **Website:** https://sentry.io
- **Contact:** [Sentry Support / DPA Contact]

**Data Processed:**
- Error logs and stack traces (may contain query fragments, user identifiers)
- Performance data
- Application monitoring data
- User session data (if enabled)

**Processing Purpose:**
- Error tracking and debugging
- Performance monitoring
- Application health monitoring
- Security event detection

**Legal Basis for Processing:**
- Article 6(1)(f) GDPR - Legitimate interest (system monitoring and improvement)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check Sentry account settings]
- **DPA Available:** [To be verified - Sentry typically provides DPA]
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [Where DPA is stored/document reference]

**International Transfers:**
- **Transfer Location:** United States
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs)
- **SCCs Status:** [To be verified]
- **Additional Safeguards:** Data Processing Agreement

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest
- Access controls
- Security monitoring
- SOC 2 Type II certified (to be verified)

**Risk Assessment:**
- **Risk Level:** Medium (US-based, processes error logs that may contain user data)
- **Mitigation:** DPA, SCCs, data minimisation (sanitise logs before sending), security certifications
- **Review Date:** [Date]

**Review Notes:**
- [Notes from DPA review]
- [Consider data sanitisation before sending to Sentry]
- [Actions taken or required]

---

### 2.6 AWS S3 (Document Storage)

**Processor Details:**
- **Name:** Amazon Web Services, Inc.
- **Location:** United States (or EU region if configured)
- **Website:** https://aws.amazon.com
- **Contact:** [AWS Support / DPA Contact]
- **Region:** [US/EU - to be confirmed]

**Data Processed:**
- Document files (knowledge base documents)
- Uploaded documents (staging, approved, archived)
- Document metadata

**Processing Purpose:**
- Store knowledge base documents
- Manage document approval workflow (staging, approved, archive)
- Document versioning and backup

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (document storage)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified - Check AWS account]
- **DPA Available:** Yes (AWS provides DPA)
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [AWS account / document reference]

**International Transfers:**
- **Transfer Location:** [US or EU - depends on region]
- **Transfer Mechanism:** 
  - If EU region: No transfer (data stays in EU)
  - If US region: Standard Contractual Clauses (SCCs) required
- **SCCs Status:** [To be verified if US region]
- **Data Residency:** [Verify region and consider EU region if possible]

**Security Measures (Processor):**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest (S3 encryption)
- Access controls (IAM, bucket policies)
- Security monitoring
- SOC 2, ISO 27001 certified

**Risk Assessment:**
- **Risk Level:** 
  - EU region: Low-Medium
  - US region: Medium
- **Mitigation:** DPA, SCCs (if US), encryption, access controls, prefer EU region
- **Review Date:** [Date]

**Review Notes:**
- [Notes from DPA review]
- [Region confirmation - consider EU region]
- [Actions taken or required]

---

### 2.7 Redis Provider

**Processor Details:**
- **Name:** [Redis Provider Name - e.g., Render Redis, AWS ElastiCache, etc.]
- **Location:** [Location - depends on provider]
- **Website:** [Provider Website]
- **Contact:** [Provider Support]

**Data Processed:**
- Cached queries (user questions)
- Cached responses (generated answers)
- Cache metadata

**Processing Purpose:**
- Improve response times through caching
- Reduce API calls to OpenAI
- Performance optimisation

**Legal Basis for Processing:**
- Article 6(1)(f) GDPR - Legitimate interest (performance optimisation)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified]
- **DPA Available:** [To be verified]
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [Where DPA is stored]

**International Transfers:**
- **Transfer Location:** [Location - depends on provider]
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs) if outside EEA
- **SCCs Status:** [To be verified if outside EEA]
- **TTL:** 24 hours (automatic expiration)

**Security Measures (Processor):**
- Encryption in transit (to be verified)
- Encryption at rest (to be verified)
- Access controls
- [Additional security measures to be verified]

**Risk Assessment:**
- **Risk Level:** Low-Medium (cached data, short TTL)
- **Mitigation:** DPA/SCCs (if required), encryption, short TTL (24 hours)
- **Review Date:** [Date]

**Review Notes:**
- [Notes from provider review]
- [TTL verification]
- [Actions taken or required]

---

### 2.8 PostgreSQL Provider

**Processor Details:**
- **Name:** [PostgreSQL Provider - e.g., Render Postgres, AWS RDS, etc.]
- **Location:** [Location - depends on provider]
- **Website:** [Provider Website]
- **Contact:** [Provider Support]

**Data Processed:**
- All database data (user accounts, query logs, all personal data)
- Database backups

**Processing Purpose:**
- Primary data storage
- Database hosting and management
- Backup storage

**Legal Basis for Processing:**
- Article 6(1)(b) GDPR - Contractual necessity (data storage)

**Data Processing Agreement (DPA) Status:**
- **Status:** [To be verified]
- **DPA Available:** [To be verified]
- **DPA Signed:** [Yes/No/Pending]
- **DPA Date:** [Date if signed]
- **DPA Location:** [Where DPA is stored]

**International Transfers:**
- **Transfer Location:** [Location - depends on provider]
- **Transfer Mechanism:** Standard Contractual Clauses (SCCs) if outside EEA
- **SCCs Status:** [To be verified if outside EEA]

**Security Measures (Processor):**
- Encryption in transit (to be verified)
- Encryption at rest (to be verified)
- Access controls
- Backup encryption
- [Additional security measures to be verified]

**Risk Assessment:**
- **Risk Level:** High (stores all personal data)
- **Mitigation:** DPA/SCCs (if required), encryption at rest and in transit, access controls, regular backups
- **Review Date:** [Date]

**Review Notes:**
- [Notes from provider review]
- [Encryption verification critical]
- [Actions taken or required]

---

## 3. Summary and Status

### 3.1 DPA Status Summary

| Processor | DPA Status | Priority | Risk Level | Action Required |
|-----------|------------|----------|------------|------------------|
| OpenAI | [To be verified] | Critical | High | Verify and sign DPA |
| Qdrant Cloud | [To be verified] | High | Medium | Verify DPA, confirm cluster location |
| Render | [To be verified] | Critical | High | Verify DPA/SCCs in terms |
| Vercel | [To be verified] | Medium | Low-Medium | Verify DPA/SCCs |
| Sentry | [To be verified] | High | Medium | Verify and sign DPA |
| AWS S3 | [To be verified] | High | Medium | Verify DPA, consider EU region |
| Redis Provider | [To be verified] | Medium | Low-Medium | Verify DPA/SCCs |
| PostgreSQL Provider | [To be verified] | Critical | High | Verify DPA/SCCs, encryption |

### 3.2 International Transfer Summary

**Processors Outside EEA:**
- OpenAI (United States) - Critical
- Render (United States) - Critical
- Vercel (United States) - Medium
- Sentry (United States) - High
- AWS S3 (United States, unless EU region) - High
- [Redis Provider] - [Location dependent]
- [PostgreSQL Provider] - [Location dependent]

**Safeguards Required:**
- Standard Contractual Clauses (SCCs) for all US transfers
- Data Processing Agreements (DPAs) for all processors
- Verification of safeguards in place

### 3.3 Action Items

**Immediate (Before Go-Live):**
1. Verify and sign OpenAI DPA (Critical)
2. Verify Render DPA/SCCs (Critical)
3. Verify PostgreSQL Provider DPA/SCCs (Critical)
4. Verify Qdrant DPA and confirm cluster location (High)

**Short-Term (Within 1 Month):**
5. Verify Sentry DPA (High)
6. Verify AWS S3 DPA and consider EU region (High)
7. Verify Vercel DPA/SCCs (Medium)
8. Verify Redis Provider DPA/SCCs (Medium)

**Ongoing:**
9. Quarterly review of all processors
10. Monitor for processor changes
11. Update register when processors change
12. Regular security assessments of processors

---

## 4. Review and Maintenance

**Review Schedule:**
- Quarterly review of all processors
- Review when adding new processors
- Review when processor agreements change
- Review when security incidents occur at processors

**Update Triggers:**
- New processor added
- Processor agreement changes
- Processor security incident
- Processor location changes
- DPA status changes

**Last Updated:** January 2026  
**Next Review:** April 2026  
**Document Owner:** Miles Waite

---

## Appendix A: DPA Verification Checklist

For each processor, verify:

- [ ] DPA is available (check provider website, account settings, or contact support)
- [ ] DPA is signed or accepted (via terms of service or separate agreement)
- [ ] DPA location is documented (where it is stored or how to access it)
- [ ] DPA date is recorded (when it was signed or accepted)
- [ ] SCCs are included in DPA or terms (for international transfers)
- [ ] Processor security measures are documented
- [ ] Risk assessment is completed
- [ ] Review date is set

---

## Appendix B: International Transfer Safeguards

**Standard Contractual Clauses (SCCs):**
- European Commission approved SCCs for data transfers
- Must be included in DPA or separate agreement
- Verify which version of SCCs (2021 version is current)

**Adequacy Decisions:**
- Some countries have adequacy decisions (no SCCs needed)
- United States does not have adequacy decision
- Verify if processor is in country with adequacy decision

**Other Safeguards:**
- Binding Corporate Rules (BCRs) - for multinational companies
- Certification schemes - verify if processor is certified
- Codes of conduct - verify if applicable

---

**Document Owner:** Miles Waite  
**Last Updated:** January 2026  
**Next Review:** April 2026
