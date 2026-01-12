# (Reference)   Exporting Hierarchies in Vena Using HQL

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
Member Name CharactersReference: Exporting Hierarchies in
Vena Using HQL
Learn how to export hierarchies in Vena using HQL.
Reference
Jun Barrozo
Updated 1 year ago
02/01/2026, 14:10 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 1/5

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
Members?There are several types of expressions that you can use to export hierarchies in Vena using HQL.
These return member positions, so a shared member with two positions would give two rows.
The export type is hierarchy. Below are six examples of different HQL expressions and what they
would return.
Example 1:
Get all members named 2010.
Note: "member" is a reserved keyword, so use "_member" instead.
_member.name = '2010'
Example 2:
Get all members whose name starts with "2".
_member.name LIKE '2%'
Example 3:
Get all members that are parents, in the "Year" dimension.
dimension.name = 'Year' and _member.numChildren > 0
Example 4:
Get all shared members.
_member.numPositions > 1
Example 5:
Get all member positions with operator (+).
Note: use 1 for add (+), 0 for ignore (~), and -1 for subtract (-).
operator = 102/01/2026, 14:10 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 2/5

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
See all 21 articlesExample 6:
Get all bottom level members, in the "Accounts" dimension.
dimension.name = 'Accounts' and _member.numChildren = 0
Was this article helpful?
5 out of 16 found this helpful
Related articles
Reference: Naming Guidelines for Dimension
Members
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple Reports
Explainer: Vena User Roles
Reference: Writing Expressions (MQL & HQL)
Reference: Modeler ExperienceRecently viewed articles
How-To: Building a Custom Roll-up Using
Calculated Members
Reference: Dynamic Member Sets
Reference: Creating a Calculated Number
That Excludes a Member
Explainer: What Are Unmapped Dimensions
and Default Members?
Explainer: What Are Linked Dimensions?02/01/2026, 14:10 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 3/5

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
Didn't find what you're looking for?02/01/2026, 14:10 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 14:10 Reference: Exporting Hierarchies in Vena Using HQL – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207465596-Reference-Exporting-Hierarchies-in-Vena-Using-HQL 5/5
