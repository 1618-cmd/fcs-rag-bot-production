# (How to)   Vena Integration  Part 6 – Channels & Field Mappings

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
ETL Jobs
Data Querying
Vena TablesHow-to: Vena Integration: Part 6 –
Channels & Field Mappings
About this series
This series is all about how to use Vena Integrations. You are in Part 6, which outlines what channels and
field mappings are and how to manage them.
Vena Integration is a large and complex tool, and it continues to grow. We've broken down the information in
this series into manageable parts, each focusing on a specific area of the Integration tool and its related
concepts.
Vena Support Team
Updated 1 month ago
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 1/55

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
How-to: Vena Integration: Part 5 -
DestinationsThis series was designed to be read in order. If you don't have any previous experience with the Integration
tool, we recommend that you follow this approach, starting with Part 1. But if you are familiar with
Integration, feel free to explore around for what you need.
Part 1: Feature Overview
Part 2: Internal Sources
Part 3: External Sources – Data Feeds & Connections
Part 4: External Sources – Import and Export API
Part 5: Destinations
Part 6: Channels & Field Mappings –you are here
Video
Check out a video of this article's content.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 2/55

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
Product UpdatesVena Integration Part 6: Channels & Field Mappings Vena Integration Part 6: Channels & Field Mappings
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application Permissionsfor
authorizations.
If Data Permissions are set up in your environment, you will also need the appropriate permissions for the
data that you are working with.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 3/55

Table of contents
About channels & field mappings
How to
Creating a channel
Configuring and running a channel
Overview: Channel Details interface
Steps to configure a channel
Running a channel again
Modifying a channel setup
Renaming a channel
Deleting a channel
Duplicate a channel
Reference Guide: Field Mappings
About channels & field mappings
Remember the basics of Integration involve the following:
1. Creating a source.
2. Linking that source to a destination using a channel.
The Channels interface is the primary component of the Integration tool. Each data integration is represented
by a channel, where you define the data source, its destination and the transformations required for the
incoming data to be mapped to the destination.
Data transformation enables compatibility with a destination that would not otherwise fit. The Integration tool
provides various prebuilt data transformation tools for this purpose, known as Field Mappings. You deploy
field mappings with a simple drag-and-drop interface, in many cases eliminating the need for complicated
SQL staging tables.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 4/55

There are a few types of field mappings available:
Direct
Formula
Split Formula
Scripted
Table
Fixed
Unpivoting
Learn more about field mapping types in the Field Mapping Reference Guide.
How to
Creating a channel
With sources and destinations set up, you can start your data integration. Begin by creating a dedicated
channel for the new integration.
1. Navigate to the Modeler tab.
2. Select Data Transformations.
3. Select Channels.
4. Select the Create button in the top right.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 5/55

5. In the menu, select Channel to open the New Channel window.
6. Enter a name in the Channel Name field to help you identify your new channel, then select Save.
7. Your channel is added to the list on the Channels page, and you’ll be directed to the Channel Details
interface to configure this new channel.
Configuring and running a channel
Configuring a channel involves specifying all the details of the data integration task the channel will represent.
After configuration, the channel is ready to run.
Overview: Channel Details interface
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 6/55

ASource selection
and detailsChoose the source for this integration. Editable at any time.
BSource fields
columnCorresponding data fields for the selected source appear here, where they may be
connected to the destination fields column (E) with field mappings (C).
Note: Not all fields need to be used; unused source fields are ignored by the
Integration tool.
CField mappings
areaField mapping blocks are placed here to connect source fields (A) to destination fields
(E).
DDestination
selection and
detailsChoose the destination for this integration. Editable at any time. 05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 7/55

EDestination fields
columnCorresponding data fields for the selected destination appear here, where they may
be connected to the source fields column (A) with field mappings (C).
Note: Unlike source fields, most connections must be made to each destination,
either to a source field or a fixed value mapping.  Destination fields that must be
connected are marked with an asterisk.
FChannel control
panelValidate – Check your channel setup for errors.
Preview – View how incoming data will appear in your database after the integration
has been completed.
Run – Begin the integration job.
Clear Mappings – Delete all field mappings.
Map by Name – Connects all matching fields by direct mapping.
Use sampled data – Runs the job using data sampled from your source instead of a
live feed; useful for testing purposes.
Fetch Sample – Pulls in a sample of data from the selected source.
GClose button Select to exit Channel Details and return to the Channels tab. Your work is
automatically saved.
Steps to set up a channel
The basic process for setting up a channel consists of six steps:
1. Add a source.
2. Add a destination.
3. Map source fields to destination fields.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 8/55

