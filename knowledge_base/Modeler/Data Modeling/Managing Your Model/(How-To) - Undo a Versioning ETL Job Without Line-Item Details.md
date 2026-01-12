# (How To)   Undo a Versioning ETL Job Without Line Item Details

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
Accounts Hierarchy in QuickHow-To: Undo a Versioning ETL Job
Without Line-Item Details
Avoid duplicate versioning jobs without Line-Item Details by undoing them.
Why use this feature?
Olalekan Adebayo
Updated 4 months ago
02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 1/11

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
Model (Clone & Remap)When we mistakenly run an unintended versioning job, it is important that we undo it properly
to avoid having duplicate or stale data in the cube.
Before you begin02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 2/11

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
AdminYou must have at least Modeler access to follow the steps in this article.
Table of contents
How to
Notes & best practices
How to
Undo a Versioning ETL job
We'll use this example as the data in this guide--follow along with your own data.
Filter = Year 2022 and Periods 10, 11, 12
From: Reforecast
To: Q2 Reforecast02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 3/11

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates1. Use the dimensions in the page filter (the year 2022 and periods 10, 11 and 12) and the
destination (scenario Q2 Reforecast) to build an MQL query for your ETL export.
2. Navigate to Data Modeler > Export and set the Manual Query toggle to ON.
3. Build an MQL query for your export under Export if following condition is true. Use the
dimensions in the page filter (the year 2022 and periods 10, 11 and 12) and the destination
(scenario Q2 Reforecast).
Note
We are only using the destination dimension in addition to the page filter for the
query since that is what we want to restore. We are not using the source
dimension.02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 4/11

02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 5/11

4. Select Advanced Options.
5. Check the box next to Export data from a date and time in the past, then enter the date
and time. Choose a time before the versioning job was run. Since the versioning job ran at
4:12 AM, we will export data from 4:10 AM. Then select Save.02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 6/11

02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 7/11

6. Select Export.
7. Navigate to Data Modeler > ETL Templates and create a File to Cube ETL job to reload the
data back into the cube.
Note
This ETL job must have a Clear Slice configuration. The columns will correspond to
the dimensions used in the page filter and the destination of the versioning
parameters. The Clear Slice will ensure the historical data is restored and any
newly created intersection as a result of that versioning job is also deleted.
Learn more about using Clear Slices to clear intersections during an ETL02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 8/11

8. Once the job is complete, the versioning ETL job has been undone or reverted.
9. Check your reports and data to confirm everything is correct.
Notes & best practices
load.
For this example, the clear slice will be Year, Period and Scenario. This will differ
based on the versioning job you are working with.02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 9/11

This should only be used to undo versioning ETL jobs where No Line-Item Details were
selected.
Clear Slices delete data (mostly old data), so be cautious that you aren't deleting something
you don't want to.
Versioning jobs create new intersections, which must be deleted when you want to use a
historical export to undo the job, so be cautious when using Clear Slices.
Was this article helpful?
0 out of 1 found this helpful
Related articles
How-To: Undoing a Versioning ETL job with
Line-Item Details (LIDs)
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
Reference: Writing Expressions (MQL & HQL)
How-To: Enable & Add a MDR Insert Row to a
Template
How-To: Restoring Data That Has Been
Accidentally Overwritten or DeletedRecently viewed articles
How-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)
How-To: Adjusting How Vena Treats Zero
Values in the Database
How-To: Building Alternate Hierarchies
How-To: Build and Manage Data Models in
Modeler
How-To: Data Model Series (Part 4): ETL Tool02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:19 How-To: Undo a Versioning ETL Job Without Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14233953668109-How-To-Undo-a-Versioning-ETL-Job-Without-Line-Item-Details 11/11
