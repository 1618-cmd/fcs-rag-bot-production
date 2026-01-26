# GDPR Compliance Review and Gap Analysis
**FCS RAG Bot Production**  
**Date:** 21 January 2026

---

## Executive Summary

This document provides a comprehensive GDPR compliance review of the FCS RAG Bot system, identifying current compliance measures, gaps, and recommendations for remediation.

**Overall Status:** Partial compliance - several critical gaps identified

**Priority Actions Required:**
1. Implement data subject rights (access, deletion, portability)
2. Add automatic data retention and deletion
3. Create privacy policy and consent mechanisms
4. Document third-party data processing agreements
5. Implement data breach notification procedures

---

## 1. Personal Data Inventory

### 1.1 Data Currently Collected

#### User Account Data (PostgreSQL - `users` table)
- Email address (personal identifier)
- Full name (optional, personal data)
- Password hash (encrypted, not personal data)
- User ID (UUID)
- Tenant ID (organisation identifier)
- Role (admin, modeler, contributor, viewer)
- Last login timestamp
- Account creation and update timestamps

**Legal Basis:** Contractual necessity (user account management)

#### Query Logs (PostgreSQL - `query_logs` table)
- User ID (personal identifier)
- User email (personal identifier)
- Question text (may contain personal or business information)
- Answer preview and full text (may contain personal or business information)
- Sources list (metadata)
- Timestamp (when query was made)
- Tenant ID (organisation identifier)

**Legal Basis:** Legitimate interest (analytics, system improvement)

#### Authentication Data
- JWT tokens (contain user_id, email, tenant_id, role)
- Session data (stored client-side in localStorage)

**Legal Basis:** Contractual necessity (authentication)

#### Calc Script Data (New Feature)
- Uploaded calc scripts (may contain business-sensitive information)
- File uploads (.docx, .txt files - may contain PII)

**Legal Basis:** Contractual necessity (service delivery)

### 1.2 Data Processed by Third Parties

#### OpenAI (LLM Provider)
- User queries sent to OpenAI API
- Calc scripts sent to OpenAI API
- Generated responses (may contain user data)

**Data Processing Agreement:** Not documented

#### Qdrant Cloud (Vector Database)
- Document embeddings (knowledge base - not personal data)
- Query embeddings (derived from user questions - indirect personal data)

**Data Processing Agreement:** Not documented

#### Sentry (Error Tracking)
- Error logs (may contain user queries, stack traces)
- Performance data (request metadata)

**Data Processing Agreement:** Not documented

#### Render (Hosting Provider)
- Application logs (may contain user data)
- Database backups (contains all personal data)

**Data Processing Agreement:** Check Render terms

#### Vercel (Frontend Hosting)
- Application logs
- Analytics data (if enabled)

**Data Processing Agreement:** Check Vercel terms

#### Redis (Caching)
- Cached queries (contains question text)
- Cached responses (contains answer text)

**Data Processing Agreement:** Check Redis provider terms

---

## 2. GDPR Article Compliance

### Article 5: Principles of Processing

#### Lawfulness, Fairness, and Transparency
**Current State:** Partial compliance

No privacy policy or data processing notice exists. A privacy policy explaining data collection and use should be created.

#### Purpose Limitation
**Current State:** Compliant

Data is collected for user authentication, query logging, and analytics. No evidence of data being used for unrelated purposes.

#### Data Minimisation
**Current State:** Partial compliance

Query logs store full questions and answers, which may contain unnecessary data. Consider anonymisation or truncation for old logs.

#### Accuracy
**Current State:** Compliant

Users can update email and full name via user management API. No mechanism exists for users to correct query log data, which may not be necessary.

#### Storage Limitation
**Current State:** Non-compliant

No automatic deletion of old data is implemented. According to PROJECT_CONTEXT.md, query logs should be retained for 90 days, user accounts for active period plus 30 days, and audit logs for 7 years. Currently, data is stored indefinitely. Automated retention and deletion scripts should be implemented.

#### Integrity and Confidentiality
**Current State:** Partial compliance

HTTPS/TLS is assumed for production (encryption in transit). Encryption at rest has not been verified (check Render/PostgreSQL settings). Access controls include user authentication and role-based access. Encryption at rest for database and backups should be verified.

