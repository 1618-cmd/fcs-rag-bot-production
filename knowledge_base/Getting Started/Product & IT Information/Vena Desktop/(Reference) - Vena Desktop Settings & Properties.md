# (Reference)   Vena Desktop Settings & Properties

Vena Solutions/Getting Started/Product & IT Information/Vena Desktop Search
Getting Started
Fundamentals
User Account Management
Support
Product & IT Information
Vena and Excel
Vena Desktop
How-To: Validating the
Authenticity of Your Installed
Vena Desktop Add-in
How-To: Removing the V365
Task Pane From Vena Desktop
How-To: Installing and
Updating the MSI Version of
Vena DesktopReference: Vena Desktop Settings &
Properties
Desktop Settings
Desktop Settings can be found in any Excel Desktop template. The settings table provides a list
of all properties associated with that particular template.
Locating template setting properties and values
1. Open any template > Vena Desktop > Settings > Advanced tab.
Vena Support Team
Updated 4 months ago
31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 1/22

Reference Guide: Vena Desktop
Keyboard Shortcuts
How-To: Customizing the Vena
Desktop Menu Ribbon
How-To: Updating Vena
Desktop
How-To: Disabling Vena
Desktop Reference in Outlook
and Word
Reference: Vena Desktop
Settings & Properties
How-To: Restoring a Missing
Vena Desktop
How-To: Checking Your Version
of Vena Desktop
Troubleshooting: Unable to
Install Vena Desktop
Troubleshooting: Access to the
path 'Vena Installer.exe' is
denied
Troubleshooting: Vena Desktop
Requires the URLs To Be Added
to Your Internet Trusted Sites
Troubleshooting: Vena Desktop
Requires Higher Version of .NET2. The left column will denote the Property Name, and the right column will contain drop-down
selections of possible Property Value.
These are the available properties from which Admins can select default-specific values
for all users.
31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 2/22

Framework During Installation
Troubleshooting: Formatting
and Formulas are Not
Displaying as Expected in Vena
Templates
Troubleshooting: Vena Desktop
Application Download Did Not
Succeed
Troubleshooting: Vena Desktop
Application Cannot Be Started
Vena 365
Explainer: What is Central
Deployment?
Resource: System Requirements
for All Vena Platforms and Add-
Ins
How-To: Getting Vena 365 for
Windows or Installing Vena
Desktop
How-To: Using Vena on a Mac or
Office Online With the Tasks Tab
How-To: Getting Vena for Mac or
Office Online
Explainer: What Are Vena
Desktop and Vena 365?Desktop Properties
Desktop Properties is a front-end user interface designed for users with the Admin role to
apply, modify, and/or delete properties for all users on the same tenant. This centrally located
interface allows admin users to specify global default settings for the Vena Desktop.
Create a Desktop property
1. Admin > Policies > Desktop Properties.
2. Select the Add Property button.
3. Fill in the New Property Name and Value fields exactly as they are denoted in the template's
settings (which can be found in the prior step).
4. Select Create.
5. Settings, as configured in the Desktop Properties, will now be applied to all users on the
same tenant.
Delete a Desktop property
1. Admin > Policies > Desktop Properties.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 3/22

How-To: Adding Vena To Trusted
Sites
How-To: Accessing Your Sandbox
Environment
How-To: Using Vena on a Citrix
Machine or Environment
How-to: Checking and Installing
.NET Framework
How-To: Clearing Your Browser
Cache
Reference: Restricted File Types
in Vena
Resources
General Troubleshooting
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc2. Locate Desktop Property in the central area.
3. To remove, select X on the desired property.
Notes/Best Practices
1. The names of the properties and values need to be entered exactly as they are denoted in
Settings, otherwise an invalid property/value will be saved.
2. Currently, only the existing Settings from the Vena Desktop can be edited in the Desktop
Properties.
3. A Contributor can still go into templates and change Settings, but they will not save. Upon
closing out of the template, they will revert to the Default properties as set by the Admin
user.
Future Development
1. New settings and properties outside of the Vena Desktop can be added in the Desktop
Properties.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 4/22

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesAdvanced and Workbook Settings
This table lists and describes all the Vena Desktop Settings or Properties including Advanced and
Workbook Settings.
Setting Name Default Description
AccessibilityMode FALSE If set to TRUE, some UI elements
changed to a form to allow easier
screen reading and keyboard
navigation.
AddinUserAgent Mozilla/5.0 (compatible;
MSIE 10.0; Windows NT
6.1; Trident/6.0)The HTTP user-agent, which the
addin sets in HTTP requests.
AddLIDSubtotalsToNumeric
ValuesOnlyTRUE If set to TRUE, this feature will
enable subtotals to be calculated
for members with Line-Item
Details and all Line-Item Details
for that member having numeric
values only.
AllowLIDConflictDeletes FALSE If the Template is set up in a way
that creates LID conflicts, we
don't allow LID Saves (because
the conflicts mean LID data
doesn't currently make sense). If31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 5/22

