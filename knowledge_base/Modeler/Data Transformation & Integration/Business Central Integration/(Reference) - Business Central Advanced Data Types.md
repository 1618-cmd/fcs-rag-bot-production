# (Reference)   Business Central Advanced Data Types

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
ETL JobsReference: Business Central Advanced
Data Types
Overview
When setting up a Microsoft  Dynamics for Business Central data  feed in V ena, you may select the
Advanced  option  to bring in data from any table in your Business Central instance . With the Advanced
Laura Harris
Updated 1 year ago
05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 1/11

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
Table Vena Trial Balance Bufferdata type option , you can access any data from Business Central using the Table No. and import
custom fields from Business Central objects.  A Table No. is a unique numerical identifier that identifies
specific table s in your instance of Business Central . This identifier is  used by the Advanced Data Type
to load the table data into V ena.

Before you begin
To follow the instructions in this article, you must  download the Business Central V ena Extension and
have Modeler  access to vena.io.  Learn how to install the extension.

Table of contents
Reference Guide
Find a Table No. in Business Central
Use the Advanced data type to retrieve data
Limitations
Reference Guide
Find a Table No. in Business Central05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 2/11

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
Destinations
Standard tables with IDs and fields can be found online. Please note that these resources are
not necessarily complete and accurate, or up to date. For cases where the table can’t be found
through online resources, please follow the steps below to find a Table No. in the Business
Central user interface.05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 3/11

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
Product Updates1. Sign in to your instance of Business Central and navigate to the appropriate tab.
In this example, we’ll use the Vendor table. You must go to the appropriate page (Employee,
Vendor, etc.) depending on your query.
2. . Once you’ve  selected your table, select  the question mark  icon. In the side panel,  select  Help
and Support  in the Other Resources  section.05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 4/11

05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 5/11

3. In the dialogue box, select Inspect pages and data .
4. . A side panel  titled Page Inspection  opens .  A field called Table will list the table name and , in
brackets, the Table No. In the example below , the Table is “Vendor ”, and the Table No. is “23”. 05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 6/11

Use the Advanced data type to retrieve data
Once you’ve retrieved your Table No. from Business Central, you can create a new Advanced
data type feed in Vena.
1. Open vena.io and navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Data Feeds from the sidebar tab.
4. Select + Add New. This opens the New Data Feed drawer.
5. Follow the steps in the New Data Feed drawer.
1. Step 1: Select Business Central. Select Next: Select Connection.
2. Select the desired connection.
3. Select the environment (i.e., Sandbox or Production) and then select Next: Select Data.
4. Enter a name for the data feed.
6. Type or select the Advanced data type.
7. Input the Table No. that you retrieved from Business Central into the Table No. field and then
select Submit.  05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 7/11

The data feed will connect to the selected table in Business Central, and you can see its
associated fields in the Data Fields field.
8. After a brief loading period, the Data Fields field will be populated with the data from the
selected table. Using the multi-select drop-down menu, you can select the fields to bring into
Vena.05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 8/11

9. Once the data fields are selected, you can enter an OData filter to restrict the data response to
only the records that match the specified criteria.
Limitations
Only one table can be selected per data feed. Use multiple data feeds to import data from multiple
tables.  05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 9/11

Each Advanced data feed can have a maximum of 20 fields.

Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Business Central Data Filtering
How-To: Set Up a Business Central Connector
and Data Feed
How-To: Downloading the Business Central
Vena Extension
Reference: Writing Expressions (MQL & HQL)
Vena Insights Series (Part 4) - Managing
Calculations: Measures, Calculated Tables &
ColumnsRecently viewed articles
How-To: Set Up a Business Central Connector
and Data Feed
Troubleshooting: ETL Load Produces “Invalid
Char Between Encapsulated Token and
Delimiter” Error
Troubleshooting: ETL Data Load With Bulk
Insert Option Does Not Import Commas (,)
Correctly
Troubleshooting: Upload Via ETL Tool Causes
Out of Memory Exception
Troubleshooting: Command Line Tool - Access
Denied05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:22 Reference: Business Central Advanced Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903678732813-Reference-Business-Central-Advanced-Data-Types 11/11
