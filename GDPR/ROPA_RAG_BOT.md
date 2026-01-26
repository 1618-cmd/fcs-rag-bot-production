# Record of Processing Activities (ROPA)
## FCS RAG Bot System

**Document Version:** 1.0  
**Date:** January 2026  
**Author:** Miles Waite  
**Review Date:** Quarterly or when processing activities change  
**Next Review:** April 2026

---

## 1. Controller Information

**Controller Name:** [Organisation Name]  
**Contact Details:** [Contact Information]  
**Data Protection Officer (if applicable):** [DPO Name and Contact]  
**Supervisory Authority:** [Relevant UK/EU Supervisory Authority]

---

## 2. Processing Activities

### 2.1 User Account Management

**Processing Activity:** User account creation, authentication, and management

**Categories of Data Subjects:**
- Employees and contractors using the FCS RAG Bot service
- Administrators managing the system

**Categories of Personal Data:**
- Email address (required)
- Full name (optional)
- Password (stored as hash, not personal data)
- User identifier (UUID)
- Tenant/organisation identifier
- User role (admin, modeler, contributor, viewer)
- Account creation timestamp
- Last login timestamp
- Account status (active/inactive)

**Purposes of Processing:**
- User authentication and authorisation
- Access control and role-based permissions
- Account management and administration
- System security and fraud prevention
- Multi-tenancy support (organisation isolation)

**Legal Basis:**
- Article 6(1)(b) GDPR - Contractual necessity
- Justification: Processing is necessary to provide user access to the service and manage user accounts as part of the service contract.

**Recipients of Data:**
- Internal: System administrators, support staff
- Third-party processors: Hosting provider (Render), Database provider (PostgreSQL), Authentication services

**International Transfers:**
- Data may be transferred to United States (hosting providers)
- Safeguards: Standard Contractual Clauses (SCCs) with processors

**Retention Period:**
- Active accounts: Retained while account is active
- Inactive accounts: Retained for 30 days after deactivation, then permanently deleted
- Audit logs: 7 years (for legal compliance)

**Security Measures:**
- Password hashing using bcrypt
- Encryption in transit (HTTPS/TLS)
- Encryption at rest (database encryption)
- Role-based access control
- Authentication required for all access
- Regular security assessments

---

### 2.2 Query Processing and Response Generation

**Processing Activity:** Processing user queries through RAG (Retrieval-Augmented Generation) system

**Categories of Data Subjects:**
- Users submitting queries to the RAG Bot
- End users whose queries may contain business or personal information

**Categories of Personal Data:**
- User identifier (linked to account)
- User email address
- Query text (may contain business information, technical details, or indirect personal data)
- Generated responses (may contain synthesised information)
- Source documents referenced
- Timestamp of query
- Response latency metrics
- Tenant/organisation identifier

**Purposes of Processing:**
- Provide AI-powered technical support and assistance
- Generate responses to user queries about Vena platform
- Analyse and explain VenaQL calculation scripts
- Improve system performance and response quality
- Debugging and system maintenance
- Usage analytics and system improvement

**Legal Basis:**
- Article 6(1)(b) GDPR - Contractual necessity (for service delivery)
- Article 6(1)(f) GDPR - Legitimate interest (for query logging and analytics)
- Justification: Query processing is necessary to deliver the core service. Query logging is necessary for system improvement, debugging, and analytics, and is balanced against user privacy through retention limits and anonymisation options.

**Recipients of Data:**
- Internal: System administrators, support staff (for debugging and support)
- Third-party processors: 
  - OpenAI (United States) - Processes queries to generate responses using GPT-4o
  - Qdrant Cloud (EU/United States) - Stores query embeddings for semantic search
  - Hosting providers (Render, Vercel) - Application logs may contain query data
  - Redis provider - Cached queries and responses

**International Transfers:**
- Data transferred to United States (OpenAI, hosting providers)
- Data may be transferred to United States (Qdrant Cloud, depending on cluster location)
- Safeguards: Standard Contractual Clauses (SCCs) with all processors, Data Processing Agreements (DPAs)

**Retention Period:**
- Query logs: 90 days from creation, then automatically deleted
- Cached queries/responses: 24 hours (Redis TTL), then automatically expired
- Audit logs: 7 years (for legal compliance)

