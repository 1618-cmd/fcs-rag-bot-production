# (Troubleshooting)   Vena Export API 200 OK   Records Returned Is 0 or Blank

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
ETL JobsTroubleshooting: Vena Export API
200 OK - Records Returned Is 0 or
Blank
Issue summary
When exporting data from your Vena environment via Vena's Export API, you may notice that no
data is returned (i.e., recordsReturned: 0) despite getting a 200 OK status code.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 1/6

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
Option 1: Ensure you have the necessary data permission to
the data model
1. Log in to vena.io.
2. Navigate to the Admin tab.
3. Select ApplicationTokens.
4. Select the appropriate token name.
5. Ensure the token has data permission access to the referenced data model. If you are using
an application token directly from your profile page, contact your Vena admin to confirm that05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 2/6

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
Status Codeyou have data permission access to the referenced data model.
6. If you do not have the necessary data permission, please select "Add permission" to add the
necessary permission.
Option 2: Check for aggregate functionality
1. Check and ensure all dimension members in your filters query are bottom-level members. In
the current Intersections endpoint, only bottom-level intersection values can be returned.
None of the filter expressions support roll-up functionality to a specified parent member. For
example, if you specify a parent-level member in the “eq” or “in” filter expression, you will not
receive a roll-up of its children. Instead, you will receive a response with empty data.
2. Instead of directly referencing a parent member, you can use the "mx" filter expression to
reference the bottom-level members of that parent member (e.g. { "field": "Account", "mx":
{"bottomLevel": {"name":"Revenue"}}}).
Option 3: Ensure you are using a valid filter query
The filters parameter must be all lowercase and added as a query parameter, not a header. The
filters will not be applied if any part of the filter parameter is capitalized. The filter parameter is
mistakenly capitalized in the example below, so no values are filtered.
Example r equest:
https://{hub}.vena.io/api/public/v1/models/{modelID}/intersections?FILTERS=
[{"field":"Year","eq":"2023"}]05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 3/6

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
& ConnectionsTo resolve this, we need to change it from FILTERS to filters. Read more about the filters
parameter and expressions in this article.
Visit this article to learn to generate example requests that include the filters parameter.
Keywords
export API returns no data
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Tenant Migration Folder With Matching ID Is Hidden
Troubleshooting: Tenant Migration HTTP 401 Unauthorized Error
Troubleshooting: Tenant Migration Authentication Failed for Application User
Troubleshooting: Tenant Migration Domain Alias, ApiUser, ApiToken Must Not Be Empty
Troubleshooting: Tenant Migration Cannot Accept Package Because It Contains Data Model X05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 4/6

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
Product Updates05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:55 Troubleshooting: Vena Export API 200 OK - Records Returned Is 0 or Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26698768138253-Troubleshooting-Vena-Export-API-200-OK-Records-Returned-Is-0-or-Blank 6/6
