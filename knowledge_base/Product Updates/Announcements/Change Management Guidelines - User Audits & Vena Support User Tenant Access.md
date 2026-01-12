# Change Management Guidelines   User Audits & Vena Support User Tenant Access

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Product Updates/Announcements Search
Getting Started
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena CopilotChange Management Guidelines: User
Audits & Vena Support User Tenant
Access

Overview
Vena Support
Updated 3 years ago
06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 1/8

Product Updates
Vena Software Updates
Vena Desktop Software
Updates
Announcements
Product Release Announcement:
Suppress Zeros Now Available in
Vena Ad Hoc
Product Release Announcement:
SSO Now Available in Vena Ad
Hoc
What's New in Vena: Spring '25
Release
What's New in Vena: Winter '25
Release
What's New in Vena: Fall '24
Release
What's New in Vena: Summer '24
Release
What's New in Vena: Winter '24
What's New in Vena: Fall '23We're introducing new features to vena.io to improve the Vena User Audit and Vena tenant
access control experience. These updates reflect Vena's efforts to apply industry best practices
for information security at the user and tenant levels. These changes will come into effect as of
April 27, 2022.
These changes will impact two key areas:
1. Tenant access by Vena support users
Only customers will be able to extend the access duration for Vena support users.
Clearing Vena support user access at the tenant level will expire all active grants to Vena
support. If Vena support user access at the tenant level is re-enabled, individual users'
previously granted support access remains revoked and must be explicitly re-granted to
permit access.
2. Vena User Audits
The Vena User Audit trail will now capture login information for all users, including logins
through Vena support user access. If a Vena support user performs an action, the User Audit
trail will capture their name as [Vena support user: Name] in the Update Details column.06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 2/8

What's New in Vena: Fall '25
Release
What's New in Vena: Summer '25
Release
Resolved - Change Management:
Important Notice - Excel Version
Compatibility Issue with Vena 365
Whats New in Vena: Spring '24
Release
What's New in Vena: Summer '23
Release
What's New in Vena: Spring '23
Release
What's New in Vena: Winter '23
Release
What's New in Vena: Fall '22
Release
What's New in Vena: Summer '22
Release
Change Management Guidelines:
Microsoft Ending Support for
Internet Explorer
Change Management Guidelines:
User Audits & Vena Support User
Q & A
What are the changes ?
Tenant access by Vena support users
Limiting access to Vena support user parameters: This update will prevent Vena
employees logging in through Vena support user access from extending the duration of Vena
support access beyond the user-specified timeline.
For example, if a user grants Vena support access to their tenant for 24 hours, the Vena
support user, once they've accessed the tenant, cannot extend the authorized time frame
beyond that original 24-hour period.
For more information about how individual users can grant Vena support access to a tenant for a
specified period, check out this article.
Clearing all access authorization at the tenant level:When an Admin disables Vena
support access at the tenant level, this will revoke access authorization granted to Vena
support by individual users.
For example, a Contributor grants Vena support access to their tenant for 30 days. An06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 3/8

Tenant Access
What's New in Vena: Spring '22
Release
See all 30 articlesAdministrator user then disables Vena support user access at the tenant level. If the
Administrator user re-enables Vena support user access at the tenant level a day later, the
grant made previously by the Contributor user has already been canceled and is not in effect.
For more information about enabling Vena support access at the tenant level, check out this
article. Enabling this feature allows individual users to grant login access to Vena support on an
as-needed basis.
Vena User Audits
User Audits will capture actions taken by Vena support users: The Vena User Audit trail
will now capture login information for all Vena support users.
For example, if an action, such as logging in, is performed by a Vena support user, that
information will be captured by the User Audit in the Update Details column.
For more information about leveraging User Audits to track and monitor user activity, check out
this article.
Why is this happening?
These feature updates are being implemented in order to give Vena Admins more visibility into
and control over Vena support user access to ensure that access is appropriate to each
customer's unique business and security needs.06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 4/8

How can I balance support needs with security?
Vena support user access allows Vena employees to access your tenant during a support
investigation, during implementation, or for a managed services contract. You control whether
access is enabled at the tenant level, and users must explicitly grant access at the user level for
any Vena support users to have access. In addition, Vena has an approval workflow and internal
tool for granting a Vena employee access to a tenant that has enabled Vena support user access.
For a Vena employee to access your tenant as a Vena support user, all three of these things
must be enabled:
The "Allow users to grant login access to Vena support personnel" setting must be turned on
at the tenant level.
The individual customer user needs to have granted Login Access to Vena support and that
access needs not to have expired.
The Vena employee needs to be granted access through our internal tool.06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 5/8

If you are in a managed services contract, the recommended configuration is to leave Vena
support user access enabled at the tenant level, and for one Admin user at the user level. You
can then leverage the User Audits table to review who has logged into your account and validate
that the accesses make sense.
During implementation
If your tenant is undergoing implementation work by our Professional Services organization, the
recommended configuration is to leave Vena support user access enabled at the tenant level,
and for one user with the required roles and permissions (e.g. Administrator, Manager, Modeler)
at the user level. You can then leverage the User Audits table to review who has logged into your
account and validate that the accesses make sense.
After implementation
If your tenant is in production and not under a managed services contract or undergoing
additional implementation work, the recommended setting is to disable Vena support user
access at the tenant level and to enable it only during a support investigation. When a support
ticket is opened, we recommend you enable Vena support user access at the tenant level, and at
the user level for a user with the same roles and permissions for the user requiring support. The
duration of the user level grant should be 7 days in most cases to ensure Vena support can both
triage the error and verify any product fix that may be required to address it. When the support
ticket is closed, you can then disable Vena support user access at the tenant level.06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 6/8

Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Change Management Guidelines: Microsoft Ending Support for Internet Explorer
What's New in Vena: Summer '22 Release
What's New in Vena: Fall '22 Release
What's New in Vena: Winter '23 Release
What's New in Vena: Spring '23 Release
Didn't find what you're looking for?
Our application support team is ready to help.06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 7/8

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request06/01/2026, 14:04 Change Management Guidelines: User Audits & Vena Support User Tenant Access – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/5811455417997-Change-Management-Guidelines-User-Audits-Vena-Support-User-Tenant-Access 8/8