something goes really wrong, you
can't even delete these
potentially broken LIDs. This
allows all LID deletes to be saved
when there are conflicts (which
can be dangerous in itself).
AllowSaveAfterContributor
CascadeFALSE If set to TRUE, this feature allows
a Contributor to Cascade a
Template and click Vena Save.
AllowSaveAfterManager
CascadeFALSE If set to TRUE, this feature allows
a Manager to Cascade a Template
and click Vena Save
AskToCheckinOnDisconnect TRUE When true, a prompt will ask a
Contributor to return an assigned
File by selecting “Disconnect”.
AuditTrailNewValueCellColor Green Colors used for new values in
Audit Trail compare.
AuditTrailValueChangedCellColorLight Blue Color is used for changed values
in the Audit Trail comparison.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 6/22

ClearValuesOnSaveTemplate FALSE If set to TRUE, intersection values
are cleared, and Line-Item Details
are hidden for each template
before saving the template. After
a template is saved, the
intersection values and Line-Item
Details are restored.
DMode FALSE If set to TRUE, this feature allows
the user to access selective Vena
Development options.
DrillParentMaxIntersection 1000 The maximum number of
intersections to return from the
drill parent tool.
The upper limit on this setting is
100000.
DrillThroughIntersectionColorMedium Purple This feature helps you select the
color with which the cell in the
template instance from which the
value originally came is
highlighted.
EmbedOfflineProperties
OnSaveFALSE If set to TRUE, additional Vena
data for offline use is saved when
the file is saved.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 7/22

EnableBrowserCheckinPrompt
IfAskToCheckinIsFalseTRUE If set to TRUE, the user will be
reminded to return to the Vena
web app browser to check the file
if AskToCheckinOnDisconnect is
false.
EnableCascadeChooserForm TRUE This settings option allows users
to disable/enable the Cascade
Choose feature. By default, it is
set to TRUE.
The user can revert to the old
Cascade feature and interface if
set to FALSE.
EnableCascadeChooserForm TRUE This settings option allows users
to disable/enable the Cascade
Choose feature. By default, it is
set to TRUE.
If set to FALSE, the User can
revert to the old Cascade feature
and interface.
EnableMacroRecorder TRUE Developer only. This enables
internal automation test creation
tools.
EnableMemberSearchButton FALSE When set to FALSE, the Choose
Box searches available members
on every keystroke.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 8/22

