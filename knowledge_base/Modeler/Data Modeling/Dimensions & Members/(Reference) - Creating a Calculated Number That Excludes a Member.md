# (Reference)   Creating a Calculated Number That Excludes a Member

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Dimensions & Members Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
How-To: Assigning Dimension
Types and Standard Members
Explainer: What Is the
Maximum Number of
Dimension Members and
Member Name CharactersReference: Creating a Calculated
Number That Excludes a Member
Use a Calculated Number  to intentionally exclude a member
from a roll-up or calculation.
Overview
Vena Support Team
Updated 1 year ago
02/01/2026, 14:09 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 1/5

How-To: Combining
Dimensions Using Multiple
Expressions for Slices to Clear
How-To: Restoring a Dimension
Member That Was Mistakenly
Deleted
How-To: Bulk Updating
Dimension or Hierarchy
Member Names
How-To: Bulk Attach/Detach
Attributes and Filter by
Attributes
How-To: Search for Members,
Attributes, Aliases and GL
Codes With the Modeler Search
Explainer: What’s the Difference
Between an Alternate Hierarchy
and Calculated Members?
How-To: Copy Data in Bulk and
Save Versioning Configurations
in Modeler
Explainer: What Are Linked
Dimensions?
Explainer: What Are Unmapped
Dimensions and Default
Members?In certain instances, you may want to intentionally exclude a member from a rollup. You can do
this using Calculated Numbers. This reference article explains how to write an expression for a
Calculated Number depending on the member you want excluded from the calculation.
Reference Guide
In the example above, let's say you want to create a rollup of Operation Divisions excluding
Division D. To go about this, the expression will be:
SUBTRACT(CHILDREN('Operating Divisions'),'Division D')
If you want to exclude Dept 401, which is a bottom level child of Division D, then the expression
will be:
SUBTRACT(BOTTOMLEVEL('Operating Divisions'),'Dept 401')
Summary:
If the excluded member is an immediate child:
SUBTRACT(CHILDREN('Target rollup member'),'Child member to be excluded')02/01/2026, 14:09 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 2/5

Reference: Creating a
Calculated Number That
Excludes a Member
Reference: Dynamic Member
Sets
How-To: Building a Custom
Roll-up Using Calculated
Members
Reference: Exporting
Hierarchies in Vena Using HQL
Reference: Naming Guidelines
for Dimension Members
How-To: Using Attribute
Aggregation
Reference: Export Intersections
and Line-Item Details
Troubleshooting: Error While
Processing the Model Slice
Expression When Previewing
Intersections
Troubleshooting: Versioning
Copy To and Copy From must
Contain the Same Set of
Dimensions
See all 21 articlesIf the excluded member is not an immediate child:
SUBTRACT(BOTTOMLEVEL('Target rollup member'),'Bottom level child member to be excluded')
Was this article helpful?
6 out of 10 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Building a Custom Roll-up Using
Calculated Members
How-To: Using Drill Functions (Drill Down, Drill
Save and Drill Transactions)
How-To: Enable & Add a MDR Insert Row to a
Template
How-To: Importing Data to Vena with
Microsoft Power Automate ConnectorRecently viewed articles
Explainer: What Are Unmapped Dimensions
and Default Members?
Explainer: What Are Linked Dimensions?
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Search for Members, Attributes,
Aliases and GL Codes With the Modeler
Search02/01/2026, 14:09 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 3/5

Managing Your Model
Functions
Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
Didn't find what you're looking for?02/01/2026, 14:09 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 14:09 Reference: Creating a Calculated Number That Excludes a Member – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115003655403-Reference-Creating-a-Calculated-Number-That-Excludes-a-Member 5/5
