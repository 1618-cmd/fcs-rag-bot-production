# (Reference)   ETL Guide   3   Command Line ETL

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
ETL JobsReference: ETL Guide - 3 - Command
Line ETL
Part 1: Overview
Part 2:Vena.io ETL
Part 3: Command Line - ETL - You are here
Part 4: Query Languages
Vena Support Team
Updated 1 month ago
02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 1/29

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
Restrictions to the SQL WHEREPart 5: SQL Staging Environment
Part 6: Using Staging Data
Table of contents
Chapter 3: Command Line  ETL
Command Line - ETL
Command Line - ETL Requirement
Command Line - ETL Tool Setup
Install Java (Windows)
Install Command Line - ETL Tool
Test Command Line - ETL
Command Line - Login Requirements
Application Tokens
Importing Data
Importing data into a Vena Table
Create Model Hierarchies (Cmd)
Modify a Hierarchy (Cmd)
Intersection Values (Cmd)
Clearing Intersection Values during Import
Clear Slices by Expression
Clear Slices by Dimensions
Exporting Intersection Values (Data) form the Cube02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 2/29

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
Data QueryingQuery Parameters
Deleting Intersections
Running an Integration Channel
Running an ETL Template
Chapter 3: Command Line ETL
Command Line - ETL
Modelers can run the Vena ETL Tool from the Command Line in order to automate data
integration tasks. All files for importing and exporting data are required to be in .csv format.
With Command Line, you can import files and monitor your progress.
Another option for automating data import is to use the Import API. Visit this link to access the
Public API User Guide.
Command Line - ETL Requirements
To use the VenaCommand Line Tool, the following requirements must be met:
Feature Requirement
User Role = MODELER02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 3/29

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
& ConnectionsFeature Requirement
User Group Application Permission = UPDATE (on the applicable Data
Model)
If Data Permissions are enabled:
Data Permission = READ/WRITE (on the applicable Data
Model)
Client Machine Java = Java Version 17
Jar File = Latest version of Jar File
(Please reach out to support@venasolutions.com for the
latest Jar file)
Network The following website must be on the approve list:
  *https://vena.io, port 443
 Note
Depending on the region of your Vena
environment, you may need to provide a host
value.
Examples: us1.vena.io, eu2.vena.io,
ca3.vena.io, us5.vena.io02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 4/29

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
Product UpdatesCommand Line - ETL Setup
Install Java (Windows)
1. If you do not have Java, or if you have an older version that needs to be updated (see version
requirements below), use the links in the table to download Java or an open-source
alternative.
Recommended Minimum02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 5/29

Java 17
Download here.
This version of Java requires an Oracle
paid subscription. If your company does
not already have an Oracle subscription
for Java, please use the link below to
download an open-source alternative.
OR
OpenJDK 17
Download here.
This is an open-source alternative to Java.
If you choose to download this software,
make sure to select version JDK 17.Java 8*
*Must default to TLS 1.2 security protocol.
2. Open a cmd window and type java -version to confirm that Java can be run from the
command line.
3. This may require adding the Java Bin directory to the executable path. In Windows this is
done via the Windows System control panel.
Install Command Line - ETL Tool (vena.io)
To download the Command Line ETL Tool:
1. Select your username at the top right of your vena.io web page.
2. Select ETL Tool from the sidebar.
3. Select Download Tool. Once downloaded, place the jar file in a directory such as  C:/Java/,
and rename the file to etl (e.g., etl.jar).
 Note
If you have an older version of Java that is not supported, you must uninstall it
and reinstall a new version. Visit this page for instructions on how to uninstall
Java.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 6/29

