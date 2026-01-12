# (Troubleshooting)   Network error System.OutofMemoryException Error Resolution

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
a Problem With Some ContentTroubleshooting: Network error
System.OutofMemoryException Error
Resolution
Issue summary
System.OutofMemoryException and may see an error message like the following:
Owais Khan
Updated 1 year ago
02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 1/6

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
Task Appears as Coming Soon
Suggested solution
1. Open Excel and navigate to the Vena tab
2. Select Settings.
02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 2/6

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
Need To Be Enabled and3. Open the Advanced tab.
4. Find SuppressRefreshonLoad and set it to True. This setting suppresses refreshing the template
on the initial load which allows the template to open.
02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 3/6

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
Vena Insights5. Open the template.
6. Locate the worksheet with excess rows or columns.
7. Select the column or row from the header where the mapping or data ends.
8. Scroll to the last active row or column.
9. Hold shift and select the last column.
10. Right-click and select Delete.
11. Select Save template or re-save the file locally and re-upload it.
12. You may change the "SuppressRefreshonLoad" back to False once this is completed.
Cause
This error occurs when Excel runs out of its memory.
One of the common causes of this error is empty & unmapped rows or columns. Although there
may be nothing in these cells, Excel still treats them as active cells and has to process them
which uses substantial memory.
Keywords
network, memory, error, system, template.
Was this article helpful?02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 4/6

Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates4 out of 4 found this helpful
Recently viewed articles
Troubleshooting: Analyze Template or Comment Window Blank or Won't Open
Troubleshooting: The Specified Path, File Name or Both Are Too Long
Troubleshooting: Text Is Being Displayed Incorrectly in Vena Desktop
Troubleshooting: The Template Was Downloaded From a Different IP Address
Troubleshooting: Opening a Vena Template in a New Excel Instance
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 12:13 Troubleshooting: Network error System.OutofMemoryException Error Resolution – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/211128143-Troubleshooting-Network-error-System-OutofMemoryException-Error-Resolution 6/6
