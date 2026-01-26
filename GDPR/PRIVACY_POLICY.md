# Privacy Policy

**Last Updated:** January 2026

## 1. Introduction

This Privacy Policy explains how we collect, use, store, and protect your personal data when you use the FCS RAG Bot service (the "Service"). We are committed to protecting your privacy and ensuring compliance with the General Data Protection Regulation (GDPR) and other applicable data protection laws.

By using the Service, you acknowledge that you have read and understood this Privacy Policy. If you do not agree with this policy, please do not use the Service.

## 2. Data Controller

The data controller responsible for processing your personal data is the organization that provides you with access to the Service. If you have questions about this Privacy Policy or wish to exercise your data protection rights, please contact your organization's administrator or the data protection officer.

## 3. Personal Data We Collect

### 3.1 Account Information

When you create an account or are provided with access to the Service, we collect the following information:

- Email address (required for account identification and authentication)
- Full name (optional, if provided by you or your organization)
- Password (stored in encrypted form using industry-standard hashing)
- User role (admin, modeler, contributor, or viewer)
- Organization or tenant identifier
- Account creation and last login timestamps

**Legal Basis:** We process this data based on contractual necessity (Article 6(1)(b) GDPR) as it is required to provide you with access to the Service and manage your account.

### 3.2 Query and Usage Data

When you use the Service to ask questions or request assistance, we collect:

- Your questions and queries submitted to the Service
- Generated responses and answers provided by the Service
- Source documents referenced in responses
- Response latency and performance metrics
- Whether responses were retrieved from cache
- Timestamps of your interactions

**Legal Basis:** We process this data based on our legitimate interest (Article 6(1)(f) GDPR) in improving the Service, analyzing usage patterns, debugging issues, and maintaining system performance. This processing is necessary for the operation and enhancement of the Service.

### 3.3 Calculation Script Analysis

If you upload calculation scripts or code files for analysis, we process:

- The content of uploaded files (including .docx, .txt, and .venaql files)
- File metadata (filename, size, upload timestamp)

**Legal Basis:** We process this data based on contractual necessity (Article 6(1)(b) GDPR) as it is required to provide the core functionality of the Service, which includes analyzing and providing guidance on calculation scripts.

### 3.4 Authentication Data

When you log in to the Service, we generate and use:

- JWT (JSON Web Token) authentication tokens containing your user identifier, email address, tenant identifier, and role
- Session information stored in your browser

**Legal Basis:** We process this data based on contractual necessity (Article 6(1)(b) GDPR) as it is required to authenticate you and maintain your session with the Service.

### 3.5 Document Management Data

If you have administrative privileges and upload documents to the knowledge base, we collect:

- Document files and their content
- Document metadata (filename, size, upload date, approval status)
- Approval or rejection decisions and associated timestamps

**Legal Basis:** We process this data based on contractual necessity (Article 6(1)(b) GDPR) as it is required to manage the knowledge base that powers the Service.

## 4. How We Use Your Personal Data

We use your personal data for the following purposes:

**Service Delivery:** To provide you with access to the Service, authenticate your identity, process your queries, and generate responses based on the knowledge base.

**Service Improvement:** To analyze usage patterns, identify common questions, improve response quality, and enhance the overall functionality of the Service.

**System Administration:** To manage user accounts, monitor system performance, detect and resolve technical issues, and maintain security.

**Compliance and Legal Obligations:** To comply with applicable laws, respond to legal requests, and protect our rights and the rights of users.

**Analytics and Reporting:** To generate aggregated, anonymized usage statistics and reports for system administrators and stakeholders.

We do not use your personal data for marketing purposes, and we do not sell or share your personal data with third parties for their marketing purposes.

## 5. Third-Party Data Processors

We use the following third-party service providers to process your personal data on our behalf:

**OpenAI (United States):** We send your queries and uploaded calculation scripts to OpenAI's API to generate responses using their language models. OpenAI processes this data according to their privacy policy and data processing agreement.

**Qdrant Cloud (European Union / United States):** We store document embeddings and query embeddings in Qdrant Cloud's vector database to enable semantic search functionality.

**Hosting Providers (United States):** We use cloud hosting providers (Render, Vercel) to host the Service infrastructure. These providers may process your data as part of hosting services, including application logs and database backups.

**Error Tracking Services (United States):** We use error tracking services (such as Sentry) to monitor system errors and performance. These services may receive error logs that could contain portions of your queries or system interactions.

**Caching Services:** We use Redis caching services to improve response times. Cached data may include your queries and responses, stored temporarily for up to 24 hours.

**Database Services:** We use PostgreSQL database services to store your account information, query logs, and other system data.

**Document Storage (AWS S3):** We use Amazon Web Services S3 to store uploaded documents and manage the knowledge base document approval workflow.

