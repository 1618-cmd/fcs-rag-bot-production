# (How To)   Set Up a Business Central Connector and Data Feed

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Business Central Integration Search
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
ETL JobsHow-To: Set Up a Business Central
Connector and Data Feed
Use Vena's Business Central Connector to automatically and easily import critical
business data for financial planning and reporting.

Sadaf Rahmanian
Updated 4 months ago
05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 1/19

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
How-To: Set Up a Business
Central Connector and Data
Feed
Reference: Business Central
Advanced Data Types
Reference: Business Central
Data Filtering
How-To: Downloading the
Business Central Vena
Extension
Reference: Business Central
Connector Custom Extension
Fields
Troubleshooting: Vena Data
Feed Not Connecting to
Business Central Extension
Troubleshooting: The Record in
Table Vena Trial Balance BufferWhy use this feature?
Create a direct connection between your Microsoft Dynamics Business Central ERP data and
Vena. Using the Vena Native API Connector, you can instantly connect your Dynamics Business
Central ERP data directly to Vena for financial planning, reporting and analysis.
The Business Central Connector imports the following data types:
General Ledger entries with custom dimensions (global and shortcut)
Trial Balance entries with custom dimensions (global and shortcut)
Learn more about the data fields available for import through the Business Central Connector.
Learn more about downloading the Business Central Vena extension.
Before you begin
To follow the instructions in this article:
You will need Modeler access
You must download the Business Central Vena extension
Note
You must sign a contract addendum before downloading the Business Central Vena
extension. Please contact your Account Manager for more details and information on
how to get started with the Business Central Connector.05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 2/19

Already Exists. Identification
Fields and Values
NetSuite Integration
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
DestinationsAs a best practice, use an account designated for integration. You should NOT be using
individual profiles for integrations. Sticking to this best practice mitigates the risk of integration
issues if an individual in your organization changes roles or leaves the company.
To establish the connection, the account used to grant Vena access to Business Central must
have:
1.  “Read and Write” permissions to the environment in Business Central
2.  “Vena Connector - All” permission set in Business Central.
1. The “Vena Connector - All” permission becomes available to assign after you have installed
the Vena extension in your Business Central instance.

Table of contents
1. Set up a Business Central Connector
2. Set up a Business Central Data Feed
3. Reference
1. Trial Balance date filter expressions
2. lastModifiedDateTime filter expressions

How to05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 3/19

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
Product UpdatesSet up a Business Central Connector
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Connections from the sidebar tab.
4. Select + New Account.
Caution
If you already have an existing V1 Business Central Connector Data Feed, you can
convert it to V2. However, the steps below are the same for the GL Entry data type.
Data Fields is a new field that cannot be left empty. Please select data fields to import
via the Data Fields drop-down list and adjust your existing ETL templates and
integration channels to reflect any changes to the imported field. If you do not
specify any fields, Vena will continue to use the V1 Connector, and you will not be
able to change your data fields. 05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 4/19

5. Select Business Central from the drop-down menu.
6. Select Connect.
7. This redirects you to a Microsoft login page. You can select an account you’ve previously
logged into or use another.
05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 5/19

8. Complete the login process through Microsoft. You may need to grant Vena access to the
application as you complete the steps.
Warning
The login credentials you use in this step should be designated for integration.
You should NOT be using individual profiles for integrations. Please ensure the
Business Account you are logging in from is used for integrations exclusively and
that permissions are appropriate for integrations only.
Sticking to this best practice mitigates the risk of integration issues if an individual
in your organization changes roles or leaves the company. By ensuring that the
account is not tied to a specific individual, the integrations can remain intact,
regardless of structural changes in your organization.05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 6/19

9. Business Central is now available under your list of accounts.
Set up a Business Central Data Feed
After the connection is created, you can set up the data feed(s) to determine the data imported
from Business Central to Vena. The fields available provide what is required for building core
financial reports and doing account-level financial planning, plus additional transaction-level
data for drill-down detail. The complete list of fields is here.05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 7/19

1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Data Feeds from the sidebar tab.
4. Select + Add New to open the Add New Data Feed drawer. This guides you through a four-step
integration process.
5. Follow the steps in the Add New Data Feed drawer.05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 8/19

Step 1: Select Business Central, then select Next: Select Connection.
05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 9/19

