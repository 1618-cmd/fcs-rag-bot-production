# (How To)   Automatically Run ETL Templates Using the ETL Scheduler

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
ETL JobsHow-To: Automatically Run ETL
Templates Using the ETL Scheduler
If you routinely run the same ETL templates, you can schedule them to trigger
automatically with the ETL Scheduler.
Laura Harris
Updated 9 days ago
02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 1/19

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

As a Modeler in your Vena environment, it is likely that you have a number of ETL templates that
you run repeatedly at regular intervals. While you can do this manually, Vena's ETL Scheduler
can automate this task for you by running specified ETL templates on a schedule of your choice.
With ETL Scheduler, schedules can be set for most types of ETL templates, and can be set to run
one or more times on a daily, weekly or monthly basis. In addition, using ETL Scheduler is not
limited only to recurring jobs. You can even use it for one-off jobs that need to run within a given
time window, such as outside of business hours.
In this article, you will learn how to configure the ETL Scheduler on your ETL templates.
Before you begin

To follow the instructions in this article, you will need at least Modeler access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
How to
Add a schedule to a template02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 2/19

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
Data QueryingYou can add a schedule to any new or existing ETL template.
To add a schedule to a template:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab. By default, you should be in the Templates
section of the ETL tool, which lists your existing ETL templates:
4. To edit an existing template: Select the
 (action) icon next to the template you want to
edit or right-click anywhere in the template row and then select View/Edit Details.
5. Both options open the ETL Template Manager drawer. You can set up your template (for a
new template) or make any necessary changes (for an existing template).
6. Select + Add Schedule.This opens the Job Schedule window.
=02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 3/19

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
& Connections
7. Configure the scheduling options as desired.
8. Select Save to save the template and activate your schedule.02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 4/19

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
Product UpdatesScheduling options

 Note
To prevent accidental integration of outdated data, scheduling cannot be added to
templates that include File to Cube, File to Stage or File to Vena Table steps.
For such templates the ETL Template Manager window grays out the + Add Schedule
button and displays a message upon hovering.
02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 5/19

When setting a schedule, you can determine the frequency that the job is run, the start and end
period during which the schedule should apply, the timezoneand add notes to the schedule.
Frequency
Schedules can be set to any of the following frequency options:
Once at
Used for one-off jobs. This option sets the template to be run once automatically at a certain
date and time. Use the calendar button to select the date and time.The time can be set to
within 5 minutes:
02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 6/19

Daily
Used for one-off jobs. This option sets the template to be run once automatically at a certain
date and time. Use the calendar button to select the date and time.The time can be set to
within 5 minutes:
In the Period section, choose one or more six-hour time windows. The template will be run at
sometime within the chosen window(s):02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 7/19

Weekly
Sets the template to be run one or more times per week, repeating anywhere between once
a week to every 6 weeks. Use theFrequency drop-down to choose the number of weeks
between repetitions:02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 8/19

In the Day(s) section, choose one or more days on which you want the template to run:02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 9/19

In the Period section, you can choose one or more six-hour time windows. The template will
be run at sometime within the chosen window(s) on the days selected under Day(s):
Monthly
Sets the template to be run once a month, repeating every one to six months. Use the
Frequencydrop-down to choose the number of months between repetitions:02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 10/19

Use the On day drop-down to choose the day of the month on which the template should be02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 11/19

run:
This drop-down allows you to choose anywhere between the 1st and 31st day of the month.
If you choose a day of the month higher than 28, the template will run on the last day of the
month in months with fewer than the selected number of days (e.g., if you choose 31, the
template will run on February 28, June 30, etc.).
In the Period section, you can choose one or more six-hour time windows. The template will02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 12/19

run at sometime within the chosen window(s) on the days selected under Day(s):
Activation & Expiration Date
If desired, you can set a date on which the schedule becomes active (runs for the first time), as
well as a date on which it expires (stops running). To do this, use the Activation Date and
Expiration Date fields:02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 13/19

As with Frequency time settings, the activation and expiration dates and times can be set to
within 5 minutes.
Both fields are optional, and may be left blank:
If no activation date is set, the schedule will trigger the first running of the template on the
next instance of the frequency you selected.
For example, if you set up the schedule on a Thursday and set it to run the template once
a week on Monday, the template will be run for the first time on the next Monday.
If no expiration is set, the schedule will run indefinitely.
Timezone02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 14/19

