# (Troubleshooting)   ETL Job Is Stuck in Waiting for SQL Transformation

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
ETL JobsTroubleshooting: ETL Job Is Stuck in
Waiting for SQL Transformation
Issue summary
During an ETL job, your first step or previous steps may complete, but then the ETL job will get
stuck at the SQL Transformation step when loading your file into Vena.
Olalekan Adebayo
Updated 2 months ago
05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 1/9

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
IDs starting with ‘#’.
Suggested solution
1. Navigate to the Modeler tab.
2. Select History from the sidebar.
3. Filter for the name of the ETL job that is stuck so that it only returns that ETL job.
4. Find the last time the ETL job was completed successfully and select the Job Name.
5. Select the Download icon to download the source file that was used.
6. Open the source file that was downloaded and your most recent source file and compare
them. Ensure the format, column headers and the number of columns are the same.
If there are differences, fix your most recent source file. A common issue here is the new
source file has extra unnecessary columns (either at the beginning, middle or end). This could
cause an error since it's not receiving the expected number of columns or the appropriate
columns in the appropriate location. For the example below, this source file had an extra
column and once removed, the job was completed successfully.05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 2/9

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
7. If there are any numeric columns that would possibly be converted in the backend, ensure
those values are all numeric and not contain non-numeric or text values as this could cause
an issue for the conversion in the backend.
8. If this is happening on a Sandbox tenant, check if anyone from your company has recently
requested a Sandbox tenant refresh. if this is the case, reach out to the Support team.
9. Check if you have recently enabled IP Filtering in your environment. If this is the case, reach
out to the Support team so we can add all the necessary SQL server IPs to the allowed list.
10. If everything looks good and the job is still stuck, reach out to the Support team.
Cause
The most common cause of this is when your recent source file is not in the same format as
expected by the system.05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 3/9

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
OverviewKeywords
etl job stuck, stuck in waiting, SQL transform step stuck, etl jammed.
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Conversion Failed When Converting Date and/or Time From Character String
Troubleshooting: ETL Vena Table Does Not Contain the Clear Slices Column ‘Column Name’
Troubleshooting: Error Invalid Input for ETL and VenaQL
Troubleshooting ETL error: You cannot create external IDs starting with ‘#’.
Troubleshooting: The File is too Large and Cannot be Exported Error when Using ETL Export05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 4/9

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
ETL Jobs at Exact Times Using05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 5/9

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
Integration05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 6/9

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
– Channels & Field Mappings05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 7/9

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
Our application support team is ready to help.05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:22 Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14718611324941-Troubleshooting-ETL-Job-Is-Stuck-in-Waiting-for-SQL-Transformation 9/9
