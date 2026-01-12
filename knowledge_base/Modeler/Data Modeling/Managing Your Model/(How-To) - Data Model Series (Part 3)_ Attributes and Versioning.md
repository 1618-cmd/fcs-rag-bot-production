# (How To)   Data Model Series (Part 3)  Attributes and Versioning

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Managing Your Model Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
Managing Your Model
Explainer: What is Data Model
Standardization?
How-To: Build Your Chart of
Accounts Hierarchy in Quick
StartHow-To: Data Model Series (Part 3):
Attributes and Versioning
About this series
This series is all about how to build and use Data Models. You are in Part 3, which provides step-by-
step instructions on how to add and manage attributes and Versioning in a Data Model.
This series was designed to be read in order. If you don't have any previous experience with the Data
Model tool, we recommend that you follow this approach, starting with Part 1. But if you are already
Vena Support Team
Updated 5 months ago
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 1/22

How-To: Formatting an Excel-
Based CSV to Maintain Leading
Zeros for ETL Jobs
How-To: Data Model Series
(Part 1): Creating a Data Model
How-To: Data Model Series
(Part 2): Hierarchies and Roll-
Ups
How-To: Data Model Series
(Part 3): Attributes and
Versioning
How-To: Data Model Series
(Part 4): ETL Tool
How-To: Build and Manage
Data Models in Modeler
How-To: Building Alternate
Hierarchies
How-To: Adjusting How Vena
Treats Zero Values in the
Database
How-To: Creating a Testing
Environment by Cloning a Data
Model (Clone & Remap)
How-To: Undo a Versioning ETL
Job Without Line-Item Detailsfamiliar with Vena Data Models and are just looking for a refresher, you can also feel free to dip in
anywhere within this series.
Part 1:  Building a Data Model
Part 2: Hierarchies and Roll-ups
Part 3:  Attributes and Versioning -you are here
Part 4: ETL Tool

Before you begin
To follow the instructions in this article, you will need at least Modeler access. If Data Permissions are
set up in your environment, you will also need the appropriate permissions for the data that you are
working with.
Table of contents
Attributes overview
Attributes
Attribute tools
How To
Create an attribute
Delete an attribute
Edit an attribute name02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 2/22

How-To: Undoing a Versioning
ETL job with Line-Item Details
(LIDs)
How-To: Downloading All Vena
Data From Your Tenant or
Environment
Troubleshooting: The Bulk Copy
Parameters Were Invalid
Troubleshooting: This Member
Does Not Exist Error During
Modeler Search
Troubleshooting: ETL Error –
Cannot Increase the Number of
Members Beyond 400000
Troubleshooting: Encountered
More Than the Limit of 1000
Unmapped Members
Functions
Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad HocAttach a dimension member to an attribute
Remove a dimension member from an attribute
Versioning overview
How to
Version data
Background processing
Related topics
Attributes overview
Attributes
Data model members, including bottom-level and parent members, can be labeled with Attributes.
Attributes group members with shared properties, even if they are in different parts of the hierarchy.
For example, office supplies like pens and markers may share a color attribute, such as blue.
Using attributes allows for the easy retrieval of members with specific characteristics, regardless of their
location within the hierarchy.
In Vena templates, attributes can be used with the Expression Editor to dynamically map members
based on selected page options. For instance, choosing a page option can filter table rows to show only
members with the corresponding attribute.
The following is an example of tagging members with attributes:
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 3/22

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
As an example, Vena can produce a Dynamic Range based on any of the attributes.
‘silver’ will produce the list of Members: Yaris, Corolla, and Odyssey
'silver’ UNION ‘CD’ will produce a list of Members: Yaris, Accent, Corolla, Odyssey
Attribute tools
A Modeler can leverage the Attributes functionality to tag Dimension Members with specific attribute
names. For example, a department Dimension Member can be tagged with a location attribute, such as
London.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 4/22

