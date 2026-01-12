# (Troubleshooting)   ETL – There Are Missing Records in the Batch

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
ETL JobsTroubleshooting: ETL – There Are
Missing Records in the Batch
Issue summary
When running an ETL job that references a Sage Intacct data feed, you may get an error "There
are missing records in the batch. Please check for any jobs running on Intacct that could be changing
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 1/6

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
Companythe data and re-run when Intacct data is stable".
Suggested solution
1. Check your Sage Intacct instance and ensure you are not currently making changes or
manipulating records while running an ETL job in Vena.
2. If you are currently manipulating records in Sage Intacct, finish making your changes.
3. Once completed in Sage Intacct and the data is now stable, go back to Vena and re-run the
ETL job.
Cause
This may happen if you are manipulating records in Sage Intacct while simultaneously running
an ETL Import Job into Vena.
Keywords
sage, intact error, etl error, missing records, intact data stable.  05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 2/6

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
Records Than ExpectedWas this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Sage Intacct ETL Error Unable to parse Query value: X != 'X'
Troubleshooting: Sage Intacct ETL Error There’s an Error With the Value for Field STATE. Value:
[P]
Troubleshooting: Sage Intacct ETL Error There Are Too Many Operations Running for This
Company
Explainer: Sage Intacct Connector Update
How-To: Set Up a Sage Intacct Connector and Data Feed05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 3/6

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
Channel Mapping With Map by05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 4/6

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
Submit a Request05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 05/01/2026, 12:48 Troubleshooting: ETL – There Are Missing Records in the Batch – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/23666967322125-Troubleshooting-ETL-There-Are-Missing-Records-in-the-Batch 6/6
