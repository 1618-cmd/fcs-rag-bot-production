# (Troubleshooting)   Response From Intacct – the Period Filter Is Required

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
ETL JobsTroubleshooting: Response From
Intacct – the Period Filter Is Required
Issue summary
When setting up a Sage Intacct data feed, this error message may appear:
Error with Intacct query; check that the fields exist and try again. Response from Intacct: The period
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 1/6

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
Companyfilter is required.
Suggested solution
Some Sage Intacct objects such as GLACCOUNTBALANCE require a query and a period
parameter.
1. If the data feed configuration Query field is blank, update it by adding a query and ensure the
PERIOD parameter is included.
2. If the data feed configuration is not blank but does not include a PERIOD in it, please add it.
3. An example query is shown below. Please update the values to fit your requirements.
 (PERIOD = 'Month Ended October 2023')
Cause
This could happen if the object you reference from Sage Intacct requires a period filter in the
query field.
Keywords05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 2/6

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
Records Than Expectedperiod is required, sage intacct, glaccountbalance
Was this article helpful?
0 out of 0 found this helpful
Related articles
Troubleshooting: Sage Intacct ETL Error Check
the Fields Exist and Try AgainRecently viewed articles
Troubleshooting: Sage Intacct ETL Error - A
Request’s Function With the Control ID Is in
Process
Troubleshooting: ETL – There Are Missing
Records in the Batch
Troubleshooting: Sage Intacct ETL Error
Unable to parse Query value: X != 'X'
Troubleshooting: Sage Intacct ETL Error
There’s an Error With the Value for Field
STATE. Value: [P]
Troubleshooting: Sage Intacct ETL Error There
Are Too Many Operations Running for This
Company05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 3/6

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
Channel Mapping With Map by05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 4/6

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
Submit a Request05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 05/01/2026, 12:48 Troubleshooting: Response From Intacct – the Period Filter Is Required – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/30623786603661-Troubleshooting-Response-From-Intacct-the-Period-Filter-Is-Required 6/6