All third-party processors are bound by data processing agreements that require them to protect your personal data and process it only in accordance with our instructions and applicable data protection laws. Where data is transferred outside the European Economic Area (EEA), we ensure appropriate safeguards are in place, such as Standard Contractual Clauses approved by the European Commission.

## 6. Data Retention

We retain your personal data only for as long as necessary to fulfill the purposes outlined in this Privacy Policy, unless a longer retention period is required or permitted by law.

**Query Logs:** We retain query logs for 90 days from the date of creation. After this period, query logs are automatically deleted.

**User Accounts:** We retain your account information while your account is active. If your account is deactivated, we retain your account data for an additional 30 days, after which it is permanently deleted.

**Audit Logs:** We retain audit logs (including access logs, security events, and administrative actions) for 7 years to comply with legal and regulatory requirements.

**Cached Data:** Cached queries and responses are automatically deleted after 24 hours.

**Calculation Scripts:** Uploaded calculation scripts are processed in real-time and are not stored separately. If calculation script content is included in query logs, it is subject to the same 90-day retention period as query logs.

**Document Uploads:** Documents uploaded to the knowledge base are retained according to your organization's document management policies. Approved documents become part of the knowledge base. Rejected documents may be archived or deleted according to administrative decisions.

## 7. Your Data Protection Rights

Under the GDPR and other applicable data protection laws, you have the following rights regarding your personal data:

**Right of Access (Article 15):** You have the right to request access to your personal data and receive a copy of the data we hold about you, including your account information and query logs.

**Right to Rectification (Article 16):** You have the right to request correction of inaccurate or incomplete personal data. You can update your email address and full name through your account settings or by contacting your administrator.

**Right to Erasure (Article 17):** You have the right to request deletion of your personal data, subject to certain exceptions (such as when we are required to retain data for legal compliance). If you request deletion, we will delete your account and associated query logs, subject to our retention policies.

**Right to Restriction of Processing (Article 18):** You have the right to request that we restrict the processing of your personal data in certain circumstances, such as when you contest the accuracy of the data or object to processing.

**Right to Data Portability (Article 20):** You have the right to receive your personal data in a structured, commonly used, and machine-readable format and to transmit that data to another service provider.

**Right to Object (Article 21):** You have the right to object to processing of your personal data based on legitimate interests. However, we may continue processing if we have compelling legitimate grounds that override your interests.

**Right to Withdraw Consent:** If we process your personal data based on consent, you have the right to withdraw your consent at any time. Withdrawal of consent does not affect the lawfulness of processing that occurred before withdrawal.

To exercise any of these rights, please contact your organization's administrator or submit a request through the Service's data protection interface (if available). We will respond to your request within 30 days, or inform you if we need additional time.

## 8. Data Security

We implement appropriate technical and organizational measures to protect your personal data against unauthorized access, alteration, disclosure, or destruction. These measures include:

- Encryption of data in transit using HTTPS/TLS protocols
- Encryption of data at rest in databases and storage systems
- Secure password hashing using industry-standard algorithms
- Authentication and authorization controls to restrict access to personal data
- Role-based access control to ensure users can only access data appropriate to their role
- Regular security assessments and monitoring
- Input validation and sanitization to prevent security vulnerabilities

Despite these measures, no method of transmission over the internet or electronic storage is completely secure. While we strive to protect your personal data, we cannot guarantee absolute security.

## 9. International Data Transfers

Your personal data may be transferred to and processed in countries outside the European Economic Area (EEA), including the United States, where some of our third-party service providers are located. When we transfer your personal data outside the EEA, we ensure appropriate safeguards are in place to protect your data, such as:

- Standard Contractual Clauses approved by the European Commission
- Adequacy decisions by the European Commission recognizing that certain countries provide adequate data protection
- Other appropriate safeguards as required by applicable data protection laws

## 10. Children's Privacy

The Service is not intended for use by individuals under the age of 16. We do not knowingly collect personal data from children under 16. If you believe we have collected personal data from a child under 16, please contact us immediately, and we will take steps to delete such information.

## 11. Changes to This Privacy Policy

We may update this Privacy Policy from time to time to reflect changes in our practices, technology, legal requirements, or other factors. We will notify you of any material changes by posting the updated Privacy Policy on the Service and updating the "Last Updated" date. Your continued use of the Service after such changes constitutes your acceptance of the updated Privacy Policy.

## 12. Contact Information

If you have questions, concerns, or requests regarding this Privacy Policy or your personal data, please contact:

- Your organization's administrator (for account-related inquiries)
- The data protection officer or data controller for your organization
- The Service support team through the appropriate channels provided by your organization

If you are not satisfied with our response to your data protection inquiry, you have the right to lodge a complaint with your local data protection supervisory authority.

---

**Document Version:** 1.0  
**Effective Date:** January 2026
