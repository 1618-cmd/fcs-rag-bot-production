# (Troubleshooting)   ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs
/ETL Job Errors & TroubleshootingSearch
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
ETL JobsTroubleshooting: ETL Number of
Columns in the File Uploaded Must Be
Equal to the Number of Columns in
the Vena Table
Soo Kim
Updated 2 years ago
05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 1/9

ETL Job Errors &
Troubleshooting
Troubleshooting: ETL Job
Error – Job Was Skipped as It
Was Already
Queued/Waiting/Running
Troubleshooting: Connection
Timed Out Error When Using
the ETL Command Line Tool
Troubleshooting: ETL Error
"There were only X members
in this row. Was expecting X
members (or 0 If deleting all
LIDs for a unique etl_id/label
/row)"
Troubleshooting: Error
Processing Workbook:
xxx.xlsx Error While
Processing the Model
Expression
Troubleshooting: The File is
too Large and Cannot be
Exported Error when Using
ETL Export
Troubleshooting ETL error:
You cannot create external
IDs starting with ‘#’.Issue summary
When running an ETL job, you may encounter the following error message:
The number of columns in the file (15) uploaded must be equal to the number of columns (9) in the
Vena Table. To add columns, please edit the table structure.
Suggested solution
Option 1: When the number of columns in the file is more
than the number of columns in the Vena Table
1. Locate the uploaded file on your computer.
2. Open the file with Notepad.
3. Delete extra columns or adjust the columns with the unwanted commas in the source. In this
example, the number of expected columns is 9.05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 2/9

Troubleshooting: Error Invalid
Input for ETL and VenaQL
Troubleshooting: ETL Vena
Table Does Not Contain the
Clear Slices Column ‘Column
Name’
Troubleshooting: Conversion
Failed When Converting Date
and/or Time From Character
String
Troubleshooting: ETL Job Is
Stuck in Waiting for SQL
Transformation
Troubleshooting: ETL Job Is
Creating or Loading Data Into
an Unmapped Folder
Troubleshooting: ETL Jobs
Getting Stuck in SQL
Transform Step When IP
Filtering Is Enabled
Troubleshooting: Invalid
Member Name for Dimension
(X): Name Is Blank
Troubleshooting: Duplicate
Rows in Staging Query Sheet
4. Save the file and re-run the ETL job.
Option 2: When the number of columns in the file is less
than the number of columns in the Vena Table
1. Locate the uploaded file on your computer.
2. Open the file with Notepad.
3. Add the missing columns and ensure the file is in the correct format.
4. Save the file and re-run the ETL job.
Option 3: When the number of columns in the file is 1
1. Locate the uploaded file on your computer.
2. Open the file with Notepad.
3. Confirm that the format and column separator appear correctly. Ensure you are selecting the
correct file format based on the column separator of your source file (comma-separated files
should use CSV, pipe-separated files should use PSV and tab-separated files should use TSV).
4. Ensure that the file format you selected when running the ETL job is the same as the file
format of the source file. In this example, the file is a PSV.05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 3/9

Troubleshooting: Some Data
Has Not Loaded After
Running an ETL Job With
Integration Channels
Troubleshooting: Staging
Query Pulling Incomplete
Information
Troubleshooting: The
Maximum Number of ETL
Errors Allowed Was Exceeded.
Dimension X Already Has a
Member Named X
Troubleshooting: ETL
Uploaded Values Are Going
Into an Undefined Member
Troubleshooting: ETL
Combined Clear Slices
Operation Contains
Overlapping Dimension With
an Empty Intersection
Troubleshooting: Template
Automation Failed Validation
Rules Cell: X Failed Validation
See all 89 articles
Reference: ETL Guide - 1 -
Overview
But when running the ETL job, CSV was selected as the file format. This causes the system to
treat all the individually separated columns as one column, which causes the error message.
5. Update the file to be comma-separated or select PSV as the file format to fix this issue.
Note
You can also open the file in Excel and check if all the columns appear in only one
column. You will notice everything appears in column A instead of columns A, B, C, D05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 4/9

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
Restrictions to the SQL WHERE
Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times UsingCause
The error indicates the number of columns in the uploaded source file doesn't match the
expected number of columns in the Vena table. This can happen if your source file is blank,
contains an extra column or is missing some columns. This may also occur if the file format that
was selected when running the ETL job is not the same as the file format of the source file.
Keywords
etl, number, columns, table, equal, error, file, uploaded, source, the number of columns in the
file, must be equal to the number of columns in the vena table
Was this article helpful?
0 out of 0 found this helpful
and E. If this is the case, the file must be fixed and re-uploaded.
05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 5/9

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
Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
IntegrationRecently viewed articles
Troubleshooting: ETL Parent Member Cannot Be Shared
Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool
Troubleshooting: ETL Delimiter Not Found
Troubleshooting: No Intersections Updated When Importing a File Using ETL Command Line or
Power Automate
Troubleshooting: ETL Numeric Data Overflow (Result Precision) Invalid Code05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 6/9

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
How-to: Vena Integration: Part 6
– Channels & Field Mappings05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 7/9

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
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:32 Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of Columns in the Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17398338131981-Troubleshooting-ETL-Number-of-Columns-in-the-File-Uploaded-Must-Be-Equal-to-the-Number-of-Columns-in-the-Vena-Table 9/9
