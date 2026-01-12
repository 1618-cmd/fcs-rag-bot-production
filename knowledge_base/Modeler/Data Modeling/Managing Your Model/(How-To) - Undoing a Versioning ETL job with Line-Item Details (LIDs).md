# (How To)   Undoing a Versioning ETL job with Line Item Details (LIDs)

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
Accounts Hierarchy in QuickHow-To: Undoing a Versioning ETL
job with Line-Item Details (LIDs)
Why use this feature?
When we mistakenly run an unintended versioning job, it is important that we undo it properly
to avoid having duplicate or stale data in the cube since versioning involves the creation of new
ETL jobs.
Olalekan Adebayo
Updated 4 months ago
02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 1/9

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
Model (Clone & Remap)Before you begin
You will need at least Modeler access to follow the steps in this article
The clear slice columns in the configuration will be based on the “Page Filter” parameters used in
the versioning job and then the destination parameter.
Table of contents
Undo a Versioning ETL job with Link to originals Selected
Undo a Versioning ETL job with Make Separate Copies Selected
Notes
Warning
Be careful when using Clear Slices. Versioning jobs create new intersections, and we
need a way to delete those newly created intersections when we want to undo the
job by using a historical export.02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 2/9

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
AdminHow to
Undo a Versioning ETL job with Link to originals  Selected
This is the same as undoing a versioning ETL job with No Line-Items deleted. This is because we
only want to delete these newly created intersections but not the Line-Item Details they are
linked to. When you delete or update Line-Item Details that are linked to multiple intersections,
all the linked intersections will be affected.
To undo a versioning ETL job with Link to originals selected, please visit this article.

Undo a Versioning ETL Job with Make Separate Copies  Selected
Step 1: Export LIDs for parameters before Versioning
Let's use this versioning ETL job as an example of what we want to undo.
Filter: Year = 2024 and Periods = 10, 11, 1202/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 3/9

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesFrom: Reforecast
To: Q2 Reforecast
Use the dimensions in the page filter (the year 2024, periods 10, 11, 12) and the destination
(scenario Q2 Reforecast) to build an MQL query for your ETL export. This export will be for Line-
Item Details. We will also pick a time before the versioning job was run.
1. Select the same date but five minutes before you ran the ETL job.
2. Select Export
3. Save this file as All-LIDs-For-This-Parameter-Before-Versioning.csv.
Step 2: Export LIDs for parameters after Versioning
1. Perform another ETL export of LIDs with the same query but this time will be the live data
and not the historical data.02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 4/9

2. Save this file as All-LIDs-For-This-Parameter-After-Versioning.csv.
3. Open the exported CSV file from Step 2 in Notepad++ or Excel. If you use Excel, be careful
that the leading 0s for dimension members are not removed.
4. Change the values in the “_cmd” column from + (plus) to - (minus) since we are trying to
delete those LIDs.
5. Save the CSV file.
Note
Do not make any changes to the CSV file (All-LIDs-For-This-Parameter-Before-
Versioning.csv) from Step 1. 02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 5/9

Step 3: Create a File to Cube ETL job
1. Create a File to Cube ETL job that will be used to reload the LID CSV files back into the cube.
2. Set the data type for this ETL job to Line-Item Details.
3. Upload the CSV file All-LIDs-For-This-Parameter-After-Versioning.csv with the ETL job created
above. This will delete all the current LIDs for these intersections. Confirm that these LIDs
were in fact deleted before going to the next step. 02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 6/9

4. Upload the CSV file All-LIDs-For-This-Parameter-Before-Versioning.csv with the same ETL job
created above. This will re-add all the LIDs that were in the cube before the versioning job for
these intersections.
5. We have now successfully deleted the new LIDs that were created by the versioning job and
re-added LIDs that were in the cube before the versioning job. Verify this by doing an ETL
export of LIDs to confirm.
6. Now that we have successfully deleted those LIDs linked to the newly created intersections
by the versioning ETL job, we want to undo a versioning job without LIDs. Learn more about
undoing a versioning job without Line-Item Details in this article.
7. Check your reports and data to confirm that everything looks good.
Notes
These steps should only be used to undo versioning ETL jobs where No Line Items was
selected.
Clear Slice can cause data deletion. It is important that be cautious when doing this.
When doing a versioning job with Make Separate Copies selected, it is important to follow the
steps in the order outlined.
Was this article helpful?
1 out of 1 found this helpful02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 7/9

Related articles
How-To: Enabling Line Item Details (LIDs) in a
Template or Report
How-To: Using Line-Item Details (LIDs) as a
Contributor
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
How-To: Enable & Add a MDR Insert Row to a
TemplateRecently viewed articles
How-To: Undo a Versioning ETL Job Without
Line-Item Details
How-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)
How-To: Adjusting How Vena Treats Zero
Values in the Database
How-To: Building Alternate Hierarchies
How-To: Build and Manage Data Models in
Modeler
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 14:19 How-To: Undoing a Versioning ETL job with Line-Item Details (LIDs) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17163939866381-How-To-Undoing-a-Versioning-ETL-job-with-Line-Item-Details-LIDs 9/9