### Article 6: Lawfulness of Processing

#### Legal Basis Assessment

1. **User Account Data**
   - Basis: Contractual necessity (Article 6(1)(b))
   - Current State: Compliant
   - Justification: Required to provide authentication and access control

2. **Query Logs**
   - Basis: Legitimate interest (Article 6(1)(f))
   - Current State: Needs documentation
   - Justification: Analytics, system improvement, debugging
   - Recommendation: Document legitimate interest assessment (LIA)

3. **Calc Script Analysis**
   - Basis: Contractual necessity (Article 6(1)(b))
   - Current State: Compliant
   - Justification: Core service functionality

### Article 7: Conditions for Consent

**Current State:** Non-compliant

No consent mechanism exists. Missing elements include privacy policy acceptance, cookie consent (if applicable), and data processing consent checkbox. Recommendations: add privacy policy acceptance on registration or login, implement cookie consent banner if using analytics cookies, and document consent in database.

### Article 13/14: Information to be Provided

**Current State:** Non-compliant

No privacy notice exists. Missing information includes: identity of data controller, purpose of processing, legal basis, data retention periods, data subject rights, third-party processors, and international transfers. A comprehensive privacy policy should be created.

### Article 15: Right of Access

**Current State:** Non-compliant

No data subject access request (DSAR) endpoint exists. Users must be able to request all their personal data. Currently, no API endpoint or process exists. Recommendations: create `/api/gdpr/access` endpoint, export user data including account info, query logs, and calc scripts, provide in JSON or CSV format, and respond within 30 days as required by GDPR.

### Article 16: Right to Rectification

**Current State:** Partially compliant

Users can update email and full name via user management API. No mechanism exists to correct query logs, which may not be necessary. It should be documented that query logs are historical records.

### Article 17: Right to Erasure ("Right to be Forgotten")

**Current State:** Non-compliant

Only soft delete is implemented (sets `is_active=False`). Required actions include: hard delete user account data, delete or anonymise query logs, delete cached data, and delete calc scripts. Recommendations: create `/api/gdpr/delete` endpoint, implement cascade deletion, anonymise query logs (keep for analytics but remove PII), and clear Redis cache for user.

### Article 18: Right to Restriction of Processing

**Current State:** Non-compliant

No ability exists to suspend processing while a dispute is resolved. Add `processing_restricted` flag to user table.

### Article 20: Right to Data Portability

**Current State:** Non-compliant

No export functionality exists. Users must be able to export their data in machine-readable format. Recommendations: create `/api/gdpr/export` endpoint, export in JSON or CSV format, and include account data, query logs, and calc scripts.

### Article 21: Right to Object

**Current State:** Non-compliant

Users should be able to object to processing based on legitimate interest. Add opt-out mechanism for query logging if not essential.

### Article 25: Data Protection by Design and by Default

**Current State:** Partial compliance

Good practices implemented include password hashing (bcrypt), JWT authentication, role-based access control, tenant isolation, and input validation. Gaps include: no data minimisation in query logs, no automatic retention or deletion, and no anonymisation options. Data minimisation and retention policies should be implemented.

### Article 30: Records of Processing Activities

**Current State:** Non-compliant

All processing activities must be documented. A processing activities register (ROPA) should be created.

### Article 32: Security of Processing

**Current State:** Partial compliance

Implemented measures include HTTPS/TLS (assumed), password hashing, authentication required, rate limiting, and input validation. Gaps include: encryption at rest not verified, no security monitoring or alerting (Sentry configured but not initialised), no documented security procedures, and no regular security audits. Recommendations: verify encryption at rest, initialise Sentry for security monitoring, document security procedures, and implement security incident response plan.

### Article 33/34: Data Breach Notification

**Current State:** Non-compliant

Required actions include: detect data breaches, notify supervisory authority within 72 hours, and notify affected users if high risk. Recommendations: implement breach detection, create breach notification procedure, and document notification process.

### Article 35: Data Protection Impact Assessment (DPIA)

**Current State:** Non-compliant

A DPIA is required for high-risk processing (per PROJECT_CONTEXT.md). The DPIA document should be completed.

### Article 37: Data Protection Officer (DPO)

**Current State:** Assessment needed

A DPO is required if: large-scale processing, systematic monitoring, or special category data processing occurs. It should be assessed whether a DPO is required.

