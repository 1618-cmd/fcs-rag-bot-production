# (How To)   Importing Data to Vena with Microsoft Power Automate Connector

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Power Automate Integration Search
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
ETL JobsHow-To: Importing Data to Vena with
Microsoft Power Automate Connector
Learn how to perform flat file integrations from external source systems with ease by leveraging
the Microsoft Power Automate Connector.
About this feature
Laura Harris
Updated 2 months ago
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 1/20

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
How-To: Importing Data to
Vena with Microsoft Power
Automate Connector
How-To: Exporting Data from
Vena With Power Automate
Connector
Troubleshooting: Power
Automate Flow Error
Automated Template X Not
Found
Power BI Integration
Sage Intacct IntegrationMicrosoft Power Automate is a cloud-based web service that enables you to create automated
data integrations between a source system and Vena. Connectors function as a proxy around an
API that allows the source to communicate with the destination (Vena). More specifically, Power
Automate allows you to connect with external source systems that are unavailable through
Vena's traditional integration methods. The Microsoft Power Automate connector may be used
to import data on an ongoing basis.
For example, when a new file is added to Dropbox, an automated workflow can instantly bring a
copy of the file into the Vena cube. In the Microsoft store, you'll find the Vena ETL connector,
which is designed using a trigger and an action pairing. When a specific trigger occurs, the pre-
defined actions are to follow. In the context of Microsoft Power Automate, a "trigger" is an event
that occurs in your connector's target application. Examples of triggers that may be used include
Dropbox, Google Drive, etc. A pre-defined action is performed in another application whenever a
trigger is prompted. In this instance, the action is to prompt an ETL job in Vena.
Learn more about exporting data from Vena with Microsoft Power Automate.
Before you begin
You will need at least Admin access to follow the instructions in this article. If Data Permissions
are set up in your environment, you will also need the appropriate permissions for the data you
are working with.
Table of contents
How to05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 2/20

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
How-To: Create Automatic
Channel Mapping With Map by
Name
AdminSet up an Application Token
Restrict Permissions
Set up Microsoft Power Automate connector
Monitor your connector
Frequently Asked Questions
How to
Before setting up your Microsoft Power Automate Connector, you must create a corresponding
application token inside Vena. We recommend always making the token first before enabling
Microsoft Power Automate.
Set up an Application Token
1. Log into Vena.io and navigate to the Admin tab.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 3/20

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates2. Select the Application Tokens tab, and select +Add Application Token.
3. Enter a name for your new application token and select Save.
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 4/20

4. Once you have created the token, it will be added to the Application Token list. Navigate to
your newly created token (it may be on the last page) and select the name to highlight it.
Then, navigate to the top of the screen and select Show Token.
5. This will prompt a pop-up window to open containing your token credentials. You can
reference these credentials anytime by selecting the Show Token button.
Restrict Permissions
If you have multiple data models, it is recommended that you restrict the account's permissions
to access only one data model. You can do this by limiting both Application and Data
Permissions.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 5/20

To restrict Application Permissions:
1. Select the +Add Permission button in the Application Permissions list.
2. In the Select Operation drop-down, select Update.
3. In the Select Type drop-down, select Model.
4. Select the model to which you wish to apply the permission.
5. In the Select Dimension drop-down, select All(*).
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 6/20

6. Select Add to add the permission.
7. Once you return to the home screen, highlight the Update All (*) permission and select Delete:
To restrict Data Permissions:
1. Select the +Add Permission button in the Data Permissions list. A pop-up window will open,
and you will be prompted to set the permissions.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 7/20

2. Select the model to which you wish to apply the permission.
3. In the Select Operation drop-down, select the type of Data Permission you wish to add (e.g.,
Write/Read).
4. Select Add to add the permission.
5. Once you have finished modifying your permissions, you will be ready to set up the Microsoft
Power Automate Connector.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 8/20

Set up Microsoft Power Automate connector
1. Log into https://make.powerautomate.com
2. Select Create to start making a flow.
3. Select a flow option based on the type of flow you want. For this example, we'll select
Automated cloud flow.
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 9/20

4. Enter a name for the flow and search for a trigger that works with the Vena ETL Connector.
Triggers that align with the connector include:
Box
One Drive
DropBox
Sharepoint
Google Drive
STFP
In this example, we'll select "SharePoint-when a file is created or modified" as the trigger.
In this context, an item represents a row in a Microsoft SharePoint list. What it is depends on05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 10/20

the user's list. For example, it can be a row in Microsoft Excel or a table in a Word document.
5. Once you choose your trigger, select Create.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 11/20

6. Select the "+" symbol to add an action.
7. Search for Vena in the Add an action task pane.
8. Select Trigger an ETL job to import data into Vena.
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 12/20

9. After selecting the Vena Connector, you will be prompted to enter the API username
(apiUser) and password (apiKey) you sourced from Vena.
10. Once you've entered the credentials, select Create new.
11. To open the task pane, select Trigger an ETL job to import data into Vena. Then, select the
Vena Model and ETL Template (based on those in your Vena environment) that you want to05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 13/20

connect.
05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 14/20

12. Select Save. If your flow contains errors, you'll be prompted to resolve them. Once your flow
saves successfully, you can test it.
13. Select Test to trigger the action.
Monitor your connector
1. Once you have finished creating your connector, you can check its status at any time by
selecting My Flows.
 Info
If you try to connect to a model and encounter an error, make sure that the
correct permissions are configured for the API token and the model.05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 15/20

2. You can also view the resulting data load in Vena's ETL history. Navigate to the Modeler tab >
History page to find your ETL job. Select the Job Name and then select the Download icon
to download and view the contents of the uploaded file.
3. If you need to delete or pause your flow, navigate to My Flows, select your flow, and select
Turn off (pause) your flow or Delete (delete).05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 16/20

Frequently Asked Questions
What is Microsoft Power Automate?
Microsoft Power Automate is a cloud-based web service that allows you to create automated
data integrations between a source system and Vena. Connectors function as a proxy around an
API that allows the source to communicate with the destination (Vena).05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 17/20

Where can I monitor the progress of Integrations?
You can track connections in Microsoft Power Automate via the My Flows tab and monitor their
progress in Vena.io by accessing the ETL Jobs tab in the Modeler.
What triggers are compatible with Vena?
The following triggers can be connected with Vena using the Microsoft Power Automate
connector:
OneDrive
SharePoint
Dropbox
Box
GoogleDrive
SFTP

Notes & limitations
The file size limit for the Microsoft Power Automate connector is 100 MB. Learn more about
Microsoft Power Automate limitations. 05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 18/20

Was this article helpful?
1 out of 2 found this helpful
Related articles
How-To: Exporting Data from Vena With
Power Automate Connector
Reference: ETL Guide - 3 - Command Line ETL
How-To: Set Up a Business Central Connector
and Data Feed
How-To: Adding Users to a Vena Tenant
How-To: Enabling Line Item Details (LIDs) in a
Template or ReportRecently viewed articles
Troubleshooting: QuickBooks Data Feed
Column Names Not Working in Data Feed
Troubleshooting: QuickBooks Unable to Pull
Historical Data
How-To: Set Up a Quickbooks Connector and
Data Feed
Troubleshooting: Error Receiving Data from
NetSuite: NetSuite Encountered an
Unexpected Error
Troubleshooting: Error Receiving Data from
NetSuite: java.lang.Exception: An Unexpected
Error Has Occurred05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 19/20

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:37 How-To: Importing Data to Vena with Microsoft Power Automate Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360026365992-How-To-Importing-Data-to-Vena-with-Microsoft-Power-Automate-Connector 20/20
