# Change Management Guidelines   Numerical Identifiers

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
Vena CopilotChange Management Guidelines:
Numerical Identifiers
Overview
Vena numerical identifiers will increase from 18 digits to 19 digits on April 29th, 2021. This will
not affect any pre-existing IDs as those will remain unchanged at 18 digits in length. However, all
Vena Support Team
Updated 1 year ago
06/01/2026, 14:06 Change Management Guidelines: Numerical Identifiers – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059701151-Change-Management-Guidelines-Numerical-Identifiers 1/5

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
What's New in Vena: Fall '23IDs made after April 29th, 2021 will have 19 digits. Read on to learn more about this change and
how it may impact you.
Q & A
What are numerical identifiers and where do I find them?
These identifiers (IDs) are assigned to all entities in Vena ie) Data Models, Dimensions, Members,
ETL Jobs, Templates, Processes, etc.
What is the change?
IDs that are made after April 29th, 2021 will have 19 digits instead of 18 digits. For example, if a
new member in a data model is created, this new member will have a member ID with 19 digits.06/01/2026, 14:06 Change Management Guidelines: Numerical Identifiers – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059701151-Change-Management-Guidelines-Numerical-Identifiers 2/5

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
User Audits & Vena Support UserWhy is this happening?
IDs are stored internally using a “long” data type that has a maximum value of
9223372036854775807, which is 19 digits long. These identifiers are based in part on the current
date and time and increase in value as time passes. On April 29th, 2021 we will reach the upper
limit of 18 digit IDs and automatically increase to 19 digits. A change like this will not be required
again within the next 20 years.
What can I do to avoid a service disruption?
If you currently utilize the following use cases please reach out to Vena Support and they will be
able to assist you.
Contact Vena Support if you:
1. Use Custom scripts to pull and store IDs as a “string” data type that only accepts 18 digits or
another data type that assumes the value fits into 18 digits.
Example: If you have a script that pulls IDs from Vena and the script only accepts18 digits, the
script would need to be updated to accept 19 digits.
Resolution: Update the script to allow for 19 digits.06/01/2026, 14:06 Change Management Guidelines: Numerical Identifiers – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059701151-Change-Management-Guidelines-Numerical-Identifiers 3/5

Tenant Access
What's New in Vena: Spring '22
Release
See all 30 articles2. Use Vena-produced IDs to sort items such as data model members using an alphanumeric
sort.
Resolution: Reach out to Vena Support as the new IDs will take precedence.
Was this article helpful?
3 out of 3 found this helpful
Related articles
Troubleshooting: Common Report Book
ProblemsRecently viewed articles
What's New in Vena: Summer '21
What's New in Vena: Fall '21 Release
What's New in Vena: Winter '22 Release
What's New in Vena: Spring '22 Release
Change Management Guidelines: User Audits
& Vena Support User Tenant Access06/01/2026, 14:06 Change Management Guidelines: Numerical Identifiers – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059701151-Change-Management-Guidelines-Numerical-Identifiers 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request06/01/2026, 14:06 Change Management Guidelines: Numerical Identifiers – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059701151-Change-Management-Guidelines-Numerical-Identifiers 5/5
