# (Troubleshooting)   Vena Import & Export API 422 Unprocessable Entity

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
ETL JobsTroubleshooting: Vena Import &
Export API 422 Unprocessable Entity
See a "422 Unprocessable Entity" error code in your V ena import or export API? Read on
to learn how to resolve your issue and get working again.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 1/7

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
ErrorIssue summary
When importing data into your Vena environment via Vena's Import API, you
may get a 422 Unprocessable Entity status code with the error:
"Expected 1 file field in multipart data with same name as partName in input."
Suggested solution
Ensure the correct number of files required by the referenced ETL template
ID has been uploaded, or the path(s) added to your call.
422 - Import - Unprocessable Entity - Expected 1 file field in multipart
data05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 2/7

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
Status CodeKeywords
import API 422 unprocessable entity
Issue summary
When importing data into your Vena environment via Vena's Import API, you
may get a 422 Unprocessable Entity status code with the error:
"No metadata part found in the multipart."
Suggested solution
Ensure your form-data has the correct key-value pairs as shown below.
file: file name or path.422 - Import - Unprocessable Entity - No Metadata part found in the
multipart05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 3/7

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
& Connections metadata: {"input":{"partName":"file","fileFormat":"CSV","fileEncoding":"
Keywords
import API 422 unprocessable entity
Issue summary
When exporting data from your V ena environment via V ena's Export API, you
may receive the following 422 Unprocessable Entity error:  The Export API422 - Export - Unprocessable Entity05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 4/7

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
Product Updatesfeature is currently disabled on your tenant.

Suggested solution
1. Ensure the Export API server property  exportAPIEnabled  has been enabled
in your V ena environment.  See this article for more information on enabling
the API.
2. If the property has been enabled and the issue continues, ensure you are
spelling it exactly as it appears above without any spaces at the end.

Cause
This may occur if you try to use the Export API feature without enabling it in your
Vena environment.

Keywords05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 5/7

export API is disabled
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Vena Import API 406 Invalid Accept Header Status Code
Troubleshooting: Vena Import & Export API 405 Method Not Allowed Status Code
Troubleshooting: Vena Import & Export 404 Not Found Status Code
Troubleshooting: Vena Import & Export API 403 Forbidden Status Code
Troubleshooting: Vena Import & Export API 401 Unauthorized Status Code05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 6/7

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:58 Troubleshooting: Vena Import & Export API 422 Unprocessable Entity – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26702791691533-Troubleshooting-Vena-Import-Export-API-422-Unprocessable-Entity 7/7
