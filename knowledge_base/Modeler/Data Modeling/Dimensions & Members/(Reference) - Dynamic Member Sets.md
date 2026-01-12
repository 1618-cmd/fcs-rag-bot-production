# (Reference)   Dynamic Member Sets

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
Member Name CharactersReference: Dynamic Member Sets
Learn about the scope of each of the available Dynamic Member Sets.
Overview
When you map a template or create Form Variables or Expressions, Vena allows you to select
hierarchy members dynamically, if desired. This is done using dynamic member sets, which are
specified groups of members defined by their position in the member hierarchy.
Laura Harris
Updated 1 year ago
02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 1/11

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
Members?Selecting members using dynamic member sets is useful if you want your mapping/Form
Variable/Expression to be able to accommodate changes to your data model, such as when
members are added, removed or modified. The available dynamic member sets are:
Children
IChildren
Descendants
IDescendants
Bottom Level
This reference guide illustrates which members are included in each of these sets.
Reference Guide
Hierarchy Diagram
To illustrate how the available sets define groups of members, consider this diagram that
describes a portion of a member hierarchy:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 2/11

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
In this example, our highest-level member is Global Consolidated. This is a parent member, as it
contains sub-members, which are referred to as children: Peak US Operations and Peak Mexico
Operations.
However, while they are children, both Peak US Operations and Peak Mexico Operations are also
parents, as they themselves have children: US001, US002 and US003 and  MX001, MX002 and
MX003, respectively. These members representing the operation areas are referred to as
bottom-level members, as they do not have any children themselves. Thus, they represent the
lowest level of the hierarchy relative to Global Consolidated.02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 3/11

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
Product UpdatesAs shown above, it is important to note that the meanings of the terms parent and child are
relative, and are determined by the frame of reference. This applies in particular to the dynamic
member sets, which are named in reference to the selected member. In the context of using
dynamic member sets, the selected member is the member which you specified prior to choosing
the dynamic member set (e.g., when mapping a template, the member you right-clicked on to
see the dynamic member set options).
In all of the examples below, the selected member is Global Consolidated.
Children
Definition: One level below the selected member in the hierarchy, but no levels below that.
Description: Includes the children of the selected member, but not any of the individual
members at lower levels, i.e., the selected member's children's children.
Illustration:
Includes the members highlighted:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 4/11

IChildren
Definition: The selected member itself and one level below the selected member in the
hierarchy, but no levels below that.
Description: The same as children, except that this set also includes the selected member.
Illustration:
Includes the members highlighted:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 5/11

Descendants
Definition: All levels below the selected member in the hierarchy.
Description: Includes all children of the selected member, the children's children, and so on
until the lowest level of the hierarchy related to the selected member.
Illustration:
Includes the members highlighted:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 6/11

IDescendants
Definition: The selected member itself and all levels below the selected member in the
hierarchy.
Description: The same as descendants, except that this set also includes the selected member
itself.
Illustration:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 7/11

Includes the members highlighted:
Bottom-level
Definition: Only the lowest level in the hierarchy under the selected member.
Description: Includes all members under the selected member that are children only, and no
members from any levels above that.
Illustration:02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 8/11

Includes the members highlighted:
Was this article helpful?
4 out of 6 found this helpful02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 9/11

Related articles
How-To: Mapping Custom Dynamic Member
Sets With the Expression Editor
How-To: Building a Custom Roll-up Using
Calculated Members
How-To: Creating and Managing Data
Permissions
How-To: Creating Tables With Multiple
Dynamic Row Mappings (Multi-Dynamic Rows)
How-To: Use Task Binding To Streamline the
Contributor Experience (Vena Desktop only)Recently viewed articles
Reference: Creating a Calculated Number
That Excludes a Member
Explainer: What Are Unmapped Dimensions
and Default Members?
Explainer: What Are Linked Dimensions?
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 10/11

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 14:09 Reference: Dynamic Member Sets – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/115001776786-Reference-Dynamic-Member-Sets 11/11