Test Command Line
Once you have Java running, test that it can execute the ETL Command Line Tool as follows:
1. Open a cmd window.
2. Type CD C:/Java/ to browse to the directory where the .jar file was placed.
3. Run the following command:
java -jar etl.jar --help
This should produce an output like this:
usage: etl-tool [--host <addr>] [--port <num>] [--ssl|--nossl]
 { --apiUser=<uid.cid> --apiKey=<key>
 | --user=<email> --password=<password>
 }
 { --modelName <name> | --modelId <id>
 }02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 7/29

 { [--queue|--noqueue]
 }
 { --loadFromStaging [--wait|--waitFully]
 | [--runTemplate=<templateId>]
 | [--stage|--stageOnly|--venaTable] [--wait|--waitFully]
 [--validate] [--templateId <id>] [--jobName <name>] --file
 "[file=]<filename>; [type=]<filetype>
 [;[table=]<tableName>] [;format={CSV|PSV|TDF}]
 [;bulkInsert={true|false}]"
 | --cancel --jobId <id>
 | --setError --jobId <id>
 | --status --jobId <id>
 | --transformComplete --jobId <id>
 | --delete <type> --deleteQuery <expr> [--nowait]
 | --export <type>
 {--exportQuery <expr> | --exportWhere <clause>}
 {--exportToFile <name> [--excludeHeaders] [--exportFormat
 {CSV|PSV|TDF}] | --exportToTable <name> [--nowait]}
 | --loadSteps <file>
--apiKey <key> The api key to use to access the
 API. Example
 4d87c176227045de9628fb5f010a7b40
 . Note: This is different from
 the password used to login!
 --apiUser <uid.cid> The api user to use to access
 the API. Example
 38450575909584901.2, (user
 38450575909584901, customer 2).
 Note: This is different from the
 username used to login!
 --cancel Request a job to be cancelled.
 Requires --jobId option.
 --clearSlices <expr> The expression specifying the
 slice of the cube to clear
 intersections from. Multiple02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 8/29

 expressions separated by a comma
 are supported.
Etc.etc.etc...
Command Reference Guide:
--apiKey <key>  The api key to use to access the API.
Example: 4d87c176227045de9628fb5f010a7b40
(This is different from the password used to login.)
--apiUser <uid.cid>  The api user to use to access the API.
Example: 38450575909584901.2, (user
38450575909584901, customer 2).
(This is different from the username used to login.)
--cancel Request a job to be cancelled.
Requires: --jobId option.
--clearSlices <expr>The expression specifying the slice of the cube to clear intersections
from. Multiple expressions separated by a comma are supported.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 9/29

--clearSlicesByColumns
<columns>A list of column names separated by commas to be used to
compute slices to clear.
--clearSlicesByDimNums
<dimensions>A list of dimension numbers separated by commas to be used to
compute slices to clear.
--createModel <name> This causes a brand new model to be created with the specified
name.
See also:--modelId.
--delete <type> Delete all <type> from the data model that matches.
--deleteQuery. <type> This query can be one of {intersections, values, lids}.
--deleteQuery <expr> The query expression to match for --delete.
--excludeHeaders Exclude header row when exporting to file.
--export <type>Export part of the datamodel to a staging table. <type> may be one
of {intersections, values, lids, hierarchy, dimensions, attributes,
user_defined, intersection_members, lid_members, variables,
setexpressions}.
--exportFormat <arg>File format for export to file (default CSV). Other options: PSV, TDF.
--exportFromTable <name>Name of table in staging DB to export from. By default, this waits for
the job to complete unless --nowait is specified.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 10/29

--exportQuery <expr> Query expression for export (model slice language). May not be
combined with--exportWhere.
--exportToFile <name> Name of file to export to.
--exportToTable <name>Name of table in staging DB to export to. By default, waits for
the job to complete unless --nowait is specified.
--exportWhere <clause>Where clause for export (HQL). May not be combined with --
exportQuery.
-F,--file <options> A data file to import (multiple allowed).
-F "[file=]<filename>;
[type=]<filetype>
[;[table=]<tableName>]
[;format={CSV|PSV|TDF}]
[;bulkInsert={true|false}]
[;clearSlices=<expr>]
[;clearSlicesByDimNums=
<expr>]
[;encoding=<fileEncoding>]
[;clearSlicesByColumns=
<listOfColumnNames>] "Where <filetype> is one of {intersections, values, lids, hierarchy,
dimensions,
attributes, user_defined, intersection_members, lid_members,
variables, setexpressions}>. and <expr> is the expression specifying
the slice of the cube to clear intersections from. Multiple
expressions separated by a comma are supported. and
<fileEncoding> is the type of encoding used by the file to be
imported, e.g. UTF-16,Windows Latin-1. and <listOfColumnNames>
is a
comma-separated list of column names to clear on.
Example:-F model.csv;hierarchy
Example:-F file=values.tdf;format=TDF;type=
intersections;encoding=CP1252
Note : Encoding UTF-8 is default if not specified; for Windows Latin-1
=CP1252; for UTF-16 use UTF-1602/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 11/29

