# (Reference)   Vena COM Functions

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
Vena Desktop
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
Template or ReportReference: Vena COM Functions
Learn about the Vena-specific COM Functions which can be deployed in VBA macros.
Overview
Vena COM functions, sometimes also called Vena Events, are functions which can be called in VBA to perform Vena-specific actions in Excel. They are useful for
creating macros to enable custom functionality on Vena-enabled workbooks.
The available functions fall into three main categories:
COM Functions, the basic building blocks of Vena COM functions
Cloud API Functions, which allow interaction with Vena Cloud
Events, which are used to trigger actions when specific events occur.
In addition, there is also a Commands sub-category. These commands are used in conjunction with the SendCommand COM function, which triggers functionality
that is part of Vena Desktop.
Table of Contents
Jan Griffiths
Updated 4 months ago
02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 1/12

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
Function and SingleGetValue
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
Product UpdatesCOM Functions
COM Functions and SaveDataETLJobID
Cloud API Functions
Events
Commands
Reference Guide
COM Functions
Function Usage Description
SendCommand Application.COMAddIns("Vena").Object.SendCommand(ActiveWorkbook, "command") See Commands section
GetProperty role = Application.COMAddIns("Vena").Object.GetProperty(ActiveWorkbook, "userrole")Only supported for parameter "userrole", and replaced
with GetUserRole()
GetUserLogin login = Application.COMAddIns("Vena").Object.GetUserLogin(ActiveWorkbook) Returns user's login (email)
GetUserRole role = Application.COMAddIns("Vena").Object.GetUserRole(ActiveWorkbook) Returns role of user in current template (Manager,
Contributor, DrilllThrough)
GetUserName name = Application.COMAddIns("Vena").Object.GetUserName(ActiveWorkbook) Returns [FirstName LastName] of current user
GetCurrentDataModel id = Application.COMAddIns("Vena").Object.GetCurrentDataModel(ActiveWorkbook) Returns (Long) ID of currently loaded data model
GetVenaProcess pid = Application.COMAddIns("Vena").Object.GetVenaProcess(ActiveWorkbook) Returns (string) ID of current process
GetDimensionNumbernum = Application.COMAddIns("Vena").Object.GetDimensionNumber(ActiveWorkbook,
"DimName")Returns the number [1..n] of the dimension with the
provided name (-1 if not found)
GetMemberId memberid = Application.COMAddIns("Vena").Object.GetMemberId(ActiveWorkbook,
"DimName", "MemberName")Returns the member ID of the specified member02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 2/12

SetConfirmSaveErrorApplication.COMAddIns("Vena").Object.SetConfirmSaveError(ActiveWorkbook, "errorMsg") Sets the error message to display when
venaConfirmSaveData() returns false
SendCommand                Application.COMAddIns("Vena").Object.SendCommand ActiveWorkbook,
"refreshstagingtablequeries"Sets a command
COM Functions and SaveDataETLJobID
If a template contains both COM functions and the SaveDataETLJobID Add-in setting, this will impact how Vena responds when a user saves data or saves the
template. In the table below, "yes" means a particular COM function is present in a template, while "no" means the COM function is not present.
User
ActionCOM Function:
venaAfterSaveCOM Function:
venaAfterDataSaveCOM Function:
venaAfterTemplateSaveCOM
Function:
SaveETLJOBID
(Add-in
setting)Expected Result
1 Save
templateNo No No No Template is saved
2 Save
templateNo No No Yes Template is saved
3 Save
templateNo No Yes No Template is saved,
venaAfterTemplateSave macro
is triggered
4 Save
templateNo No Yes Yes Template is saved,
venaAfterTemplateSave macro
is triggered
5 Save
templateNo Yes No No Template is saved
6 Save
templateNo Yes No Yes Template is saved02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 3/12

