# (How To)   Creating Advanced Integration Setups With VenaQL

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Data Querying Search
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
ETL JobsHow-To: Creating Advanced
Integration Setups With VenaQL
Need to create an integration that is too complex to achieve with a standard
integration channel setup? Use VenaQL to combine sources and perform advanced
data transformations.
Why use this feature?
Laura Harris
Updated 1 month ago
02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 1/32

Data Querying
How-To: Using the Query Agent
to Build MQL Expressions (Beta)
Reference: Writing Expressions
(MQL & HQL)
Reference: Using Wildcard in
Model Slice Expression
Troubleshooting: ETL Export
MQL Query Returning No Data
How-To: Creating Advanced
Integration Setups With VenaQL
Troubleshooting: MQL Invalid
Expression Syntax When
Creating a Calculated Member
Troubleshooting: ETL Error
Guide
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite IntegrationVenaQL is a SQL-like query language for advanced data transformation, which helps perform
tasks such as:
Joining multiple Vena sources, such as Salesforce connectors, ERP connectors and Vena
tables.
Building complex logic involving multiple tables.
Consolidating data from multiple sources.
Building logic based on table values, like:
In-transaction matching,
Balance sheet activity calculations,
Dynamic allocations.
Before you begin
To follow the instructions in this article, you must have at least Modeler access. If you are
unfamiliar with the Vena Integration tool, please read the Integration article series before
proceeding.
As VenaQL syntax is similar to SQL, familiarity with SQL — particularly SELECT statements—is
essential for these queries. Please refer to the Reference Guide in this article for details on
VenaQL syntax.
Video
Check out a video of this article's content.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 2/32

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
How-To: Restoring Data That Has
Been Accidentally Overwritten orVideo VenaQL Video VenaQL
Table of Contents
About the feature
VenaQL
VenaQL sources
Reducing ETL complexity with VenaQL
Enabling VenaQL on Azure
VenaQL Query Editor02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 3/32

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
Product UpdatesGetting there
Overview
Creating VenaQL queries
Reference Guide
Supported functions
Notes and limitations on supported functionality
VenaQL Cheat Sheet
Source availability
Best practices
Use Cases
Use Case #1 - Unioning multiple tables
Use Case #2 - Joining multiple data sources

About the feature
VenaQL
VenaQL is a query language that allows complex transformations supported by SQL, without the
complexity of managing a database.
Within the Integration tool, VenaQL acts as a type of integration source. It is NOT a source itself,
as it does not contain data—rather, it draws data from multiple sources, then manipulates that
data before feeding it into an integration channel and on to its destination.
This process allows for easier querying of multiple sources inside Vena than with SQL alone.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 4/32

VenaQL sources
The VenaQL source is like a container for a VenaQL query, allowing it to be used as part of an
integration channel.
Think of a VenaQL source as an automatic staging table and transformation assistant. Data is
processed in the source itself, so data transformation work is completed before data is output to
the channel. Querying is easier and there’s no need to separately stage the data first. Output
data from a VenaQL source is fully ready to be integrated into the destination.
Reducing ETL complexity with VenaQL
Say you have four different sources to integrate data from. To integrate data from all four, you’d
traditionally have to create four separate integration channels, each with its own ETL logic and
clear slice configuration, to ensure proper consolidation.
With VenaQL, this entire process is streamlined into one easy-to-maintain query:02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 5/32

Enabling VenaQL on Azure
If your organization hosts Vena on Microsoft Azure, you must enable VenaQL via a server
property.
1. Locate the following server property:
Server Property Name: restrictVenaQLDevelopment
2. Set this property to false.
Note
Organizations hosted on AWS can skip this section.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 6/32

VenaQL Query Editor
Getting there
The Query Editor is built into Vena’s Integration tool and is the primary user interface for
VenaQL. To get to the Editor:
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar.
3. Select Channels from the sidebar tab.
4. Select the Create button in the top right-hand corner of the screen.
5. Hover over Source to view its sub-menu and select VenaQL.
02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 7/32

6. This opens the VenaQL Query Editor.
Overview
Note
Microsoft Azure users: If you do not see the VenaQL option in the Source menu,
you likely have the Restrict functionality for VenaQL set to true. Refer to the above
section to remove the restriction.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 8/32

