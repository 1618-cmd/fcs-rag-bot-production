# (How To)   Data Model Series (Part 2)  Hierarchies and Roll Ups

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Managing Your Model Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
Managing Your Model
Explainer: What is Data Model
Standardization?
How-To: Build Your Chart of
Accounts Hierarchy in Quick
StartHow-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
About this series
This series is all about how to build and use Data Models. You are in Part 2, which provides step-by-step
instructions on how to build and manage a Dimension.
This series was designed to be read in order. If you don't have any previous experience with the Data
Model tool, we recommend that you follow this approach, starting with Part 1. But if you are already
familiar with Vena Data Models and are just looking for a refresher, you can also feel free to dip in
anywhere within this series.
Vena Support Team
Updated 6 months ago
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 1/19

How-To: Formatting an Excel-
Based CSV to Maintain Leading
Zeros for ETL Jobs
How-To: Data Model Series
(Part 1): Creating a Data Model
How-To: Data Model Series
(Part 2): Hierarchies and Roll-
Ups
How-To: Data Model Series
(Part 3): Attributes and
Versioning
How-To: Data Model Series
(Part 4): ETL Tool
How-To: Build and Manage
Data Models in Modeler
How-To: Building Alternate
Hierarchies
How-To: Adjusting How Vena
Treats Zero Values in the
Database
How-To: Creating a Testing
Environment by Cloning a Data
Model (Clone & Remap)
How-To: Undo a Versioning ETL
Job Without Line-Item Details
How-To: Undoing a Versioning
ETL job with Line-Item DetailsPart 1: Building a Data Model
Part 2:  Hierarchies and Roll-ups -you are here
Part 3:  Attributes and Versioning
Part 4:  ETL Tool
Before you begin
To follow the instructions in this article, you will need at least Modeler access. If Data Permissions are set
up in your environment, you will also need the appropriate permissions for the data that you are working
with.
Table of contents
Overview
Hierarchies and roll-ups
Dimension/Dimension Member tools
How to
Add a Dimension
Edit a Dimension Name
Delete a Dimension
Create a Dimension Member
Rename a Dimension Member
Add a Dimension Member Alias
Cut/Paste a Dimension Member
Share a Dimension Member02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 2/19

(LIDs)
How-To: Downloading All Vena
Data From Your Tenant or
Environment
Troubleshooting: The Bulk Copy
Parameters Were Invalid
Troubleshooting: This Member
Does Not Exist Error During
Modeler Search
Troubleshooting: ETL Error –
Cannot Increase the Number of
Members Beyond 400000
Troubleshooting: Encountered
More Than the Limit of 1000
Unmapped Members
Functions
Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena InsightsDelete a Dimension Member
Overview
Hierarchies and Roll-Ups
The dimensions of an OLAP cube are structured into hierarchies. For example, in a database that tracks
information for periods, hierarchies may be broken down into:
All Period (Complete year)
Halves
Quarters
Months
An example of a hierarchy. (Displaying dimensions and dimension members.)
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 3/19

Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
ADimensions Display all dimensions created within a data model.
BDimension MembersDimension member hierarchy.
CRoll-up Lower-level members (child members) will "roll-up" under this umbrella.
DBottom Level MemberLower-level dimension member which fits under the parent umbrella
dimension members.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 4/19

Dimension/Dimension Member tools
Leverage the available tools on the Members page to build your hierarchy.
AChoose Data ModelSelect the drop-down menu, and then select from the available data
models.
BDimensions A list of dimensions of the selected data model.
CDimension MemberSelected dimension member.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 5/19

DOperator Aggregation method used for roll-up dimension member:
 (~) No Aggregation
 (+) Add
 (-) Subtract
EEdit Allows you to rename the member, add/edit an alias, add/edit attributes
and add/edit an operator.
FSibling Member Create a new sibling of the selected member.
GChild Member Create a new child (subordinate) member of the selected member.
HPreview IntersectionsPreview all data intersections for selected member with the option to
export to a CSV file.
IExpand All Display all levels of the hierarchy.
JCut  Cut the selected member.
KAdd Calculated
MemberAdd a calculated member to this dimension member.
Learn more about Calculated Members.
LSort Children by NameOption to sort children alphabetically by name.
MSort Children by AliasOption to sort children alphabetically by alias.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 6/19

NPin as Default MemberAllows you to manually select a specific member as the Default Member.
Learn more about Default Members.
ODelete Allows you to delete a dimension member.
How to
Add a Dimension
1. Navigate to the Modelertab. The Data Modeler window should open automatically.
2. Select the data model that you want to add the dimension to (Reporting, in this example).
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 7/19

Or, if you are in the Members section, choose your data model from the drop-down menu:
3. Select the pencil icon (
) at the end of the Dimensions list.
4. Select + Add Dimension.
5. Enter a name for the new Dimension in the textbox.
6. Select +Add Dimension to save the dimension.
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 8/19

Edit a Dimension name
Editing a dimension name after it has been created will impact existing data records but will not impact
(break) reports that display the data from a specific data model.
1. Navigate to the Modeler tab.
2. Select the Data Modeler sidebar.
Note_Icon_Small.png Note
Be aware that if you add a new Dimension, any previously mapped templates will have to be
updated to map the new Dimension.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 9/19

3. Select the
(pencil) icon at the end of all the dimension names. This opens the drawer showing
existing dimensions in the model.
4. Hover over the dimension you want to rename and select the
  (pencil) icon.
