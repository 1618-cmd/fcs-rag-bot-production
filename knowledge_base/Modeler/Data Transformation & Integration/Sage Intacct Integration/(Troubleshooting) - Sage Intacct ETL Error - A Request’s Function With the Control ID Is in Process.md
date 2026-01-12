# (Troubleshooting)   Sage Intacct ETL Error   A Request’s Function With the Control ID Is in Process

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
ETL JobsTroubleshooting: Sage Intacct ETL
Error - A Request’s Function With the
Control ID Is in Process
Issue summary
When running an ETL job referencing a Sage Intacct data feed, you may encounter the following
error message: A request's function with the control ID X is in process.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 1/6

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
CompanySuggested solution
This error occurs when two similar Sage Queries are being processed at the same time.
1. Check if the failed Intacct ETL job has been duplicated and both are running at the same time.
2. If you have a Sandbox environment, ensure that the Intacct ETL jobs have not been
configured or are not running at the same time in your Production and Sandbox tenants. If
they are running at the same time across both environments, this could cause interference.
3. If there are multiple Intacct ETL jobs with the same or similar Sage Queries, please add a
delay between the execution of the ETL jobs so there is no interference.
4. Once you've completed all of the previous steps, try re-running the ETL job again.
5. If all looks good and the issue persists, please contact Vena Support.
Keywords
sage, intact, function with the control ID is in process
Was this article helpful?
0 out of 0 found this helpful05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 2/6

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
Records Than ExpectedRecently viewed articles
Troubleshooting: ETL – There Are Missing Records in the Batch
Troubleshooting: Sage Intacct ETL Error Unable to parse Query value: X != 'X'
Troubleshooting: Sage Intacct ETL Error There’s an Error With the Value for Field STATE. Value:
[P]
Troubleshooting: Sage Intacct ETL Error There Are Too Many Operations Running for This
Company
Explainer: Sage Intacct Connector Update05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 3/6

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
Channel Mapping With Map by05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 4/6

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
Submit a Request05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 05/01/2026, 12:48 Troubleshooting: Sage Intacct ETL Error - A Request’s Function With the Control ID Is in Process – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/26727976485133-Troubleshooting-Sage-Intacct-ETL-Error-A-Request-s-Function-With-the-Control-ID-Is-in-Process 6/6