---

## 3. Data Retention Policies

**Current State:** Not implemented

### Required Policies (from PROJECT_CONTEXT.md):

| Data Type | Required Retention | Current Status |
|-----------|-------------------|----------------|
| Query logs | 90 days | Stored indefinitely |
| Audit logs | 7 years | Not separately tracked |
| User accounts | Active + 30 days | Stored indefinitely |
| Cached queries | 24 hours (TTL) | Implemented |
| Calc scripts | Not specified | Stored in query logs indefinitely |

### Recommendations:

1. **Implement Automated Deletion:**
   ```python
   # Scheduled job to delete old query logs
   DELETE FROM query_logs 
   WHERE created_at < NOW() - INTERVAL '90 days';
   ```

2. **Implement User Account Cleanup:**
   ```python
   # Delete inactive users after 30 days
   DELETE FROM users 
   WHERE is_active = False 
   AND updated_at < NOW() - INTERVAL '30 days';
   ```

3. **Add Retention Configuration:**
   - Add to `config.py`: `query_log_retention_days`, `user_account_retention_days`
   - Create scheduled cleanup script
   - Run daily via cron job or Render scheduled job

---

## 4. Third-Party Data Processors

**Current State:** Agreements not documented

### Third-Party Processors Identified:

| Processor | Data Processed | Location | DPA Status |
|-----------|---------------|----------|------------|
| OpenAI | User queries, calc scripts, responses | USA | Not verified |
| Qdrant Cloud | Query embeddings, document embeddings | EU/USA | Not verified |
| Sentry | Error logs, performance data | USA | Not verified |
| Render | All application data, backups | USA | Check terms |
| Vercel | Frontend logs, analytics | USA | Check terms |
| Redis Provider | Cached queries/responses | Unknown | Check terms |
| PostgreSQL Provider | All database data | Unknown | Check terms |

### Recommendations:

1. **Verify Data Processing Agreements (DPAs):**
   - Check OpenAI DPA (should be available in OpenAI account)
   - Check Qdrant Cloud DPA
   - Check Sentry DPA
   - Check Render terms of service
   - Check Vercel terms of service
   - Document all DPAs in project documentation

2. **International Transfers:**
   - Risk: Data transferred to USA (OpenAI, Sentry, Render, Vercel)
   - Required: Standard Contractual Clauses (SCCs) or adequacy decision
   - Recommendation: Verify all processors have appropriate transfer mechanisms

3. **Create Processor Register:**
   - Document all processors
   - Include: Name, location, data processed, legal basis, safeguards

---

## 5. Data Subject Rights Implementation

**Current State:** Not implemented

### Required Endpoints:

#### 5.1 Right of Access (Article 15)
```python
GET /api/gdpr/access
# Returns: All user's personal data in JSON format
```

**Implementation Required:**
- Export user account data
- Export all query logs for user
- Export calc scripts (if stored separately)
- Format: JSON or CSV
- Response time: Within 30 days

#### 5.2 Right to Erasure (Article 17)
```python
DELETE /api/gdpr/delete
# Deletes: User account, query logs, cached data
```

**Implementation Required:**
- Hard delete user account
- Anonymise or delete query logs
- Clear Redis cache
- Delete calc scripts
- Confirm deletion

#### 5.3 Right to Data Portability (Article 20)
```python
GET /api/gdpr/export
# Returns: Machine-readable export (JSON/CSV)
```

**Implementation Required:**
- Same as access request
- Machine-readable format
- Structured data (JSON preferred)

#### 5.4 Right to Rectification (Article 16)
```python
PUT /api/users/{user_id}
# Already exists - verify it works correctly
```

**Current State:** Partially implemented

#### 5.5 Right to Restriction (Article 18)
```python
POST /api/gdpr/restrict
# Sets processing_restricted flag
```

**Implementation Required:**
- Add `processing_restricted` field to user table
- Block processing when restricted
- Document restriction reason

---

## 6. Security Measures

### Current Implementation:

**Implemented:**
- Password hashing (bcrypt)
- JWT authentication
- Role-based access control
- Tenant isolation
- Input validation
- Rate limiting
- HTTPS/TLS (assumed for production)

