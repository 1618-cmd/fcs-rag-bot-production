# (Troubleshooting)   ETL   Duplicate Intersections Found During Import

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
ETL JobsTroubleshooting: ETL - Duplicate
Intersections Found During Import
Issue summary
Issue 1#
Duplicate intersection found during import.
Olalekan Adebayo
Updated 2 years ago
05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 1/9

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
IDs starting with ‘#’.1st Error Message:
Suggested solution
1. Select the arrow in the error message to display the duplicated intersections.
2. Open the file in Excel.
3. Use the sort and filter options to find the duplicated intersections.
In this example 1,   opening the .csv file reveals that lines 1 and 2 are the same intersection,
despite the fact that the Value column is different.
4. Remove all duplicates from the file so there's only one occurrence of the intersections
members in that row.
5. Re-run your job.
Cause
This happens when two or more rows have exactly the same set of dimension members in your
source file during a direct file-to-cube ETL job, even if the intersection values are different. This05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 2/9

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
Rows in Staging Query Sheetcould also happen in an ETL job that uses an integration channel where the aggregate mode is
UNIQUE.
Issue 2#
Duplicate intersection found during import.
Suggested solution
1. Select the arrow in the error message to display the duplicated intersections. 05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 3/9

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
Overview2. Open the downloaded file in Excel.
3. Use the sort and filter options to find the duplicated intersections. In this example, opened
the downloaded file,    and filter by Account 20015, Entity 10, Product HBG, Business Partner
Solarwinds, the Year 2023, and Period 3 as shown in the error message, you will see there are
two different values under the same dimensions. As the channel detected duplicate
intersections, it failed.
The screenshot shows that name of one of your Business Partners was changed from
"Solarwinds" to "SolarWinds" in QBO which in turn caused VQL to not recognize it as the
same value and treated it as 2 unique members (This is because VenaQL and Vena tables are
case-sensitive. So a word with uppercase "S" and lowercase "s" are different). However,  the
intersection load is treating it as duplicates.
4.  Navigate to the Modeler page
5. Find the appropriate member name
6. Since the dimension member name was changed in the source system, please rename the
member name to the updated member as per QBO.
7. Re-run the ETL job.05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 4/9

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
This happens when the name of the member in the modeler is different than the name of the
member in the QBO load. For example Solarwind in Modeler and SolarWind in QBO.
The venaQL does not recognize it as having the same value and treated it as 2 unique members
How to find where the duplicates are from if not present in the source:
If the duplicates are not present in the source but instead it's been created due to a
transformation step (e.g. Integration channel, table mapping, VenaQL, Stored Procedure), you
have to go through where and how each column is getting its value and this should lead to a
configuration causing the issue. The idea is to focus on columns with different and unique values
but now with the same values after a transformation. This is common with ETL jobs that assign
different departments or an intersection that has both "Actual" and "Plan" data but the ETL job is
now trying to save both unique intersections into the "Actual" dimension.
Since the same intersection will now have two rows with the same intersection and the05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 5/9

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
Integrationaggregate mode of the challe is "UNIQUE", this will cause the system to error out.
In the example above, you have to decide which one is the correct one and delete the incorrect
one or the one that is not needed. So the source will only have one row.
Keywords
duplicate, intersections, import, during, etl, failed, error, load, cube, file
Was this article helpful?
0 out of 0 found this helpful05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 6/9

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
– Channels & Field MappingsRelated articles
How-To: Finding and Fixing Duplicate
Intersection Template Warnings
Reference: ETL Guide - 1 - Overview
How-To: Granting Vena Support Access to
Your Tenant
How-To: Map a Process Variable to a
Template (Vena 365 Only)
How-To: Enabling Line Item Details (LIDs) in a
Template or ReportRecently viewed articles
Troubleshooting: ETL - Row Contained X Fields
Troubleshooting: ETL - Error Converting Data
Type Nvarchar to Numeric
Troubleshooting: ETL Command Line Tool 401
Unauthorized Error
Troubleshooting: ETL Command Line Tool 422
Null Error
Troubleshooting: Index X out of Bounds for
Length X05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 7/9

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
Our application support team is ready to help.05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 12:07 Troubleshooting: ETL - Duplicate Intersections Found During Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14003873838349-Troubleshooting-ETL-Duplicate-Intersections-Found-During-Import 9/9
