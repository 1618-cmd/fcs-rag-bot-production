# GDPR Compliance Business Requirements Document

**Document Version:** 1.0  
**Date:** January 2026  
**Status:** Draft for Review

## Executive Summary

This document outlines the business requirements for achieving GDPR compliance in the FCS RAG Bot system. The requirements are derived from the commitments made in the Privacy Policy and the gaps identified in the current system implementation.

The requirements are prioritised into three phases: Critical (must be implemented before Privacy Policy publication), High Priority (within one month), and Medium Priority (within three months). Failure to implement critical requirements before publishing the Privacy Policy creates significant legal and reputational risk.

## 1. Background and Context

The FCS RAG Bot system processes personal data including user account information, query logs, and uploaded calculation scripts. A Privacy Policy has been drafted that commits to specific data handling practices and user rights under GDPR.

A compliance review has identified gaps between the Privacy Policy commitments and the current system implementation. This document specifies the business requirements to bridge those gaps and ensure the system can deliver on its privacy commitments.

## 2. Critical Requirements (Phase 1)

### 2.1 Data Subject Rights Implementation

**Requirement ID:** REQ-001  
**Priority:** Critical  
**GDPR Article:** 15, 17, 20

**Business Need:**  
Users must be able to exercise their fundamental GDPR rights: access to their data, deletion of their data, and export of their data in a portable format. The Privacy Policy explicitly commits to these rights, and failure to provide them creates legal liability.

**Requirements:**

1. **Right of Access (Article 15)**
   - The system must provide an endpoint that allows authenticated users to request all personal data held about them
   - The response must include: account information, all query logs associated with the user, any uploaded calculation scripts, and authentication history
   - Data must be provided in a human-readable format (JSON or CSV)
   - Response must be provided within 30 days of request, as required by GDPR

2. **Right to Erasure (Article 17)**
   - The system must provide an endpoint that allows authenticated users to request deletion of their personal data
   - Deletion must include: user account, all associated query logs, cached data in Redis, and any uploaded files
   - Query logs may be anonymised rather than deleted if they are required for aggregated analytics (user_id and user_email removed, but query content retained in anonymised form)
   - Deletion must be verifiable and irreversible (hard delete, not soft delete)
   - System must confirm deletion to the user

3. **Right to Data Portability (Article 20)**
   - The system must provide an endpoint that exports user data in a structured, machine-readable format
   - Export format must be JSON or CSV
   - Export must include all data provided in access requests
   - Data must be structured to enable transfer to another service provider

**Acceptance Criteria:**
- All three endpoints are accessible to authenticated users
- Endpoints return complete data sets within 30 days
- Deletion requests are fully processed and verified
- Export format is machine-readable and complete
- All endpoints are documented and tested

**Business Impact:**  
High. Without these capabilities, the organisation cannot fulfil its legal obligations under GDPR, creating significant legal and regulatory risk. Users may file complaints with supervisory authorities if they cannot exercise their rights.

### 2.2 Automated Data Retention and Deletion

**Requirement ID:** REQ-002  
**Priority:** Critical  
**GDPR Article:** 5(1)(e)

**Business Need:**  
The Privacy Policy commits to specific data retention periods: query logs for 90 days, user accounts for active period plus 30 days, and cached data for 24 hours. Currently, data is stored indefinitely, creating a direct contradiction between policy and practice.

**Requirements:**

1. **Query Log Retention**
   - Query logs must be automatically deleted 90 days after creation
   - Deletion must occur daily via automated process
   - Process must be auditable and logged
   - Exception: audit logs (security events, access logs) must be retained for 7 years for legal compliance

2. **User Account Retention**
   - Active user accounts must be retained while the account is active
   - Inactive accounts (where is_active = False) must be retained for 30 days after deactivation
   - After 30 days, inactive accounts must be permanently deleted
   - Deletion must cascade to associated query logs (unless already deleted per retention policy)

