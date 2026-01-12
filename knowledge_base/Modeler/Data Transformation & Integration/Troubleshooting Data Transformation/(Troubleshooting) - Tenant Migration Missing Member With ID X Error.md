# (Troubleshooting)   Tenant Migration Missing Member With ID X Error

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
Missing Member With ID X Error
Issue summary
When doing a tenant-to-tenant migration, you may encounter the following error: Errors: Missing
Member with ID X.
Olalekan Adebayo
Updated 2 years ago
05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 1/6

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
1. When migrating components that are linked to dimension members (e.g., a process variable
that is linked to a dimension member), ensure that the dimension members also exist in the
destination tenant's data model with the same name and member ID.
2. This is common when you have migrated the data model in the past but the model has new
members in the source tenant that are being referenced and are not yet in the destination
tenant. Create the same dimension member with the same member ID in the appropriate
data model in the destination tenant.
3. Once you find the new dimension member(s) in your source tenant, export the member with
its member ID.
4. Log in to the destination tenant, import the hierarchy file that was downloaded from the
source tenant and ensure the member IDs remain the same.
Note05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 2/6

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
This may occur if you try to migrate a component that is linked to a dimension member in the
source tenant but that dimension member does not exist in the destination tenant.
Keywords
missing member, tenant migration error
 Just creating a new dimension member in your destination model with the same
name will not work. Use a hierarchy import job so it creates the member with the
same name and member ID as the source tenant.
This could also happen when migrating/receiving Vena's Pre-Configured Solution
Packages. You may already have received a packaged solution (the most common
would be the Finance cube ID 651628815408562176), but you may not have the
latest hierarchies and members created as part of the Foundation Revamp. When
migrating a solution, you’re also migrating a process with pre-set process
variables tagged to the following members: PlanningMethod: Regular Planning,
PlanScenario: Plan. These members must also be created with the same name
and member ID. Reach out to the Support team to solve this issue. 05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 3/6

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
& ConnectionsWas this article helpful?
0 out of 0 found this helpful
Recently viewed articles
How-To: Set Up a SalesForce Connector and Data Feed
Troubleshooting: Error With Intacct Request: IP Address Denied
Troubleshooting: ResultID From Sage Has X Fewer Remaining Records Than Expected
Troubleshooting: Sage Intacct ETL Error - The Service Is Temporarily Offline
Troubleshooting: Sage Intacct ETL Error Check the Fields Exist and Try Again05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 4/6

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
Product Updates05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:52 Troubleshooting: Tenant Migration Missing Member With ID X Error – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18000796802317-Troubleshooting-Tenant-Migration-Missing-Member-With-ID-X-Error 6/6
