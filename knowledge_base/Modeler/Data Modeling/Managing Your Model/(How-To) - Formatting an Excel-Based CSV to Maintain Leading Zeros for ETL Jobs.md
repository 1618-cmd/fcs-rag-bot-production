# (How To)   Formatting an Excel Based CSV to Maintain Leading Zeros for ETL Jobs

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
Accounts Hierarchy in QuickHow-To: Formatting an Excel-Based
CSV to Maintain Leading Zeros for
ETL Jobs
Closing and re-opening your Excel-based CSV files may result in a loss of leading
zeros. Read this article to learn how to format an Excel-based CSV to maintain leading
zeros.
Olalekan Adebayo
Updated 7 months ago
02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 1/6

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
Model (Clone & Remap)Why use this feature?
If you have dimension members with leading zeros (0055, 00100, 098899, etc.), there is an Excel
limitation that suppresses them and causes the ETL job to unintentionally create new dimension
members. You'll need to edit your CSV file in Excel to maintain the leading zeros.
How to
Format an Excel-based CSV file to maintain leading zeros
1. Open the file in Excel.
2. Select all the cells or columns that should have leading zeros.
3. Right-click on the selection.
4. Select Format Cells…
5. Select Custom from the Category options.02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 2/6

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
Admin6. Select #,##0.
7. In the Type: field, enter in the number of leading zeros you want. For example, if you want
only one leading zero, enter 0#,##0. If you want two leading zeros, then enter 00#,##0.02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 3/6

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
8. Select OK.
9. Save the file. There are now leading zeros in the cells you specified.
10. To confirm that leading zeros are present, open the file in Notepad and it should have the
leading zeros.
Notes02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 4/6

Making this formatting change to have leading zeros should be done once all editing in the
file is complete, as reopening the Excel file may cause the leading zeros to be suppressed
again.
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Data Model Series (Part 1): Creating a
Data ModelRecently viewed articles
How-To: Build Your Chart of Accounts
Hierarchy in Quick Start
How-To: Data Model Series (Part 1): Creating a
Data Model
Explainer: What is Data Model
Standardization?
Troubleshooting: Versioning Copy To and
Copy From Must Be Bottom-Level Members
Troubleshooting: Versioning Copy To and
Copy From must Contain the Same Set of
Dimensions02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:14 How-To: Formatting an Excel-Based CSV to Maintain Leading Zeros for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233859678989-How-To-Formatting-an-Excel-Based-CSV-to-Maintain-Leading-Zeros-for-ETL-Jobs 6/6
