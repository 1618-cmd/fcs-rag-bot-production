# (Explainer)   Using the Contributor Connector for Office Online

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
Vena DesktopExplainer: Using the Contributor
Connector for Office Online
 If you've set up Vena 365 for Office Online, read on to learn more about the Contributor
Connector experience.
Table of Contents
 How to
Using the Vena Contributor Connector
Contributor Connector Features
Vena Support Team
Updated 4 months ago
02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 1/18

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
Function and SingleGetValueChecking files back in
Notes & Known Limitations
Before you begin
You will need at least Contributor access to follow the instructions in this article. To use the Vena
Contributor Connector with Excel Online,you must connect your Microsoft Account to Vena.
Using the Vena Contributor Connector
Once you have downloaded or opened a task form, the Vena Contributor Connector allows you
to work on it: saving inputs, working with Line-Item Details, or using the Drill functions.
To use the Contributor Connector: When you download a task form and open it in Excel
(either the Mac version or Excel Online), the Contributor Connector will be installed
automatically. The first time that you open a file with the Contributor Connector, you will see a
prompt asking you if you want to start the Contributor Connector:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 2/18

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
Product Updates
Select theStartbutton, and the Contributor Connector will load:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 3/18

02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 4/18

1. You can now begin using the functions in the Contributor Connector to work with your task
form.
2. From this point on, the Contributor Connector will open whenever you open a file from Vena
with Excel Online or Excel for Mac, and will also automatically and silently install minor
updates. Note that, from time to time, a major update will be released. When this happens,
you will see a prompt like this:
Excel for Mac:
Excel Online:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 5/18

3. If you see one of these prompts, selectUpdate now/Updateto install the update, and the
Contributor Connector will re-appear automatically after updating. Keep in mind that you will
not be able to use the Contributor Connector until you have installed the update.
Contributor Connector Features
Save, Refresh, Choose & Cascade
The Contributor Connector supports the sameSave,Refresh,ChooseandCascadefunctionality of
Vena Desktop.
Save: Select theSavebutton to save your data inputs back to your Vena database:
Following a successful save, a confirmation will be displayed were the Save button usually02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 6/18

appears:
Refresh: Select theRefreshbutton to refresh the data displayed in your current task form
with the most recent data from your Vena database:
You will see a warning that proceeding will cause unsaved data to be lost:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 7/18

Select OK,and when the data has been refreshed, a message will appear:
SelectOpen template, and the refreshed data will load into a new browser tab.
Choose: If the task form you are using has been configured with the ability to switch between
different datasets ("page options"),selectChoose to select which dataset you want to view:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 8/18

Selecting Choose will bring up a menu that allows you to choose the desired page option(s):
Use the drop-down menus to choose the new page option(s) you want to view (the currently
displayed page option will be indicated withChecked Out), then select OK. Your selections will02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 9/18

be processed, and a message will appear:
Select theOpen templatebutton, and the task form with your new page options will load in a
new browser tab.
Cascade:If the task form you are using has been configured with multiple page options, you
can also use theCascadefunction to view different datasets side-by-side:
Learn how to use Cascade.02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 10/18

Line-Item Details
If the feature is enabled on the task form you are using, you can use the Line-Item Details tools
to add, remove and move Line Items:
To add a Line Item:
Select a cell in a row where you would like to add a Line Item.
Select theInsert LIDbutton in the Contributor Connector menu to add a Line Item to that row:
To remove a Line Item:
Select a Line Item you would like to remove.
Select theRemove LIDbutton in the Contributor Connector menu to remove that Line Item:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 11/18

To move a Line Item:
Select the Line Item you would like to move.
Select theMove LIDbutton in the Contributor Connector menu:
A message will appear asking you to select another Line Item to move the selected Line Item
below it:
02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 12/18

Select the Line Item under which you would like to move the selected Line Item, and it will be
moved there.
Note that you can only use the move feature to reorder Line-Item Details belonging to the
same intersection;Movecannot be used to move Line-Item Details to other intersections.
Drill Saves, Drill Transactions & Drill Down
Drill Saves, Drill Transactions and Drill Down (collectively known as the Drill functions) allow you
to see more context about the numbers displayed on your task form:
Learn more about Drill Functions..
Checking files back in
Unlike Vena Desktop, the Contributor Connector can't automatically check in a task form when
you exit, so this requires an additional step.02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 13/18

To check a file in after use:
Log in to Vena and selectContributor(if you are not taken to the Contributor section by default)
to view your Task List.
Locate the task you were working on in the Task List, then select it to open the Task Drawer
for this task.
Under theFormssection, you should see that the task form you have checked out will have
aCheck Inbutton next to it:
Depending on how you checked the file out originally, the appearance of the Check In button
will differ slightly:02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 14/18

If you are using a Mac and checked out the file withDownload (Check Out), you will see
this button:
To complete your check-in, simply select the button.
If you checked out the file withExcel Online (Check Out), you will see this button:
To check the file in, select this button and a new section of the Task Drawer will slide
open:
Select theCheck Inbutton here, and you will see a prompt asking you to make sure you02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 15/18

have no unsaved changes. To complete the check in, select theCheck Inbutton in the
prompt.
Notes & Known Limitations
Excel Online does not support Vena 365.
Excel Online only supports standard Excel files (XLSX), and is not compatible with macro-
enabled Excel files (XLSM). While you can still view reports in XLSM format in Excel Online, a
message is shown to warn you that the file may not function as intended when viewed in
Excel Online. Input templates in XLSM format cannotbe opened with Excel Online at this
time.
Excel Online does not support Soft Validations. If a task form has been set up with validation
rules (i.e. inputs must meet certain requirements) and the validation type has been set to
'soft' (displays a warning that validation failed, but permits saving data), opening the task
form in Excel Online will treat the validation type as 'hard' instead (prevents saving data if
validation fails).
You will only need to sign in to Office 365 once in a given session. If you close one task form
after signing in and subsequently open another one in the same session, you will remain
signed in and can immediately use the Vena Contributor Connector.
If you link a shared Microsoft account to Vena (i.e. multiple Vena accounts all link to the same
Microsoft account), keep in mind that files opened from Vena by any of these users will
appear in the Vena-createdAPPSfolder in OneDrive, and can therefore be accessed by any
other user with access to the OneDrive account (including files that they would not have
access to through Vena).
The Contributor experience for Mac users does not currently support templates with multiple
data models.02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 16/18

Vena 365 Mac Install and Troubleshooting Guide.PDF900 KB
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Reference: GetValues() COM Function and SingleGetValue Wrapper Function
Explainer: Redesigned Choose and Cascade Menus
How-To: Saving Files to Vena Database Intersections
How-To: Switch Between Dimensions Using the Choose Box
Reference: Vena COM Functions02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 17/18

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:32 Explainer: Using the Contributor Connector for Office Online – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16162749200269-Explainer-Using-the-Contributor-Connector-for-Office-Online 18/18
