# (How To)   Using Scratchpads in Vena 365

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Contributor and Tasks/Performing Tasks Search
Getting Started
Manager
Contributor and Tasks
Contributor Fundamentals
Accessing Templates
Performing Tasks
How-To: Using Scratchpads in
Vena 365
Explainer: Date Formats in Vena
Templates
How-To: Using Scratchpads in
Vena DesktopHow-To: Using Scratchpads in Vena
365
Create additional worksheets in Vena 365 with Scratchpads to add historical data,
implement account reconciliation and perform calculations.
Why use this feature?
Mia Shabsove
Updated 3 months ago
02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 1/9

How-To: Using a File With
Concurrent Contributor in the
Tasks Tab
How-To: Using Line-Item Details
(LIDs) as a Contributor
How-To: Commenting on
Templates in Excel Online
How-To: Checking Out a File With
Concurrent Checkout
How-To: Using Comments in a
Template or Report
How-To: Viewing Multiple
Datasets at the Same Time With
Cascade
Reference: Vena COM Functions
How-To: Switch Between
Dimensions Using the Choose
Box
How-To: Saving Files to Vena
Database Intersections
Explainer: Redesigned Choose
and Cascade Menus
Reference: GetValues() COM
Function and SingleGetValueScratchpads for Vena is essentially an area for rough work that you can use to provide additional
context and details. Scratchpads allow you to add extra worksheets to a file. You can use this
additional worksheet to add historical data, implement account reconciliation and perform
calculations to aid in your tasks.
Before you begin
To follow the instructions in this article, you must have Contributor access. The template
properties must be set to Hybrid by your Manager. Learn more about template properties.
Table of contents
How to
Notes & limitations
Use Case
How to
1. Navigate to the Contributor or Tasks tab.
2. Select your task and open the associated file.
3. In the Vena 365 task pane, select Data Inspection section.02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 2/9

Wrapper Function
Explainer: Using the Contributor
Connector for Office Online
Troubleshooting
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates4. Select Inser t Scrat chpad.
5. A new sheet named Scr at chp ad_0 will open in the file.
6. Add your data or calculations to the scratchpad.
7. Once you’ve added your data or calculations, select Finish Input .
8. The scratchpad will be saved to this task.
Differences between Scratchpads for Vena Desktop and Vena 365
Note
This scratchpad will only be saved to this specific task. Other Contributors or Managers
that have access to this task will also have access to the scratchpad you just created. 02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 3/9

There are several  functional dif ferences between Scratchpads for V ena Desktop  and V ena 365. They
are outlined in the following table.
Template
PropertyInterface Task Behavior Predefined
Scratchpads
Vena Desktop   Scratchpads
can
   be used with
   Hybrid or
   Standalone
   templates. The
   main objective
   is to allow
   Contributors to
   save structural
   changes.
   However, the
   best practice is
   to use Hybrid
   templates.    There are no
   interface
   changes.   Input Tasks
   Hybrid
   templates:
   Changes are
   task specific.
   Only
   Contributors
   within the task
   can see them.
   Managers do
   not see
   Scratchpad
   changes.
   Standalone
   templates:
   Changes are
   visible to
   everyone; they
   are not task
   specific.
   Managers can
   also see
   changes.     Supported
   Managers can
   create structure
   and designs in
   their
Scratchpads
   to guide
   Contributors to
   where inputs
   should be. Vena
   Desktop allows
   Managers to
   design a
   Scratchpad tab
   that dictates the
   location of
   Contributor
   inputs.
   Contributors can
   make inputs in
   the Scratchpad
   and when they
   make saves, the
   data in the02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 4/9

   If the process
   is reset, the
   Scratchpad
   tabs and its
   data will
   remain.
   Review Tasks
   Reviewers can
   also see the
   Scratchpad
   changes.    predefined
   Scratchpads are
   preserved in the
   input and review
   task.
Vena 365   Only Hybrid
   templates will
   have the Insert
   Scratchpad
   button.   When there is a
   Hybrid
template,
   the Insert
   Scratchpad
   button is
visible.   Input Tasks
   Scratchpad
   tabs and
   Contributor-
   created tabs
   will remain
   within the
   same input
   task.
   If the process
   is reset, the
   Scratchpad
   tabs and its
   data will
   remain.    Not Supported
   In Vena 365,
   Managers can
   create
predefined
   scratchpads but
   Contributor edits
   on Manager-
   created tabs will
   not be retained.
   This poses an
   issue as it results
   in the loss of
   context. If an
   intersection’s
   input was
derived02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 5/9

Review Tasks
  Reviewers
can view the
Scratchpad
changes if they
are added as a
Watcher on the
input task.    from a formula
   based on a
   Scratchpad’s
   data, the missing
   inputs will cause
   a versioning
   problem.
Notes & limitations
If your Manager has Concurrent Contributor enabled, any scratchpad created will only be
saved to the page options that it was created in. If Concurrent Contributor is not enabled, any
scratchpad created will be saved to the task and will appear on all page options.
Suppose a scratchpad is created with Concurrent Contributor not enabled and later it is
enabled. In that case, the scratchpad will be saved to all page options and any scratchpad
created after Concurrent Contributor was enabled will only appear on the page option it was
created in.
If the template type is changed back to Central after scratchpads are created, they will not be
lost. The scratchpads will no longer be inserted when a template is opened from the task.
If the file hasn’t been saved since it was changed back to a Central template type, simply
switching the template type back to Hybrid will continue allowing the saved scratchpads
to be inserted into the file load.
If the file has been saved, the scratchpads will have to be recovered and restored from the
Audit Trail feature.02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 6/9

Standalone templates are not supported on Vena 365. If you want more information on the
template types, Learn more about template types.
Scratchpads are not supported in .xslm files.
Reviewers may only view the scratchpad if they are added as, at minimum, a Watcher on the
input task. Learn more about Task roles in process workflows.
Use Case
To follow the instructions in this use case, you must have Contributor access and the
template properties must be set to Hybrid by your Manager.
SuperCorp is a company that uses Vena for accounting. To do this, they create a
template called General Ledger to use for their financial records by all departments.
Manager Julie creates a task for Contributor Angela to enter her department's
financials for that quarter. Julie ensures that the template property is set to Hybrid
so Angela can utilize scratchpads for account reconciliation purposes.
Angela navigates to the Contributor tab, opens the task she needs to complete and
checks out the file. To start the account reconciliation process, Angela wants to open
a scratchpad. In the Vena 365 window, she selects Data Inspection and then selects
Insert Scratchpad.
In the scratchpad, Angela performs the account reconciliation and finishes her task.
When she’s done, she selects Save Data to Vena. Julie can now open the task Angela
has finished and see the account reconciliation process Angela created in the
scratchpad.02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 7/9

Was this article helpful?
0 out of 0 found this helpful
Related articles
Explainer: The Difference Between Central,
Standalone and Hybrid Templates
How-To: Using Scratchpads in Vena Desktop
How-To: Using Dynamic Task Bindings (Vena
365 Only)
Reference: Vena 365 Manager Start Guide
How-To: PowerPoint Series (Part 1): Getting
Started With Vena for Microsoft PowerPointRecently viewed articles
How-To: Viewing or Opening Templates from
a Completed Task or Process
Resource: Vena 365 & Vena Desktop
Contributor Guides
Explainer: New Tasks Tab Experience
Resource: Vena 365 Contributor Migration
Guide
How-To: Reporting on Task Bindings
Didn't find what you're looking for?02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 11:25 How-To: Using Scratchpads in Vena 365 – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/9837254743565-How-To-Using-Scratchpads-in-Vena-365 9/9