--helpPrint this message.
--host <addr> The hostname or region of your Vena account defaults to vena.io.
To find your region, check the URL when logged into Vena account.
Examples: us1.vena.io, eu2.venaio, ca3.vena.io, us5.vena.io.
--jobId <id> Specify a job ID (for certain operations).
Example: --jobId=79026536904130560
--jobName <name> Specify a job name (when creating a new job only).
--loadFromStaging  Load data from the SQL staging area. This creates a new job ID.
--loadSteps <fileName> Name of file containing load steps.
--modelId <id> The Id of the model to apply the etl job to.
See also: --modelName.
--modelName <name> The name of the model to apply the etl job to.
See also: --modelId.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 12/29

--noqueue Do not queue this ETL Job if another job is already running under
this data model.
--nossl Don't use SSL encryption to connect to the server.
--nowait Don’t wait for the job to fully complete before returning. The
command will return as soon as the job is submitted.
-p,--password <password>The password to use to access the API.
This is the same password you would use to log in to the Vena
application.
--pageSize Optional. Combines with --export=intersections to set the export
page size. This will improve performance and stability based on the
data model.
--port <num> The port to connect to on the API server. Defaults to 443 with SSL or
80 without SSL.
--queueQueue this ETL job if another job is already running under this data
model.
--retryUploads Optional. Combines with --runTemplate to automatically retry
uploaded jobs that encounter issues.
--runChannel <channelId>Id of integrations channel to run.
--runTemplateRun the ETL template with the given id.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 13/29

<templateId>
--setError <msg> Set the job status to error with optional error message.
Requires: --jobId option.
--ssl Use SSL encryption to connect to the server (this is the default).
--stage  Load the files into the SQL staging area and await SQL transform.
--stageAndTransformLoad the files into the SQL staging area and await SQL transform.
--stageOnly Load the files into the SQL staging area.
--status Request status for the specified etlJob.
Requires:--jobId option.
--templateId <id> Specify a template ID to associate when creating a new job.
--transformComplete Signal to the server that SQL transform is complete and to start
loading from the SQL staging area.
Requires: --jobId option.
-u,--username <email> The username to use to access the API. This is the same username
you would use to log in to the vena application.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 14/29

--validateValidate the import files. This performs a dry run without saving
data, and sends back a list of validation results.
--venaTable Load the files into a Vena Table.
--verbose Show the server calls made while the command runs.
--version  Print the version of the cmdline tool.
--wait Wait for job to complete (or fail) before returning. Returns status
code 0 if the job was successful and non-zero if it failed. For jobs run
with --stage or
--stageAndTransform, this will only wait until the job has completed
the first step (reached IN_STAGING).
--waitFullyWait for job to fully complete (or fail) before returning. Returns
status code 0 if the job was successful and non-zero if it failed.
For jobs run with --stage or --stageAndTransform, this will wait until
the job has fully completed. Command Line - Login Requirements
Enter the command with all options on a single line.
User credentials can be either a username/password combination or an apiUser/apiKey
combination, not both.
For clients on vena.io, use the following host/port combination with SSL option:
 java -jar etl.jar -u=trainee1@venatraining.com -p=venapass02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 15/29

Application Tokens
If you are automating the ETL Command Line tool via a batch file, you may opt to use an
apiUser/apiKey combination. Since everything in the Command Line is stored in plain text, you
may not want to use your vena.io login credentials as they will remain a part of the batch file.
However, it should be noted that you cannot access templates with an apiUser/ apiKey
combination, although you can still load and retrieve data from the cube.
To use an apiUser/apiKey instead of standard username/password credentials, create an
Application Token. To do this follow the instructions below:
1. Navigate to the Admin tab.
2. Navigate to the Application Tokens page.
3. Select Add Application Token.
4. Enter the name for your new Application Token.
5. Select Save to create the new token.
02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 16/29

6. Select the newly created Application Token to highlight it.
7. Select Show Token. This opens a pop-up with the apiUser and apiKey for the selected token.
You will use these credentials in the Command Line with the --apiUser and --apiKey
arguments in place of --username and --password.
8. Copy the tokens.
9. Select OK when you’re done.
02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 17/29

Importing Data
Specify a Data Model (by Name or ID), and one or more .csv files. For example:
java -jar etl.jar --modelName "TestModel"
 --file="model.csv;hierarchy"
