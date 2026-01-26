# Data Breach Notification Procedures
## FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Annually or when procedures change  
**Next Review:** January 2027

---

## 1. Purpose and Scope

This document establishes procedures for detecting, assessing, and notifying data breaches in the FCS RAG Bot system, in compliance with Articles 33 and 34 of the GDPR.

**Scope:** All personal data breaches involving the FCS RAG Bot system, including breaches at third-party processors that affect our data subjects.

**Applicability:** All staff members who may become aware of a potential data breach must follow these procedures.

---

## 2. Definitions

**Personal Data Breach:** A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored, or otherwise processed.

**Examples of Data Breaches:**
- Unauthorised access to user accounts
- Unauthorised access to query logs or database
- Data breach at third-party processor (OpenAI, hosting provider, etc.)
- Accidental deletion or alteration of personal data
- Loss of data storage devices or backups
- Ransomware or malware attacks
- Phishing attacks resulting in unauthorised access
- Insider threats or unauthorised employee access

**Not a Breach:**
- Authorised access by authorised personnel
- Planned system maintenance with proper controls
- Data deletion in accordance with retention policies
- Anonymised data that cannot be re-identified

---

## 3. Breach Detection

### 3.1 Detection Mechanisms

**Automated Monitoring:**
- Security event logging and monitoring
- Error tracking (Sentry) for suspicious activity
- Access logging and audit trails
- System performance monitoring
- Database access monitoring

**Manual Detection:**
- Staff reports of suspicious activity
- User reports of unauthorised access
- Third-party notifications (processors, hosting providers)
- Security assessments and audits
- Incident response activities

### 3.2 Reporting Channels

**Immediate Reporting:**
- Email: [Data Protection Officer / Security Team Email]
- Phone: [Emergency Contact Number]
- Internal ticketing system: [Ticket System]
- Direct report to line manager

**All staff must report potential breaches immediately upon discovery.**

---

## 4. Breach Assessment

### 4.1 Initial Assessment (Within 1 Hour)

Upon discovery of a potential breach, the following information must be gathered:

**What Happened:**
- Description of the incident
- When did it occur (date and time)
- How was it discovered
- Who discovered it

**What Data Was Affected:**
- Categories of personal data
- Number of data subjects affected (if known)
- Types of data subjects (users, administrators, etc.)
- Sensitivity of data

**Impact Assessment:**
- Is personal data at risk?
- Can data be accessed by unauthorised parties?
- Is data encrypted or otherwise protected?
- What is the potential harm to data subjects?

**Containment:**
- Has the breach been contained?
- What immediate actions have been taken?
- Is the breach ongoing?

### 4.2 Detailed Assessment (Within 4 Hours)

**Risk to Data Subjects:**
- Identity theft or fraud
- Financial loss
- Damage to reputation
- Loss of confidentiality
- Any other significant economic or social disadvantage

**Likelihood and Severity:**
- High risk: Significant likelihood of harm, severe impact
- Medium risk: Moderate likelihood or moderate impact
- Low risk: Low likelihood and low impact

**Breach Classification:**
- **Confirmed Breach:** Personal data has been compromised
- **Potential Breach:** Investigation required to confirm
- **Not a Breach:** No personal data compromised

### 4.3 Assessment Team

**Core Team:**
- Data Protection Officer / Legal Counsel
- Technical Lead / Security Team
- System Administrator
- Management / Incident Response Lead

**Additional Support (as needed):**
- External legal counsel
- Forensic investigators
- Public relations / Communications

---

## 5. Breach Response

### 5.1 Immediate Response (Within 1 Hour)

**Containment:**
1. Isolate affected systems if breach is ongoing
2. Revoke compromised access credentials
3. Block unauthorised access points
4. Preserve evidence for investigation
5. Document all actions taken

**Investigation:**
1. Determine scope and extent of breach
2. Identify affected data and data subjects
3. Assess risk to data subjects
4. Determine root cause
5. Identify any vulnerabilities exploited

**Remediation:**
1. Patch vulnerabilities
2. Strengthen security controls
3. Update access controls
4. Enhance monitoring
5. Implement additional safeguards

