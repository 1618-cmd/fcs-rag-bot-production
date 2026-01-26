# Data Protection Impact Assessment (DPIA)
## FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Annually or when processing changes significantly  
**Next Review:** January 2027

---

## 1. Executive Summary

This Data Protection Impact Assessment (DPIA) evaluates the data protection risks associated with the FCS RAG Bot system, which uses artificial intelligence and machine learning technologies to provide technical support and assistance for the Vena financial consolidation platform.

The system processes personal data including user account information, query logs, and uploaded calculation scripts. It utilises third-party AI services (OpenAI GPT-4o) and stores data across multiple cloud providers, including services located outside the European Economic Area.

**Key Findings:**
- The system involves high-risk processing due to AI/ML technologies and automated processing
- Personal data is transferred to third parties, including processors in the United States
- Query logs may contain business-sensitive information
- Mitigation measures are in place, but ongoing monitoring and review are required

**Recommendation:** Proceed with implementation, subject to implementation of identified mitigation measures and regular review of risks.

---

## 2. Description of Processing

### 2.1 System Overview

The FCS RAG Bot is a Retrieval-Augmented Generation (RAG) system that:
- Processes natural language queries from users
- Retrieves relevant documentation from a knowledge base
- Generates responses using OpenAI's GPT-4o language model
- Analyses and explains VenaQL calculation scripts
- Logs queries and responses for analytics and system improvement

### 2.2 Processing Activities

**Primary Processing Activities:**
1. User account management and authentication
2. Query processing through RAG pipeline
3. AI-powered response generation using OpenAI GPT-4o
4. Calculation script analysis and explanation
5. Query logging and analytics
6. Document management and knowledge base maintenance

**Data Categories:**
- User account data (email, name, role, authentication data)
- Query data (user questions, generated responses, timestamps)
- Calculation scripts (uploaded code files for analysis)
- Document metadata (knowledge base management)
- System logs and analytics data

**Data Subjects:**
- Employees and contractors using the service
- Administrators managing the system
- End users whose queries may contain business information

### 2.3 Data Flows

**Data Collection:**
- Users create accounts and provide email/name
- Users submit queries through web interface
- Users upload calculation scripts for analysis
- Administrators upload documents to knowledge base

**Data Processing:**
- Queries are sent to OpenAI API (United States) for response generation
- Query embeddings are stored in Qdrant Cloud (EU/United States) for semantic search
- Query logs are stored in PostgreSQL database
- Documents are stored in AWS S3 and embedded in Qdrant

**Data Storage:**
- User accounts: PostgreSQL database
- Query logs: PostgreSQL database (90-day retention)
- Cached queries: Redis (24-hour TTL)
- Documents: AWS S3
- Embeddings: Qdrant Cloud

**Data Sharing:**
- Data shared with OpenAI for response generation
- Data shared with hosting providers (Render, Vercel) for infrastructure
- Data shared with monitoring services (Sentry) for error tracking

---

## 3. Necessity and Proportionality Assessment

### 3.1 Necessity

**Is the processing necessary for the stated purpose?**
Yes. The processing is necessary to:
- Provide the core RAG Bot service functionality
- Authenticate and authorise users
- Generate accurate and relevant responses
- Analyse calculation scripts as a core service feature
- Maintain system security and performance

**Could the purpose be achieved with less personal data?**
Partially. Some data minimisation opportunities exist:
- Query logs could be anonymised after 30 days (currently 90 days)
- Query logs could store only previews rather than full text
- However, full query text is necessary for debugging and support purposes

**Recommendation:** Implement anonymisation of query logs after 30 days, retaining full logs only for active support cases.

### 3.2 Proportionality

**Is the processing proportionate to the purpose?**
Yes, with mitigation measures:
- Processing is limited to what is necessary for service delivery
- Retention periods are defined and enforced (90 days for query logs)
- Access controls restrict data access to authorised personnel
- Users are informed of processing through Privacy Policy

**Balancing Test:**
- Legitimate interests (system improvement, analytics) are balanced against user privacy through:
  - Limited retention periods
  - Access controls
  - Anonymisation options
  - User rights (access, deletion, objection)

---

## 4. Risk Assessment

### 4.1 Risk Identification

#### Risk 1: Unauthorised Access to Personal Data

**Description:** Unauthorised individuals gain access to user accounts, query logs, or uploaded calculation scripts.

**Likelihood:** Medium
- System has authentication and access controls
- However, vulnerabilities could be exploited
- Third-party processors could be compromised

**Impact:** High
- Personal data exposure
- Business-sensitive information disclosure
- Loss of user trust
- Regulatory fines

**Risk Level:** Medium-High

**Mitigation Measures:**
- Strong authentication (password hashing, JWT tokens)
- Role-based access control
- Encryption in transit and at rest
- Regular security assessments
- Security monitoring and alerting
- Access logging and audit trails

**Residual Risk:** Low-Medium (with mitigation measures in place)

---

#### Risk 2: Data Breach at Third-Party Processor

