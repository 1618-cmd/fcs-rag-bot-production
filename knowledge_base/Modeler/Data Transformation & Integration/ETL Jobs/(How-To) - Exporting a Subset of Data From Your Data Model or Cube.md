# (How To)   Exporting a Subset of Data From Your Data Model or Cube

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
ETL JobsHow-To: Exporting a Subset of Data
From Your Data Model or Cube
Instead of doing a mass export of all data in your data model, you may only want to
export a subset of data.
Why use this feature?
Olalekan Adebayo
Updated 7 months ago
02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 1/6

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
Restrictions to the SQL WHEREThis feature allows you to define a query to export only a subset of data from your data model
instead of exporting the entire data model. This means your export will be faster to download
and allows you to focus on only the data you are interested in.
Before you begin
To follow the instructions in this article, you will need at least Modeler access and the necessary
data permissions.
How to
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar and then select Export.
3. You can leverage our MQL expression to export data from the cube with a Manual Query or
use Quick Export to refine your query.
For example, if you are looking to export only the data for the year 2023, you can use the
MQL query: dimension('year':'2023')
=02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 2/6

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
This same logic can also be applied with other dimensions and members and you can have
multiple dimension conditions in one query.
For example, if you want all 2023 actual data, the query will be:
dimension('year':'2023')
dimension('scenario':'actual').02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 3/6

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
& Connections4. Select Preview to review the data query before committing to an ETL Export.
You can also export from multiple members within the same dimension.
Dimension('DimensionName' : union('Member1' 'Member2' '...'))
This expression exports all data associated with Member1, Member2, etc. from the
DimensionName dimension. 02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 4/6

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
Product UpdatesNotes
If you have multiple data models, ensure you are in the appropriate one and that you have the
correct data permission to view the data.
Was this article helpful?
1 out of 2 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
How-To: Exporting CSV Files for ETL Job
How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
Vena Insights Series (Part 2) - Building
Dashboards With Vena InsightsRecently viewed articles
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
How-To: Exporting Data From a SQL Staging
Table
Reference: ETL Guide - 6- Using Staging Data
Reference: ETL Guide - 5 - SQL Staging
Environment
Reference: ETL Guide - 4 - Query Languages02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:44 How-To: Exporting a Subset of Data From Your Data Model or Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14720594430861-How-To-Exporting-a-Subset-of-Data-From-Your-Data-Model-or-Cube 6/6
