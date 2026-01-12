# (Troubleshooting)   Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job

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
ETL JobsTroubleshooting: Size Must Be
Between 0 and 16793600 (16MB)
When Running an ETL Job
Issue summary
Sometimes when running an ETL Job, you may get the following error message:
Mendez Dixon
Updated 1 year ago
05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 1/9

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
IDs starting with ‘#’.Write failed with error code 10334 and error message 'BSONObj size: 16920007 (0x1022DC7) is
invalid. Size must be between 0 and 16793600(16MB) First element: _id: 1333777988706107392.

Suggested solution
1. Find the integration channel that results in an error.
2. Check the Clear Slice configuration for the destination of the channel. If more than five or six
dimensions are checked off, review it to see if there is a way to reduce the number of
dimensions to clear.
Caution05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 2/9

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
Extreme care must be taken while modifying Clear Slices to avoid unintended data
deletions. If you need further assistance, please reach out to the Support team.05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 3/9

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
Overview05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 4/9

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
ETL Jobs at Exact Times Using
05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 5/9

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
3. Alternatively, reduce the number of steps in the ETL which utilizes the Clear Slice feature or
split it into two or more ETLs.
Cause
This could happen when the integration channel/job is creating a log file greater than 16 MB.
This may be due to too many dimensions being checked off for the Clear Slice configuration.
Keywords
10334 Error, BSONObj SIze, 16920007(0x1022DC7), 16MB, ETL Job Error, Size Must be Between 0
and 1679360005/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 6/9

How-To: Setting up Email
Notifications for ETL Jobs
How-To: Checking the ETL Tool
Version
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
Feature OverviewWas this article helpful?
0 out of 0 found this helpful
Related articles
Reference: ETL Guide - 1 - OverviewRecently viewed articles
Troubleshooting: ETL Error Thrown by
Scripted Mapping
Troubleshooting: Exporting Intersections via
ETL Command Line Creates a Blank File
Troubleshooting: ETL Number of Columns in
the File Uploaded Must Be Equal to the
Number of Columns in the Vena Table
Troubleshooting: ETL Parent Member Cannot
Be Shared
Troubleshooting: PKIX Path Building Failed
When Using the ETL Command Line Tool05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 7/9

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
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 8/9

Vena Copilot
Product Updates
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 11:33 Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21197001889549-Troubleshooting-Size-Must-Be-Between-0-and-16793600-16MB-When-Running-an-ETL-Job 9/9