### 5.2 Documentation

**Breach Log:**
- Date and time of discovery
- Date and time of breach (if known)
- Description of breach
- Affected data and data subjects
- Risk assessment
- Actions taken
- Notification details (if applicable)
- Follow-up actions

**Evidence Preservation:**
- Logs and audit trails
- System snapshots
- Communication records
- Investigation notes

---

## 6. Breach Notification

### 6.1 Supervisory Authority Notification (Article 33)

**When Required:**
- Notification required for ALL personal data breaches
- Must be made within 72 hours of becoming aware of the breach
- If notification cannot be made within 72 hours, reasons for delay must be provided

**Notification Content:**
- Nature of the breach (categories and approximate number of data subjects, categories and approximate number of personal data records)
- Name and contact details of Data Protection Officer or contact point
- Likely consequences of the breach
- Measures proposed or taken to address the breach and mitigate its effects

**Notification Method:**
- Submit to supervisory authority through official channels
- Use supervisory authority breach notification form (if available)
- Maintain record of notification

**Supervisory Authority Contact:**
- [UK: Information Commissioner's Office (ICO)]
- [EU: Relevant national supervisory authority]
- Website: [Supervisory Authority Website]
- Breach Notification Portal: [Portal URL]

**Template:** See Appendix A

### 6.2 Data Subject Notification (Article 34)

**When Required:**
- Notification required if breach is likely to result in HIGH RISK to rights and freedoms of data subjects
- Must be made without undue delay
- Exception: If data is encrypted and encryption key not compromised, notification may not be required

**High Risk Indicators:**
- Sensitive personal data compromised
- Large number of data subjects affected
- Data could be used for identity theft or fraud
- Significant financial or reputational harm possible
- Data subjects cannot easily mitigate the risk themselves

**Notification Content:**
- Clear and plain language description of the breach
- Name and contact details of Data Protection Officer or contact point
- Likely consequences of the breach
- Measures proposed or taken to address the breach and mitigate its effects
- Advice on steps data subjects can take to protect themselves

**Notification Method:**
- Direct communication (email, letter) to affected data subjects
- Public communication (website notice) if direct communication not feasible
- Consider urgency and method of communication

**Template:** See Appendix B

### 6.3 Third-Party Processor Notification

**When Required:**
- If breach occurs at third-party processor, processor must notify us without undue delay
- We must then assess and notify supervisory authority and data subjects if required

**Our Obligations:**
- Ensure processors have breach notification procedures
- Verify processors notify us promptly
- Assess breach and determine our notification obligations

---

## 7. Post-Breach Actions

### 7.1 Investigation and Root Cause Analysis

**Investigation:**
- Conduct thorough investigation of breach
- Identify root cause
- Identify any systemic issues
- Document findings

**Root Cause Analysis:**
- What vulnerabilities were exploited?
- Were security controls adequate?
- Were procedures followed?
- What improvements are needed?

### 7.2 Remediation and Prevention

**Immediate Remediation:**
- Patch vulnerabilities
- Strengthen security controls
- Update procedures
- Enhance monitoring

**Long-Term Prevention:**
- Implement additional security measures
- Update policies and procedures
- Staff training on breach prevention
- Regular security assessments
- Review and update breach procedures

### 7.3 Review and Lessons Learned

**Post-Incident Review:**
- Review breach response effectiveness
- Identify lessons learned
- Update procedures based on experience
- Share learnings with team

**Documentation:**
- Maintain breach log
- Document lessons learned
- Update risk assessments
- Update DPIA if necessary

---

## 8. Roles and Responsibilities

### 8.1 Data Protection Officer / Legal Counsel

**Responsibilities:**
- Coordinate breach response
- Assess legal obligations
- Prepare supervisory authority notifications
- Prepare data subject notifications
- Liaise with supervisory authority
- Legal advice and guidance

### 8.2 Technical Lead / Security Team

**Responsibilities:**
- Technical investigation
- Containment and remediation
- Security assessment
- Vulnerability patching
- Evidence collection
- Technical documentation

### 8.3 System Administrator

**Responsibilities:**
- System access control
- Log analysis
- System restoration
- Backup and recovery
- Technical support

### 8.4 Management / Incident Response Lead

**Responsibilities:**
- Overall coordination
- Resource allocation
- Decision-making
- Communication with stakeholders
- Post-incident review

### 8.5 All Staff

**Responsibilities:**
- Report potential breaches immediately
- Follow breach response procedures
- Preserve evidence
- Cooperate with investigation
- Maintain confidentiality

---

## 9. Training and Awareness

**Staff Training:**
- All staff must be trained on breach detection and reporting
- Training must be provided upon hire and annually
- Training must cover:
  - What constitutes a data breach
  - How to detect breaches
  - Reporting procedures
  - Importance of timely reporting

**Regular Updates:**
- Procedures updated based on experience
- Staff notified of procedure changes
- Regular refresher training

---

## 10. Testing and Review

**Regular Testing:**
- Tabletop exercises for breach response
- Simulated breach scenarios
- Review of response effectiveness
- Identification of improvement areas

**Procedure Review:**
- Annual review of procedures
- Update based on:
  - Regulatory changes
  - Industry best practices
  - Lessons learned from incidents
  - System changes

---

## 11. Contact Information

**Data Protection Officer:**
- Name: [DPO Name]
- Email: [DPO Email]
- Phone: [DPO Phone]

**Security Team:**
- Email: [Security Email]
- Phone: [Security Phone]
- Emergency: [Emergency Contact]

**Supervisory Authority:**
- [UK: Information Commissioner's Office (ICO)]
- Website: https://ico.org.uk
- Phone: 0303 123 1113
- Breach Notification: [Portal URL]

**Legal Counsel:**
- Name: [Legal Counsel Name]
- Email: [Legal Email]
- Phone: [Legal Phone]

---

## Appendix A: Supervisory Authority Notification Template

**To:** [Supervisory Authority Name]  
**From:** [Organisation Name]  
**Date:** [Date of Notification]  
**Subject:** Personal Data Breach Notification

**1. Nature of the Breach:**
[Description of the breach, including what happened, when it occurred, and how it was discovered]

**2. Categories of Personal Data:**
[Categories of personal data affected, e.g., user account data, query logs, calculation scripts]

**3. Approximate Number of Data Subjects:**
[Number of data subjects affected, or estimate if exact number not known]

**4. Approximate Number of Personal Data Records:**
[Number of personal data records affected]

**5. Contact Details:**
- Data Protection Officer: [Name, Email, Phone]
- Organisation: [Name, Address, Contact]

**6. Likely Consequences:**
[Description of likely consequences for data subjects, e.g., identity theft, financial loss, reputational damage]

**7. Measures Proposed or Taken:**
[Description of measures taken to address the breach and mitigate its effects, including containment, investigation, and remediation]

**8. Additional Information:**
[Any other relevant information]

---

## Appendix B: Data Subject Notification Template

**Subject:** Important: Data Security Incident Notification

Dear [Data Subject Name],

We are writing to inform you of a data security incident that may have affected your personal data.

**What Happened:**
[Clear, plain language description of what happened, when it occurred, and what data may have been affected]

**What Information Was Involved:**
[Description of the personal data that may have been affected, e.g., email address, query history]

**What We Are Doing:**
[Description of measures taken to address the incident, including:
- Immediate actions taken
- Investigation steps
- Security enhancements
- Ongoing monitoring]

**What You Can Do:**
[Advice on steps data subjects can take to protect themselves, such as:
- Change passwords
- Monitor accounts for suspicious activity
- Be cautious of phishing attempts
- Review account activity]

**For More Information:**
If you have questions or concerns, please contact us:
- Email: [Contact Email]
- Phone: [Contact Phone]
- Data Protection Officer: [DPO Contact]

We sincerely apologise for this incident and any concern it may cause. We take data protection seriously and are committed to protecting your personal data.

Sincerely,
[Organisation Name]
[Date]

---

**Document Owner:** Miles Waite  
**Last Updated:** January 2026  
**Next Review:** January 2027
