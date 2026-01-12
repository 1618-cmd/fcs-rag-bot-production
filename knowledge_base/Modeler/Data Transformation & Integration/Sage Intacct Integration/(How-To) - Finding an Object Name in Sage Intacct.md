# (How To)   Finding an Object Name in Sage Intacct

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Sage Intacct Integration Search
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
ETL JobsHow-To: Finding an Object Name in
Sage Intacct
Refine your Sage Intacct data feed with object names for precise data retrieval.
Why use this feature?
Vena Support Team
Updated 8 months ago
05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 1/8

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
How-To: Finding an Object
Name in Sage Intacct
How-To: Set Up a Sage Intacct
Connector and Data Feed
Explainer: Sage Intacct
Connector Update
Troubleshooting: Sage Intacct
ETL Error There Are Too Many
Operations Running for This
CompanyWhen setting up a Sage Intacct data feed, you have the flexibility to enhance your search by
adding an object name. This feature allows you to refine queries within Sage Intacct tables,
ensuring more precise data retrieval. By specifying object names, such as SODOCUMENT*,
PODOCUMENT*, and INVDOCUMENT*, you can also access custom fields associated with these
_DOCUMENT objects, making your data feed more tailored and efficient.
Before you begin
You will need at least Modeler access to follow the instructions in this article.
Before you can create an Intacct connection in Vena, you must first create a corresponding Web
Services Connection in your Intacct account.
How to
1. Log in to your Sage Intacct account.05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 2/8

Troubleshooting: Sage Intacct
ETL Error There’s an Error With
the Value for Field STATE.
Value: [P]
Troubleshooting: Sage Intacct
ETL Error Unable to parse
Query value: X != 'X'
Troubleshooting: ETL – There
Are Missing Records in the
Batch
Troubleshooting: Sage Intacct
ETL Error - A Request’s Function
With the Control ID Is in
Process
Troubleshooting: Response
From Intacct – the Period Filter
Is Required
Troubleshooting: Sage Intacct
ETL Error Check the Fields Exist
and Try Again
Troubleshooting: Sage Intacct
ETL Error - The Service Is
Temporarily Offline
Troubleshooting: ResultID From
Sage Has X Fewer Remaining
Records Than Expected2. Navigate to Platform Services and select Objects,
The table onscreen shows the objects Vena can query.
3. In the fifth column, copy the Integration name for your object. You’ll need this integration
name when creating your Sage Intacct data feed in Vena.05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 3/8

Troubleshooting: Error With
Intacct Request: IP Address
Denied
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
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map by
Use Case: Finding a _DOCUMENT Object
Sam at Supercorp wants to query an object from Sage Intacct that has a custom field
to retrieve precise data and access custom fields associated with this object. In this
instance, it's a _DOCUMENT object. To do this, he needs,  to specify the object in the
following format:
{IntegrationName}.{Object}
Objects affected: SODOCUMENT*, PODOCUMENT*, INVDOCUMENT*
1. SODOCUMENT: Sales Order Documents, which include details about sales orders.05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 4/8

Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
2. PODOCUMENT: Purchase Order Documents, containing information about
purchase orders.
3. INVDOCUMENT: Invoice Documents, which include data related to invoices
issued.
Example
Object: Sales Invoice TM
Integration Name: SODOCUMENTENTRY
Formatted Object Name: SODOCUMENTENTRY.Sales Invoice TM05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 5/8

Was this article helpful?
05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 6/8

1 out of 1 found this helpful
Related articles
How-To: Set Up a Sage Intacct Connector and
Data Feed
Explainer: New Tasks Tab Experience
Troubleshooting: Common Template
Automation Problems
How-To: Set Up a SalesForce Connector and
Data Feed
Resource: Vena 365 & Vena Desktop
Contributor GuidesRecently viewed articles
Troubleshooting: Unable To Connect to Vena
Insights Connector
Troubleshooting: Vena Insights Connector
Intersection Values Showing as Zero
Troubleshooting: Vena Insights Connector
Data Model Intersections or Values Table Is
Blank
Troubleshooting: Vena Insights Connector
Load and Transform Data Buttons Grayed Out
Troubleshooting: Vena Insights Connector
Users Able To See Data Models They Don’t
Have Access To
Didn't find what you're looking for?05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 7/8

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request05/01/2026, 12:45 How-To: Finding an Object Name in Sage Intacct – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/35838014219661-How-To-Finding-an-Object-Name-in-Sage-Intacct 8/8
