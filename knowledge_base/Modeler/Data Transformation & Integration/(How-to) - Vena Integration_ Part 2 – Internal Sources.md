# (How to)   Vena Integration  Part 2 – Internal Sources

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
ETL JobsHow-to: Vena Integration: Part 2 –
Internal Sources
About this series
This series is all about how to use Vena Integrations. You are in Part 2, which outlines what
internal sources are and how to create and manage them.
Vena Support
Updated 1 month ago
05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 1/23

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
– External Sources – Data FeedsVena Integration is a large and complex tool, and it continues to grow. We've broken down the
information in this series into manageable parts, each focusing on a specific area of the
Integration tool and its related concepts.
This series was designed to be read in order. If you don't have any previous experience with the
Integration tool, we recommend that you follow this approach, starting with Part 1. But if you are
familiar with Integration, feel free to explore around for what you need.
Part 1: Feature Overview
Part 2: Internal Sources –you are here
Part 3: External Sources – Data Feeds & Connections
Part 4: External Sources – Import and Export API
Part 5: Destinationspan
Part 6: Channels & Field Mappings
Video
Check out a video of this article's content.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 2/23

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
Product UpdatesVena Integration Part 2: Internal Sources Vena Integration Part 2: Internal Sources
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application
Permissionsfor authorizations.
If Data Permissions are set up in your environment, you will also need the appropriate
permissions for the data that you are working with.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 3/23

Table of contents
About Sources
How to
Create an internal source
Manage your sources
Previewing a source
Editing a source
Deleting a source
Reference Guide: Source Types
About sources
Remember the basics of Integration involve the following:
1. Creating a source.
2. Linking that source to a destination using a channel.
Sources tell the Integration tool everything it needs to know about the data you want to bring
into Vena: what data to retrieve, and where to find it.
It's important to note that a source doesn't only point to the location of the data but also
specifies which data you want from that location (the "data load").
The distinction is important because multiple integration tasks may pull different data from the
same location. Create separate sources for each integration task to customize your data queries.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 4/23

There are a few different types of sources:
Internal
Data Model
Process
SQL Staging
Excel
CSV
User
Learn more about the internal source types in the Source Reference Guide.
External
External sources refer to:
1. The built-in connections made between Vena and a third-party application, which include:
2. Salesforce
3. QuickBooks
4. Intacct
5. Business Central
6. NetSuite
7. Other third-party connections utilizing Vena’s public API.
This article details internal sources only. Learn about external sources and built-in
connections in Parts 3 and 4 of this series. 05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 5/23

How to
Creating an internal source
When you create a new source, the basic procedure is the same regardless of the source type.
This section outlines the general steps to create any source, while details specific to each source
type are covered in the Reference Guide.
1. Navigate to the Modeler tab.
2. Select Data Transformations.
3. Select Channels.
4. Select the Create button in the top right.
5. In the menu, select Source to open the Create Source pop-up.
05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 6/23

6. Begin by typing a name into the Source Name field to describe your source. Then, use the
Source Type drop-down to choose which kind of source you want to create:
7. After you choose a source type, additional fields will appear that are specific to that type of
source. For instructions on how to configure each source type, visit the Reference Guide.
8. When you have finished configuring the new source, select Create. The newly created source
will appear at the root level of the Channels tab.
Note
For information on VenaQL sources, visit this article.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 7/23

Managing sources
When you save a new source, it appears in the Channels tab with a yellow icon and its logo.
Right-click or select the vertical ellipses (
) to view options for renaming, moving (into or out
of a folder) or deleting the source. Use the Preview data function to test if the source works
correctly.
Previewing a source
The Preview data function allows you to quickly preview any type of source by pulling in a small
sample of its data. This is useful for verifying if a source has been set up correctly.
1. In the Channels tab, select Preview data for the source you wish to preview (see above).05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 8/23

2. The previewed data is displayed as a table in a new pop-up window.
3. Troubleshoot your source setup by exporting all rows without the need to create "dummy"
channels to preview streamed data. When finished, select Close to return to the Channels
tab.
Editing a source
You may make changes to a source (such as modifying its setup or renaming it) at any time.
1. On the Channels tab, navigate to the source you want to edit in the list (you can use the
filters to help find the desired source).05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 9/23

2. Select the source name you want to modify.
3. This opens the Edit Source pop-up, which is identical in structure to the Create Source pop-up
and varies depending on the type of source selected (e.g. Selecting a VenaQL source opens
the VenaQL Query Editor). Use the fields and drop-downs (as applicable) to make the desired
changes.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 10/23

4. When you have finished making your changes, select Save. This will close the EditSource
window, and you will return to the Channels tab.
Deleting a source
You may delete a source at any time, provided it is not currently used as part of a channel setup.
1. On the Channels tab, select Delete for the source in question(see above).
2. A message will appear asking if you are sure you want to delete the source. Select Delete to
proceed.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 11/23

