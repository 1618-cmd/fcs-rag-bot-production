# (How To)   Create and Manage a Data Model Hierarchy Using ETL Import

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
ETL JobsHow-To: Create and Manage a Data
Model Hierarchy Using ETL Import
Using Vena'sETL(Export-Transform-Load) tool, you can significantly reduce the effort and
time needed to perform bulk actions on your data model. ETL allows you to automate many of
the steps involved in creating and managing a data model using just a simple .csv file and is an
invaluable time-saving tool for any Vena Modeler.
Video
Laura Harris
Updated 1 month ago
02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 1/21

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
Restrictions to the SQL WHERECheck out a video of this article's content.
ETL Tool Hierarchy load ETL Tool Hierarchy load
Why use this feature?
This article focuses on the ETL tool's File To Cube Import feature and will teach you how to
perform an ETL Import to modify your hierarchy, as well as how to format the necessary .csv file.
In addition, practical examples are provided to demonstrate how to perform various common
hierarchy management actions using the ETL tool.
The ETL tool has numerous functions, including different types of Import. However, the scope of
this guide is limited to importing a hierarchy to the data cube File To Cube, and will not describe
any of the other available functions. Additionally, while it is possible to perform the actions02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 2/21

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
Data Queryingdescribed in this guide using SQL staging tables, this guide only covers using the direct .csv file
method.
Before you begin
To complete the steps outlined on this page, you will need at least Modeler access.
Table of contents
How to
Part 1: Prepare the .csv file
Part 2: Perform the ETL Import
Notes
Examples
Best Practices
How to
Part 1: Prepare the .csv file
To upload a hierarchy using ETL:
1. Create a .csv file containing a table of the hierarchy members to be created, deleted, shared
or modified.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 3/21

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
& Connections2. The format for a .csv file used to add/remove/share/modify members is as follows (header
row in bold):
_Dimension Name_Child
name_Child Alias _Parent
Name_Operator_Cmd
Account New
AccountA New AccountAll Accounts + +
Dimension Name (mandatory): The dimension name for the member referenced in the
row.
Child Name (mandatory): Name of the member to be created, deleted, shared or modified.
Parent Name (optional): Indication of the member parent. Required if adding a member as
a child, sharing a member as a child or deleting a child. A blank entry will indicate a top-level
Note
Each row in the table specifies a single dimension member and instructs the ETL
tool on what action should be performed on it. The .csv file must be created
according to a specific format so that it can be understood by the ETL tool. As ETL
Import always interprets .csv files according to this format, a header row can be
included but is not mandatory. However, for ease of use and to facilitate
troubleshooting, including a header row is recommended. For clarity, all of the
examples included in this guide will use a header row.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 4/21

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
Product Updatesmember. Also used to help identify shared members, where the same member appears in
the hierarchy multiple times under different parents.
Operator (optional): Sets the rollup calculation type: + (add), - (subtract) or ~ (ignore). If left
blank, + will be set by default.
CMD (optional): Indicates if the row member should be added to or deleted from the
hierarchy. The operators + (add) or - (delete) may be used. If left blank, + will be set by
default. If the entry is used to modify an alias or operator, + should be used.
Part 2: Perform the ETL Import
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab. By default, you should be in the Templates
section of the ETL tool, which lists your existing ETL templates.
4. Select + Create Template. This opens the ETL Template drawer.
5. Enter a name for the ETL Template.
6. Select Add Step. 02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 5/21

7. Select File to Cube from the drop-down menu.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 6/21

02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 7/21

8. Select Hierarchy from the Select Data Type drop-down menu.
9. Select Add.You can add additional steps if desired, however, this guide will only cover
hierarchy uploads, so only one step is needed.
10. Select Save to add the new step to the ETL template.
11. Select the
 (Run) icon next to the ETL Import template you want to execute.
1. Drag and drop a file, or browse your desktop and select a file.
2. Select a File format for the source document.
3. Select the File encoding.
4. Select the number of Accepted invalid lines.
*The number of acceptable invalid lines allows a user to specify the number of row errors
that can be skipped as part of an import.Since this is a File to Cube template, you will have to
do some additional configurations:
Note
You cannot create a schedule for templates with File to Cube of File to Stage
steps.
However, you can enable job notifications. To enable job notifications, move the
toggle next to Enable Notifications to ON.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 8/21

