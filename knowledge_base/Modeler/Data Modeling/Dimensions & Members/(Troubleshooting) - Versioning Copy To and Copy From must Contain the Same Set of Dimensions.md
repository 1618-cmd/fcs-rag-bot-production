# (Troubleshooting)   Versioning Copy To and Copy From must Contain the Same Set of Dimensions

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
and Copy From must Contain the
Same Set of Dimensions
Issue summary
When trying to run a versioning job or save a versioning configuration, you may receive the
following error message: Copy to and C opy from must c ontain the s ame s et of dimensions .
Olalekan Adebayo
Updated 2 years ago
02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 1/6

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

Suggested solution
This may happen if you do not have the same set of dimensions in the Copy From and Copy To
sections. In the example below, we must add Period in the Copy From section and Year in the
Copy To section.02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 2/6

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
See all 21 articles
We will need to update the parameters so that the Copy From and Copy To sections have the
same set of dimensions.
Now, we are copying from Year to Year and from Period to Period.02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 3/6

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
Once completed, you will be able to run the versioning job successfully or save the versioning
configuration successfully.
Cause
This could happen if you do not have the same set of dimensions in the Copy From and Copy To
sections.02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 4/6

Keywords
versioning, copy to, copy from, must contain the same set of dimensions
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Data Model Series (Part 3): Attributes
and Versioning
Explainer: What is Data Model
Standardization?
How-To: Creating Tables With Multiple
Dynamic Row Mappings (Multi-Dynamic Rows)
Reference: Writing Expressions (MQL & HQL)Recently viewed articles
Troubleshooting: Error While Processing the
Model Slice Expression When Previewing
Intersections
Reference: Export Intersections and Line-Item
Details
How-To: Using Attribute Aggregation
Reference: Naming Guidelines for Dimension
Members
Reference: Exporting Hierarchies in Vena
Using HQL02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:12 Troubleshooting: Versioning Copy To and Copy From must Contain the Same Set of Dimensions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15552012841741-Troubleshooting-Versioning-Copy-To-and-Copy-From-must-Contain-the-Same-Set-of-Dimensions 6/6
