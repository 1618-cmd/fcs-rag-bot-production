# (Reference)   Modeler Experience

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Modeler Fundamentals Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Reference: Modeler Experience
Data Modeling
Functions
Calcs (Scripts)
Data Transformation &
IntegrationReference: Modeler Experience
New to Vena or the Modeler role? This article is a good place to start!
About the Modeler role
Vena Modelers are users with access to the Modeler tab in the web application (vena.io).
Vena Support Team
Updated 1 month ago
02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 1/23

Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesModelers are responsible for designing, updating and maintaining the data models that serve
as the backbone for organizational reporting and analytics. This role also includes managing ETL
processes and performing data transformations to ensure accurate, efficient and integrated
data flows across the platform.
This article introduces the key aspects of the Modeler role, including how to navigate the
Modeler tab and where to find help articles for how-to guidance and best practices.
Table of contents
Navigation
Data Modeler
Members
Revisions
Attributes
Preview Intersections
Calculated Members
Versioning
ETL Templates
Export
Settings
Functions
Scripts
Data Transformations
Channels
VenaQL
Vena Tables02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 2/23

Data Feeds
Connections
History

Navigation
AModeler Tab Selecting the Modeler tab opens the Data Modeler page.
BData Modeler Lists the data models associated with your Vena tenant. Select a data
model to open its members (see D below).
CFunctions MenuVena’s Foreign Exchange Conversion function for converting values from
local currencies to one or more reporting currencies. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 3/23

DScripts Editor Use the Vena Calcs scripting language to run calculations and
simulations for business rules at the database level for all dimensions
and members.
EData
TransformationsVena’s tool for importing data from external systems and integrating
with your Vena data.
FHistory A list of all ETL jobs and their progress, including details of any errors
encountered during the process.
GMembers MenuLists dimensions and members associated with a particular data model.
Includes features for creating and managing dimensions and their
member hierarchies, plus attributes, aliases, roll-up operators and
calculated members. Preview intersection values contained in the data
models as well.
HVersioning ToolA flexible tool for copying data from one part of the data model to
another, helpful for budgeting and what-if scenarios.
IETL Templates
ListLists all ETL templates associated with a data model and their schedules
(if applicable). Includes options to create and schedule new ETL
templates.
JExport Menu  Export options for each data model including values, hierarchies, Line-
Item Details (LIDs) and attributes. Use the quick export options or
manually write an export query using MQL and HQL expressions.
K Settings MenuChoose options for how each data model treats zeroes and blank
spaces. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 4/23

LAdd New Model
buttonSelect to add a new data model.
Data Modeler
When you open the Modeler tab, you land on the Data Modeler page. All data models are listed,
along with their descriptions and dimension lists. From this page, select the data model you
want to work with or add a new data model.
Learn more about data models, plus their members and dimensions, in Vena’s Knowledge
Base under Modeler > Data Models:02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 5/23

Members
Select a data model to open the Members page (A). Change data models using the drop-down
menu (B). Dimensions in the selected data model are listed in a horizontal row across the top of
the window (C). Select the pencil icon (
) to open the Manage Dimensions drawer and edit or
add new dimensions (D).
Select a dimension to view its members in the table and hover over a member line to view
options:
Edit Member Details (E)
Add Sibling (F)
Member Actions Menu (G)02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 6/23

Learn more about dimensions and members.
Revisions
Select Revisions to review data model revisions with ease. Each revision is accompanied by a
description, action (updated, deleted, added), the time the revision occurred and the user who
made the change.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 7/23

Learn more about revisions for audit tracking.
Attributes
Select Manage > Attributes to open an interactive window where you can search existing
Attributes, edit, delete or add new Attributes as needed.
02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 8/23

Learn more about Attributes.
Preview Intersections
Hover on a member line and right-click or select the vertical ellipses (
) to open its menu, then
select Preview Intersection.
In this window, you can view intersections and export the list into a CSV file.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 9/23

