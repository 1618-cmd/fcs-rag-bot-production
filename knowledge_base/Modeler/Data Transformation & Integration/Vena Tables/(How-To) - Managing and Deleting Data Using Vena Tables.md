# (How To)   Managing and Deleting Data Using Vena Tables

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Vena Tables Search
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
ETL JobsHow-To: Managing and Deleting Data
Using Vena Tables
Need to create an integration that is too complex to achieve with a standard channel
setup? Use Vena Tables to stage data, store Drill Transactions and use it as a query
for VenaQL.
Laura Harris
Updated 2 months ago
02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 1/22

Data Querying
Vena Tables
Explainer: Set Staging or
Transactions Tables When
Building a Vena Table
How-To: Exporting Data From a
Vena Table
How-To: Managing and Deleting
Data Using Vena Tables
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
Troubleshooting DataWhy use this feature?
With the introduction of Vena Tables, we have built on our existing integration functionality and
are empowering users to perform complex data transformations quickly and easily. Vena Tables
function as a data repository for staging data, storing Drill Transactions and as a source for
queries in VenaQL.
Before you begin
To follow the instructions in this article, you will need Modeler access. Additionally, if you are
unfamiliar with the Vena Integration tool, please read the main Integration article series (with a
focus on Part 2 and Part 3) before proceeding.

Table of contents
How to
Create a Vena Table
Option 1: Create a Vena Table object
Create a Vena Table destination
Create a new channel
Option 2: Create a template
Delete all rows from a Vena Table
Delete one or multiple rows from a Vena Table02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 2/22

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
Vena Ad HocNotes & limitations
How to
Create a Vena Table
There are two methods that you can use to create Vena Tables. These options are dependent on
your data source. If you wish to use data that is not available as a file (e.g., data from an external
source system such as Netsuite or Salesforce), please proceed to Option 1.If you have a file
containing data that you wish to load, please proceed to Option 2.
Option 1: Create a Vena Table object
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Channels from the sidebar tab.
4. Select Create from the upper right-hand corner of the screen.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 3/22

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates5. Select Vena Table from the drop-down menu.
In the pop-up modal, follow the prompts to create your new Vena Table:
AEnter a unique table name (may contain letters and numerals).
BEnter unique column names for each column (may contain letters and numerals). Note that
leading and trailing whitespaces are not allowed in the column names.
CSelect a data model from the drop-down menu.
 DSelect Create. 02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 4/22

Create a Vena Table destination
A Vena Table destination is required to populate a table from a source other than a direct File to
Vena Table ETL job.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 5/22

1. Once you have created your Vena Table Object, select Create in the upper-right corner of the
screen.
2. Select Destination from the drop-down menu.
3. In the pop-up modal, follow the prompts to create your new destination:
ACreate a unique destination name.
BSelect Vena Table as your Destination Type from the Destination Typedrop-down menu.
CSelect the Vena Table that you just created from the Vena Table drop-down menu.
DIf you wish to incorporate Clear Slices, check the appropriate boxes. Note that if no Clear
Slices in the Vena Table are selected, the data in the Vena Table will be cleared each time
data is loaded to the Vena Table.
EOnce you are satisfied with your Destination, select Create.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 6/22

02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 7/22

02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 8/22

4. Your newly created Destination will appear.
Create a new channel
After creating your new Vena Table destination, the next step is to create a channel to pull in
data from your desired source. For step-by-step instructions on how to create a channel in Vena,
please refer to this article on Destinations, Channels and Field Mappings. When creating the new
channel, make sure you choose the Vena Table destination that you just created as your desired
destination.
1. Select Create from the upper right-hand corner of the screen.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 9/22

2. Select Channel from the drop-down menu.
3. This opens the New Channel pop-up window.
4. Enter a descriptive name into the Channel Name field to help you identify your new channel.
5. Select Save. Your channel will be added to the list on the Set up page, and you will
automatically be taken to the Channel Details interface, where your channel is now ready to
be configured.
6. When configuring your channel, remember to select your newly created Vena Table as the
desired Destination. To do so, select the Add destination button in the upper right-hand
corner of the screen.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 10/22

7. Choose Select Existing Designation from the drop-down menu.
8. A pop-up window opens that provides a list of existing destinations. Select the Vena Table
destination you just created.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 11/22

9. Choose Select to close the window.
10. Select your desired source. In the upper left-hand corner of the screen, select Source.
11. Once you have done so, the fields associated with that source will automatically appear in the
Channel window.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 12/22

12. Map your Source fields to your Destination fields. To do so, right-click a Source to add a field
mapping and double-click to edit mappings. You can also select Map by Name, which02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 13/22

