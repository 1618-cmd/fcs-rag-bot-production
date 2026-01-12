# (How To)   Bulk Updating Dimension or Hierarchy Member Names

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
Member Name CharactersHow-To: Bulk Updating Dimension or
Hierarchy Member Names
You may have a business change or requirement that requires bulk updates of
dimension or hierarchy member names.

Olalekan Adebayo
Updated 7 months ago
02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 1/10

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
Members?Why use this feature?
Some business changes or updates may require you to update your current dimension member
names to a different format. This feature allows you to make these updates in bulk instead of
updating them one by one.
Before you begin
To follow the instructions in this article, you will need at least Modeler access.
How to
1. Navigate to the Modeler tab.
2. Select Data Modeler in the sidebar.
3. Select Export from the sidebar tab.
4. Under Choose what you would like to export:, select Hierarchy.
5. Under Export if following condition is true, you can use an MQL or HQL query to specify only
the part of the hierarchy you are interested in. If this is blank, then the entire hierarchy will
be exported.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 2/10

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
See all 21 articles
6. Select Advanced Options to refine your export.
7. Under Where would you like to export to?, select File.
8. Under File format, select CSV.
9. Check the boxes next to Include column headers in export? and Include member IDs in export?.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 3/10

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
Product Updates10. Save the Advanced Options.
11. Open the file in Excel or Notepad.
If opening with Excel, it’s important to note that it will try to rename the member IDs.
However, member IDs must stay the same. Because of this, follow these steps to ensure the
member IDs remain the same in Excel (see this article for more details on maintaining
dimension member IDs):
1. Open the exported CSV file in Notepad or Notepad++.
2. Open a blank Excel window and highlight the 7th column which is the _member_id
column.
3. Right-click the highlighted column and select Format cells.
4. Change the format to Text. This ensures that Excel does not try to change the format or
values when we paste the exported hierarchy file.
5. Return to the Notepad file and copy the contents.
6. Then return to the blank Excel file and select cell A1 and paste. If Excel places all of the
data in just column A, use the Text to Column feature from the Data tab in Excel.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 4/10

7. Select Delimited, and then select Next.
8. Check the box next to the Comma, and then select Next.
9. Select all the columns or just the 7th column (_member_id) and select text as the column
data format.
10. Select Finish.
12. Make the desired changes and save the file. Save as CSV if you used a blank Excel file and re-
import the CSV file with a hierarchy load. You can use an existing load hierarchy ETL job or
create one if it doesn't exist.
13.  To import:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab.
4. Select an existing Load Hierarchy job and select the play button.
5. If a Load Hierarchy job doesn’t exist, create one:
1. Select + Create Template
2. Enter "Load Hierarchy" as the name.
3. Select Add Step.
4. Select File to Cube.
5. Select Hierarchy in the Data Type drop-down
6. Select Add.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 5/10

7. Select Save and then select the Play button.
6. The ETL Template Execution window opens. Drag and drop the CSV file or select browse
files and select the CSV file from your computer.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 6/10

7. Select Run.
02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 7/10

8. During the import, the system checks for the Member ID and if it exists, the new name will
be used instead of creating a new member.
9. Once completed, check your hierarchy and confirm everything looks good.
Was this article helpful?
0 out of 1 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)Recently viewed articles
How-To: Restoring a Dimension Member That
Was Mistakenly Deleted
Note
This will also automatically update your templates with the updated member
names since the system references the names using the unique member IDs.02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 8/10

How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
How-To: Building Alternate Hierarchies
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
How-To: Enabling Line Item Details (LIDs) in a
Template or ReportHow-To: Combining Dimensions Using
Multiple Expressions for Slices to Clear
Explainer: What Is the Maximum Number of
Dimension Members and Member Name
Characters
How-To: Assigning Dimension Types and
Standard Members
Reference: Modeler Experience
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:05 How-To: Bulk Updating Dimension or Hierarchy Member Names – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15550666629133-How-To-Bulk-Updating-Dimension-or-Hierarchy-Member-Names 10/10
