# (How To)   Data Model Series (Part 1)  Creating a Data Model

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
Accounts Hierarchy in QuickHow-To: Data Model Series (Part 1):
Creating a Data Model
About this series
This series is all about how to create and use Data Models. You are in Part 1, which provides
step-by-step instructions on how to create and manage a data model.
Laura Harris
Updated 7 months ago
02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 1/19

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
Model (Clone & Remap)This series was designed to be read in order. If you don't have any previous experience with the
data model tool, we recommend that you follow this approach, starting with Part 1. But if you
are already familiar with Vena data models and are just looking for a refresher, you can also feel
free to dip in anywhere within this series.
Part 1: Creating a Data Model -you are here
Part 2: Hierarchies and Roll-ups
Part 3: Attributes and Versioning
Part 4: ETL Tool
What is a Data Model?
A data model is a multidimensional database that stores both numeric and narrative data. It can
be built using multiple dimensions, each with many members. An intersection of members from
each dimension comprises an individual data point.
OLAP cube example:02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 2/19

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
Admin
The data point in the top-right cell can be defined as the value for the total income, in Quarter 4, for
the Litigation Department. Each piece of data is found at the intersection point of all Dimensions.
Before you begin
To follow the instructions in this article, you will need at least Modeler access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 3/19

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
 User Permission Requirements
Users are required to possess the following permissions to perform data model-
related tasks such as creating, updating, or deleting dimensional hierarchies and
members. The same permissions functionality can also be applied to processes and
specific data sets. For more information, check out the Application Permissions Guide
and the Data Permissions Guide.
The Vena Admin is responsible for creating/assigning all of the above permissions.
Contents within a model include:
Dimensions of a model
Members of a dimension02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 4/19

Table of contents
How to
Create a Data Model
Rename a Data Model
Attach a Data Model to a Process
Export a Data Model
Clone a Data Model
Delete a Data Model
Notes & Limitations
Best Practices
Related Topics
Contents within a process include:
Tasks
Activities
Review Tasks
Task Details
Approve/Reject capabilities, etc.02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 5/19

How to
Create a Data Model
1.
Navigate to the  Modeler  tab.
2.
Select the Data Modeler  sidebar.
3.
Select + Add New Model .
4.
The Add Data Model drawer opens on the right side of the screen. Name the new data model,
then select Next: Configure Model Dimensions.  02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 6/19


5.
Configure the dimensions for the new model. Select +Add Dimension to add Standard
Dimensions or include custom dimensions. When you’re  finished, select Save Model.
02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 7/19

Rename a Data Model
Name changes will impact existing data records but will not impact (break) reports that display
the data from a specific data model.
1. Navigate to the Modeler tab.
2. Select the Data Modeler sidebar.
02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 8/19

3. Hover over the data model that you want to rename. Select the Edit (pencil).
4. Enter a new name in the text box.
5. Select + Update to save your changes.
Attach a Data Model to a Process
Attaching one or more data models to a process will:
Allow users with different data permissions to access different templates.
Pull data from multiple data models for a specific process.02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 9/19

Users in the Manager role can create templates/reports to write/read from different data
models.
To attach a data model to a process:
1. Navigate to the Manager tab.
2. Select the process you want to attach a data model to from the Processes table. This opens
the process workflow.
Note
If you run into an "invalid data model" error message when working with Ad Hoc
reporting, follow the steps below to ensure that your process is attached to the correct
data model.02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 10/19

3. On the Designer page, select the
(gear) icon in the upper right-hand corner.
4. Select Manage Models from the drop-down list.
5. Use the Attach New Model drop-down to select the data model that you want to attach to the
process.
02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 11/19

6. Select Attach to complete the action once you've selected the model.
Export a Data Model
In order to export/migrate data from one environment (tenant) to another in Vena, you have two
options. You can either use the ETL Export functionality or Tenant Migration. Identifying what
you are trying to accomplish will help you to decide which option to use.
1. Export Data Model via ETL Tool
The ETL tool is Vena's traditional tool for importing and exporting data. With the ETL tool, you
can export data model hierarchies, selected dimensions and intersection data without
requiring the use of a template. More information about the ETL Export tool, including step-
by-step instructions, can be found here.
02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 12/19

