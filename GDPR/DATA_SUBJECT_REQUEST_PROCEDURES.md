# Data Subject Request Procedures
## FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Annually or when procedures change  
**Next Review:** January 2027

---

## 1. Purpose and Scope

This document establishes procedures for handling data subject requests under Articles 15-22 of the GDPR, including requests for access, rectification, erasure, restriction, portability, and objection.

**Scope:** All data subject requests relating to personal data processed in the FCS RAG Bot system.

**Legal Requirements:**
- Requests must be responded to within 30 days (may be extended to 60 days for complex requests)
- Requests must be handled free of charge (except for manifestly unfounded or excessive requests)
- Requests must be verified to ensure they come from the data subject

---

## 2. Types of Data Subject Requests

### 2.1 Right of Access (Article 15)

**What Data Subjects Can Request:**
- Confirmation that their personal data is being processed
- Access to their personal data
- Information about processing (purposes, categories, recipients, retention, rights, etc.)

**Common Requests:**
- "What data do you have about me?"
- "Send me a copy of all my data"
- "Show me my query history"

### 2.2 Right to Rectification (Article 16)

**What Data Subjects Can Request:**
- Correction of inaccurate personal data
- Completion of incomplete personal data

**Common Requests:**
- "Update my email address"
- "Correct my name"
- "Fix incorrect information"

### 2.3 Right to Erasure / Right to be Forgotten (Article 17)

**What Data Subjects Can Request:**
- Deletion of their personal data
- Erasure of data that is no longer necessary, unlawfully processed, or where consent is withdrawn

**Common Requests:**
- "Delete my account"
- "Remove all my data"
- "I want to be forgotten"

### 2.4 Right to Restriction of Processing (Article 18)

**What Data Subjects Can Request:**
- Temporary restriction of processing while accuracy is contested
- Restriction when processing is unlawful but erasure not requested
- Restriction when data no longer needed but required for legal claims

**Common Requests:**
- "Stop processing my data while we resolve this issue"
- "Suspend my account temporarily"

### 2.5 Right to Data Portability (Article 20)

**What Data Subjects Can Request:**
- Receive their personal data in a structured, commonly used, machine-readable format
- Transmit data to another service provider

**Common Requests:**
- "Export my data"
- "Give me my data in JSON/CSV format"
- "Transfer my data to another service"

### 2.6 Right to Object (Article 21)

**What Data Subjects Can Request:**
- Object to processing based on legitimate interests
- Object to processing for direct marketing

**Common Requests:**
- "I object to query logging"
- "Stop using my data for analytics"

---

## 3. Request Receipt and Verification

### 3.1 Receiving Requests

**Acceptable Methods:**
- Email to: [Data Protection Email]
- Web form: [Data Subject Request Form URL]
- Written letter to: [Organisation Address]
- API endpoint: `/api/gdpr/access`, `/api/gdpr/delete`, `/api/gdpr/export`
- In-person request (if applicable)

**Required Information:**
- Data subject's identity (to verify request)
- Type of request (access, deletion, export, etc.)
- Any specific data or time period (if applicable)

### 3.2 Verification

**Identity Verification:**
- Verify request comes from data subject
- Methods:
  - Email from registered email address
  - Account authentication (for API requests)
  - Identity documents (for written requests)
  - Security questions or additional verification

**Verification Process:**
1. Confirm identity matches account holder
2. Verify email address matches registered account
3. For sensitive requests (deletion), require additional verification
4. Document verification method used

**If Identity Cannot Be Verified:**
- Request additional verification
- Explain why verification is necessary
- Do not process request until verified

### 3.3 Request Logging

**Log Entry Must Include:**
- Request date and time
- Requestor identity (email, user ID)
- Request type
- Verification method
- Request details
- Assigned handler
- Status (received, in progress, completed, refused)
- Response date
- Any extensions or complications

---

## 4. Request Processing

### 4.1 Initial Response (Within 1 Week)

**Acknowledge Receipt:**
- Send acknowledgment within 1 week of receipt
- Confirm request received and being processed
- Provide expected response timeframe (30 days)
- Provide contact information for questions

**Acknowledgment Template:**
"Thank you for your data subject request. We have received your request and are processing it. We will respond within 30 days. If you have any questions, please contact [Contact Information]."

### 4.2 Data Collection (Within 2 Weeks)

**Identify Data Locations:**
- User account data (PostgreSQL: users table)
- Query logs (PostgreSQL: query_logs table)
- Cached data (Redis)
- Document uploads (if stored separately)
- Authentication tokens (if stored)
- Any other personal data

**Data Collection Process:**
1. Query database for user's account data
2. Query database for user's query logs
3. Check Redis cache for user's cached queries
4. Check S3 for user-uploaded documents (if applicable)
5. Compile all personal data
6. Review for completeness

