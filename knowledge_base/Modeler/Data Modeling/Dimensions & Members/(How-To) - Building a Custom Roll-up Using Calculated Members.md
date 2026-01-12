# (How To)   Building a Custom Roll up Using Calculated Members

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
Member Name CharactersHow-To: Building a Custom Roll-up
Using Calculated Members
Create custom roll-ups using Calculated Members for more efficient report creation.
Why use this feature?
In Vena, can create special members that are comprised of other members--called Calculated
Members.
Vena Support Team
Updated 6 months ago
02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 1/10

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
Members?Calculated Members are most often used to create a special roll-up that is not supported by the
regular hierarchy. This roll-up can then be used as a custom reporting bucket, representing a
useful shortcut when building reports.
In this article, you will learn about situations in which Calculated Members can be used, as well
as how to create them.
Before you begin
In order to complete the steps outlined on this page, you need at least Modeler access.
Additionally, to map Calculated Members on templates and reports, you need Manager access
and the relevant Data Permissions for the Calculated Members (if Data Permissions are set up in
your environment).
Use case examples
The following examples illustrate when using a Calculated Member would be recommended. To
go straight to the instructions on how to create a Calculated Member, skip to the How tosection.
Example 1
Imagine that your company operates a number of stores nationwide. In your hierarchy, the
stores are placed under parent members representing the city in which they are located (e.g.,
Chicago, New York, etc.), and are tagged with attributes based on the type of product they carry
(e.g., Widget A, Widget B, etc.).02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 2/10

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
See all 21 articlesGiven this hierarchy, if you were creating a report and wanted to get a number representing just
the stores carrying Widget A, it would not be possible to use a roll-up. Since the hierarchy is
organized geographically, it will give you a roll-up for all the stores in, say, Chicago, but not for all
the stores that carry Widget A (regardless of location). Instead, you would need to find a
different approach.
Example 2
Consider a standard hierarchy in which all of your expense accounts are grouped under a parent
member named Total Expenses. If you build a report and map the Total Expenses roll-up, the
report will display a figure that includes all of the expense accounts listed under the Total
Expenses parent. But what if you wanted to exclude an account?
For example, in some instances, it might be useful to see a figure representing all of your
expenses, but without depreciation included. In this case, the Total Expenses roll-up will not work,
as it will include the Depreciation account. You would need to find some other way of getting
total expenses with depreciation excluded.
Solutions: Alternate Hierarchies vs. Calculated Members
Creating alternate hierarchies with shared members can solve the problem of rolling up specific
members, such as all stores with Widget A or all expense accounts except depreciation.
However, this method can clutter your hierarchy.
A better solution is to use a Calculated Member. By writing a simple expression, you can create a
synthetic parent member for a subset of members (e.g., "all stores with Widget A" or "all
expense accounts except depreciation"). This allows you to use the Calculated Member in
reports for roll-ups.02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 3/10

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
Product UpdatesSome other benefits of using Calculated Members instead of alternate hierarchies:
Parent members cannot be shared, but Calculated Members can include both parent and
bottom level members.
Unlike alternate hierarchies, Calculated Members can be defined both statically and
dynamically.
For a more extensive list of differences between Alternate Hierarchies and Calculated Members,
visit this article.
How to
Setting up a Calculated Member is a two-step process:
1. Create the Calculated Member in the data model.
2. Define the members to be rolled up.
Create & Configure a Calculated Member
Calculated Members are created in the Modeler, similar to the way standard members are
created.
To create a Calculated Member:
1. Navigate to the Modeler tab.
2. Select Data Modeler, then Members in the sidebar.02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 4/10

3. Choose the data model you want to modify using the drop-down menu.
4. Select the dimension under which you want to create the Calculated Member.
 Note
When choosing where to create a Calculated Member, remember it will be
included in the roll-up to its parent member. For more information about the
placement of Calculated Members within your hierarchy, review the Notes & Best
Practices section at the end of this article.02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 5/10

5. Right-click on a member that is on the same level as where you want to create the Calculated
Member.
6. Select Add Calculated Member from the menu that appears.
Add Calculated Member functions essentially the same way as Add Sibling in that the new
member is created alongside the member that you right-clicked on, not above (parent) or
below (child).
7. In the text box that appears, type in a name for the Calculated Member.
8. If desired, you can also specify an Alias, add an attribute or select an operator for the
Calculated Member. If you want to skip this, leave the text box blank.
9. If you are ready to configure your Calculated Member, proceed to step 11. If you want to
configure your Calculated Member at a later time, select Save.
02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 6/10

10. Once you have created a Calculated Member, you need to specify which members it will
comprise. You do this by writing an expression, a short instruction that defines the members
and (optionally) attributes that you want to include or exclude.
11. Select Σ Edit Expression.
12. The Editing Calculated member window will appear with the name of the Calculated Member
listed at the top. In the text field provided, type in your expression using Model Slice Query
Language (MQL):
Expressions are constructed using MQL syntax.
Please use this reference guide for comprehensive help with writing MQL expressions.
13. When you have entered your expression, select Save.
14. The Calculated Member is now ready to be used.
15. You can always edit a Calculated Member by right-clicking on it and selecting Edit.02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 7/10

Notes & best practices
Calculated Members must be located at the bottom-level of the hierarchy. They cannot be
parent members or have child members.
When you right-click on a member which has been configured with an expression, the option
Validate Calculated Members is available. Note that selecting this option only performs cycle
detection on the expression and cannot determine if the expression is otherwise valid (i.e.,
whether it will work in an intended way).
Because intersections formed with Calculated Members are not "true" intersections, the
Preview intersections function found in the Data Modeler does not work for Calculated
Members.
We recommend creating Calculated Members at the root level of a dimension or under a
designated parent. This ensures accurate roll-ups, as including Calculated Member under a
parent in the hierarchy and then mapping that parent on a report will cause incorrect figures.
Alternatively, if you do wish to place a Calculated Member among your hierarchy, you can
prevent it from being included in roll-ups to its parent member by setting the Operator for
the Calculated Member to '~' (i.e. "do not include in roll-up").
The character limit for Calculated Members is 255.
Was this article helpful?
15 out of 16 found this helpful
Related articles Recently viewed articles02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 8/10

Reference: Writing Expressions (MQL & HQL)
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
How-To: Using Expand and Collapse with
Multi-Dynamic Row Mappings
Reference: Vena 365 Manager Start GuideReference: Dynamic Member Sets
Reference: Creating a Calculated Number
That Excludes a Member
Explainer: What Are Unmapped Dimensions
and Default Members?
Explainer: What Are Linked Dimensions?
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:09 How-To: Building a Custom Roll-up Using Calculated Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/208150543-How-To-Building-a-Custom-Roll-up-Using-Calculated-Members 10/10
