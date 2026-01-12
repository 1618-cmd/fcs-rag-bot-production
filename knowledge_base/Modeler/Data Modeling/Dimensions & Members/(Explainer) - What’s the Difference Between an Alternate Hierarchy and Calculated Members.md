# (Explainer)   What’s the Difference Between an Alternate Hierarchy and Calculated Members

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
Member Name Characters
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
AttributesExplainer: What’s the Difference Between an Alternate
Hierarchy and Calculated Members?
What is an Alternate Hierarchy?
An Alternate Hierarchy allows you to create alternate groupings of members from an existing data model to simplify mapping and allow for automatic updates
to the data from your source system. In an Alternate Hierarchy, you can repeat the same members in both hierarchies but revise the order of your members via
your alternate hierarchy.  For example, if you need a breakdown by a particular set (e.g., projects in a particular month), you can create an alternate hierarchy to
list the projects in the order of the month they start.
What is a Calculated Member?
In Vena, you have the ability to create special members that are composed of other members through an MQL statement. These members are called Calculated
Members. In practice, Calculated Members are most often used when you want to create a special roll-up that is not supported by your regular hierarchy. This
roll-up can then be used as a custom reporting bucket, representing a useful shortcut when building reports. Calculated members are displayed on a template as
a total of the expression in a single member.
How do I choose which one to use?
Vena Support Team
Updated 7 months ago
02/01/2026, 14:07 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calculated-Members 1/4

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
Copy To and Copy From mustDepending on the scenario, you may have the option of choosing either an alternate hierarchy or calculated members. There are benefits and limitations to both
of these options, outlined below:
Alternate Hierarchy Calculated Member
Only bottom-level members can be shared members. Can contain members from any level of the hierarchy, in any combination.
When you set up an alternate hierarchy, it remains static unless you modify it. Can be dynamic, static or a combination of the two.
The visualization of members is simplified. Visualization occurs via the MQL statement. Visualization in the template is one
line member (components are not broken down).
Supported in Drill Down. Not supported in Drill Down.
Supported in Drill Transactions. Not supported in Drill Transactions.
Can build multiple levels into a hierarchy. Can only be a total.
Can be automatically updated through channels. Not supported.
Can have multiple different alternate hierarchies. This is not easy to accomplish
using attributes or calculated members.Can have multiple different calculated members.
Can be difficult to maintain if you don’t have this information stored
somewhere else. AH are an arbitrary rollup and typically you have to duplicate
every single member in the hierarchy because they need to be part of your alternate
rollups somewhere.Easy to maintain since it is in one expression.
Helpful links
How-To: Build an Alternate Hierarchy02/01/2026, 14:07 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calculated-Members 2/4

Contain the Same Set of
Dimensions
See all 21 articles
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
Product UpdatesHow-To: Build a Custom roll-up using Calculated Members
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Building a Custom Roll-up Using Calculated Members
How-To: Building Alternate Hierarchies
Reference: Writing Expressions (MQL & HQL)
How-To: Maintaining Dimension Member IDs When Updating Existing
Members
How-To: Create and Manage a Data Model Hierarchy Using ETL ImportRecently viewed articles
How-To: Search for Members, Attributes, Aliases and GL Codes With the
Modeler Search
How-To: Bulk Attach/Detach Attributes and Filter by Attributes
How-To: Bulk Updating Dimension or Hierarchy Member Names
How-To: Restoring a Dimension Member That Was Mistakenly Deleted
How-To: Combining Dimensions Using Multiple Expressions for Slices to Clear
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:07 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calculated-Members 3/4

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:07 Explainer: What’s the Difference Between an Alternate Hierarchy and Calculated Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360059243651-Explainer-What-s-the-Difference-Between-an-Alternate-Hierarchy-and-Calculated-Members 4/4
