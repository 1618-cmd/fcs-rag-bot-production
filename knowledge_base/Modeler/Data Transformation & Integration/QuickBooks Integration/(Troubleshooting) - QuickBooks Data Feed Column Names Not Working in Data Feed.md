# (Troubleshooting)   QuickBooks Data Feed Column Names Not Working in Data Feed

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/QuickBooks Integration Search
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
ETL Jobs
Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite IntegrationTroubleshooting: QuickBooks Data Feed Column Names
Not Working in Data Feed
Issue summary
When setting up your QuickBooks (QBO) data feed to bring in specific columns, you may realize it doesn't work even after you specify the
column names you want.
Mendez Dixon
Updated 1 year ago
05/01/2026, 12:33 Troubleshooting: QuickBooks Data Feed Column Names Not Working in Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17167356300557-Troubleshooting-QuickBooks-Data-Feed-Column-Names-Not-Working-in-Data-Feed 1/4

QuickBooks Integration
How-To: Set Up a Quickbooks
Connector and Data Feed
Troubleshooting: QuickBooks
Unable to Pull Historical Data
Troubleshooting: QuickBooks
Data Feed Column Names Not
Working in Data Feed
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
Deleted
Suggested solution
1. Vena will return a default list if it does not recognize the specified columns.
The recommended columns are listed below. You can copy and paste the intended fields.
tx_date,account_name,subt_nat_amount,nat_open_bal,account_num,memo,txn_type,name,class,customer,klass_name,cust_name,vend_name,dept_name
2. Alternatively, the column indexes can be used instead of the column names:
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16...
05/01/2026, 12:33 Troubleshooting: QuickBooks Data Feed Column Names Not Working in Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17167356300557-Troubleshooting-QuickBooks-Data-Feed-Column-Names-Not-Working-in-Data-Feed 2/4

How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
Cause
Vena may not recognize the columns specified due to improper column names, spelling errors, or inaccurate syntax.
Keywords
QBO, Column names, Quick book column, Data feed, Data feed connection
Was this article helpful?05/01/2026, 12:33 Troubleshooting: QuickBooks Data Feed Column Names Not Working in Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17167356300557-Troubleshooting-QuickBooks-Data-Feed-Column-Names-Not-Working-in-Data-Feed 3/4

0 out of 1 found this helpful
Recently viewed articles
Troubleshooting: QuickBooks Unable to Pull Historical Data
How-To: Set Up a Quickbooks Connector and Data Feed
Troubleshooting: Error Receiving Data from NetSuite: NetSuite Encountered an Unexpected Error
Troubleshooting: Error Receiving Data from NetSuite: java.lang.Exception: An Unexpected Error Has Occurred
Troubleshooting: NetSuite An nlobjSearchFilter Contains an Invalid Operator
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:33 Troubleshooting: QuickBooks Data Feed Column Names Not Working in Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17167356300557-Troubleshooting-QuickBooks-Data-Feed-Column-Names-Not-Working-in-Data-Feed 4/4