4. Validate the channel setup.
5. Preview results (optional).
6. Run the channel and integrate data.
Let’s go over these steps in detail.
Step 1: Add a source
1. Ensure your source is set up and in the Channels list as outlined in Part 2 of this series.
2. On the Channel Details page, select + Add Source.
3. In the source selection window, select the source you want to use then the Select button.
Note
Once channels are established, they remain persistent. When you need to perform the same data
integration again, you can simply execute the previously configured channel or make any
necessary adjustments.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 9/55

You can also select Preview to view a small sample of data pulled in by the selected source.
4. The selection window will close, and you’ll return to the main Channel Details page. The Integration tool
automatically detects and displays incoming data fields under the Source fields column.
Step 2: Add a destination
1. Select + Add destination. To use an existing destination then choose Select Existing Destination. To
create a new destination, select the destination type you want to use. Learn more about destination
types.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 10/55

2. In the destination selection menu, select the Destination you want to use then the Select button.
3. The selection window closes, and you’ll return to the Channel Details page. The destination data fields will
be displayed under the Destination Fields column.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 11/55

Step 3: Map source fields to destination fields
Next, you'll connect your source fields to your destination fields with field mappings. This section outlines a
few basic options. For detailed instructions on all field mapping types, refer to the Field Mappings
Reference Guide.
Simple direct mapping
The simplest field method is a drag-and-drop connection between a source and a destination.
1. Select a source field on its connection node and hold, then drag the arrow that appears to the desired
destination.
2. A direct mapping block appears in the Field Mappings area, with one arrow leading to it from the source
and another to the destination.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 12/55

Independent mapping blocks
You can also create field mapping blocks independently, then connect them to source fields and/or
destination fields later. You must use this method to create types other than Direct Mappings.
Note
You can click-and-drag the field mapping blocks to arrange them around the Field Mapping
area as needed.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 13/55

1. Right-click anywhere in the Field Mappings area to open the menu and select the Field Mapping type you
wish to create.
2. Double-click the mapping block to configure its options, then select Save.
3. Drag-and-drop between the connection nodes to create arrows connecting the source fields, field mapping
block and destination. You may move the field mapping block around the Field Mapping area to a new
position.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 14/55

Chained mappings
To perform complex transformations, connect multiple field mapping blocks in sequence (called chain
mappings). Each step uses output from the one before.
For example, include a currency conversion by chaining a table mapping (for an exchange rate lookup)
followed by a formula mapping to calculate the amount in the target currency.
Note05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 15/55

1. Create at least two field mapping blocks and configure their options as needed. Select and hold the field
mapping block to position it around the field mapping area.
2. To chain field mappings, connect a source field to the first field mapping block in the chair with the same
drag-and-drop method as the previous sections. Then, connect that field mapping block to the next one,
and so on.
While you can have multiple chains per channel, there is a maximum of 10 field mapping blocks
per chain sequence.
All types of field mapping blocks may be chained except Unpivoting Mappings.
Chains do not need to be continuous. You can cross-link chains or link into and out of chains
to/from other field mappings, as needed.
Use the Mapping Output tab in the Preview feature to see (and troubleshoot) the output of your
chained mappings.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 16/55

Step 4: Validate
Note
Using the same Vena database as both source and destination is recommended only for experts. If
they overlap, data just written to the destination can be re-processed as part of the source,
causing unexpected outputs in jobs with transformations.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 17/55

At any time in your setup, use the Validate tool to determine what steps you still need to complete to set up
the channel. You do not have to wait until you’re finished connecting all required sources and dimensions.
1. Select Validate in the Channel Control Panel.
Note: If you’re using an external source that has not been set up as a Connection with Vena, you’ll be
prompted to enter a password to authorize the external system. Continue by selecting the blue Validate
button in the password prompt window after entering your password. Learn more about external
connections.
2. The Validation tool will check and highlight any problems with your mappings. In the example below, there
are problems with some of the destination fields, as well as one of the field mappings.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 18/55

