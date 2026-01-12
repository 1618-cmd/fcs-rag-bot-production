# (How To)   Adjusting How Vena Treats Zero Values in the Database

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
StartHow-To: Adjusting How Vena Treats Zero
Values in the Database
In most databases, blanks and zeros are functionally identical, and Vena treats them as
equivalent for performance reasons. But in some specific cases, it's important to make a
distinction between a zero value and a blank value.
Why use this feature?
Vena Support Team
Updated 6 months ago
02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 1/11

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
ETL job with Line-Item DetailsIn most databases, blank intersections and zero values are treated the same way. Removing zeros and
leaving intersections blank typically has no practical impact.
However, Vena processes zeros like any other data, while blank intersections are ignored. Replacing zeros
with blanks can improve template performance by reducing template load times, so Vena replaces zeros with
blanks by default.
In some industries, especially those with regulatory requirements (e.g., CCAR), it is essential to retain zero
values. In such cases, you may need to adjust how Vena handles zero values to ensure they remain intact.
This guide explains how to configure your data model to modify Vena's treatment of zeros and how to
replace existing zeros with blanks if needed.
Before you begin
In order to complete the steps described in this article, you will require at least Modeler access. You will also
need the necessary Application Permissions to read and update the data model you will be working with.
How to
Basic Functionality
You can turn ON/OFF the feature that retains zeros in your data model. By default, it is OFF, meaning zeros
are saved as blanks. If turned ON, Vena will keep zeros and not replace them with blanks. This setting applies
to the entire data model but only affects new data inputs after the change.
Note02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 2/11

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
Vena Insights
Vena for MicrosoftTo change how Vena handles zero values:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select Settings from the sidebar tab.
4. Select the toggle next to Retain zeros for this model:
ON will save any zero input into the database as a value.
OFF will discard any zero input into the database and keep that intersection blank.
5. Any changes you make take effect immediately; there is no need to save.
Advanced functionality
Add Slice
Changing this setting affects only standalone zero values which are exactly zero. It will not affect
any values that greater or lesser than zero (e.g., 0.1, etc.), nor will it remove zeros from values
containing them (e.g., 10.05 will not become 1.5).02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 3/11

PowerPoint
Vena Copilot
Product UpdatesFor more specific control, use the Add Slice feature to retain zeros in select parts of the data model. This
feature works only to retain zeros for specified slices, not to discard them selectively.
With Add Slice, you can target single members, multiple members or dynamic groups (e.g., bottom-level,
IDescendants). If you leave any dimensions unconfigured, Vena treats them as if all members in those
dimensions are selected (e.g., IDescendants).
To only retain zeros for specific parts of the Data Model:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select Settings from the sidebar tab.
4. Ensure that Retain zeros for this model is set to ON.
Caution
Zeros will only be retained for the configured slices if the ON/OFF toggle is set to ON. If the ON/OFF
toggle is in the OFF position, zeros will not be retained for any slices listed under Retain zeros for
these slices of the model.02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 4/11

5. Select +Add Slice to open the Add/Edit Restrictions drawer.
6. Use the Select Dimension drop-down menu to choose the dimension to define your slice.
7. In the Members section, navigate to the member you would like to use to define the slice. Right-click on
the member to see selection options.02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 5/11

8. Select the option that describes the slice (or part of the slice) you want. The corresponding members will
be added to the Restrictions section. This is a preview string of all configured restrictions in the green-
colored panel below.
02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 6/11

To make changes to the restrictions you've configured so far, select the trash can icon next to the item
you'd like to remove in the Restrictions section.
9. Select Save Changes once you have finished configuring the slice.
10. You will return to the main Settings screen, where your configured slice is added under Retain zeros for
these slices of the model. To modify or remove an existing slice, select the slice under Retain zeros for this
model, select either the Edit or Delete button.
Delete Existing Zeros
As noted above, modifying the Retain zeros for this model setting only affects zeros that are entered into the
database going forward, after the change is made. If you already have zeros in your database (either because
they were input manually or from ETL loads) and you would like to replace them with nulls/blanks to improve
performance, you can do this with the Delete Existing Zeros function.
This finds and removes all existing zeros from your database upon activation. How this works depends on
how you have configured the Retain zeros for this model setting:
Retain Zeros Setting Data Model Slices Delete Existing Zeros Behavior
OFF No Clears all zeros from entire database
ON No Will not clear any zeros
ON or OFF Yes Clears all zeros except from the slices
To delete any existing zero values from your database and replace them with blanks:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 7/11

3. Select Settings from the sidebar tab.
4. Verify your Retain zeros for this model setting and whether you have configured any slices to determine
what will happen when you use Delete Existing Zeros (refer to the table above).
5. Select Delete existing zeros.
6. This opens a warning pop-up. Select Yes to confirm that you would like to delete zeros.
7. A confirmation lets you know that a delete zeros job was scheduled and added to your ETL jobs queue.
You can check on the progress of this job by selecting History in the Modeler sidebar menu.02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 8/11

8. Once the ETL job finishes, all zeros will be removed from your database and replaced with blanks.
Blank empty rollups for this model
When enabled, the Blank Empty Rollups setting changes how Vena handles parent-level rollups if child
intersections are blank or contain non-numeric values (e.g., text). If ON, parent rollups without numerical
data at the child level appear as blanks. If OFF, they display as zeros.
02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 9/11

Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
5 out of 5 found this helpful
Related articles
Troubleshooting: Unable To Save or Show Zero (0)
Value on a TemplateRecently viewed articles
How-To: Building Alternate Hierarchies
How-To: Build and Manage Data Models in Modeler
Caution
This is a compatibility setting for users migrating to Vena Cloud from Vena OnSite. If you are not
migrating from Vena OnSite, we strongly recommend that you do not change this setting.
02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 10/11

Reference: Writing Expressions (MQL & HQL)
How-To: Setting up Data Validation Rules
Reference: Vena Calcs - 1 - Managing Scripts
Troubleshooting: Common Template Automation
ProblemsHow-To: Data Model Series (Part 4): ETL Tool
How-To: Data Model Series (Part 3): Attributes and
Versioning
How-To: Data Model Series (Part 2): Hierarchies and
Roll-Ups
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:18 How-To: Adjusting How Vena Treats Zero Values in the Database – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207427413-How-To-Adjusting-How-Vena-Treats-Zero-Values-in-the-Database 11/11
