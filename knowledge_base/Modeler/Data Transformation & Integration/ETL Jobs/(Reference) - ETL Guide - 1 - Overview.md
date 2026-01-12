# (Reference)   ETL Guide   1   Overview

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
ETL JobsReference: ETL Guide - 1 - Overview
Part 1: Overview - You are here
Part 2: Vena.io ETL
Part 3: Command Line ETL
Part 4: Query Languages
Part 5: SQL Staging Environment
Vena Support Team
Updated 29 days ago
02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 1/20

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
Restrictions to the SQL WHEREPart 6: Using Staging Data
Table of contents
Chapter 1: Overview
Introduction to ETL
ETL Options
Prerequisites
User Permissions Setup
ETL Requirements
Import Options and Data Source Requirements
Source Data Formats
Chapter 1: Overview
Introduction to ETL
The process of extracting data from source systems and loading to the Vena Database is
commonly called ETL, which stands for extraction, transformation and loading.
Vena ETL is an easy-to-use tool, designed to assist Modelers with data integration tasks since
designing and maintaining the data integration process could be complex and resource-02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 2/20

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
Data Queryingintensive. Modelers can leverage the ETL tools available in Vena Cloud to manage the following
data integration tasks:
Import Data, Hierarchies, Attributes, Line Items, and User Defined formats from .csv and .tdf.
Transform data to a Vena standardized format to meet integration requirements.
Export Data and Hierarchies.
There are 2 methods of loading data into the Vena Data Model via the ETL:
Load data directly from a standard file in the following formats:
.csv
.Scsv
.tdf
Load data via a staging table. This is required if data is not in a standarized format accepted
by the Vena Model. So, SQL transformations are used against staging data.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 3/20

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
& ConnectionsETL Options
Modelers can perform ETL Data Integration tasks using one of the following options:
1. ETL option in vena.io (visit Chapter 2: vena.io ETL)
2. Vena command line ETL tool (visit Chapter 3: Command Line ETL)
Note_Icon_Small.png Note
Staging Tables are only required for the User Defined file format.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 4/20

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
Prerequisites
User Permissions Setup
Users are required to have the following Permissions to perform ETL Data Integration tasks.
They must have access to the Modeler role, Create/Read/Update/Delete Application Permissions
on the data model, and Read/Write Data Permissions (if applicable).02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 5/20

Note_Icon_Small.png Note
The Vena Admin is responsible for creating and/or assigning all of the above
Permissions.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 6/20

ETL Requirements
Import Options to Data Source Requirements
Vena source data is required to be in Comma-separated values (.csv) format. Users can load the
following data structures from a .csv file:
Step Type
The Step Type defines the source and target order of operations for the import template.
Import TypeDescriptionStaging Table
Required?
File to CubeUsed when the objective is to import from a File to the Cube.      ✗
File to StageUsed when the objective is to import from a File to a Staging
Table.      ✔
SQL TransformUsed when the objective is to manipulate data in the Staging
Table using a SQL Query.      ✗
Stage to CubeUsed when the objective is to import from a Staging Table to
the Cube.      ✗
Cube to StageUsed when the objective is to import from the Cube to
a Staging Table.      ✔02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 7/20

Data Type
The Data Type defines the contents that are to be imported.
Import Type DescriptionStaging Table
Required?
Dimension
HierarchyData Model structure made up of
Dimensions and Dimension Members.      ✗
Values Values belonging to the Dimension Members.       ✗
Line-Item DetailsLine-Item Detail values.       ✗
Attributes Attribute tags on the Data Model Dimensions.       ✗
User Defined User Defined criteria which uses a Staging Table.       ✔
Source Data Formats
Each source data file needs to be in a certain format to load Data, Dimension Hierarchies,
Intersection Values, Line-Item Details and Attributes.Files need to have specific header names or02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 8/20

no headers at all (order of the columns have to be the same). Also, the dimensions must first be
added in the Data Model under the Modeler tab, prior to importing data files.
Hierarchies
Hierarchy load files can be used for the following actions:
Create a hierarchy
Create an alternate hierarchy
Re-structure an existing hierarchy
Loading a New Hierarchy
Here is a sample of a file that can be used to create a Dimension Hierarchy. As with all .csv files,
the spaces are entirely optional. Note the use of commas (,) to delimit the columns. The headers
must be the same as below:
_Dimension
Name_Child
name _Child Alias _Parent Name  _Operator _Cmd
Time Year Year +
Time  H1  Half  Year + +
Time All
QuartersAll Quarters     Year + +
Time Q1 Quarter 1 All Quarters + +02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 9/20

Time Q2 Quarter 2 All Quarters + +
Time Jan January Q1 + +
Time Feb February Q1 + +
Time Mar March Q1 + +
Time Apr April Q2 + +
Time May May Q2 + +
Time Jun June Q2 + +
Time Jan January H1 + +
Time Feb February H1 + +
Time Mar March H1 + +
Time Apr April H1 + +
Time May May H1 + +
Time Jun June H1 + +02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 10/20

Modify a Hierarchy
To modify a Hierarchy, one can use the same file format with an extra “_Cmd” column on the
right indicating whether to add or remove a parent/child relationship from the model.
For example, suppose Jan currently existed within Q1, nestled within H1. To use ETL to remove
the month Jan from its current location, to live directly under Year, one would create a file like
this:
_Dimension
Name_Child
name _Child Alias_Parent
Name  _Operator _Cmd
Time Jan January H1 + -
Time Jan January Q1 + -
Time Jan January Year + +
Hierarchy Guidelines
The dimension members are denoted in a parent/child structure.
Field Description
_Dimension
NameName of the Dimension.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 11/20

