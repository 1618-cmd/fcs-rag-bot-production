# (Reference)   ETL Guide   6  Using Staging Data

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
ETL JobsReference: ETL Guide - 6- Using
Staging Data
Part 1:ETL Guide Overview
Part 2:Vena.io ETL
Part 3:Command Line - ETL
Part 4:Query Languages
Part 5:SQL Staging Environment
Vena Support Team
Updated 1 year ago
02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 1/12

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
Restrictions to the SQL WHEREPart 6:Using Staging Data -You are here
Table of contents
Chapter 6: Using Staging Data
Staging Queries
Drill Through to Transactions
Chapter 6: Using Staging Data
Staging Queries
Staging Queries is a function on Vena Desktop for Managers that allows a connection from
within a template to query any tables or views in the Staging Environment, and pull the results
onto a worksheet. Any data table created from the ETL Import process is accessible by Staging
Queries.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 2/12

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
Data Querying
Each Staging Query is associated with a worksheet in the template and will retrieve data onto it.
It is not dependant on the Data Model Refresh nor is it dependant on the state of an ETL import
process.
The querying method is defined by a similar structure to the SQL WHERE clause so that users are
enabled to extract only those records that fulfill a specified criterion. There is also an option to
choose which columns to appear for each query.
SQL query format:
SELECT <column_name> , <column_name>
FROM <table_name>
WHERE <column_name>  operator <value>02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 3/12

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
& Connections
The Query field entered gets inserted as-is and represents the SQL WHERE clause when the
Staging table is queried.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 4/12

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
Product Updates
Headers of staging table can be formatted and it will retain formatting even when staging data is
refreshed.
Without formatting:02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 5/12

With formatting:
Cut and paste the named range cell to desired placement and format the surrounding cells.
Vena begins outputting data from the_vena_StagingQuery named cell.
When the desired format is set as desired, run the query again with the following steps.
Data Model > Staging Queries > Edit > OK > Close02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 6/12

Cells modified to the top or left of the staging table will be retained even when the table is
refreshed. Cells modified to the bottom or right of the staging table will be removed after the
table is refreshed.
Drill Through to Transactions
Transactions drill-through is available to Contributors through Vena Desktop, provided that an
appropriately structured transaction data file is imported into a table in the Staging
Environment. Users can choose an intersection and select the Drill > Transactions to see the
transaction details for that amount.
Below is a sample of a load file. The first columns must represent the dimensions in the same
order as it is found in the Modeler. The dimension names indicated in the file must match the
dimension names used in the data model, but prefixed with an underscore ‘_’. Choose a data cell
and then select Drill > Transactions.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 7/12

The Drill > Transactions query window allows you to choose the columns of the Transaction
table or view to appear. Unlike Staging Queries, the Sheet Name and Query fields are
automatically filled in. Vena populates the Query field with an auto-generated SQL WHERE clause
based on the members in the intersection point of the data cell.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 8/12

For any intersection point dimension member that is not a bottom-level member, Vena will
include all of the bottom-level members in an IN operator of the SQL WHERE clause.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 9/12

The result of a Drill Through to Transactions is displayed in a new tab. All subsequent drills will
show results in a new worksheet tab. The format is not updatable. The SQL query used to query
the transaction data appears in cell A1.02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 10/12

Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: ETL Guide - 5 - SQL Staging
Environment
Reference: ETL Guide - 4 - Query LanguagesRecently viewed articles
Reference: ETL Guide - 5 - SQL Staging
Environment
Reference: ETL Guide - 4 - Query Languages02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 11/12

How-To: Setting up a Staging Query (Vena 365
Only)
How-To: Managing and Deleting Data Using
Vena Tables
Reference: ETL Guide - 2 - Vena.io ETLReference: ETL Guide - 3 - Command Line ETL
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 1 - Overview
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:43 Reference: ETL Guide - 6- Using Staging Data – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028071552-Reference-ETL-Guide-6-Using-Staging-Data 12/12
