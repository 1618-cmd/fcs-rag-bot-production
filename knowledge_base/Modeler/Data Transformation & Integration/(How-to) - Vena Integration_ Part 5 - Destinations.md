# (How to)   Vena Integration  Part 5   Destinations

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
ETL JobsHow-to: Vena Integration: Part 5 -
Destinations
About this series
This series is all about how to use Vena Integrations. You are in Part 5, which outlines what
destinations are and how to create and manage them.
Vena Support Team
Updated 1 month ago
05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 1/34

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
Part 2: Internal Sources
Part 3: External Sources – Data Feeds & Connections
Part 4: External Sources – Import and Export API
Part 5: Destinations – you are here
Part 6: Channels & Field Mappings
Video
Check out a video of this article's content.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 2/34

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
Product UpdatesVena Integration Part 5: Destinations Vena Integration Part 5: Destinations
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application
Permissionsfor authorizations.
If Data Permissionsare set up in your environment, you will also need the appropriate
permissions for the data that you are working with.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 3/34

Table of contents
About destinations
How to
Create a destination
Manage a destination
Editing a destination
Deleting a destination
Reference Guide: Destination Types
Internal destinations
Vena
Vena Table
Staging Table
Placeholder
Process
External destinations
Salesforce
About destinations
Remember the basics of Integration involve the following:
1. Creating a source.
2. Linking that source to a destination using a channel.
Destinations specify where the Integration tool sends your data. Most often, this is a Vena
database, but you can also configure destinations to write data to external systems supported05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 4/34

by Integration.
Supported Destination types:
Internal
Vena
Vena Table
Process
Placeholder
Staging Table
External
Salesforce
Learn more about the destination types in the Reference Guide.
How to
Creating a destination
As with sources, the basic procedure for creating a destination is the same regardless of the type
of destination. This section outlines the general steps to create any destination, while details
specific to each destination type are covered in the Reference Guide.
1. Navigate to the Modeler tab.
2. Select Data Transformations.
3. Select Channels.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 5/34

4. Select the Create button in the top right.
5. In the menu, select Destination to open the Create Destination pop-up.
6. Enter a name into the Destination Name field. Use the Destination Type drop-down to choose
your source.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 6/34

7. When you choose a destination type, additional fields appear that are specific to that type of
destination. For instructions on how to configure each destination type, refer to the
Reference Guide.
Note
Use Intersections and Intersection Members data types together. Intersection
Members ensures all referenced members in your source are present in the
destination's data model. If a channel with an Intersections destination runs
and members are missing, the integration job will fail.
To import intersection values when the source and destination structures
differ, set up two channels: one with the destination as Vena/Intersection05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 7/34

Members, and another as Vena/Intersections. Run the Intersection Members
channel first to create missing members, then run the Intersections channel.
Best practice: Create your field mapping logic in the Intersections channel.
Then, use the Intersections channel as the source for Intersection Members,
mapping fields directly. This keeps mapping logic in one place, making later
updates easier.
05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 8/34

8. When you have finished configuring the new destination, select Create. The newly created
destination will appear at the root level of the Channels tab.
Managing destinations
When you save a new destination, it appears in the Channels tab with a green icon. Right-click or
select the vertical ellipses (
)to view options for renaming, moving (into or out of a folder) or
deleting the destination.

Editing a destination
You may make changes to a destination (such as modifying its setup or renaming it) at any time.
1. On the Channels tab, navigate to the source you want to edit in the list (you can use the
filters to help find the desired destination).
05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 9/34

2. Select the destination name you want to modify.
3. This opens the Edit Destination window. Use the fields and drop-downs (as applicable) to
make the desired changes.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 10/34

4. Select Save when you have finished making changes. This closes the Edit Destination window
and you will be returned to Channels.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 11/34

Deleting a destination
You may delete a destination at any time, provided it is not currently used as part of a channel
setup.
1. On the Channels tab, select the vertical ellipses (
) for the destination in question.
2. Select Delete from the drop-down menu.
3. A confirmation window will ask if you are sure you want to delete the destination. Select
Delete to proceed.
4. You will be returned to the Channels tab, where the destination will immediately be removed
from the list.
Note
You can't delete destinations that are still being used as part of a channel setup.
You’ll see an error message if you attempt this.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 12/34

