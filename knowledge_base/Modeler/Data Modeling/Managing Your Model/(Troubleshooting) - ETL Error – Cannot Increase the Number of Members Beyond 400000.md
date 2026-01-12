# (Troubleshooting)   ETL Error – Cannot Increase the Number of Members Beyond 400000

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Managing Your Model Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
Managing Your Model
Explainer: What is Data Model
Standardization?
How-To: Build Your Chart of
Accounts Hierarchy in QuickTroubleshooting: ETL Error – Cannot
Increase the Number of Members
Beyond 400000
Issue summary
When running an ETL Job with a hierarchy upload you may come
across the following error:
Miguel Buan
Updated 1 year ago
02/01/2026, 14:20 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyond-400000 1/5

Start
How-To: Formatting an Excel-
Based CSV to Maintain Leading
Zeros for ETL Jobs
How-To: Data Model Series
(Part 1): Creating a Data Model
How-To: Data Model Series
(Part 2): Hierarchies and Roll-
Ups
How-To: Data Model Series
(Part 3): Attributes and
Versioning
How-To: Data Model Series
(Part 4): ETL Tool
How-To: Build and Manage
Data Models in Modeler
How-To: Building Alternate
Hierarchies
How-To: Adjusting How Vena
Treats Zero Values in the
Database
How-To: Creating a Testing
Environment by Cloning a Data
Model (Clone & Remap)Exceeded max allowable row errors (1 invalid rows). Last at row xxxxx:
Cannot increase the number of members beyond 400000
Suggested solution #1
1. Review the data model for members that are no longer being used.
2. Remove these members to make space for the new ones.
Suggested solution #2
Redesign the data model to move the bulk dimension into the value dimension. This treats the
members as values to save space in the data model.
If assistance is required when doing so, reach out to your Customer Success Manager to connect
with the Professional Services team.02/01/2026, 14:20 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyond-400000 2/5

How-To: Undo a Versioning ETL
Job Without Line-Item Details
How-To: Undoing a Versioning
ETL job with Line-Item Details
(LIDs)
How-To: Downloading All Vena
Data From Your Tenant or
Environment
Troubleshooting: The Bulk Copy
Parameters Were Invalid
Troubleshooting: This Member
Does Not Exist Error During
Modeler Search
Troubleshooting: ETL Error –
Cannot Increase the Number of
Members Beyond 400000
Troubleshooting: Encountered
More Than the Limit of 1000
Unmapped Members
Functions
Calcs (Scripts)
Data Transformation &
Integration
AdminCause
There is a limit of 400,000 members per data model. Attempting to load more members gives
this error. Visit this article for more information on maximum members and member characters.
Keywords
etl, error, hierarchy, max, rows, invalid, increase, members
Was this article helpful?
0 out of 0 found this helpful
Related articles
Troubleshooting: Encountered More Than the
Limit of 1000 Unmapped Members
Troubleshooting: ETL Error GuideRecently viewed articles
Troubleshooting: This Member Does Not Exist
Error During Modeler Search
Troubleshooting: The Bulk Copy Parameters
Were Invalid
How-To: Downloading All Vena Data From
Your Tenant or Environment
How-To: Undoing a Versioning ETL job with02/01/2026, 14:20 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyond-400000 3/5

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesLine-Item Details (LIDs)
How-To: Undo a Versioning ETL Job Without
Line-Item Details
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:20 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyond-400000 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:20 Troubleshooting: ETL Error – Cannot Increase the Number of Members Beyond 400000 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20125010992525-Troubleshooting-ETL-Error-Cannot-Increase-the-Number-of-Members-Beyond-400000 5/5
