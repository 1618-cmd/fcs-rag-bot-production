# (Troubleshooting)   Template Data Save  2146826265 Error Caused By #REF! In Cells

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Contributor and Tasks/Troubleshooting/Troubleshooting Tasks Search
Getting Started
Manager
Contributor and Tasks
Contributor Fundamentals
Accessing Templates
Performing Tasks
Troubleshooting
Troubleshooting Template
and Report Access
Troubleshooting
Connection IssuesTroubleshooting: Template Data Save
-2146826265 Error Caused By #REF!
In Cells
Issue summary
When saving data on your template, you may receive the following error -2146826265 Do you
want to continue the save?
Miguel Buan
Updated 1 year ago
02/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 1/6

Troubleshooting Missing
Features
Troubleshooting: Error
Handling
Troubleshooting Tasks
Troubleshooting: Data Not
Appearing on a Template for
Some Users
Troubleshooting: Task Due
Date Notification Email does
not Show the Due Date
Correctly
Troubleshooting: Save
Template Prompt Randomly
Pops Up
Troubleshooting: Cannot Save
Data When the Process Is Not
Running
Troubleshooting: Adding
Comments to Intersection
Causes 404 Not Found Network
Error
Troubleshooting: Undo or Reset
a Submitted TaskOR
-2146826265. Data save failed. Please verify your inputs are correct and try again.
Suggested solution
The issue is caused by a #REF! in a data validation message cell.
1. Navigate to the Data Validation message cell on the template.
Learn to identify the Data Validation rule or message cell in Vena Desktop.
Learn to identify the Data Validation rule or message cell in Vena 365.02/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 2/6

Troubleshooting: Unable to See
the Submit Button on My Task
as a Contributor
Troubleshooting: Task Forms
Are Showing in a Random
Order for Contributors
Troubleshooting: Unable To
Save or Show Zero (0) Value on
a Template
Troubleshooting: Macros Are
Disabled in Excel When Initially
Opening Templates
Troubleshooting: Access
Denied When Trying To Save
Data or Template
Troubleshooting: Do You Want
To Continue the Save?
Troubleshooting: Save Data
Button Is Greyed Out or Not
Clickable
Troubleshooting: Template
Data Save -2146826265 Error
Caused By #REF! In Cells
Troubleshooting: Template
Data Save -2146826273 Error
Caused By #VALUE! In Cells2. Check if there's a #REF! error.
3. Remove or fix the #REF!'s from the cell.
4. Select Save Template.
5. Select Save Data and the errors should be solved.02/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 3/6

Troubleshooting: Template
Data Save -2146826259 Error
Caused By #NAME? In Cells
Troubleshooting: Template
Data Save -2146826288 Error
Caused By #NULL! In Cells
Troubleshooting: Template
Data Save -2146826252 Error
Caused By #NUM! In Cells
Troubleshooting: Template
Data Save -2146826281 Error
Caused By #DIV/0! In Cells
Troubleshooting: Template
Data Save -2146826246 Error
Caused By #N/A! In Cells
See all 34 articles
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
Cause
This may occur if the data validation message cell has a #REF! error. The cell reference was
removed or is no longer available.
Keywords
template, template error, data, data save, #REF, #REF!, -2146826265
Note
Excel.xlCVErr  Range.Value     In .NET
-------------  -----------  ---------------
    2000         #NULL!       -2146826288
    2007         #DIV/0!      -2146826281
    2015         #VALUE!      -2146826273
    2023         #REF!        -2146826265
    2029         #NAME?       -2146826259
    2036         #NUM!        -2146826252
    2042         #N/A         -214682624602/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 4/6

PowerPoint
Vena Copilot
Product UpdatesWas this article helpful?
0 out of 0 found this helpful
Related articles
Troubleshooting: Common Template
Automation ProblemsRecently viewed articles
Troubleshooting: Save Data Button Is Greyed
Out or Not Clickable
Troubleshooting: Do You Want To Continue
the Save?
Troubleshooting: Access Denied When Trying
To Save Data or Template
Troubleshooting: Macros Are Disabled in
Excel When Initially Opening Templates
Troubleshooting: Unable To Save or Show
Zero (0) Value on a Template02/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 12:36 Troubleshooting: Template Data Save -2146826265 Error Caused By #REF! In Cells – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16432849744653-Troubleshooting-Template-Data-Save-2146826265-Error-Caused-By-REF-In-Cells 6/6