Data models: Model hierarchies and
attributes.✔
Selected Dimensions: Isolate specific
dimensions for export. ✔
Intersection Data
✔
Processes: Process workflows and their
metadata (e.g., task assignments, due dates,
task form assignments, process variables,
etc.).✘
Integration Components: Integration
setups, including sources, channels, and
destinations.✘
2. Export a data model via Tenant Migration
The Tenant Migration feature allows you to easily maintain a multi-environment system by
duplicating work done in one environment in any of your other environments. This means
you can fully build out a complex process in a development (Sandbox) environment away
from live users,  then move it over to a testing environment where you can safely validate it
without touching production data, and finally deploy it on your production environment
when it's ready. Read the Tenant Migration article for more information and step-by-step02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 13/19

instructions.
Data models: Model hierarchies and
attributes.✔
Selected Dimensions: Isolate specific
dimensions for export. ✘
Intersection Data
✘
Processes: Process workflows and their
metadata (e.g., task assignments, due dates,
task form assignments, process variables,
etc.).✔
Integration Components: Integration
setups, including sources, channels, and
destinations.✔
Clone a Data Model
Read this article for full instructions on how to clone a data model. 02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 14/19

Delete a Data Model
1. Navigate to the Modelertab.
2. Navigate to the Data Modeler sidebar.
 Note
After you duplicate a cube, the associated processes should also be duplicated.
This allows the user to re-map any existing templates to the new cube without
disturbing existing templates connected to the source cube.
After the processes have been duplicated, the user should disconnect the new
cube from the source processes to prevent any association with the original data
model. The source cube should only be connected to the source processes and
the new cube should only be connected to the new duplicated processes.
Warning
Delete data models with care, as this may cause errors in PivotT ables or formulas that
reference these tables. PivotT able results can change in unexpected ways after a
relationship is deleted  or deactivated.02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 15/19

3. Hover over the data model you want to delete and select the
 (delete) icon.
4. A confirmation modal will ask you to confirm the deletion. Select Yes, Delete Model to
remove the data model.
5. The data model will be deleted and removed from the list. You have completed the deletion
of the testing environment from your Vena tenant.
 Caution
Ensure there are no processes attached to the data model. Once a data model is
deleted, it will no longer be accessible and can adversely impact any workflow
processes previously attached to it. Processes can be detached by deselecting the02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 16/19


Notes & Limitations
You can build multiple data models in any Vena application.
Each process may connect to multiple data models.
Best Practices
Ensure that each user has the proper access to relevant data models. For example, if a user
doesn't have to provide changes (manual input) to a model, then ensure their Data
Permissions are set to Read.
Make sure that only those individuals who need to make changes (edit, add, remove) are
given Write permissions. The best practice is to only give Write access to users who
modify data. This reduces the risk of data corruption and accidental errors.
Related Topics
Read about how to clone and view a data model.
Read about how to export a data model.
Attach Process button in the Manage Model drawer, accessible via the Manager tab.
Read this article for step-by-step instructions on how to detach a process. 02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 17/19

Read about how to create and manage a data model hierarchy using ETL Import.
Read about how to map from multiple data models to a single template.
Was this article helpful?
5 out of 6 found this helpful
Related articles
How-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
How-To: Build and Manage Data Models in
Modeler
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: Assigning Dimension Types and
Standard Members
How-To: Data Model Series (Part 4): ETL ToolRecently viewed articles
How-To: Formatting an Excel-Based CSV to
Maintain Leading Zeros for ETL Jobs
How-To: Build Your Chart of Accounts
Hierarchy in Quick Start
Explainer: What is Data Model
Standardization?
Troubleshooting: Versioning Copy To and
Copy From Must Be Bottom-Level Members
Troubleshooting: Versioning Copy To and
Copy From must Contain the Same Set of
Dimensions02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 18/19

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:15 How-To: Data Model Series (Part 1): Creating a Data Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039508511-How-To-Data-Model-Series-Part-1-Creating-a-Data-Model 19/19
