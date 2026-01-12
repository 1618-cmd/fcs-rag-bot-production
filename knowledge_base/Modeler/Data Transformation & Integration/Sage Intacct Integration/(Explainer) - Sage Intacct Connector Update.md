# (Explainer)   Sage Intacct Connector Update

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
ETL JobsExplainer: Sage Intacct Connector
Update
We've made some recent changes to the Sage Intacct Connector to improve the
experience and help you continue to optimize and automate your financial process.
Read on to learn more!
Overview
Vena Support Team
Updated 1 year ago
05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 1/6

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
CompanyWe’ve updated the Sage Intacct integration to leverage a newer version of their API. This change
from the legacy “readbyQuery” to the new “Query” API will happen in phases, and if you use this
connector, you will be informed when the upgrade is being applied to your integration. There is
no change needed from you to enable this upgrade, and it will not affect the data you are
importing to Vena from Sage Intacct.
With these changes, you’ll notice fewer errors when running ETL imports from Sage Intacct and
an improved overall experience.
What are the changes?
API Object upgrade
When planning this upgrade, a primary focus was eliminating manual updates to your Sage
Intacct data feeds. While most objects will now use the API V2, two objects have not been
upgraded due to system limitations. Data imports from these objects will continue to perform as
they do today.
Objects:
1. GLACCOUNTBALANCE
2. ASSET
Additionally, the following six objects will continue to use the legacy version of the API  if you
use the * (select all) filter when retrieving data:
1.
vendor 05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 2/6

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
Records Than ExpectedNew error handling
With the API, if you’re manipulating records in Sage Intacct while simultaneously running an
ETL Import Job into vena.io, Vena may detect that some records are missing. If this occurs,
Vena will cancel the job and show a new error message. If this error occurs, finish making your
changes in Sage Intacct and re-run the job when the Sage Intacct data is stable.2. customer
3. apbill
4. arinvoice
5. reportingperiod
6. journal
05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 3/6

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
Channel Mapping With Map byTo learn more about resolving this issue, check out this article on Intacct ETL error handling.
To learn more about the Sage Intacct API, check out Intacct's API documentation.
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
How-To: Set Up a Sage Intacct Connector and Data Feed
How-To: Finding an Object Name in Sage Intacct
Troubleshooting: Unable To Connect to Vena Insights Connector
Troubleshooting: Vena Insights Connector Intersection Values Showing as Zero
Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 4/6

Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 05/01/2026, 12:46 Explainer: Sage Intacct Connector Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23727555948941-Explainer-Sage-Intacct-Connector-Update 6/6
