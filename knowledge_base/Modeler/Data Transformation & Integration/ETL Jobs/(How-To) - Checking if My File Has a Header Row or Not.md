# (How To)   Checking if My File Has a Header Row or Not

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs Search
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
ETL JobsHow-To: Checking if My File Has a
Header Row or Not
Use this method to confirm if your source file has a Header Row.
Why use this feature?
Olalekan Adebayo
Updated 1 year ago
02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 1/6

ETL Job Errors &
Troubleshooting
Reference: ETL Guide - 1 -
Overview
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
Restrictions to the SQL WHEREThere are some ETL jobs that require that your source file has a header row to ensure it aligns
with the destination.
Before you begin
To follow the instructions in this article, you will need at least Modeler access.
How to
In Vena, any column that starts with an underscore "_" is treated as a column header and will not
be inserted into the SQL or Vena table.
1. Open your source file in Notepad or Excel, if one or all the columns in the first row starts with
an underscore, that row is treated as the header row and the row is ignored.
2. If one or all the columns in the first row do not start with an underscore, there is no header
row.
Was this article helpful?02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 2/6

Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Using
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
Data Querying0 out of 0 found this helpful
Recently viewed articles
How-To: Automatically Run ETL Templates Using the ETL Scheduler
How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL
Explainer: ETL Export Feature Updates
Reference: Additional Security Restrictions to the SQL WHERE Clause
How-To: Exporting a Subset of Data From Your Data Model or Cube02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 3/6

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
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feeds
& Connections02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 4/6

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
PowerPoint
Vena Copilot
Product Updates02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:46 How-To: Checking if My File Has a Header Row or Not – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14717674461069-How-To-Checking-if-My-File-Has-a-Header-Row-or-Not 6/6
