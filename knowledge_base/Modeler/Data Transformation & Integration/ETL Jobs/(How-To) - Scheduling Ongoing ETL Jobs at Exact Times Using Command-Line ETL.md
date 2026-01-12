# (How To)   Scheduling Ongoing ETL Jobs at Exact Times Using Command Line ETL

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs Search
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
ETL JobsHow-To: Scheduling Ongoing ETL
Jobs at Exact Times Using Command-
Line ETL
Automatically run ETL jobs or schedule a data upload into Vena at a specific time instead of
using time brackets.
Olalekan Adebayo
Updated 9 days ago
02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 1/11

ETL Job Errors &
Troubleshooting
Reference: ETL Guide - 1 -
Overview
Reference: ETL Guide - 2 -
Vena.io ETL
Reference: ETL Guide - 3 -
Command Line ETL
Reference: ETL Guide - 4 -
Query Languages
Reference: ETL Guide - 5 - SQL
Staging Environment
Reference: ETL Guide - 6- Using
Staging Data
How-To: Exporting Data From a
SQL Staging Table
How-To: Create and Manage a
Data Model Hierarchy Using
ETL Import
How-To: Exporting a Subset of
Data From Your Data Model or
Cube
Reference: Additional Security
Restrictions to the SQL WHEREWhy use this feature?
Currently, our native ETL job scheduler is only available for ETL jobs that do not require a source
file and only allows you to select time brackets (e.g., 12 AM - 5:59 AM or 6 AM - 11:59 AM, etc.) to
run your ETL jobs. With the steps outlined here, you will be able to select the specific times you
want your ETL jobs to run automatically.
Before you begin
You need to have at least Modeler access in Vena and a
dmin access to the computer/server where your ETL jobs will run from. You will also need access
to the Task Scheduler on the computer or server.
How to
Note
If you are looking to automatically run an ETL job that does not require a source file
(CSV, TDF, PSV), skip to Step 2.02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 2/11

Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Using
Command-Line ETL
How-To: Automatically Run ETL
Templates Using the ETL
Scheduler
How-To: Checking if My File Has
a Header Row or Not
How-To: Exporting CSV Files for
ETL Job
How-To: Use Clear Slices to
Clear Intersections During an
ETL Load
How-To: Maintaining
Dimension Member IDs When
Updating Existing Members
How-To: Setting up Email
Notifications for ETL Jobs
How-To: Checking the ETL Tool
Version
Data QueryingAutomatically run ETL jobs or import data into Vena at
specific times
Step 1
Get your computer or server set up for our ETL Command-Line tool and prepare your CSV file.
You must work with your IT team to generate your source file from your SQL server/external
system and then place it in a folder. You will have to know how often the file is generated and
around what time, as this is crucial for the Task Scheduler step.
Step 2
Prepare your ETL script and make it a batch (.bat) file. See Reference: ETL Guide - 3 - Command
Line ETL on how to write the script.
Example:
You can create an ETL job "File to Staging Table" and then write a script to run the ETL template -
-runTemplate="template ID" and supply the path to the CSV file. This will automatically upload
the provided source file into the Vena staging table automatically.
Note
You can create other types of ETL jobs too. Visit this article on command line ETL for
more details. You can also automatically run ETL jobs that do not require an actual
source file (e.g., ETL with SalesFoce, Sage Intacct, NetSuite sources).02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 3/11

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
Salesforce Integration
Troubleshooting Data
Transformation
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feeds
& ConnectionsStep 3
Create a Windows Task Scheduler to run the batch script from Step 2 automatically at set times.
You will also have to create a Windows Task Scheduler to run the batch script at different
intervals throughout the day (depending on what you want).
The interval will depend on how often your SQL server/external system is creating the CSV file in
the appropriate folder.
The idea is to set the task to run about 15-30 minutes after the CSV file is created to allow
enough buffer time in case your SQL server/external system doesn't generate the file on time.

Example of how to run a template automation ETL job at a
specific time
1. Visit this article to get your computer compatible with the Vena Command-Line ETL tool.
2. To prepare the batch file to run the ETL template Financial Model Save Data, the batch file
should look like this (Note: u = YOUR EMAIL and p=YOUR PASSWORD used for Vena or you
could also use an Application Token)
Batch File: financialModelSaveDate.bat
java -jar etl.jar -u=admin@abc.com -p=password --modelName="Finance" --runTemplate
"1296401193807642625"
Note: Ensure that there isn’t already a Job Schedule created since we will be using the
Windows Task Scheduler to schedule this ETL job.02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 4/11

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
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
3. Create a Task Scheduler that runs the batch file every day at 7:30 AM.
4. Create a Windows task scheduler to run this batch file (financialModelSaveDate.bat) every
day at precisely 7:30 AM. You can work with your IT team on this.
Here's a YouTube video showing how to create a Windows Task Scheduler.
5. Use the following sample Task Scheduler setup:
General tab: This is where the ETL name is entered, and you can specify if it should run
whether the user is logged in or not.02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 5/11

02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 6/11

Triggers tab: This is where we set up the schedule.
Actions tab: This is specified in the Task Scheduler what to do. In our case, we are setting
it up to run a program and execute the batch.02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 7/11

02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 8/11

Conditions tab: This is where we set conditions on when this task can or should run.
Check the Settings tab and ensure that the History tab is enabled, as it will be useful
when troubleshooting issues with the Task Scheduler.
Notes & best practices
Ensure the user account attached to the Task Scheduler has Admin access. 02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 9/11

The computer or server should always be turned ON so the task can kick off at the
appropriate times.
Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: ETL Guide - 3 - Command Line ETL
How-To: Automatically Run ETL Templates
Using the ETL Scheduler
Explainer: ETL Export Feature Updates
Reference: Vena Calcs - 2 - Notation and
Syntax
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple ReportsRecently viewed articles
Explainer: ETL Export Feature Updates
Reference: Additional Security Restrictions to
the SQL WHERE Clause
How-To: Exporting a Subset of Data From
Your Data Model or Cube
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
How-To: Exporting Data From a SQL Staging
Table02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:45 How-To: Scheduling Ongoing ETL Jobs at Exact Times Using Command-Line ETL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14234493839245-How-To-Scheduling-Ongoing-ETL-Jobs-at-Exact-Times-Using-Command-Line-ETL 11/11