**Missing:**
- Encryption at rest verification
- Security monitoring (Sentry not initialised)
- Security incident response plan
- Regular security audits
- Penetration testing (mentioned in requirements, not done)
- Data breach detection
- Access logging and audit trail

### Recommendations:

1. **Verify Encryption at Rest:**
   - Check Render PostgreSQL encryption
   - Check Qdrant Cloud encryption
   - Check Redis encryption
   - Document encryption status

2. **Initialise Sentry:**
   - Already configured, needs initialisation in code
   - Enable security monitoring
   - Set up alerts for suspicious activity

3. **Implement Audit Logging:**
   - Log all data access
   - Log all data modifications
   - Log all GDPR requests (access, deletion, export)
   - Store audit logs separately (7-year retention)

4. **Security Procedures:**
   - Document security incident response
   - Create breach notification procedure
   - Regular security reviews

---

## 7. Privacy Policy and Consent

**Current State:** Not implemented

### Required:

1. **Privacy Policy:**
   - What data is collected
   - Why it is collected (legal basis)
   - How it is used
   - Who it is shared with (third parties)
   - Data retention periods
   - Data subject rights
   - Contact information for DPO/Data Controller
   - International transfers
   - Cookie policy (if applicable)

2. **Consent Mechanism:**
   - Privacy policy acceptance on registration
   - Cookie consent banner (if using analytics)
   - Consent tracking in database
   - Ability to withdraw consent

3. **Data Processing Notice:**
   - Display at point of data collection
   - Clear, plain language
   - Accessible format

### Recommendations:

1. **Create Privacy Policy Document:**
   - Location: `/docs/PRIVACY_POLICY.md`
   - Also: Add to frontend (footer link, registration page)

2. **Implement Consent Tracking:**
   ```python
   # Add to User model
   privacy_policy_accepted: bool
   privacy_policy_accepted_at: DateTime
   cookie_consent: bool
   cookie_consent_at: DateTime
   ```

3. **Add Consent UI:**
   - Privacy policy checkbox on registration
   - Cookie consent banner (if needed)
   - Consent management page

---

## 8. Data Minimisation

**Current State:** Partial

### Issues Identified:

1. **Query Logs Store Full Data:**
   - Stores complete question text (may contain PII)
   - Stores complete answer text (may contain sensitive info)
   - Stores user email (identifiable)

2. **Calc Scripts:**
   - May contain business-sensitive information
   - Stored in query logs or processed in real-time

### Recommendations:

1. **Anonymise Old Query Logs:**
   - After 30 days: Remove user_email, anonymise user_id
   - After 90 days: Delete entirely
   - Keep aggregated analytics (no PII)

2. **Minimise Data Collection:**
   - Consider: Hash user questions instead of storing full text
   - Consider: Store only answer preview, not full answer
   - Consider: Separate PII from query content

3. **Calc Script Handling:**
   - Process in real-time, do not store unless necessary
   - If stored: Encrypt or anonymise
   - Add retention policy for calc scripts

---

## 9. Gap Analysis Summary

### Critical Gaps (Must Fix):

| Gap | Article | Priority | Effort |
|-----|---------|----------|--------|
| No data subject access endpoint | Art. 15 | Critical | Medium |
| No data deletion endpoint | Art. 17 | Critical | Medium |
| No data export endpoint | Art. 20 | Critical | Medium |
| No automatic data retention/deletion | Art. 5(1)(e) | Critical | Medium |
| No privacy policy | Art. 13/14 | Critical | Low |
| No consent mechanism | Art. 7 | Critical | Medium |
| No DPIA completed | Art. 35 | Critical | High |
| Third-party DPAs not verified | Art. 28 | Critical | Low |

### High Priority Gaps:

| Gap | Article | Priority | Effort |
|-----|---------|----------|--------|
| No data breach notification procedure | Art. 33/34 | High | Medium |
| No processing activities register | Art. 30 | High | Low |
| Encryption at rest not verified | Art. 32 | High | Low |
| No restriction of processing | Art. 18 | High | Low |
| No right to object | Art. 21 | High | Low |

### Medium Priority Gaps:

| Gap | Article | Priority | Effort |
|-----|---------|----------|--------|
| Sentry not initialised | Art. 32 | Medium | Low |
| No audit logging | Art. 30 | Medium | Medium |
| No security incident response plan | Art. 32 | Medium | Medium |
| Data minimisation not optimal | Art. 5(1)(c) | Medium | Medium |

