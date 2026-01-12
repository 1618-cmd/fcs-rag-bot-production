# (How To)   Exporting CSV Files for ETL Job

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
ETL JobsHow-To: Exporting CSV Files for ETL
Job
Easily preview ETL intersections and ETL Job information with Vena's Export to CSV
functionality.
Why use this feature?
Laura Harris
Updated 1 month ago
02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 1/9

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
Restrictions to the SQL WHEREIf you're responsible for overseeing multiple ETL jobs, it can be challenging to keep track of all
your ETL jobs With Vena’s Export to CSV functionality, you can easily preview ETL intersections
and ETL Job information and export this information to a CSV.
Before you begin
To follow the instructions in this article, you will need at least Modeler access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
Table of contents
How to
Export intersections preview to .csv
Export from the ETL page
Download .csv for ETL Job
Notes
How to
Export intersections preview to CSV02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 2/9

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
Data Querying1. Navigate toModeler tab.
2. Select Data Modeler from the sidebar.
3. Select Members from the sidebar tab.
4. Right-click on the desired member or select the vertical ellipses at the end of the row to open
the menu.
5. Select Preview Intersections to open the Preview Intersections window.
6. Select Export to download a CSV file to your Desktop folder.
Export from the ETL page
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select Export from the sidebar tab.02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 3/9

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
& Connections4. Select the appropriate data model from the data model drop-down.
5. Choose the values you would like to export.
6. Select Advanced Options.
7. Select CSV under the heading File format.
8. Check any boxes to select other options (Include column headers in export, etc.) for your
export.02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 4/9

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
Product Updates9. Select Save when you are finished.
10. Select Export at the bottom-right side of the page to begin your ETL export.
11. This begins a background process to export the data to a file. You can check the progress in
the History tab.02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 5/9

Download CSV for ETL job

To download a CSV file for a specific ETL job, you must open the History tab and open the
corresponding window to download the CSV file.
1. Navigate to the Modeler tab.
2. Select History from the sidebar.
3. Select the Job Name. This opens a drawer.
Note_Icon_Small.png Note
You are the only user that will be able to download the CSV file and you can only
download this file once. If you need to download the file a second time, you must re-
run an export.02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 6/9

4. Select the Download (
) icon to download your CSV file.
Notes
When exporting sources to a CSV, the CSV will include headers prefixed with "_" in the
following cases:
When previewing data when right-clicking on members in the data model.
Note_Icon_Small.png Note
Users cannot download files for any ETL jobs that are more than 365 days old.02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 7/9

Exporting from the preview data window when right-clicking on members in the data
model.
Exporting on the transform & load page when you preview a source.
Exporting on the channels page when changing sources.
Exporting from the preview output window in a channel.
Previewing a data feed in the data feed tab, then selecting export.
Was this article helpful?
1 out of 5 found this helpful
Related articles
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
How-To: Exporting Data From a SQL Staging
Table
Reference: Writing Expressions (MQL & HQL)
Explainer: Vena User RolesRecently viewed articles
How-To: Checking if My File Has a Header Row
or Not
How-To: Automatically Run ETL Templates
Using the ETL Scheduler
How-To: Scheduling Ongoing ETL Jobs at Exact
Times Using Command-Line ETL
Explainer: ETL Export Feature Updates02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 8/9

How-To: Building Alternate Hierarchies Reference: Additional Security Restrictions to
the SQL WHERE Clause
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:46 How-To: Exporting CSV Files for ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360037234851-How-To-Exporting-CSV-Files-for-ETL-Job 9/9
