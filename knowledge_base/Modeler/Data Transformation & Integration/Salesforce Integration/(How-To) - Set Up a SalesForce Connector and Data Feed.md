# (How To)   Set Up a SalesForce Connector and Data Feed

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Salesforce Integration Search
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
ETL JobsHow-To: Set Up a SalesForce
Connector and Data Feed
Learn more about native connectors and data feeds (how to edit, delete, preview, etc.).
Table of contents
How to
Laura Harris
Updated 7 months ago
05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 1/13

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
How-To: Set Up a SalesForce
Connector and Data Feed
Troubleshooting Data
Transformation
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal SourcesSalesforce connection
Set up a Salesforce connector
Salesforce data feed
Set up a Salesforce data feed

How to
Salesforce connection
The Salesforce connection allows you to create and store an access token in Salesforce.
Set up a Salesforce connector
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Connections from the sidebar tab.05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 2/13

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
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot4. Select + New Account.
5. Select Salesforce from the drop-down menu.
6. When you create a new connection and select Salesforce as the account type, an additional
ﬁeld will appear.
7. Select either Production or Sandbox as your chosen Environment, depending on how you
intend to use the connector.
05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 3/13

Product Updates8. Select Connect.
9. You will be redirected to the Salesforce login page. Enter your Salesforce credentials and
select Log In.05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 4/13

05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 5/13

Salesforce data feed10. After successfully logging in, you will be asked if you want to allow Vena to access certain
aspects of your Salesforce account. Select Allow to continue.
11. This will connect your Salesforce account to Vena. The new Salesforce connection will now
appear under your Available Accounts list.  05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 6/13

With the Salesforce data feed type, you can extract data from your Salesforce account. Queries
for data are structured in the Salesforce Object Query Language (SOQL). A reference for SOQL is
available from Salesforce here.
Set up a Salesforce data feed
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Data Feed from the sidebar tab.
4. Select the + Add New button.
5. In the Add New Data Feed pop-up, you will be guided through a four-step integration process
that begins with selecting your source. Once you have selected your source, selectNext:05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 7/13

Select Connection:
6. Use the radio buttons to select the connection you wish to use. Once you have done this,
select Next: Feed Details:05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 8/13

7. With the Salesforce data feed type, you can extract data from your Salesforce account.
Queries for data are structured in the Salesforce Object Query Language (SOQL). A reference
for SOQL is available from Salesforce here.05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 9/13

05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 10/13

A
Name:Use this field to create a unique identifier for your data feed.
B
SOQL Query field: Used to define the data you want to pull from Salesforce as a SOQL
query. For a SOQL reference guide, see this page.
C
Include deleted records checkbox (optional): Used to specify if you want to include
records you have previously deleted in Salesforce among the dataset to be extracted.
D
Add Another Feed (optional): Used to create additional feeds from the same Salesforce
source.05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 11/13

8. Once you have entered the appropriate Feed Details, select Next: Summaryto view a
summary of the information. If you are satisfied with all the details, selectAdd Data Feed.
9. When you save a new data feed, it is added to the list in the Transform & Load page and
marked with a yellow icon
 indicating that it is a data feed, and a logo identifying the data
feed type. From here, you can leverage your native connectors as Sources.
Was this article helpful?
1 out of 1 found this helpful
Related articles
How-To: Set Up a Quickbooks Connector and
Data Feed
How-To: Set Up a Business Central Connector
and Data Feed
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple Reports
How-to: Vena Integration: Part 5 -
DestinationsRecently viewed articles
Troubleshooting: Error With Intacct Request:
IP Address Denied
Troubleshooting: ResultID From Sage Has X
Fewer Remaining Records Than Expected
Troubleshooting: Sage Intacct ETL Error - The
Service Is Temporarily Offline
Troubleshooting: Sage Intacct ETL Error Check
the Fields Exist and Try Again05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 12/13

How-to: Vena Integration: Part 6 – Channels &
Field MappingsTroubleshooting: Response From Intacct – the
Period Filter Is Required
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:51 How-To: Set Up a SalesForce Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034939171-How-To-Set-Up-a-SalesForce-Connector-and-Data-Feed 13/13
