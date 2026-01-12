# (Reference)   ETL Guide   2   Vena.io ETL

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
ETL JobsReference: ETL Guide - 2 - Vena.io ETL
Part 1: Overview
Part 2: Vena.io ETL - You are here
Part 3: Command Line ETL
Part 4: Query Languages
Part 5: SQL Staging Environment
Laura Harris
Updated 1 month ago
02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 1/30

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
Chapter 2: Vena.io ETL
ETL Import
Vena.io ETL Screen Layout
Create an ETL Template
File to Cube or Stage to Cube
File to Stage or Stage to Cube
SQL Transform
Channel
Generate Report Books
File to Vena Table
Template Automation
Execute an ETL Template
ETL Jobs
ETL Template Example
Delete an ETL Template
ETL Export/ Exporting a Data Model
Export Query Conditions02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 2/30

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
Data QueryingChapter 2: Vena.io ETL
ETL import
The setup and management of ETL activity can be found in vena.io by navigating to Modeler >
Data Modeler > ETL. Users must have Modeler access.
Every ETL import job requires a template to be defined first.
Using an ETL template increases the likelihood that your ETL job will load successfully, and you
can set up repeating import ETL jobs. Examples of import jobs are Monthly Actuals Update or
Weekly HR Data Refresh. For these jobs, they can have the same steps, but with different source
files.
Each job step in the ETL import template represents a placeholder for files that will be imported.
Each step will be created in chronological order as they are set up, but the steps can be
reordered. The benefit of this is to be able to define multiple steps as part of the same ETL
template. Each step of the import template is defined by two required decisions:
1. What is the step type?
File to Cube, File to Stage, SQL Transform, Stage to Cube, Cube to Stage
2. What is the import type?
Attributes, Hierarchies, Line-Item Details, User Defined, Values
Each time an ETL template is executed, it is called an ETL Job. An ETL job is like instantiating an
ETL template by uploading actual files in place of the placeholders of each job step.
ETL jobs can be tracked with an associated Job ID. To view the Job ID for any ETL job, navigate to
the History sidebar in the Modeler tab. Job IDs are listed in the ETL Jobs table. Below is a high-
level order of operations for setting up and executing an ETL template.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 3/30

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
& Connections
StepDescription
Step 1 - Create Template
The import Step Type field is mandatory. (Import to File, Import to Stage, SQL
Transform, etc.)
Import Data Type field is mandatory. (Attributes, Hierarchy, Values, etc.)
A Staging Table is only needed if File to Stage and Cube to Stage import step types
are selected.
The Template is saved under the ETL Templates.
The Template can be run multiple times. It will run the steps in chronological
order.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 4/30

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
Product UpdatesStepDescription
Step 2 - Execute Template
When users execute an ETL Template:
If the step is File to Cube or File to Stage, they will be prompted to specify:
A source data file.
A source data format.
The number of acceptable invalid lines.
If the step is Cube to Stage:
They will be prompted to specify a query that is written in Standard Query
Language (SQL).
The ETL Job is generated every time a template is executed.
The following image shows the make up of an ETL template:
02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 5/30

Vena.io ETL screen layout
Users with Modeler access and the necessary permissions can use the vena.io Data Integration
features.
Overview of the vena.io ETL options:
 Note
Please refer to the SQL Staging Environment section for options available after
loading .csv files into a Staging table. A Staging environment must be created before
an import can be made.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 6/30

FeatureDescription
AETL
TemplatesFound in the sidebartab and available only to users assigned the Modeler
role.Each time you create a new template and initiate a new ETL Job, a log
(Job schedule) is recorded on this page.
BExport A separate tab to select criteria (e.g., Hierarchy, Line-Item Details) and
export format (e.g., Staging Table, .csv).
C+ Create
TemplateSelect this button to createa new ETL template.
Create an ETL Template
For all of the following options, you must first navigate to the Modeler tab and open the ETL
Templates page.
File to Cube or Stage to Cube
When creating an ETL Template, it's important to consider the data type that you are importing:
Data Type
The Data Type defines the contents that will be imported.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 7/30