**Data Sources:**
- PostgreSQL: `SELECT * FROM users WHERE id = ?`
- PostgreSQL: `SELECT * FROM query_logs WHERE user_id = ?`
- Redis: Check for cached entries with user identifier
- S3: Check for user-uploaded files (if stored)

### 4.3 Response Preparation (Within 3 Weeks)

**For Access Requests:**
- Compile all personal data
- Format in human-readable format (JSON or CSV)
- Include processing information (purposes, legal basis, retention, etc.)
- Include data subject rights information
- Prepare response document

**For Deletion Requests:**
- Identify all data to be deleted
- Check for legal exceptions (e.g., legal holds, ongoing investigations)
- Prepare deletion plan
- Execute deletion (see Section 5)
- Confirm deletion

**For Export Requests:**
- Compile all personal data
- Format in machine-readable format (JSON preferred, CSV acceptable)
- Structure data for portability
- Prepare export file

**For Rectification Requests:**
- Verify requested changes
- Update data in database
- Confirm changes made
- Notify data subject

**For Restriction Requests:**
- Set processing_restricted flag in user account
- Block query processing for restricted users
- Document restriction reason
- Notify data subject

**For Objection Requests:**
- Assess objection validity
- If valid: Implement anonymisation or stop processing
- If not valid: Explain why processing continues
- Document decision

### 4.4 Response Delivery (Within 30 Days)

**Response Methods:**
- Email with data attached (for access/export)
- Secure file transfer (for large files)
- Written letter (if requested)
- API response (for API requests)

**Response Content:**
- All requested personal data (for access/export)
- Confirmation of actions taken (for deletion/rectification)
- Explanation of decisions (for restriction/objection)
- Information about data subject rights
- Contact information for complaints

**If Extension Required:**
- Notify data subject within 30 days
- Explain reason for extension (complexity, multiple requests)
- Provide new response date (maximum 60 days total)
- Document extension reason

---

## 5. Specific Request Types

### 5.1 Access Request (Article 15)

**Data to Include:**
- Account information (email, name, role, creation date, last login)
- All query logs (question, answer, sources, timestamp)
- Any uploaded calculation scripts (if stored)
- Authentication history (if logged)
- Processing information (purposes, legal basis, retention, etc.)

**Format:**
- JSON or CSV format
- Human-readable
- Organised by data type
- Include metadata (when data was collected, retention period)

**Response Template:**
```json
{
  "account": {
    "email": "user@example.com",
    "name": "User Name",
    "role": "viewer",
    "created_at": "2026-01-01T00:00:00Z",
    "last_login": "2026-01-15T10:30:00Z"
  },
  "query_logs": [
    {
      "question": "How do I configure...",
      "answer_preview": "To configure...",
      "sources": ["document1.md", "document2.md"],
      "timestamp": "2026-01-10T14:20:00Z"
    }
  ],
  "processing_information": {
    "purposes": ["Service delivery", "Analytics"],
    "legal_basis": ["Contractual necessity", "Legitimate interest"],
    "retention": "90 days for query logs"
  }
}
```

### 5.2 Deletion Request (Article 17)

**Deletion Process:**
1. Verify request and identity
2. Check for legal exceptions:
   - Legal obligations (e.g., audit logs must be retained)
   - Legal claims (ongoing disputes)
   - Public interest
3. If no exceptions: Proceed with deletion
4. Delete user account (hard delete)
5. Delete or anonymise query logs
6. Clear Redis cache for user
7. Delete uploaded files (if stored separately)
8. Confirm deletion to data subject

**Deletion Steps:**
```sql
-- Delete query logs
DELETE FROM query_logs WHERE user_id = ?;

-- Anonymise query logs (alternative if deletion not possible)
UPDATE query_logs 
SET user_id = NULL, user_email = NULL 
WHERE user_id = ?;

-- Delete user account
DELETE FROM users WHERE id = ?;

-- Clear Redis cache
-- Remove all keys associated with user_id
```

**Exceptions:**
- Audit logs: Retain for 7 years (legal requirement)
- If query logs are needed for legal claims: May restrict processing instead of deleting
- If deletion would affect other users: Assess on case-by-case basis

**Confirmation:**
- Confirm all data deleted
- Provide list of what was deleted
- Explain any data retained (and why)

### 5.3 Export Request (Article 20)

**Export Format:**
- JSON (preferred, machine-readable)
- CSV (alternative)
- Structured and portable

**Data to Include:**
- Same as access request
- Structured for portability
- Include metadata for context

**Export File:**
- Named: `user_data_export_[user_id]_[date].json`
- Include all personal data
- Include processing metadata
- Instructions for importing to another service (if applicable)

### 5.4 Rectification Request (Article 16)

**Process:**
1. Verify requested changes are accurate
2. Update data in database
3. Verify changes saved correctly
4. Confirm to data subject

**Common Rectifications:**
- Email address update
- Name correction
- Role update (if user has permission)

**Note:** Query logs are historical records and generally cannot be rectified. If query log contains incorrect information, document the correction separately.