3. Select Details in the red warning banner above the Channel Control Panel.
4. A pop-up will appear containing detailed descriptions of the problems the Validation tool identified.
5. You can also hover your pointer over each of the error icons (
) in the mapping area to see details
about each specific issue:
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 19/55

6. Resolve any issues, then select Validate again. Repeat steps 1-5 until no more problems are reported.
Once validation is passed, a corresponding message will be displayed above the Channel Control Panel.
Step 5: Preview
Before you run the channel, it is recommended that you check the output to ensure it meets your
expectations.
Note
The best practice is to validate early and often. As you set up a channel, you can use the Validation
tool at any time (not just when you have finished your setup), as it is designed to provide ongoing
guidance on the steps needed to successfully complete your channel setup.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 20/55

1. Select Preview in the Channel Control Panel.
2. This opens a pop-up with a preview of the first ten lines of input and output data.
The input data is displayed by default.
3. Select the tabs at the top of the window to navigate between views:05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 21/55

Mapping Output displays the direct output of each field mapping.
Output displays the ultimate value that will be written to the destination.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 22/55

Warnings display any important information you should be aware of before proceeding.
4. You can also export the output data to a CSV file:
Select Export output to CSV to download a CSV file containing all of the output rows that would be
produced by running the channel. This feature is useful for seeing the complete output of your channel
without having to commit to writing it to a destination.
Select Export mapping output to CSV to download a CSV file containing all of the output rows that
would be produced by the field mappings in the channel. This feature is useful for validating if the data
is being transformed correctly by the mappings or to spot any issues.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 23/55

5. When you are finished with the preview, select Close.
Using sampled data for previews
Use the Preview tool with the Fetch Sample feature to avoid pulling live data every time you preview your
channel setup.
1. Below the Channel Control Panel, select Fetch Sample to pull in a sample of the first ten lines of data from
your selected source.
Note: Using Fetch Sample with an external source type for which no authorization is in place will prompt
you for your password.
2. After you select Fetch Sample, the box next to Use sampled data will be checked by default:
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 24/55

To turn this option off and resume pulling live data when using Preview, uncheck Use sampled data. You
can select Fetch Sample again at any time to retrieve a fresh sample.
Step 6: Run the Integration
1. Once you are satisfied with your integration set up, select Run in the Channel Control Panel.
2. If there is a problem with your channel setup and the job cannot be run, an error message appears,
outlining the problem.
3. If this happens, select OK to return to the Channel Details page and resolve the issue. Then select Run to
try again. 05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 25/55

4. Repeat steps 2-3 until a message box appears above the Channel Control Panel to indicate that the
Integration job has been added to the ETL queue.
5. Select Jobs in this message box to go directly to the History tab and see the status of the Integration job or
select History from the sidebar.
Running a channel again
Channel setups are persistent, so you can run them as often as needed. You can also schedule them for
automatic runs with the ETL Scheduler. Learn more about automatically running ETL templates on a
schedule.
To run an existing channel again:
1. Navigate to the Modeler tab, then Data Transformations > Channels.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 26/55

2. Select the channel to open the Channel Details page.
3. Select Run in the Channel Control Panel. The channel will run and the Integration job will be added to the
list in the History tab.
Modifying a channel setup
You can modify a channel at any time. Changes are saved automatically, and we recommend that you Verify
and Preview your new setup before selecting Run.
1. Select the channel to open the Channel Details page.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 27/55

2. Make your changes using the Channel Details interface. You can change any aspect of the channel,
including the source, destination and field mappings.
To change a source, select Change in the Source column.
To change a destination, select Change in the Destination column.
Note: Any destination fields previously connected to field mappings will remain mapped, but any
mappings that could not be recreated with the new destination fields will be highlighted.
To change a field mapping:05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 28/55

1. Rearrange by dragging-and-dropping the field mapping blocks.
2. Delete field mappings by selecting the X on the field mapping block.
3. To modify a field mapping block, double-click it to open its options menu.
4. Add a new field mapping by right-clicking anywhere in the Field Mappings area to open the list of
mapping block options.
Renaming a channel
You can rename a channel at any time.
1. Navigate to the Modeler tab, then select Data Transformations > Channels.
2. Right-click or select the vertical ellipses (
) in line with the channel name to open its options menu, then
select Rename.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 29/55

