# (Reference)   ETL Guide   5   SQL Staging Environment

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
ETL JobsReference: ETL Guide - 5 - SQL Staging
Environment
Part 1:ETL Guide Overview
Part 2:Vena.io ETL
Part 3:Command Line - ETL
Part 4:Query Languages
Vena Support Team
Updated 4 months ago
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 1/23

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
Restrictions to the SQL WHERE
ClausePart 5:SQL Staging Environment -You are here
Part 6:Using Staging Data
Table of contents
Chapter 5: SQL Staging Environment
The SQL Staging Environment Overview
Upload Data to the Staging Environment (vena.io & cmd)
vena.io
Command Line
Providing Multiple Import/Export Steps
Clearing Intersection value with Staging
Clear Slice by Expressions
Clear Slices by Dimension
Carrying Out a Staging Transformation
Finalizing a Staging Transformation
Chapter 5: SQL Staging Environment
The SQL Staging Environment Overview02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 2/23

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
Data Querying
Vena TablesBy default, the data in the CSV files are imported directly into the Vena Cube. However, in some
cases, transformation of the data is required before importing. A SQL staging environment is
provided for this purpose and is hosted by Vena.
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 3/23

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
How-to: Vena Integration: Part 4
– Import and Export API
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 4/23

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
Product UpdatesUpload Data to the Staging Environment (vena.io & cmd)
Data can be imported into the Staging Environment through vena.io or the Command Line ETL. After
an import Job is completed, the ETL process commences and sets the Staging Environment to a
Waiting state. During the Waiting state, no further import processes can be made. The reason for this
approach is so that Vena Consultants have the opportunity to connect to the Staging Environment to
apply manual SQL transformations or kick off automated transformations (i.e., stored procedures or
jobs). When the transformation is complete, you can run a command line to tell Vena to update the
Job state to Complete, which reopens the Staging Environment for new import Jobs.
Modelers will be able to run the Vena ETL Tool from the Command Line in order to automate data
integration tasks. All files for importing and exporting data must be in CSV or TDF format. With the
Command Line tool, you can import files and monitor your progress.
vena.io
Create an ETL Import Template with one or more User Defined import steps.
To create an ETL template:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar. If you have multiple data models, ensure the correct data
model is selected.
3. Select ETL Templates from the sidebar tab. By default, you should be in the Templates section of
the ETL tool, which lists your existing ETL templates in the ETL Job Schedule table.02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 5/23

4. Select +Create Template.
There are 4 step types that can be used in an ETL template to import via the Staging Environment:
ETL Staging (vena.io):
step typesDescription
File to Stage Loads the files into the SQL Staging area.
SQL Transform Awaits SQL transformations for the files loaded into the SQL Staging area.
Stage to Cube Loads data from a Staging table into the Vena database.
Cube to Stage Loads data from the Vena database to the Staging table if additional SQL
transformations are required.
Below is an example of how each step can be used for importing data via the Staging table:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 6/23

Step 1
-Upload Monthly Actuals to a staging table.
Step 2
- Extract hierarchy to the staging environment, which will be used in the next
step to filter on accounts in the cube.
Step 3
- Transform the data to be uploaded to cube and hierarchy.
Step 4
- Push hierarchy from stage to cube.
Step 5
- Push values from stage to cube.
Note
The data types available will differ depending on which step type you select:
File to Stage SQL Transform Stage to Cube Cube to Stage
Attributes No input
parameters
required Attributes Attributes
Hierarchy Hierarchy Hierarchy
User Defined Values Values
Values Line-Item Details Line-Item Details
Line-Item Details Alias Mapping Alias Mapping
Alias Mapping   02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 7/23

02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 8/23

Select Run to execute the Template. At this point, you can also enter a job name for easier
identification.
To view your ETL job, select History from the sidebar.
A successful execution causes the Staging Environment to enter a Not Started state and locks the
system from further ETL imports.
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 9/23

 Command Line
Using Command Line to upload CSV or TDF files to the SQL staging environment, use the --
stage option.
java -jar ../../target/ETL.jar - host=localhost -port=8080 --Username= johnsmith -- Password= venapas
--modelName= "MODELNAME"  --stage --file='xyz.csv;user\_defined;xyz\_table'
The CSV or TDF file formats accepted are the same formats as for non-staging pathway, plus a
user_defined format, which allows for arbitrary CSV or TDFfiles. All rows must have the same number
of columns.
There can be multiple user-defined CSV or TDF files, and the schema for each can be different, but be
sure to give them unique table names. The name of the input table must be specified in the
command-line argument for each file:
--file='xyz.csv;user_defined;xyz_table'
Providing Multiple Import/Export Steps
There are 4 step types used as an individual Command Line option to import via the Staging
Environment:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 10/23

