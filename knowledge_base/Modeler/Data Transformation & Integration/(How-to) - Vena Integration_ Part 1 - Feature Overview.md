# (How to)   Vena Integration  Part 1   Feature Overview

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
ETL JobsHow-to: Vena Integration: Part 1 -
Feature Overview
About this series
This series is all about how to use Vena Integrations. You are on Part 1, which provides an
overview of the Integration tool's capabilities.
Vena Support
Updated 1 month ago
05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 1/13

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
Part 1: Feature Overview – you are here
Part 2: Internal Sources
Part 3: External Sources – Data Feeds & Connections
Part 4: External Sources – Import and Export API
Part 5: Destinations
Part 6: Channels & Field Mappings
Video
Check out a video of this article's content.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 2/13

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
Product UpdatesVena Integration Part 1: Feature Overview Vena Integration Part 1: Feature Overview
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application
Permissionsfor authorizations.
IfData Permissionsare set up in your environment, you will also need the appropriate
permissions for the data that you are working with.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 3/13

To use some features of the Integration tool successfully, you may need additional specialized
skills or knowledge. Applicable topics include:
Model Slice Query Language/Hibernate Query Language
Excel formula syntax
SQL
VenaQL
Supported third-party connectors: Salesforce, NetSuite, QuickBooks, Sage Intacct or Business
Central
Table of contents
Why use Integrations?
About Integrations
How to: Find and navigate the integration tool
Channels
Data feeds
Connections

Why use Integrations?
The Vena Integration tool simplifies data management by enabling seamless movement
between external sources, internal Vena databases and external systems, with on-the-fly
transformations. It is particularly useful for routine imports from systems like NetSuite or
Salesforce, leveraging APIs for direct data retrieval.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 4/13

The tool offers an intuitive interface to configure how data integrates into your Vena database,
and once set up, tasks can be repeated with a single click, making it ideal for recurring imports.
Integration ensures efficiency and consistency while handling data transfers.
This article walks you through using the Integration tool to import, transform and manage data
effectively.
About Integrations
Integration consists of three main components: Sources, Destinations and Channels.
Sources define the locations from which data can be streamed into the Integration tool, as well
as the data itself. Both internal (e.g., Vena databases, CSV files, etc.) and external (e.g., NetSuite,
QuickBooks, Salesforce, etc.) source types are supported.
Destinations are the counterpart to sources; they define where the processed source data will
be written. While the ultimate destination in most cases is a Vena database, other internal and
external source types are also available to support a variety of use cases.
Channels define a connection between a data source and a destination. You configure a
channel by selecting the source and destination of the data, then specifying any transformations
that are needed to make the source data fit the chosen destination. All channel settings are
saved, and channels can be run again or modified as needed.
Vena’s Integration tool helps you manage these components. The basic operation of the
Integration tool involves:
1. Creating a source.
2. Linking that source to a destination using a channel. 05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 5/13

You define how source data moves to the destination by configuring the channel in a drag-and-
drop interface with options to create special adaptors that transform the incoming data with
Excel formulas or lookup tables. You may also write predefined values for the destination.

How to
Find and navigate the Integration tool
The Integration tool is found in the Modeler tab, under Data Transformations in the sidebar
menu. There are three submenus under Data Transformations: Channels, Data Feeds and
Connections.
Caution
Integration is a powerful tool for importing and transforming data but use it with
caution. Understand its effects on your database before executing any job. Although
changes can be reversed, doing so is inconvenient and time-consuming, potentially
disrupting your processes.
While learning this tool, we recommend testing with a cloned data model instead of
your production model. Once successful in testing, replicate setups in your
production model.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 6/13

Channels
Any channel, source or destination you create is added to the list of Integration components in
your Channels page.
05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 7/13

AName List of channels, sources and destinations. By default, the list is sorted in
alphanumeric ascending order (0-9, A-Z) by this column. Organize these into
folders by selecting Create (G), then Folders to make a new folder. Then,
right-click the component and select Move to relocate it into the folder.
Select the Name header to reverse the sort order or type into the Filter text
field to search for a keyword.
BType Displays the type of integration component: Folder, Source, Channel or
Destination. Use the drop-down menu under the column header to narrow
the list down to a specific component.
CChannel
SourceChannels only. Displays the source used by the channel. Select the source to
view and edit its details. Use the Filter text field to search for specific sources.
DSource TypeSources only. Displays the label or logo of the source type. Use the drop-
down menu under the column header to narrow the list down to a specific
type.
EChannel
DestinationChannels only. Displays the destination used by the channel. Select the
destination to view and edit its details. Use the Filter text field to search for
specific destinations.
FDestination
TypeDestinations only. Displays the label or logo of the destination type. Use the
drop-down menu under the column header to narrow the list down to a
specific type.
GSearch boxKeyword search for all Integration components, regardless of type.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 8/13

HCreate Select to create a new Folder, Source (including VenaQL queries as sources),
Destination, Channel or Vena Table.
Data feeds
Data feeds tell the Integration tool what data to retrieve and where to find it—not only the data
location (external source, Vena Table, etc.) but the specific data from that location (the “data
load”).
AAdd New
Data FeedCreate a new data feed.
BExternal
SourceSource of the target data. May be NetSuite, Salesforce, QuickBooks, Intacct
or Business Central. 05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 9/13

CData Feed
NameName of this specific data feed. You name this feed when you select + Add
New. Right-click and select Edit to rename the feed if desired.
DConnection
NameDifferent data feeds from the same source may have different connections
to different data sets. You name this connection when creating a new data
feed. Right-click and select Edit to rename the connection if desired.
E Last
Successful
RunDate and time of the most recent run of this feed without error.
Connections
Before creating a data feed, you must establish a connection to the external source. This
Connections tab deals specifical with Vena's direct connections - NetSuite, Salesforce, Intuit
QuickBooks, Sage Intacct and Business Central. These secure connections use access tokens
that give Vena permission to connect to these third-party accounts. Connections only need to be
set up once, then they are saved in the Integration tool.
Indirect connections are created using APIs. Learn more about Vena's Import and Export API.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 10/13

Create a new connection by selecting + New Account. Separate articles describe how to connect
with each external source in more detail:
How-To: Set Up a Business Central Connector and Data Feed
How-To: Setting Up a NetSuite Connector and Data Feed
How-To: Set Up a Quickbooks Connector and Data Feed
How-To: Set Up a Sage Intacct Connector and Data Feed
How-To: Set Up a SalesForce Connector and Data Feed
Was this article helpful?
11 out of 11 found this helpful05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 11/13

Related articles
How-to: Vena Integration: Part 2 – Internal
Sources
How-to: Vena Integration: Part 4 – Import and
Export API
Reference: Writing Expressions (MQL & HQL)
How-To: Data Model Series (Part 1): Creating a
Data Model
How-To: Create Automatic Channel Mapping
With Map by NameRecently viewed articles
Troubleshooting: Vena Export API 429 Too
Many Requests Status Code
Troubleshooting: Vena Import & Export API
422 Unprocessable Entity
Troubleshooting: Vena Import API 406 Invalid
Accept Header Status Code
Troubleshooting: Vena Import & Export API
405 Method Not Allowed Status Code
Troubleshooting: Vena Import & Export 404
Not Found Status Code
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 12/13

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 12:59 How-to: Vena Integration: Part 1 - Feature Overview – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001301883-How-to-Vena-Integration-Part-1-Feature-Overview 13/13