3. **Cached Data Retention**
   - Redis cache entries must have a maximum TTL of 24 hours
   - Cache must automatically expire after 24 hours
   - No manual intervention required

4. **Retention Process**
   - Automated job must run daily to enforce retention policies
   - Process must be scheduled and monitored
   - Failures must be logged and alert administrators
   - Process must be idempotent (safe to run multiple times)

**Acceptance Criteria:**
- Query logs older than 90 days are automatically deleted
- Inactive user accounts are deleted 30 days after deactivation
- Cache entries expire after 24 hours
- Retention process runs daily without manual intervention
- All deletions are logged for audit purposes

**Business Impact:**  
Critical. The Privacy Policy explicitly commits to these retention periods. Failure to implement automated deletion means the organisation is not delivering on its published commitments, creating legal and compliance risk.

### 2.3 Consent Mechanism

**Requirement ID:** REQ-003  
**Priority:** Critical  
**GDPR Article:** 7

**Business Need:**  
The Privacy Policy states that users acknowledge reading and understanding the policy by using the service. However, there is no mechanism to track or record this consent, making it impossible to prove consent if challenged.

**Requirements:**

1. **Consent Tracking**
   - Database must store: privacy_policy_accepted (boolean), privacy_policy_accepted_at (timestamp), privacy_policy_version (string)
   - Consent must be recorded when user first accesses the service or when policy is updated
   - Consent must be linked to specific policy version

2. **User Interface**
   - Registration or first login must display Privacy Policy acceptance checkbox
   - Checkbox must link to full Privacy Policy document
   - User cannot proceed without accepting policy
   - Acceptance must be clearly recorded and timestamped

3. **Policy Versioning**
   - System must track which version of Privacy Policy user accepted
   - When policy is updated, users must be notified and may need to re-consent (depending on nature of changes)
   - Version history must be maintained

4. **Existing Users**
   - Users who registered before consent mechanism must be handled
   - Options: require consent on next login, or document that consent was implied by continued use
   - Legal review recommended for approach

**Acceptance Criteria:**
- All new users must accept Privacy Policy before accessing service
- Consent is recorded with timestamp and version
- Policy versioning is tracked
- Existing users are handled appropriately
- Consent can be audited and verified

**Business Impact:**  
High. Without consent tracking, the organisation cannot demonstrate that users consented to data processing, which is required for certain processing activities. This creates legal risk if consent is challenged.

### 2.4 Third-Party Data Processing Agreement Verification

**Requirement ID:** REQ-004  
**Priority:** Critical  
**GDPR Article:** 28

**Business Need:**  
The Privacy Policy states that all third-party processors are bound by data processing agreements. However, these agreements have not been verified, and the status is unknown. This creates risk if processors are not compliant.

**Requirements:**

1. **Processor Register**
   - Document must be created listing all third-party processors
   - For each processor, record: name, location, data processed, DPA status, international transfer safeguards
   - Register must be maintained and updated

2. **DPA Verification**
   - Verify DPA status for: OpenAI, Qdrant Cloud, Render, Vercel, Sentry, AWS S3, Redis provider, PostgreSQL provider
   - Document DPA status (signed, in progress, not available)
   - For processors without DPAs, assess risk and document mitigation

3. **International Transfers**
   - Identify all processors located outside EEA (particularly United States)
   - Verify appropriate safeguards are in place (Standard Contractual Clauses, adequacy decisions)
   - Document transfer mechanisms for each processor

4. **Documentation**
   - Create processor register document
   - Document DPA status and transfer mechanisms
   - Review and update quarterly

**Acceptance Criteria:**
- Processor register is complete and accurate
- DPA status is verified for all critical processors (OpenAI, hosting providers)
- International transfer safeguards are documented
- Register is maintained and reviewed regularly

**Business Impact:**  
High. The Privacy Policy commits to DPAs with all processors. If processors do not have appropriate agreements, the organisation may be in breach of GDPR requirements for processor relationships.

## 3. High Priority Requirements (Phase 2)