**Security Measures:**
- Encryption in transit (HTTPS/TLS) for all API calls
- Encryption at rest for database storage
- Access controls restrict query log access to authorised personnel
- Input validation and sanitisation
- Rate limiting to prevent abuse
- Regular security monitoring

---

### 2.3 Calculation Script Analysis

**Processing Activity:** Analysis of uploaded VenaQL calculation scripts and code files

**Categories of Data Subjects:**
- Users uploading calculation scripts for analysis
- Users whose business data may be embedded in scripts

**Categories of Personal Data:**
- User identifier (linked to account)
- Uploaded file content (calculation scripts, code files)
- File metadata (filename, size, upload timestamp)
- Analysis results and recommendations
- May contain business-sensitive information or indirect personal data

**Purposes of Processing:**
- Analyse VenaQL calculation scripts for errors, syntax issues, or optimisation opportunities
- Provide technical guidance and recommendations
- Explain script functionality and components
- Troubleshoot calculation script issues
- Core service functionality

**Legal Basis:**
- Article 6(1)(b) GDPR - Contractual necessity
- Justification: Processing uploaded scripts is necessary to provide the core analysis functionality of the service.

**Recipients of Data:**
- Internal: System administrators (for support and debugging)
- Third-party processors:
  - OpenAI (United States) - Processes script content to generate analysis and recommendations
  - Hosting providers - Application logs may contain script content

**International Transfers:**
- Data transferred to United States (OpenAI, hosting providers)
- Safeguards: Standard Contractual Clauses (SCCs), Data Processing Agreements (DPAs)

**Retention Period:**
- Scripts processed in real-time and not stored separately
- If script content included in query logs: Subject to 90-day retention period
- No separate storage of script files

**Security Measures:**
- Encryption in transit (HTTPS/TLS)
- File size limits and validation
- Input sanitisation
- Access controls
- Scripts processed in memory, not persisted to disk separately

---

### 2.4 Document Management and Knowledge Base

**Processing Activity:** Management of knowledge base documents through approval workflow

**Categories of Data Subjects:**
- Administrators uploading and managing documents
- Users whose information may be referenced in knowledge base documents (indirect)

**Categories of Personal Data:**
- Administrator identifier (for document uploads and approvals)
- Document files and content (technical documentation, may contain indirect personal data)
- Document metadata (filename, size, upload date, approval status)
- Approval/rejection decisions and timestamps
- Document version history

**Purposes of Processing:**
- Manage knowledge base content through staging, approval, and archiving workflow
- Maintain approved documentation for RAG system
- Track document lifecycle and versioning
- Ensure quality and accuracy of knowledge base

**Legal Basis:**
- Article 6(1)(b) GDPR - Contractual necessity
- Justification: Document management is necessary to maintain the knowledge base that powers the RAG service.

**Recipients of Data:**
- Internal: Administrators, content managers
- Third-party processors:
  - AWS S3 (United States) - Document storage
  - Qdrant Cloud (EU/United States) - Document embeddings for semantic search

**International Transfers:**
- Data transferred to United States (AWS S3)
- Data may be transferred to United States (Qdrant Cloud, depending on cluster location)
- Safeguards: Standard Contractual Clauses (SCCs), Data Processing Agreements (DPAs)

**Retention Period:**
- Approved documents: Retained as part of knowledge base (indefinite, as required for service)
- Rejected/archived documents: Retained according to organisation document retention policy
- Document metadata: Retained while document is in system

**Security Measures:**
- Encryption at rest (S3 encryption)
- Encryption in transit (HTTPS/TLS)
- Access controls (admin-only for document management)
- Version control and audit trail
- Secure file upload validation

---

### 2.5 System Analytics and Monitoring

**Processing Activity:** System performance monitoring, error tracking, and usage analytics

**Categories of Data Subjects:**
- Users whose interactions generate analytics data
- Users whose queries may appear in error logs

**Categories of Personal Data:**
- Aggregated usage statistics (anonymised)
- Error logs (may contain query fragments, user identifiers)
- Performance metrics (response times, system health)
- User identifiers (for usage analytics, if not anonymised)

**Purposes of Processing:**
- Monitor system performance and availability
- Identify and resolve technical issues
- Analyse usage patterns for system improvement
- Generate reports for stakeholders
- Security monitoring and threat detection

