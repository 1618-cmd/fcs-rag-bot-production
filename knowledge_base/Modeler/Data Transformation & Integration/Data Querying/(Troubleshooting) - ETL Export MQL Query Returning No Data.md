# (Troubleshooting)   ETL Export MQL Query Returning No Data

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Data Querying Search
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
ETL JobsTroubleshooting: ETL Export MQL
Query Returning No Data
Issue summary
When trying to export data via the ETL export tool, the MQL query entered may return no data.
When you preview it, you will receive the following message: No results found.
Olalekan Adebayo
Updated 1 year ago
02/01/2026, 16:50 Troubleshooting: ETL Export MQL Query Returning No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717996966669-Troubleshooting-ETL-Export-MQL-Query-Returning-No-Data 1/5

Data Querying
How-To: Using the Query Agent
to Build MQL Expressions (Beta)
Reference: Writing Expressions
(MQL & HQL)
Reference: Using Wildcard in
Model Slice Expression
Troubleshooting: ETL Export
MQL Query Returning No Data
How-To: Creating Advanced
Integration Setups With VenaQL
Troubleshooting: MQL Invalid
Expression Syntax When
Creating a Calculated Member
Troubleshooting: ETL Error
Guide
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
Suggested solution
1. Check and confirm there is data in those intersections in the cube.
2. Check that you have the necessary data permission to view the data.
3. Check that your MQL query is using BOTTOMLEVEL, since all data is stored at the bottom
level of all intersections in Vena.
In this example, the function used is CHILDREN and since these are all parent-level
intersections, no data is returned.
To fix this, change the query to dimension('Account':bottomlevel('OPEX')) and the data is
returned.
4. To check if your query returned the desired results, select Preview and move the Raw Output
toggle to ON. 02/01/2026, 16:50 Troubleshooting: ETL Export MQL Query Returning No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717996966669-Troubleshooting-ETL-Export-MQL-Query-Returning-No-Data 2/5

QuickBooks Integration
Power Automate
Integration
Power BI Integration
Sage Intacct Integration
Salesforce Integration
Troubleshooting Data
Transformation
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feeds
& Connections
How-to: Vena Integration: Part 4
– Import and Export API
How-to: Vena Integration: Part 5 -
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Keywords
etl export, no data, nothing to display, mql02/01/2026, 16:50 Troubleshooting: ETL Export MQL Query Returning No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717996966669-Troubleshooting-ETL-Export-MQL-Query-Returning-No-Data 3/5

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
Product UpdatesWas this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Reference: Using Wildcard in Model Slice Expression
Reference: Writing Expressions (MQL & HQL)
How-To: Using the Query Agent to Build MQL Expressions (Beta)
How-To: Checking the ETL Tool Version
How-To: Setting up Email Notifications for ETL Jobs
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:50 Troubleshooting: ETL Export MQL Query Returning No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717996966669-Troubleshooting-ETL-Export-MQL-Query-Returning-No-Data 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:50 Troubleshooting: ETL Export MQL Query Returning No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717996966669-Troubleshooting-ETL-Export-MQL-Query-Returning-No-Data 5/5
