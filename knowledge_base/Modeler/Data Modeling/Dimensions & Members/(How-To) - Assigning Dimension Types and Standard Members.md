# (How To)   Assigning Dimension Types and Standard Members

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
Member Name CharactersHow-To: Assigning Dimension Types
and Standard Members
Leverage Dimension Types and Standard Membersto unlock further capabilities
with your data models.
Video
Check out a video of this article's content.
Mia Shabsove
Updated 1 month ago
02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 1/19

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
Members?Assigning Dimension Types & Standard Members Assigning Dimension Types & Standard Members
Why use this feature?
Assign Dimension Types and Standard Members in your data models to add context and more
efficiently leverage exciting new features. By implementing Dimension Types and Standard
Members, you can unlock further capabilities such as FX Functions, Insights, Template Studio,
Vena Copilot and more.
Dimension Types and Standard Members integrate a Vena standard definition for members and
dimensions in your data model. For example, you might name your Net Income member NI,02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 2/19

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
See all 21 articlesRevenue member Sales or Account dimension GL Accounts. We continue to offer this flexibility in
naming conventions and now, with this additional layer of standardization in our product, we
can offer exciting new features at scale with minimal model configuration from customers.
Using Dimension Types and Standard Members ensures that regardless of whether your Income
Statement member is called “Income Statement” or “IS” if assigned the Standard Member
Income Statement, Vena understands the purpose of that member and can seamlessly integrate
your data model when expanding your solution to Vena Insights, FX Functions etc.
Dimension Types that you can use
This is the current list of available Dimension Types that can be assigned. Additional Dimension
Types will become available as we explore additional use cases.
Dimension
TypeDefinition Related Dimension
Name Examples
Account   A dimension whose members represent a chart of
   accounts for financial reporting purposes. Account, Accounts,
 GL Account
Entity   A dimension whose members represent
   organizational information, such as subsidiaries. Entity, Company,
 Entities, Legal Entity,
 Organization
Department   A dimension whose members represent
   organizational functions. Department,
 Departments
Year    A dimension whose members represent time in
   years. Year, Years,
 Fiscal Year02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 3/19

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
Product UpdatesMonth   A dimension whose members represent time
   periods, such as quarters, halves, months. Period, Periods, Month
Scenario A dimension whose members represent planning or
 strategic analysis information - a categorization of a
 value. Scenario, Scenarios
Currency A dimension whose members represent currency
 information. Currency, Currencies
MeasureA dimension whose members represent the
defining characteristic of an intersection - value,
comment, adjustment. Measure, Measures
Custom A dimension whose members does not fit
 an existing Vena Dimension Type and is considered
"custom". Employee, Data
Source,   Asset, Class,
Item,   Subsidiary,
Category
Geography A dimension whose members represent geographic
 information.  Location, Region,
 Geography, State,
Branch
Project A dimension whose members represent project
identification   information.  Project, Project Type,
Project   Code
Customer A dimension whose members represent customer or
contact   information.  Customer, Customer
Type,   Opportunity
Product A dimension whose members represent product
information.  Product, Product Line,
 Product Family,
Product   Category
Vendor A dimension whose members represent vendor or
contact   information.  Vendor, Vendors02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 4/19

Standard Members that you can use
This is the current list of available Standard Members that can be assigned for each Dimension
Type. Additional Standard Members may become available as we explore additional use cases.
The list is comprised of common financial members that are most relevant for each Dimension
Type. These are expected to be very common if you are using Vena for financial planning and
reporting.
Dimension Type Standard Members
Account Accounts Payable
Accounts Receivable
Assets
Balance Sheet
Benefits
Cash
Costs Of Goods Sold
Current Assets
Current Liabilities
Deferred Revenue
EBIT
Equity
Fixed Assets
Gross Margin
Headcount
Liabilities
Long Term Debt
Long Term Liabilities
Net Income
Non-Current Assets
Operating Expenses
Other Accounts  02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 5/19

Prepaid Expenses
Revenue
Retained Earnings
Salaries
Undefined
Entity All Entities
Undefined
Department All Departments
Undefined
Year All Years
2021
2022
2023
2024
2025
2026
2027
2028
Undefined
Month YTDs
QTDs
Full Year
Opening Balance
January
February
March
April  02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 6/19

May
June  July
August
September
October
November
December
Q1
Q2
Q3
Q4
H1
H2
Undefined
Scenario Actual
Plan
Undefined
All Scenarios
Currency Local
All Reporting Currencies
Undefined
All Currencies
Measure Total Value
Value
Undefined
Other Measures
Geography  All Geographies
Undefined 02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 7/19

