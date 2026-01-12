# (How To)   Use Clear Slices to Clear Intersections During an ETL Load

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
ETL JobsHow-To: Use Clear Slices to Clear
Intersections During an ETL Load
Clear Slices is a Vena feature that ensures your new data uploads fully replace old data.
This article explains the Clear Slices feature in ETL loads. For using Clear Slices with integrations,
visit this article.
Video
Vena Support Team
Updated 1 month ago
02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 1/16

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
Restrictions to the SQL WHERECheck out a video of this article's content.
Video Clear Slices in ETL Loads Video Clear Slices in ETL Loads
Why use this feature?
When updating actuals data in Vena using ETL (Extract, Transform, Load) from an external GL
system, modelers may occasionally need to overwrite a previously populated intersection with a
zero balance.
If your GL system exports a ‘0’ value:
The new data load will proceed without issues.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 2/16

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
Data QueryingVena will recognize the ‘0’ and overwrite the existing data at the intersection.
In this scenario, you likely don’t need to use Clear Slices.
If your GL system exports a blank (empty) value:
Vena ignores blank values during the load process.
As a result, any blank intersections in the new data will retain the old values, rather than
replacing them.
In this case, using Clear Slices is recommended to remove the previous data before loading
the new set.
Because Vena doesn't interpret blanks as valid values, clearing out previous data explicitly is
necessary when your source system provides blanks instead of zeros.
Manually deleting old data is tedious and error-prone. Clear Slices streamlines the process by
automatically clearing outdated intersections before loading new data.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 3/16

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
About Clear Slices
Clear Slices is integrated into the Vena ETL Templates interface and can be configured within
either File to Cube or Stage to Cube steps when the Values data type is selected. This feature is
currently not supported for the Attributes data type.
Clear Slices runs after the data load, allowing it to skip intersections already updated by the new
data. It then deletes any remaining values in the specified slice.
There are two configuration options:
Slices to Clear
Slices to Clear by Dimension
These options support different use cases and can be used individually or together within the
same ETL template.
Slices to Clear02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 4/16

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
Product UpdatesSlices to Clear uses a Model Query Language (MQL) expression to define specific portions
(slices) of the database to be cleared. This expression is entered directly into a designated field
within the ETL template configuration.
When the ETL runs, any unmodified values within the defined slices are deleted after the data
load completes.
For example:
dimension('Account':'Income Statement') dimension('Scenario':'Actual')
This MQL expression targets only Income Statement values in the Actual scenario, ensuring
that no unintended data outside these slices is cleared.
Note: The Slices to Clear option is static—it always clears the same predefined slices, regardless
of which areas are updated during the data load.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 5/16

Slices to Clear by dimension
Slices to Clear by Dimension is a dynamic option. Instead of using a fixed MQL expression, you
select one or more dimensions in the ETL template to define which members should be cleared
based on the data being loaded.
Consider this example:
AccountEntityScenario Year Period Value
AdvertisingDept 101Actuals 2017 Dec 200
Dimensions like Account, Entity, Scenario, Year, and Period define the intersection where the
value (200) is written. 02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 6/16

With the Slices to Clear by Dimension option, you select a subset of these dimensions in your
ETL template. For example, Account, Scenario, and Period. When the ETL runs, Vena uses these
selected dimensions to define a slice for each row of incoming data. In the example above, this
results in the slice:
{Advertising, Actuals, Dec}
This process repeats for every unique combination of selected dimension members in the load.
After the data is loaded, Clear Slices deletes any unmodified values within those dynamically
defined slices.
Unlike the static Slices to Clear option, Slices to Clear by Dimension is dynamic. It adapts to
the actual data being loaded, clearing only the relevant parts of the database, even if those slices
vary from one load to the next.

Using Slices to Clear and Slices by dimension
together02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 7/16

When using the Clear Slices options together, only data found in slices meeting both options’
conditions are cleared.
For example, if you manually define a slice with MQL like this:
dimension('Department':'Dept 101') dimension('Year':'2018')
And define slices by dimension, such as this:
{Advertising, Budget}
Then the system combines them into a single slice:
{Advertising, Dept 101, Budget, 2018}
Only data found in this combined slice will be cleared.
Combining Slices to Clear (static) and Slices to Clear by Dimension (dynamic) provides an
added layer of control and safety.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 8/16

