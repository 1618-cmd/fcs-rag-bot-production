# (How To)   Build and Manage Data Models in Modeler

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
Accounts Hierarchy in QuickHow-To: Build and Manage Data
Models in Modeler
Why use this feature?
This guide is intended to explain how to build a data model, how to maintain it, and some
helpful tools and tricks.
Laura Harris
Updated 1 year ago
02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 1/27

Start
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
Model (Clone & Remap)Table of contents
How to
Data Model: Build your data model
Add a data model
Dimensions: Structure your data model
Add dimensions
Members: Populate your hierarchy
Add members
Move members
Edit or delete members
Attributes: Create alternate views
Add attributes
Attach members to an attribute
Detach members from an attribute
Maintaining your data model
Revisions for audit tracking
Preview Intersections
Advanced member modeling
Shared members and alternate hierarchies
Calculated members
How to02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 2/27

How-To: Undo a Versioning ETL
Job Without Line-Item Details
How-To: Undoing a Versioning
ETL job with Line-Item Details
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
AdminData Model: Build your data model
Add a data model
1. Log into vena.io and select the Modeler tab.
2. Select +Add New Model.
3. Enter a Data Model Name and Description, and select +Add.
4. Your new data model will appear in the list of available models:
02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 3/27

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
Dimensions: Structure your data model
Add dimensions
1. Select the data model you just created.
2. Select the pencil (edit) button beside No Dimensions Available. (If you're adding dimensions
to an existing model, select the pencil icon at the end of the dimensions list.)
3. This opens a panel with options to add dimensions or link dimensions from existing models.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 4/27

4. Repeat steps 2-3 to add or link additional dimensions as needed.

Members: Populate your hierarchy
Add members
1. To add a member to your hierarchy, select the plus (+) icon on the member you would like to
add a child under. This opens the in-line edit panel.
2. You can add a Member Name, Alias, Attribute and/or define the Operator here.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 5/27

Move Members
1. To move a single member, select the grab icon to the left of the member and drag it to the
intended position.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 6/27

2. To move members in bulk, simply select the checkboxes beside the members you want to
move, then use the grab icon to move the members to their new position.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 7/27

Edit or delete Members
1. To edit or delete a member, right-click or select the vertical ellipsis in the member row. (If
you want to simply edit a member, you can also select the pencil (edit) icon in the member
row.)
2. Select Edit from the window to edit a member. To delete a member, select Delete at the
bottom of the window.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 8/27

3. If you select Edit, the inline panel opens. You can make changes to the Member Name, Alias,
Attached attributes, and operator from here.
4. After you've made your revisions, select Update to save the changes.
Attributes: Create alternative views
Add attributes02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 9/27

1. Select the Manage Attributes button. This opens the attributes drawer.
2. To add an attribute, select + Add Attribute. 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 10/27

3. Enter the attribute name and save it by selecting the + Add Attribute button below the
attribute field. You should see your new attribute in the sidebar.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 11/27

Attach members to an attribute
1. To attach members to an attribute, select the member by clicking on the pencil (edit) button
in the member row.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 12/27

2. Using the drop-down menu, select the checkbox next to the attribute(s) you want to attach to
your member.
3. Select + Update to save your changes.  Your new attribute will appear alongside its member.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 13/27

Detach members from an attribute
1. To detach members to an attribute, select the member by selecting the pencil (edit) button
in the member row.
02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 14/27

2. Using the drop-down menu, clear the checkbox next to the attribute(s) you want to remove
from your member.
3. Select + Update to save your changes.
Maintaining your data model
Revisions for audit tracking
1. To check what changes were made previously to a data model, select Revisions to open the
revisions window.
02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 15/27

2. Use the pagination and “go to page” to find the date of transactions you’re looking for. You
may copy/paste this table for your records.
Preview intersections
1. To preview intersections, right-click anywhere on a member row or use the vertical ellipses
to open the drop-down menu. 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 16/27

2. Select Preview Intersections.
3. This opens the Preview Intersections window.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 17/27

4. You can use the Export button to download the values in the window.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 18/27

Advanced member modeling
Shared members and alternate hierarchies
You may want to recall a roll-up that includes/excludes members from the main hierarchy.
Youcan do this by sharing members to another parent and mapping the new alternative parent
to the template later on. To share a member, perform the following steps:
1. Right-click anywhere on a member row or use the vertical ellipses (3 dots) to open the
dialogue box. 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 19/27

2. Select the Share Member option.
3. Select the parent member you would like to share under and select Complete Share to
share the member. 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 20/27

4. The member will now also appear under the parent member selected. There will be a shared
icon beside the shared member name. Deleting one position will not delete the others.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 21/27

Learn more about alternate hierarchies in this article.
Calculated members
Another way to recall a roll-up that includes/excludes a group of members or parents without
cluttering the hierarchy is to use a calculated member.
1. Right-click anywhere on a member row or use the ellipsis and select Add Calculated
Member from the drop-down menu. 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 22/27

2. In the in-line panel, name the calculated member and select Edit Expression to add MQL
expressions.
3. In this example, we want to add accounts 4000 (Product Sales) and 4020 (Subscription Sales).
Once you're finished, select Save to save your expression.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 23/27

4. Back in the in-line editor, select + Add Member to save the calculated member.
5. To edit the expression of a calculated member, right-click and select Open Expression Editor
from the menu.02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 24/27

Learn more about calculated members in this article.

Was this article helpful?
3 out of 4 found this helpful
Related articles Recently viewed articles02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 25/27

How-To: Building Alternate Hierarchies
How-To: Data Model Series (Part 1): Creating a
Data Model
Explainer: What is Data Model
Standardization?
Vena Insights Series (Part 2) - Building
Dashboards With Vena Insights
Reference: Auditability in VenaHow-To: Data Model Series (Part 4): ETL Tool
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
How-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)
How-To: Data Model Series (Part 1): Creating a
Data Model
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 26/27

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:16 How-To: Build and Manage Data Models in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360053389851-How-To-Build-and-Manage-Data-Models-in-Modeler 27/27
