# (Troubleshooting)   PKIX Path Building Failed When Using the ETL Command Line Tool

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
ETL JobsTroubleshooting: PKIX Path Building
Failed When Using the ETL Command
Line Tool
Issue summary
When running a batch script to import data into Vena via the ETL Command Line tool, you may
encounter the following error:
Marjana
Updated 1 year ago
05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 1/9

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
IDs starting with ‘#’.PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find
valid certification path to requested target
Suggested solution
This issue could occur if the SSL certificate is missing or being re-written by another issuer that is
not a trusted certificate issuer listed in the Java Keystore chain.
The root certificate of vena.ioshould be in the Java Keystore for the ETL Command Line tool to
work.
1. Verify that the certification path is correct. To check the certification path:
a. Navigate to vena.io in Microsoft Edge.
b. Select the lock icon that appears on the address bar.
c. Select View Certificates.
d. Select the Certification Path tab. 05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 2/9

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
The certificate path should have a public certificate issuer in it - as it will be included in
Java's Keystore (trusted certificates) chain by default.
2. Check the debug log and ensure Vena's SSL certificate is not being rewritten by a network
proxy.
3. If your certification looks different than the one in the image above or if it is being rewritten
by a network proxy:
a. Add the third-party issuer's root certificate to Java's Keystore.
OR
b. Bypass the proxy and do not rewrite the certificate.05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 3/9

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
OverviewCause
This can happen if the SSL certificate path for Vena.io is modified.
Keywords
PKIX path building failed
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: ETL Delimiter Not Found
Troubleshooting: No Intersections Updated When Importing a File Using ETL Command Line or
Power Automate
Troubleshooting: ETL Numeric Data Overflow (Result Precision) Invalid Code05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 4/9

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
ETL Jobs at Exact Times UsingTroubleshooting: File-to-Cube ETL Job Not Transferring Some Data
Troubleshooting: Template Automation Failed Validation Rules Cell: X Failed Validation05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 5/9

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
Integration05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 6/9

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
– Channels & Field Mappings05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 7/9

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
Our application support team is ready to help.05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:30 Troubleshooting: PKIX Path Building Failed When Using the ETL Command Line Tool – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27928101466765-Troubleshooting-PKIX-Path-Building-Failed-When-Using-the-ETL-Command-Line-Tool 9/9
