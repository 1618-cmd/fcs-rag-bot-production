# (Reference)   Business Central Data Filtering

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Business Central Integration Search
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
ETL JobsReference: Business Central Data
Filtering
Overview
With Dynamic Date filters for Business Central, you can use dynamic variables to “set and forget”
a filter without updating when the month or year rolls over. There are two filters available,
currentMonth and currentYear:
Vena Support Team
Updated 2 months ago
05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 1/10

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
How-To: Set Up a Business
Central Connector and Data
Feed
Reference: Business Central
Advanced Data Types
Reference: Business Central
Data Filtering
How-To: Downloading the
Business Central Vena
Extension
Reference: Business Central
Connector Custom Extension
Fields
Troubleshooting: Vena Data
Feed Not Connecting to
Business Central Extension
Troubleshooting: The Record in
Table Vena Trial Balance BuffercurrentMonth: This filter uses the number value of the current month and year at the time a
request is submitted (e.g., Jan 2025) and returns results based on that filter expression.
currentYear: This filter uses the number value of the current year at the time a request is
submitted (e.g., 2025) and returns results based on that filter expression.
Before you begin
To use the Dynamic Date Filters in Business Central, you must first install the Business Central
Vena Extension and have Modeler access in vena.io. Learn how to install the extension.
Table of contents
Reference Guide
Supported OData filters
Available Dynamic Variables
currentMonth
currentYear
Filter examples
How to
Filter Trial Balance data types
Filter example for Trial Balance data feed
Limitations
Reference Guide05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 2/10

Already Exists. Identification
Fields and Values
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
How-to: Vena Integration: Part 4
– Import and Export API
How-to: Vena Integration: Part 5 -
DestinationsSupported OData filters
Vena follows the OData standard and supports the following logical operators:
OData
filter*Description
lt The lt operator returns true if the left operand is less than the right operand,
otherwise, it returns false.
gt The gt operator returns true if the left operand is greater than the right operand,
otherwise, it returns false.
le The le operator returns true if the left operand is less than or equal to the right
operand, otherwise, it returns false.
ge The ge operator returns true if the left operand is greater than or equal to the
right operand, otherwise, it returns false.
eq The eq operator returns true if the left operand is equal to the right operand,
otherwise, it returns false.
and The and operator returns true if both the left and right operands evaluate to true,
otherwise, it returns false.
or The or operator returns false if both the left and right operands both evaluate to
false, otherwise, it returns true.
*These OData filters are case sensitive and should always be written in lowercase.05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 3/10

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
Product UpdatesAvailable Dynamic Variables
There are two Dynamic Date variables available, currentMonth and currentYear. In the following
section, we’ll look at some examples of how they can be used.
currentMonth
This Dynamic Variable represents the current month of the current year.
Sample filters
Note
To learn more about logical operators in OData filters, see OData Version 4.0. Part 2:
URL Conventions Plus Errata 03.
Note
Both currentMonth and currentYear are written in camelCase and are case- sensitive.05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 4/10

currentMonth() = current month
currentMonth(-1) = previous month
currentMonth(-2) = 2 months ago
Example: The current date is January 2025
currentMonth(-2) = November 2024
currentYear
This Dynamic Variable represents the current year.
Sample filters
currentYear() = current year
currentYear (-1) = previous year
currentYear (-2) = 2 years ago
Example: The current date is December 2024
currentYear(-1) = 202305/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 5/10

Filter examples
Dynamic Date filter Data Selected
postingDate gt
currentMonth(-2)If the data feed runs in June, “-2” will be applied to that to get April
(the fourth month of the year). The “gt” (greater than) filter retrieves
records with a posting date greater than April 2024 or all records
from May 2024 and later.
This filter retrieves all records with a posting date in either the
current month or the month before the current month as of the time
it runs.
postingDate ge
currentYear(-2)If the data feed runs in 2024, “-2” will be applied to that to get 2022.
The “ge” (greater than or equal to) filter will retrieve records with a
posting date greater than or equal to 2022 or all records from 2022
and later.
dateFilter ge
currentMonth(-3) andIf the data feed runs in June, the first part of the filter “-3” will be
applied to that date (June) to get March (the 3rd month of the year).
The “ge” (greater than or equal to) filter retrieves records with a date05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 6/10

dateFilter lt
currentMonth()filter value greater than March 2024 or all records from March 2024
and later.
For the second part of the filter, “lt” (less than) will be applied to the
current month (June) to get all records with a date filter value that is
less than June 2024. As a result, this filter will return all records from
March 2024 up to but not including June. The records returned will
be from March, April, and May 2024.
dateFilter ge
currentMonth(-1) and
dateFilter le
currentMonth()This Trial Balance data feed setup will only pull the last month of
data. This filter will include all data from the previous month (e.g., if
run in August, then it will return data from July 1 to July 31). If setup
correctly, your data loads should speed up and require no manual
updates.
How to
Filter Trial Balance data types
Trial Balance is one of the available data types in a Business Central data feed. Unlike General
Ledger and Advanced, it only supports limited OData filters for Dynamic Date filters. Only the le
(less than or equal to) and eq (equal to) operators are allowed—using any others will cause an
error.
Supported operators:05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 7/10

le
eq
Unsupported operators:
lt
ge
gt
and
or
Filter example for Trial Balance data feed
Dynamic Date filter Notes
dateFilter le/eq
currentMonth(-1)This correct filter will return ending balances from the last month
based on the dateFilter field.
Limitations
currentMonth and currentYear cannot be used in the same filter expression in a data feed.
Since Trial Balance values are a range starting with the first entries in a General Ledger, the
Trial Balance data type only supports the le OData operator for dates. Using any other OData
operator will result in an error. Please refer to the "How to Filter Trial Balance data types"
section for more information.05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 8/10

Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Set Up a Business Central Connector
and Data Feed
Reference: Business Central Advanced Data
Types
How-To: Downloading the Business Central
Vena Extension
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
How-To: Setting Up a NetSuite Connector and
Data FeedRecently viewed articles
Reference: Business Central Advanced Data
Types
How-To: Set Up a Business Central Connector
and Data Feed
Troubleshooting: ETL Load Produces “Invalid
Char Between Encapsulated Token and
Delimiter” Error
Troubleshooting: ETL Data Load With Bulk
Insert Option Does Not Import Commas (,)
Correctly
Troubleshooting: Upload Via ETL Tool Causes
Out of Memory Exception05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:22 Reference: Business Central Data Filtering – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/28903592986125-Reference-Business-Central-Data-Filtering 10/10
