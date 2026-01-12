# (How To)   Viewing Multiple Datasets at the Same Time With Cascade

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
Vena DesktopHow-To: Viewing Multiple Datasets at
the Same Time With Cascade
With Vena Desktop's Cascade feature you can view different datasets side-by-side,
allowing you to quickly switch between them.
Why use this feature?
Jan Griffiths
Updated 2 months ago
02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 1/24

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
Function and SingleGetValueIn Vena, Managers have the ability to configure Excel templates with multiple "page options" -
user-selectable filters that allow different datasets to be viewed on the same template.
Most often, you will interact with page options by using Vena Desktop's Choose button to switch
between datasets on the same worksheet. This is fine for many use cases, but what if you need
to repeatedly switch back and forth between datasets, such as when comparing reports? In this
situation, having both datasets open side-by-side would be preferable, and the Cascade
function lets you do just that.
Like Choose, Cascade allows you to view different page options on a template - but instead of
displaying a single dataset at a time, Cascade can open several of them simultaneously, so you
can switch between them much faster than you could with Choose. With Cascade, you can choose
between two main ways of doing this: either view the different datasets on separate worksheets
within the same file, or as separate files.
In this article, you will learn how to use the different options of the Cascade function on both
Vena Desktop and the Contributor Connector for Mac/Office Online, as well as the benefits and
limitations of each of the available options.
Before you begin
To follow the instructions in this article, you will need Manager or Contributor access. If Data
Permissions are set up in your environment, you will also need the appropriate permissions for
the data that you are working with.
Vena Academy E-Learning02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 2/24

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
Product UpdatesHow to
Cascade is supported in both the Vena Desktop, and the Contributor Connector for Mac and
Office Online, though the available options differ between the two. In general, you can use
Cascade on any template or report which has selectable page options, i.e. any file on which you
can use the Choose function.
To use Cascade, simply click on the Cascade button:
Vena Desktop
Contributor Connector for Mac/Office Online
To learn more about the Cascade feature, take this interactive e-learning course. 02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 3/24

This will open the Cascade menu, from which you can choose the specific page options you want
to cascade, and how you want to cascade them. The available options for cascading are outlined
below.
Instructions for Vena Desktop for Windows
Instructions for Contributor Connector for Mac/Office Online
 Note
Bear in mind that the main purpose of the Cascade feature is to allow very similar
datasets to be viewed side-by-side: it is designed in such a way that cascaded
datasets will differ in only one dimension, even if page options are available for more
than one dimension.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 4/24

