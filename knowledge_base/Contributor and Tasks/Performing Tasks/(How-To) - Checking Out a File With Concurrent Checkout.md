# (How To)   Checking Out a File With Concurrent Checkout

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
Vena DesktopHow-To: Checking Out a File With
Concurrent Checkout
Here's what you need to know if your Vena Manager has enabled Concurrent
Checkout, which allows you to check out files at the same time as other Contributors.
About Concurrent Checkout
Jan Griffiths
Updated 1 year ago
02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 1/12

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
Function and SingleGetValueWhat is Concurrent Checkout?
In Vena, checking out a task form as a Contributor means that you are "reserving" it. As long as a
task form is checked out in your name, no one else can work on it. Because only one person can
use a task form at any given time, this helps to prevent conflicting inputs and version control
issues. However, it also means that other Contributors who need to use the same form have to
wait until it is available again.
Concurrent Checkout is an optional feature that Vena Managers can enable on particular task
forms. Instead of checking out the entire task form as normal, Concurrent Checkout allows you
to check out only a specific set of page options. This means that multiple users can work on a
task form at the same time. When one set of page options is checked out, this still leaves the
remaining page options available for other users to check out. For task forms with many users,
this can save a lot of time - you don't need to wait your turn to check out the form, because you
can just work on it at the same time as everyone else.
How is it different from the regular checkout process?
The way you check out a task form with Concurrent Checkout is almost identical to the regular
process, except that you may sometimes be unable to select specific page options because they
are already checked out. You can identify a Concurrent Checkout task form using the following
icon, which appears next to the form in the Forms tab of the Task Drawer:
02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 2/12

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
Product UpdatesWhen you see this icon, keep in mind that some page options may already be checked out by
other users and therefore unavailable. In this article, we will cover how you can find out which
page options are already checked out.
Before you begin
To follow the instructions in this article, you will need at least Contributor access.
The instructions also assume that you are using Windows Excel and that you have the latest
version of the Vena Excel Add-In for Windows installed. Alternatively, you can also use Office
2016 for Mac or an Office 365 subscription (see the Notes section for details).
How to
The process for checking out a Concurrent Checkout task form will work slightly differently
depending on the Template Property that was set on it by your Vena Manager, as well as
whether or not you are using Windows.
Use the appearance of the Check Out button in the Contributor Task Drawer to determine which
instructions to use:
Check Out button looks like Template Property used Use these instructions
Central/Standalone Method One02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 3/12

Hybrid Method Two
Checking out a Concurrent Checkout task form (Method
One)
Use these instructions if you know that the template you are using is a Central or Standalone
template, or if the Check Out button on the task form is split into two parts like this:
To check out a Concurrent Checkout task form (Central/Standalone templates):
1. Log in to Vena. If you are not taken there by default, navigate to the Contributor tab to go to
the Contributor Task List.
2. In the Task List, select the task you want to work on and the Task Drawer opens with more
details.
3. In the Task Drawer, select the Forms tab. Task forms that have Concurrent Checkout enabled
have a special icon (
) next to the form name.
4. Next to this task form, on the right, you will see a split Check Out button. Select the left part
of this button (the part with the Check Out label).
When you hover your mouse over this button, a tooltip will appear to indicate that
Concurrent Checkout is enabled:02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 4/12

If the Check Out button that you see is not split, skip to the instructions for Method Two.
5. This downloads and opens the task form in Excel as normal. As soon as it loads in Excel, the
Choose menu will appear.
6. Use the Choose menu to select the page option(s) you want to check out. Select OK and the
page option(s) you chose will be checked out in your name and loaded in Excel.
7. If the page option(s) you have selected are already checked out by another Contributor, you
will see an error message.
8. If you see this error message, you have a few options. You can:02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 5/12