**Description:** Data breach occurs at OpenAI, hosting provider, or other third-party processor, exposing user queries or calculation scripts.

**Likelihood:** Low-Medium
- Reputable processors with security measures
- However, third-party breaches are common
- Data is transferred to United States (OpenAI, hosting)

**Impact:** High
- Exposure of user queries (may contain business information)
- Exposure of calculation scripts (may contain sensitive business logic)
- Loss of user trust
- Regulatory fines
- Potential notification requirements

**Risk Level:** Medium-High

**Mitigation Measures:**
- Data Processing Agreements (DPAs) with all processors
- Standard Contractual Clauses (SCCs) for international transfers
- Due diligence on processor security practices
- Breach notification procedures
- Regular review of processor security
- Data minimisation (send only necessary data to processors)

**Residual Risk:** Medium (third-party risk is inherent but mitigated through agreements and due diligence)

---

#### Risk 3: Inadequate Data Retention and Deletion

**Description:** Personal data is retained longer than necessary, or deletion requests are not properly processed.

**Likelihood:** Medium
- Automated retention not yet implemented
- Manual deletion processes prone to error
- Backup systems may retain data beyond retention period

**Impact:** Medium
- Non-compliance with GDPR retention requirements
- Increased risk exposure over time
- User rights not properly exercised

**Risk Level:** Medium

**Mitigation Measures:**
- Automated data retention and deletion (90 days for query logs)
- Automated user account deletion (30 days after deactivation)
- Data subject deletion request procedures
- Backup retention policies aligned with primary retention
- Regular audits of retention compliance
- Documentation of retention periods

**Residual Risk:** Low (once automated retention is implemented)

---

#### Risk 4: Inability to Fulfil Data Subject Rights

**Description:** System cannot properly respond to data subject access, deletion, or portability requests within required timeframes.

**Likelihood:** Medium
- Data subject request procedures not yet implemented
- Data may be stored across multiple systems
- Complex data relationships (user accounts, query logs, cache)

**Impact:** Medium
- Non-compliance with GDPR requirements
- User complaints
- Regulatory fines
- Loss of user trust

**Risk Level:** Medium

**Mitigation Measures:**
- Data subject request procedures
- Automated data export functionality
- Automated data deletion functionality
- Clear documentation of data locations
- Staff training on handling requests
- Response time tracking and monitoring

**Residual Risk:** Low (once procedures and systems are implemented)

---

#### Risk 5: AI Processing Errors or Bias

**Description:** OpenAI's AI model generates incorrect, biased, or inappropriate responses, potentially causing harm or discrimination.

**Likelihood:** Low-Medium
- AI models can produce errors or hallucinations
- Training data may contain biases
- Responses may not always be accurate

**Impact:** Medium
- Incorrect technical guidance provided to users
- Potential business impact if users rely on incorrect information
- Loss of user trust
- However, system is designed for technical support, not critical decision-making

**Risk Level:** Low-Medium

**Mitigation Measures:**
- RAG system grounds responses in knowledge base documents
- Source citations provided with all responses
- Anti-hallucination prompts in system design
- User feedback mechanisms
- Regular monitoring of response quality
- Clear disclaimers about AI-generated content
- Human review processes for critical responses

**Residual Risk:** Low-Medium (AI risk is inherent but mitigated through grounding and monitoring)

---

#### Risk 6: International Data Transfer Risks

**Description:** Personal data transferred to United States or other countries outside EEA without adequate safeguards.

**Likelihood:** Low (if safeguards are in place)
- Standard Contractual Clauses should be in place
- However, safeguards must be verified

**Impact:** High
- Non-compliance with GDPR transfer requirements
- Regulatory fines
- Potential suspension of data transfers

**Risk Level:** Medium (until safeguards are verified)

**Mitigation Measures:**
- Verify Standard Contractual Clauses (SCCs) with all processors
- Verify Data Processing Agreements (DPAs) with all processors
- Document all international transfers
- Regular review of transfer mechanisms
- Consider EU-based alternatives where possible (e.g., Qdrant EU cluster)

**Residual Risk:** Low (once safeguards are verified and documented)

---

### 4.2 Risk Summary

| Risk | Likelihood | Impact | Risk Level | Residual Risk (with mitigation) |
|------|------------|--------|------------|----------------------------------|
| Unauthorised Access | Medium | High | Medium-High | Low-Medium |
| Third-Party Breach | Low-Medium | High | Medium-High | Medium |
| Inadequate Retention | Medium | Medium | Medium | Low |
| Inability to Fulfil Rights | Medium | Medium | Medium | Low |
| AI Processing Errors | Low-Medium | Medium | Low-Medium | Low-Medium |
| International Transfers | Low | High | Medium | Low |

**Overall Risk Assessment:** Medium-High (before mitigation), Low-Medium (after mitigation)

---

## 5. Mitigation Measures

### 5.1 Technical Measures