7 Save
templateNo Yes Yes No Template is saved,
venaAfterTemplateSave macro
is triggered
8 Save
templateNo Yes Yes Yes Template is saved,
venaAfterTemplateSave macro
is triggered
9 Save
templateYes No No No Template is saved,
venaAfterSave macro is
triggered
10 Save
templateYes No No No Template is saved,
venaAfterSave macro is
triggered
11 Save
templateYes No No Yes Template is saved,
venaAfterSave macro is
triggered
12 Save
templateYes No Yes No Template is saved,
venaAfterSave macro is
triggered,
venaAfterTemplateSave macro
is triggered
13 Save
templateYes No Yes Yes Template is saved,
venaAfterSave macro is
triggered,
venaAfterTemplateSave macro
is triggered
14 Save
templateYes Yes No No Template is saved,
venaAfterSave macro is
triggered
15 Save
templateYes Yes No Yes Template is saved,
venaAfterSave macro is
triggered
16 Save
templateYes Yes Yes No Template is saved,
venaAfterSave macro is
triggered,
venaAfterTemplateSave macro
is triggered02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 4/12

17 Save
templateYes Yes Yes Yes Template is saved,
venaAfterSave macro is
triggered,
venaAfterTemplateSave macro
is triggered
User
ActionCOM Function:
venaAfterSaveCOM Function:
venaAfterDataSaveCOM Function:
venaAfterTemplateSaveCOM
Function:
SaveETLJOBID
(Add-in
setting)Expected Result
1 Save dataNo No No No Data is saved
2 Save dataNo No No Yes Data is saved, ETL job is
triggered
3 Save dataNo Yes No No Data is saved,
venaAfterDataSave macro is
triggered
4 Save dataNo Yes No Yes Data is saved, ETL job is
triggered
5 Save dataYes No No No Data is saved,
venaAfterDataSave macro is
triggered
6 Save dataYes No No Yes Data is saved, ETL job is
triggered
7 Save dataYes Yes No No Data is saved, venaAfterSave
macro is triggered,
venaAfterDataSave macro is
triggered
8 Save dataYes Yes No Yes Data is saved, ETL job is
triggered
9 Save dataNo No Yes No Data is saved02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 5/12

10 Save dataNo No Yes Yes Data is saved, ETL job is
triggered
11 Save dataNo Yes Yes No Data is saved,
venaAfterDataSave macro is
triggered
12 Save dataNo Yes Yes Yes Data is saved, ETL job is
triggered
13 Save dataYes No Yes No  Data is saved,
venaAfterDataSave macro is
triggered
14 Save dataYes No Yes Yes Data is saved, ETL job is
triggered
15 Save dataYes Yes Yes No Data is saved, venaAfterSave
macro is triggered,
venaAfterDataSave macro is
triggered
16 Save dataYes Yes Yes Yes Data is saved, ETL job is
triggered
Cloud API Functions
Function Usage Description
VenaRestCall_AddMember ret = Application.COMAddIns("Vena").Object.VenaRestCall_AddMember(ActiveWorkbook,
dimNum, "memberName", "memberAlias", "parentMemberName", "op")Creates a new member.
ParentMemberName can be null or
empty.
Op ""1""=add, ""0""=ignore,
""-1""=subtract.
 Note
If an error occurs, each of the functions in the table below will return a JSON object with the key "error". The value of this object is the error string,
which provides more details about the error.02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 6/12

