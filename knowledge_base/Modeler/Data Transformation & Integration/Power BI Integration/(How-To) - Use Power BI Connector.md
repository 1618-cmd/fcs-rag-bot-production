# (How To)   Use Power BI Connector

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Power BI Integration Search
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
ETL JobsHow-To: Use Power BI Connector
Create incredible data visualizations and share your results with colleagues in Power
BI.
**Please contact your Account Manager to enable this feature.**
Laura Harris
Updated 8 months ago
05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 1/18

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
How-To: Use Power BI
Connector
How-To: Visualizing Data in the
Power BI Connector on Desktop
by Creating a Rollup Value
Measure
Explainer: Power BI Connector
Member Aliases
How-To: Clear or Refresh
Permissions in Power BI
Troubleshooting: Vena Insights
Connector Table Relationship IsWhy use this feature?
Interactive data visualization can offer unique and valuable perspectives on your business, and
organizations are increasingly using data analytics tools like Power BI to crunch their datasets
and unlock these insights. To help you visualize your Vena data with Power BI, we’re introducing
a Vena Connector for Power BI.  In this article, you will learn how to import data from Vena for
use in Power BI, as well as what kinds of data you need to import.
Before you begin
You will need the appropriate Application Permissions to work with the data model(s) you want
to export, and (if applicable) the necessary Data Permissions for the data therein.
You will also need to make note of your API User ID and generate an API Key in Vena.
Table of contents
How to
Import a Data Model Hierarchy
Setting up Auto-Refresh
Notes and Best Practices
Resources
Source API User ID/Key05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 2/18

Not Auto-Detected
Troubleshooting: Vena Insights
Connector Invalid Application
Token Provided
Troubleshooting: Vena Insights
Connector SigntoLevel Column
Not Available
Troubleshooting: Vena Insights
Connector Failed to Update
Data Source Credentials
Troubleshooting: Vena Insights
Connector Users Able To See
Data Models They Don’t Have
Access To
Troubleshooting: Vena Insights
Connector Load and Transform
Data Buttons Grayed Out
Troubleshooting: Vena Insights
Connector Data Model
Intersections or Values Table Is
Blank
Troubleshooting: Vena Insights
Connector Intersection Values
Showing as Zero
Troubleshooting: Unable To
Connect to Vena InsightsPower BI Version Overview
How to
With Power BI, you can import both hierarchies and values in a way that is optimized for Power
BI. This means that you can directly import the files into Power BI, with no need to first reformat
or manipulate the data. As a result, this process can be easily repeated on a routine basis to
update your Vena data in Power BI.
In this guide, we will look at how to perform data imports in Power BI.  Additional information
and instructions on building reports are available in Power BI's documentation.
Import a Data Model Hierarchy
You can choose to import either all of the dimensions in a data model at once or individual
dimensions separately.
 Shared Members in Power BI
If your data model contains shared members, these will also be included in an import
of your data model hierarchy. However, you will need to manually establish the
relationship between values in shared members.05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 3/18

Connector
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
How-To: Create Automatic
Channel Mapping With Map by
Name1. Download and install Power BI Desktop, which is an application that runs on your local
computer. You can download Power BI Desktop directly or access the online version.
Alternatively, your organization may choose to purchase the Pro version of Power BI. See an
overview of the different offerings from Power BI here.
2. Open Power BI and locate the navigator pane, select Get Data and then navigate to the
bottom of the drop-down menu and select More:05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 4/18

Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 5/18

3. Select the Other tab to locate the Vena Connector. Scroll through the available connectors
until you find Vena. Select the connector and then select Connect.
4. Select a source region. You can find your source region by logging into vena.io and viewing
the region listed in the URL.05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 6/18

5. Select an endpoint and then select option v2.
6. Next, you’ll be prompted to enter an API User ID and API Key token (learn how to access your
API User ID and API Key here). Enter your credentials into the appropriate fields and select
Connect.
7. In the Navigator window, select the appropriate data set and select the desired dimensions.
Select Load when you’re finished.05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 7/18

 Note
Once you have established your source region and entered your API User ID and User Key,
you do not need to re-enter your API credentials each time you log in. Simply select your
source region (e.g. US2) and you will be directly taken to the Navigator window. 05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 8/18

8. Once you have loaded your data, you are ready to use Power BI to create a variety of reports
and visualizations. For further instructions and tutorials on how to use Power BI, visit the
Power BI website for articles and walkthroughs.
Suggested reading:
Create a report from a dataset
Create dashboards
Use Q&A to explore your data

