# (How To)   Copy Data in Bulk and Save Versioning Configurations in Modeler

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Dimensions & Members Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
How-To: Assigning Dimension
Types and Standard Members
Explainer: What Is the
Maximum Number of
Dimension Members and
Member Name CharactersHow-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Bulk-copy data with the Versioning tool to quickly create new budgets or scenarios
from your existing data.
Why use this feature?
Laura Harris
Updated 4 months ago
02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 1/19

How-To: Combining
Dimensions Using Multiple
Expressions for Slices to Clear
How-To: Restoring a Dimension
Member That Was Mistakenly
Deleted
How-To: Bulk Updating
Dimension or Hierarchy
Member Names
How-To: Bulk Attach/Detach
Attributes and Filter by
Attributes
How-To: Search for Members,
Attributes, Aliases and GL
Codes With the Modeler Search
Explainer: What’s the Difference
Between an Alternate Hierarchy
and Calculated Members?
How-To: Copy Data in Bulk and
Save Versioning Configurations
in Modeler
Explainer: What Are Linked
Dimensions?
Explainer: What Are Unmapped
Dimensions and Default
Members?Versioning is a flexible tool that lets you copy data from one part of your data model to another.
It's especially useful for creating budgets--For example, by copying last year’s actuals or budgets
into the upcoming year’s budget to establish a baseline for contributors.
While budgeting is the most common use case, Versioning’s ability to copy large volumes of
intersection data also supports other scenarios, such as:
Modeling What-If scenarios by duplicating budget versions from a single template.
Clearing data by copying blank values into target intersections using the Clear Destination
Values option.
In this article, you’ll learn how to:
Use Versioning for basic data copying tasks.
Leverage advanced options for more complex scenarios.
Remove data from intersections using Versioning.
Before you begin
To complete the steps outlined in this article, you will need at least Modeler access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
Table of contents
How to02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 2/19

Reference: Creating a
Calculated Number That
Excludes a Member
Reference: Dynamic Member
Sets
How-To: Building a Custom
Roll-up Using Calculated
Members
Reference: Exporting
Hierarchies in Vena Using HQL
Reference: Naming Guidelines
for Dimension Members
How-To: Using Attribute
Aggregation
Reference: Export Intersections
and Line-Item Details
Troubleshooting: Error While
Processing the Model Slice
Expression When Previewing
Intersections
Troubleshooting: Versioning
Copy To and Copy From must
Contain the Same Set of
Dimensions
See all 21 articlesBasic Versioning
To Edit Saved Versioning Configurations
Advanced Versioning options
Copy Line-Item Details
Version Parent Members
Clear all destination intersection values before copying
Run Calcs
Remove data with Versioning
How to
Basic Versioning
Using the Versioning tool to copy a budget from one month or year to the next only takes a few
steps to complete.
To copy values from one set of Intersections to another:
1. Log in to Vena and navigate to the Modeler tab.
2. Select Data Modeler.02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 3/19

Managing Your Model
Functions
Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates3. Select the appropriate data model from the data model dropdown list at the top of the page.
4. Select the appropriate data model from the data model drop-down list at the top of the
page.02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 4/19

5. Input a name for your Versioning Configuration.
 Note
If you choose to run your Versioning configuration immediately, you do not have to
input a name. However, if you intend to save the configuration for a later date, you02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 5/19

6. Select the dimension that you want to copy.
7. Choose a member that describes the type of intersections you would like to bulk copy, then
hover over that member row. Three icons should appear:
Filter by
Copy From
Copy To
Select the
 (Filter by) button to add your member to the Filter Dimension by Members
section under Versioning Configuration.
must include a name.
 Note02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 6/19

8. Choose the member to copy from and select
(Copy From) in the Member row to add it to
the Copy From section. This is where you select the source of the data to be copied.
For example, if it were currently 2020 and you wanted to copy your 2020 budget to 2021, you
would choose the Y2020(or similar) member here. If you leave this section blank, Vena will
copy all data for all dimensions in the data model.
9. Now, choose the member that you would like to copy to and select the
(Copy To) button
to add it to the Copy To section. This is where you select the destination of the copied data.
For example, if you wanted to copy your 2020 budget to 2021, you would choose the Y2021
(or similar) member here.
You can add more than one member from unique dimensions. For example, during
a cycle rollover, if you want to version last year's December Actuals to January
Budget, Copy from: 2020 (Year), Actuals (Scenario), December (Month). Copy to:
2021 (Year), Budget (Scenario), January (Month)
02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 7/19