A. Source name field. Enter a name for the VenaQL source here. You cannot save a VenaQL
source without naming it.
B. Channels and Sources pane. Channels and sources that can be referenced in the VenaQL
query. You may also extract and preview individual sources. See the note below on source
availability.
Note02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 9/32

C. Source options. Copy, preview or refresh data from a particular source.
D. Query pane: Create the VenaQL query using VenaQL syntax here. See the Reference Guide
below for help.
E. Refresh All button. Refreshes all source data for the VenaQL query. This must be done at
least once before previewing the source.
F. Preview VenaQL source button. Generates a preview of the output of the VenaQL source,
using the query as currently configured in the Query Pane. Once generated, this preview is
displayed under the Current Source tab in the Preview Pane.
G. Save button. Allows you to save the query, regardless of state (including incomplete/invalid
queries). Check off the Save and Validate option to also validate the query when saving
(unchecked by default).
H. Close button. Closes the VenaQL Query Editor and returns you to the Channels sidebar tab.
I. Pane resize/close handles. Click-and-drag to resize each of the Channels and Sources, Query
and Preview Panes, or click to close.
J. Preview pane. Displays previews of the query output and the source. The VenaQL query
output is displayed under the Current Source tab, while a source preview is shown under an
additional tab with the name of the previewed source. The Current Source tab is always visible;
only one source preview tab may be viewed at a time (in addition to the Current Source tab).
The options listed here are the sources in the same file path as your VenaQL query.
Sources in other file paths may be included in your query as well.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 10/32

Creating VenaQL Queries
Like a SQL SELECT statement, a VenaQL query always follows the basic SELECT statement
structure: SELECT x FROM y. The main difference is the FROM clause identifies the sources you
wish to draw from—in standard SQL, FROM identifies the table containing your data.
These VenaQL sources can be existing Integration sources of any type, including other channels
and other VenaQL sources.
The basic steps of creating a VenaQL query are:
1. Extract and preview sources
2. Write the VenaQL query
3. Save and Validate (or just Save)
4. Debug
5. Deploy
Note
Existing staging data and procedures are not automatically available via Vena Tables;
they must be ported over by Vena Consultants. If you would like to move existing
staging data and procedures, please contact your Account Manager.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 11/32

Let’s look at this process in more detail.
Step 1: Extract and preview sources
Consider the classic SQL query SELECT x FROM y.
‘x’ = the column of the source being queried.
‘y’ = the source itself. In SQL, this is a specific table. In VenaQL, this can be a table, a connected
GL, an Integration channel or even another VenaQL source already set up.
1. You must extract a source’s inputs to a staging area before it can be previewed. Under
Channels and Sources in the Query Editor, hover over a source to see its options.
Note
There are limitations to what SQL-type commands VenaQL accepts. For example,
SELECT * is not supported in VenaQL. Refer to the Reference Guide in this article
for details on which queries VenaQL supports.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 12/32

2. Select the
(Refresh data) icon to open a tab in the Preview pane for that source. If
needed, select Jobs to view the History tab of the integration tool to check on the
extraction’s progress. 02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 13/32

Note: Ensure you have named and saved this source first, so you may return to it.
3. Repeat this extraction process for any other source you want to use in your query.
4. When the extraction jobs show as Completed in the History tab, return to the Query Editor
and select Preview next to each of the extracted sources. This opens a tab for that source in02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 14/32

the Preview pane, showing all column names.
Step 2: Write the VenaQL query
Using the column and table names from the extraction preview, enter your query (e.g., SELECT...)
in the Query pane. Refer to the Reference Guidefor syntax help.
You may use the Copy to clipboard icon in-line with a channel or source to copy and paste their
names in your query. Hover over a column name in the Preview pane to copy its name to a02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 15/32

clipboard as well.
Step 3: Preview and validate
1. Select the checkbox next to Save and Validate.
02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 16/32

2. Select Save.
The Query Editor will perform a query validation (checking for syntax errors, whether a
source is valid, etc.). Once complete, the results are displayed in a new window.
Failed Validation:
Passed Validation:02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 17/32

3. Check the query at any time to ensure returns the expected results by selecting Preview.
This preview appears under the Current Source tab in the Preview pane.
02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 18/32

