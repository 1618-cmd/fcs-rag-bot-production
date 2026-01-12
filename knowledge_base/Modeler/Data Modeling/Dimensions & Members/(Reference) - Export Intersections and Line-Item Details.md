# (Reference)   Export Intersections and Line Item Details

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
Member Name CharactersReference: Export Intersections and
Line-Item Details
Overview
When applying a filter against an extract of intersections or line items details, you must use
Model Slice Expression Language syntax.
Vena Support Team
Updated 4 months ago
02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 1/6

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
Members?
On the ETL Command Line Tool, you can leverage the Intersections and Line-Item Detail export
by choosing to use different filter query options.
02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 2/6

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
See all 21 articlesReference Guide
Model Slice Query Language
Below is an overview of how to create a Model Slice Query. For more information about MQL,
visit this article.
Here is an example expression from that language:
dimension('Time': children('Q1'))
dimension('Department': children('Software Development'))
Syntax formatting
The query consists of a list of 'dimension(...) expressions separated by whitespace.  There should
be one for each dimension in the model.  This example would apply to a model having two
dimensions: 'Time' and 'Department'.
The right-hand part of the dimension expression describes what members to include for that
dimension. Thus, the example expression we looked at previously, selects all children of 'Q1' for
the 'Time' dimension and all children of 'Software development' for the 'Department' dimension:
Children
IChildren
Descendants
IDescendants
BottomLevel
Ancestors
IAncestors
Parents
Ascendants02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 3/6

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
Product UpdatesThese can be combined with the following set operators:
Union
Intersection
Subtract
Not
Building on our earlier example, we could use the following expressions:
dimension('Time': union( children('Q1') children(Q2)) )
dimension('Department': not( children('Software Development')) )
You can also list members one by one like this:
 dimension('Time': union('Q1' 'Q2') )
Line-Item Details
For Line-Item Detail, you can filter on the Label and/or ID:
label(name('My Label'))
label(ETLId(#1234567))
Was this article helpful?
2 out of 10 found this helpful02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 4/6

Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Enabling Line Item Details (LIDs) in a
Template or Report
How-To: Using Line-Item Details (LIDs) as a
Contributor
How-To: Exporting CSV Files for ETL Job
Reference: ETL Guide - 1 - OverviewRecently viewed articles
How-To: Using Attribute Aggregation
Reference: Naming Guidelines for Dimension
Members
Reference: Exporting Hierarchies in Vena
Using HQL
How-To: Building a Custom Roll-up Using
Calculated Members
Reference: Dynamic Member Sets
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:11 Reference: Export Intersections and Line-Item Details – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/204264029-Reference-Export-Intersections-and-Line-Item-Details 6/6
