# (Troubleshooting)   Parent Members Display No Data

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
ETL JobsTroubleshooting: Parent Members
Display No Data
Issue summary
Data has been loaded into a model. When mapping a template against this model, a bottom-
level intersection shows the loaded data. However, once you change one of the member
selections to a parent member, which should include the loaded values at this bottom level, data
is not displayed. Sometimes, you can see “-”, which represents no value.
Permanently deleted user
Updated 1 year ago
05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 1/9

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
Part 1: Check the Operator
This behavior may be caused by the Operator configuration in Vena.io>Modeler>Data
Modeler>Members.
In this section, we can review the dimensions, dimension members and dimension hierarchy
setup. In the table, there is an Operator column. The Operator controls how the bottom-level
members roll up into the parent member. The possible selections are: +, - and ~.
If we have members PARENT, CHILD1 and CHILD2, we can expect the following aggregation:
          PARENT - Parent of CHILD1 and CHILD2.
          CHILD1 - Child of PARENT, value is 1
          CHILD2 - Child of PARENT, value is 105/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 2/9

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
Rows in Staging Query SheetScenario 1, Both Children have the operator: + (SUM Operator)
PARENT = 2
Scenario 2, Both Children have the operator: - (SUBTRACT Operator)
PARENT = -2
Scenario 3, Both Children have the operator: ~ (IGNORE Operator)
PARENT = 0
Part 2: Parent-level mapped intersection is expected to display text values
If the cell is mapped to a parent-level intersection and you are expecting a text value (e.g., name
or job title), the values will not be displayed. This is because the system tries to sum up bottom-
level members and since text values cannot be summed up, it will show blank or zero.
To see a text value in an intersection, the cell must be mapped to all bottom-level members.
Part 3: Ensure the member's alias is not the same as the combination of
another member's name and its alias
For example,
Correct: Member name = 12 and Alias = Jan05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 3/9

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
OverviewIncorrect: Member name = 12 (Jan) and Alias = 12 (Jan).
When using a Form Variable mapping, this could confuse the system which causes the mapping
to point to the wrong member. In this case, rename the alias so it is not the same as the
combination of another member's name and its alias.
Was this article helpful?05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 4/9

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
ETL Jobs at Exact Times Using2 out of 2 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
Explainer: Role-Based Licensing Enforcement
in Vena
How-To: Using Line-Item Details (LIDs) as a
Contributor
How-To: Creating Advanced Integration
Setups With VenaQL
Troubleshooting: Data Is Not Showing in a
Template for a User But Is Showing for OthersRecently viewed articles
Troubleshooting: ETL - Member "" Not Found
in Dimension
Troubleshooting: ETL - Duplicate Intersections
Found During Import
Troubleshooting: ETL - Row Contained X Fields
Troubleshooting: ETL - Error Converting Data
Type Nvarchar to Numeric
Troubleshooting: ETL Command Line Tool 401
Unauthorized Error05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 5/9

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
Integration05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 6/9

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
– Channels & Field Mappings05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 7/9

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
Our application support team is ready to help.05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 12:08 Troubleshooting: Parent Members Display No Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201911009-Troubleshooting-Parent-Members-Display-No-Data 9/9