Note: You must first refresh the data referenced in the query (as described in Step 1) for the
Preview function to work.
Step 4: Debug
Use the validation and preview functions to debug your query as needed. Then, select Save.
Step 5: Deploy
Select Close to return to the Channels window. The completed VenaQL source will now appear
in this table, ready for deployment in an Integration channel like any other source.
02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 19/32

Reference Guide
Supported functions
Below are the accepted syntaxes for use in VenaQL, including their uses for those needing a
knowledge refresh.
Function Syntax Use
String Functions
TRIM TRIM([characters FROM ]string) Removes leading or trailing
characters or spaces from a
string.
LTRIM LTRIM(string) Removes leading spaces.
RTRIM RTRIM(string) Removes trailing spaces.
LEFT LEFT(string, number_of_chars) Extracts a number of characters
from a string (starting from left).
RIGHT RIGHT(string, number_of_chars) Extracts a number of characters
from a string (starting from
right).
SUBSTRING SUBSTRING(string, start, length) Extracts some characters from a
string.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 20/32

CHARINDEX CHARINDEX(substring, string, start) Searches for a substring in a
string and returns the position.
If the substring is not found, the
function returns 0.
Note: Not case-sensitive.
STRPOS STRPOS(string, substring) Returns the position of the first
occurrence of a substring in a
string.
If the substring is not found, the
function returns 0.
Note: Case-sensitive. Common
in PostgreSQL.
LENGTH LENGTH(string) Returns the length of a string (in
bytes).
CONCAT CONCAT(expression1, expression2) Adds two expressions together.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 21/32

REPLACE REPLACE(string, from_string, new_string)Replaces all occurrences of a
substring within a string, with a
new substring.
UPPER UPPER(text) Converts a string to upper-case.
LOWER LOWER(text) Converts a string to lower-case.
Aggregate functions - performs a calculation on a set of values and returns a single value.
COUNT COUNT(expression) Returns the number of records
returned by a select query.
Note: NULL values are not
counted.
AVG AVG(expression) Returns the average value of an
expression.
MIN MIN(expression) Returns the minimum value in a
set of values.
MAX MAX(expression) Returns the maximum value in a
set of values.
SUM SUM(expression) Calculates the total for a set of
values.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 22/32

Note: NULL values are ignored.
STDEV STDEV(expression) Calculates the amount of
variation for a set of values.
STDEVP STDEVP(expression) Calculates the population
standard deviation for a set of
values.
VAR VAR(expression) Calculates how far values in a set
deviate from the mean.
VARP VARP(expression) Calculates the population
variance for a set of values.
Joins - combines rows from two or more tables, based on a related column between them.
INNER JOINSELECTcolumn_name(s)
FROMtable1
INNERJOINtable2
ONtable1.column_name = table2.column_name;Selects records that have
matching values in both tables.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 23/32

LEFT JOINSELECTcolumn_name(s)
FROMtable1
LEFTJOINtable2
ONtable1.column_name = table2.column_name;Returns all records from the left
table (table1), and the matching
records from the right table
(table2). The result is 0 records
from the right side, if there is no
match.
RIGHT JOINSELECTcolumn_name(s)
FROMtable1
RIGHTJOINtable2
ONtable1.column_name = table2.column_name;Returns all records from the
right table (table2), and the
matching records from the left
table (table1). The result is 0
records from the left side, if
there is no match.
FULL JOINSELECTcolumn_name(s)
FROMtable1
FULLOUTERJOINtable2
ONtable1.column_name = table2.column_name
WHEREcondition;Returns all records when there is
a match in left (table1) or right
(table2) table records.
Unions
UNION
DISTINCTSELECTcolumn_name(s)FROMtable1
UNION
SELECTcolumn_name(s)FROMtable2Combines the result-set of two
or more SELECT statements.
UNION ALLSELECTcolumn_name(s)FROMtable1
UNIONALL
SELECTcolumn_name(s)FROMtable2The UNION operator selects only
distinct values by default. To
allow duplicate values, use
UNION ALL.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 24/32