---

## 10. Recommendations and Action Plan

### Phase 1: Critical Compliance (Weeks 1-2)

1. **Create Privacy Policy**
   - Write comprehensive privacy policy
   - Add to frontend
   - Link from registration/login

2. **Implement Data Subject Rights Endpoints**
   - `/api/gdpr/access` - Data access request
   - `/api/gdpr/delete` - Data deletion request
   - `/api/gdpr/export` - Data portability export

3. **Implement Data Retention**
   - Create cleanup script
   - Schedule daily execution
   - Test thoroughly

4. **Verify Third-Party DPAs**
   - Check OpenAI DPA
   - Check Qdrant DPA
   - Check Sentry DPA
   - Check Render/Vercel terms
   - Document findings

### Phase 2: High Priority (Weeks 3-4)

5. **Implement Consent Mechanism**
   - Add privacy policy acceptance
   - Track consent in database
   - Add consent management UI

6. **Create Data Breach Procedure**
   - Document breach detection
   - Create notification template
   - Assign responsibilities

7. **Complete DPIA**
   - Document processing activities
   - Assess risks
   - Document mitigation measures

8. **Verify Security**
   - Check encryption at rest
   - Initialise Sentry
   - Document security measures

### Phase 3: Medium Priority (Weeks 5-6)

9. **Implement Additional Rights**
   - Right to restriction
   - Right to object
   - Processing activities register

10. **Enhance Security**
    - Audit logging
    - Security monitoring
    - Incident response plan

11. **Data Minimisation**
    - Review data collection
    - Implement anonymisation
    - Optimise storage

---

## 11. Compliance Checklist

### Legal Basis and Documentation
- [ ] Privacy policy created and published
- [ ] Consent mechanism implemented
- [ ] Legal basis documented for each processing activity
- [ ] Processing activities register (ROPA) created
- [ ] DPIA completed
- [ ] Third-party DPAs verified and documented

### Data Subject Rights
- [ ] Right of access endpoint implemented
- [ ] Right to erasure endpoint implemented
- [ ] Right to data portability endpoint implemented
- [ ] Right to rectification verified working
- [ ] Right to restriction implemented
- [ ] Right to object implemented
- [ ] All rights documented in privacy policy

### Data Protection
- [ ] Data retention policies implemented
- [ ] Automatic deletion scripts created
- [ ] Encryption at rest verified
- [ ] Encryption in transit verified (HTTPS)
- [ ] Access controls implemented
- [ ] Security monitoring active (Sentry)
- [ ] Audit logging implemented

### Breach and Incident Management
- [ ] Data breach detection implemented
- [ ] Breach notification procedure documented
- [ ] Incident response plan created
- [ ] Contact information for DPO/Controller available

### Third-Party Processors
- [ ] All processors identified
- [ ] DPAs verified for all processors
- [ ] International transfers documented
- [ ] Processor register maintained

---

## 12. Next Steps

1. **Immediate Actions:**
   - Review this document with legal/compliance team
   - Prioritise gaps based on risk assessment
   - Assign ownership for each gap

2. **Short-term (1-2 weeks):**
   - Implement critical gaps (data subject rights, retention)
   - Create privacy policy
   - Verify third-party DPAs

3. **Medium-term (1-2 months):**
   - Complete DPIA
   - Implement all data subject rights
   - Enhance security measures

4. **Ongoing:**
   - Regular compliance reviews
   - Security audits
   - Update documentation as system evolves

---

## Appendix: GDPR Articles Reference

- Article 5: Principles of processing
- Article 6: Lawfulness of processing
- Article 7: Conditions for consent
- Article 13/14: Information to be provided
- Article 15: Right of access
- Article 16: Right to rectification
- Article 17: Right to erasure
- Article 18: Right to restriction
- Article 20: Right to data portability
- Article 21: Right to object
- Article 25: Data protection by design
- Article 30: Records of processing
- Article 32: Security of processing
- Article 33/34: Data breach notification
- Article 35: Data Protection Impact Assessment
- Article 37: Data Protection Officer

---

**Document Version:** 1.0  
**Last Updated:** 21 January 2026  
**Next Review:** 21 February 2026