When set to TRUE, a button
appears in the Choose Box
member search. When the button
is selected, the available
members will be searched.
EnableMultipleDataModels FALSE When set to TRUE, the Desktop
can open and work with
templates and multiple data
models.
ForceMacroCommandPopups
HashCOmmentsInStagingQueries
HideColumnText #hidecolumn Displays the Vena command
syntax (#hidecolumn) used for
hiding columns.
HideRowText #hiderow Displays the Vena command
syntax (#hiderow) used for hiding
rows.
HideTemplateValidationResultsFALSE If set to TRUE, the results after
validating a template (i.e. Vena
errors/warnings pane) will not be
displayed.
HttpGetResponseTimeoutIn
Milliseconds600000 The maximum time the Desktop
will wait for a response from the31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 9/22

server.
Although it says maximum GET
response, this value seems to be
applied to all HTTP requests.
JsonLogPath C:\Users\Joe\AppData
\Roaming\VenaSolutions
\VenaSPM\VenaSPM.logThe location of the JSON log.
The user cannot change this
value; it defaults to the location of
the Vena log. May be unused.
JsonTruncateLengthInChars 1024 Unused.
LastPromotedUpdateVersion 1.0.0.0 The last version of the Desktop
the user was presented for
update.
This setting gets updated
automatically.
LastSuccessfulServiceURL The last URL the Desktop
successfully used to connect to
Vena.
Users do not need to update this
value.
LaunchVenaMonitorOnConectTRUE31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 10/22

LineItemDetailsColor Light Blue Not used.
LockCheckColumnText #lockcheckcolumn Displays the Vena command
syntax (#lockcolumn) used for
locking column(s).
LockCheckRowText #lockcheckrow Displays the Vena command
syntax (#hidecolumn) used for
hiding columns.
LockColumnText #lockcolumn Do not change. This is the
keyword that Vena uses to unlock
a row in conjunction with the
LockCheckRowText.
LockRowText #lockrow Do not change. This is the
keyword that Vena uses to unlock
a row in conjunction with the
LockCheckColumnText.
LogJson TRUE Not used.
MappedRangeHighlightColor Red The color used by the highlight
range tool.
NumberOfDrillThroughRevisions10 The maximum number of
revisions displayed by the drill-
through tool.
OfflineEnabled FALSE If set to TRUE, the Go Offline
button will be enabled. This31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 11/22

feature might be deprecated
soon
OldUpdateCheckMd5Hash Not used.
OpenVenaWorkbooksInSeparate
ExcelInstancesIf set to TRUE, each Vena
workbook will open in a new
instance of Excel. If FALSE,
multiple Vena workbooks may be
opened by the same instance of
Excel.
PasswordOverride The password to use to unlock
Vena workbooks. This setting is
only necessary for overriding the
sheet's password set by the Set
Sheet Password tool.
PromptIfAllPasswordsFail TRUE Possibly unused.
ProtectedViewDelayedConnect
TimeoutInMilliseconds1000 Not used.
RangeConcatenatorString
OverrideIf not blank, this string will be
used to concatenate ranges for
building Excel ranges such as:
A1,B4,D12. (In this example the
comma is the range separator.) In
general, this should not need to
be set, as we determine the range
when the worksheet opens. If this31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 12/22

determination fails, setting this
value may fix issues specific to
localized non-English
environments.
RefreshAllConnectionsOnData
RefreshTRUE If TRUE, refreshes the workbook's
external data ranges and
PivotTable reports (set up
through standard Excel
functionality) when Vena updates.
SaveNewBlankLIDsOnExisting
LIDRowsTRUE If set to FALSE, new line item
entries found in existing line item
rows will not be saved if they are
blank.
ServerAsyncSaveEnabled FALSE If set to TRUE, Asynchronous save
will be enabled.
ShowAttributeMembers
InExpressionEditor
ShowChooseAsList
ShowColumnText #showcolumn Displays the Vena command
syntax (#showcolumn) that needs
to be used for showing columns.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 13/22

ShowRevVarButton
ShowRowText #showrow Displays the Vena command
syntax (#showrow) to be used for
showing rows.
ShowVenaUpdatePopupOn
CloseTRUE If set to FALSE, notification about
Vena Desktop update will not be
shown on close.
SkipProxyCredentialsCheck FALSE If set to TRUE, web requests
through proxy will skip checking
whether proxy requires
authentication.
SuppressRefreshOnLoad FALSE If set to FALSE, this will load the
page without refreshing the data.
UnlockColumnText #unlockcolumn Displays the Vena command
syntax (#unlockcolumn) to be
used for unlocking column(s).
Also used with #lockcolumn
condition when the latter does
not hold true.
UnlockRowText #unlockrow Do not change. Vena uses this
keyword in conjunction with the
LockCheckColumnText to unlock
a row.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 14/22

UpgradeNeeded TRUE If set to TRUE, Vena will attempt
to update its settings.
If set to FALSE, settings are up-to-
date.
Users do not need to update this
value.
ValidateOnSaveTemplate FALSEIf set to TRUE,  If set to TRUE, this feature will
run Analyze/Validate Template
before all Save Templates and
warn about errors.
WarnLIDNotFullyDisplayed
OnDeleteTRUE If set to TRUE, the user will be
warned when deleting a line-item
row if there are other line-item
entries associated with the row
that is not in the current
template.
WarnManagerSaveOnly
SavesDataTRUE If set to TRUE, the manager(s) will
be warned that Save Data does
not save the template.
WarnOnRefresh TRUE If set to TRUE, a message will be
shown on refresh reminding the
user that refreshing will cause
any unsaved data change to be
discarded.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 15/22

Users may set this to FALSE by
clicking "Do not remind again" on
the reminder dialog.
WarnUnlockedParentCells FALSE If set to TRUE, this feature will
warn about unlocked parent cells
WebCachingEnabled FALSE If set to TRUE, the Desktop's web-
caching feature will be enabled.
AllowMultiChoose FALSE
CheckProtectedOverride FALSE
CollapseChooseBoxmembers FALSE
DisableClearingBrokenFV
IntersectionsFALSE
ExternalDataSourceURL Sets the URL for the external data
source drill tool.
FastChooseEnabled
FastFormulaScanEnabled If TRUE, evaluating whether cells
have formulas or are locked is
performed using cached values. If
FALSE, read all cells again.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 16/22

FullRefreshAfterPerBlockList If TRUE, a refresh will be
performed on all remaining
blocks after blocks specified by
per-block refresh.
HideDynamicsOn
SaveTemplateFALSE
LastSaved
LoadedSuccessfully Indicates whether the workbook
settings were successfully loaded.
Users cannot directly update
these settings.
CheckProtectedOverride If TRUE, evaluate whether cells
are locked using the worksheet's
Evaluate method. If FALSE,
evaluates whether cells are
locked using a special formula on
a hidden sheet.
Comments in the code indicate
this setting is meant to be
temporary.
DisableClearingBrokenFV
IntersectionsIf FALSE, unlocked intersection
cells with broken form variables
will be cleared.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 17/22

HashCommentsIn
StagingQueriesTRUE When TRUE, lines in staging query
results which begin with # will be
treated as comments.
When FALSE, lines in staging
query results which begin with #
will not be treated as comments
and will appear in staging table
query results.
The default behaviour matches
previous releases, the new
behaviour uses a new library with
the same performance but is
standards-compliant. The new
behaviour fixes  EA-1208 - Staging
tables not working
properly DONE, should be
deprecated upon further testing.
HideDynamicsOnSaveTemplate If TRUE, Line-Item Details, multi-
dynamic blocks, dynamic rows
and dynamic columns will be
cleared when the template is
saved. Dynamic page options are
unaffected.
MaximumColumns
BeforeWarning1000 The number of columns at which
a warning will be displayed to
managers indicates that template31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 18/22

performance may be affected by
the size of the template.
MaximumRowsBeforeWarning10000 The number of rows at which a
warning will be displayed to
managers indicates that template
size may affect template
performance.
MDRRowInsertSectionName Select combination for
data entry
PerBlockRefreshNodes
PreventBrokenFVDoubleRefreshFALSE If TRUE, second refresh will be
prevented when the template has
broken form variables.
PreventCellReferenceUpdates
OnCascadeFALSE
RibbonButtonMap
RibbonButtons
SaveDataETLJobID
SolutionPackageName31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 19/22

SolutionPackage
TemplateName
SolutionPackage
TemplateVersion
UpdateStaticMappings TRUE If TRUE, text cells with static
mappings will be updated to
reflect their current member
name each time a template is
opened. If FALSE, text cells with
static mappings will not be
updated.
Note: If FALSE, this setting is
changed to TRUE when the
template is saved.
UseTextFormatForDrill
TransactionFALSE If TRUE, worksheets created by
the Drill Transactions tool will
have all cells formatted as strings.
UISettings Persists default UI properties
such as PCR form dimensions.
Users cannot directly update
these settings.31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 20/22

Attachments
Add In Properties.pdf300 KB
Vena Desktop (Windows) Settings and Description .docx30 KB
Was this article helpful?
4 out of 4 found this helpful
Related articles
How-To: Getting Vena 365 for Windows or
Installing Vena Desktop
How-To: Enabling Line Item Details (LIDs) in a
Template or Report
How-To: Mapping Data From Multiple Data
Models on a Single Template (Vena Desktop
Only)
How-To: Setting up a Staging Query (Vena 365
Only)Recently viewed articles
How-To: Disabling Vena Desktop Reference in
Outlook and Word
How-To: Updating Vena Desktop
How-To: Customizing the Vena Desktop Menu
Ribbon
Reference Guide: Vena Desktop Keyboard
Shortcuts
How-To: Installing and Updating the MSI
Version of Vena Desktop31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 21/22

How-To: Granting Vena Support Access to
Your Tenant
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request31/12/2025, 12:54 Reference: Vena Desktop Settings & Properties – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206681023-Reference-Vena-Desktop-Settings-Properties 22/22