automatically maps matching fields by using direct mapping.
13. If you are satisfied with your channel setup, select Run in the Channel Control Panel to start
the ETL job. If the setup is valid, a message will appear above the Channel Control Panel to
indicate that the Integration job has been added to the ETL queue.
14. To view your job, select Jobs to navigate to the History > ETL Jobs tab to view the status of your
job. Once it is complete, you are now ready to use your new Vena Table as a source in a
VenaQL query.
02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 14/22

Option 2: Create a template
1. Select the Modeler tab.
2. Select Data Modeler in the sidebar.
3. Select ETL Templates.
4. Select +Create Template.This opens the ETL Template Manager drawer.
5. Enter a name for the ETL Template.
6. Select File to Vena Table from the drop-down menu.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 15/22

7. Select an existing table or create a new one.
8. Configure the rest of the steps for your template.
9. Select Add to save the step.
10. Select Save to save the template. This returns you to the ETL Job Schedule page.
11. Select the
 (Run) icon to run your new job.
12. This opens the ETL Template Executiondrawer.
1. Select Choose File. Find the file on your device and open it.
2. Select a File format for the source document.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 16/22

3. Select the File encoding.
4. Select the number of Accepted Invalid Lines.
*The number of acceptable invalid lines allows a user to specify the number of row errors
that can be skipped as part of an import.
13. Select Run. This transfers data from the file into your Vena Table. You can view the progress
of your ETL Job on the ETL Jobs page.Once your ETL Job is complete, you are ready to use the
new Data Model in a Vena Table.
Delete all rows from a Vena Table
This process allows you to remove or delete all of the rows in a Vena table (i.e., make it an empty
table).
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Find the appropriate Vena Table.
4. Preview the table to confirm the structure and header.
02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 17/22

5. Prepare a CSV file with the same column headers but with no rows.
6. Navigate to the Modeler tab.
7. Select the appropriate data model.
8. Select ETL from the sidebar tab.
9. Create a new File-to-Vena table ETL job with the same table name.
10. Ensure there are no Clear Slices configured.
11. Load the empty CSV file into the Vena Table.
02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 18/22

12. Since there are no Clear Slices, the system will delete everything in the Vena Table and
replace it with the source file (an empty table).
Delete one or multiple rows from a Vena Table
This process allows you to remove or delete one or multiple rows in a Vena table.
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Find the appropriate Vena Table.
4. Preview the table and select Export to CSV.
5. Open the exported CSV file in Notepad or Excel. Be careful when using Excel as it may
automatically change the format/values of some columns.
6. Remove the unwanted row(s) and save the CSV File.
7. Navigate to the Modeler tab.
8. Select the appropriate data model.
9. Select ETL from the sidebar tab.
10. Create a new File-to-Vena table ETL job with the same table name.
11. Ensure there are no Clear Slices configured.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 19/22

12. Load the saved CSV file from Step 6 into the Vena Table.
13. Since there are no Clear Slices, the system will delete everything in the Vena Table and
replace it with the source file. The source file now contains all the rows you want, except the
rows we do not want, successfully removing the rows.
Notes & limitations
When a Clear Slice is configured for a column or field, the system deletes all rows in the Vena
Table that match the incoming values. For example, if clearing on Year and incoming data
only includes 2019, all rows with 2019 will be cleared, even if 2018 is also present.
If no Clear Slice is configured, all rows in the Vena Table will be deleted and replaced with
incoming data.02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 20/22

If a Vena Table is used as a source or destination in an ETL job, re-running the job without
unwanted rows may delete those rows from the table, depending on the Clear Slice
configuration.
Each tenant can have a maximum of 100 Vena Tables.
You cannot save or use a Vena Table if any column name contains a backslash (\) character.
Users familiar with Drill Staging and Drill Transactions on SQL staging tables can apply the
same methodology to Vena Tables.
Was this article helpful?
1 out of 1 found this helpful
Related articles
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
How-To: Creating and Managing Data
Permissions
Vena Insights Series (Part 1) - Introduction to
Vena Insights
Explainer: Vena Copilot OverviewRecently viewed articles
How-To: Exporting Data From a Vena Table
Explainer: Set Staging or Transactions Tables
When Building a Vena Table
Troubleshooting: ETL Error Guide
Troubleshooting: MQL Invalid Expression
Syntax When Creating a Calculated Member02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 21/22

How-To: Bulk Attach/Detach Attributes and
Filter by AttributesHow-To: Creating Advanced Integration
Setups With VenaQL
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:55 How-To: Managing and Deleting Data Using Vena Tables – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360022667351-How-To-Managing-and-Deleting-Data-Using-Vena-Tables 22/22