AModeler tab The area of the application where elements such as data models,
integrations and the ETL tool reside.
BData Modeler page This page used to create and manage data models, attributes and
versioning.
CMembers page The Members page is how you access, create and manage your
dimensions and members.
DChoose Data ModelSelect a data model from the available list.
EDimensions View, edit or delete dimensions.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 5/22

FManage Lists existing attributes, as well as the options to create or delete
attributes. Note: In Standard Models, you will see a Manage drop-
down menu. Under the drop-down menu, you can manage your
attributes and range rules. Visit this article for more information on
range rules.
GAttached Members Displays current attributes assigned to members.

How to
Create an attribute
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Locate the dimension member you want to add an attribute to.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 6/22

4. Right-click on the dimension member and select Edit from the menu.
5. Select + Add Attribute. A drawer opens with a list of existing attributes.
6. Select + Add Attribute.
7. Enter an attribute name.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 7/22

8. Select + Add Attribute to save the new attribute.
9. Select Done to close the drawer.
Delete an attribute
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select Manage A ttributes. This opens the attributes drawer.
4. Hover over the attribute you want to delete and select the
 (delete) icon.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 8/22

5. Select Yes, Delete Attribute in the pop-up confirmation.
Edit an attribute name
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select Manage A ttributes. This opens the attributes drawer.
Note
If you are using a Standard Model, select Manage > Attributes. 02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 9/22

4. Hover over the attribute you want to edit and select the
(pencil) icon.
5. Rename your attribute.
6. Select Update to finalize the changes.
7. Select Done to close the drawer.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 10/22

Attach a dimension member to an attribute
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Locate the dimension member you want to add an attribute to.
4. Right-click on the dimension member and select Edit from the menu.
5. Select the check-box next to each attribute in the drop-down menu that you want to attach to the
dimension member.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 11/22

6. Select + Update to save your changes.
Remove a dimension member from an attribute
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Locate the dimension member you want to add an attribute to.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 12/22

4. Right-click on the dimension member and select Edit from the menu.
5. Uncheck the check-box next to each attribute in the drop-down menu that you want to remove from
the dimension member.
6. Select + Update to save your changes.
 Versioning overview
Versioning allows Modelers to bulk copy data from one group of intersections and write them to
another group of intersections within the same data model. The desired data set can be isolated by
adding Dimension Members in the Page(s) box. The Page(s) box acts as a list of filters for identifying the
data set to copy. For example, a Modeler may want all collected "Plan" data to become the pre-
populated "Forecast" data for a particular year.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 13/22

AVersioning Displays utilities used to bulk copy data between dimension members.
BDimension Members Navigate and select dimension member.
CSaved Configurations Existing versioning configurations that you can run and edit.
DConfiguration Name Choose a name for your versioning configuration.
EFilter Dimensions by
MembersUse the Filter section to narrow down what data you want to copy, i.e.,
limit copying to data involving your selected members.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 14/22

FCopy From Copy from dimension member.
GCopy To Copy to dimension member.
HCopy Line Items Choose whether line items are copied; and if so, in which format.
IVersion Parent MembersChoose whether parent members will be included or not when
defining what to copy.
JClear Destination
Intersections Before CopyIf selected, Vena will clear out all values in the destination (“Copy To”)
intersections, then copy over the values from the source (“Copy
From”).
KRun Calcs If you have any Vena Calcs set up that include the destination
intersections in their scope, this option allows you to specify whether
or not those calcs are executed when the data copy is performed.
LSave Save your versioning configuration.
MRun Execute copy based on chosen parameters.
Learn more about Versioning in Modeler.
 02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 15/22

How to
Version data
1. Log in to Vena and navigate to the Modeler tab.
2. Select Data Modeler.
3. Select Versioning from the sidebar tab.
4. Select the appropriate data model from the data model drop-down list at the top of the page.
5. Input a name for your Versioning Configuration.
02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 16/22