Setting up Auto-Refresh
Ensure that you always have up-to-date data in your dashboards with Power BI Auto-refresh.
1. Find the data set in the PowerBI web service.05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 9/18

2. After you have located your data set, select the Refresh button in the Actions column.
3. Select Data Source Credentials > Edit Credentials.
05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 10/18

4. Edit your credentials (use your API Username and API Key to do this).
05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 11/18

5. Manually refresh your data and then schedule your refresh.
Notes & Best Practices
The Power BI connector is available to customers on a private Vena cloud tenant. We will
work with your organization to set up the integration.
Power BI does not have any concept of roll-up operators, which are the symbols you can set in
the Vena Data Modeler that determine how a child member rolls up to its parent (e.g., +/add,
-/subtract, and ~/ignore). This means that these operators are not included when you import
your data model hierarchy from Vena. Power BI will calculate roll-ups exclusively as summed
totals, so for hierarchies that use the -/subtract or ~/ignore operators, the roll-ups you see in
Power BI may differ from those you see in Vena.05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 12/18

In Vena, values are typically stored in database intersections. However, some values are not
stored in the database, but rather calculated dynamically when they are queried (e.g., viewed
on a template). The types of non-stored values are roll-up values (i.e., the values associated
with non-bottom-level members); values for intersections defined by a calculated member
and values generated by .read Calcs. These values cannot be exported from Vena, so they will
not be available when you import Vena data into Power BI.
While importing the data model hierarchy into Power BI is optional (but recommended),
importing just a partial set of dimensions from your data model is also possible. If you do
this, the hierarchical relationships will be available for the dimension that was imported, and
unavailable for the dimensions that were not. If the granularity is not essential for a given
dimension, you may elect not to import its hierarchy. However, as a best practice, we
strongly recommend importing your full hierarchy wherever possible to preserve flexibility.
While this issue is not specific to imports of Vena data, it is worth noting that Power BI can
sometimes have difficulty automatically identifying the header row in an imported file. To
resolve this, use the Use First Row as Headers function in the Power BI Query Editor.
Resources
Source API User ID/Key
1. To access your APIUser and APIKey, navigate to vena.io, select your username and navigate
to the tab labeled Application Tokens. This is the recommended authorization and
authentication method for Power BI.
Note05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 13/18

2.  Select the Copy button (
)  to copy/paste your API User ID and API Key from Vena into
Power BI.
2.) Power BI Version overview
The option to create or manage application tokens is only available from your
user profile page if your Vena admin has enabled the setting. Learn how to
troubleshoot if you can't see your application token. Learn how to locate your
application token. 05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 14/18

Overview of the features and functionality associated with each version of Power BI. The version
that you choose will be dependent upon your business needs:
Feature ProPremium
Get Data into Power BI
Get Vena Data into Power BI ✔ ✔
Create dashboards or reports
Create Dashboards or Reports in Power BI using Vena
data✔ ✔
Update dashboards or reports with the latest data
Update Dashboards or Reports created in Power BI
using Vena data with the latest Vena data✔ ✔
Automatically update Dashboards or Reports created in
Power BI using Vena data with the latest Vena data✔ ✔05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 15/18

Share dashboards or reports
Collaborate with coworkers to create meaningful
reports and dashboards in workspaces on
app.powerbi.com✔ ✔
Bundle those dashboards and reports into apps and
distribute them to a larger group or your whole
organization.✔ ✔
Create shared datasets that your coworkers can use as
the basis for their reports in their workspaces.✔ ✔
Create a template app to distribute to external Power BI
users via Microsoft AppSource.✔ ✔
Share dashboards or reports with other licensed users,
from the service or the Power BI mobile apps.✔ ✔05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 16/18

Was this article helpful?
7 out of 8 found this helpful
Related articles
How-To: Visualizing Data in the Power BI
Connector on Desktop by Creating a Rollup
Value Measure
Reference: Writing Expressions (MQL & HQL)
Vena Insights Series (Part 1) - Introduction to
Vena Insights
Vena Insights Series (Part 2) - Building
Dashboards With Vena Insights
How-To: Use Clear Slices to Clear
Intersections During an ETL LoadRecently viewed articles
Troubleshooting: Power Automate Flow Error
Automated Template X Not Found
How-To: Exporting Data from Vena With
Power Automate Connector
How-To: Importing Data to Vena with
Microsoft Power Automate Connector
Troubleshooting: QuickBooks Data Feed
Column Names Not Working in Data Feed
Troubleshooting: QuickBooks Unable to Pull
Historical Data05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 17/18

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:40 How-To: Use Power BI Connector – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360035636892-How-To-Use-Power-BI-Connector 18/18
