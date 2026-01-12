# (Reference)   GetValues() COM Function and SingleGetValue Wrapper Function

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
Vena DesktopReference: GetValues() COM Function
and SingleGetValue Wrapper Function
getValues() is a COM function for Excel VBA that allows a user to read a single data value from an
intersection of the Data Model that is connected with the workbook.
The main inspiration behind this function is to aid in a situation where a template has two
Sections and the 2 Section contains Form Variable mappings that refer to a data value that
should appear in the 1 Section after it has loaded.
Vena Support Team
Updated 1 year ago
nd
st
02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 1/7

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
Function and SingleGetValueSince we cannot set a load order for Sections, leveraging this function in a Vena BeforeRefresh()
subroutine would enable a value to appear on the Excel grid before Sections are processed.
Function Parameters
The parameters for getValues() is the following:
Workbook Object
Dimension Cell Range
Member Cell Range
The Cell Ranges can be a reference to a Named Range on the Sheet.
Syntax:
getSingleValue =
Application.COMAddIns("Vena").Object.VenaRestCall_GetValues(ActiveWorkbook,
DimensionArray, MemberArray)
Below is an example on how to use getValues() to bring a single intersection value into a cell.
Copy this function into a Module in your Excel Macro Enabled Workbook, and SingleGetValue()
would be immediately available for use.
SingleGetValue()
Public Function getSingleValue(dimensions As Range, members As Range)02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 2/7

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
Product UpdatesDim DimensionArray As Variant
ReDim DimensionArray(dimensions.Rows.Count - 1)
Dim i As Long
i = 0
For Each rng In dimensions
   DimensionArray(i) = rng.Value
   i = i + 1
Next
Dim MemberArray As Variant
ReDim MemberArray(0, members.Rows.Count - 1)
i = 0
For Each rng In members
   MemberArray(0, i) = rng.Value
   i = i + 1
Next02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 3/7

getSingleValue =
Application.COMAddIns("Vena").Object.VenaRestCall_GetValues(ActiveWorkbook,
DimensionArray, MemberArray)
End Function
Example of how to use SingleGetValue() in a cell02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 4/7

02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 5/7

Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Vena COM Functions
How-To: Setting Drill Transactions on a
Template or Report
How-To: Switch Between Dimensions Using
the Choose Box
How-To: Restoring a Missing Vena DesktopRecently viewed articles
Explainer: Redesigned Choose and Cascade
Menus
How-To: Saving Files to Vena Database
Intersections
How-To: Switch Between Dimensions Using
the Choose Box
Reference: Vena COM Functions02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 6/7

How-To: Viewing Multiple Datasets at the
Same Time With Cascade
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:32 Reference: GetValues() COM Function and SingleGetValue Wrapper Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/205005285-Reference-GetValues-COM-Function-and-SingleGetValue-Wrapper-Function 7/7
