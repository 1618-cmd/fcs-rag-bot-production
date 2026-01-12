# (Reference)   Vena Calcs   1   Managing Scripts

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Calcs (Scripts) Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Calcs (Scripts)
Explainer: Target Member
Attribute Calc Trigger
Reference: Sparse CalcsReference: Vena Calcs - 1 - Managing
Scripts
About this series
This series is about how to write and use Vena Calculation Scripts. You are on Part 1, which
provides an overview of Calc Scripts and how to manage them.
Vena Support Team
Updated 1 month ago
02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 1/29

Reference: Vena Calcs - 1 -
Managing Scripts
Reference: Vena Calcs - 2 -
Notation and Syntax
Reference: Vena Calcs - 3 - Data
Types
Reference: Vena Calcs - 4 -
Operators
Reference: Vena Calcs - 5 -
Functions
Reference: Vena Calcs - 6 -
Conditional Statements
Reference: Vena Calcs - 7 -
Currency Conversions
Reference: Vena Calcs - 8 -
Examples
Reference: Vena Calcs - 9 -
Troubleshooting
Troubleshoot: Calc Target
Contains Data Even Though It
Shouldn’t
Troubleshooting: Calc Conversion
Not Working or Zero Values
AppearingVena Calculations Scripts (or Vena Calcs) is a scripting language designed for Vena data models.
Vena Calcs provides a powerful and flexible way to run calculations and simulations for business
rules at the database level for all dimensions and members.
You can apply Calcs for a variety of uses, including:
Calculating financial ratios and percentages
Departmental/employee allocations
FX currency conversions
We've broken down Vena Calcs into nine articles. They can be read consecutively or browsed as
needed.
Part 1: Managing Scripts - You are here
Part 2: Notation and Syntax
Part 3:Data Types
Part 4: Operators
Part 5:Functions
Part 6:Conditional Statements
Part 7: Currency Conversions
Part 8:Examples
Part 9: Troubleshooting
 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 2/29

Troubleshooting: Calc Is Not
Triggering or Calculating After
Data Load or Import
Troubleshooting: Calc Script
Using .BottomLevel() and
.Exclude() in a Tuple Not Working
Properly
Troubleshooting: No Values
Generate for a Reporting
Currency
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesVideo
Check out a video of this article's content.
Video Vena Calcs Part 1 Video Vena Calcs Part 1
Table of contents
Calc Scripts Overview
Calc Script Editor
How To
Create a Calc Script Page02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 3/29

Managing a Calc Script Page
Script Writing
Revisions (Script History)
Deploy and Undeploy
Calculation Graph
Calculation Profiler
Script Details
Calc Scripts Overview
Vena Calc Scripts are data-model-specific and only work within the model they are written in.
Calc Scripts can be created by adding script pages under the desired data model.
Calc Script Editor
Vena Calc Scripts are input and managed on the front-end Script Editor. To use the editor
effectively, it is important to familiarize yourself with the functionality.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 4/29

Feature Description
ASearch Locate specific Calc Scripts using the Search bar.
BRename Choose a name for your calc.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 5/29

CDelete Delete your calc.
Caution: Deleting a calc erases all values associated with it, impacting all
templates and reports linked to that script.
DRevisions Calculation History Viewer: Compares the script’s current version with
a past one. Learn more about calc revisions.
E Save Select Save any time you make changes to a Calc Script.
F"Disable/"EnableEnabling a Calc Script allows it to run whenever its source intersection
data changes.
Disabling a Calc Script effectively turns it “off” and it will not run.
GDeploy/
Undeploy Deploying a calc means running the script with all existing data currently
saved in the data model.
Undeploying a calc means erasing all values saved by this calc. Learn
more about Deploy/Undeploy and how it impacts calc scripts.
H View Calc ProfilerProvides an in-depth overview of the execution of a calculation or set of
calculations.Learn more about the Calc Profiler.
ICalculation
GraphShows a view of the dependencies between different calculations,
allowing you to see which calculations depend on which other
calculations. Learn more about the Calc Graph.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 6/29

J Add Calc Script
PageCreates a new Calc Script page for the data model. Each page is
managed through the buttons at the top of the list of data models.
Depending on the current state of the script, the exact list of options
available may vary (e.g., Deploy/Undeploy, Enable/Disable).
KScript Detail Shows the number of total potential intersections in the sources stated
by each scope and the potential resulting number of target
intersections.
How To
Create a Calc Script Page
1. Navigate to the Modeler tab.
2. Select Scripts in the sidebar to access your scripts.
3. Select the folder for the data model you want to create a calc for. Each folder represents a
data model and can be expanded to show all calcs associated with it. 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 7/29

4. Select + to create a new Calcs Script Page.
02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 8/29

5. Enter a name for your new Calcs Script and select Save.
6. Once you have created your page you can start on your Calcs Script.
Managing a Calc Script Page02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 9/29

Script Writing
Select your Vena Calc Script to view its contents. By default, the script is enabled and comes into
effect as soon as you can save it successfully. Vena does not save the script if there are errors.
Verification is applied to the syntax whenever a script is saved. If there are errors upon saving, a
debug window appears below the script window.
An asterisk (*) after the name of the script signifies it has unsaved changes. A green icon means
that the script is currently enabled. Greyed out names means it is not enabled.
Revisions (Script History)
Select Revisions to access a script’s Calculation History and compare the current version of a
script with a past version of the same script.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 10/29

In the view (below), the current version of the script is shown in the right pane, and an older
version is shown to the left. Above each pane is the name of that version of the script and its
enabled/disabled state.
Select the drop-down menu in the left pane to choose from all previous versions of the calc.
These versions are listed by date and time and provide a short summary of the differences
between that version and the previous version.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 11/29

