# (Troubleshooting)   ETL Could Not Submit Job

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
ETL JobsTroubleshooting: ETL Could Not
Submit Job
Issue summary
Could not submit job.
Another job ([job ID]) is already running under this data model.
Olalekan Adebayo
Updated 2 years ago
05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 1/9

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
This error means that since one ETL job is already running for the data model, no other jobs can
be queued because the setting to do so has not been enabled.
To enable it:
1. Navigate to the Admin tab.
2. Select the Policies page.
3. Select Server Properties from the sidebar.
4. Select Add Property.
5. Enter queueETLJobs.
6. Select Create.
Set the toggle for the queueETLJobs property to TRUE.05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 2/9

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
Rows in Staging Query SheetCause
This error message will occur when ETL job queuing is not enabled for your tenant or
environment.
Keywords
etl, load, could not submit, already running
Was this article helpful?
0 out of 0 found this helpful
Related articles
Troubleshooting: ETL Job Error – Job Was
Skipped as It Was Already
Queued/Waiting/RunningRecently viewed articles
Troubleshooting: ETL Error in Loaded File-
String Contains Invalid or Unsupported UTF8
Code Points
Troubleshooting: ETL Unsupported Encoding
"Latin-1" Latin-1
Troubleshooting: ETL Template with Template
Automation Fails to Run Due to Invalid Page05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 3/9

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
OverviewOptions
Troubleshooting: ETL Error in Loaded File-
String length Exceeds DDL Length
Troubleshooting: Integration Export Error 504
Gateway Time-Out05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 4/9

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
ETL Jobs at Exact Times Using05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 5/9

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
Integration05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 6/9

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
– Channels & Field Mappings05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 7/9

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
Our application support team is ready to help.05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:59 Troubleshooting: ETL Could Not Submit Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14312704153485-Troubleshooting-ETL-Could-Not-Submit-Job 9/9