12. Select Run. This begins the Import job which will transfer the hierarchy from the .csv file into
your data cube.
13. You can check on the progress of the Import job by selecting Historyfrom the sidebar tab.
Locate the job in the Jobs table by name to check on its status.
14. When your ETL Import job has been completed, you can review the changes to your hierarchy
by selecting the Members tab in the Modeler section, where all dimensions and their
corresponding members are listed.
Notes02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 9/21

Each row of the .csv file references a single member and a single action.
All member additions ('+' CMD) will be processed before any deletions ('-' CMD), regardless of
the order in which they appear in the .csv file. When the ETL tool encounters a delete CMD,
the referenced member will be “marked for deletion” at the end of the corresponding ETL
step, making it possible to “move” a member by deleting it first, then adding it back with a
different parent later in the same file.
Each step of an ETL job will be processed as a separate file.
Adding a member with the same name as an existing member, but with a different parent,
will create a shared member.
Sharing a member will result in two members in two locations of the hierarchy, sharing the
same intersection values, Alias, and internal member ID.
Shared members act like a single entity, and changes to the Alias or Operator for one shared
member will be applied to all shared members of the same name.
Only bottom-level members can be shared.
Moving a member is a two-step process, wherein a member is first deleted in the original
location and then added back to a new location.
Adding ('+' CMD) a member with the same name and parent as an existing member will
update the Alias and/or Operator for that member to whatever is specified in the .csv file, but
will not otherwise affect the existing member or intersection values.
For shared members, the parent name field will determine which instance of the member is
being referenced in the hierarchy.
There are no confirmations for deletions.
If a member is deleted and not added back in the same file, all intersection data will also be
deleted.
If a parent member is deleted and not added back in the same file, all children and
intersections will also be deleted.
Deleting a member in one .csv file and adding it back using another .csv file, even to the same
location and with the same name, will result in the member being assigned a new Member ID
and may cause mapping problems. Moving a member must be completed in a single ETL step
and within a single upload file.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 10/21

Examples
You can refer to the following practical examples for help in creating your .csv hierarchy file. In
each example, the key parameter for the operation has been highlighted in red. The effects that
running each example would have on a hypothetical hierarchy are also shown in a before/after
illustration.
I. Add a new member
To create a new member in the hierarchy, use '+' in the CMD column:
_Dimension Name_Child
name_Child Alias _Parent
Name_Operator_Cmd
Products Widget ProA Bigger
WidgetWidgets + +
Hierarchy Before Hierarchy After
All Products
Widgets
Widget XLAll Products
Widgets
Widget Pro02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 11/21

Widget XL
I. Delete an existing member
To remove a member from the hierarchy, use '-' in the CMD column:
_Dimension Name_Child name_Child Alias_Parent Name_Operator_Cmd
Products WidgetOld Widget Widgets + -
This will remove the indicated member from the hierarchy.
If you do not add the same member back as part of the same ETL Import, and there are no
shared members of the same name, all intersections will also be deleted.
Hierarchy Before Hierarchy After02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 12/21

All Products
Widget
Widget XL
Widget Pro
WidgetsAll Products
Widget XL
Widget Pro
Widgets
III. Add a shared member
To add a member with the same name as an already existing member, but under a different
parent (a shared member), use '+' in the CMD column:
_Dimension Name_Child name_Child Alias_Parent Name_Operator_Cmd
Products Widget Pro New Products + +
The child name must be the same as a member who already exists in the hierarchy or a
member that has already appeared higher in the table in the same .csv file.
The parent name must be different from the parent under which the existing member is
located.
The new shared member can have a different alias than the existing member if desired.
Only bottom-level members can be shared. Attempting to create a shared member that is a
parent will result in an error.02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 13/21

Hierarchy Before Hierarchy After
All Products
Widget
Widget XL
Widget Pro
Widgets
New Products
Widget XLAll Products
Widget
Widget XL
Widget Pro
Widgets
New Products
Widget XL
Widget Pro
IV. Delete a shared member
To remove a shared member (a member with the same name as another member under a
different parent) from the hierarchy, use '-' in the CMD column:
_Dimension Name_Child name_Child Alias_Parent Name_Operator_Cmd
Products Widget Pro Widgets + -02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 14/21