Calculated Members
The Calculated Members tool is used for custom roll-ups, allowing you to:
Create special members from existing ones.
Report on specific data subsets not supported by standard hierarchies.
This feature enhances reporting efficiency and flexibility in data analysis.
Create a new Calculated Member by right-clicking or selecting the vertical ellipses in line with
the member on the same level as where you want to create that Calculated Member, then select
Add Calculated Member. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 10/23

Learn more about building a custom roll-up with Calculated Members.
Versioning
Bulk-copy data from one part of your data model to another using the Versioning tool or set and
save Versioning configurations for future use. Create new budgets or copy last year’s numbers
as a baseline for the coming year quickly and accurately. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 11/23

Learn more about Versioning.
ETL Templates
Automate ETL templates in Vena with the ETL Scheduler to set schedules for daily, weekly or
monthly runs, making it easier to manage repetitive tasks.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 12/23

Learn more about scheduling ETL jobs.
Export
Use query expressions to export a subset of your data for faster downloads and to focus only on
the data you’re interested in.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 13/23

Learn more about exporting a subset of data from a data model.
Settings
The Settings menu contains two options you may apply to each data model:
1. Retain Zeros For This Model – Toggle this setting to ON to keep any zeros input and not
replace them with blanks. This option can be fine-tuned to specific slices of the data model as
well.
2. Blank Empty Rollups For This Model – Toggle this setting to ON to ensure parent-level
rollups without numerical data at the child level are displayed as blanks instead of zeros. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 14/23

Learn more about how Vena treats zeroes and black spaces.
Functions
Vena Functions ensure that data remains up to date by executing automated calculations across
the data model. Currently, the available function is the Foreign Exchange (FX) Conversion
Function, which facilitates international transactions by establishing calculations for currency
conversion across reports.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 15/23

Learn more about Vena’s Foreign Exchange (FX) Conversion Function.
Scripts
Use Vena Calculation Scripts (Vena Calcs) in the Calc Script Editor to run calculations and
simulations for business rules at the database level.02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 16/23

Learn more about Vena Calcs.
Data Transformations
The Data Transformations tab contains Channels, Data Feeds and Connections, enabling seamless
data integration and manipulation.
02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 17/23

Visit the Knowledge Base for the Vena Integration Series of help articles.
Channels
A channel represents each data integration, specifying the data source, destination and
transformation process. View your current channels or select Create to add a new folder,
source, destination, channel or Vena Table.
VenaQL
Utilize Vena’s query language to extract data from multiple sources at once. Access the VenaQL
Editor by selecting Create > Source > VenaQL. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 18/23

Learn more about VenaQL.
Vena Tables
Vena Tables serve as a data repository for staging data, storing Drill Transactions and as a
source for queries in VenaQL. Create a new one by selecting Create > Vena Table.
02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 19/23

Learn more about Vena Tables.
Data Feeds
Data feeds specify the data to be retrieved and identify its precise location within the model,
ensuring that the correct information is targeted for extraction. It’s possible to have multiple
data feeds drawing different data loads from the same source. Create a new data feed by
selecting + Add New.
Learn more about data feeds.
Connections
The Connections section is where you’ll set up links between Vena and supported data systems:
Business Central
Sage Intacct02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 20/23

NetSuite
QuickBooks
Salesforce
These connections ensure efficient data sharing and real-time updates across platforms. Create
a new connection by selecting + New Account.
Learn more about managing connections.
History
View a list of ETL jobs, their statuses and any associated errors preventing them from completing
in the History tab of the Modeler sidebar menu. 02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 21/23

Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Assigning Dimension Types and
Standard Members
How-To: Data Model Series (Part 1): Creating a
Data ModelRecently viewed articles
Troubleshooting: Exit Edit Mode and Retry
When Saving
Troubleshooting: Data Save Failed Most Likely
Because of an Expired Session Error02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 22/23

How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
How-To: Data Model Series (Part 4): ETL Tool
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple ReportsTroubleshooting: Save Data Is Unavailable
Until a Successful Refresh Is Completed
Troubleshooting: The Remote Server
Returned (500) Internal Server Error When
Saving Data
Troubleshooting: Value Cannot be Null Error
Message When Saving Data
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:01 Reference: Modeler Experience – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/39308751797645-Reference-Modeler-Experience 23/23