**Encryption:**
- All data encrypted in transit (HTTPS/TLS)
- All data encrypted at rest (databases, storage)
- Encryption keys managed securely

**Access Controls:**
- Strong authentication (password hashing, JWT tokens)
- Role-based access control
- Multi-tenancy isolation
- Regular access reviews

**Data Minimisation:**
- Collect only necessary data
- Anonymise query logs after 30 days
- Implement data retention and deletion
- Minimise data sent to third-party processors

**Security Monitoring:**
- Error tracking and monitoring (Sentry)
- Security event logging
- Regular security assessments
- Incident detection and response

### 5.2 Organisational Measures

**Policies and Procedures:**
- Privacy Policy
- Data Retention Policy
- Data Breach Notification Procedures
- Data Subject Request Procedures
- Security policies and procedures

**Staff Training:**
- Data protection training
- Security awareness training
- Procedures for handling data subject requests
- Breach response training

**Contractual Safeguards:**
- Data Processing Agreements (DPAs) with all processors
- Standard Contractual Clauses (SCCs) for international transfers
- Regular review of processor agreements
- Processor security assessments

**Governance:**
- Regular review of processing activities (ROPA)
- Regular DPIA reviews
- Compliance monitoring
- Incident response procedures

### 5.3 Ongoing Measures

**Regular Reviews:**
- Quarterly ROPA review
- Annual DPIA review
- Regular security assessments
- Processor security reviews

**Monitoring:**
- Security event monitoring
- Compliance monitoring
- Data subject request tracking
- Breach detection and response

**Continuous Improvement:**
- Update mitigation measures based on new risks
- Improve security measures as threats evolve
- Enhance data minimisation where possible
- Regular staff training updates

---

## 6. Consultation

### 6.1 Internal Consultation

This DPIA has been reviewed by:
- Technical Lead
- Security Team
- Legal/Compliance Team
- Data Protection Officer (if applicable)

### 6.2 Data Subject Consultation

**Considerations:**
- Users are informed of processing through Privacy Policy
- Users can exercise data subject rights
- User feedback mechanisms in place
- Regular communication about data processing

**Recommendation:** Consider user survey or feedback mechanism to assess user concerns about data processing.

### 6.3 Supervisory Authority Consultation

**When Required:**
- Consultation with supervisory authority required if residual risk remains high after mitigation
- Current assessment: Residual risk is Low-Medium, consultation may not be required
- However, consultation recommended if significant concerns remain

**Recommendation:** Monitor residual risks and consult supervisory authority if risks increase or new risks emerge.

---

## 7. Conclusion and Recommendations

### 7.1 Overall Assessment

The FCS RAG Bot system involves high-risk processing due to:
- Use of AI/ML technologies
- Automated processing of personal data
- International data transfers
- Processing of potentially sensitive business information

However, with appropriate mitigation measures in place, the residual risks are manageable and acceptable.

### 7.2 Recommendations

**Immediate Actions (Before Go-Live):**
1. Verify Data Processing Agreements (DPAs) with all third-party processors
2. Verify Standard Contractual Clauses (SCCs) for international transfers
3. Implement automated data retention and deletion
4. Implement data subject request procedures
5. Implement data breach notification procedures
6. Complete security documentation

**Short-Term Actions (Within 1 Month):**
1. Implement query log anonymisation after 30 days
2. Conduct security assessment
3. Staff training on data protection
4. Regular monitoring and review processes

**Ongoing Actions:**
1. Quarterly review of ROPA
2. Annual review of DPIA
3. Regular security assessments
4. Regular review of processor security
5. Continuous improvement of mitigation measures

### 7.3 Approval

This DPIA has been reviewed and the risks are considered acceptable with the identified mitigation measures in place.

**Approved by:**

**Data Protection Officer / Legal Counsel:** _________________ Date: _______

**Technical Lead:** _________________ Date: _______

**Risk Owner:** _________________ Date: _______

---

## 8. Review Schedule

This DPIA must be reviewed:
- Annually
- When processing activities change significantly
- When new risks are identified
- When mitigation measures change
- Upon request from supervisory authority

**Last Updated:** January 2026  
**Next Review:** January 2027  
**Document Owner:** Miles Waite

---

## Appendix A: Related Documents

- Privacy Policy
- Record of Processing Activities (ROPA)
- Data Breach Notification Procedures
- Data Subject Request Procedures
- Processor Register
- Security Documentation
- Legitimate Interest Assessment (for query logging)

---

## Appendix B: Risk Assessment Methodology

Risks were assessed using the following criteria:

**Likelihood:**
- Low: Unlikely to occur
- Medium: May occur
- High: Likely to occur

**Impact:**
- Low: Minimal impact on data subjects
- Medium: Moderate impact on data subjects
- High: Significant impact on data subjects

**Risk Level:**
- Low: Low likelihood, low impact
- Medium: Medium likelihood or medium impact
- High: High likelihood or high impact
- Critical: High likelihood and high impact

**Residual Risk:**
Assessed after implementation of mitigation measures.
