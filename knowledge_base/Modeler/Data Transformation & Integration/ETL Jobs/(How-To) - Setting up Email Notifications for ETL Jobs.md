# (How To)   Setting up Email Notifications for ETL Jobs

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
ETL JobsHow-To: Setting up Email
Notifications for ETL Jobs
Use ETL Notifications to get automated email notifications and keep tabs on your
ETL jobs.
Why use this feature?
Vena Support Team
Updated 1 year ago
02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 1/11

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
Restrictions to the SQL WHEREModelers spend a lot of time in Vena managing ETL jobs. Because many ETL jobs take a while to
complete, it’s important to keep on top of them, resolving any errors as quickly as possible to
keep your Vena environment running smoothly.
While keeping a watchful eye on your ETL jobs queue is one way to do this, it's not the most
efficient use of your time. ETL Notifications make keeping tabs on your ETL jobs a lot easier.
With ETL Notifications, you can set up automated email notifications that trigger when any of
the following key events occur:
An ETL job is completed.
An ETL job experiences an error.
Someone cancels a running ETL job.
You'll be notified by email as soon as one of these events happens, freeing you up to work on
other tasks without having to worry that you'll miss something.
In this article, you'll learn about how to set up and use ETL Notifications.
Before you begin
To follow the instructions in this article, you will need at least Modeler access.
How to
ETL Notifications is an optional feature that you can enable on any ETL template. It allows you to
send automatic email notifications to any number of users or user groups in your Vena
environment whenever an ETL job finishes, errors out or is manually cancelled.02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 2/11

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
Data QueryingEnabling ETL job notifications
Notifications for ETL job events are set for each ETL template individually. When doing so, you
have the choice of sending notifications for any combination of trigger events, i.e., just one, any
two or all three.
To set up email notifications on an email template:
1. Navigate to the Modeler tab.
2. Select Data Modeler from the sidebar.
3. Select ETL Templates from the sidebar tab.
4. Either right-click on the row or select the vertical ellipses at the end of the row of the
template you want to add an email notification for.
5. Select View/Edit Details. This opens the ETL Template Manager drawer.02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 3/11

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
& Connections6. Move the toggle next to Job Notifications to ON.
7. Enter users or user groups in the Users/Groups to notify field. As you begin typing, matching
users and groups will be suggested.
8. Select suggestions to add them to the list of recipients. When you add recipients, they appear
below the search field (users in blue and user groups in orange). To remove a recipient, select
the X next to their name.02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 4/11

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
Product Updates9. When you have completed your recipient list, use the checkboxes under Receive notifications
for to choose which events will trigger email notifications when this ETL template is run:
Job Completed: The job has finished successfully without errors.
Job Error: The job was automatically stopped due to an error.
Job Cancelled: The job was cancelled by a user while running.
10. Select Save to apply your notification settings when you are finished. Your specified
recipients will be notified by email whenever the selected trigger event occurs for this ETL
template.
 Note
You can also add email addresses with the Venacorp domain, eg.,
user@venacorp.com. This lets consultants get notified directly on ETL jobs, thereby
monitoring ETL activities for customers when needed. An example scenario would be02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 5/11

Modifying or disabling ETL job notifications
You can make changes to or stop ETL job notifications at any time.
To change or cancel email notifications on an email template:
1. Repeat steps 1-4 under Enabling ETL job notifications above. This should open the ETL
Template Manager drawer.
2. When you are finished, select Save.
To make changes:Select the
(Pencil) iconand add/remove recipients or change
which notifications are sent.
To cancel email notifications:Select the
 (Trash) icon next to Job Notifications to
cancel email notifications for this ETL template.
Reference guide
Examples of the email notifications that are sent for each of the trigger events are displayed
below.
a customer still in the implementation stage, and a Service representative is handling
all the data loads.
In this case, you can type a valid Venacorp email in the 'Select users/groups to notify'
field. This will not trigger auto-suggestions as these are not part of the customer's list
of users.02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 6/11

Job Completed
Job Error02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 7/11

02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 8/11

Job Cancelled
Notes & best practices
Email notifications will be sent to your selected users' Vena email address, i.e., the email
address that they use to log in to Vena. Please ensure that your recipients know to check this
email for ETL notifications.02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 9/11

As with any email notification system, there is a chance that recipients may have trouble
receiving the emails due to spam filtering. To help avoid this, please ask recipients to add no-
reply@vena.io to the approve list, if necessary.
While you can choose to send notifications for any combination of trigger events to any
combination of users, you can only set up one notification per ETL template. This means that
it is not possible, for example, to send job completion notifications to one user and job error
notifications to a different user for the same ETL template.
When configuring notification recipients, you can only add users who hold the Modeler role
and have at least Read access to the relevant data model.
It is not possible to see from the list of ETL templates whether an ETL template has
notifications enabled. To check, you must view each template's settings individually.
Because ETL Notifications are tied to the ETL web interface (ETL templates), they will not be
sent for ETL jobs that are executed from the Command Line. However, as a workaround, you
can set up a "dummy" ETL template in Vena (containing any steps you wish) and configure
ETL Notifications on it according to your preference. Then, when running ETL jobs from the
Command Line, you can invoke the dummy template using its Template ID and the --
templateId parameter. This will trigger an email notification for the ETL job run from the
Command Line, per the notification settings on the dummy template.
Was this article helpful?
0 out of 1 found this helpful
Recently viewed articles02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 10/11

How-To: Maintaining Dimension Member IDs When Updating Existing Members
How-To: Use Clear Slices to Clear Intersections During an ETL Load
How-To: Exporting CSV Files for ETL Job
How-To: Checking if My File Has a Header Row or Not
How-To: Automatically Run ETL Templates Using the ETL Scheduler
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:47 How-To: Setting up Email Notifications for ETL Jobs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003966752-How-To-Setting-up-Email-Notifications-for-ETL-Jobs 11/11
