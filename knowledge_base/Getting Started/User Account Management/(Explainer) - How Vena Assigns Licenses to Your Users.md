# (Explainer)   How Vena Assigns Licenses to Your Users

Vena Solutions/Getting Started/User Account Management Search
Getting Started
Fundamentals
User Account Management
Explainer: How Vena Assigns
Licenses to Your Users
Reference: Your Vena Profile
How-To: Reset or Change Your
Password
How-To: Viewing CPE/CPD Credits
and Downloading Certificates
How-To: Linking or Re-linking
Your Microsoft Account to Vena
How-To: Receiving Marketing and
Product Updates From Vena
How-To: Subscribing to
Knowledge Base UpdatesExplainer: How Vena Assigns Licenses
to Your Users
Understanding how Vena assigns licenses ensures you know why a user's required
license and consumed license may not always match.
What determines a user’s required license?
A user’s required license is determined by their highest-level role in Vena:
View Only / Reports →  View Only license
Contributor →  Contributor license
Mia Shabsove
Updated 18 days ago
31/12/2025, 12:07 Explainer: How Vena Assigns Licenses to Your Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/41883188831629-Explainer-How-Vena-Assigns-Licenses-to-Your-Users 1/5

Explainer: Role-Based Licensing
Enforcement in Vena
Support
Product & IT Information
Resources
General Troubleshooting
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesManager, Modeler or Admin →  Power User license
This required license always appears in Admin > Users, even if you don’t have any available
licenses of that type.
How does Vena decide which license a user consumes?
When Vena enforces license limits, it assigns them based on the licenses your
tenant has available.
Vena follows a simple allocation model:
It first tries to assign the required license.
If no licenses of that type are available, Vena assigns the next higher-tier license so the user
can continue working.
License tiers (highest →  lowest):
Power User
Contributor
View Only
This means a View Only user may consume a Contributor or Power User license when lower-tier
licenses are fully used. While the View Only user may consume a different license, the user will
only have View Only privileges.
Why don’t required and consumed licenses always
match?
You may notice:
The Users list shows what license each user requires. 31/12/2025, 12:07 Explainer: How Vena Assigns Licenses to Your Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/41883188831629-Explainer-How-Vena-Assigns-Licenses-to-Your-Users 2/5

The License Overview on the Admin > Policies > General page and Licenses
Summary drawer on the Admin > Users > License Summary page show what your
tenant actually consumes.
Because Vena moves up the license tier when a specific type isn’t available, these two values
often differ.
Example
Imagine you have the following:
Users:
1 Power User
10 View Only users
Available licenses:
2 Power Licenses
4 Contributor Licenses
5 View Only Licenses
Required licenses (based on roles):
1 Power License
10 View Only Licenses
Consumed licenses:
Power User: 2/2 Licenses
Contributor User: 4/4 Licenses
View Only User: 5/5 Licenses31/12/2025, 12:07 Explainer: How Vena Assigns Licenses to Your Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/41883188831629-Explainer-How-Vena-Assigns-Licenses-to-Your-Users 3/5

Why this happens:
Only five View Only licenses exist, so Vena assigns the remaining five View Only users to
Contributor licenses (4) and then Power User licenses (1). This ensures users can continue
working even when the exact license type they require isn’t available.
Was this article helpful?
0 out of 0 found this helpful
Related articles
Explainer: Vena User Roles
Explainer: Role-Based Licensing Enforcement
in Vena
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple Reports
How-To: Adding Vena To Trusted Sites
How-To: Creating and Managing Application
PermissionsRecently viewed articles
Explainer: Is Vena Accessible For People With
Disabilities?
Reference: Vena Glossary
How-To: Access Vena's Training Platform
Explainer: Vena Viewer Role
Explainer: Vena User Roles31/12/2025, 12:07 Explainer: How Vena Assigns Licenses to Your Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/41883188831629-Explainer-How-Vena-Assigns-Licenses-to-Your-Users 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request31/12/2025, 12:07 Explainer: How Vena Assigns Licenses to Your Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/41883188831629-Explainer-How-Vena-Assigns-Licenses-to-Your-Users 5/5
