# (Troubleshooting)   Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job

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
ETL JobsTroubleshooting: Network Error (422)
Unprocessable Entity Error When a
Data Save Is Trying To Start an ETL
Job
Issue summary
Olalekan Adebayo
Updated 2 years ago
05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 1/9

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
IDs starting with ‘#’.After saving data on a template, you may receive the following error when the system is trying to
start an ETL job: 422 Unprocessable Entity.
Suggested solution
1. If your template is macro-enabled, check for any VenaAfterSaveData macros for any
referenced ETL job ID. If your template is not macro-enabled, check the SaveDataETLJobID
workbook setting for any referenced ETL job ID.
Workbook setting05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 2/9

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
2. This means an ETL job should be started whenever you select Save Data on your template
and that an ETL job/template must exist in your data model with the same ID.
3. Open the template.
4. Select Data Models. This shows you the data model(s) attached to your template.
05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 3/9

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
Overview5. Check the Case Study Model and ensure there's an ETL job with that same ID.
6. Select the Pencil icon on each ETL template/job to check the ID.
7. If there's an ETL job that you intend to run after each data save but the ID is different,update
the ID on the macro or workbook setting and save the template.
If you don’t intend to start any ETL jobs after each data save, remove the section of your
macro that calls for an ETL job to be started or remove the ID from the SaveDataETLJobID
workbook setting so it is blank.
8. Once updated, save your template and you should no longer get an error after each save
data.
Cause
This may happen if the template has been configured to run an ETL job (e.g cube-to-cube ETL
job) after a data save via a VenaAfterSaveData macro or the SaveDataETLJobID setting but the ETL
job ID that was supplied does not exist in that data model.05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 4/9

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
ETL Jobs at Exact Times UsingKeywords
422 network error, data save unable to start ETL job, template error, network error
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Cube to Cube ETL Job Not Transferring Some Data
Troubleshooting: Size Must Be Between 0 and 16793600 (16MB) When Running an ETL Job
Troubleshooting: ETL Error Thrown by Scripted Mapping
Troubleshooting: Exporting Intersections via ETL Command Line Creates a Blank File
Troubleshooting: ETL Number of Columns in the File Uploaded Must Be Equal to the Number of
Columns in the Vena Table05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 5/9

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
Integration05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 6/9

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
– Channels & Field Mappings05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 7/9

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
Our application support team is ready to help.05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:34 Troubleshooting: Network Error (422) Unprocessable Entity Error When a Data Save Is Trying To Start an ETL Job – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16394919664525-Troubleshooting-Network-Error-422-Unprocessable-Entity-Error-When-a-Data-Save-Is-Trying-To-Start-an-ETL-Job 9/9