The times you specify in various places under Frequency and Activation/Expiration Date can be
set to refer to any timezone of your choice. Use the dropdown menu to choose the desired
timezone:
You must select a timezone (typically, this would be your local timezone) before you can save a
template with an attached schedule. When you select a timezone, the current time in that
timezone is displayed under the dropdown to help you verify if the timezone selected is correct:
If the selected timezone observes Daylight Saving Time (DST), the ETL Scheduler automatically
shifts the time while DST is in effect.
Notes
If desired, you can use the Notes field to leave notes or instructions concerning the schedule or
template. Keep in mind that these notes will be visible only when editing the schedule and
cannot be seen elsewhere (including the ETL Job Schedule table in the Templates section).02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 15/19

ETL Job Schedule Table

All ETL templates, both with and without scheduling, are listed in the ETL Job Schedule table,
which is shown by default when you navigate to the ETL tab in Vena's Modelertab:
Templates with a schedule are indicated under the Schedule column, which shows a brief
summary of the schedule. You can also see when the schedule was last run under Last Execution.
 Note02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 16/19

Notes & best practices

It is possible for two ETL jobs based on the same ETL template to overlap. For example, if you
manually run a template using the Play button, and the resulting job is still running at the
time that the next scheduled execution is set to take place. If this occurs, the first job to be
started will be complete, and the second will be skipped (not run).
If any step of a scheduled ETL job encounters an error, the associated schedule will be
disabled to avoid a situation where a job that contains errors is continually rerun. To resolve
this, fix the error, then manually reenable the schedule.
If a scheduled job is running and you click the Play button for the same template, the
scheduled job will continue, and the manually executed job will be queued to start after
completion of the scheduled job.
Another situation in which two jobs based on the same ETL template can overlap is when you
set two jobs to run fairly close together (e.g., in consecutive six-hour windows, such as
Evening and Overnight). If the job takes a long time to complete, it can run into the next
scheduled execution, which will be canceled as a result. As a best practice, if you are adding a
schedule to a job that typically takes a long time to complete, take this into account when
planning your schedule timings.
Both scheduled and unscheduled templates can be run immediately on an on-
demand basis at any time by selecting the
(Play) button under the Actions
column.
Doing this does not affect the scheduling of a scheduled template unless the
processing of the job runs into the next execution time (see note below).02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 17/19

Before saving a scheduled template, it is important that you ensure that the selected
timezone is correct in order to ensure that scheduled jobs will actually run when you expect
them to. To do this, use the current time readout after selecting a timezone and compare this
to your local time.
As a best practice, it is strongly recommended that you try to construct the simplest possible
schedule that meets your requirements. For example, it is possible to create a schedule to
run a template every day in two ways: (1) by setting a daily schedule that repeats every one
day, or (2) by creating a weekly schedule that repeats every week and checking off every day.
While the results should be the same, the preferred option would be (1), as it is simpler and
thus is less prone to problems.
While you should aim for the simplest solution, your specific requirements should also
remain a primary consideration when creating a schedule. If, in the example above, you
wanted a schedule that repeats daily, but only on weekdays, option (2) would be more
appropriate (in which case, you would not check Saturday and Sunday in the Day(s)
section).
Was this article helpful?
1 out of 2 found this helpful
Related articles
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 1 - OverviewRecently viewed articles
How-To: Scheduling Ongoing ETL Jobs at Exact
Times Using Command-Line ETL
Explainer: ETL Export Feature Updates02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 18/19

How-To: Use Power BI Connector
Vena Insights Series (Part 3) - Editing Your
Dashboards
Explainer: Vena User RolesReference: Additional Security Restrictions to
the SQL WHERE Clause
How-To: Exporting a Subset of Data From
Your Data Model or Cube
How-To: Create and Manage a Data Model
Hierarchy Using ETL Import
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:45 How-To: Automatically Run ETL Templates Using the ETL Scheduler – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115002967646-How-To-Automatically-Run-ETL-Templates-Using-the-ETL-Scheduler 19/19
