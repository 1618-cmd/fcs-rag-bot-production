# (How To)   Restoring Data That Has Been Accidentally Overwritten or Deleted

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration Search
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
ETL JobsHow-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
About this feature
If you accidentally delete or overwrite data, don’t panic. Vena saves all historical data written to
the database, allowing you to restore it easily. This process relies on Vena's Drill Saves
Jan Griffiths
Updated 4 months ago
05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 1/11

Data Querying
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
– External Sources – Data Feedsfunctionality, which automatically keeps a full history of all values written to an intersection.
As using Drill Saves for every intersection would be tedious, use the ETL tool for efficient
restoration across multiple intersections. Export historical intersection and Line-Item Detail data
for any selected date and time (in five-minute increments), then import the data back into Vena.
This restores all affected values to their state at the chosen timestamp, undoing deletions or
overwrites.
Before you begin
To restore data using this method, you need Modeler access and appropriate Data Permissions
if they are configured in your environment.
This process restores deleted intersection values but does not revert an entire template to a
specific snapshot. For example, assume you have a blank input template:
On Monday, you complete rows 1-10 and save.
On Tuesday, you complete rows 11-20 and save.
Then, you realize you accidentally deleted parts of rows 1-10, and want to restore them.
To restore Monday's missing values while keeping Tuesday's data intact, this method works.
However, if you wish to discard Tuesday’s data entirely and revert the template to only Monday’s
state, this method cannot achieve that. It restores values saved previously without removing
later additions.
How to
The first step you must complete is to export historical data for the date/time you want to
restore.05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 2/11

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
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesTo export historical data:
1. Log in to Vena.
2. Navigate to theModelertab.
3. Select Data Modeler from the sidebar.
4. Select Export from the sidebar tab.
5. In the dropdown menu under Choose what you would like to export, select either Values or
Line Item-Details, depending on the type of data you want to restore (you can also repeat
these steps to export both types).05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 3/11

6. Toggle Manual Query to ON.
7. Under Export if following condition is true, type in parameters in HQL format to filter the data
you would like to export.For more information, visit the ETL User Guide. This will narrow the
export down to only the values you want to restore, reducing the file size and time needed to
export and import. 05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 4/11

8. Select Advanced Options and check the box next to Export data from a date and time in the
past?
9. Choose the exact date and time (to the nearest 5 minutes) that you would like to export (i.e.,
restore to).
05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 5/11

10. In the options under Export to, select File and then select CSV under File format.
11. Select Save and then select Export to begin the data export and the download of your CSV
file.
12. Save the CSV file to a location you can find easily.
You are now ready to import the historical data and complete the Restore step.
To import (restore) the historical data:05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 6/11

1. Log in to Vena.
2. Navigate to the Modeler tab.
3. Select Data Modeler from the sidebar.
4. Select ETL Templates from the sidebar tab.
5. Select +Create Template.
This opens theETL Template Manager drawer.
6. Enter a name for the template.
7. In the Add Step drop-down menu, choose File To Cube.
8. In the Data Type drop-down menu, choose Values or Line-Item Details.
9. Select Add to save the step and add it to the list of steps. 05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 7/11

10. Select Save to save the template
11. The new template appears in the ETL Templates list on the left side of the ETL page. Select
the play button to run the template.
This opens the ETL Template Execution pop-up.05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 8/11

12. Ensure the File format is set to CSV, then drag and drop your file or selectbrowse files.
13. Select the CSV file you downloaded earlier after completing the historical data export.
14. For Acceptable invalid lines, select a value of your choice (lower values will have less
tolerance for errors; a selection of 0 should generally work for this type of import).
15. Select Run to begin the import job which will transfer the data from the CSV file into your
data cube, restoring the values to the selected date and time.
16. When your ETL Import job is complete (navigate to the Jobs section under the ETL tab), you
can check that your data was restored by opening an appropriate template.
After you have completed both the Export and Import steps described above, your deleted or
overwritten data is restored.05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 9/11

Was this article helpful?
3 out of 5 found this helpful
Related articles
How-To: Exporting CSV Files for ETL Job
Troubleshooting: Microsoft 365 Has Been
Configured to Prevent Individual Acquisition
and Execution of Office Store Add-ins
Explainer: Vena Flags
How-To: Granting Vena Support Access to
Your Tenant
Troubleshooting: Common Template
Automation ProblemsRecently viewed articles
How-to: Vena Integration: Part 6 – Channels &
Field Mappings
How-to: Vena Integration: Part 5 -
Destinations
How-to: Vena Integration: Part 4 – Import and
Export API
How-to: Vena Integration: Part 3 – External
Sources – Data Feeds & Connections
How-to: Vena Integration: Part 2 – Internal
Sources05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 13:03 How-To: Restoring Data That Has Been Accidentally Overwritten or Deleted – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/210732886-How-To-Restoring-Data-That-Has-Been-Accidentally-Overwritten-or-Deleted 11/11