**Legal Basis:**
- Article 6(1)(f) GDPR - Legitimate interest
- Justification: System monitoring and analytics are necessary for maintaining service quality, security, and continuous improvement. Processing is balanced through anonymisation where possible and retention limits.

**Recipients of Data:**
- Internal: System administrators, technical team, management
- Third-party processors:
  - Sentry (United States) - Error tracking and performance monitoring
  - Hosting providers - Application and infrastructure logs

**International Transfers:**
- Data transferred to United States (Sentry, hosting providers)
- Safeguards: Standard Contractual Clauses (SCCs), Data Processing Agreements (DPAs)

**Retention Period:**
- Error logs: 90 days (aligned with query log retention)
- Performance metrics: 90 days
- Aggregated analytics: Indefinite (anonymised, no personal data)
- Security logs: 7 years (for compliance)

**Security Measures:**
- Log encryption
- Access controls on log data
- Anonymisation of personal data in aggregated analytics
- Secure log storage
- Regular log review and rotation

---

## 3. Third-Party Processors

### 3.1 Processor Register

| Processor Name | Location | Data Processed | DPA Status | Transfer Safeguards | Review Date |
|----------------|----------|----------------|------------|---------------------|-------------|
| OpenAI | United States | User queries, calculation scripts, generated responses | [Status to be verified] | SCCs, DPA | [Date] |
| Qdrant Cloud | EU/United States | Document embeddings, query embeddings | [Status to be verified] | SCCs (if US), DPA | [Date] |
| Render | United States | All application data, database backups, logs | [Status to be verified] | SCCs, Terms of Service | [Date] |
| Vercel | United States | Frontend application logs, analytics | [Status to be verified] | SCCs, Terms of Service | [Date] |
| Sentry | United States | Error logs, performance data, stack traces | [Status to be verified] | SCCs, DPA | [Date] |
| AWS S3 | United States | Document files, knowledge base content | [Status to be verified] | SCCs, DPA | [Date] |
| Redis Provider | [Location] | Cached queries and responses | [Status to be verified] | SCCs (if outside EEA) | [Date] |
| PostgreSQL Provider | [Location] | All database data (accounts, query logs) | [Status to be verified] | SCCs (if outside EEA) | [Date] |

**Note:** DPA status and transfer safeguards must be verified and documented. This register must be updated when processor relationships change.

---

## 4. Data Subject Rights

The following rights are available to data subjects and are documented in the Privacy Policy:

- Right of access (Article 15)
- Right to rectification (Article 16)
- Right to erasure (Article 17)
- Right to restriction of processing (Article 18)
- Right to data portability (Article 20)
- Right to object (Article 21)

Procedures for handling data subject requests are documented separately in the Data Subject Request Procedures document.

---

## 5. Security Measures Summary

**Technical Measures:**
- Encryption in transit (HTTPS/TLS) for all data transmission
- Encryption at rest for databases and storage systems
- Secure password hashing (bcrypt)
- Authentication and authorisation controls
- Role-based access control
- Input validation and sanitisation
- Rate limiting
- Security monitoring and logging

**Organisational Measures:**
- Access controls and user authentication
- Regular security assessments
- Staff training on data protection
- Incident response procedures
- Data breach notification procedures
- Regular review of processing activities

---

## 6. Review and Maintenance

This ROPA must be reviewed and updated:
- Quarterly (every 3 months)
- When new processing activities are introduced
- When third-party processors change
- When retention periods change
- When legal basis for processing changes
- Upon request from supervisory authority

**Last Updated:** January 2026  
**Next Review:** April 2026  
**Document Owner:** Miles Waite

---

## 7. Approval

This Record of Processing Activities has been reviewed and approved by:

**Data Protection Officer / Legal Counsel:** _________________ Date: _______

**Technical Lead:** _________________ Date: _______

**Compliance Officer:** _________________ Date: _______

---

**Appendix A: Glossary**

- **RAG:** Retrieval-Augmented Generation - AI system that retrieves relevant documents and generates responses
- **VenaQL:** Query language for the Vena financial consolidation platform
- **DPA:** Data Processing Agreement
- **SCCs:** Standard Contractual Clauses
- **EEA:** European Economic Area
- **TTL:** Time To Live (cache expiration)