Returns JSON response from server
(may not be required)
VenaRestCall_AddMemberWithPositionret =
Application.COMAddIns("Vena").Object.VenaRestCall_AddMemberWithPosition(ActiveWorkbook,
dimNum, "memberName", "memberAlias", "parentMemberName",  "previousMemberName",
"op")As AddMember, but with position
information (provide a
previousMemberName as well as a
parent)
VenaRestCall_AddMembers ret = Application.COMAddIns("Vena").Object.VenaRestCall_AddMembers(ActiveWorkbook,
dimNum, MyArray)Creates multiple members (see
comment 1 below)
VenaRestCall_AddAndShareMemberret =
Application.COMAddIns("Vena").Object.VenaRestCall_AddAndShareMember(ActiveWorkbook,
"dimensionName", "memberName", "memberAlias", "parentMemberName", "op")Creates a new member, if member
exists then it will share the
member. ParentMemberName can
be null or empty.
Op ""1""=add, ""0""=ignore,
""-1""=subtract.
Returns JSON response from server
(may not be required)
VenaRestCall_DeleteMember ret =
Application.COMAddIns("Vena").Object.VenaRestCall_DeleteMember(ActiveWorkbook,"dimName",
"memberName", "parentMemberName")Deletes a member ;
parentMemberName is not
optional and needs to be specified
VenaRestCall_GetValue ret = Application.COMAddIns("Vena").Object.VenaRestCall_GetValue(ActiveWorkbook,
Dimensions, Members)Gets intersection value from server
(see comment 2 below)
VenaRestCall_GetValues ret = Application.COMAddIns("Vena").Object.VenaRestCall_GetValues(ActiveWorkbook,
Dimensions, MemberArray)Gets intersection values from
server (see comment 3 below)
VenaRestCall_ClearAllAttributes ret = Application.COMAddIns("Vena").Object.VenaRestCall_ClearAllAttributes(ActiveWorkbook,
"DimName", "memberName")Clears all attribute attachments
from specified member in specified
dimension
VenaRestCall_AttachAttribute ret = Application.COMAddIns("Vena").Object.VenaRestCall_AttachAttribute(ActiveWorkbook,
"DimName", "memberName", "attributeName")Attaches (existing) attribute to
specified dimension member
VenaRestCall_AttachAttributes ret = Application.COMAddIns("Vena").Object.VenaRestCall_AttachAttributes(ActiveWorkbook,
"DimName", "memberName", attributeNameList)Attaches (existing) attributes (listed
in array attributeNameList) to
specified dimension member
VenaRestCall_DetachAttribute ret = Application.COMAddIns("Vena").Object.VenaRestCall_DetachAttribute(ActiveWorkbook,
"DimName", "memberName", "attributeName")Detaches (existing) attribute from
specified dimension member02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 7/12

VenaRestCall_DetachAttributes ret = Application.COMAddIns("Vena").Object.VenaRestCall_DetachAttributes(ActiveWorkbook,
"DimName", "memberName", attributeNameList)Detaches (existing) attributes
(listed in array attributeNameList)
to specified dimension member
VenaRestCall_AddAndAttachAttributeret =
Application.COMAddIns("Vena").Object.VenaRestCall_AddAndAttachAttribute(ActiveWorkbook,
"DimName", "memberName", attributeNameList)Creates and Attaches (new)
attribute to specified dimension
member
IsAttributeAttached ret = Application.COMAddIns("Vena").Object.IsAttributeAttached(ActiveWorkbook, "DimName",
"memberName", "attributeName")Checks if an attribute is attached to
a member; returns True or False
Note on VenaRestCall_AddMembers:
MyArray must be 2D array like:
Dim MyArray(2, 4) As String
MyArray(0, 0) = "BulkMember1"
MyArray(0, 1) = "BulkAlias1"
MyArray(0, 2) = "Departments"
MyArray(0, 3) = vbNullString
MyArray(0, 4) = "1"
MyArray(1, 0) = "BulkMember2"
MyArray(1, 1) = "BulkAlias2"
MyArray(1, 2) = "BulkMember1"
MyArray(1, 3) = vbNullString
MyArray(1, 4) = "1"
MyArray(2, 0) = "BulkMember3"
MyArray(2, 1) = "BulkAlias3"
MyArray(2, 2) = "BulkMember1"
MyArray(2, 3) = "BulkMember2"
MyArray(2, 4) = "1"
Note on VenaRestCall_GetValue:
Dimensions and Members defined as arrays like:
Dim Dimensions(2) As String02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 8/12

Dimensions(0) = "Period"
Dimensions(1) = "Department"
Dimensions(2) = "Year"
Dim Members(2) As String
Members(0) = "jan"
Members(1) = "department 3"
Members(2) = "Y2015"
Note on VenaRestCall_GetValues:
Dimensions and MemberArray defined as arrays like:
Dim Dimensions(2) As String
Dimensions(0) = "Period"
Dimensions(1) = "Department"
Dimensions(2) = "Year"
Dim MemberArray(1, 2) As String
MemberArray(0, 0) = "jan"
MemberArray(0, 1) = "department 3"
MemberArray(0, 2) = "Y2015"
MemberArray(1, 0) = "mar"
MemberArray(1, 1) = "department 1"
MemberArray(1, 2) = "Y2015"
Events
Create these subs in a VBA Module, and Vena Desktop will fire them at the appropriate time.
Function Usage Description
venaBeforeLoad Public Sub venaBeforeLoad() Called once when a file is opened, after the Vena Ribbon is connected,
before the load begins.
venaAfterLoad Public Sub venaAfterLoad() Called once when a file is opened, after all loading and refreshing has been
done, just before returning control to the user02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 9/12