3. Enter the new name, then press Enter on your keyboard to save.
Deleting a channel
You can delete a channel as long as it isn’t being used as a source in a different channel. In this case, you’ll see
a warning message, and you must remove this channel as a source before deleting it.
1. Navigate to the Modeler tab, then select Data Transformations > Channels.
2. Right-click or select the vertical ellipses (
) in line with the channel name to open its options menu, then
select Delete.
3. A pop-up will appear asking if you are sure you want to delete the channel. Select Delete to proceed.
4. You will be returned to the Channels tab, where the channel will immediately be removed from the list.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 30/55

Duplicating a channel
The Duplicate feature allows you to build on your previous work efforts and copy Vena channels quickly and
easily.
1. Navigate to the Modeler tab, then select Data Transformations > Channels.
2. Right-click or select the vertical ellipses (
) in line with the channel name to open its options menu, then
select Duplicate.
3. Your duplicated channel will appear in the row below the original channel. If you want to rename your
duplicate channel, select the vertical ellipses at the end of the duplicate channel row and select Rename
from the drop-down menu options.
Note
Duplicate is only available for channels; you cannot duplicate destinations, folders or sources.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 31/55

4. Once you have copied your channel, you can click on the new channel to view it. You'll see that the source,
destination and channel mappings have all been copied from the original channel.

Reference Guide: Field Mapping Types
This guide explains each field mapping type in the Integration tool and how to configure them.
Field mapping types serve specific purposes and appear in channels as grey oval blocks with light blue
connection nodes and unique symbols. To configure a field mapping, double-click its block to open options.
Settings apply only to the selected block; if you use several blocks of the same type, configure each
individually.
Direct
Formula
Split Formula
Scripted
Table
Fixed
Unpivoting
Direct Mapping
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 32/55

Use direct mapping to transfer data from a source field to a destination field without changes—input and
output remain identical. This is the default mapping type when connecting fields.
To edit a direct mapping, double-click its block in the Field Mappings area of Channel Details. This opens a pop-
up with options for that specific mapping.
Available options include:05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 33/55

Name: Name the mapping block for easy identification.
Default Value: Enter a value to use if the source field is blank; otherwise, it remains blank.
Remove leading and trailing whitespace: Removes extra spaces from the source field if checked
(default). Uncheck to keep whitespace.
Formula Mapping
Formula mappings use Excel formulas to transform incoming source data before writing it to the destination
field.
Double-click on a formula mapping block to open a pop-up where you can enter a name for your mapping
and the formula.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 34/55

For proper referencing in the formula, the correct names of any connected source fields are listed under
Available inputs. Therefore, it is recommended to connect the relevant source fields to the formula mapping
block before configuring it.
Not all Excel functions can be used with formula mappings. Currently, the following functions are supported:
ABS
ACOS
ACOSH
ADDRESS
AND
ASIN
ASINH
ATAN
ATAN2COUNTBLANK
COUNTIF
DATE
DATEDIF
DATEVALUE
DAY
DAYS360
DEC2BIN
DEC2HEXHOUR
HYPERLINK
IF
IFERROR
IFNA
IFS
IMAGINARY
IMREAL
INDEXLOOKUP
LOWER
MATCH
MAX
MAXA
MAXIFS
MEDIAN
MID
MINPOWER
PPMT
PRODUCT
PROPER
PV
QUOTIENT
RADIANS
RAND
RANDBETWEENSUM
SUMIF
SUMIFS
SUMPRODUCT
SUMSQ
SUMX2MY2
SUMX2PY2
SUMXMY2
T05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 35/55

