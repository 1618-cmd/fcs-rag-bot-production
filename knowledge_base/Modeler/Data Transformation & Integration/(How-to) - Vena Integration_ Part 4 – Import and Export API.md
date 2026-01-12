# (How to)   Vena Integration  Part 4 – Import and Export API

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
ETL JobsHow-to: Vena Integration: Part 4 –
Import and Export API
About this series
This series is all about how to use Vena Integrations. You are on Part 4, which details how to
access Vena’s import and export APIs and create a Vena template for your import API.
Vena Support
Updated 4 months ago
05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 1/11

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
Part 4: External Sources – Import and Export API – you are here
Part 5: Destinations
Part 6: Channels & Field Mappings
Before you begin
To follow the instructions in this series, you will need Modeler access.
To work with authorizations for external systems, you will need the necessary Application
Permissionsfor authorizations.
If Data Permissions are set up in your environment, you will also need the appropriate
permissions for the data that you are working with.05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 2/11

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
Product UpdatesTo use some features of the Integration tool successfully, you may need additional specialized
skills or knowledge. Applicable topics include:
Model Slice Query Language/Hibernate Query Language
Excel formula syntax
SQL
VenaQL
Supported third-party connectors: Salesforce, NetSuite, QuickBooks, Sage Intacct or Business
Central
Table of Contents
Vena API & Documentation
Setting up a Vena template for an API import
Vena API & Documentation
Follow the link below to access Vena’s Import and Export API, plus find comprehensive reference
guides and examples to support you along the way.
Vena API Documentation
Setting up a Vena template for an API import05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 3/11

Why use this feature?
Before using the public Vena API to import data, you must configure your Vena template to
receive incoming data.
The Import API lets you automate ETL jobs by setting up templates in Vena and triggering them
via multiple endpoints. This article explains how to prepare Vena templates for use with the
Import API.
The Vena Import API has several endpoints that let you run ETL jobs in Vena through REST
requests. For example, the Start With Data endpoint lets you run a job with a JSON object as the
data payload. The API developer docs list the required request parameters for this endpoint:
How to
Step 1 - Set up a Vena Table to accommodate API data
1. Navigate to the Modeler tab.
2. Select Data Transformations from the sidebar. 05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 4/11

3. Select Channels from the sidebar tab.
4. Select Create from the upper right-hand corner of the screen.
5. Select Vena Table from the drop-down menu.
05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 5/11

6. In the Create Vena Table drawer, follow the prompts to create your new Vena Table:
AEnter unique column names for each column (may contain letters and numerals). Please
note that leading and trailing whitespaces are not allowed in the column names.05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 6/11

BThe number of columns must match the data being uploaded via the API
CYou must assign a data model to each unique Vena Table to segregate data models. In
this way, you will only be able to view this Vena Table if you have the appropriate
permissions for the affiliated data model.
DSelect Create when finished creating your Vena Table.
7. The new Vena Table will appear on your Channelspage:
In the next step, you’ll use your Vena Table to build an ETL template.
Step 2: Create an ETL Template for File to Vena Table
Enter reference info here. This could be a table, diagram, etc.
1. Navigate to the Modeler  tab.
2. Select Data Modeler  from the sidebar .
3. Select ETL from the sidebar tab. By default, you should be in the Templates  section of the ETL
tool, which lists your existing ETL  templates.  05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 7/11

4. Select + Create T emplate .
5. Enter a name for the ETL  Template.
6. Select Add Step .
7. Select File to V ena T able from the drop-down menu.
8. Select  Save .
05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 8/11

Step 3: Locate  your template ID for the API Job
1. Locate your new ETL template on the ETL Template page.
2. Select the vertical ellipses at the end of the row and select View/Edit Details from the menu.
3. Locate your ID and copy it (CTRL+C).
4. You will use your ETL Template ID when sending a POST request as part of your API data
load. Learn more about using the Vena Public API to import data from Dynamics 365
Business Central.05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 9/11

Was this article helpful?
4 out of 6 found this helpful
Related articles
How-to: Vena Integration: Part 3 – External
Sources – Data Feeds & Connections
How-to: Vena Integration: Part 1 - Feature
Overview
How-to: Vena Integration: Part 2 – Internal
Sources
How-To: Create Automatic Channel Mapping
With Map by Name
How-To: Setting up a Staging Query (Vena 365
Only)Recently viewed articles
How-to: Vena Integration: Part 3 – External
Sources – Data Feeds & Connections
How-to: Vena Integration: Part 2 – Internal
Sources
How-to: Vena Integration: Part 1 - Feature
Overview
Troubleshooting: Vena Export API 429 Too
Many Requests Status Code
Troubleshooting: Vena Import & Export API
422 Unprocessable Entity05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 13:01 How-to: Vena Integration: Part 4 – Import and Export API – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115005668603-How-to-Vena-Integration-Part-4-Import-and-Export-API 11/11