Reference Guide: Destination Types
This reference guide describes each of the different destination types available in the Integration
tool and provides details on how to configure each one. The available destination types are:
Internal
Vena
Vena Table
Staging Table
Placeholder
Process
External
Salesforce
Internal destinations
Vena
Vena destinations are used for Integration jobs where the target for incoming data is your
database. They can be set up for any of these six data types:
Alias Mapping: Used for importing Member Aliases (description) associated with Member
Names into your model.
Attributes: Used for importing dimension member attributes.
Hierarchy: Used for importing a data model hierarchy.
Intersections: Used for importing intersection values. This is the only data type with
additional options:05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 13/34

Slices To Clear & Slices To Clear by dimension. If you want incoming data to fully
replace existing data in the destination, use the Slices To Clear options. They add a
"clearing" step to remove old data that wasn't overwritten by new data. This method is
faster than deleting all data beforehand because it only removes the leftover
intersections.
Slices To Clear – Uses MQL expressions to specify data to clear. This option is static,
meaning the same data slices are always cleared when the channel is run, regardless
of the structure or content of incoming data. Write the MQL query in the text field to
activate.
Slices To Clear by dimension – Choose destination dimensions and their members to
define the slices to be cleared. Use checkboxes to select dimensions, which will appear
in the text field.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 14/34

Visit the Clear Slices article if you require more detailed instructions and best practices
for using Slices To Clear and Slices To Clear by dimension.
Warning
Aggregation Mode.  If your source has duplicate or conflicting values for the same
intersection, the destination can handle them in one of two ways. Choose the best option for
Using Slices To Clear and Slices To Clear by dimension will delete intersection
data from your Vena database. Before using this feature, please ensure you
understand the consequences and are confident that your setup will only
delete the intended data.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 15/34

your situation:
Unique (default) - Select this option to treat any duplicated intersection reference as an
error, stopping the Integration job if duplicates are found. Data up to the first duplicate
will still be saved to the database.
Sum - Select this option to combine multiple references to the same intersection. The tool
will sum the values of each reference and write the total to the destination intersection,
replacing any existing value. For instance, if an intersection is referenced three times with
values 15, 35, and 50, the total value of 100 will be written to the destination. This option
only works for numeric data; non-numeric data will be treated as zeros. If your source
contains non-numeric data, avoid using the Sum option.
Intersection members: Used in conjunction with Intersections channels. Ensures that the
members that define the intersections exist in the data model before values are written to
those intersections.
Line-Item Details: Used for importing Line-Item Details values and associated information.
Each of the available Vena data types has its own set of pre-defined destination fields. These are
displayed after you select the data model and data type in the Create Vena Destination window:05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 16/34

For reference information about the destination fields for each data type, refer to the ETL Guide.
Vena Table
For information on Vena Tables as a destination, including set up, visit this article.
Staging Table05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 17/34

Staging tables are typically used when the field mappings don't support the data transformation
you need. You can import data into a staging table and then use an ETL tool for further
processing before sending it on to the database.
The options for staging table destinations are like those for Vena destinations, referring to the
type of import you'll use with the staging table. The available data types are:
Hierarchy: Used for importing a data model hierarchy.
Attributes: Used for importing dimension member attributes.
Intersections: Used for importing intersection values. Shares the same format as Intersection
Members, so there is no separate data type for Intersection Members as there is with other
destinations.
Line-Item Details: Used for importing Line-Item Details values and associated information.
User Defined: Used for custom staging tables with user-defined column names.
Each of the available staging table data types has its own set of appropriate mandatory
destination fields (except for User Defined, where all the destination fields are custom created
based on the columns in the table). These are displayed after you select the data model and
data type in the Create Destination window:05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 18/34

Note05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 19/34

Staging tables will appear in the Staging Table drop-down for selection as your destination.
Placeholder
For complex transformations requiring multiple steps, use channel chaining. You can select a
previously configured channel as the source for a new one, enabling sequential data processing.
Intermediate channels still require a destination for the transformed data. Use the Placeholder
destination type to create custom destination fields, preparing data for the next channel in the
chain without setting up a Vena database.
If you haven't performed any ETL tasks requiring a staging table, you may not have
any. To create them, run an ETL Import job with a File To Stage or Cube To Stage step,
or an ETL Export job targeting a staging table.
Caution
With the introduction of chained field mappings, Placeholder destinations are no
longer needed in most cases. For simplicity, we recommend that you use chained
field mappings instead of Placeholder destinations wherever possible.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 20/34

You can create up to 50 destination fields. Select +Add Field (A) to create a custom field or
Populate From Source (B) to automatically create a set of destination fields to match the
source fields.
Process
Process destinations allow you to write stored process metadata directly to an existing process
within Vena, allowing for bulk modifications.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 21/34