Project All Projects
Undefined
Customer All Customers
Undefined
Product All Products
Undefined
Vendor All Vendors
Undefined
Before you begin
To follow the instructions in this guide, you will need at least Modeler access. You will also need
appropriate data permissions for the data model.
Table of contents
How to
Adding or editing a Dimension Type
Removing a Dimension Type
Assigning a Standard Member
Unassigning a Standard Member
Notes & limitations 02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 8/19

How to

Adding or editing a Dimension Type

1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select the pencil (
) icon to edit your members. This opens the Dimensions drawer.
4. Select the pencil (
) icon next to the dimension associated with the Dimension Type you
want to edit.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 9/19

5. Select theDimension Type you want to assign from the drop-down menu.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 10/19

02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 11/19

6. Select the checkmark ( ✔)iconto confirm your selection.
7. Select Done to close the drawer.
Note
After assigning Dimension Types, assign your Standard Members by following the steps
below.
Removing a Dimension Type
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select the pencil (
) icon to edit your members. This opens the Dimensions drawer.
4. Select the pencil (
) icon next to the dimension you want to edit the Dimension Type of.
5. Select Customfrom the drop-down menu.
6. Select the checkmark ( ✔)iconto confirm your selection.
7. Select Done to close the drawer.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 12/19

Assigning a Standard Member
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select the pencil icon next to the dimension you want to edit the Standard Members for.
This opens the Manage Model  drawer.
4. Select Standar d Member s.
Note
Before assigning Standard Members, you must assign Dimension Types to your
model. Standard Members will become available for each corresponding
Dimension Type in your model.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 13/19

02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 14/19

5. Select a dimension to assign Standard Members in the drop-down menu.
6. Select the pencil (
)icon next to the Standard Vena Member and select the corresponding
member from the drop-down menu. You can use the search function or scroll through the list
to find members.
7. Select the checkmark ( ✔)iconto confirm your selection.
8. Select Done to close the drawer.
Note
You will only see dimensions in this drop-down that you have assigned a
Dimension Type. 02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 15/19

Unassigning Standard Members
1. Navigate to the Modeler tab.
2. Navigate to the appropriate data model.
3. Select the pencil icon next to the dimension you want to edit the Standard Members for.
This opens the Manage Model  drawer.
4. Select the pencil (
) icon next to the Standard Member you want to unassign.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 16/19

5. Select Unassign Memberfrom the drop-down menu.
6. Select the checkmark ( ✔)iconto confirm your selection.
7. Select Done to close the drawer.
Notes & limitations
There are 14 Dimension Types that you can use: Account, Entity, Department, Year, Period,
Scenario, Measure, Currency, Custom, Geography, Project, Customer, Product and Vendor.
More Dimension Types are expected to be added in the future to support expanding use
cases.
Custom is the only Dimension Type that can be tagged more than once in the same model.02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 17/19

When creating new models from scratch, you can now add new dimensions with pre-defined
Dimension Types from the dropdown list in addition to the standard custom dimensions.
Dimension Types are retained in every model where a dimension is linked.
Dimension Types must be assigned before assigning Standard Members.
You are not required to assign all Standard Members – we highly encourage customers to
assign as many as are relevant or in use in your data models.
A member from your hierarchy can only be assigned to one Standard Member.
Expression Σ  (or Calculated) members cannot be assigned to a Standard Member.
If a Dimension Type is unassigned or if a dimension is deleted that had Standard Members
assigned, those Standard Members will also be deleted.
Was this article helpful?
2 out of 4 found this helpful
Related articles
How-To: Creating an AI Model
Explainer: What is Data Model
Standardization?
Explainer: What Are Linked Dimensions?Recently viewed articles
Reference: Modeler Experience
Troubleshooting: Exit Edit Mode and Retry
When Saving
Troubleshooting: Data Save Failed Most Likely
Because of an Expired Session Error02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 18/19

How-To: Building Alternate Hierarchies
How-To: Using Vena CopilotTroubleshooting: Save Data Is Unavailable
Until a Successful Refresh Is Completed
Troubleshooting: The Remote Server
Returned (500) Internal Server Error When
Saving Data
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:04 How-To: Assigning Dimension Types and Standard Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/20299565240845-How-To-Assigning-Dimension-Types-and-Standard-Members 19/19
