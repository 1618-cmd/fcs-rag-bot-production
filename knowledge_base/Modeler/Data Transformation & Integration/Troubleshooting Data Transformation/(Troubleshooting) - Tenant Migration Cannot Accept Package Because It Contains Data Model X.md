# (Troubleshooting)   Tenant Migration Cannot Accept Package Because It Contains Data Model X

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration
/Troubleshooting Data TransformationSearch
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Calcs (Scripts)
Data Transformation &
Integration
ETL JobsTroubleshooting: Tenant Migration
Cannot Accept Package Because It
Contains Data Model X
Issue summary
When performing a tenant-to-tenant migration, you may encounter the following error: Errors:
Cannot accept package because it contains Data Model with ID X
Olalekan Adebayo
Updated 2 years ago
05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 1/6

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
QuickBooks Integration
Power Automate
Integration
Power BI Integration
Sage Intacct Integration
Salesforce Integration
Troubleshooting Data
Transformation
Troubleshooting: Tenant
Migration Missing Member
With ID X Error
Troubleshooting: Tenant
Migration Missing Model X
Error
Suggested solution
This error means the data model has been migrated in the past and it already exists in the
destination tenant. Tenant migration doesn't migrate intersection data so if you are looking to
get the data updated, you have to manually export the intersection data from the source tenant
and then manually import it into the destination tenant.
To do this:
1. De-select the data model from the migration package and resend the migration.
2. If there are any structural changes in the model, we suggest manually updating it in the
destination model.
3. If you need to migrate the data model again, first delete the data model from the destination
tenant and migrate it again.
Warning05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 2/6

Troubleshooting: Tenant
Migration Cannot Accept
Package Because It Contains
Data Model X
Troubleshooting: Tenant
Migration Domain Alias,
ApiUser, ApiToken Must Not Be
Empty
Troubleshooting: Tenant
Migration Authentication Failed
for Application User
Troubleshooting: Tenant
Migration HTTP 401
Unauthorized Error
Troubleshooting: Tenant
Migration Folder With Matching
ID Is Hidden
Troubleshooting: Vena Export
API 200 OK - Records Returned
Is 0 or Blank
Troubleshooting: Vena Export
API 400 Bad Request Status
Code
Troubleshooting: Vena Import
& Export API 401 Unauthorized
Status CodeCause
This may occur if you are trying to migrate a data model from the source tenant to a destination
tenant but the model has been migrated in the past so it already exists in the destination tenant.
Keywords
cannot accept package, contained data model, tenant migration error
Was this article helpful?
0 out of 0 found this helpful
Deleting a data model will delete all its dimensions and intersection data. Migration
of a data model from one environment will only migrate the dimensions and
members but not the intersection data. To get the intersection data, you have to
export it from the source environment and import it into the destination
environment.05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 3/6

Troubleshooting: Vena Import
& Export API 403 Forbidden
Status Code
Troubleshooting: Vena Import
& Export 404 Not Found Status
Code
Troubleshooting: Vena Import
& Export API 405 Method Not
Allowed Status Code
Troubleshooting: Vena Import
API 406 Invalid Accept Header
Status Code
Troubleshooting: Vena Import
& Export API 422
Unprocessable Entity
Troubleshooting: Vena Export
API 429 Too Many Requests
Status Code
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feeds
& ConnectionsRelated articles
Explainer: Vena User Roles
Troubleshooting: Intersection Mapped to
Calculated Member Not Pulling Any Data
Troubleshooting: Template Automation Error
in the Worker Thread 0
How-To: Installing and Updating the MSI
Version of Vena Desktop
Troubleshooting: ETL - Duplicate Intersections
Found During ImportRecently viewed articles
Troubleshooting: Tenant Migration Missing
Model X Error
Troubleshooting: Tenant Migration Missing
Member With ID X Error
How-To: Set Up a SalesForce Connector and
Data Feed
Troubleshooting: Error With Intacct Request:
IP Address Denied
Troubleshooting: ResultID From Sage Has X
Fewer Remaining Records Than Expected05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 4/6

How-to: Vena Integration: Part 4
– Import and Export API
How-to: Vena Integration: Part 5 -
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:53 Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17930070125453-Troubleshooting-Tenant-Migration-Cannot-Accept-Package-Because-It-Contains-Data-Model-X 6/6