You can send in more than one .csvfile by adding additional --file options.
Files can even be of different types.
For example, you could send in a "hierarchy" file followed by an "intersection" file to load
data into the model you just created.
When you send in multiple files they will be loaded in sequence.
For more information see the ETL Jobs.
You can load files in CSV (comma delimited format) or TDF (tab delimited format).
Use bulkInsertwhen loading large files into the data model for improved performance. Use
the flagbulkInsert=true to leverage bulk insert. Warning: Bulk Insert does not take into
account quotations that are typically used to surround text values in a CSV format. Therefore,
use TDF format for load files in this situation.
Caution
Bulk Insert does not take into account quotations that are typically used to surround
text values in a CSV format. Therefore, use TDF format for load files in this situation.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 18/29

Example:
java -jar etl.jar -u=trainee1@venatraining.com -p=venapass
--createModel="ETL Tool Model 11"
 --file=model.csv;intersections;bulkInsert=true
Importing Data into a Vena Table
Specify a Vena Table Name, File Name, Job Name, and Data Model (by Name or ID).
To import data into a Vena Table use the --venaTable command along with the --jobName and --
file command to run a new ETLFileToVenaTable job.
For example:
java -jar etl.jar -u=trainee1@venatraining.com -p=venapass --jobName
"Loading file to VenaTable" --file
"venaTableData.csv;table=VenaTablePersistentData"  --venaTable --
modelId "634162677727363072"
Create Model Hierarchies (Command)
To create this model on the server and supposing the source data file is model.csv, follow these
steps:02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 19/29

java -jar etl.jar -u="trainee1@venatraining.com"
-p="venapass" --createModel="Model123" --file=model.csv;hierarchy
Modify a Hierarchy (Cmd)
To modify a Hierarchy, one can use the same file format with an extra_Cmd column on the right
indicating whether to add or remove a Parent Child Relationship from the model.
java -jar etl.jar -Username="johnsmith" --Password="venapass" --modelName "Model1123"
--file=change-model.csv;hierarchy
Instead of specifying that a new model should be created with the--createModel flag, we
specified the name of the model to modify using the --modelName flag.
Intersection Values (Command)
The command to submit this would be:
java -jar etl.jar -Username=johnsmith --Password=venapass --modelId=79035143750156288 --
file='intersections.csv;intersections'
 Note02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 20/29

Clearing Intersection Values during Import
There is an option to clear intersection values from specified slices of the cube as part of an ETL
import data load. Any existing data in the specified slice not being updated via the import file will
be cleared. Otherwise, the existing data will be overwritten with the new data that is being
imported.
To perform this option, specify the slices as a sub-option of the file command:
--file=intersections.csv;intersections;<keyword>
Where <keyword> corresponds to one of the supported clear slices method keywords. There are
two supported keywords: clearSlices and clearSlicesByDimNums.
Clear Slices by Expression
The clearslices keyword allows you to define the slices to clear using Model Query Language
expressions.
To do this, you would specify the slices as such:
When file names, user names or passwords do not include a space, you do not
need to use double quotes to set the parameter.
To import Intersection Values, a Data Model with the given Dimensions must
already exist.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 21/29

--clearSlices=<expression>
where <expression> is a string that specifies one slice or more than one slice separated by a
comma using model slice expression language. For more information on expression syntax,
please refer to the Model Query Language section.
Examples:
This command defines one slice to be cleared: {Ottawa, Squirrel}
--clearSlices="dimension('City':'Ottawa') dimension('Animal':'Squirrel')”
This command defines two slices to be cleared: {Ottawa, Squirrel} and {Toronto, Squirrel}
--clearSlices="dimension('City':'Ottawa')
dimension('Animal':'Squirrel'),
dimension('City':'Toronto') dimension('Animal':'Squirrel')”
Clear Slices by Dimension
The clearslicesByDimNums keyword allows you to define the slices to clear by referencing a
series of dimension numbers in the destination.
To do this, you would specify the slices as such:
--clearSlicesByDimNums=<numbers>02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 22/29

where <numbers>is a string that specifies one or more dimension numbers separated by a
comma.
Examples:
This command defines the slices to be cleared as all those slices present in the import that
correspond to the first and third dimensions:
--clearSlicesByDimNums="1,3”
For example, if your staging table contained the following rows and you used the command
above, the slices specified to be cleared would be {Ottawa, 2014}, {Toronto, 2014} and
{Waterloo, 2015}.
_dim1_member_dim2_member_dim3_member_value_etl_id
Ottawa Squirrel 2014 20
Toronto Squirrel 2014 30
Waterloo Rabbit 2015 40
When you specify a slice to clear, the behavior follows a regular load of intersections, with the
exception that any values in the specified slice(s) that are not found in staging will be cleared.
As such:
If there is a new intersection in the out values staging table, it is loaded to the cube.
If there is an existing intersection in the table with an unchanged value, no change occurs.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 23/29

