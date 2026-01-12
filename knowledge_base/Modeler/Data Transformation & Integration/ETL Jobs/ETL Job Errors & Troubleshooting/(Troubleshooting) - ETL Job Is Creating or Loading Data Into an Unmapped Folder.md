# (Troubleshooting)   ETL Job Is Creating or Loading Data Into an Unmapped Folder

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
ETL JobsTroubleshooting: ETL Job Is Creating
or Loading Data Into an Unmapped
Folder
Issue summary
After running an ETL job, you may notice that a folder named Unmappedhas been created and
that Vena loaded specific intersection members as a child(ren) of this parent member.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 1/9

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
Although the name of the new folder is Unmapped, this does not mean that these members
have not been mapped on your templates.
It simply means that this member did not exist as part of your hierarchy before the ETL job
loading them into your data model. Since the system doesn't know where to place them in your
hierarchy, it creates a parent member named Unmapped outside of your other hierarchy05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 2/9

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
Rows in Staging Query Sheetmembers. This is so it doesn't affect any of your existing templates when the system is rolling up
the values for the bottom-level members.
Where to place unmapped members
There are two courses of action here, depending on whether:
1. Members were correctly placed in the Unmapped folder because they are new dimension
members.
2. Members were incorrectly placed in the Unmapped folder because they actually already exist.
1. Members were correctly placed in the Unmapped folder because they are new
dimension members.
You must manually move the members into their correct position in the hierarchy or ensure
new members are created in the correct position in the hierarchy before loading data into
them.
2. Members were incorrectly placed in the Unmapped folder because they actually already
exist
If your members already existed before the ETL load, this change may have occurred for the
following reasons:
Leading Zeros (0s):
A common reason why this issue occurs is due to leading zeros.
For example, if your dimension member has leading zeros (e.g., 01, 02, 03, 04, etc.) but when
you loaded data into the cube, the dimension member was 1, 2, 3, 4, etc., then the system05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 3/9

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
Overviewwill create or place these new members (without the leading zeros) in the Unmapped folder
because:
The new members do not currently exist (in any format) in the data model hierarchy.
Or,
The new members are different from the members with leading zeros in the data model
hierarchy. 05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 4/9

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
ETL Jobs at Exact Times Using In the following example, the system is expecting All Periods to display with leading zeros:
But the source file didn’t have leading zeros in the Period dimension:05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 5/9

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
Integration
To fix this,you can delete the unwanted members from the Unmappedfolder and reload the
source file. However, before youdo so, ensure the file contains the correct format and
dimension names in your hierarchy.
Note
Dropping leading zeros is common when editing with Excel; visit this article to learn
how to ensure leading zeros are retained. You only need to apply this on the columns05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 6/9

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
– Channels & Field Mappings
Cause
This issue may be caused by one of two reasons:
1. You have unmapped members in your data model. To avoid this issue going forward, make
sure your hierarchy member names are updated to match the data coming from your source
system or source file before you start an ETL load.
2. The naming convention changed in your source system. Before you start an ETL load, make
sure that the naming convention in your source system has not been recently updated and that
it still matches the members in Vena. If the external source system naming convention has
changed, make sure to update to respective data model in vena.io.
Keywords
unmapped folder, unmapped member.
Was this article helpful?
that require leading zeros.05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 7/9

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
Product Updates0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation
Troubleshooting: Conversion Failed When Converting Date and/or Time From Character String
Troubleshooting: ETL Vena Table Does Not Contain the Clear Slices Column ‘Column Name’
Troubleshooting: Error Invalid Input for ETL and VenaQL
Troubleshooting ETL error: You cannot create external IDs starting with ‘#’.
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:23 Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/19421264926861-Troubleshooting-ETL-Job-Is-Creating-or-Loading-Data-Into-an-Unmapped-Folder 9/9