### 5.5 Restriction Request (Article 18)

**Process:**
1. Set `processing_restricted = true` in user account
2. Block query processing for restricted users
3. Document restriction reason
4. Notify data subject

**Restriction Effects:**
- User cannot submit queries
- Existing data retained but not processed
- User account remains but access restricted

**Lifting Restriction:**
- When restriction reason resolved
- Update `processing_restricted = false`
- Restore user access
- Notify data subject

### 5.6 Objection Request (Article 21)

**Process:**
1. Assess objection validity
2. If objection to legitimate interest processing:
   - Assess if legitimate interest overrides objection
   - If yes: Continue processing, explain why
   - If no: Implement anonymisation or stop processing
3. Document decision
4. Notify data subject

**For Query Logging:**
- If user objects to query logging:
  - Assess if logging is necessary
  - If necessary: Explain why, continue with anonymisation
  - If not necessary: Implement immediate anonymisation

---

## 6. Refusal of Requests

### 6.1 When Requests Can Be Refused

**Manifestly Unfounded Requests:**
- Repeated requests with no legitimate purpose
- Requests clearly intended to harass or disrupt
- Requests that are clearly not from data subject

**Excessive Requests:**
- Multiple requests in short time period
- Requests requiring disproportionate effort
- Requests that are clearly excessive

**Legal Exceptions:**
- Legal obligations require retention
- Legal claims require data retention
- Public interest
- Legitimate interests override (for erasure requests)

### 6.2 Refusal Process

**Document Refusal:**
- Reason for refusal
- Legal basis for refusal
- Right to lodge complaint with supervisory authority
- Right to seek judicial remedy

**Notify Data Subject:**
- Explain refusal reason
- Provide contact information for complaints
- Provide supervisory authority contact information

**Refusal Template:**
"We are unable to fulfil your request because [reason]. This refusal is based on [legal basis]. You have the right to lodge a complaint with [Supervisory Authority] if you are not satisfied with our response."

---

## 7. Fees

**General Rule:**
- Data subject requests are free of charge

**Exceptions:**
- Manifestly unfounded or excessive requests: May charge reasonable fee
- Additional copies: May charge reasonable fee for additional copies

**Fee Calculation:**
- Based on administrative costs
- Must be reasonable
- Must be communicated to data subject before processing

---

## 8. Record Keeping

**Request Log:**
- Maintain log of all data subject requests
- Include: date, type, identity, status, response date, outcome
- Retain for audit and compliance purposes

**Response Records:**
- Keep copies of responses sent
- Document any refusals and reasons
- Maintain evidence of verification

**Retention:**
- Request logs: 7 years (for audit and compliance)
- Response records: 7 years

---

## 9. Staff Training

**Training Requirements:**
- All staff who may receive requests must be trained
- Training upon hire and annually
- Training must cover:
  - Types of requests
  - Verification procedures
  - Response timeframes
  - Data collection methods
  - Response preparation
  - Record keeping

**Designated Handlers:**
- Designate specific staff to handle requests
- Ensure handlers are trained and available
- Provide escalation procedures

---

## 10. Contact Information

**Data Subject Request Contact:**
- Email: [Data Protection Email]
- Phone: [Contact Phone]
- Address: [Organisation Address]
- Web Form: [Request Form URL]
- API: `/api/gdpr/access`, `/api/gdpr/delete`, `/api/gdpr/export`

**Data Protection Officer:**
- Name: [DPO Name]
- Email: [DPO Email]
- Phone: [DPO Phone]

**Supervisory Authority:**
- [UK: Information Commissioner's Office (ICO)]
- Website: https://ico.org.uk
- Phone: 0303 123 1113

---

## Appendix A: Request Templates

### Access Request Acknowledgment

Subject: Acknowledgment of Your Data Access Request

Dear [Data Subject Name],

Thank you for your data subject access request. We have received your request and are processing it.

**Your Request:**
- Request Type: Access to personal data
- Request Date: [Date]
- Expected Response Date: [Date + 30 days]

We will provide you with:
- Confirmation of whether we process your personal data
- Access to your personal data
- Information about how we process your data

If you have any questions, please contact us at [Contact Information].

Sincerely,
[Organisation Name]

### Deletion Request Confirmation

Subject: Confirmation of Data Deletion

Dear [Data Subject Name],

We have processed your request for deletion of your personal data.

**Actions Taken:**
- User account deleted: [Date]
- Query logs deleted/anonymised: [Date]
- Cached data cleared: [Date]

**Data Retained (if applicable):**
- [List any data retained and reason, e.g., audit logs retained for 7 years for legal compliance]

Your personal data has been permanently deleted from our systems, subject to any legal retention requirements.

If you have any questions, please contact us at [Contact Information].

Sincerely,
[Organisation Name]

---

**Document Owner:** Miles Waite  
**Last Updated:** January 2026  
**Next Review:** January 2027
