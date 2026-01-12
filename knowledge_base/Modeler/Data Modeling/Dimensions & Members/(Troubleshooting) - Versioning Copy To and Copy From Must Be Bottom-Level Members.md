# (Troubleshooting)   Versioning Copy To and Copy From Must Be Bottom Level Members

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
Member Name CharactersTroubleshooting: Versioning Copy To
and Copy From Must Be Bottom-Level
Members
Issue summary
When trying to run a versioning job or save a versioning configuration, you may receive the
following error message:
Olalekan Adebayo
Updated 1 year ago
02/01/2026, 14:13 Troubleshooting: Versioning Copy To and Copy From Must Be Bottom-Level Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27390514036237-Troubleshooting-Versioning-Copy-To-and-Copy-From-Must-Be-Bottom-Level-Members 1/5

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
Members?Copy to and Copy from must be bottom-level members.
Suggested solution
1. Ensure the dimension members in your Copy From or Copy To are not parent members.
2. If one of the dimension members in your Copy From or Copy To is a calculated member,
ensure the calculated member's expression window is blank and does not contain any
expression as shown below. For example, 'Empty' is a common calculated member used in02/01/2026, 14:13 Troubleshooting: Versioning Copy To and Copy From Must Be Bottom-Level Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27390514036237-Troubleshooting-Versioning-Copy-To-and-Copy-From-Must-Be-Bottom-Level-Members 2/5

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
See all 21 articlesversioning to clear our other dimension intersection values.
Cause
This could happen if one of the dimension members in your Copy From or Copy To is a parent
or calculated member with an expression in it.
Keywords
versioning, copy to, copy from, must be bottom-level member 02/01/2026, 14:13 Troubleshooting: Versioning Copy To and Copy From Must Be Bottom-Level Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27390514036237-Troubleshooting-Versioning-Copy-To-and-Copy-From-Must-Be-Bottom-Level-Members 3/5

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
Product UpdatesWas this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
How-To: Data Model Series (Part 3): Attributes
and Versioning
Troubleshooting: Versioning Copy To and
Copy From must Contain the Same Set of
Dimensions
How-To: Using Drill Functions (Drill Down, Drill
Save and Drill Transactions)
How-To: Setting Up a NetSuite Connector and
Data FeedRecently viewed articles
Troubleshooting: Versioning Copy To and
Copy From must Contain the Same Set of
Dimensions
Troubleshooting: Error While Processing the
Model Slice Expression When Previewing
Intersections
Reference: Export Intersections and Line-Item
Details
How-To: Using Attribute Aggregation
Reference: Naming Guidelines for Dimension
Members02/01/2026, 14:13 Troubleshooting: Versioning Copy To and Copy From Must Be Bottom-Level Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27390514036237-Troubleshooting-Versioning-Copy-To-and-Copy-From-Must-Be-Bottom-Level-Members 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:13 Troubleshooting: Versioning Copy To and Copy From Must Be Bottom-Level Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/27390514036237-Troubleshooting-Versioning-Copy-To-and-Copy-From-Must-Be-Bottom-Level-Members 5/5