ATANH
AVEDEV
AVERAGE
AVERAGEIF
AVERAGEIFS
BIN2DEC
CEILING
CELL
CHAR
CHOOSE
CLEAN
CODE
COLUMN
COLUMNS
COMBIN
COMPLEX
CONCAT
CONCATENATE
COS
COSH
COUNT
COUNTADEGREES
DELTA
DEVSQ
DGET
DMIN
DOLLAR
EDATE
EOMONTH
ERROR_TYPE
EVEN
EXACT
EXP
FACT
FACTDOUBLE
FALSE
FIND
FIXED
FLOOR
FREQUENCY
FV
HEX2DEC
HLOOKUPINDIRECT
INT
INTERCEPT
IPMT
IRR
ISBLANK
ISERR
ISERROR
ISEVEN
ISLOGICAL
ISNA
ISNONTEXT
ISNUMBER
ISODD
ISREF
ISTEXT
LARGE
LEFT
LEN
LN
LOG
LOG10MINA
MINIFS
MINUTE
MIRR
MOD
MODE
MONTH
MROUND
NA
NETWORKDAYS
NOT
NOW
NPER
NPV
NUMBERVALUE
OCT2DEC
ODD
OR
PERCENTILE
PI
PMT
POISSONRANK
RANK_EQ
RATE
REPLACE
REPT
RIGHT
ROMAN
ROUND
ROUNDDOWN
ROUNDUP
SEARCH
SECOND
SIGN
SIN
SINH
SLOPE
SMALL
SQRT
STDEV
SUBSTITUTESUBTOTALTAN
TANH
TEXT
TIME
TODAY
TRANSPOSE
TRIM
TRUE
TRUNC
UPPER
VALUE
VAR
VARP
VLOOKUP
WEEKDAY
WEEKNUM
WORKDAY
XOR
YEAR
YEARFRAC
Notes on Formula Mapping
In the Excel or Javascript transformation step of channels, if you use the keyword "Ignore", it will
ignore that row.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 36/55

Split Formula Mapping
If you are splitting segments of data with a formula mapping, consider using Vena’s custom Split Functions.
These formulas are useful for separating segments such as the year and period from a date or an account
code from its alias description.
There are three custom Split Functions available:
SPLIT_LEFT: Splits at the first occurrence of a delimiter.
SPLIT_RIGHT: Splits at the last occurrence of a delimiter.
SPLIT_EVERY: Splits at every occurrence of a delimiter.
The syntax for the formula is:
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 37/55

=SPLIT_FUNCTION(input[‘Column name’], delimiter, index, second delimiter, third delimiter,...)
Example
Data Formula Output
1000 - Cash=SPLIT_LEFT(input[‘Data’], “-”, 0)  1000
1000 - Cash=SPLIT_LEFT(input[‘Data’], “-”, 1)  Cash
1000 - Cash=SPLIT_RIGHT(input[‘Data’], “-”, 0) Cash
1001.1105.785=SPLIT_EVERY(input[‘Data’], “.”, 0) 1001
1001.1105.785=SPLIT_EVERY(input[‘Data’], “.”, 1) 1105
1001.1105.785=SPLIT_EVERY(input[‘Data’], “.”, 2) 785
1300.56-236 = SPLIT_EVERY(input[‘Data’], “.”, 0, ”-”) 1300
Scripted Mapping
Note
The second and third delimiters are optional for Split Functions.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 38/55

Scripted mappings use JavaScript to transform incoming source data before writing it to the destination field.
Double-clicking on a scripted mapping block in the Field Mappings area of the Channel Details view opens a
pop-up allowing you to enter a name for your script as well as the code itself.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 39/55

To help you reference them in the script, the correct name(s) for any connected source fields are listed under
Available inputs. For this reason, it is recommended that you connect the relevant source fields to the scripted
mapping block before configuring it.
Note05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 40/55

Table Mapping
Table mappings let you use values from source fields to look up related data in a reference table and write the
result to a destination field.
When a value from one or more source fields matches a row in the lookup table, the mapping takes the
corresponding output value from another column and writes it to the destination field.
For example, if your lookup table has a left column for inputs and a right column for outputs, you can specify
which columns to use for searching and for returning results:
InputOutput
RedAlpha
BlueBravo
In the Excel or JavaScript transformation step of channels, if you use the keyword “Ignore”, it will
ignore that row.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 41/55

GreenCharlie
YellowDelta
PurpleEcho
If the source value is Green, the table mapping finds Green in the input column, locates the same row in the
output column and then writes Charlie to the destination. This links input Green to its mapped value Charlie as
defined in the lookup table.
Lookup tables may have just two columns or multiple columns for mapping several source fields. When using
multiple columns, specify which columns correspond to each source field. For example, adding a third column
to the previous table allows for more complex mappings.
Input 1Input 2Output
CircleRedAlpha
SquareBlueBravo
TriangleGreenCharlie
CircleYellowDelta
SquarePurpleEcho
For this example, we will configure the table mapping to look for values coming from the source field called
Shapes in the Input 1 column, and values coming from the source field Colors in the Input 2 column.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 42/55

