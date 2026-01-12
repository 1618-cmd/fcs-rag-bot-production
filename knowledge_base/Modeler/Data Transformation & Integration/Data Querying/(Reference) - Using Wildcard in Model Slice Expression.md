# (Reference)   Using Wildcard in Model Slice Expression

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Data Querying Search
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
ETL JobsReference: Using Wildcard in Model
Slice Expression
Use Wildcard in Model Slice Expressions to specifically export intended intersections.
Reference
You can use a wildcard when exporting intersections in ETL.
Jun Barrozo
Updated 3 years ago
02/01/2026, 16:50 Reference: Using Wildcard in Model Slice Expression – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212548386-Reference-Using-Wildcard-in-Model-Slice-Expression 1/5

Data Querying
How-To: Using the Query Agent
to Build MQL Expressions (Beta)
Reference: Writing Expressions
(MQL & HQL)
Reference: Using Wildcard in
Model Slice Expression
Troubleshooting: ETL Export
MQL Query Returning No Data
How-To: Creating Advanced
Integration Setups With VenaQL
Troubleshooting: MQL Invalid
Expression Syntax When
Creating a Calculated Member
Troubleshooting: ETL Error
Guide
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite IntegrationFor example, if you want to export all the intersections where the Account ends in '08', the
syntax would be:
dimension('Account':'*08')
You can use the wildcard at the end or at the start of the member name, however, you cannot
use both at the same time.
Was this article helpful?
2 out of 2 found this helpful
Related articles
Video Resource: Creating and Using Wildcard
Mappings (Vena 365 Only)Recently viewed articles
Reference: Writing Expressions (MQL & HQL)
Note
If the name matches exactly, that will cancel the wildcard functionality. If you happen
to have a member called exactly *08 then there's no way to search for members
ending in 08 anymore.02/01/2026, 16:50 Reference: Using Wildcard in Model Slice Expression – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212548386-Reference-Using-Wildcard-in-Model-Slice-Expression 2/5

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
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten orHow-To: Using the Query Agent to Build MQL
Expressions (Beta)
How-To: Creating Advanced Integration
Setups With VenaQL
How-To: Combining Dimensions Using
Multiple Expressions for Slices to Clear
Troubleshooting: ETL Export MQL Query
Returning No DataHow-To: Using the Query Agent to Build MQL
Expressions (Beta)
How-To: Checking the ETL Tool Version
How-To: Setting up Email Notifications for ETL
Jobs
How-To: Maintaining Dimension Member IDs
When Updating Existing Members02/01/2026, 16:50 Reference: Using Wildcard in Model Slice Expression – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212548386-Reference-Using-Wildcard-in-Model-Slice-Expression 3/5

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
Product Updates
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:50 Reference: Using Wildcard in Model Slice Expression – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212548386-Reference-Using-Wildcard-in-Model-Slice-Expression 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:50 Reference: Using Wildcard in Model Slice Expression – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212548386-Reference-Using-Wildcard-in-Model-Slice-Expression 5/5