6. Select the dimension that you want to copy.
7. Choose a member that describes the type of intersections you would like to bulk copy, then hover
over that member row. Three icons should appear:
Filter Dimension by Members
Copy From
Copy To
Select the
 (Filter Dimension by Members) button to add your member to the Filter Dimension
by Members section under Versioning Configuration.
Note
If you choose to run your Versioning configuration immediately, you do not have to input
a name. However, if you intend to save the configuration for a later date, you must
include a name.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 17/22

8. Use the Filter section to narrow down what data you want to copy, i.e., limit copying to data involving
your selected members. For example, if you were copying your budget, you would choose the
Budget member (or similar).
9. Next, choose the member that you would like to copy from and select
 (Copy From) in the
Member row to add it to the Copy From section. This is where you select the source of the data to be
copied.
For example, if it were currently 2020 and you wanted to copy your 2020 budget to 2021, you would
choose the Y2020 (or similar) member here. If you leave this section blank, Vena will copy all data for
Note
You can add more than one member from unique dimensions. For example, during a
cycle rollover, if you want to version last year's December Actuals to January Budget, Copy
from: 2020 (Year), Actuals (Scenario), December (Month). Copy to: 2021 (Year), Budget
(Scenario), January (Month).02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 18/22

all dimensions in the data model.
10. Now, choose the member that you would like to copy to and select the
 (Copy To) button to add
it to the Copy To section. This is where you select the destination of the copied data. For example, if
you wanted to copy your 2020 budget to 2021, you would choose the Y2021 (or similar) member
here.
11. For basic Versioning, do not change the options from their default settings (see a screenshot of
default settings, below):
Note
The member you choose for Copy To and Copy From must be the same dimensions.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 19/22

By leaving the default settings unchanged, this means you answer "No" to the following questions:
- Do you want to clear all destination intersection values before copying? No
- Do you want to copy line items? No
- Do you want to run calls? No
- Do you want to version parent members? No
See Advanced Versioning Options below for more information on these functions.
12. Select Run to start the Versioning job, which will copy the specified values. You can also select Save
to save your configuration without running it.
13. If you select the Run button, Vena will create and process a new Versioning job, and display a
message confirming that your Versioning job has started.
14. Versioning jobs appear with ETL jobs in the History section of the Modeler interface, where you can
see their status.
For information on Versioning in the Modeler, please refer to this article.
Background processing
The Versioning process may take longer depending on the volume of intersections being copied. During
this time, the data model remains unlocked, allowing users to use Vena regularly while the data copy
processes in the background.
 To view the status of your job:
1. Select Data Modeler.
2. Select History from the sidebar.
3. Your job should be visible on the ETL Jobs page.
4. In the table, you'll see Versioning jobs with Versioning in the Job Name column, along with an outline
of the configured job.02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 20/22

5. You can check the job status using the indicators on the right side.
Related topics
Check out this article to learn how to dynamically map tables based on attributes.
Check out this article to learn how to copy data in bulk with Versioning.
Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
2 out of 3 found this helpful
Related articles
How-To: Copy Data in Bulk and Save Versioning
Configurations in Modeler
How-To: Assigning Dimension Types and
Standard Members
How-To: Bulk Attach/Detach Attributes and Filter
by AttributesRecently viewed articles
How-To: Data Model Series (Part 2): Hierarchies
and Roll-Ups
How-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)
How-To: Data Model Series (Part 1): Creating a
Data Model02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 21/22

How-To: Roll Over a Process for the Next Cycle
How-To: Data Model Series (Part 2): Hierarchies
and Roll-UpsHow-To: Formatting an Excel-Based CSV to
Maintain Leading Zeros for ETL Jobs
How-To: Build Your Chart of Accounts Hierarchy
in Quick Start
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:15 How-To: Data Model Series (Part 3): Attributes and Versioning – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360039572432-How-To-Data-Model-Series-Part-3-Attributes-and-Versioning 22/22