3. You will return to the Channels tab, where the source will immediately be removed from the
list.
Note
You can't delete sources that are still being used as part of a channel setup. You’ll see
an error message if you attempt this:
05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 12/23

Reference Guide: Internal Source Types

Data Model
The Data Model source type lets you extract data from a Vena database, typically for
transforming and loading it into another Vena database or back into the same one. While similar
to the Versioning tool, it offers a simpler process using the Channels interface.
To delete such a source, you must first remove it from any channels indicated.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 13/23

AData
ModelChoose the data model from which to pull data.
BData
TypeChoose the type of data to extract from the selected model. You can choose:
Attributes
Hierarchy
Intersections
Line-Item Details05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 14/23

CQuery
fieldOptional. Use this field to narrow the selection to a specific part of the data model,
known as a slice. Slices are defined using expression queries written in Model Slice
Query Language (for Intersections and Line-Item Details) or Hibernate Query
Language (for Hierarchy and Attributes. For multiple slices, separate each
expression with a comma.
Learn more about writing MQL and HQL expressions.
Process
The Process source type lets you extract Vena process metadata for reporting or recording into a
Vena database. Use this with the Process destination type to populate or modify processes in bulk
via the Integration tool.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 15/23

AProcess
OptionsChoose whether the source includes all processes or a specific process.
BData TypeChoose what type of process-related data to pull with this source. The options
are:
Tasks: Selects all process workflow metadata (i.e. activities, activity items,
associated users, task forms, due dates, etc.).
Task Audits: Selects all process activity metadata (i.e. records of task
submissions and review approvals and submission, associated users,
timestamps, etc.).05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 16/23

CWith
ConditionInclude processes based on their status (e.g., In Play, Paused, Completed, Not
Started) by checking the desired statuses (multiples are allowed). Processes
without the selected statuses will be excluded. If no boxes are checked, all
processes will be included regardless of status.
Note: These settings appear only after you have chosen the Process Option
and Data Type.
SQL Staging
The SQL Staging source type allows you to extract data from one of your Vena staging stables.
This is useful for situations where you want to use a staging table to perform transformations
that are not possible with the Integration tool, then further process the prepared data using
Integration.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 17/23

AData ModelChoose the data model to which the staging table belongs.
B Select
StatementSpecify the staging table and the data to pull by entering an SQL SELECT
statement to define the table name and records to be returned.
Excel05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 18/23

ASelect
FileSelect the uploaded Excel file that contains your data table.
Note: Only files already uploaded to Vena can be selected.
BSheet
nameSpecify the name of the sheet where the table is located, as it appears in Excel.
CColumnsSelect the columns you want to include by typing in their Excel letters, separated
by commas (e.g., A,B,C,D). You can skip columns (e.g., A,C,D,F).
DFirst rowSpecify the Excel row number that corresponds to the first row of the table.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 19/23

EHeader
rowSpecify the Excel row number if the table has a header row. Leave this blank if
there is no header or you want to omit it.
Note: Including a header row in an Excel source file is recommended because it
ensures that the headers are used to label the source fields in the Channel
Details view when selecting an Excel source. Without a header row, source fields
will be labeled with the Excel column letter (e.g., A, B, C), potentially complicating
the channel setup process.
CSV
Use this option to import data from a file in the CSV (comma separated values) format.
ASelect FileSelect to open the file browser and choose the CSV file to extract data from. 05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 20/23

Note: Only files uploaded to Vena can be selected.
User
The User source type extracts user data from the Users tab in the Admin section of Vena. It is
primarily for reporting on Vena users and does not have any configurable options.
Was this article helpful?
4 out of 4 found this helpful05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 21/23

Related articles
How-to: Vena Integration: Part 3 – External
Sources – Data Feeds & Connections
Reference: Writing Expressions (MQL & HQL)
How-to: Vena Integration: Part 1 - Feature
Overview
How-to: Vena Integration: Part 4 – Import and
Export API
Reference: ETL Guide - 4 - Query LanguagesRecently viewed articles
How-to: Vena Integration: Part 1 - Feature
Overview
Troubleshooting: Vena Export API 429 Too
Many Requests Status Code
Troubleshooting: Vena Import & Export API
422 Unprocessable Entity
Troubleshooting: Vena Import API 406 Invalid
Accept Header Status Code
Troubleshooting: Vena Import & Export API
405 Method Not Allowed Status Code
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 22/23

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 13:00 How-to: Vena Integration: Part 2 – Internal Sources – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027300271-How-to-Vena-Integration-Part-2-Internal-Sources 23/23