Deploy and Undeploy
Deploying a calc means to run the script with all existing data currently saved in the data model.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 12/29

1. Select Deploy. A confirmation message appears, prompting you to select Deploy to continue.
2. In cases with large amounts of data, this process could take several hours to complete.
Monitor the status of the deploy in the History tab of the sidebar menu.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 13/29

Undeploying a calc means erasing all values that were saved by this calc. This is particularly
helpful for debugging. For example, if a user inputs data in USD, the calc would produce the
following data for CAD:
Jan Feb Mar
USD 100 120 110
CAD 105 127 11602/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 14/29

If a user then saved the value 140 to the intersection at Feb>CAD, then selected Undeploy, the
sheet would display:
Jan Feb Mar
USD 100 120 110
CAD 140
Calculation Graph
The Calculation Graph shows a view of the dependencies between different calculations (which
calculations depend on which other calculations).
Viewing the Graph
View the Calculation Graph by selecting the eye icon (
) in the Data Model row.
02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 15/29

When the graph is built, Vena reads each calculation and generates a node for every bottom-
level scope. Each node is labeled with the calculation name and a number for the scope it came
from.
The first bottom-level scope in a calculation begins with the number 0 and each successive
scope receives the next number. If a node’s name is too long, it’s shortened with an ellipsis (...).
To view the full name, move your mouse over that node.
To view the full names of all nodes at the same time, select Show full names of all calculations
on the bottom left of the window.
Arrows in the graph point from sources to targets. In the example below, the node FX Convers...
uses a value produced by the node Forecast [....]:02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 16/29

Hovering over a node highlights its connecting arrow and provides more information.
Incoming arrows are green and outgoing arrows are blue. The counters in the bottom left list the
number of nodes acting as sources (incoming) and as targets (outgoing) of the current node. 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 17/29

Example 1 below highlights a node with four outgoing targets:
Example 2 below highlights a node with four incoming sources:02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 18/29

Manipulating the Graph
Selecting a node hides all other nodes not connected to it. Select Back To Previous View to
bring back the other nodes. 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 19/29

Select and drag a node allows to reposition it in the view.
Use the mouse scroll wheel to zoom in and out.
Calculation Profiler
The Calculation Profiler provides an in-depth overview of the execution of a calculation or set of
calculations.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 20/29

To open the profiler, select the clock icon (
) next to a data model.
ADate & TimeDay and time of the current data set. Select this drop-down for data from the
10 most recent deploys or ETL data loads in real time.
BNode ListA list of all the nodes being calculated. Each can be expanded to view a listing
of all steps involved in the calculation.
CCalculation
GraphA view of how the Calculation Graph looked at the time of the deploy. If the
deploy is currently in progress, the completed nodes will be colored green.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 21/29

Nodes currently being calculated will be colored blue and nodes to be
calculated will be colored grey. If the deploy has been completed, all nodes
will be colored green.
Below is a sample calculation expanded in Profiler, from a data model containing almost 37,000
intersections to be sources for this calculation. For large amounts like this, Vena creates batches
of up to 1000 source intersections, resulting in 37 batches in this case. 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 22/29

This calculation took the following steps:
1. Fetched the intersections to be used for this batch.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 23/29

2. Built the graph specific to those intersections.
3. Found the groups of interdependent intersections in the graph.
4. Loaded any dependencies.
1. Cached dependencies are values either supplied in the source intersections or calculated
by a previous step.
2. Missing dependencies are new values that need to be fetched from the Cube, if, for
example, the calculation has other sources from the cube which were not part of the
current batch of 1000.
5. Calculated each group
1. In this case, for 1000 source intersections, there were 1000 independent groups, meaning
that there were no interdependent intersections in the batch.
6. Stored the results in the Cube.
1. In this case, from 1000 source intersections, Vena produced 1000 results, meaning that
each of those source intersections directly produced a result. If, for example, one of the
source intersections was an FX rate, we might see many more than 1000 results
produced.
In the right column, the profiler lists the time, in milliseconds, that each step took. In this
example, calculation A took just over 44 seconds, with Batch #1 taking 2.333 seconds and Batch
#2 taking 1.488 seconds.
Note
If a calculation has multiple sources from the cube and only one of them is supplied in a batch,
then in Step #4, the rest of the intersections will be fetched for that specific calculation.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 24/29

Later in the deploy, those intersections will be part of some other batch. In that case, Vena
knows that they have already been used to produce a value and won’t recalculate it. In this case,
less than 1000 results may be produced.
Script Details
Script Details show the number of total potential intersections in the sources stated by each
scope and the potential resulting number of target intersections. They can also be used to
calculate the potential fan-in/out ratio (the number of potential sources to the number of
potential targets).
Select the green graph icon (
) next to the script to open Script Details. 02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 25/29

02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 26/29

Calculation name The first scope of the calc that is highlighted.
# of source intersectionsThe number of potential source intersections in scope or subscope.
# of target intersectionsThe number of potential target intersections in scope or subscope.02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 27/29

Was this article helpful?
4 out of 4 found this helpful
Related articles
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 4 - Operators
Reference: Vena Calcs - 6 - Conditional
Statements
Explainer: Target Member Attribute Calc
TriggerRecently viewed articles
Reference: Sparse Calcs
Explainer: Target Member Attribute Calc
Trigger
How-To: Using Vena’s Foreign Exchange (FX)
Conversion Function
Reference: Vena’s Foreign Exchange (FX)
Conversion Function FAQs
Troubleshooting: Encountered More Than the
Limit of 1000 Unmapped Members
Didn't find what you're looking for?02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 28/29

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 14:23 Reference: Vena Calcs - 1 - Managing Scripts – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027865191-Reference-Vena-Calcs-1-Managing-Scripts 29/29