Typically, modifying process parameters (like due dates) requires editing each task individually,
which is inefficient for large-scale changes. Instead, you can export process metadata to a Vena
database, update values (e.g., due dates, Smart Due Dates) like any intersection value and use
the Process destination type to write changes back to an existing process.
Key limitations for Process destinations:
Existing processes only: You can modify only processes that already exist. Creating new
processes or populating empty ones is not supported.
Strict data formatting: Data must match the precise format extracted with the Process
source type. Incorrectly formatted data will be rejected.
Limited fields: Only task due dates and user assignments (Owner/Support Worker/Watcher)
can be modified. Task names or task positions cannot be changed through Integration.
While any source type or field mapping can technically be used, these restrictions mean internal
sources (Data Model, Excel, CSV, SQL Staging and Process) and Direct Mapping field mappings
are most practical.
Recommended steps for bulk process updates:
1. Extract process metadata from an existing process to a Vena database.
2. Modify due dates or user assignments using Excel or a staging table.
3. Write the updated data to a Process destination using one-to-one Direct Mappings.
When creating a Process destination from the Channel Details page, you first enter a name (as an
identifier; it’s not used to specify the target process) and select Save. The following destination
fields will be created:05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 22/34

Process Path: The target process within Vena to be modified by connecting it to a source
field, which contains the process path (i.e., from process metadata extracted to a Vena
database, or a fixed mapping containing the process path as its value).
Values written to this field must be taken directly from a Process source and cannot be
modified.
Note
Creating a process destination from the Channels list (as opposed to the Channel
Details page), simply adds the name alongside the other listings. You’ll see the above
fields when adding the process destination in the Channel Details page.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 23/34

Task Path: The tasks and their location within the target process, as contained in the source.
Values written to this field must be taken directly from a Process source and cannot be
modified.
Measure: The type of metadata (i.e., due date, user, etc.).
Values written to this field must be taken directly from a Process source and cannot be
modified.
Value: The actual metadata value to be written (i.e., a date, time, time zone, email address,
etc.).
Can be modified for user assignments (email address of an existing user) and due
dates/smart due dates.
Command: Used similarly to ETL imports to define whether a change in the source should be
written to the target process or removed from it.
Can be modified: Acceptable values are + (add) or - (remove).
For Smart Due Dates, only + is accepted.
Incoming data is processed line-by-line, from top to bottom. In the case of conflicting lines
existing in the source data (e.g., two lines referencing the same process, task, measure,
value, etc., but with different commands), the last-processed line will take precedence.
Modifying Due Dates with the Process Destination
The Process Destination is mainly used to bulk update task due dates. To set due dates via
Integration, ensure they have the correct measure and format based on their type
(standard/fixed or smart/relative).
For both types, setting the value under the Command column to + will set the due date, while -
will remove it. If multiple due date lines reference the same task, the last processed line will be05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 24/34

adopted. For example, a + command followed by a - command will remove the due date since
removal was processed last.
Standard (Fixed) Due Dates
A standard due date refers to a due date set to a fixed date and time. Exporting a process (using
the Process source type) generates two lines of data for each task with a due date in that
process, like this:
Process Task MeasureCommand Value
.[Process Path].[Task Path]Due Date + 21-06-18 18:00
.[Process Path].[Task Path]Time Zone + Canada/Eastern UTC -04:00
You can identify the lines which relate to a standard due date by the values Due Date and Time
Zone in the Measure column. To make changes to a standard due date with Integration, you can
modify the values in the Value column on these lines.
The Due Date measure accepts values in the following format:
Format Example
YYYY-MM-dd HH:mm:ss(Only one space character between date and
time.)2020-09-
05T17:00:00Z05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 25/34

If you do not specify a time, your Vena environment's Global Due Date time setting will be used.
If no Global Due Date time is set, the server default of 00:00 UTC-5 (midnight EST) will be used.
The Time Zone measure accepts any of the following values:
Pacific/Samoa
Pacific/Honolulu
America/Anchorage
Canada/Pacific
Canada/Mountain
America/Phoenix
Canada/Central
Canada/Saskatchewan
Canada/Eastern
America/Caracas
Canada/Atlantic
America/Campo_Grande
Canada/Newfoundland
America/Buenos_Aires
Atlantic/Azores
Europe/London
Europe/Paris
Note
The time must be set using 24-hour (military) time; e.g., 08:00 for 8 AM, 23:00 for 11
PM, etc.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 26/34

