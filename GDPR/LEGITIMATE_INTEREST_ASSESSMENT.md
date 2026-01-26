# Legitimate Interest Assessment (LIA)
## Query Logging in FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Annually or when processing changes  
**Next Review:** January 2027

---

## 1. Purpose

This document assesses the legitimate interest for processing personal data through query logging in the FCS RAG Bot system, in accordance with Article 6(1)(f) of the GDPR.

**Processing Activity:** Logging user queries, responses, and associated metadata for analytics, system improvement, debugging, and support purposes.

**Legal Basis:** Article 6(1)(f) GDPR - Legitimate interests of the controller

---

## 2. Processing Description

### 2.1 What Data is Processed

**Personal Data Logged:**
- User identifier (linked to user account)
- User email address
- Query text (user's question)
- Generated response (answer provided by system)
- Source documents referenced
- Timestamp of query
- Response latency
- Whether response was cached
- Tenant/organisation identifier

**Data Storage:**
- Stored in PostgreSQL database (query_logs table)
- Retained for 90 days, then automatically deleted
- Cached in Redis for 24 hours (TTL), then automatically expired

### 2.2 Purpose of Processing

**Primary Purposes:**
1. **System Analytics:** Analyse usage patterns, common questions, system performance
2. **System Improvement:** Identify areas for improvement, optimise responses, enhance knowledge base
3. **Debugging and Support:** Troubleshoot technical issues, investigate errors, provide user support
4. **Quality Assurance:** Monitor response quality, identify incorrect responses, improve accuracy
5. **Security Monitoring:** Detect suspicious activity, identify abuse, maintain system security

**Secondary Purposes:**
- Generate usage reports for stakeholders
- Understand user needs and preferences
- Identify knowledge gaps in documentation
- Measure system performance and reliability

---

## 3. Legitimate Interest Assessment

### 3.1 Legitimate Interest Test

**Step 1: Identify the Legitimate Interest**

The organisation has legitimate interests in:
- Maintaining and improving the quality of the RAG Bot service
- Ensuring system reliability and performance
- Providing effective user support and troubleshooting
- Understanding how the service is used to inform development
- Detecting and preventing abuse or security threats
- Demonstrating service value to stakeholders

**Step 2: Necessity Test**

**Is the processing necessary for the legitimate interest?**

Yes. Query logging is necessary because:
- **Analytics:** Cannot analyse usage patterns without logging queries
- **Debugging:** Cannot troubleshoot issues without query logs
- **Support:** Cannot provide user support without access to query history
- **Improvement:** Cannot improve system without understanding user needs
- **Security:** Cannot detect abuse without monitoring queries

**Could the purpose be achieved with less personal data?**

Partially. Some data minimisation is possible:
- User email could be removed after 30 days (anonymise, keep user_id)
- Full response text may not be necessary (preview sufficient for analytics)
- However, full query and response are necessary for debugging and support

**Recommendation:** Implement anonymisation after 30 days (remove user_email, keep anonymised user_id for analytics).

**Step 3: Balancing Test**

**Legitimate Interests of the Controller:**
- Improve service quality and user experience
- Maintain system reliability and performance
- Provide effective support and troubleshooting
- Understand user needs and system usage
- Detect and prevent abuse
- Demonstrate service value

**Impact on Data Subjects:**
- Privacy impact: Queries may contain business information or indirect personal data
- Control: Users can request deletion of their query logs
- Transparency: Users are informed of logging through Privacy Policy
- Retention: Limited retention period (90 days) reduces long-term impact
- Anonymisation: Option to anonymise after 30 days further reduces impact

**Balancing Assessment:**

**Factors Favouring Legitimate Interest:**
- Processing is necessary for core service functionality
- Limited retention period (90 days) minimises long-term impact
- Users are informed of processing (transparency)
- Users can exercise rights (access, deletion, objection)
- Data minimisation measures in place (anonymisation option)
- Security measures protect data
- Processing benefits users (improved service quality)

**Factors Against Legitimate Interest:**
- Queries may contain sensitive business information
- Users may not expect queries to be logged
- However, logging is disclosed in Privacy Policy

**Conclusion:** The legitimate interests of the controller outweigh the privacy impact on data subjects, provided that:
- Retention is limited to 90 days
- Anonymisation is implemented after 30 days
- Users are informed and can exercise rights
- Security measures are in place

---

## 4. Necessity Assessment

### 4.1 Is Processing Necessary?

**For Analytics:**
- Necessary: Cannot analyse usage without logging
- Alternative: Aggregated, anonymised statistics (but less useful)
- Conclusion: Logging with user identifiers is necessary for meaningful analytics

**For Debugging:**
- Necessary: Cannot debug issues without query logs
- Alternative: Log without user identifiers (but limits ability to trace issues to specific users)
- Conclusion: User identifiers necessary for effective debugging

**For Support:**
- Necessary: Cannot provide user support without query history
- Alternative: Users provide query history themselves (but inefficient)
- Conclusion: Logging is necessary for efficient support

**For System Improvement:**
- Necessary: Cannot improve system without understanding usage
- Alternative: User surveys (but less comprehensive)
- Conclusion: Logging is necessary for data-driven improvement

**Overall Conclusion:** Processing is necessary for the stated legitimate interests. However, data minimisation can be improved through anonymisation after 30 days.

### 4.2 Could Purpose Be Achieved Differently?

**Alternatives Considered:**

1. **No Logging:**
   - Impact: Cannot analyse, debug, or improve system effectively
   - Conclusion: Not viable for service operation

2. **Anonymised Logging Only:**
   - Impact: Limits debugging and support capabilities
   - Conclusion: Partial solution - anonymise after 30 days, keep full logs for active support

3. **Opt-In Logging:**
   - Impact: Incomplete data, limits analytics value
   - Conclusion: Not viable for system improvement

4. **Shorter Retention (30 days instead of 90):**
   - Impact: May limit historical analysis
   - Conclusion: Acceptable compromise - implement anonymisation after 30 days

**Recommendation:** Implement hybrid approach:
- Full logs retained for 30 days (for debugging and support)
- Anonymised logs (user_email removed) retained for additional 60 days (for analytics)
- Total retention: 90 days

---

## 5. Balancing Test

### 5.1 Legitimate Interests

**Organisation's Legitimate Interests:**
1. **Service Quality:** Improve RAG Bot responses and accuracy
2. **System Reliability:** Maintain system performance and uptime
3. **User Support:** Provide effective troubleshooting and support
4. **Business Operations:** Understand service usage and value
5. **Security:** Detect and prevent abuse or attacks

**Strength of Interests:**
- Strong: Service quality and reliability are core business functions
- Strong: User support is essential for user satisfaction
- Medium: Analytics support business decisions but not critical
- Strong: Security is essential for data protection

### 5.2 Impact on Data Subjects

**Privacy Impact:**
- **Data Collected:** Queries may contain business information or indirect personal data
- **Retention:** 90 days (limited, reduces long-term impact)
- **Access:** Data accessible to system administrators
- **Control:** Users can request deletion or object to processing

**Potential Harm:**
- **Low:** Queries are technical questions, typically not highly sensitive
- **Medium:** Queries may contain business information (but users choose what to query)
- **Low:** Limited retention reduces risk
- **Low:** Security measures protect data

**Mitigating Factors:**
- Users are informed of logging (Privacy Policy)
- Users can exercise rights (access, deletion, objection)
- Limited retention (90 days)
- Anonymisation option after 30 days
- Security measures in place
- Access controls limit who can view logs

### 5.3 Balancing Conclusion

**Assessment:**
The legitimate interests of the organisation in maintaining and improving the RAG Bot service are strong and necessary. The privacy impact on data subjects is moderate but mitigated through:
- Limited retention (90 days)
- Anonymisation after 30 days
- User rights (access, deletion, objection)
- Security measures
- Transparency (Privacy Policy)

**Conclusion:** The legitimate interests outweigh the privacy impact, provided that:
1. Retention is limited to 90 days
2. Anonymisation is implemented after 30 days
3. Users are informed and can exercise rights
4. Security measures are maintained
5. Processing is regularly reviewed

---

## 6. Mitigation Measures

### 6.1 Data Minimisation

**Implemented:**
- Limited retention (90 days)
- Automatic deletion after retention period
- Cache TTL (24 hours)

**To Be Implemented:**
- Anonymisation after 30 days (remove user_email, keep anonymised user_id)
- Consider storing only answer previews for old logs

### 6.2 Transparency

**Implemented:**
- Privacy Policy explains query logging
- Users informed of processing purpose
- Users informed of retention period

**To Be Enhanced:**
- Clear explanation in Privacy Policy
- User dashboard showing their query history (if applicable)

### 6.3 User Control

**Implemented:**
- Users can request access to their query logs
- Users can request deletion of their query logs
- Users can object to processing

**To Be Enhanced:**
- Easy-to-use data subject request process
- Clear instructions for exercising rights

### 6.4 Security

**Implemented:**
- Encryption in transit (HTTPS/TLS)
- Encryption at rest (database encryption)
- Access controls (role-based access)
- Authentication required

**Maintained:**
- Regular security assessments
- Access logging
- Security monitoring

### 6.5 Retention

**Implemented:**
- 90-day retention period
- Automatic deletion
- Cache TTL (24 hours)

**Verified:**
- Automated deletion process works correctly
- No data retained beyond retention period
- Backups also respect retention

---

## 7. Objection Handling

### 7.1 Right to Object

Users have the right to object to query logging under Article 21 GDPR.

**Objection Assessment:**

**If User Objects:**
1. Assess whether legitimate interest overrides objection
2. Consider user's specific circumstances
3. If objection is valid: Implement anonymisation or stop logging for that user
4. If legitimate interest overrides: Continue processing, explain why

**Current Assessment:**
- Query logging is necessary for service operation
- However, anonymisation can address privacy concerns
- Recommendation: Offer immediate anonymisation as compromise

**Objection Process:**
1. User submits objection
2. Assess objection and user circumstances
3. If valid: Implement anonymisation for user's queries
4. If not valid: Explain why processing continues
5. Document decision

### 7.2 Anonymisation Option

**Implementation:**
- Remove user_email immediately upon objection
- Keep anonymised user_id for analytics (if necessary)
- Or: Stop logging user's queries entirely (if user prefers)

**Balance:**
- Respects user privacy concerns
- Maintains analytics capability (with anonymised data)
- Preserves legitimate interests where possible

---

## 8. Review and Monitoring

### 8.1 Regular Review

This assessment must be reviewed:
- Annually
- When processing changes significantly
- When user complaints are received
- When new risks are identified
- Upon request from supervisory authority

### 8.2 Monitoring

**Monitor:**
- User objections to processing
- Data subject requests related to query logs
- Retention compliance (verify 90-day deletion)
- Anonymisation implementation (verify 30-day anonymisation)
- Security incidents affecting query logs

**Metrics:**
- Number of data subject requests related to query logs
- Number of objections received
- Retention compliance rate
- Anonymisation implementation rate

---

## 9. Conclusion

### 9.1 Legitimate Interest Confirmed

The organisation has a legitimate interest in query logging for:
- System analytics and improvement
- Debugging and support
- Security monitoring
- Service quality assurance

### 9.2 Necessity Confirmed

Query logging is necessary for these purposes and cannot be achieved effectively through less intrusive means.

### 9.3 Balancing Test Passed

The legitimate interests outweigh the privacy impact, provided that:
- Retention is limited to 90 days
- Anonymisation is implemented after 30 days
- Users are informed and can exercise rights
- Security measures are maintained
- Processing is regularly reviewed

### 9.4 Conditions

This legitimate interest assessment is valid subject to:
1. Implementation of 30-day anonymisation
2. Maintenance of 90-day retention limit
3. Continued transparency and user rights
4. Regular review and monitoring
5. Implementation of all mitigation measures

---

## 10. Approval

This Legitimate Interest Assessment has been reviewed and approved.

**Approved by:**

**Data Protection Officer / Legal Counsel:** _________________ Date: _______

**Technical Lead:** _________________ Date: _______

**Risk Owner:** _________________ Date: _______

---

**Document Owner:** Miles Waite  
**Last Updated:** January 2026  
**Next Review:** January 2027

---

## Appendix A: Related Documents

- Privacy Policy
- Record of Processing Activities (ROPA)
- Data Protection Impact Assessment (DPIA)
- Data Subject Request Procedures
- Data Retention Policy

---

## Appendix B: Legal Framework

**Article 6(1)(f) GDPR:**
"Processing shall be lawful only if and to the extent that at least one of the following applies: (f) processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, in particular where the data subject is a child."

**Three-Part Test:**
1. Legitimate interest exists
2. Processing is necessary for that interest
3. Legitimate interest is not overridden by data subject's interests

This assessment addresses all three parts of the test.
