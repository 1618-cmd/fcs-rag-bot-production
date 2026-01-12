# (Troubleshooting)   Data Not Appearing on a Template for Some Users

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
Connection IssuesTroubleshooting: Data Not Appearing
on a Template for Some Users
Issue summary
For some users, values may not appear in one or more of their templates, even though these
users have the relevant data permissions.
Omair Riasat
Updated 3 months ago
02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 1/6

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
a Submitted TaskSuggested solution #1
Check if the affected users are on a version of Excel that does not support certain formulas.
1. For the affected user, check their version of Excel. Learn more about how to check your Excel
version.
2. Check for Excel function compatibility issues in the affected template, especially if the user is
using an older version of Excel. Learn more about Microsoft Excel functions.
If the function has a version marker, it indicates that the function was recently introduced
and is not available in earlier versions of Excel.
3. You can also use the Excel Compatibility Checker to find possible compatibility issues. From
Excel, navigate to File > Info and select the Check for Issues dropdown. Select Check
Compatibility.
4. This will show a list of all potential issues along with the Excel versions that would be
affected. You may find it easier to use the Copy to New Sheet function to review all entries.02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 2/6

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
5. If there are formulas in the template that are not compatible with some users' version of
Excel, there are two options. Either upgrade the version of Excel that the users are using or
replace the problematic formulas with compatible ones.
6. Once you have made any changes to the template, select Save Template.
7. Check to see if the issue is resolved.
Suggested solution #2
This can also happen if the client has a date related dimension and the users who are facing the
issue are using their local language regional setting for the date.02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 3/6

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
Vena for MicrosoftSo for example if there is a dimension called Week and has members in the format of say
10.Jul.25. When local language regional date settings are used, the month is translated into the
local language and breaks the mappings in the template so that no data is displayed. In this case
to resolve is to change the regional date settings to the US format. Refer to your internal IT Team
for assistance on changing your regional date settings.
Cause
This issue can occur if users have older versions of Excel that are not compatible with the
formulas your template uses.
Check local date formats and region settings for any incompatibilities
Keywords
data, template, issues, values not appearing, data not appearing, compatibility, excel version,
formula compatibility
Was this article helpful?
0 out of 0 found this helpful02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 4/6

PowerPoint
Vena Copilot
Product UpdatesRelated articles
Troubleshooting: Data Discrepancy or Data
Not Appearing on a Template
How-To: Find Your Excel Version
Troubleshooting: Vena Copilot No
Appropriate Application or Data Permissions
Troubleshooting: Invalid Member Name for
Dimension (X): Name Is Blank
How-To: Creating and Managing Data
PermissionsRecently viewed articles
Troubleshooting: Network Error 404 Not
Found When Saving Data in a Template
Troubleshooting: We Can’t Open Your
Workbook in Excel Online Because It Exceeds
the File Limit
Troubleshooting: Excel Online Does Not
Support Running or Interacting With Form
Controls
Troubleshooting: Vena Desktop Installation
Error - An Unexpected Error Occurred
Troubleshooting: Vena Desktop on Mac/Excel
Online - There Was an Error Processing Your
Request
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 12:30 Troubleshooting: Data Not Appearing on a Template for Some Users – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/37481217094029-Troubleshooting-Data-Not-Appearing-on-a-Template-for-Some-Users 6/6