### 3.1 Right to Restriction of Processing

**Requirement ID:** REQ-005  
**Priority:** High  
**GDPR Article:** 18

**Business Need:**  
Users have the right to request restriction of processing in certain circumstances (e.g., contesting data accuracy, objecting to processing). The system must be able to honour these requests.

**Requirements:**

1. **Restriction Mechanism**
   - User table must include processing_restricted (boolean) field
   - When restricted, user queries must be blocked or processing suspended
   - Reason for restriction must be recorded
   - Restriction must be reversible by administrator

2. **User Interface**
   - Users must be able to request restriction through support channels
   - Administrators must be able to apply and lift restrictions
   - Users must be notified when restriction is applied or lifted

3. **Processing Logic**
   - System must check restriction status before processing queries
   - Restricted users should receive clear message explaining restriction
   - Admin override capability for legitimate business needs

**Acceptance Criteria:**
- Restriction can be applied to user accounts
- Restricted users cannot submit queries
- Restriction reason is recorded
- Administrators can manage restrictions
- Users are notified of restriction status

**Business Impact:**  
Medium. This right is less commonly exercised but must be available when requested. Failure to provide it creates compliance risk.

### 3.2 Right to Object

**Requirement ID:** REQ-006  
**Priority:** High  
**GDPR Article:** 21

**Business Need:**  
Users have the right to object to processing based on legitimate interests. For query logging, users may object if logging is not essential for service delivery.

**Requirements:**

1. **Objection Mechanism**
   - Users must be able to object to query logging (if not essential)
   - Alternative: queries are anonymised immediately (user_id removed) rather than stored with personal identifiers
   - Objection must be recorded and honoured

2. **Impact Assessment**
   - Assess whether query logging is essential for service delivery
   - If essential, document why objection cannot be honoured
   - If not essential, provide anonymisation option

3. **Implementation**
   - If objection is allowed: implement immediate anonymisation of query logs
   - User_id and user_email must be removed at point of logging
   - Query content may be retained for analytics in anonymised form

**Acceptance Criteria:**
- Users can object to query logging
- Objections are recorded and processed
- Anonymisation is implemented if objection is honoured
- Impact on analytics is documented

**Business Impact:**  
Medium. This right must be available, but the business impact depends on whether query logging is considered essential. If logging is essential, the organisation may continue processing but must document the legitimate interest override.

### 3.3 Data Breach Notification Procedures

**Requirement ID:** REQ-007  
**Priority:** High  
**GDPR Article:** 33, 34

**Business Need:**  
GDPR requires notification of data breaches to supervisory authorities within 72 hours and to affected users if high risk. The organisation must have procedures to detect, assess, and notify breaches.

**Requirements:**

1. **Breach Detection**
   - System must monitor for unauthorised access, data leaks, security incidents
   - Automated alerts for suspicious activity
   - Logging and monitoring must enable breach detection

2. **Breach Assessment**
   - Procedure to assess whether breach occurred
   - Procedure to assess severity and risk to individuals
   - Decision framework for notification requirements

3. **Notification Procedures**
   - Template for supervisory authority notification (72-hour requirement)
   - Template for user notification (if high risk)
   - Process for identifying and contacting affected users
   - Escalation procedures for breach response

4. **Documentation**
   - Breach response procedure document
   - Incident response plan
   - Contact information for supervisory authority
   - Roles and responsibilities defined

**Acceptance Criteria:**
- Breach detection mechanisms are in place
- Breach assessment procedure is documented
- Notification templates are prepared
- Response procedures are documented and tested
- Key personnel are trained on procedures

**Business Impact:**  
High. Data breaches can result in significant fines and reputational damage. Having procedures in place is essential for compliance and risk management.

### 3.4 Security Verification and Documentation

**Requirement ID:** REQ-008  
**Priority:** High  
**GDPR Article:** 32

**Business Need:**  
The Privacy Policy lists security measures including encryption, access controls, and monitoring. These measures must be verified and documented to demonstrate compliance.