If there is an existing intersection in the table with a changed value, the value is updated in
the cube.
If there are any intersections in the specified slice(s) of the cube that do not exist in the table,
their values will be cleared.
Exporting Intersection Values (Data) from the Cube
There are two destinations that a data export can be directed to. There is an export from the
data model to a csv file or to a staging table.
Exporting to a csv file:
java -jar etl.jar --export <type> --exportQuery <where clause> --exportToFile <File name>
Exporting to a table in the SQL Staging Environment:
 Note
The --file suboption clearSlices can only be used for ETL imports from file to cube.
To use the clearSlices feature for staging operations, there is a stand-alone --
clearSlices option. See the Clearing Intersection Values with Staging section.
This feature only clears the values of the intersections in the specified slice(s) and
does not delete line item details.02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 24/29

 java -jar etl.jar --export <type> --exportQuery <where clause> --exportToTable <table name>
Query Parameters
ETL imports and exports from the command line may be supplied with a query to filter the
resulting intersections, lids, hierarchies or attributes.
java -jar etl.jar --export intersections --exportToFile "<file name>" --exportQuery "<model slice
expression>"
intersections may be replaced with lids for importing/exporting LIDs. For more information, see
the Model Slice Query Language section.
Imports/exports with the types hierarchy, attributes, or user_defined use the --
exportWhere command with the Hibernate Query Languagesyntax.
Deleting Intersections
This feature uses the Model Slice Query Language to decide which intersections to delete. The
delete type can be one of: {intersections, values, lids}. Choosing intersections means both values
as well as any attached line item details will be deleted. Choosing values means only the values
will be cleared and choosing lids means only the line item details will be deleted.
java -jar etl.jar --delete <type> intersections --deleteQuery <expression>;
Syntax example:02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 25/29

 
 
 java -jar etl.jar -u=USERNAME -p=PASSWORD --modelName="MODELNAME" --delete intersections --d
"dimension('Dimension1':'Member-To-Delete') dimension('Dimension2': 'Member-To-Delete')"
Example 1:
Removing data from data model called Budget, where the year is 2014, period is 009 and the
scenario is Budget:
java -jar etl.jar -u=admin@training.com -p=1abcdefg --modelName="Budget" -delete intersectio
"dimension('Year':'2014') dimension('Period': '009') dimension('Scenario': 'Budget')"
Running an Integration Channel
To run an integrations channel that has been configured and validated from the command line,
the following command can be used, where channelId is the ID of the integrations channel:
-runChannel <channelId>
The channel ID can be found in the page's URL after /channels/.
Example:
java -jar etl.jar -u=admin@training.com -p=password --modelName="Budget" --runChannel 12492802/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 26/29

Running an ETL Template
To run an ETL Template that has been created in the ETL web interface from the command line,
use this command, wheretemplateId is the ID of the ETL template:
--runTemplate <templateId>
The channel ID can be found in the top right corner of the ETL Template Manager after selecting
the Edit button.
If the ETL template specified has one or more steps which require files, these can be supplied
using the--filecommand, in the order that they should be used in the target template.
Note that --runTemplate cannot be combined with any of the following options:
templateId
clearSlices
clearSlicesByDimNums
loadSteps
runChannel
export
exportToTable
exportFromTable
exportToFile
exportWhere
exportQuery
delete
deleteQuery
jobName02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 27/29

 jobId
cancel
loadFromStaging
stage
stageAndTransform
venaTable
Example:
java -jar etl.jar -u=admin@training.com -p=password --modelName="Budget" --runTemplate 48709
Was this article helpful?
6 out of 6 found this helpful
Related articles
Reference: ETL Guide - 1 - Overview
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 4 - Query LanguagesRecently viewed articles
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 1 - Overview02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 28/29

How-To: Importing Data to Vena with
Microsoft Power Automate Connector
Reference: ETL Guide - 6- Using Staging DataTroubleshooting: No Values Generate for a
Reporting Currency
Troubleshooting: Calc Script Using
.BottomLevel() and .Exclude() in a Tuple Not
Working Properly
Troubleshooting: Calc Is Not Triggering or
Calculating After Data Load or Import
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:42 Reference: ETL Guide - 3 - Command Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028227571-Reference-ETL-Guide-3-Command-Line-ETL 29/29