10. For basic Versioning, do not change the options from their default settings (see a screenshot
of default settings, below):
By leaving the default settings unchanged, this means you answer "No" to the following
questions:
- Do you want to clear all destination intersection values before copying? No
- Do you want to copy line items? No
- Do you want to run calls? No
- Do you want to version parent members? No
SeeAdvanced Versioning Optionsbelow for more information on these functions
11. Select Runto start the Versioning job, which will copy the specified values. You can also
select Saveto save your configuration without running it.
 Note
The member you choose for Copy To and Copy From must be the same
dimensions.02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 8/19

12. If you select the Run button, Vena will create and process a new Versioning job, and display a
message confirming that your Versioning job has started.
13. Versioning jobs appear with ETL jobs in the History section of the Modeler interface, where
you can see their status.
To review Versioning job status:
1. Select Data Modeler.
2. Select Historyfrom the sidebar.
3. Your job should be visible on the ETL Jobs page.
4. In the table, you'll see Versioning jobs with Versioning in the Job Name column, along with an
outline of the configured job.
5. You can check the job status using the indicators on the right side.
The time required to complete a Versioning job depends on the number of intersections being
copied and written. For large jobs, processing may take a while, so Versioning runs in the
background.
While the job is processing:
The data model remains unlocked.
All users can continue working in Vena without interruption.
To Edit Saved Versioning Configurations:
You can save and edit versioning parameters. For example, if you create a configuration to
version forecasts over each month, you can edit an existing versioning configuration instead of
making multiple new ones.
If the last Saved Versioning Configuration has the following parameters:
Filter: Forecast, Total Expenses account, 202102/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 9/19

Copy From: 01-Jan
Copy To: 02-Feb
Rather than creating a new Versioning Configuration in the next month to copy from 02-Feb to
03-Mar, you can edit the existing Versioning Configuration above and modify the Copy From and
Copy To members, without having to redo filters from scratch.
1. Navigate to the Modeler tab.
2. Select Data Modeler.
3. Select Versioning from the sidebar.
4. Ensure the data model that is selected contains the Saved Versioning Configuration you
want to edit.
5. Select the Saved Versioning Configuration from the dropdown menu that you want to edit.
02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 10/19

6. Make changes to the Description, Filter, Copy From, Copy To, Copy Line-ItemDetails, Clear
destination values & Run Calcs checkboxes that you want.
7. A modal will appear asking you to confirm overwriting the saved configuration. Select Yes,
Overwrite.
Advanced Versioning options
Four advanced options are available to modify how the Versioning job is run. You can use these
options to change how the tool performs certain details of the data copy.
Note
Changing the name will create an entirely new saved versioning configuration.02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 11/19

Copy Line-Item Details
This option allows you to specify whether Versioning should clear out values in the destination
member(s) before copying.
No Line-Item Details
If set toNo Line-Item Details (default selection): Versioning will only overwrite intersections
where there is incoming data, (i.e. where a value is actually being copied over), and will do
nothing with intersections where the destination has a value but the source value is blank
(null).
The option to Version Parent Members is not available if you select No Line-Item Details.
Link to originals
If set to Link to originals,  Versioning will clear out all values in the destination intersections
first, then copy the values over from the source.
The option to Version Parent Members becomes available when you select Link to originals.02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 12/19

Make separate copies
Allows you to choose whether line items are copied; and if yes, in which format.
If set toNo Line-Item Details (default selection): Only regular values will be copied; Line-Item
Details will be omitted.
If set toLink to originals: Both regular values and Line-Item Details will be copied to the
destination; Line-Item Details in the destination will have the same unique Row IDs as in the
source.
Selecting this option is useful if there are Line-Item Details in your source data and you
intend to compare the source and destination on a variance report.
Due to the shared Row IDs, deleting any Line-Item Detailanywherein your data model will
also delete every other Line-Item Detail with the same Row ID (i.e. any that were copied
using Versioning with theData and Line Itemsoption selected).
If set toYes, make separate copies: Both regular values and Line-Item Details will be copied to
the destination; Line-Item Details in the destination will receive their own unique Row IDs,02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 13/19