5. Type in the new dimension name and select + Update to save the change.
Delete a Dimension
It is rare that you would need to delete a dimension after setting up a data model. However, in the event
that you have made an error or need to re-order members, then you can delete a dimension by following
these steps.
1. Navigate to the Modeler tab.
2. Select the Data Modeler sidebar.
3. Select the
(pencil) icon at the end of all the dimension names. This opens the drawer showing
existing dimensions in the model.
4. Hover over the dimension you want to delete and select the
(trash) icon.
5. Select Yes, Delete Dimension in the confirmation pop-up to delete the dimension.
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 10/19

Create a Member
1. Navigate to the Modeler tab.
2. Navigate to the Data Modeler page.
3. Navigate to the Members sidebar tab.
4. Select the data model from the drop-down menu.
5. Select the targeted dimension.
6. Right-click a dimension member.
7. Select either Add Sibling orAdd Child as your new member.
Caution_Icon_Small.png Caution
Be aware that if you delete a dimension, all dependent mappings will lose access to related
members and data.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 11/19

AAvailable
Dimension
MembersSibling - Sibling members are members on the same hierarchical level
under the same parent member.
Child - A Childmember is a sub-member (descendant) of a
Parent/Sibling member.
B
AliasAn alternative description used to reference a Dimension Member.
C
OperatorAggregation method used for Dimension Members.
 (~) No Aggregation
 (+) Add
 (-) Subtract
Rename a Member
Like dimensions, editing a member name after it has been created will impact existing data records but will
not impact (break) reports that display the data from a specific data model.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 12/19

1. Locate the member you want to rename from the member list.
2. Hover over the member and select the
 (pencil) icon.
3. Rename your member.
4. Select + Update to save the change.
Add a Dimension Member Alias
An Alias is an alternative descriptive handle used to reference the dimension member. An alias can be
referenced when applying data mappings. It is useful as dimension members can have long or complex
names, and aliases provide the ability to use alternate names.
1. Locate the member you want to add an alias for.
2. Hover over the member and select the
 (pencil) icon.
3. Add a name under the Alias textbox.
4. Select + Update to save the change.
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 13/19

Cut/Paste a Dimension Member
Re-ordering dimension members often occurs as a result of organizational changes, such as the reduction
or reallocation or cost centers. In this event, easily move a dimension member to a different location by
following these steps.
1. Select the appropriatedata model.
2. Right-click anywhere in line with the dimension member you wish to modify.
3. Select cut.
4. Navigate to the dimension member location you wish to paste.
5. Right-click the dimension and select Paste.
02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 14/19

6. This will deposit the member in the new position in the hierarchy. Select Cancel if you no longer wish to
move the member.
Share a Dimension Member
The Shared Members functionality allows Modelers to create alternate hierarchies within a dimension.
Shared members make aggregated reporting of collected data  in a number of ways possible. For example,
within the Period dimension, Month members can be shared to allow for the aggregation of quarter-to-
date and year-to-date values. To share a dimension, follow these steps:
1. Select the data model.
2. Select the dimension from the Member Name list you wish to share.
3. Right-click the dimension member from the Member Name list.
4. Select the Shar e button. A pop-up window notifies you that the member can now be shared.
5. Navigate to, then right-click on the destination umbrella dimension member you wish to share with.
Right-click on the member and select Complete Share button. Select Cancel if you no longer wish to02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 15/19

share the member.
6. The shared member will appear in the hierarchy with a Share symbol next to it.
Delete a Dimension Member
In order to preserve historical reporting, any member with data attached to it should not be deleted.
Deleting a member will also delete all associated data. It should be noted that unused members may be
excluded from a report without being deleted.
1. Navigate to the desired data model.
2. Right-click the dimension member from the Member Name list that you want to delete.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 16/19

3. Select Delete.
4. If you are sure you want to delete the member, select Delete in the confirmation pop-up window.
Related Topics
To learn how to clone and view a data model: How-To: Creating a Testing Environment by Cloning a
Data Model (Clone & Remap).
To learn about how to export a subset of a data model: How-To: Exporting Subset of Data From Your
Data Model or Cube.
To learn how to create and manage a data model hierarchy using ETL Import: How-To: Create and
Manage a Data Model Hierarchy Using ETL Import.02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 17/19

To learn how to map from multiple data models to a single template: How-To: Mapping Data From
Multiple Data Models on a Single Template.
To learn about how to link dimensions:  Explainer: What Are Linked Dimensions?
To learn about how to create a custom roll-up without creating alternate hierarchies: How-To:
Building a Custom Roll-up Using Calculated Members.
Was this article helpful?
2 out of 3 found this helpful
Related articles
How-To: Data Model Series (Part 3): Attributes and
Versioning
How-To: Data Model Series (Part 1): Creating a Data
Model
How-To: Exporting CSV Files for ETL Job
How-To: Building Alternate Hierarchies
How-To: Data Model Series (Part 4): ETL ToolRecently viewed articles
How-To: Creating a Testing Environment by Cloning
a Data Model (Clone & Remap)
How-To: Data Model Series (Part 1): Creating a Data
Model
How-To: Formatting an Excel-Based CSV to
Maintain Leading Zeros for ETL Jobs
How-To: Build Your Chart of Accounts Hierarchy in
Quick Start
Explainer: What is Data Model Standardization?02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 18/19

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:15 How-To: Data Model Series (Part 2): Hierarchies and Roll-Ups – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039163832-How-To-Data-Model-Series-Part-2-Hierarchies-and-Roll-Ups 19/19