ETL Staging
(vena.io):
step typesCommand Line (cmd):
options syntaxDescription
File to Stage--file "[file=]<filename>;
[type=]<filetype>
[;[table=]<tableName>]
[;format={CSV|TDF}]
 [;bulkInsert={true|false}]
[;clearSlices=<expr>]"
 --stageOnlyLoads the files into the SQL Staging area.
SQL
Transform--transformComple --jobId
<id>Awaits SQL transformations (--
transformComplete or --cancel or --setError) for the
files that have been loaded into the SQL Staging area.
Stage to Cube--loadFromStaging Loads data of the given type (hierarchy, LIDS,
attributes and/or intersections) from the Staging
table into the Vena Data Model.
Cube to Stage--export <type> --
exportToTable <tableName>Export hierarchy and intersections from the Vena
Data Model to Staging table, if additional SQL
transformations are required.
The step types can also be combined and executed sequentially if the import via the Staging
environment requires multiple steps. To do this, use the following Command Line with a text file that
includes all the steps with each step on a separate line:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 11/23

--loadSteps <fileName> Name of File containing load steps.
Each line of the file can include one of the following steps for importing via the Staging Environment:
ETL Staging
(vena.io):
step typesCommand Line (cmd):
options syntaxDescription
File to CubefileToCube "[file=]<filename>;
[type=]<filetype>
[;[table=]<tableName>]
[;format={CSV|TDF}] --
stageOnlyLoads the files into the Vena Data Model.
File to StagefileToStage "[file=]<filename>;
[type=]<filetype>
[;[table=]<tableName>]
[;format={CSV|TDF}]
 [;bulkInsert={true|false}]
[;clearSlices=]"
 --stageOnlyLoads the files into the SQL Staging area.
SQL
TransformsqlTransform --jobId <id> Awaits SQL transformations for the files that have
been loaded into the SQL Staging area.02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 12/23

ETL Staging
(vena.io):
step typesCommand Line (cmd):
options syntaxDescription
Stage to CubestageToCube [type=<type>]
[;clearSlides=<expression>]Loads data of the given type (hierarchy, LIDS,
attributes and/or intersections) from the Staging
table into the Vena Data Model.
Cube to StagecubeToStage type=
<type>;table=<tableName>
[;exportWhere=<clause>]
[;exportQuery=<expression]Export hierarchy and intersections from the Vena
Data Model to Staging table, if additional SQL
transformations are required.
Where:
type may be one of: intersections, lids, hierarchy, attributes, user_defined.
exportWhere=<clause>: Where clause for export (HQL). May not be combined withexportQuery.
exportQuery=<expression>: Query expression for export (model slice language). May not be
combined withexportWhere.
clearSlices=<expression>: Expression (model slice language) to define the slice(s) of the cube to
clear intersections from. May only be combined withtype = intersections.
clearSlicesByDimNums=<numbers>: Numbers to define the dimensions used to compute the
slice(s) of the cube to clear intersections from. May only be combined withtype = intersections.
Using the same example as above, each step can be configured together for importing via the Staging
table using--loadSteps Command-Line with the text file containing a list of multiple steps:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 13/23

Step 1Upload Monthly Actuals to a staging table.
Step 2Extract hierarchy to the staging environment, which will be used in the next
step to filter on accounts in the cube.
Step 3Transform the data to be uploaded to cube and hierarchy.
Step 4Push hierarchy from stage to cube.
Step 5Push values from stage to cube.
Example Command:
java -jar ../../target/ETL.jar -host=staging.vena.io -Username=johnsmith
--Password=venapass --modelName="FinancialReportingCube" -loadSteps
files/multi_steps_cmd_example.txt
Example steps within the text file:
fileToStage
files/Jan_MonthlyActuals .csv;intersections;ts_MonthlyActuals;format= CSV;bulkInsert=true
cubeToStage type=hierarchy ;table=the_Hierarchy
sqlTransform
stageToCube type=hierarchy
stageToCube type=intersections
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 14/23

Clearing Intersection value with Staging
You can clear intersection values from specified slices of the data model when loading intersections
from the SQL Staging Environment. There are two supported keywords:
clearSlices and clearSlicesByDimNums.
Clear Slice by Expressions
The clearslices keyword allows you to define the slices to clear using Model Query Language
expressions.
To do this, you would specify the slices as such:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 15/23

--clearSlices=<expression>
where <expression>is a string that specifies one slice or more than one slice separated by a comma
using model slice expression language. For more information on expression syntax, please refer to
the Model Query Language section.
Examples:
This command defines one slice to be cleared: {Ottawa, Squirrel}
--clearSlices= "dimension(' City':'Ottawa' ) dimension( 'Animal' :'Squirrel' )”
This command defines two slices to be cleared: {Ottawa, Squirrel} and {Toronto, Squirrel}
--clearSlices= "dimension(' City':'Ottawa' ) dimension( 'Animal' :'Squirrel' ),
dimension( 'City':'Toronto' ) dimension( 'Animal' :'Squirrel' )”
Clear Slices by Dimension
The clearslicesByDimNums keyword allows you to define the slices to clear by referencing a series of
dimension numbers in the destination.
To do this, you would specify the slices as such:
--clearSlicesByDimNums=<numbers>
where <numbers> is a string that specifies one or more dimension numbers separated by a comma.
Examples:02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 16/23