Import Type DescriptionStaging Table
Required?
Dimension
HierarchyData Model structure made up of Dimensions and
Dimension Members.      ✗
Values Values belonging to the Dimension Members.       ✗
Line-Item DetailsLine-Item Detail values.       ✗
Attributes Attributetags on the Data Model Dimensions.       ✗
User Defined User Defined criteria which uses a Staging Table.      ✔
1. Select + Create Template.
2. Enter a name for the ETL Template.
3. Select Add Step.
4. Select File to Cube or Stage to Cube from the Add Step drop-down menu. You may have to
scroll in the drop-down menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 8/30

5. Select the desired data type (Alias Mapping, Attributes, Hierarchies, Line-Item Details, Values)
from the Select Data Type drop-down menu.
6. Select Add.
7. Select Save.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 9/30

File to Stage or Cube to Stage
1. Select + Create Template.
2. Enter a name for the ETL template.
3. Select Add Step.
4. SelectFile to Stage or Cube to Stage from the Add Step drop-down menu. You may have to
scroll in the drop-down menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 10/30

5. Select the desired data type (Attributes, Hierarchies, Line-Item Details, Values, User Defined)
from the Data Type drop-down menu.
6. Type or select a table from the Table drop-down menu. 02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 11/30

7. Select Add.
8. Select Save.
SQL Transform
1. Select + Create Template.
2. Enter a name for the ETL Template.
3. Select Add Step.
4. Select SQL Transform from the Add Step drop-down menu. You may have to scroll in the
drop-down menu to see all the options.
 Note
Staging Tables are required for the File to Stage import step.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 12/30

5. Select Add.
6. Select Save.
Channel
1. Select + Create Template.
2. Enter a name for the ETL template.
3. Select Add Step.
4. Select Channel from the Add Step drop-down menu. You may have to scroll in the drop-down
menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 13/30

5. Select a channel that you have previously set up.
6. Select Add.
7. Select Save.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 14/30

Generate Report Books
1. Select + Create Template.
2. Enter a name for the ETL template.
3. Select Add Step.
4. Select Generate Report Book from the Add Step drop-down menu. You may have to scroll in
the drop-down menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 15/30

5. Select a process that you have previously set up.
6. Select Add.
7. Select Save.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 16/30

File to Vena Table
1. Select + Create Template.
2. Enter a name for the ETL template.
3. Select Add Step.
4. Select File to Vena Table from the Add Step drop-down menu. You may have to scroll in the
drop-down menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 17/30

5. Select a Vena Table that you have previously set up.
6. Select Add.
7. Select Save.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 18/30

Template Automation
1. Select + Create Template.
2. Enter a name for the ETL template.
3. Select Add Step.
4. Select Template Automation from the Add Step drop-down menu. You may have to scroll in
the drop-down menu to see all the options.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 19/30

5. Select a process that you have previously set up.
6. Select Add.
7. Select Save.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 20/30

Execute an ETL template
1. On the ETL Templates page, select the
(Run) icon next to the ETL Import template you
want to execute.
2. If there is a step for File to Stage orCube to Stage:
1. Select Choose File. Find the file on your device and open it.
2. Select a File format for the source document.
3. Select the File encoding.
4. Select the number of Accepted Invalid Lines.
*The number of acceptable invalid lines allows a user to specify the number of row errors
that can be skipped as part of an import.
Caution
When data models share dimensions, running ETL jobs at the same time can cause
data conflicts and calculation errors. For example, if one ETL job is updating a shared
dimension while another relies on it for calculations, running these jobs at the same
time can lead to incorrect calculations.
Learn more about Linked Dimensions.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 21/30

3. Select Run.
ETL Jobs
After you execute an ETL Template, you can view the ETL job log in the ETL Jobs table on the
History page.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 22/30