Step 2: Select the desired connection. Select the environment (i.e., Sandbox or
Production). Select Next: Select Data to proceed to Step 3.
Step 3: Enter a name for the data feed.
Step 4: Type or select a data type:
Trial Balance - Data fields are pre-selected and cannot be altered.
General Ledger (GL) Entry - You must manually select fields to import and adjust your
existing ETL templates and integration channels to reflect any changes to the imported
fields. Use the checkboxes to select your fields or type your entries into the text fields.
Learn more about Business Central fields available in the General Ledger and Trial
Balance data type.
Advanced - For importing fields from any Business Central table, including custom
fields added to standard tables and fields from custom tables. Learn more about the
Business Central Advanced data type. 05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 10/19

Step 5: Review the selections you have made for the data feed. Select Add Data Feed to
confirm your selections.05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 11/19

Your data feed is now set up. A message will notify you that the data feed was successfully
added.
For guidance on performing data transformations and loading data from data feeds
into your data models & transaction tables, please see this article.
Impor tant not es on setting up data feeds
Separate data feeds must be set up for each General Ledger, Trial Balance and Advanced
data type when extracting data from Business Central.
Separate data feeds must be set up for each entity (company) within your Business
Central instance.
Data Type filters for the Business Central Connector use ODATA filter expressions. Refer
to the How-To: Set Up a Business Central Connector and Data Feed for guidance on
writing ODATA filter expressions. For further help with using OData, visit this article
in Microsoft's documentation.
If the Vena Business Central extension has yet to be installed successfully on your
Business Central instance, you will encounter an error when attempting to Preview or
proceed past this step. For steps on installing the Business Central extension, visit this
article.
If you use OData filter expressions that rely on a specific date (for example, dateFilter eq
2023-08-31),you can use the Dynamic Date filter functionality to "set and forget" a filter.
 Vena's Business Central extension does not support the on-prem version of Business Central.
We recommend using the Advanced method to load the Balance sheet data to avoid the possible
timeout issues in future.
Reference05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 12/19

1. Trial Balance dateFilter  expressions
For Trial Balance data feeds, if you use OData filter expressions that rely on a specific date (for
example, dateFilter eq 2023-08-31), you must update the filter monthly to accommodate the
changing filter expression.
In the example below, we will change the expression from dateFilter eq 2023-08-31 to dateFilter
eq 2023-09-30.
1. Open your Trial Balance data feed and navigate to the text input field for Add Filter for this
Data Type.
2. Update your filter in the text field with your new OData expression.
3. Use the Preview pane to confirm that your date filter has been correctly updated.
05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 13/19

Other examples of Trial Balance dateFilter expressions:
Filter Expression Date Range
dateFilter ge 2018-01-01 and dateFilter
le 2020-12-31Trial balance encompassing transactions for
2018,2019,2020 calendar year.
dateFilter ge 2018-01-01 Trial Balance encompassing transactions after and
including Jan 1 2018.
dateFilter le 2022-12-31 Trial Balance encompassing transactions before and
including Dec 31 2022.
2. lastModifiedDateTime  filter expressions
1. lastModifiedDateTime filter –  Modified before Jan.01, 2023
For entries modified before Jan. 01, 2023, use this filter:
lastModifiedDateTime lt 2023-01-01T00:00:00.000Z05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 14/19

2. lastModifiedDateTime filter – Modified after midnight, Dec. 30, 1999
For entries modifed after midnight on Dec. 30 1999, use this filter:05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 15/19

lastModifiedDateTime gt 1999-12-31T00:00:00.000Z
Note: We recommend using gt to ensure midnight entries are captured.
3. lastModifiedDateTime filter – Modified after Dec. 31, 2021
For entriesmodified after Dec. 31, 2021, use this filter:
lastModifiedDateTime ge 2022-01-01T00:00:00.000Z   05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 16/19

For a list of Business Central custom extension fields, visit this article. 05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 17/19

Was this article helpful?
3 out of 3 found this helpful
Related articles
How-To: Downloading the Business Central
Vena Extension
Reference: Business Central Connector
Custom Extension Fields
Troubleshooting: Vena Data Feed Not
Connecting to Business Central Extension
Explainer: Vena User Roles
Explainer: What is Data Model
Standardization?Recently viewed articles
Troubleshooting: ETL Load Produces “Invalid
Char Between Encapsulated Token and
Delimiter” Error
Troubleshooting: ETL Data Load With Bulk
Insert Option Does Not Import Commas (,)
Correctly
Troubleshooting: Upload Via ETL Tool Causes
Out of Memory Exception
Troubleshooting: Command Line Tool - Access
Denied
Troubleshooting: Job Error When Loading
LIDS: Bulk Write Operation Error on Server05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 18/19

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:21 How-To: Set Up a Business Central Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9835585960077-How-To-Set-Up-a-Business-Central-Connector-and-Data-Feed 19/19
