# (How To)   Maintaining Dimension Member IDs When Updating Existing Members

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs Search
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
ETL JobsHow-To: Maintaining Dimension
Member IDs When Updating Existing
Members
Update existing dimension members in bulk while maintaining member IDs.
Olalekan Adebayo
Updated 5 months ago
02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 1/13

ETL Job Errors &
Troubleshooting
Reference: ETL Guide - 1 -
Overview
Reference: ETL Guide - 2 -
Vena.io ETL
Reference: ETL Guide - 3 -
Command Line ETL
Reference: ETL Guide - 4 -
Query Languages
Reference: ETL Guide - 5 - SQL
Staging Environment
Reference: ETL Guide - 6- Using
Staging Data
How-To: Exporting Data From a
SQL Staging Table
How-To: Create and Manage a
Data Model Hierarchy Using
ETL Import
How-To: Exporting a Subset of
Data From Your Data Model or
Cube
Reference: Additional Security
Restrictions to the SQL WHEREWhy use this feature?
Sometimes, a mass update to your hierarchy or member naming convention is required. This
feature allows you to update existing dimension members in bulk. This is also applicable when
working with member names with leading zeros.
Before you begin
To follow the instructions in this article, you will need Modeler access.
How to
Step 1: Export your current hierarchy or the appropriate section  of your
hierarchy
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select Export from the sidebar tab.
4. Select Hierarchy from the drop-down list.
5. You can leave the Export if following condition is true field blank if you are trying to export your
entire hierarchy. If you are only interested in a particular dimension or particular parent
folder, you can use HQL or MQL. Read this article for further detail on writing HQL or MQL
expressions.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 2/13

Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Using
Command-Line ETL
How-To: Automatically Run ETL
Templates Using the ETL
Scheduler
How-To: Checking if My File Has
a Header Row or Not
How-To: Exporting CSV Files for
ETL Job
How-To: Use Clear Slices to
Clear Intersections During an
ETL Load
How-To: Maintaining
Dimension Member IDs When
Updating Existing Members
How-To: Setting up Email
Notifications for ETL Jobs
How-To: Checking the ETL Tool
Version
Data QueryingIn this example, we will be exporting all member positions with operator (+) .
6. Select Advanced Options to refine your export.
7. Select File.
8. Select CSV.
9. Leave File encoding as Unicode (UTF-8).02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 3/13

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
– External Sources – Data Feeds
& Connections10. Ensure both Include column headers in export and Include member IDs in export are checked.
11. If you want to preview your query results, select Preview.
12. When you're ready, select Export.
13. If your export is successful, a pop-up window will appear. You can monitor the progress of
your job on the History page.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 4/13

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
Product Updates

Step 2: Open the exported CSV file in Notepad or Notepad++
1. Locate the downloaded CSV file.
2. Open the file with Notepad or Notepad++.
3. Open a blank Excel window.
4. Select all the cells in Excel and update the format to Text.
5. Return to the opened file in Notepad or Notepad++ from step 2.
6. Copy the file contents and paste it into the new Excel window.
7. Navigate to the Data tab and select Text to Columns.
This will open the Convert Text to Columns Wizard.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 5/13

8. Select the radio button next to Delimited and then select Next.
02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 6/13

9. Select the choosebox next toComma and then select Next.
10. Scroll to the appropriate column or all columns and select them. This will help maintain
leading zeros.
11. Select the radio button next to Text as the Column data format.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 7/13

12. Select Finish.
13. On the main spreadsheet, you will notice the member IDs are retaining their format, and no
ending zeros were added. If applied to member names with leading zeros (e.g., period,02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 8/13

account IDs), this will also ensure the leading zeros are retained.
14. Make all necessary edits and save the file as CSV.
Step 3: Create a hierarchy load ETL template or use an existing one
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab.
4. Create a new hierarchy load ETL or use an existing hierarchy load ETL template.
Visit this article for instructions on how to create a hierarchy ETL load.
5. Once your template is created (or you have selected an existing template), select Run.
6. Select the CSV fileyou saved in step 2.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 9/13

7. Select Run.
8. This should update your hierarchy as intended.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 10/13


Notes & Best Practices
Once finalized, it is important not to reopen and edit the file again in Excel. But if you must,
you will have to repeat the process in Excel, as it doesn't remember the "text" format since
it's a CSV file.
When dealing with an existing dimension member, the system will treat a member the same
and update it accordingly if the member ID.
When dealing with an existing dimension member, the system will treat a member as a new
member even if the name is the same as an existing one if the member ID is different. This
can happen if Excel has automatically updated the format of the column causing the member
IDs to change.
Two different members with the same name but different member IDs are not allowed.
When using this on an intersection source file, only use text format for dimension member
names and not the "_value" column as that could cause an issue with summing up.
Was this article helpful?
0 out of 0 found this helpful02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 11/13

Related articles
How-To: Creating Tables With Multiple
Dynamic Row Mappings (Multi-Dynamic Rows)
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
Vena Insights Series (Part 2) - Building
Dashboards With Vena Insights
Explainer: What Are Linked Dimensions?
How-To: Data Model Series (Part 2):
Hierarchies and Roll-UpsRecently viewed articles
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
How-To: Exporting CSV Files for ETL Job
How-To: Checking if My File Has a Header Row
or Not
How-To: Automatically Run ETL Templates
Using the ETL Scheduler
How-To: Scheduling Ongoing ETL Jobs at Exact
Times Using Command-Line ETL
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 12/13

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:47 How-To: Maintaining Dimension Member IDs When Updating Existing Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18383563364493-How-To-Maintaining-Dimension-Member-IDs-When-Updating-Existing-Members 13/13