This command defines the slices to be cleared as all those slices present in the import that
correspond to the first and third dimensions:
--clearSlicesByDimNums="1,3”
For example, if your staging table contained the following rows, and you used the command above,
the slices specified to be cleared would be {Ottawa, 2014}, {Toronto, 2014} and {Waterloo, 2015}.
_dim1_member _dim2_member _dim3_member _value_etl_id
Ottawa Squirrel 2014 20
Toronto Squirrel 2014 30
Waterloo Rabbit 2015 40
When you specify a slice to clear, the behavior follows a regular load of intersections, with the
exception that any values in the specified slice(s) that are not found in staging will be cleared.
As such:
If there is a new intersection in the out values staging table, it is loaded to the cube.
If there is an existing intersection in the table with an unchanged value, no change occurs.
If there is an existing intersection in the table with a changed value, the value is updated in the
cube.
If any intersections in the specified slice(s) of the cube do not exist in the table, their values will be
cleared.02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 17/23

The commands --clearSlices and --clearSlicesByDimNums can be used with --stage, --
stageAndTransform, --loadFromStaging and --loadSteps.
Examples:
--stage --file "file=clearSlices4.csv;
type=intersections; format=CSV; bulkInsert=true"
-clearSlices= "dimension(' Years':'Y2014')
dimension( 'Locations' :children( 'Location11-20' )"
--loadFromStaging --clearSlices=”dimension(' Years':'2014')
dimension( 'Month':'Jan')”
Carrying out as Staging Transformation
 Note
This feature only clears the values of the intersections in the specified slice(s) and does
not delete Line-Item Details.
For information on using --clearSlices or --clearSlicesByDimNums with --loadSteps, see the
Providing Multiple Import/Export Steps section.02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 18/23

When the upload into the SQL staging environment is complete, a tableetl_jobswill be created with a
single row containing the ETL job ID in columnjob_id. This signals that the SQL transformation can
start. Additionally, it will create four empty output tables related to thejob_id.
Data TypeTable Name
(output)
hierarchyout_hierarchies
intersectionsout_values
attributesout_attributes
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 19/23

Data TypeTable Name
(output)
lids out_lids
The goal of the transformation process is to place the data into these four output tables. When the
transformation is complete, the Vena server will read from these tables in a predetermined order and
load the data into the Vena Cube. This data is treated the same as if it came from the CSV files in a
direct CSVto Vena Cube ETL (without staging), so the same restrictions apply.
The Vena app server is not involved in the transformation process. The transformation process is free
to manipulate, create and delete tables as needed.
Below is the SQL perspective of loaded data table. Immediately after the first import of any kind into
the Staging Environment, the ETL Jobs and four Output tables are created. Users can create
additional tables and views or Stored Procedures and Jobs to apply transformations. Populate the
Output tables when finished.
02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 20/23

 
Finalizing a Staging Transformation
When the SQL transformation is finished, it should signal the server by calling the following REST API:
GET /api/etl/jobs/<etl job id>/transformComplete
Alternatively, use the ETL command line tool:
java -jar ../../target/ETL.jar - host=localhost -port=8080  -Username= johnsmith -- Password= venapass
--transformComplete --jobId=12345
The server will then continue to the loading step of the ETL.
If the SQL transformation encounters a problem and can't recover, it can update the status by calling:
GET /api/etl/jobs/ <etl job id> /setError?message= <URL encoded error message>02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 21/23

 Alternatively, use the ETL command line tool:
java -jar ../../target/ETL.jar - host=localhost -port=8080   -Username= johnsmith -- Password= venapas
--setError 'my error message' --job=12345
Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
2 out of 3 found this helpful
Related articles
Reference: ETL Guide - 6- Using Staging Data
Reference: ETL Guide - 4 - Query Languages
How-To: Exporting Data From a SQL Staging
Table
Reference: Writing Expressions (MQL & HQL)Recently viewed articles
Reference: ETL Guide - 4 - Query Languages
Reference: ETL Guide - 3 - Command Line ETL
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 1 - Overview02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 22/23

How-To: Setting up a Staging Query (Vena 365
Only)Troubleshooting: No Values Generate for a
Reporting Currency
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:43 Reference: ETL Guide - 5 - SQL Staging Environment – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321591-Reference-ETL-Guide-5-SQL-Staging-Environment 23/23
