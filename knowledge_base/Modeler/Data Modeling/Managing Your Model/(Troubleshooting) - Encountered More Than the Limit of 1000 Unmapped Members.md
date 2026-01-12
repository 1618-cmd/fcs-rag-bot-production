# (Troubleshooting)   Encountered More Than the Limit of 1000 Unmapped Members

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
Accounts Hierarchy in QuickTroubleshooting: Encountered More
Than the Limit of 1000 Unmapped
Members
Issue summary
When running an ETL job, you may encounter the following error:
Marjana
Updated 2 years ago
02/01/2026, 14:21 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Members 1/5

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
Model (Clone & Remap)Encountered more than the limit of 1000 unmapped members. Please use a hierarchy export to
create more than 1000 members.
Suggested solution
This error is returned when too many new dimension members are added during an
intersection ETL load.
There are two possible reasons why you might see this error:
1. These dimension member names should already exist.
This is common with leading 0s in your member names. For example, if your member names
have leading 0s (e.g., 011, 012, 033, etc.) but your source file is missing the leading 0s (e.g., 11,
12, 33), this causes an issue since "011" is different from "11". The system will try to create a
new member "11" instead of loading the data into the already existing member "011". To fix
this, correct the source file by ensuring the dimension member names are correct, have the
correct format and re-upload it.
2. These dimension member names are actually new and did not exist before the
intersection load.02/01/2026, 14:21 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Members 2/5

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
Admin1.In this case, the fix is to first upload the member names into your hierarchy and then re-
run the intersection load so the system knows where to save the data.
2.Prepare your hierarchy import file to add the new members to your data model.
3.Create a new ETL job with hierarchy import into the cube.
4.Run the hierarchy ETL job created above to import new dimension members. This will
ensure they reside in your data model hierarchy.
5.Re-run the original intersection load ETL job.
Cause
This may occur if there are too many new dimension members while importing data via an ETL
job.
Keywords
etl job error, too many unmapped members error 02/01/2026, 14:21 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Members 3/5

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesWas this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Vena’s Foreign Exchange (FX)
Conversion Function FAQsRecently viewed articles
Troubleshooting: ETL Error – Cannot Increase
the Number of Members Beyond 400000
Troubleshooting: This Member Does Not Exist
Error During Modeler Search
Troubleshooting: The Bulk Copy Parameters
Were Invalid
How-To: Downloading All Vena Data From
Your Tenant or Environment
How-To: Undoing a Versioning ETL job with
Line-Item Details (LIDs)02/01/2026, 14:21 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Members 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:21 Troubleshooting: Encountered More Than the Limit of 1000 Unmapped Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20074506822157-Troubleshooting-Encountered-More-Than-the-Limit-of-1000-Unmapped-Members 5/5
