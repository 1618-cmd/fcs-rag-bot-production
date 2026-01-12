# (Troubleshooting)   Some Data Has Not Loaded After Running an ETL Job With Integration Channels

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
ETL JobsTroubleshooting: Some Data Has Not
Loaded After Running an ETL Job
With Integration Channels
Issue summary
After running an ETL job that contains integration channels, you may notice some intersections
were not transferred or are missing in the cube.
Omair Riasat
Updated 1 year ago
05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 1/9

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
IDs starting with ‘#’.Suggested solution
Check the source by following these steps:
1. Navigate to the integration channel and locate the source.
2. Export the source.
3. Open it in Excel or Notepad and ensure the data you are looking to transfer is in the
channel's source. If it is not present then that's the issue and it must be addressed.
Check the integration channel by following the steps:
1. Review the channel and all the transformations involved.
2. Confirm that none of the transformations will ignore that member or change the name to
a different name in the destination model.
3. Check all non-direct mappings (e.g., formula, scripted, table mappings) and ensure none
of them are configured to ignore the affected dimension or intersection.
4. If there's a table source mapping that gets its data from a data model in the channels'
transformation, ensure the user running the channel or ETL job has the necessary data
permission to the data model.
If neither of the above have worked, check the following:
1. If the aggregation mode is sum, ensure the values were not saved as text. For example, if a
value has double quotes or commas in the source, the summation of text values will equate
to 0. If your destination is also not configured to retain zero, then any intersections that
equate to zero will not be saved in the destination.
2. Preview the integration channel, export the output and review it to confirm if the data is
there. This will determine if it's a channel issue or a template mapping issue.05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 2/9

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
Rows in Staging Query Sheet3. If the ETL job is configured to start via a macro, the job may not automatically run after a data
save for some users if they have not enabled the necessary macro settings. Ask those users
to allow all macros to run.
4. Review the source file of the ETL in question and compare with a source file that successfully
loaded the data in the past. Pay attention to the Columns containing Date and confirm if the
format has changed, specially if there are formula mappings in the Integration Channel of the
ETL that are dependent on those columns, e.g. Year, Period etc.
Keywords
stage, staging table, vena table, integration channel, channel, transformation, ignore, data
missing, data load
Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: ETL Guide - 1 - OverviewRecently viewed articles
Troubleshooting: Duplicate Rows in Staging
Query Sheet
Troubleshooting: Invalid Member Name for05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 3/9

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
OverviewDimension (X): Name Is Blank
Troubleshooting: ETL Jobs Getting Stuck in
SQL Transform Step When IP Filtering Is
Enabled
Troubleshooting: ETL Job Is Creating or
Loading Data Into an Unmapped Folder
Troubleshooting: ETL Job Is Stuck in Waiting
for SQL Transformation05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 4/9

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
ETL Jobs at Exact Times Using05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 5/9

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
Integration05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 6/9

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
– Channels & Field Mappings05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 7/9

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
Our application support team is ready to help.05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:25 Troubleshooting: Some Data Has Not Loaded After Running an ETL Job With Integration Channels – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/18551953301645-Troubleshooting-Some-Data-Has-Not-Loaded-After-Running-an-ETL-Job-With-Integration-Channels 9/9
