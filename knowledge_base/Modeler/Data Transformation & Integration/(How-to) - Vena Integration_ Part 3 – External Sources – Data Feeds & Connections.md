# (How to)   Vena Integration  Part 3 – External Sources – Data Feeds & Connections

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration Search
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
ETL JobsHow-to: Vena Integration: Part 3 –
External Sources – Data Feeds &
Connections
About this series
This series is all about how to use Vena Integrations. You are in Part 3, which describes the
process for integrating and synchronizing data from multiple external source systems that can
Vena Support
Updated 1 month ago
05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 1/18

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
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feedsbe directly connected with Vena.
Vena Integration is a large and complex tool, and it continues to grow. We've broken down the
information in this series into manageable parts, each focusing on a specific area of the
Integration tool and its related concepts.
This series was designed to be read in order. If you don't have any previous experience with the
Integration tool, we recommend that you follow this approach, starting with Part 1. But if you are
familiar with Integration, feel free to explore around for what you need.
Part 1: Feature Overview
Part 2: Internal Sources
Part 3: External Sources – Data Feeds & Connections – you are here
Part 4: External Sources – Import and Export API
Part 5: Destinations
Part 6: Channels & Field Mappings
Video
Check out a video of this article's content.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 2/18

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
Vena Copilot
Product UpdatesVena Integration Part 3: Data Feeds Vena Integration Part 3: Data Feeds
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application
Permissionsfor authorizations.
IfData Permissions are set up in your environment, you will also need the appropriate
permissions for the data that you are working with.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 3/18

Table of contents
About data feeds and connectors
How to
Create a connector
Delete a connector
Create a data feed
Edit a data feed
Delete a data feed
About data feeds and connectors
The basics of Integration involve the following:
1. Creating a source.
2. Linking that source to a destination using a channel.
In Part 2 of this series, we covered internal sources and explained that the Integration tool needs
users to specify the location of the source data and which data to pull from the source.
For external sources, specific data is chosen via data feeds. Vena accesses these external
sources using built-in connectors.
First, set up the connection between Vena and the external source, then create a data feed to
specify which data to pull. Like with internal sources, you can set up multiple feeds for different
datasets.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 4/18

Available external sources (third-party accounts) Vena can directly connect to are:
Salesforce
QuickBooks
Sage Intacct
Business Central
NetSuite
To import data from other sources, you must leverage the Vena Import API.
Vena uses tokens to connect with your third-party accounts, allowing seamless integration
without requiring login credentials (except Intacct, which requires a username and password,
that only needs to be entered once). These secure tokens are stored within the external system,
so you don't need to share your credentials with Vena.
Note
Application Permissions for Connections: When a connection to an external data
feed system is set up, any Integration user with access to that connection can use its
data in the Integration tool.
Because external data feeds may contain sensitive information, restrict access by
limiting who can manage connections. Users need a specific Application Permission
before they can create, view, edit, or delete connections.
The Integration Connection Application Permission controls these abilities, ensuring
that only authorized users can:05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 5/18

How to
Creating a connector
You must set up a connection before creating its data feed.
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar menu.
3. Select Connections, then + New Account.
Select a connection when creating a data feed (limiting data feed access), and
Delete a connection.
Only users with Admin access can set Application Permissions. Learn more about
Application Permissions.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 6/18

4. Select the type of account to set up a connection for, then select Connect.
5. Depending on the type of account you choose, you must complete some additional steps to
finish the connection setup. Each application has a separate article for how to set up its
connection and data feed:
1. Salesforce
2. QuickBooks
3. Sage Intacct
4. Business Central
5. NetSuite
6. Once you have created a connection, it will appear in the Available Accounts section of the
Connections pane. For more information about a connection, select the Edit Connection05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 7/18

pencil icon (
).
Deleting a connector
You can delete a connector at any time. However, if a corresponding data feed relies on the
deleted connector, you will need to enter login credentials each time you use that data feed.
1. Select the Delete Connection icon (
) in line with the connection you want deleted.
05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 8/18

2. A prompt will appear to confirm if you want to delete the connection:
1. Select Preview References to see a list of data feeds and channels that rely on this
connection to work.
2. Select Delete to proceed with the deletion.
Creating a data feed
After establishing your connections, you can create a variety of data feeds. This section provides
general steps for creating a data feed, with specific details available in each connection type's
article.
1. Navigate to the Modeler tab, then select Data Transformations from the sidebar menu.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 9/18

2. Select Data Feeds, then + Add New.
3. The Add New Data Feed flow will guide you through a four-step integration process, beginning
with selecting your source. Select the icon associated with the source you want to use, then
select Next: Select Connection.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 10/18

4. Select the radio button for the connection you want to use or select Create New
[Connector Name] Connection to create a new connection if you haven’t already. Then,
select Next: Select Data.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 11/18

5. The next steps depend on which connector you’re using. The following articles outline steps
specific to each connector:
1. Salesforce
2. QuickBooks
3. Sage Intacct
4. Business Central
5. NetSuite05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 12/18

6. Optional: Select Add another feed to create additional feeds to this connector.
7. Select Next: Summary. This page contains an overview of the data feed information,
including source, connection and any additional data feeds you created.
When you have finished configuring the new data feed, select Add Data Feed. The newly
created data feed will appear on the Data Feeds page.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 13/18

Edit a data feed
1. Right-click or select the vertical ellipses (
) in line with the data feed you want to edit, then
select Edit.
2. Once you've updated your data feed query, select Refresh Data to preview your data with
the applied changes.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 14/18

3. To troubleshoot your data feed further by performing a complete export of all the rows,
select Export to CSV.
4. Once you have finished, select Save Data Feed to retain your changes.

Delete a data feed
Delete a data feed at any time, provided it is not in use by a channel setup. Attempt to delete an
in-use data feed results in an error message. You must remove the data feed from the channel
setup to continue with the deletion.
1. Right-click or select the vertical ellipses (
) in line with the data feed you want to edit, then
select Delete.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 15/18

2. Select Delete in the confirmation message.
Was this article helpful?
6 out of 6 found this helpful05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 16/18

Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Set Up a Quickbooks Connector and
Data Feed
How-To: Create Automatic Channel Mapping
With Map by Name
How-To: Set Up a Business Central Connector
and Data Feed
How-To: Using Dynamic Task Bindings (Vena
365 Only)Recently viewed articles
How-to: Vena Integration: Part 2 – Internal
Sources
How-to: Vena Integration: Part 1 - Feature
Overview
Troubleshooting: Vena Export API 429 Too
Many Requests Status Code
Troubleshooting: Vena Import & Export API
422 Unprocessable Entity
Troubleshooting: Vena Import API 406 Invalid
Accept Header Status Code
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 17/18

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 13:00 How-to: Vena Integration: Part 3 – External Sources – Data Feeds & Connections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005667806-How-to-Vena-Integration-Part-3-External-Sources-Data-Feeds-Connections 18/18