If the incoming value from Shapes is Square, and the one from Colors is Blue, the table mapping will check if it
can find those values in the lookup table in the columns we specified. It finds Square on both the second and
fifth rows of the Input 1 column, but Blue only on the second row of the Input 2 column:
Input 1Input 2Output
CircleRedAlpha
SquareBlueBravo
TriangleGreenCharlie
CircleYellowDelta
SquarePurpleEcho
Both input values need to be found in the same row to result in a match. So, of these two options, only the
second row [Square, Blue] is considered a match, while the fifth row [Square, Purple] will be disregarded. The
value found on the second row of the output column is Bravo, so this is the value that will be written to the
destination field.
Note
If multiple matches in the lookup table produce identical outputs, the output value will be written
as usual. If the outputs differ, an error will be reported.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 43/55

Before you can set up a table mapping block, the mapping table you intend to use must already exist as a
source under the Sources tab. Any source type may be used as a mapping table, as the data in each source
can be represented as a table (the source fields are essentially the same as column headings). Alternatively,
you can also use an existing channel as the mapping table.
To configure a table mapping:
1. Double-click on a table mapping block to open the configuration pop-up.
2. You must first connect a table mapping block to at least one source field as well as a destination field
before configuring it, otherwise the error message below appears.
3. Enter a name for this table mapping block in the Name field.
4. Using the drop-down menu under Table Source, choose the source that you would like to use as a mapping
table for this mapping block.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 44/55

5. After you select the source table, select Preview Table Source to see a preview of the selected mapping
table.
6. If you want to change the source table at this point, select a new one from the drop-down and then select
Detect Fields.
7. Once you select the source table, additional fields appear to configure the mapping table. These include
Inputs for source fields providing search values and Output for destination fields where the table values will
be written.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 45/55

8. Use the drop-down menu(s) under Inputs to select the column(s) of the mapping table that contains the
values you want to search for.
9. In the drop-down menu under Output, select the column that has the values you want to write to the
destination field.
10. Choose the Default Behavior that the table mapping will use when it is unable to find a value from the
source field in the mapping table. The available options are:
1. Ignore Row (Default): If the mapping table cannot find a match for the incoming value(s), it will ignore
the entire row of incoming data from the source (i.e., the row consisting of values from all connected
source fields in the channel).
2. Default Value: If no match is found, a specified default value will be written to the destination field
instead. Use the text field to enter the default value you want to use.
3. Default Field: If no match is found, the value from a specified source field will be written to the
destination field instead. You can choose any source field for this purpose, not just those connected to
the table mapping block. Use the drop-down menu to choose the desired default field.
4. Blank Value: If no match is found, no value will be written to the destination field (i.e., it will be left
blank).
5. Error: If no match is found, no value will be written and an error message will be shown.
11. When you have finished configuring the table mapping, select Save to save your changes and close the
configuration window.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 46/55

Fixed Mapping
Fixed mappings write a specified value to a destination field, requiring no source field. These blocks have one
connection node that connects only to destination fields.
Double-clicking a fixed mapping block in the Field Mappings area of the Channel Details view opens a pop-up to
name the block and set the fixed value for the destination:
Note
When you create a table mapping block, the selected lookup table cannot exceed 1 million cells of
data in size (e.g., 100 columns by 10,000 rows, or any other combination that totals a million cells).05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 47/55

If you do not specify a value for a fixed mapping block, it will default to writing a blank (null) to the destination
field.
Unpivoting Mapping
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 48/55

Unpivoting mappings are intended for situations where your incoming data has multiple values on the same
table row, and you want to write all (or some) of these values to your database. This process involves
reconfiguring the incoming data so that each value is in its own row and therefore has a full set of dimensions
to form an intersection. In other words, working with data formatted like this means 'rotating' every incoming
row so that several new rows are formed from it, one for each of the distinct values that you want to save to
individual intersections. The unpivoting mapping performs this operation automatically.
For example, imagine a source which contains billable hours for a number of employees, broken down by
month. Part of the incoming data might look like this:
NameRegionJanFebMarApr
John SmithUS East14213715196
Jane DoeUS Central128145139165
Joe BloggsCA East101128143154
To record each of those figures in your database as a separate intersection value, the table needs to be
unpivoted to place each value in its own row.
Unpivoting the data from the above table that relates to John Smith looks like this:
NameRegionMonthBillable Hours
John SmithUS EastJan 142
John SmithUS EastFeb 137
John SmithUS EastMar 15105/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 49/55

