# (How To)   Set Up a Quickbooks Connector and Data Feed

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
ETL JobsHow-To: Set Up a Quickbooks
Connector and Data Feed
Visit this article for more information about native connectors and data feeds (how to edit,
delete, preview, etc.) and links to other native connectors.
Table of contents
Laura Harris
Updated 8 months ago
05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 1/15

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
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
Troubleshooting DataHow to
QuickBooks connection
Set up a QuickBooks connector
QuickBooks data feed
Set up a QuickBooks data feed
QuickBooks query
QuickBooks report
How to
QuickBooks connection
Set up a QuickBooks connector
1. Navigate to the  Modeler tab.
2. Select Data T ransformations from the sidebar .
3. Select Connections  from the sidebar tab.
4. Select + New Account .05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 2/15

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
How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
5. Select QuickBooks  from the drop-down menu.
05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 3/15

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates6. You will be redirected to the QuickBooks login page. Here, type in your QuickBooks account
credentials, and select Sign In . 05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 4/15

05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 5/15

QuickBooks data feed
Set up a QuickBooks data feed7. After successfully logging in, you will be asked if you want to allow V ena to access certain aspects
of your QuickBooks account. Select Authorize to continue.
8. Once you have connected your QuickBooks account, select Connect to complete the connection
setup. The new QuickBooks connection will now appear under your Available Accounts list.
 05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 6/15

Open the Modeler tab in vena.io.
Select Data Transformations in the sidebar.
Select the Data Feeds option; once you've opened the page, select the +Add New button.
In the Add New Data Feed window, you will be guided through a four-step integration process
that begins with selecting your source. Once you have selected your source, select Next: Select
Connection:
In the Select Connection box, use the radio buttons to select the connection you wish to use.
Once you have done this, select Next: Select Data:05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 7/15

Set up a QuickBooks query
The QuickBooks Query data feed type is one of two data feed types that can be used to pull data
from QuickBooks Online. This type allows you to create a query using an SQL-like language to
extract a custom data set.05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 8/15

1. New Custom Data:Select QuickBooks Query.
2. Name:Select a unique identifier for your query.
3. Query String field: Used to define the data you would like to extract from QuickBooks using
a QuickBooks Query. A reference guide on how to structure the query can be found here.
4. Add Another Feed (optional): Used to create additional feeds from the same QuickBooks
source.05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 9/15

Set up a QuickBooks report
The QuickBooks Report data feed type is one of two data feed types that can be used to pull in
data from QuickBooks Online. This type allows you to pull in data from QuickBooks Reports.05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 10/15

05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 11/15

1. New Custom Data:Select QuickBooks Report.
2. Name:Select a unique identifier for your report.
3. Report: Used to specify the name string of the QuickBooks report from which you want to
extract data, e.g. BalanceSheet. A reference for the available reports and their name strings
can be foundhere (name strings are under the column "QuickBooks Reports API Endpoint").
4. Columns field(optional): Used to extract only specific columns from the report. To do this,
enter the names of the desired columns, separated by commas (e.g. "Account, Date, Balance").
5. Time Period field(optional): Used to specify the time period for which to pull data. To do this,
enter the appropriate time period value. The accepted values (per QuickBooks) are:
Today
Yesterday
This Week
Last Week
This Week-to-date
Last Week-to-date
Next Week
Next 4 Weeks
This Month
Last Month
This Month-to-date
Last Month-to-date
Next Month
This Fiscal Quarter
Last Fiscal Quarter
This Fiscal Quarter-to-date
Last Fiscal Quarter-to-date
Next Fiscal Quarter05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 12/15

This Fiscal Year
Last Fiscal Year
This Fiscal Year-to-date
Last Fiscal Year-to-date
Next Fiscal Year
6. Add Another Feed (optional): Used to create additional feeds from the same Quickbooks
source.
Once you have entered the appropriate Feed Details, click Next: Summary to view a summary of
the information. If you are satisfied with all the details, click Add Data Feed.
When you save a new data feed, it is added to the list in the Transform & Load page and marked
with a yellow icon
 indicating that it is a data feed, and a logo identifying the data feed type.
From here, you can leverage your native connectors as Sources.
Limitations
Quickbooks is not compatible with Internet Explorer 11 and Edge browsers.05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 13/15

Was this article helpful?
1 out of 2 found this helpful
Related articles
Troubleshooting: QuickBooks Unable to Pull
Historical Data
How-To: Set Up a Sage Intacct Connector and
Data Feed
How-To: Set Up a SalesForce Connector and
Data Feed
How-To: Set Up a Business Central Connector
and Data Feed
How-To: Enable & Add a MDR Insert Row to a
TemplateRecently viewed articles
Troubleshooting: Error Receiving Data from
NetSuite: NetSuite Encountered an
Unexpected Error
Troubleshooting: Error Receiving Data from
NetSuite: java.lang.Exception: An Unexpected
Error Has Occurred
Troubleshooting: NetSuite An
nlobjSearchFilter Contains an Invalid Operator
Troubleshooting: NetSuite Script Execution
Time Exceeded
Troubleshooting: NetSuite Has Encountered
an Error: "null" During ETL05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 14/15

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:32 How-To: Set Up a Quickbooks Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034615472-How-To-Set-Up-a-Quickbooks-Connector-and-Data-Feed 15/15
