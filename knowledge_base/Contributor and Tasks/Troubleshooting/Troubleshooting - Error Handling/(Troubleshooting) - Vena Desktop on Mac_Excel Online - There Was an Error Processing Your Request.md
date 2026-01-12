# (Troubleshooting)   Vena Desktop on Mac Excel Online   There Was an Error Processing Your Request

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Contributor and Tasks/Troubleshooting/Troubleshooting: Error Handling Search
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
Connection IssuesTroubleshooting: Vena Desktop on
Mac/Excel Online - There Was an
Error Processing Your Request
Issue summary
When opening a template on Vena Desktop for Mac or Excel online, you may get the following
error message: There was an error processing your request. It has been logged (ID 123X).
Olalekan Adebayo
Updated 1 year ago
02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 1/7

Troubleshooting Missing
Features
Troubleshooting: Error
Handling
Troubleshooting: Contributors
Receiving “File Not Permitted”
Error When They Check Out
Files
Troubleshooting: The Template
Has Errors - Please Contact
Your Administrator
Troubleshooting: This Template
Has Errors
Troubleshooting:
Errors/Warnings Box Appears
Blank in Excel and Shows
Information in an Additional
Window
Troubleshooting: Network Error
(422) Unprocessable Entity.
Resulting 2D Grid Would Be Too
Large
Troubleshooting: Microsoft
Visual Basic: Run-Time Error
‘1004’ Application-Defined or
Object-Defined Error
Suggested solution
This error appears when the template contains a feature unsupported by Vena Desktop for Mac
or Excel online. The most common is a template that uses Multiple Data Models.
1. Please check the template or reach out to your Vena Manager to ensure it does not contain
any of the unsupported features listed below.
Macros and Formulas
Macros: Macros will not be executed per Vena Macro Triggers. Templates that depend on
macros to function will not work properly.
User Defined Function (UDF): Similarly to macros, Mac/Office Online is unable to
resolve/execute User Defined Functions.
LOOKUP and XLOOKUP: The formulas ‘LOOKUP()’ and ‘XLOOKUP()’ are not supported.
However, VLOOKUP() and HLOOKUP() are supported.
INDIRECT Formula: INDIRECT is not supported.
Double-Negative: (--) is used in Excel formulas to turn a boolean into a number. It is not
supported in SSP. (1*) can be used instead, for the same result (e.g., =--True(), with the result
of '1').02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 2/7

Troubleshooting: Mac Add-
in/Excel Online Error While
Processing the Model Slice
Expression
Troubleshooting: Contributor -
Microsoft Refresh Token Has
Expired Due to Inactivity
Troubleshooting: Vena Desktop
Has Fired an Exception
Troubleshooting: This Content
is Blocked
Troubleshooting: Vena Desktop
on Mac/Excel Online - There
Was an Error Processing Your
Request
Troubleshooting: Vena Desktop
Installation Error - An
Unexpected Error Occurred
Troubleshooting: Excel Online
Does Not Support Running or
Interacting With Form Controls
Troubleshooting: We Can’t
Open Your Workbook in Excel
Online Because It Exceeds the
File LimitEquals-Plus: (“=+” at the start of a formula) This is an old method of formatting formulas and
it is not supported. Removing the plus will have no effect on the formula’s result.
TEXT() Formula: The TEXT formula is not supported. It may sometimes be computed but the
results are unreliable, so TEXT should be avoided.
‘International' Excel Formulas: Formulas that use semicolon ';' as a separator are not
supported.
Array (CSE) Formulas: Array formulas are not supported. Array formulas are formulas
applied to multiple cells in a sheet that start and end with ‘curly brackets’ - “{ }”.
Formulas with Structured References (Table-Style References): These are a functional
alternative to standard ‘A1’-style references and use the format “@[columnname]”.
Full row or column references (eg. A:A, 2:2): Occurring as range references in formulas,
this style of reference cannot be computed.
INDEX() can only accept row or column reference: When using the INDEX() formula (most
commonly used with MATCH), either the row or column variable must remain empty.
 Mapping Methods and Refresh Configurations
Block Form Variables: While regular Form Variables are supported, those where a single
Form Variable Named Range is applied to a block of multiple cells (known as a Block Form
Variable) can't be used. Block Form Variables are typically used for ‘Old’ Multi-Dynamic Rows
(SSS) Mappings, and can be identified using the Excel Name Manager as Form Variable
Mappings that extend across a range.
MDR "Copy Down": This is a specific case where MDR from one section/block "copies down",
or duplicates mappings from another section/block, due to its expansion. In SSP, the second
block’s mappings will not successfully be "copied down".
Special Refreshes: The use of a Double Refresh and/or Customized Refresh in the template can
cause issues, as these are not supported. Refresh will be conducted in arbitrary block order.
Default Mappings: For each block, all dimensions on the template must be manually
mapped. If dimensions are missing, they will not be completed with assigned Default02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 3/7

Troubleshooting: Network Error
404 Not Found When Saving
Data in a Template
Troubleshooting Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesMappings.
 Other Vena Functionalities
Multiple Data Models: Mac/Office Online will only work on templates mapped with a single
data model.
Very Large Staging Queries: Staging queries that result in over 100,000 results will cause
the template processor to crash, and no file will be returned.
Other Excel Functionalities
External Data Connections of any kind: Including formula references to other workbooks
and query connections to other files.
Templat es with Enable It erative Calculation Enabled:  This Excel setting allows circular
references, which cannot be calculated. The screenshot below shows the location for this
feature in the Excel Options menu.
Sheets Wider than 1000 Columns: This results in a large "used range", which cannot be
evaluated. ‘Used Range’ can be evaluated on each sheet with Ctrl+End, which takes you to the
bottom-right cell of the used range. This is most commonly due to values or formulas filled
wider than necessary. Sheets can have more than 1000 rows. When a sheet has more than
1000 columns, Vena Desktop will show a warning that the sheet is large.02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 4/7

Multiple date formats: The format used for dates must be consistent across the template.
Other Functionalities
Microsoft OneDrive: This could cause an issue if the system is not able to access your
OneDrive, causing a 403 error in the backend. java.io.IOException: An error occurred. Response
code: 403, Response message: Forbidden
Contact your Vena Admin to review the template for any Multi-Dynamic Row (MDR) or
Dynamic Expression mappings that may not be validating or executing successfully (i.e.,
giving errors or empty). Sometimes, these errors or empty spaces are due to spelling errors.
2. Fix or remove all unsupported features. In the case of OneDrive, contact your IT team to grant
Vena the ability to manage files in OneDrive.
Cause 02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 5/7

This could happen if the template you are trying to open contains one or more features that are
not supported by Vena Desktop on Mac or Excel online.
Keywords
error processing request, mac add-in, template issue, excel online, vena desktop
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: This Content is Blocked
Troubleshooting: Vena Desktop Has Fired an Exception
Troubleshooting: Contributor - Microsoft Refresh Token Has Expired Due to Inactivity
Troubleshooting: Mac Add-in/Excel Online Error While Processing the Model Slice Expression
Troubleshooting: Microsoft Visual Basic: Run-Time Error ‘1004’ Application-Defined or Object-
Defined Error02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 6/7

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 12:27 Troubleshooting: Vena Desktop on Mac/Excel Online - There Was an Error Processing Your Request – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14507786032141-Troubleshooting-Vena-Desktop-on-Mac-Excel-Online-There-Was-an-Error-Processing-Your-Request 7/7
