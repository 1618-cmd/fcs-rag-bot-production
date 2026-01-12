# (Troubleshooting)   The Template Didn't Refresh. You Can Try Again by Reloading the Add in

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Contributor and Tasks/Troubleshooting
/Troubleshooting Template and Report AccessSearch
Getting Started
Manager
Contributor and Tasks
Contributor Fundamentals
Accessing Templates
Performing Tasks
Troubleshooting
Troubleshooting Template
and Report Access
Troubleshooting: Error on
Opening Template - We Found
a Problem With Some ContentTroubleshooting: The Template Didn't
Refresh. You Can Try Again by
Reloading the Add-in
Issue summary
When opening templates using Vena 365 you might come across the following error message:
The template didn't refresh. You can try again by reloading the Add-in. If the problem persists, contact
Mendez Dixon
Updated 1 year ago
02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 1/7

Troubleshooting: Vena Desktop
Toolbar or Ribbon Is Missing
Troubleshooting: Template or
Report is in View-Only Mode
Troubleshooting: Failed to
Download Form for a Review
Task
Troubleshooting: These Page
Options Are Currently Checked
Out
Troubleshooting:
Venamonitor.exe - This
Application Could Not Be
Started
Troubleshooting: This Add-In
Comes From a Shared Folder
Troubleshooting: Intermittent
Issue With Vena 365 Panel Not
Loading
Troubleshooting: Choose Box
Options or Members Are Not
Collapsed by Default
Troubleshooting: Contributor
Task Appears as Coming Soonyour administrator or support.
Suggested solution 1: check for form variable mapping in
page selection mapping
1. This could happen if there's a Form Variable mapping in a Page Selection mapping. Clear the
mapping to remove the Form Variable and re-map the Page Selection mapping to a static or
dynamic mapping without the Form Variable.
2. Refresh the template.
3. This could also happen if there's a Multi-Dynamic Row or dynamic mapping and a form
variable in the same row/column and the form variable depends on the dynamic        row. This is
currently not supported.02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 2/7

Troubleshooting: Not Able to
See or Select Appropriate
Dimension in the Choose Box
on Templates with Task
Bindings
Troubleshooting: This Add-In Is
No Longer Supported on This
Application
Troubleshooting: The Template
Didn't Refresh. You Can Try
Again by Reloading the Add-in
Troubleshooting: The File Has
No Page Options to Choose and
Cannot Be Opened Using
Concurrent Contributor
Troubleshooting: We Can’t Start
the Add-In Because It Isn’t Set
Up Properly
Troubleshooting: View Checked
Out Page Options Button Not
Visible as a Contributor
Troubleshooting: Vena Desktop
- adxloader.Vena.dll add-in
Error
Troubleshooting: Page Options
Need To Be Enabled andSuggested solution 2: check for Excel number of rows
limitation
1. Check the number of rows in your sheets are not close to the Excel limit (1,048,576). If they
are, delete all the rows that should be empty. The rows may appear to be empty but could
have formatting applied to them for example, which means Excel classes these as non-empty
cells. On refresh, the dynamically created rows cannot be created because the Excel row limit
would be breached which will lead to a refresh error in Vena.
Suggested solution 3: check for a member or alias with the
same name as the combination of another member and its
alias
1. Ensure that a dimension member's name or its alias is not the same as the combination of
another member's name and its alias.02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 3/7

Selected in Order To Use
Concurrent Checkout
Troubleshooting: Network 422
Error Member With Name =
-2146826238 Not Found
Troubleshooting:
Authentication Timeout
See all 32 articles
Troubleshooting
Connection Issues
Troubleshooting Missing
Features
Troubleshooting: Error
Handling
Troubleshooting Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
2. You can check the data model revisions for ETL members creating unmapped members from
the time the template last refreshed correctly to the time it first started to produce the
refresh error.
3. Using the date/time, find the corresponding ETL job and check the members of this file to see
if any ambiguously named members were created, usually into the unmapped folder.
4. Update or delete the unwanted dimension members and re-open the template.
Suggested solution 3: check for ROW() functions
This issue can also occur when block ordering isn't able to execute because a ROWS function in
Excel references itself. Since block ordering couldn’t be performed, the process required by the02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 4/7

Vena for Microsoft
PowerPoint
Vena Copilot
Product Updatessystem is not completed, hence the template fails to refresh. To fix this,
1. In your template, look for the columns that contain ROWS functions.
2. Highlight the columns, right-click them, and select Clear Contents.
3. Check to see if the template refreshes successfully.
4. Another option is to adjust the ROW() formula to contain actual cells in the parenthesis, for
example, ROW(AL9) instead of just ROW(). Both formulas would return the same value and
since a cell is now referenced, it doesn’t “create” a circular dependency - allowing the
template to refresh properly.
Keywords
Template didn't refresh, Refresh error, V365 refresh, V365 error
Was this article helpful?
0 out of 8 found this helpful
Related articles
How-To: Map a Process Variable to a
Template (Vena 365 Only)
Reference: Vena Calcs - 1 - Managing ScriptsRecently viewed articles
Troubleshooting: This Add-In Is No Longer
Supported on This Application02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 5/7

Troubleshooting: This Template Has Errors
How-To: Granting Vena Support Access to
Your Tenant
How-To: Getting Vena for Mac or Office
OnlineTroubleshooting: Not Able to See or Select
Appropriate Dimension in the Choose Box on
Templates with Task Bindings
Troubleshooting: Contributor Task Appears as
Coming Soon
Troubleshooting: Choose Box Options or
Members Are Not Collapsed by Default
Troubleshooting: Intermittent Issue With Vena
365 Panel Not Loading
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 6/7

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 11:40 Troubleshooting: The Template Didn't Refresh. You Can Try Again by Reloading the Add-in – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/17012101964813-Troubleshooting-The-Template-Didn-t-Refresh-You-Can-Try-Again-by-Reloading-the-Add-in 7/7
