# (Troubleshooting)   ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled

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
ETL JobsTroubleshooting: ETL Jobs Getting
Stuck in SQL Transform Step When IP
Filtering Is Enabled
Issue summary
Recently enabled IP Filtering in your environment and ETL jobs with an SQL Transformation step
are getting stuck.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 1/9

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
IDs starting with ‘#’.Error Message:
Job Not Started.
This job has not started yet.
Suggest ed solution
Step 1:05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 2/9

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
Rows in Staging Query SheetNavigate to Admin > Policies >IP Filtering and confirm that IP filtering is enabled. If enabled,
the IP Allowed List will be shown.

Step 2:
If the IP filtering is enabled, under Allowed IP Addresses confirm that Vena's SQL server's public IP
address for your Vena Hub has been added.
Note
To enable IP filtering for the first time, please see How-To: Setting Up IP Filtering05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 3/9

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
Step 3:
If the IP address is not already added, select Add IP Address to add it.
See the public IP address for your Vena Hub below.
SQL Server Vena Hub Public IP Address
US1 54.82.64.185
US2 54.82.64.185
US3 54.68.91.15805/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 4/9

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
ETL Jobs at Exact Times UsingCA3 52.60.192.195
EU1 54.76.107.111
Step 4:
Cancel the stuck ETL jobs and re-run them.
Cause
Note
To confirm your Vena Hub, check the URL box while logged into vena.
The URL below shows this tenant is in the US2 V ena Hub.
This means you need to add this Public IP " 54.82.64.185" to your IP Allow ed List .05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 5/9

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
IntegrationThis issue can occur if you enable IP Filtering but our SQL server's public IP address for your
Vena Hub has not been added to the Allowed IP Addresses.
Keywords
ETL, load, stuck, SQL, IP, filtering
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: ETL Job Is Creating or Loading Data Into an Unmapped Folder
Troubleshooting: ETL Job Is Stuck in Waiting for SQL Transformation
Troubleshooting: Conversion Failed When Converting Date and/or Time From Character String
Troubleshooting: ETL Vena Table Does Not Contain the Clear Slices Column ‘Column Name’
Troubleshooting: Error Invalid Input for ETL and VenaQL05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 6/9

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
– Channels & Field Mappings05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 7/9

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
Our application support team is ready to help.05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:23 Troubleshooting: ETL Jobs Getting Stuck in SQL Transform Step When IP Filtering Is Enabled – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233545201805-Troubleshooting-ETL-Jobs-Getting-Stuck-in-SQL-Transform-Step-When-IP-Filtering-Is-Enabled 9/9