Field Description
_Child
NameMembers must be specified from the top down. For example, any parent
referenced in a row must have appeared in a previous row.
_Child AliasAlternative title associated with the respective dimension member.
_Parent
NameLeaving the column _Parent_Name empty means that the member will be
added at the top of the hierarchy.
_OperatorThe Operator is used for roll-ups, and can be +, -, or \~ (ignore).
_Cmd(Optional): Indicates which relationships to add or remove between members.
Use “-“ and “+” to indicate whether the member should be removed from the
associated parent.
+ Adds the respective member to parent
- Removes the respective member from parent. It does not mean delete.
If omitted, a “+” is assumed.
Intersection Values
Intersections are the data values of a model. Intersections can be manually keyed into templates
as a way to commit data into the cube, or they can be imported for mass upload purposes.
File Format to Import Intersections
Here is a sample of a file that can be used to load values into the Data Model. This example has
two Dimensions, Account and Period, as well as the associated values.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 12/20

_dim1_member _dim2_member_dimN_member..._value
Sales Jan ... 78,000
Sales Feb ... 66,000
Sales Mar ... 43,000
Fee Income Jan ... 36,000
Fee Income Feb ... 12,000
Fee Income Mar ... 61,000
Intersection Guidelines
Field Description
_dim1_memberA column using the format _dim<value>_member is defined for each Dimension.
_dim2_memberA column using the format _dim<value>_member is defined for each Dimension.
_value Data values for the respective Intersection Points.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 13/20

Line-Item Details
Line-Item Details are an additional level of detail that can be added to the general ledger. This
feature is mainly used from a budgeting perspective for users to build a budget by entering
detailed lines, but can also be imported into the application.
File Format to Import Line Items Details
Here is a sample of a file that can be used to import Line-Item Details. The result of this import
would bring in two new line items for Cost of Sales and Supplies for January.
_dim1_member,_dim2_member,_dimN_member...,_lid_label_text,_lid_value,_etl_id,
Cost of Sales,Jan, ..., Freight, AA1,
Cost of Sales,Jan, ..., Other Fees,AA1,
Supplies, Jan, ..., Machine
Rentals,BB1,
Note_Icon_Small.png Note
To import intersection values, a data model with the given dimensions must already
exist.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 14/20

Supplies, Feb, ..., Machine
Rentals,BB1,
Line-Item Details Guidelines
Field Description
_dim1_memberA column using the format _dim<value>_member is defined for each Dimension.
_dim2_memberA column using the format _dim<value>_member is defined for each Dimension.
_lid_label_textLine-Item Detail respective text label.
_lid_value Line-Item Detail respective value.
_etl_id (Optional) - Allows you to control whether a line is created, or whether an
existing line is to be re-used instead. These ID’s would need to be generated
outside of Vena.
The _etl_ids are 40 character strings. They will be saved in the database so you can use them
even across multiple ETL loads.
If you specify an _etl_id then the system will use it to keep track of that label on future lines.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 15/20

If you want to re-use the same label elsewhere, simply provide the same _etl_id. In the example
above, although we are loading four LIDs, only one label will be created for Supplies. LIDs are
supported for both bottom-level intersections and parent (roll-up) intersections.
Attributes
Attributes are user-defined tags that can be added to members of a dimension. Attributes assist
in providing more detail to members without defining them as part of the dimensional hierarchy
and can also be used in an expression to further filter on the hierarchy based on the joint use of
operators and the attributes.
File Format to Import Attributes
To import attributes, a four-column format is used: Dimension Name, Member Name, Attribute
Name and Command.
dim_namemember_nameattr_namecmd
D1 M1 A1 +//attaches M1 to A1.
D1 M1 A1 -//removes M1 from A1.
D1 A1 -//removes attribute A1
from all members.
D1 M1 -//removes all attribute
from M1 member.02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 16/20

Field Description
dim_name This column defines the dimension name.
member_nameThis column defines the dimension member name.
attr_name This column defines the dimension member attribute
name.
cmd + Attaches the respective attribute,
- Removes the respective attribute,
If omitted, a “+” is assumed.
User-Defined
A user-defined data format refers to an import whereby external data outside of the general
ledger is brought into a staging table, to be connected to Vena.
File Format to Import User Defined
A user-defined data format refers to an import whereby external data outside of the general
ledger is brought into a staging table, to be connected to Vena.
_cats    , _dogs02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 17/20

maru     , snoopy
nyan cat , doge
If the first row contains fields beginning with an underscore, it is treated as a header row. The
header values will be used as the column names in the SQL table. Otherwise, the SQL columns
are namedc1, c2, c3, etc., based on the number of columns in the first row. In this example, the
table will be created with two columns named_cats and _dogs. Currently, white space cannot be
included in a column name. For example,_cat typewill fail with an error on load.
Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
3 out of 4 found this helpful
Related articles
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 3 - Command Line ETLRecently viewed articles
Troubleshooting: No Values Generate for a
Reporting Currency02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 18/20

Troubleshooting: ETL Error Guide
How-To: Importing Data to Vena with
Microsoft Power Automate Connector
How-To: Bulk Attach/Detach Attributes and
Filter by AttributesTroubleshooting: Calc Script Using
.BottomLevel() and .Exclude() in a Tuple Not
Working Properly
Troubleshooting: Calc Is Not Triggering or
Calculating After Data Load or Import
Troubleshooting: Calc Conversion Not
Working or Zero Values Appearing
Troubleshoot: Calc Target Contains Data Even
Though It Shouldn’t
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 19/20

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 16:41 Reference: ETL Guide - 1 - Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027735972-Reference-ETL-Guide-1-Overview 20/20