While the dynamic option clears slices based on the incoming data, it can also introduce risk,
especially if the data file contains errors or unexpected values. By also defining a static MQL
slice, you create a safeguard: only slices that fall within the static definition are eligible for
clearing.
This ensures that, regardless of what's in the load file, Clear Slices only removes data from
intersections explicitly allowed by the static slice.
Before you begin
To follow the instructions in this article, you will need at least Modeler access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
Caution
If you use both options at the same time, you may not reference the same dimension
in both options. If you do this, an error will occur when the ETL template is run.
 Warning02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 9/16

How to
Using Clear Slices on an ETL Template
You can configure both Slices To Clear and Slices To Clear by dimension on File To Cube or Stage to
Cube steps with the Values Data Type within any new or existing ETL template.
The instructions below discuss how to set up Clear Slices on a new step on new or existing ETL
templates. For instructions on how to add Clear Slices to existing Steps (within existing ETL
templates), see the section Modifying an existing Clear Slices configuration.
To use Clear Slices on a template:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab. By default, you should be in the Templates
section of the ETL tool, which lists your existing ETL templates:
Using Clear Slices will delete intersection data from your Vena database. Before using
this feature, please ensure you understand the consequences and are confident that
your configuration will only delete the data you intend to delete.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 10/16

4. To configure Slice To Clear on an existing template: Either select the vertical ellipsis or
right-click on the row containing the template you want to configure Slices To Clear on and
select View/Edit Details. This opens the ETL Template Manager drawer.
To configure Slice To Clear on a new template:Select +Create Template. This opens the
ETL Template Manager drawer. Enter a name for your ETL template. 02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 11/16

5. From the ETL Template Manager Drawer, select the Add Step drop-down menu. Then, select
either File To Cubeor Stage To Cube.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 12/16

6. From the Data Type drop-down menu, select Values. This expands the Clear Slices interface
where you can configure either Slices to clear by dimension, Query slices to clear or both.
7. To use Slices to clear by dimension: Select the dimensions that will define the dynamic slices
by using the checkbox beside each dimension. The selected dimensions will then appear in
the text field.
To use Query slices to clear: Enter an MQL expression that describes the desired slices. Refer
to this guide for help with formatting the expression.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 13/16

8. Select Add when you have finished configuring the step. This will also apply your Clear Slices
configuration on that step.
9. Select Save when you are finished configuring the ETL template.
10. The next time you run this ETL template, Clear Slices will be in effect as you configured it.
Modifying an existing Clear Slices configuration
If you have set up steps with Clear Slices on any ETL template, you can edit the configuration or
turn off Clear Slices at any time. You can also use these instructions if you want to add Clear
Slices to an existing step in a previously created ETL template.
To modify an existing Clear Slices configuration:
1. Either select the vertical ellipsis or right-click on the row containing the template you want
to configure Slices to Clear on.
2. Select View/Edit Details. This opens the ETL Template Manager drawer.
3. Select View under the column labeled Clear Slices next to File to Cube and Stage to Cube steps.
4. Make any desired changes. If you want to completely disable Clear Slices on this step, delete
the MQL expression and/or uncheck all the dimension boxes.
5. Select Save to save your Clear Slices changes.
6. Select Save to save your ETL template changes.02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 14/16

Was this article helpful?
6 out of 10 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Setting up a Staging Query (Vena 365
Only)
Vena Insights Series (Part 4) - Managing
Calculations: Measures, Calculated Tables &
Columns
How-To: Using Expand and Collapse with
Multi-Dynamic Row Mappings
Explainer: Target Member Attribute Calc
TriggerRecently viewed articles
How-To: Exporting CSV Files for ETL Job
How-To: Checking if My File Has a Header Row
or Not
How-To: Automatically Run ETL Templates
Using the ETL Scheduler
How-To: Scheduling Ongoing ETL Jobs at Exact
Times Using Command-Line ETL
Explainer: ETL Export Feature Updates02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 15/16

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:47 How-To: Use Clear Slices to Clear Intersections During an ETL Load – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360005023672-How-To-Use-Clear-Slices-to-Clear-Intersections-During-an-ETL-Load 16/16