Using Cascade  in Vena Desktop
Cascading to sheets
The default and most commonly used option of Cascade is Cascade to sheet, which opens the
different datasets on different worksheets within the same Excel file. With this option, switching
between datasets is as simple as clicking on their respective worksheet tabs.
The benefit of using this option is that each of the resulting worksheets remains connected to
Vena, allowing you to refresh the data they contain at any time. However, using Cascade to sheet
on a large or complex original worksheet can take a very long time, and may result in a very
large file.
For example, if you have page options in the Years and Departments dimensions on a
given report, you can choose to cascade members of any one dimension (e.g. "2015
and 2016", or "Sales and Finance"), but not a combination of dimensions (e.g. "2015
and Sales and Finance").
 Note
If one of the selected page options is already displayed on the existing worksheet, it
will not be opened as a new worksheet to avoid duplication.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 5/24

To use Cascade to sheet:
1. Log in to Vena and open a template that has multiple page options configured.
Do this from the Files Library as a Manager, or by using it from the Task List as a
Contributor.
2. Open the template in Excel, and choose whichever page options you want to view initially.
3. When the template has loaded, click on the Cascade button in the Vena ribbon:
4. This will open the Cascade menu. Here, you should see that the dropdown in the lower left
corner already shows Cascade to sheet (if not, set it to this option):
5. You will also be prompted to choose the dimension that contains the page options you want
to cascade:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 6/24

6. When you have selected a dimension, the hierarchy browser section will appear. This displays
the members of the selected dimension that have been configured as page options on this
template:
7. Use the hierarchy browser to select your page options. You can select just a single page
option by clicking on it, or multi-select by clicking on each page option while holding down
the Ctrl key:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 7/24

8. When you have chosen the page options you want to cascade, click on OK. Vena will process
the cascade operation, and the page options will appear as new sheets in your workbook:
 What does Create choose options do?
When you select Cascade to sheet, you will also see a checkbox for Create choose
options:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 8/24

Cascading to files
If you would prefer to view each dataset in a separate file, rather than as worksheets in the same
file, you can use the Cascade to file option. This is useful if you want to create one-off reports
This option applies only to files with a particular structure, namely those that have
multiple sections with dynamic page options. Using Cascade to sheet on this kind of
file can result in a situation where the cascaded sheets have their own selectable page
options.
By default, the Choose function will show a single drop-down menu for each
selectable page option that appears on the original sheet, and this selection will also
drive the page options displayed on the cascaded sheets.
However, if you want to choose page options for each cascaded sheet separately
from those on the original sheet, you can check the box next to Create choose options,
and this will expand the Choose menu with additional drop-down menus for each
cascaded sheet, so that you can choose the page options on every sheet individually
(rather than seeing the same page options across all sheets).02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 9/24

with different dataset variations from a single main report, such as for use in presentations or
distribution by email. You can also use Cascade to file when you want multiple datasets to be
visible at the same time, such as on separate monitors.
The main downside to this option is that none of the resulting files remain connected to Vena, so
the data they contain can't be refreshed from Vena using the Refresh button. Instead, you would
need to repeat the cascading operation to get refreshed data.
To cascade to separate files:
1. Follow steps 1-7 under the Cascading to sheets section above.
2. After you have selected the desired page options, but before you click on OK, change the
dropdown menu in the lower left from Cascade to sheet to Cascade to file:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 10/24

3. Click on OK, and the Browse For Folder window will open. Use it to choose the location on your
computer where you want to save the files that will result from the cascade. When you have
chosen the location, click on OK.
4. Each of the cascaded files will be processed (you will see the Vena loading bar in Excel) and
saved to the specified location. Note that, once the loading bar disappears, nothing in Excel
will appear to have changed. This is normal - the cascaded files will not open automatically,
but will be saved in the specified folder and can be opened from there.
5. Navigate to the folder on your computer that you specified in step 3, and you should see the
cascaded files. Each file will be named automatically with the name of the template and the
name of the page option to which it pertains:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 11/24

6. You now can now open the cascaded files as standard Excel files.
Cascading without mappings
If you want to cascade a lot of datasets at once (i.e. five and up), you can consider the Cascade
without mappings option. By eliminating the Vena mappings from the resulting worksheets, it can
often reduce the time needed to complete the cascade operation, and can also avoid Excel
crashes when you cascade larger templates. The result is very similar to Cascade to sheets, except
that the resulting Excel file is much smaller and can often perform better.
As with Cascade to file, the main limitation of this option is that data on the resulting worksheets
can't be refreshed when you use the Refresh button in Vena Desktop.
 Note
Remember that none of the files generated by Cascade to file will be Vena-enabled, so
the Vena ribbon in Excel will appear in its disconnected state when you open these
files.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 12/24

To cascade to without mappings:
1. Follow steps 1-7 under the Cascading to sheets section above.
2. After you have selected the desired page options, but before you click on OK, change the
dropdown menu in the lower left from Cascade to sheet to Cascade without mappings:
3. Click on OK, and the cascade will be processed (you will see the Vena loading bar). When it is
complete, the selected page options will appear as new sheets in your Excel file, just as they
do with the Cascade to sheets option:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 13/24

Using Cascade in the Contributor Connector for
Mac/Office Online
You can also use Cascade in the Contributor Connector when using Vena on a Mac or in Office
Online. The Contributor Connector version of Cascade supports one type of cascade operation,
which is very similar to the Cascade without mappings option in Vena Desktop. As with that
option, the worksheets generated by using Cascade in the Contributor Connector will be
disconnected from Vena, and can't be refreshed with the Refresh function.
 Note
Unlike the Cascade to sheet option, Cascade without mappings will generate a new
sheet for every page option that you choose, even if it is a duplicate of the one
displayed on the existing worksheet.
In addition, remember that sheets generated by Cascade without mappings can't be
refreshed. Sheets that result from Cascade without mappings can be identified by
their light blue tab color.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 14/24

To use Cascade in the Contributor Connector:
1. Navigate to the Contributor or Tasks tab, and open the task which contains the task form
you want to use (it should have multiple page options configured).
2. Choose whichever page options you want to view initially, then open the file using your
preferred option (Mac or Office Online) in the normal way.
3. When the task form has loaded, click on the Cascade button in the Contributor Connector
menu:
4. This will open the Cascade menu:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 15/24

5. First, use the drop-down under Select a dimension to cascade to choose the dimension that
contains the page options you want to cascade:
02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 16/24

6. Next, use the selection pane under Select a member to choose the page options that you want
to cascade. Simply click on a page option member to highlight it, and add it to the Select
Members pane on the right by clicking on the > button:
7. Continue adding members that you want to cascade to new sheets to the SelectedMembers
pane. Members that you have added to the Selected Members pane will become grayed out in
the Select a member pane:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 17/24

8. You can also multi-select members in the Select a member pane by holding down the Ctrl key
while you click on them, and you can filter the list of members by using the Filter Member
search box. If you need to remove members that you previously added to the Selected
Members pane, simply click on them, then click on the < button. Or, click on Clear All to
remove all current selections.
9. Once you have finished making your selections, click on the OK button. The Contributor
Connector will process your cascade operation:
10. When it has finished processing, you will see a message that your cascaded data is available
in a new window:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 18/24

11. Click on Open, and your cascaded sheets will be displayed in a new browser window (or tab):
12. Note that the cascaded sheets are disconnected from Vena, and the Contributor Connector
will not be displayed on them as a result. However, your original worksheet will remain open
in a separate tab/window, and you can return to it to use the functions of the Contributor
Connector there. You can also easily identify the cascaded sheets because they will have
CASCADED in the filename shown at the top of the window:02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 19/24

Notes & limitations
With concurrent check-out, it will not be reflected if a user has applied Cascade to sheets.
If a section is mapped that feeds into another section on another tab it will not cascade
properly.
The Cascade function was designed for use on reports. While it can also be used on input
templates, you should be aware that inputs made on cascaded sheets will not be saved to
the database when you click Save Data - only the original sheet may be used for data inputs.
Because the Cascade to sheet option copies Vena mappings to the cascaded sheets, saving
data inputs on those sheets is theoretically possible, but this is disabled by default. To
enable data saves on cascaded sheets, you can set AllowSaveAfterContributorCascade to
True (Settings > Advanced). However, we strongly recommend against doing this, as
Cascade was not designed for input templates, and changing this setting can cause
unexpected template behavior and other issues.
There is also a related setting, AllowSaveAfterManagerCascade. If set to True, it allows you to
use Save Template after using Cascade, which will save the cascaded sheets onto the
template as well.
After using Cascade to sheet, you can remove additional (cascaded) worksheets from the
workbook by right-clicking on them, then clicking on Delete.
If you are using the file as a Contributor, deleting the cascaded worksheets is not
necessary, as they will not be saved when you close the file.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 20/24

The only exception is if the file is a Hybrid or Standalone file: in these cases, cascaded
sheets will be retained in the file (per the rules for the applicable template property).
Using Cascade multiple times with different page options selected will result in additional
worksheets being opened. If you use Cascade to sheet, the cascaded worksheets from the
previous cascade operation will be removed and replaced. If you use Cascade without
mappings, the new worksheets will simply be added on to the existing ones.
Like Choose, Cascade will only work on files with selectable page options. If a file does not
have selectable page options, the Choose button will be disabled (greyed out) in the Vena
ribbon:
While the Cascade button will remain active (clickable/not greyed out) if there are no
selectable page options, clicking on it will result in an error message:
For Cascade to sheet/Cascade without mappings: Any form controls or ActiveX objects with
assigned macros on a template will be removed from the original sheet upon cascading,
while those without assigned macros will be left on the original sheet, but will not be
included in the cascaded sheets.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 21/24

Vena-enabled files rely on Named Ranges for mappings to work. When you use Cascade to
sheet, the majority of Named Ranges from the original sheet are copied to the cascaded
sheets, essentially multiplying the number of Named Ranges in the workbook by the number
of cascaded sheets. The total number of Named Ranges that can exist in an Excel workbook
is limited by the memory available on your computer, so if a Cascade to sheet operation
causes this limit to be exceeded, Excel will crash. If this happens, consider cascading on fewer
page options, or use Cascade without mappings.
If you use Cascade on a file that contains multiple sections with Line-Item Details, the
cascaded sheets will only enable Line-Item Details (LIDs) for the same section you cascaded
from. This is because, in the resulting cascaded sheets, only the section that was cascaded
can be expected to differ from the original sheet, while in most cases the other sections
would be identical to the original. Enabling LIDs on these identical sections would cause an
error in Vena Desktop. To avoid this, LIDs are therefore not enabled on the sections expected
to be identical to the original (i.e. those that were not cascaded).
Bear this limitation in mind if your template is designed such that the section being
cascaded dynamically drives other sections (e.g. a dummy section). In this case, the
sections that were not cascaded would actually not be identical to the original sheet when
they appear on the cascaded sheets. However, because of this limitation, they would still
not have LIDs enabled.02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 22/24

Was this article helpful?
5 out of 6 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Enable & Add a MDR Insert Row to a
Template
How-To: Access Vena's Training Platform
How-To: Using Scratchpads in Vena 365
How-To: Formatting Columns in Vena InsightsRecently viewed articles
How-To: Using Comments in a Template or
Report
How-To: Checking Out a File With Concurrent
Checkout
How-To: Commenting on Templates in Excel
Online
How-To: Using Line-Item Details (LIDs) as a
Contributor
How-To: Using a File With Concurrent
Contributor in the Tasks Tab02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 23/24

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:30 How-To: Viewing Multiple Datasets at the Same Time With Cascade – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206510533-How-To-Viewing-Multiple-Datasets-at-the-Same-Time-With-Cascade 24/24
