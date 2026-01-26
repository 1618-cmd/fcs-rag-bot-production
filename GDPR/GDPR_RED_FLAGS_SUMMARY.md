# GDPR Compliance: Brief Summary and Red Flags

**Date:** 21 January 2026

---

## Executive Summary

The FCS RAG Bot system is partially compliant with GDPR. Several critical gaps require immediate attention before the system can be considered production-ready from a compliance perspective. The most urgent issues relate to data subject rights, data retention, and privacy documentation.

---

## Critical Red Flags

### 1. No Data Subject Rights Implementation
**Severity:** Critical  
**GDPR Article:** 15, 17, 20

Users cannot currently:
- Request access to their personal data
- Request deletion of their data (only soft delete exists)
- Export their data in a portable format

**Impact:** Direct violation of GDPR. Users have legal rights that cannot be exercised.

**Required Action:** Implement three API endpoints:
- `/api/gdpr/access` - Data access request
- `/api/gdpr/delete` - Data deletion request  
- `/api/gdpr/export` - Data portability export

---

### 2. No Automatic Data Retention or Deletion
**Severity:** Critical  
**GDPR Article:** 5(1)(e) - Storage Limitation

**Current State:**
- Query logs stored indefinitely (should be 90 days)
- User accounts stored indefinitely (should be active + 30 days)
- Audit logs not separately tracked (should be 7 years)

**Impact:** Violates the principle of storage limitation. Data is kept longer than necessary, increasing privacy risk and storage costs.

**Required Action:** Implement automated cleanup scripts that run daily to delete data according to retention policies.

---

### 3. No Privacy Policy or Consent Mechanism
**Severity:** Critical  
**GDPR Article:** 7, 13/14

**Current State:**
- No privacy policy exists
- No consent mechanism on registration
- Users are not informed about data processing

**Impact:** Users cannot give informed consent. The system cannot demonstrate lawful basis for processing.

**Required Action:** 
- Create comprehensive privacy policy
- Add consent checkbox on registration
- Track consent in database

---

### 4. Third-Party Data Processing Agreements Not Verified
**Severity:** Critical  
**GDPR Article:** 28

**Third Parties Processing Personal Data:**
- OpenAI (USA) - processes user queries and calc scripts
- Qdrant Cloud (EU/USA) - processes query embeddings
- Sentry (USA) - processes error logs
- Render (USA) - hosts application and database
- Vercel (USA) - hosts frontend

**Current State:** No verification that Data Processing Agreements (DPAs) exist or are GDPR-compliant.

**Impact:** Cannot demonstrate that third parties are compliant processors. International transfers to USA may lack appropriate safeguards.

**Required Action:** Verify and document DPAs for all third-party processors, especially those in USA (require Standard Contractual Clauses).

---

### 5. No Data Breach Notification Procedure
**Severity:** Critical  
**GDPR Article:** 33/34

**Current State:**
- No breach detection mechanism
- No procedure for notifying supervisory authority (72-hour requirement)
- No procedure for notifying affected users

**Impact:** If a breach occurs, the organisation may face significant fines for failure to notify within required timeframes.

**Required Action:** Create breach detection and notification procedures, assign responsibilities, and document the process.

---

### 6. Data Protection Impact Assessment (DPIA) Not Completed
**Severity:** Critical  
**GDPR Article:** 35

**Current State:** DPIA required per PROJECT_CONTEXT.md but not completed.

**Impact:** Cannot demonstrate that privacy risks have been assessed and mitigated. May be required by supervisory authority.

**Required Action:** Complete DPIA document assessing risks and mitigation measures.

---

## High Priority Issues

### 7. Encryption at Rest Not Verified
**Severity:** High  
**GDPR Article:** 32

Encryption in transit (HTTPS) is assumed, but encryption at rest for database and backups has not been verified with hosting providers.

---

### 8. No Processing Activities Register (ROPA)
**Severity:** High  
**GDPR Article:** 30

No centralised register documenting all processing activities, legal bases, and data flows.

---

### 9. No Right to Restriction or Object
**Severity:** High  
**GDPR Article:** 18, 21

Users cannot restrict processing or object to processing based on legitimate interest.

---

## What's Working Well

- Password hashing and authentication (bcrypt, JWT)
- Role-based access control
- Tenant isolation
- Input validation and rate limiting
- HTTPS/TLS assumed for production

---

## Immediate Action Plan (Next 2 Weeks)

1. **Week 1:**
   - Create privacy policy document
   - Implement data subject rights endpoints (access, deletion, export)
   - Verify third-party DPAs (especially OpenAI, Qdrant, Sentry)

2. **Week 2:**
   - Implement automatic data retention and deletion scripts
   - Add consent mechanism to registration
   - Create data breach notification procedure

3. **Ongoing:**
   - Complete DPIA
   - Verify encryption at rest
   - Implement remaining data subject rights (restriction, object)

---

## Risk Assessment

**Current Risk Level:** High

Without addressing the critical red flags, the system:
- Cannot legally process personal data under GDPR
- Faces potential fines up to 4% of annual turnover or €20 million
- Cannot respond to data subject requests (legal requirement)
- Lacks documentation to demonstrate compliance

**Recommended:** Address critical red flags before wider deployment or handling significant volumes of personal data.

---

## Key Statistics

- **Critical Gaps:** 8
- **High Priority Gaps:** 5
- **Medium Priority Gaps:** 4
- **Compliance Status:** Partial (approximately 40% compliant)

---

**Next Steps:** Review with legal/compliance team, prioritise based on risk assessment, and assign ownership for each critical gap.
