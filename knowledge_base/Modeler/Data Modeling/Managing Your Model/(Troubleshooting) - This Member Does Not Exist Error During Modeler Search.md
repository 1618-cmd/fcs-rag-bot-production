# (Troubleshooting)   This Member Does Not Exist Error During Modeler Search

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
Accounts Hierarchy in QuickTroubleshooting: This Member Does
Not Exist Error During Modeler
Search
Issue summary
When searching in the Modeler tab, you may receive the following error message:
Omair Riasat
Updated 2 years ago
02/01/2026, 14:20 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 1/5

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
Model (Clone & Remap)This member does not exist in XXXXXXX
Suggested solution
If you are not a Vena Admin you will need the assistance of a Vena Admin to help you follow the
steps below.
1. Navigate to the Admin tab and check the User Groups assigned to your account.
2. Check each User Group you or the affected user are assigned to ensure that there are no
restrictions on the dimension that you search in when receiving the error. If there are, amend
the data permissions. Keep in mind that any changes to data permissions will affect all users
that belong to the same User Group.
3. If there are no restrictions in any of the User Groups for the dimension you’re searching for,
check to see if the dimension is linked.
In the Modeler tab, select the chain icon next to the dimension name.
4. If it is a linked dimension, you will need at least Read access to all data models that this
dimension is linked to. For further information on managing data permissions, please see
this article.
Cause
This error can occur if there are restrictions on data permissions or if there are linked
dimensions where the user does not have Read access to all linked data models.02/01/2026, 14:20 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 2/5

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
AdminKeywords
modeler search, search function, unable to search, member not found, member does not exist,
modeler tab
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Add Images to Vena Insights
Dashboards
Troubleshooting: ETL Error – Cannot Increase
the Number of Members Beyond 400000
Troubleshooting: ETL - Member "" Not Found
in DimensionRecently viewed articles
Troubleshooting: The Bulk Copy Parameters
Were Invalid
How-To: Downloading All Vena Data From
Your Tenant or Environment
How-To: Undoing a Versioning ETL job with
Line-Item Details (LIDs)
How-To: Undo a Versioning ETL Job Without
Line-Item Details02/01/2026, 14:20 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 3/5

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesHow-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:20 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:20 Troubleshooting: This Member Does Not Exist Error During Modeler Search – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/21567965458061-Troubleshooting-This-Member-Does-Not-Exist-Error-During-Modeler-Search 5/5
