# (Troubleshooting)   ETL Job Completed Successfully But No Data Is in the Cube

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs
/ETL Job Errors & TroubleshootingSearch
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
ETL JobsTroubleshooting: ETL Job Completed
Successfully But No Data Is in the
Cube
Issue summary
You may run an ETL job with your source file and the job may complete successfully with no
errors, but no data will be added, updated or deleted.
Olalekan Adebayo
Updated 3 months ago
05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 1/9

ETL Job Errors &
Troubleshooting
Troubleshooting: ETL Job
Error – Job Was Skipped as It
Was Already
Queued/Waiting/Running
Troubleshooting: Connection
Timed Out Error When Using
the ETL Command Line Tool
Troubleshooting: ETL Error
"There were only X members
in this row. Was expecting X
members (or 0 If deleting all
LIDs for a unique etl_id/label
/row)"
Troubleshooting: Error
Processing Workbook:
xxx.xlsx Error While
Processing the Model
Expression
Troubleshooting: The File is
too Large and Cannot be
Exported Error when Using
ETL Export
Troubleshooting ETL error:
You cannot create external
IDs starting with ‘#’.
Suggested solution
1. Ensure that you, the account or the application token used has the necessary data
permissions. Some times new tokens are created without any data permissions. This could
also cause an issue where the ETL job will delete data (via Clear Slice) but won't save the new
data that is loaded.05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 2/9

Troubleshooting: Error Invalid
Input for ETL and VenaQL
Troubleshooting: ETL Vena
Table Does Not Contain the
Clear Slices Column ‘Column
Name’
Troubleshooting: Conversion
Failed When Converting Date
and/or Time From Character
String
Troubleshooting: ETL Job Is
Stuck in Waiting for SQL
Transformation
Troubleshooting: ETL Job Is
Creating or Loading Data Into
an Unmapped Folder
Troubleshooting: ETL Jobs
Getting Stuck in SQL
Transform Step When IP
Filtering Is Enabled
Troubleshooting: Invalid
Member Name for Dimension
(X): Name Is Blank
Troubleshooting: Duplicate
Rows in Staging Query Sheet
If you are manually running the job or using a username and password combination in your
batch script, have your Vena Admin check your data permissions settings.
2. Ensure that you are not loading zero values into those intersections. If your environment has
Retain zeros for this model set to OFF and you load a file with just zero values, if the
intersections exist then they will be deleted. If the intersections do not exist, nothing will be05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 3/9

Troubleshooting: Some Data
Has Not Loaded After
Running an ETL Job With
Integration Channels
Troubleshooting: Staging
Query Pulling Incomplete
Information
Troubleshooting: The
Maximum Number of ETL
Errors Allowed Was Exceeded.
Dimension X Already Has a
Member Named X
Troubleshooting: ETL
Uploaded Values Are Going
Into an Undefined Member
Troubleshooting: ETL
Combined Clear Slices
Operation Contains
Overlapping Dimension With
an Empty Intersection
Troubleshooting: Template
Automation Failed Validation
Rules Cell: X Failed Validation
See all 89 articles
Reference: ETL Guide - 1 -
Overviewwritten into the cube since you are not retaining zeros.
3. If your ETL job has an integration channel that is using a SUM for its aggregation mode, open
the file and ensure there are no double quotes or commas for the values. The system will
treat them as text. Since you can't sum text values, it will save nothing into the cube.
Rules to follow:
dots ( . ) and negative ( - ) are allowed
commas ( , ) and double-quotes ( "" ) and brackets ( () ) are not allowed.
4. Check the intersections that are being loaded and ensure they are not part of a calc target.
We are not able to load or manually save data into calc targets (i.e., intersections that are
being calculated by our calc script). An exception here would be if your organization has
enabled the flag to allow data to be saved on top of calc targets.
The easiest way to determine this would be to check your calc scripts or map a bottom-level
intersection from your source file. Perform a Drill Save, if you see a Drill Calc button, then it05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 4/9

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
Restrictions to the SQL WHERE
Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Usingmeans that the intersection is a calc target intersection and the data can only be saved via a
calc script. The solution is to load the data into the source target instead and then the calc
target is automatically re-calculated.
5. When Zeroing out an intersection(s), ensure the format of all the dimensions from the source
file match what is in the cube.
For example, We would like to clear or zero out the intersection below.
But the source file looks like the image below (notice how the date values are different).
Since the "Date: dimension is in two different formats, these are two different unique
intersections and the system will not clear out the intended intersection.
To clear it out successfully, your dimensions should be in the same format and your source
file should look like this.
05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 5/9

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
Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration6. Check the members are actual members and not Calculated members. The screen shots
below is not allowed.
7. Check your source file's new line or end-of-line characters.
a. Open the source file in Notepad++.
b. Select View.
c. Select Show Symbol.
d. Select Show All Characters.
e. If some of the rows end with CR (i.e. Mac style line terminators) instead of CRLF (Windows
style line terminators) as shown below. Different operating systems or applications use
different line terminators/breaks.
05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 6/9

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
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappingsf. Re-run the ETL job with the Windows Latin-1 file encoding selected.
Cause
This could happen if you or the token used does not have the appropriate permission or those
intersections are part of a calc target. This could also happen if your source file is using the Mac-
style line terminators instead of the Windows-style line terminators
Keywords
etl completed but no data, data not loading, no data in cube, No Data After Successful ETL
Import
Was this article helpful?
0 out of 0 found this helpful05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 7/9

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
Product UpdatesRelated articles
How-To: Bulk Updating Dimension or
Hierarchy Member Names
How-To: PowerPoint Series (Part 1): Getting
Started With Vena for Microsoft PowerPoint
How-To: Map a Process Variable to a
Template (Vena 365 Only)
Explainer: Role-Based Licensing Enforcement
in Vena
How-To: Setting Up a NetSuite Connector and
Data FeedRecently viewed articles
Troubleshooting: Invalid ETL Mapping Output
Produced
Troubleshooting: No Matching Row in the ETL
Lookup Table
Troubleshooting: ETL Error While Processing
the Model Expression. Unexpected Token EOF
Troubleshooting: ETL Service Error-
Destination of the Channel is a Data Model
That Does Not Match the ETL Job's Data
Model
Troubleshooting: ETL Mapping Table is Empty
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 11:50 Troubleshooting: ETL Job Completed Successfully But No Data Is in the Cube – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14719436503181-Troubleshooting-ETL-Job-Completed-Successfully-But-No-Data-Is-in-the-Cube 9/9