**Requirements:**

1. **Encryption Verification**
   - Verify encryption at rest for: PostgreSQL database, Redis cache, AWS S3 storage
   - Verify encryption in transit (HTTPS/TLS) for all connections
   - Document encryption status and mechanisms

2. **Access Controls**
   - Verify authentication and authorisation controls are implemented
   - Verify role-based access control is functioning
   - Document access control mechanisms

3. **Security Monitoring**
   - Verify Sentry error tracking is operational
   - Implement security event logging
   - Document monitoring and alerting mechanisms

4. **Security Documentation**
   - Create security measures document
   - Document all technical and organisational measures
   - Review and update security documentation regularly

**Acceptance Criteria:**
- Encryption is verified for all data storage
- Access controls are documented and verified
- Security monitoring is operational
- Security documentation is complete and current

**Business Impact:**  
High. Security measures are a core GDPR requirement. Documentation demonstrates compliance and helps identify gaps.

## 4. Medium Priority Requirements (Phase 3)

### 4.1 Processing Activities Register (ROPA)

**Requirement ID:** REQ-009  
**Priority:** Medium  
**GDPR Article:** 30

**Business Need:**  
GDPR requires organisations to maintain a record of processing activities documenting all personal data processing. This is an internal compliance requirement.

**Requirements:**

1. **ROPA Document**
   - Create comprehensive record of processing activities
   - Include: purposes of processing, categories of data subjects, categories of personal data, recipients, retention periods, security measures
   - Format: spreadsheet or structured document

2. **Maintenance**
   - Review and update ROPA quarterly
   - Update when system changes affect processing activities
   - Maintain version history

3. **Completeness**
   - All processing activities must be documented
   - Legal basis for each activity must be specified
   - Third-party processors must be listed

**Acceptance Criteria:**
- ROPA document is complete and accurate
- All processing activities are documented
- ROPA is maintained and updated regularly
- Document is available for supervisory authority review

**Business Impact:**  
Medium. ROPA is required for compliance but is primarily internal documentation. It helps demonstrate compliance and identify processing activities.

### 4.2 Data Minimisation Review

**Requirement ID:** REQ-010  
**Priority:** Medium  
**GDPR Article:** 5(1)(c)

**Business Need:**  
GDPR requires data minimisation: only collect and process data that is necessary. Current query logs store full questions and answers, which may exceed what is necessary.

**Requirements:**

1. **Data Collection Review**
   - Review what data is collected in query logs
   - Assess whether full question/answer text is necessary
   - Consider alternatives: previews, hashes, anonymisation

2. **Minimisation Implementation**
   - If full text is not necessary, implement minimisation
   - Options: store only previews, hash questions, anonymise after 30 days
   - Balance functionality needs with minimisation

3. **Documentation**
   - Document data minimisation decisions
   - Justify any data collection that may seem excessive
   - Review periodically

**Acceptance Criteria:**
- Data collection is reviewed for minimisation
- Unnecessary data collection is eliminated or minimised
- Decisions are documented and justified
- Review is conducted periodically

**Business Impact:**  
Medium. Data minimisation reduces risk and storage costs. However, full query logs may be necessary for debugging and analytics, requiring careful balance.

### 4.3 Audit Logging

**Requirement ID:** REQ-011  
**Priority:** Medium  
**GDPR Article:** 30, 32

**Business Need:**  
Audit logs are required to track data access, modifications, and security events. These logs must be retained for 7 years for compliance purposes.

**Requirements:**

1. **Audit Log Implementation**
   - Log all data access (who accessed what data, when)
   - Log all data modifications (who changed what, when)
   - Log all GDPR requests (access, deletion, export requests)
   - Log security events and administrative actions

2. **Log Storage**
   - Audit logs must be stored separately from application logs
   - Logs must be tamper-evident
   - Retention: 7 years as specified in Privacy Policy

3. **Log Access**
   - Audit logs must be accessible to administrators
   - Access to audit logs must itself be logged
   - Logs must be searchable and queryable