The child name must be the same as a shared member which already exists in the hierarchy
or a shared member that has already appeared higher in the table in the same .csv file.
The parent name must be the parent of the shared member and will determine which of the
shared members will be removed.
As long as at least one member with the same name as the deleted member still exists in the
hierarchy by the end of the .csv file (i.e., after all changes specified in the file have been
processed), no intersections will be deleted.
Hierarchy Before Hierarchy After
All Products
Widget
Widget XL
Widget Pro
Widgets
New Widgets
Widget XL
Widget ProAll Products
Widget
Widget XL
Widgets
New Widgets
Widget XL
Widget Pro
V. Move a member
To move a member from one branch of the hierarchy to another (i.e. between parents), use '-'
followed by '+' in the CMD column:02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 15/21

_Dimension Name_Child name_Child Alias_Parent Name_Operator_Cmd
Products Widget 2.0 Widgets + -
Products Widget 2.0 New Widgets + +
The ETL tool always processes additions to the hierarchy before deletions, regardless of the
order in which they appear in the .csv file. Placing the '-' command before the '+' command
marks the first member for deletion, then "moves" it when it is added back.
If both the '+' and '-' commands are used in the same .csv file, no intersection data will be lost
and all Member IDs will remain unchanged.
This method works with both bottom-level and parent members.
You may also reverse the order for bottom-level members:
_Dimension Name_Child name_Child Alias_Parent Name_Operator_Cmd
Products Widget 2.0 New Widgets + +02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 16/21

Products Widget 2.0 Widgets + -
This creates a temporary "shared" member in the location to which the member will
eventually be moved, then deletes the original member.
If you run the '+' command and the '-' command in this way in separate .csv files the result
will be identical to running them together in the same .csv file. However, if run separately, the
"shared" member will be visible in the hierarchy until deleted by running the second .csv file
through the ETL tool.
Hierarchy Before Hierarchy After
All Products
Widget
Widget 2.0
Widgets
New Widgets
Widget XLAll Products
Widget
Widgets
New Widgets
Widget XL
Widget 2.0
VI. Add parents and children simultaneously02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 17/21

To add multiple parents and any children at the same time, use '+' in the CMD column multiple
times in order. This is useful when creating the initial hierarchy where none exists yet.
_Dimension
Name_Child
name_Child Alias _Parent
Name_Operator_Cmd
Products All Products + +
Products All Widgets All Products + +
Products Widget Regular
WidgetAll Widgets + +
Products WidgetXLSpecial WidgetAll Widgets + +
All parents must appear in the table before their children are listed.
Members at the root (highest) level of the hierarchy - both parent and bottom-level
members, have no entry in the parent name column.
Hierarchy Before Hierarchy After
[Empty Hierarchy] All Products
Widget (Regular Widget)
WidgetXL (Special Widget)02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 18/21

All Widgets
Best practices
If you would like to delete members using ETL, it is recommended that you instead move
them to a special Members to be Deleted parent and then delete them manually (in the
Modeler section), rather than allow the final deletion to be performed by the ETL tool. This
helps to ensure that no members are deleted accidentally.
When moving bottom-level members between parents, it is acceptable to use the '+'
command before the '-' command to create a temporary shared member, which allows the
move to be performed across separate .csv files.
If you would like to move a parent member and all of its children (including all associated
intersection data and member IDs):
First, use the '-' command in one row referencing the original location.
Then, follow it with a '+' command row later in the same file indicating the new location.
This is the reverse of the logic used for bottom-level members but is necessary because it
notifies the ETL tool that deletion will be pending. If the parent addition is entered above
the deletion in the table, the ETL Import will fail because of the server.
Was this article helpful?
20 out of 23 found this helpful02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 19/21

Related articles
How-To: Building Alternate Hierarchies
How-To: Exporting CSV Files for ETL Job
Reference: ETL Guide - 2 - Vena.io ETL
How-To: Setting up Page Options for the
Choose Box
How-To: Set Up a Business Central Connector
and Data FeedRecently viewed articles
How-To: Exporting Data From a SQL Staging
Table
Reference: ETL Guide - 6- Using Staging Data
Reference: ETL Guide - 5 - SQL Staging
Environment
Reference: ETL Guide - 4 - Query Languages
Reference: ETL Guide - 3 - Command Line ETL
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 20/21

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 16:44 How-To: Create and Manage a Data Model Hierarchy Using ETL Import – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115000712323-How-To-Create-and-Manage-a-Data-Model-Hierarchy-Using-ETL-Import 21/21
