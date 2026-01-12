# (Troubleshooting)   Job Error When Loading LIDS  Bulk Write Operation Error on Server

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
ETL JobsTroubleshooting: Job Error When
Loading LIDS: Bulk Write Operation
Error on Server
Issue summary
When executing an ETL load for Line-Item Details, the job errors out and an error message
similar to the one below is displayed when clicking on the Error:
Vena Support Team
Updated 4 months ago
05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 1/9

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
IDs starting with ‘#’.Problem loading ETL at row 71000 of staging table out_lids Bulk write operation error on server
10.5.2.37:27017. Write errors: [BulkWriteError{index=9, code=66, message='After applying the update
to the document {_id: 276552304529113107 , ...}, the (immutable) field '_id' was found to have been
altered to _id: 276552304529113108', details={ }}].
Suggested solution
The above error message is indicative of duplicate LIDs
Please ensure that there are no duplicate LIDs in your source file or in the respective out_lids
table
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Enabling Line Item Details (LIDs) in a
Template or ReportRecently viewed articles
Troubleshooting: Parent Members Display No
Data05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 2/9

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
Rows in Staging Query SheetTroubleshooting: ETL - Member "" Not Found
in Dimension
Troubleshooting: ETL - Duplicate Intersections
Found During Import
Troubleshooting: ETL - Row Contained X Fields
Troubleshooting: ETL - Error Converting Data
Type Nvarchar to Numeric05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 3/9

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
Overview05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 4/9

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
ETL Jobs at Exact Times Using05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 5/9

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
Integration05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 6/9

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
– Channels & Field Mappings05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 7/9

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
Our application support team is ready to help.05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 12:09 Troubleshooting: Job Error When Loading LIDS: Bulk Write Operation Error on Server – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206211936-Troubleshooting-Job-Error-When-Loading-LIDS-Bulk-Write-Operation-Error-on-Server 9/9