**Acceptance Criteria:**
- All data access is logged
- All data modifications are logged
- GDPR requests are logged
- Audit logs are retained for 7 years
- Logs are accessible and searchable

**Business Impact:**  
Medium. Audit logs are essential for security and compliance but are primarily operational. They help detect breaches and demonstrate compliance.

### 4.4 Data Protection Impact Assessment (DPIA)

**Requirement ID:** REQ-012  
**Priority:** Medium  
**GDPR Article:** 35

**Business Need:**  
A DPIA is required for high-risk processing activities. The system processes personal data using AI/ML technologies, which may constitute high-risk processing.

**Requirements:**

1. **DPIA Completion**
   - Complete DPIA document assessing risks of processing
   - Identify risks to data subjects
   - Document mitigation measures
   - Review with data protection officer or legal counsel

2. **Risk Assessment**
   - Assess risks of: AI processing, data storage, third-party processors, international transfers
   - Document likelihood and impact of risks
   - Identify residual risks after mitigation

3. **Mitigation Measures**
   - Document existing security and privacy measures
   - Identify additional measures if needed
   - Implement additional measures if required

**Acceptance Criteria:**
- DPIA document is completed
- Risks are identified and assessed
- Mitigation measures are documented
- DPIA is reviewed and approved
- Additional measures are implemented if required

**Business Impact:**  
Medium. DPIA is required for high-risk processing but is primarily a documentation and assessment exercise. It helps identify and mitigate risks.

## 5. Implementation Considerations

### 5.1 Dependencies

Critical requirements (Phase 1) are interdependent:
- Data subject rights endpoints require database access and query log structure
- Automated retention requires data subject rights to handle edge cases
- Consent mechanism should be implemented before Privacy Policy publication

High priority requirements can be implemented in parallel after Phase 1 is complete.

### 5.2 Resource Requirements

**Phase 1 (Critical):**
- Development time: 2-3 weeks for data subject rights endpoints
- Development time: 1 week for automated retention
- Development time: 1 week for consent mechanism
- Legal/compliance time: 1 week for DPA verification
- Total: 5-6 weeks

**Phase 2 (High Priority):**
- Development time: 1-2 weeks per requirement
- Documentation time: 1 week for breach procedures
- Total: 4-5 weeks

**Phase 3 (Medium Priority):**
- Documentation and review: ongoing
- Development time: 1-2 weeks for audit logging
- Total: 2-3 weeks

### 5.3 Risk Mitigation

**Legal Risk:**
- Implement critical requirements before Privacy Policy publication
- Document any gaps and timeline for remediation
- Legal review of consent mechanism and data subject rights implementation

**Technical Risk:**
- Test data deletion thoroughly to avoid accidental data loss
- Implement backup and recovery procedures
- Test retention processes in non-production environment first

**Operational Risk:**
- Train support staff on GDPR requests
- Document procedures for handling user requests
- Establish escalation procedures for complex requests

## 6. Success Criteria

The GDPR compliance implementation will be considered successful when:

1. All critical requirements (Phase 1) are implemented and tested
2. Privacy Policy commitments can be fulfilled operationally
3. Users can exercise all GDPR rights through system interfaces
4. Data retention policies are automatically enforced
5. Consent is tracked and verifiable
6. Third-party processor agreements are verified and documented
7. Security measures are verified and documented
8. Breach notification procedures are in place and tested

## 7. Approval and Sign-Off

This document requires approval from:
- Data Protection Officer or Legal Counsel
- Technical Lead
- Product Owner
- Compliance Officer

**Document Owner:** [To be assigned]  
**Review Date:** Quarterly or when system changes affect processing activities  
**Next Review:** [Date]

---

**Appendix A: GDPR Articles Reference**

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
- Article 28: Processor relationships
- Article 30: Records of processing
- Article 32: Security of processing
- Article 33/34: Data breach notification
- Article 35: Data Protection Impact Assessment