Africa/Cairo
Asia/Baghdad
Asia/Tehran
Asia/Baku
Asia/Kabul
Asia/Karachi
Asia/Kolkata
Asia/Kathmandu
Asia/Almaty
Asia/Bangkok
Asia/Hong_Kong
Asia/Tokyo
Australia/Adelaide
Pacific/Guam
Asia/Magadan
Pacific/Kwajalein
Pacific/Fiji
Note
An exported due date time zone will also include "UTC -XX:XX" as part of the time
zone value, where the Xs represent the offset of that time zone from UTC (in hours).
The offset is included only for information, and this portion does not need to be
included when you write a time zone value to a Vena process with Integration (i.e.,
you need only include "Canada/Eastern", not the full string of "Canada/Eastern UTC
-04:00").05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 27/34

Smart (relative) Due Dates
A smart due date is established when specific conditions are met. This condition is defined in
relation to a key date, which is set as a certain number of days before or after that date. The key
date can be the task's start date, the process's start date, or the process's end date. When
exporting a process (using the Process source type), two lines of data are generated for each
smart due date within that process, as illustrated below:
Process Task MeasureCommand Value
.[Process Path].[Task Path]Due Date + 15 work day(s) after task starts
.[Process Path].[Task Path]Smart Due Date + 15 AfterStart
You can identify the lines which relate to a smart due date by the value Smart Due Date in the
Measure column. To make changes to a smart due date with Integration, you can modify the
values in the Value column on these lines.
The Smart Due Date measure accepts values in the following format:
Format Description Example
n AfterStart Set smart due date n workdays after the task starts 5 AfterStart
n AfterProcessStartSet smart due date n workdays after the process
starts10
AfterProcessStart05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 28/34

n
BeforeProcessEndSet smart due date n workdays before the process
ends1 BeforeProcessEnd
Every smart due date in an exported process also generates a line with the value Due Date in the
Measure column, just like a standard due date.
If the smart due date has not yet been activated (i.e., its condition has not yet been met), the
value in the Value column will display a text string describing the smart due date, rather than a
specific date and time. For example:
Process TaskMeasureCommand Value
.[Process Path].[Task Path]Due Date + 1 work day(s) before process ends
Once the smart due date has been activated, a standard (fixed) due date is calculated, and this
descriptive text string is changed to a date and time in the normal DD-MM-YY HH:MM format.
When setting smart due dates via Integration, remember:
If a Process destination receives a smart due date's "descriptive text string" in the Value
column for the Due Date measure, it will cause an error and stop the integration task.
The integration will process data up to the first such error; all prior lines are processed
successfully.
To prevent errors, remove any Due Date lines from incoming data if a smart due date is also
set for that task. This avoids setting a standard due date where a smart due date is intended.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 29/34

External destinations
Salesforce
You can also use Integration to send data to Salesforce, whether from Vena or another
Salesforce source involving data transformation.
Salesforce destinations generate destination fields based on the columns of the selected
Salesforce object (table). To set up:
Name the destination and enter the Salesforce Object name.
Select a Salesforce authorization or enter login credentials.
After selecting an object and entering credentials, the Integration tool retrieves the object's
destination fields, which display in the Create Destination window.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 30/34

All columns from the specified Salesforce object will be imported, which might result in a lengthy
list of destination fields. To manage this, you may choose only the desired destination fields by
transferring them from the Destination fields box to the Selected fields box using the provided
buttons:05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 31/34

The Salesforce Operation Type determines how Salesforce handles duplicates in the incoming
data.
INSERT: Integration job fails if the incoming row already exists in Salesforce (default).
UPSERT: Replaces existing Salesforce rows with incoming data if they match. Select a unique
Salesforce Upsert Field to act as a key field, ensuring each row has a unique value. Salesforce
checks for duplicates based on this field and updates matching rows.
Was this article helpful?
0 out of 0 found this helpful05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 32/34

Related articles
How-to: Vena Integration: Part 6 – Channels &
Field Mappings
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
How-To: Installing the Vena Suite Bundle for
NetSuite
How-To: Creating and Managing Data
Permissions
Troubleshooting: Microsoft 365 Has Been
Configured to Prevent Individual Acquisition
and Execution of Office Store Add-insRecently viewed articles
How-to: Vena Integration: Part 4 – Import and
Export API
How-to: Vena Integration: Part 3 – External
Sources – Data Feeds & Connections
How-to: Vena Integration: Part 2 – Internal
Sources
How-to: Vena Integration: Part 1 - Feature
Overview
Troubleshooting: Vena Export API 429 Too
Many Requests Status Code
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 33/34

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 13:01 How-to: Vena Integration: Part 5 - Destinations – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38631593514253-How-to-Vena-Integration-Part-5-Destinations 34/34