distinct from those in the source.
If there are Line-Item Details in your source data and you do not need to compare data at
a Line-Item Detail level on variance reports, the recommended option isData and Line
Item Rollover
The option to Version Parent Members becomes available when you select Make separate
copies.
The graphic below illustrates the results of using either the Link to originals(Data and Line Items)
or theMake separate copies(Data and Line Items Rollover) options on the same data:
02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 14/19

Version Parent Members
This option allows you to choose whether parent members will be included or not when
defining what to copy.
Because values can't be stored at a parent-level intersection, this option is used to version
Line-Item Details associated with parent members, so it works in conjunction with theCopy
line items?  drop-down list.
If the box is left unchecked(default selection): When you add a parent member to
thePage(s)section, only the Bottom Level of members under the selected parent will be
included. If you do not choose any members for a dimension, all Bottom Level members of
that dimension will be included.
If the box is checked: When you add a parent member to thePage(s)section, all of its
descendants (the selected parent member's children and their children, etc.)and the parent
member itself(along with its Line-Item Details) will be included. If you do not choose any
members for a dimension,all membersof that dimension will be included, not just those at
the Bottom Level.
Clear all destination intersection values before copying02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 15/19

This option allows you to specify whether Versioning should clear out values in the
destination member(s) before copying.
If set toNo(default selection): Versioning will only overwrite intersections where there is
incoming data, (i.e. where a value is actually being copied over), and will do nothing with
intersections where the destination has a value but the source value is blank (null).
If set toYes: Versioning will clear out all values in the destination intersections first, then copy
the values over from the source.
The graphic below illustrates the results of turningClear Destination Valueson or off using the
same data:
02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 16/19

Run Calcs
If you have any Vena Calcs set up that include the destination intersections in their scope,
this option allows you to specify whether or not those Calcs are executed when the data copy
is performed.
Remove data with Versioning
While its primary purpose is to populate intersections by copying data into them, Versioning can
also be used as a way ofremovingdata from intersections. It does this by copying a blank set of
values onto the intersections to be cleared out, while also leveraging theClear Destination
Valuesoption.
When you run the Versioning job,Clear Destination Values deletes the existing values in the target
intersections, and then "overwrites" them with the blank values from the source intersections,
effectively clearing out the target.
Steps to Clear Data
1. Follow the steps above to navigate to Modeler > Versioning.
2. Create a blank member (e.g., Remove Data) under the Scenario dimension or another
appropriate dimension:
In the Dimensions panel, select the dimension.
In Dimension Members, right-click the desired parent and choose Add Child.
3. Define the intersections to clear:02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 17/19

In the Page(s) section under Versioning Parameters, add the members that define the
intersections to be cleared.
If you omit a dimension, all members from that dimension will be included.
4. Set up the copy parameters:
In Copy From, select the Remove Data member.
In Copy To, select the destination member whose intersections you want to clear.
5. Configure options:
SetClear all destination intersection values before copying?toYes.
SetCopy Line-Item DetailstoNo Line-Item Details(orLink to originalsif line items
need to be removed).
6. Select Runto clear the specified intersections.
Was this article helpful?
1 out of 2 found this helpful
Related articles
How-To: Data Model Series (Part 3): Attributes
and Versioning
Reference: Writing Expressions (MQL & HQL)
How-To: Using Vena's Mapping SummaryRecently viewed articles
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Search for Members, Attributes,
Aliases and GL Codes With the Modeler
Search02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 18/19

How-To: Using Expand and Collapse with
Multi-Dynamic Row Mappings
How-To: Setting up a Staging Query (Vena 365
Only)How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
How-To: Bulk Updating Dimension or
Hierarchy Member Names
How-To: Restoring a Dimension Member That
Was Mistakenly Deleted
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:08 How-To: Copy Data in Bulk and Save Versioning Configurations in Modeler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059076331-How-To-Copy-Data-in-Bulk-and-Save-Versioning-Configurations-in-Modeler 19/19