Feature Description
AHistory History navigates to the ETL Jobs section.
BJob ID A unique tag used to identify a specific Job.
CJob Name Name assigned to the Job by User. Select the name to see additional
details for each step of the execution, including Step Description, Log,
Errors, Started On, Completed On, Status, and Rows Processed.
aSteps A unique tag used to identify a specific Job.
bLog Timestamp and associated details.
cErrors Any errors associated with the Job.
dStarted When the specified Job Template was executed
(local time).02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 23/30

Feature Description
eCompletedWhen the specified Job Template finished
executing. (local time)
fStatus Status of the respective Job.
gRows
ProcessedThe number of rows processed successfully.
DCreated OnThe date and time that the Job was created.
ELast Run The date and time that the Job was last run.
FUser The User that ran the Job.
GData ModelThe name of the affiliated Data Model.
HStatus The Status of the respective Job.
Delete an ETL template
1. On the ETL Templates page, either right-click the row or select the vertical ellipsis at the end of
the row you want to delete.
2. Select Delete.
3. Select Delete Template in the pop-up window to confirm the deletion.
ETL Export/Exporting a Data Model02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 24/30

Unlike import, you do not need to have a template defined to export data or metadata. Below
are the specific export options. Modelers can use the ETL Export feature to export Dimension
Hierarchies and Data from a Data Model. Learn more about ETL Export in this article.
Feature Description
AETL Export Location of the ETL Export page.
BSelect Export
Type02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 25/30

Feature Description
Export
TypeDescription
Alias
Mapping Used to export Member Aliases
(descriptions) associated with Member
Names in your model.
AttributesAttribute tags on the Model Dimensions.
HierarchyData Model structure is made up
of Dimensions and Dimension Members.
Hierarchy
(BI)Data Model structure made up of
Dimensions and Dimension Members
formatted in a way that Power BI can digest.
Line-Item
DetailsLine-Item Detail values.
Staging
TableStaging Table are used for Staging Queries or
Drill-Transactions.
Values Values belonging to the Dimension
Members.
Vena
TableValues belonging to Dimension Members
including calculated members, parent
member totals and read calcs.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 26/30

Feature Description
CAdvanced
Options Additional options so you can customize your export and choose the
export destination, file format, and file encoding.
Export Query conditions
When exporting data, best practice is to filter it to limit the export to required datasets. This will
help ensure that your ETL job runs successfully and loads in a timely manner. To filter your
query, you can use a clause on the export command.
The Export Query field accepts an HQL WHERE clause conditional filter.
Example 1:
Export all data that is in the Year 2025.
dimension('Year':'Y2025')
Example 2:
Export all data that is in Year 2025 and 2026.
dimension('Year':union('Y2025''Y2026'))02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 27/30

Example 3:
Export all data that is in Year 2025 and 2026 and Entity member Dept 101.
dimension('Year':union('Y2025''Y2026'))dimension('Entity':'Dept 101')
Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
3 out of 6 found this helpful
 Note
HQL stands for Hibernate Query Language, a data querying language roughly based
on SQL. From the vena.io web interface, you can also export data to a downloadable
.csv file, which doesn’t require a staging table. The data exported is in the same
format as the import format (CSV/tabular).02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 28/30

Related articles
Reference: ETL Guide - 3 - Command Line ETL
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
How-To: Exporting CSV Files for ETL Job
How-To: Setting up a Staging Query (Vena 365
Only)
How-To: Bulk Attach/Detach Attributes and
Filter by AttributesRecently viewed articles
Reference: ETL Guide - 1 - Overview
Troubleshooting: No Values Generate for a
Reporting Currency
Troubleshooting: Calc Script Using
.BottomLevel() and .Exclude() in a Tuple Not
Working Properly
Troubleshooting: Calc Is Not Triggering or
Calculating After Data Load or Import
Troubleshooting: Calc Conversion Not
Working or Zero Values Appearing
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 29/30

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:41 Reference: ETL Guide - 2 - Vena.io ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028194291-Reference-ETL-Guide-2-Vena-io-ETL 30/30
