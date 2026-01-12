# (How To)   Bulk Attach Detach Attributes and Filter by Attributes

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
Member Name CharactersHow-To: Bulk Attach/Detach
Attributes and Filter by Attributes
Maintaining your attributes is easier than ever with new features like bulk attach
attributes and filter by attribute.
Why use this feature?
Laura Harris
Updated 7 months ago
02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 1/12

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
Members?With Vena’s new attribute maintenance functionality, we’ve introduced two new features to
enhance how you work with attributes. Bulkattribute attach and detach lets you add or
remove multiple attributes to a dimension member with a few easy clicks. With filter by
attribute, searching through your attributes is easier than before. You can quickly filter through
a dimension hierarchy by a specific attribute and view all members currently attached to that
attribute.
In this article, you’ll learn about attribute maintenance, how to bulk attach and detach attributes
and how to filter a hierarchy by a specific attribute.
Before you begin
To follow the instructions in this article, you will need Modeler access. If you’re unfamiliar with
how to create an attribute, please check out this article.
Table of contents
How to
Bulk attribute attach and detach
Attach attributes
Detach attributes
Filter by attributes
Notes02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 2/12

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
See all 21 articlesHow to
Bulk attribute attach and detach
Attach attributes
In the example below, we’ll add the attribute Currency to specific members in the Measure
dimension.
1. Log in to vena.io and select the Modeler tab.
2. Navigate to the Data Modeler page and select the data model where you want to manage
your attributes.
3. Select the dimension where you want to manage the associated attributes.
4. Use the checkboxes next to the member names to select the members that you want to add
attributes to.02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 3/12

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
5. Select the Actions menu and select Attach Attributes from the drop-down menu.
6. Use the drop-down list in the Attach Attributes pop-up to select your desired attributes. You
can also select multiple attributes.02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 4/12

7. Select Attach Selected Attributes to save your changes.
8. You should see your newly attached attributes in the Attributes column beside your selected
members.02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 5/12

Detach attributes
1. Log in to vena.io and select the Modeler tab.
2. Navigate to the Data Modeler page and select the data model where you want to manage
your attributes. 02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 6/12

3. Select the dimension where you want to manage the associated attributes.
4. Use the checkboxes next to the member names to select the members where you want to
detach attributes.
02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 7/12

5. Select the Actions menu and select Attach Attributes from the drop-down menu.
6. If you only have one attribute attached to your selected members, your confirmation
message will look like this. If you have more than one attribute attached to your members,
you will be prompted to select the attribute(s) you want to remove from a drop-down list.
7. Select Detach Selected Attributes to save your changes.
8. The page will automatically refresh to show that your selected attributes are no longer
attached to the selected members.02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 8/12

Filter by attributes
Filter by attribute lets you filter your hierarchy by a specific attribute and identifies all
members associated with a particular attribute. In the example below, we will be filtering using
the Drivers Maintenance | No Forecast attribute.
1. Log in to vena.io and select the Modeler tab.
2. Navigate to the Data Modeler page and select the data model where you want to filter your
attributes.
3. Select the Dimension that you want to search.
4. Select the filter icon (
) next to Attributes.
5. The menu will display all attributes attached to members in this particular dimension. Select
the attribute you want to filter. You can only filter one attribute at a time.
02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 9/12

6. Select Apply Selection to filter your members.
7. The page will refresh and display all members associated with the attribute you selected. At
the top of the table, you will see the number of results for this filtered search. You can
continue to filter by selecting another attribute from the attributes menu.
8. On this page, you can also bulk select any number of members from this filtered list and
detach the attribute. With bulk select, you can manage members and attributes if you want
to make quick changes or double-check that the correct members are attached to a given
attribute when troubleshooting data.
Notes & best practices
There is no limit to the number of attributes you can attach or detach to a particular
member. To add new attributes, follow the instructions in this article.
When using filter by attributes, you can only filter one attribute at a time.
Bulk attach/detach attribute actions aren’t available in the right-click context menu.02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 10/12

Was this article helpful?
1 out of 4 found this helpful
Related articles
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: Build and Manage Data Models in
Modeler
Reference: Writing Expressions (MQL & HQL)
How-To: Using Attribute Aggregation
How-To: Search for Members, Attributes,
Aliases and GL Codes With the Modeler
SearchRecently viewed articles
How-To: Bulk Updating Dimension or
Hierarchy Member Names
How-To: Restoring a Dimension Member That
Was Mistakenly Deleted
How-To: Combining Dimensions Using
Multiple Expressions for Slices to Clear
Explainer: What Is the Maximum Number of
Dimension Members and Member Name
Characters02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 11/12

How-To: Assigning Dimension Types and
Standard Members
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:06 How-To: Bulk Attach/Detach Attributes and Filter by Attributes – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728056717-How-To-Bulk-Attach-Detach-Attributes-and-Filter-by-Attributes 12/12