Other functions
CASTCAST(expression AS datatype(length)) Converts a value (of any type)
into a specified datatype.
COALESCE COALESCE(val1, val2, ...., val_n) Returns the first non-null value
in a list.
GROUP BYSELECTcolumn_name(s)
FROMtable_name
WHEREcondition
GROUPBYcolumn_name(s)Groups rows that have the same
values into summary rows.
ORDER BYSELECTcolumn1, column2, ...
FROMtable_name
ORDERBYcolumn1, column2, ... ASC|DESC;Used to sort the result-set in
ascending or descending order.Notes and limitations on supported functionality
While VenaQL empowers users to manipulate data independently, there are a few limitations to
be aware of:
1. Users can insert multi-line comments into VenaQL using the `/* <multi line comment> */`
syntax.
2. Pivot/unpivot syntax is not yet available. However, this functionality can be achieved through
integration channels.
3. The columns are all currently TEXT.
4. Expressions can only be TEXT or DECIMAL at this time. Additionally, DATEand TIME types are
not yet available.
5. Existing staging data and procedures are not automatically available via Redshift; they must
be ported over by Vena Consultants. If you would like to move existing staging data and
procedures, please contact your assigned Account Manager.
6. VQL supports only SELECT statements. Users cannot create, update, delete or insert tables.
7. Foreign keys, triggers, stored processes and constraints are not yet supported.
8. SELECT * is not supported. This is intentional, and it will never be supported in VQL.
9. Users cannot preview VQL sources that reference other VQL sources without first extracting
all sources to staging.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 25/32

10. Windows functions are not yet supported.
11. Users can only comment on lines with -- .
12. Multi-line comments will not be supported.
13. VenaQL performs case-sensitive string comparisons. To ensure consistent results, use
LOWER or UPPER functions to normalize text values in SELECT statements for faster
processing. If preserving original text case is needed, apply these functions in WHERE,
HAVING, ON or ORDER BY clauses. Additionally, normalize case for data imported via file
uploads or Vena Table Destination channels.
14. The query SELECT DISTINCT is supported by Vena.
Cheat Sheet 02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 26/32

Source availability
Any source with a unique name can be queried, such as Salesforce connectors, ERP connectors,
Vena tables, and even other VenaQL sources. Two sources with the same name cannot be
queried.
Remember, the sources that appear under the Channels and Sources pane in the Query Editor
are simply those in the same file path as the query you’re writing. Others may be referenced as
well.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 27/32

Best Practices
We recommend inserting comments into your VenaQL code to describe the purpose of your
VenaQL source. This provides context for your team and Vena Support if they are required for
troubleshooting.
Recommended details:
Author, date, description, purpose
Remember to start with "--"
Example:
----------------------------------
-- Author:
-- Date:
Note
Channels are considered sources, and you can reference the output of a channel
from VenaQL.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 28/32

-- Description:
----------------------------------
Use Cases
Use Case #1 – Unioning multiple tables
SELECT
     "Account",
     "Entity",
     "Department",
     "Amount",
     "Date"
FROM "TableA"
UNION ALL
SELECT
     "Account",
     "Entity",
     "Department",
     "Amount",
     "Date"
FROM "TableB"02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 29/32

Use Case #2 – Joining multiple data sources
SELECT
     a."AccountID",
     a."Entity",
     a."Department",
     a."Rate",
     a."Amount",
     b."Salesrep",
     b."Opportunity",
     b."Description",
     c."Industry",
     c."Vendor"
FROM "Vena Table" AS a
INNER JOIN "Salesforce Source" AS b
     ON a."AccountID" = b."AccountID"
INNER JOIN "Vena Cube Source" AS c
     ON a."AccountID" = c."AccountID"
VenaQL Cheat Sheet.jpg200 KB
Was this article helpful?
7 out of 8 found this helpful02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 30/32

Related articles
Reference: Vena Calcs - 5 - Functions
How-To: Setting up a Staging Query (Vena 365
Only)
Reference: ETL Guide - 5 - SQL Staging
Environment
How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
Troubleshooting: Adding up Drill Down Values
Returns an Incorrect Total or Incorrect Rollup
MultiplierRecently viewed articles
Troubleshooting: MQL Invalid Expression
Syntax When Creating a Calculated Member
Troubleshooting: ETL Export MQL Query
Returning No Data
Reference: Using Wildcard in Model Slice
Expression
Reference: Writing Expressions (MQL & HQL)
How-To: Using the Query Agent to Build MQL
Expressions (Beta)
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 31/32

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:51 How-To: Creating Advanced Integration Setups With VenaQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360021796492-How-To-Creating-Advanced-Integration-Setups-With-VenaQL 32/32
