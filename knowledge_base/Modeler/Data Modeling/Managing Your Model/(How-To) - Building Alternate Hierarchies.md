# (How To)   Building Alternate Hierarchies

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
Accounts Hierarchy in QuickHow-To: Building Alternate
Hierarchies
Create custom roll-ups usingAlternate Hierarchiesfor efficient report creation.
Why use this feature?
An alternate hierarchy allows you to create alternate groupings of members from an existing
data model to simplify mapping and allow for automatic updates to the data from your source
Laura Harris
Updated 1 year ago
02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 1/11

Start
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
Model (Clone & Remap)system. In an alternate hierarchy, the same members can be repeated in both hierarchies, but
the way in which you order or roll up your members can be revised via your alternate hierarchy.
For example, if you need a breakdown by a particular set (e.g., projects in a particular month),
you can create an alternate hierarchy to list the projects in the order of the month that they
start.
(If you’re unsure whether to use an alternate hierarchy or a calculated member to meet your
project needs, learn more here.)
Before you begin
In order to complete the steps outlined on this page, you will need at least Modeler access and
the appropriate Application Permissions for the model you are updating.
If Data Permissions are set up in your environment, you will also need the appropriate
permissions for the data that you are working with.
Vena Academy E-Learning
To learn more about setting up custom roll-ups with alternate hierarchies, take this
interactive e-learning course. 02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 2/11

How-To: Undo a Versioning ETL
Job Without Line-Item Details
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
AdminHow to
Create an alternate hierarchy
To create an alternate hierarchy, you will need to add additional sibling and child members to
your existing hierarchy of choice. In the example, below, we will be adding an alternate hierarchy
to a data model used for tracking projects.
Create new Parents, Siblings, and Children
1. Log into vena.io and navigate to the Modeler tab.
2. Locate the data model where you want to create the alternate hierarchy and find the relevant
member.02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 3/11

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates3. Right-click the Parent member and select Add Sibling from the drop-down menu.
4. Enter the name of your new member.
5. Select  +Add Member.
6. Depending on how you want to organize your hierarchy, you can continue to add Siblings.
7. Once you’ve created your Siblings, right-click the sibling member you just created and select
Add Child. 02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 4/11

8.  Name your new member and select +Add Member.
9. Continue until you’ve finished adding all your child members. Once you’ve added your
children, the next step is to share your members to the alternate hierarchy.
Share Members02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 5/11

1. To share members to an alternate hierarchy, right-click on a member (or select the vertical
ellipses beside the member) and select Share Member from the drop-down menu.
2. A confirmation message confirming that the member is ready to share will appear.
3. Right-click the Child member you want to share to and select Complete Share from the drop-
down menu.02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 6/11

4. Confirm that the member has been successfully shared when the
 symbol appears next
to both the original member and the shared member.02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 7/11

02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 8/11

5. Once you’ve finished sharing all your members, your alternate hierarchy is ready for use.
02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 9/11

Was this article helpful?
7 out of 10 found this helpful
Related articles
How-To: Building a Custom Roll-up Using
Calculated Members
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Bulk Updating Dimension or
Hierarchy Member Names
How-To: Build and Manage Data Models in
Modeler
How-To: Setting up Page Options for the
Choose BoxRecently viewed articles
How-To: Build and Manage Data Models in
Modeler
How-To: Data Model Series (Part 4): ETL Tool
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
How-To: Creating a Testing Environment by
Cloning a Data Model (Clone & Remap)02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:16 How-To: Building Alternate Hierarchies – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055667031-How-To-Building-Alternate-Hierarchies 11/11
