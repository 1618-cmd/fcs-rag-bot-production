# (Troubleshooting)   Unable To Save or Show Zero (0) Value on a Template

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
Connection IssuesTroubleshooting: Unable To Save or
Show Zero (0) Value on a Template
Issue summary
When saving the value 0 on a mapped cell, you may notice the value is not saving or that you
were able to load the 0 value into an intersection, but it's not showing on the cell in your
template.
Olalekan Adebayo
Updated 2 years ago
02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 1/6

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
a Submitted TaskSuggested solution
1. Navigate to the Modeler page.
2. Open the appropriate data model.
3. Select Settings from the sidebar tab.
4. Ensure the Retain zer os for this model  toggle is set to ON, either for the model or for particular
members or slices. Ensure that the mapping of the cell's intersection falls into the slices
defined in the Retain zer os for this dat a model setting.
5. If the cell is from a Multi-Dynamic Row (MDR) mapping, ensure the setting Treat Zeros as
Blanks is not checked. If it is checked, uncheck it.02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 2/6

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
Caused By #VALUE! In Cells
6. Check Excel's advanced options and confirm the setting Show a zero in cells that have zero
value is checked.
7. Ensure the format of the affected cells can show 0. In this example, there was a custom
format which causes 0 to show as "-". We updated the cell's format to Custom which allows a
0 value to be displayed as she below.02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 3/6

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
Current format: (* #,##0.00);(* (#,##0.00);(* "-"??);(@_)
Suggested format: (* #,##0.00);(* (#,##0.00);(* "0"??);(@_)
8. Once the format has been updated, the 0 values are now displayed.
Cause
This may happen if your data model has not been configured to retain zeros or if your MDR
mapping is treating zeros as blanks.02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 4/6

PowerPoint
Vena Copilot
Product UpdatesKeywords
unable to save zero (0) in a cell on a template, unable to show 0 (zero) on a template
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Task Forms Are Showing in a Random Order for Contributors
Troubleshooting: Unable to See the Submit Button on My Task as a Contributor
Troubleshooting: Undo or Reset a Submitted Task
Troubleshooting: Adding Comments to Intersection Causes 404 Not Found Network Error
Troubleshooting: Cannot Save Data When the Process Is Not Running02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 12:34 Troubleshooting: Unable To Save or Show Zero (0) Value on a Template – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/16395466518413-Troubleshooting-Unable-To-Save-or-Show-Zero-0-Value-on-a-Template 6/6