venaBeforeDynamicRefreshPublic Sub venaBeforeDynamicRefresh() Called near the start of a refresh, before dynamic members are refreshed,
which is done before data is refreshed
venaBeforeRefresh Public Sub venaBeforeRefresh() Called after dynamic members are refreshed but before data is refreshed
venaAfterRefresh Public Sub venaAfterRefresh() Called after a data refresh is complete
venaAfterDrillTransaction Public Sub venaAfterDrillTransaction() Called after a drill transaction is complete
venaBeforeSave Public Sub venaBeforeSave() Called before a save (Template or Data) is started
venaBeforeSaveTemplate Public Sub venaBeforeSaveTemplate() Called before a save (Template only) is started
venaBeforeSaveData Public Sub venaBeforeSaveData() Called before a save (Data only) is started
venaAfterSave Public Sub venaAfterSave() Called after a save (Template or Data) is finished
venaAfterSaveTemplate Public Sub venaAfterSaveTemplate() Called after a save (Template only) is finished
venaAfterSaveData Public Sub venaAfterSaveData() Called after a save (Data only) is finished
venaConfirmSaveData Public Function venaConfirmSaveData() "Called before a Data Save (only), and must be a function that returns True
or False.
If False, will NOT continue with save data. If False, can call
SetConfirmSaveError() to set up the message the addin will show to the
user"
VenaAfterLineItemInsert Public Function VenaAfterLineItemInsert() Called after on or multiple Line-Item Detail(s) are added
Commands
Sends a command to Vena Desktop to perform an action. Used in conjunction with the SendCommandCOM function.
Function Usage Description
refresh Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "refresh"Triggers a Refresh Data (as per the button click)
savepartial Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "savepartial"Triggers a Save Data (as per the Save Data button click)02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 10/12

reloaddatamodel Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "reloaddatamodel"Triggers a reload of the currently loaded data model into the Addin's
memory
hide Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "hide"Triggers a Hide (as per the button click)
show Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "show"Triggers a Show (as per the button click)
drill_transaction Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "drill_transaction"Triggers a Transaction Drillthrough (as per the button click)
insertlid Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "insertlid"Triggers a LID Insert (as per the button click)
refreshstagingtablequeriesApplication.COMAddins("Vena").Object.SendCommand
ActiveWorkbook, "refreshstagingtablequeries"Trigger a refresh in the staging table (as per the button selection).
selectlids Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "selectlids"Triggers a LID Select (as per the button click)
movelids Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "movelids"Triggers a LID Move (as per the button click)
removelid Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "removelid"Triggers a LID Remove (as per the button click)
save Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "save"Triggers a Save Data (as per the Save All button click)
multiinsertlids Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "multiinsertlids", NumberOfLidsToInsertTriggers a Multi LID Insert (as per the button click)
Warning: There is no oversight on NumberOfLidsToInsert on the Vena
Desktop side, i.e., it can theoretically be higher than 50
cleardynamics Application.COMAddIns("Vena").Object.SendCommand
ActiveWorkbook, "cleardynamics"Triggers a Hide All Dynamics (as per the button click)
Was this article helpful?02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 11/12

12 out of 16 found this helpful
Related articles
Reference: GetValues() COM Function and SingleGetValue Wrapper Function
How-To: Use Clear Slices to Clear Intersections During an ETL Load
Explainer: Vena User Roles
How-To: Granting Vena Support Access to Your Tenant
Vena Insights Series (Part 4) - Managing Calculations: Measures, Calculated
Tables & ColumnsRecently viewed articles
How-To: Viewing Multiple Datasets at the Same Time With Cascade
How-To: Using Comments in a Template or Report
How-To: Checking Out a File With Concurrent Checkout
How-To: Commenting on Templates in Excel Online
How-To: Using Line-Item Details (LIDs) as a Contributor
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:30 Reference: Vena COM Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/203468789-Reference-Vena-COM-Functions 12/12