Select Yes to view the selected page options as Read-Only, i.e. view data, but not save any
inputs (the Save Data button will be disabled).
Select No and return to the Choose menu to choose different page options.
Select No and close Excel to wait until the page options you want are available again.
9. If you want to see which page options are currently checked out, and by whom, return to the
Task Drawer in your browser and select the arrow section of the Check Out button.
10. This will open another section of the Task Drawer with more options. Select View Checked
Out Page Options in the Task Drawer.
11. After you have successfully checked out page options, use the task form as normal.
12. When you are finished, save your inputs (if applicable) and close Excel. When you are
prompted whether you want to check in, select Yes to check the page options back in.
Alternatively, you can also check page options back in by selecting the Check In button in
the Task Drawer in the Vena Contributor interface.02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 6/12

Checking out a Concurrent Checkout task form (Method
Two)
Use these instructions if you know that the template you are using is a Hybrid template, or if the
Check Out button on the task form is a one-piece (not split) button with an arrow, like this:
To check out a Concurrent Checkout task form (Hybrid templates):
1. Log in to Vena. If you are not taken there by default, navigate to the Contributor tab to go to
the Contributor Task List.
2. In the Task List, select the task you want to work on, and the Task Drawer opens with more
details.
3. In the Task Drawer, look at the Forms tab. Task forms that have Concurrent Checkout enabled
have a special icon (
) next to the form name.
4. Next to this task form, on the right, select the Check Out button with the arrow.
When you hover your mouse over this button, a tooltip will appear to indicate that
Concurrent Checkout is enabled.
02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 7/12

If the Check Out button that you see is split into two parts, follow the instructions above
for Method One.
5. A new section of the Task Drawer will slide open, showing additional checkout options. Use
the drop-down menu(s) to select the page option(s) that you want to check out, then select
Download (Check Out).
6. This will check out the selected page option(s) in your name and the task form will download
and open in Excel.
7. If the page option(s) you have selected are already checked out by another Contributor, you
will see an error message.02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 8/12

8. If you see this error message, select OK to choose different page options, or to return to the
Task Drawer to wait until the page options you want have been checked in again.
If you would like to see which page options are currently checked out, and by whom,
select View Checked Out Page Options in the Task Drawer.
9. After you have successfully checked out page options, use the task form as normal.
10. When you are finished, save your inputs (if applicable) and close Excel. When you are
prompted whether you want to check in, select Yes to check the page options back in.02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 9/12

Alternatively, you can also check page options back in by selecting Check In in the Task
Drawer in the Vena Contributor interface.
Notes
Mac and Office Online users can also check out page options on files enabled with
Concurrent Checkout:
If you are a Mac user, use the instructions from Method Two.
If you use Office Online, choose Method One or Method Two depending on the
appearance of the Check Out button, then choose Excel Online (Check Out) in step 5.
Concurrent Checkout is designed primarily for continuous tasks that are never submitted.
Please be sure to follow your Vena Manager's instructions for submitting such tasks.
 Note
With this check out method, your page option selection is processed on the Vena
web app, rather than in Excel. As a result, the Choose button in the Excel Add-In will
be disabled.
If you would like to switch page options, close Excel and select Check In, then select
new page options to check out.02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 10/12

Was this article helpful?
2 out of 2 found this helpful
Related articles
How-To: Allowing Multiple Contributors To
Use the Same File With Concurrent
Contributor
Explainer: What Are Vena Desktop and Vena
365?
How-To: Fixing Multiple Data Model
Compatibility Issues with Vena 365
Explainer: Fixing Macro Compatibility Issues
with Vena 365
Resource: Vena 365 & Vena Desktop
Contributor GuidesRecently viewed articles
How-To: Commenting on Templates in Excel
Online
How-To: Using Line-Item Details (LIDs) as a
Contributor
How-To: Using a File With Concurrent
Contributor in the Tasks Tab
How-To: Using Scratchpads in Vena Desktop
Explainer: Date Formats in Vena Templates02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 11/12

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:28 How-To: Checking Out a File With Concurrent Checkout – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360001910032-How-To-Checking-Out-a-File-With-Concurrent-Checkout 12/12
