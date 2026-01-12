# (Explainer)   Set Staging or Transactions Tables When Building a Vena Table

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Vena Tables Search
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
ETL JobsExplainer: Set Staging or Transactions
Tables When Building a Vena Table
Take control of your data by designating  Transaction or Staging tables when working with V ena
Tables.

Transaction and Staging tables important?
Vena Support Team
Updated 11 months ago
02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 1/8

Data Querying
Vena Tables
Explainer: Set Staging or
Transactions Tables When
Building a Vena Table
How-To: Exporting Data From a
Vena Table
How-To: Managing and Deleting
Data Using Vena Tables
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
Troubleshooting DataOn the V ena platform, tables organize and present data logically to address specific business
function s. When creating a V ena Table, selecting a Transaction or Staging table lets users take
control of the creation process.  Previously , there was no formalized way to define the intended
function of a V ena Table. For example, if a table held ephemeral staging data or persistent transaction
data, the creation process was identical, with dif ferences only apparent  at the use case and clear
slice level. With the V ena Hub on Azure (VHOA) project, users can now manually select Transaction
or Staging table types.
Table types
Staging: Used for data transformations
Transaction: Used for drilling into compiled data
Before you define a table type, you must create a new Vena Table:
1. Navigate to the Modeler tab and select Data Transformations.
2. Select Channels.
3. Select Create and choose Vena Table from the drop-down list.
When the Create Vena Table window opens, the Transaction button is disabled by default. To
enable the button, select a data model from the drop-down list.02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 2/8

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
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Once you select a data model, V ena pre-populates its dimensions into your chosen table . If you clear
the data model selection , the Transaction button will be disabled again.  02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 3/8

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesHow do I edit a table after I’ve created it?
If you want to edit the table after it’s created , and if it is a Transaction table you will not be able to:
Remove dimension columns
Change data model
Change table type
Every other action is permitted .
How do I populate dimensions?
Dimensions are now automatically populated in the table columns, significantly reducing the
need for troubleshooting drill tables.02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 4/8

02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 5/8

Can I dynamically link to a data model?
Tables are now directly linked to the data model. Any changes to dimensions—whether added,
deleted, or renamed—will automatically reflect in the table, ensuring seamless updates.
How do I add new columns to a Vena Table?
When a user creates a Vena Table, that table focuses on the parent-level members of the data
model. Adding a column to a Vena table refocuses the table contents on the bottom-level
members.
Can I switch between table types and data models?
There are a few use cases where you can switch between table types and data models.
Case 1:  Switching from "Staging"  to "Transaction"
A confirmation modal appears. If the user confirms, all columns are reset, and
dimensions from the selected data model are populated.
Case 2:  Switching within Data Models while on "Staging"
No confirmation modal appears.
Case 3:  Switching from "Transaction"  to "Staging"
A confirmation modal appears. If the user confirms, all columns are reset.
Case 4:  Switching within Data Models while on "Transaction"
A confirmation modal appears. If the user confirms, all columns are reset and
updated according to the newly selected data model.  02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 6/8

Was this article helpful?
0 out of 2 found this helpful


Related articles
How-To: Setting Drill Transactions on a
Template or Report
How-To: Setting up a Staging Query (Vena 365
Only)
How-To: Using Drill Functions (Drill Down, Drill
Save and Drill Transactions)
Reference: ETL Guide - 5 - SQL Staging
Environment
Explainer: Vena User RolesRecently viewed articles
Troubleshooting: ETL Error Guide
Troubleshooting: MQL Invalid Expression
Syntax When Creating a Calculated Member
How-To: Creating Advanced Integration
Setups With VenaQL
Troubleshooting: ETL Export MQL Query
Returning No Data
Reference: Using Wildcard in Model Slice
Expression02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 7/8

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:53 Explainer: Set Staging or Transactions Tables When Building a Vena Table – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/33910970385421-Explainer-Set-Staging-or-Transactions-Tables-When-Building-a-Vena-Table 8/8
