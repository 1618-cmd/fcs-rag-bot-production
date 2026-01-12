# (How To)   Downloading the Business Central Vena Extension

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
ETL JobsHow-To: Downloading the Business
Central Vena Extension
Why use this feature?
Vena Support Team
Updated 8 months ago
05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 1/13

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
Table Vena Trial Balance BufferCreate a direct connection between your Microsoft Dynamics Business Central ERP data and
Vena. With the Business Central Vena extension, you can instantly connect your Dynamics
Business Central ERP data directly to Vena for financial planning, reporting and analysis.
Before you begin
To follow the instructions provided in this article, you must have at least Modeler access.
You also need:
Caution
Data entered into custom fields or tables cannot be accessed and pulled into Vena by
the Business Central connector.
Note
You must sign a contract addendum before downloading the Business Central
extension. Please contact your Account Manager for more details and information on
how to get started with the Business Central Connector.05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 2/13

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
Destinations Login credentials for a Business Central account with (EXTEND. MGT. - ADMIN) access to
install the Vena Business Central extension in that environment.
You must assign a license to the user via the Microsoft Entra admin center (previously
known as the Azure Active Directory), and then sync users in Business Central.
This account must also have permission to access the data you're trying to pull.
As a best practice, use an account designated for integration. You should NOT be using
individual profiles for integrations. Sticking to this best practice mitigates the risk of integration
issues if an individual in your organization changes roles or leaves the company.
To establish the connection, the account used to grant Vena access to Business Central must
have:
1.  “Read and Write” permissions to the environment in Business Central
2.  “Vena Connector - All” permission set in Business Central.
1. The “Vena Connector - All” permission becomes available to assign after you have installed
the Vena extension in your Business Central instance.
Table of contents
How to
Install the Business Central Vena Extension
Update the Business Central Vena Extension
I encountered an error, what do I do?
Assign VENA CONNECTOR-ALL permission to a user
What if I want to apply the permission for multiple companies?05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 3/13

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
Product Updates How to
Install the Business Central Vena Extension
1. Copy and paste this URL into your internet search bar:
https://businesscentral.dynamics.com/[TENANT  ID]/?noSignUpCheck=1&filter=%27ID%27%20IS%20
2. Before you select ENTER, replace “[TENANT ID]”with your unique Microsoft Entra (Azure)
tenant ID.
3. When the page loads, selectyour environmentand then select Install. Please note that
extensions in Business Central apply only to the environment they are installed in.
4. Next,you’ll be prompted to choose your language.SelectEnglish - Canadaand then select
Install.05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 4/13

5. Your extension will begin to install.
6. Once your Vena installation is complete, you will see the Vena extension in the Business
CentralInstalled Extensions window.
7. To accessInstalled Extensions, open the search bar in Business Central, type in “Extensions”
and select Extension Management.05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 5/13

8. The Vena extension will be available in your Installed Extensions window.

Update the Business Central Vena Extension
If you’ve previously installed the Vena Extension, you can update to the latest version of the
extension. Updating to the latest version will ensure you have the latest features, performance,05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 6/13

and security improvements Vena has released to the extension.
1. Navigate to the Dynamics 365 Business Central Admin Center.
2. Navigate to the Environments tab.
3. Find the Vena extension in the list, and then select Install update.
 The installation in progress  will be visible  in the Environment Operations menu.
An alternative way to update the extension is to remove the Vena extension and then reinstall it.
You can uninstall the extension via the Extension Management page in Business Central, and05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 7/13

then reinstall it following the steps in the Install the Business Central Vena Extension section of
this article.
1. Assign the user for the integrationtheVENA CONNECTOR-ALL permission. If you’re unsure
how to assign the permission, check out the section below.
Assign VENA CONNECTOR-ALL permission to a user
1. Navigate to https://businesscentral.dynamics.com and log in.
2. Open the search menu and enter “user” in the input field.
I encountered an error, what do I do?
The most common reasons you might see an error are insufficient permissions or if
the extension was previously downloaded.
Insufficient Permissions: If you don’t have appropriate permissions, you will receive
the following error message: You do not have sufficient permissions to manage
extensions. Please contact your administrator.
Extension already installed: If the extension is already installed, the status will
display as Failed, and the summary will indicate that an extension with that
application ID is already installed in the environment.05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 8/13

3. Select Users from the search results.
4. Locate your user on the table and select their name to open their user card.
5. Select New Line and type “vena” or the horizontal ellipses to open the Permission Set Lookup
window. 05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 9/13

6. Enter “vena connect” in the input field and then select the VENA CONNECTOR permission
set.
7. You should now see the VENA CONNECTOR-ALL permission set in the table.
Now that the permission set is applied, you must assign the new permission to a specific
company.05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 10/13

8. Navigate to the Company drop-down menu and select your company.
9. Your VENA CONNECTOR-ALL permission set is now assigned.
What if I want to apply the permission for multiple companies?
Each Business Central instance connects to specific environments (for example,
Production and Sandbox). If you have more than one company in a single
environment and you want to apply the VENA CONNECTOR-ALL permission to each
one, you must create a new line for each subsequent company.
05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 11/13

Was this article helpful?
2 out of 3 found this helpful
Related articles
How-To: Set Up a Business Central Connector
and Data Feed
Reference: Business Central Connector
Custom Extension Fields
Vena Insights Series (Part 1) - Introduction to
Vena Insights
Explainer: Vena User Roles
How-To: Using Vena on a Mac or Office Online
With the Tasks TabRecently viewed articles
Reference: Business Central Data Filtering
Reference: Business Central Advanced Data
Types
How-To: Set Up a Business Central Connector
and Data Feed
Troubleshooting: ETL Load Produces “Invalid
Char Between Encapsulated Token and
Delimiter” Error
Troubleshooting: ETL Data Load With Bulk
Insert Option Does Not Import Commas (,)
Correctly
05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 12/13

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:24 How-To: Downloading the Business Central Vena Extension – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21330876043405-How-To-Downloading-the-Business-Central-Vena-Extension 13/13