John SmithUS EastApr 96
Unpivoting converts one row from the input table into four rows, making the data ready for database
integration. This on-the-fly transformation simplifies working with source data without needing it to be
preformatted.
To configure an unpivoting mapping:05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 50/55

1. Double-click an unpivoting mapping block to open the configuration pop-up.
2. Enter a name for the unpivoting mapping into the Name field, and a name for the group of source fields
you want to unpivot into the Source Fields Groups Name field.
05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 51/55

3. Select the source fields you want to unpivot. Instead of dragging and connecting each field, simply multi-
select the desired fields under "Select fields to unpivot" in the unpivoting mapping configuration.
4. If desired, check the box for Ignore Blanks.
1. If it is checked: The unpivoted row with the missing value is discarded, and no change is made to the
intersection.
Note
The fields you select here do not have to be adjacent to one another. You can multi-select
individual fields by holding down the Ctrl key while selecting.05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 52/55

2. If it is unchecked: The unpivoted row with the missing value is included, and a blank/null value is
written to the intersection.
5. After you have selected the field(s) to unpivot, select Save to save your changes. (Disregard the Headings
and Values dropdowns for the moment; you will return and configure these later).
6. After selecting Save, the configuration pop-up will close, and the source fields that you selected in step 3
will be combined into a source fields group, represented by a green-colored source field. The source fields
group is also automatically connected to the unpivoting mapping:
7. Now, draw connections between the unpivoting mapping and the destination fields. You will need to
connect the unpivoting mapping to two destination fields; one representing the table heading for the
resulting rows (e.g., Months in the above example) and one for the values to be written.
8. Double-click the unpivoting mapping block to reopen the configuration pop-up. You should see that the
Headings and Values dropdown menus have changed from Select Column to the names of the destination
fields that you connected in the previous step.
Note
Unpivoting mapping is the only type of field mapping which can (and must) be connected to
multiple destination fields (always exactly two).05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 53/55

9. By default, the unpivoting mapping will assign the first destination field you connected to Headings, and
the second to Values. If this is incorrect, use the drop-down menus to switch the columns.
10. When you are satisfied with your setup, select Save to close the configuration window.
Additional Notes about the Unpivoting Mapping
You can only use one unpivoting mapping per channel.
Unpivoting mapping blocks can't be chained (connected in sequence with other mapping blocks).
Individual source fields connected to an unpivoting mapping can also be linked to other field mappings, if
required. Selecting source fields using the unpivoting mapping configuration window groups them
together, which prevents connecting individual source fields that are part of the group to other field
mappings later. Therefore, it is recommended to complete all other aspects of your channel setup before
configuring an unpivoting mapping.
Green-colored source fields groups will always appear below all other source fields.
The unpivoting process arranges the output rows from top to bottom in the same order as the columns
appeared from left to right in the input table (e.g., if the columns in the input table were Jan, Feb, Mar from
left to right, the resulting unpivoted rows would be ordered from top to bottom as Jan, Feb, Mar).
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-to: Vena Integration: Part 3 – External Sources –
Data Feeds & Connections
How-to: Vena Integration: Part 5 - DestinationsRecently viewed articles
How-to: Vena Integration: Part 5 - Destinations
How-to: Vena Integration: Part 4 – Import and Export05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 54/55

How-To: Bulk Attach/Detach Attributes and Filter by
Attributes
How-To: Using Vena Ad Hoc To View Your Data and
Make Simple Reports
How-To: Set Up a Business Central Connector and
Data FeedAPI
How-to: Vena Integration: Part 3 – External Sources –
Data Feeds & Connections
How-to: Vena Integration: Part 2 – Internal Sources
How-to: Vena Integration: Part 1 - Feature Overview
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 13:02 How-to: Vena Integration: Part 6 – Channels & Field Mappings – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38650833545485-How-to-Vena-Integration-Part-6-Channels-Field-Mappings 55/55
