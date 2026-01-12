# (How To)   Build Your Chart of Accounts Hierarchy in Quick Start

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Managing Your Model Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
Managing Your Model
Explainer: What is Data Model
Standardization?
How-To: Build Your Chart of
Accounts Hierarchy in QuickHow-To: Build Your Chart of Accounts
Hierarchy in Quick Start
Quick Start is a new, centralized tool that allows you to set up your data model faster
and speed up the time to get value out of Vena. In step four of Quick Start, you can
build your chart of accounts hierarchy.
This allows you to add members (GL account numbers), edit member names and
aliases (account descriptions) and assign range rules (define groupings of accounts).
Mia Shabsove
Updated 7 months ago
02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 1/20

Start
How-To: Formatting an Excel-
Based CSV to Maintain Leading
Zeros for ETL Jobs
How-To: Data Model Series
(Part 1): Creating a Data Model
How-To: Data Model Series
(Part 2): Hierarchies and Roll-
Ups
How-To: Data Model Series
(Part 3): Attributes and
Versioning
How-To: Data Model Series
(Part 4): ETL Tool
How-To: Build and Manage
Data Models in Modeler
How-To: Building Alternate
Hierarchies
How-To: Adjusting How Vena
Treats Zero Values in the
Database
How-To: Creating a Testing
Environment by Cloning a Data
Model (Clone & Remap)Why use this feature?
There are two existing ways you can build your account hierarchy in Vena: direct CSV upload or
manual creation through the Modeler interface. Direct CSV upload requires a specific Vena
format that can be time-consuming to transpose to, and manual through the Modeler can be a
slow process. For setting up your data model from scratch, there is now a better way. Using
Vena’s Quick Start Hierarchy Build, you can significantly reduce the effort and time needed to set
up your data model.
This article focuses on step four of Vena’s Quick Start feature and will teach you how to build
your chart of accounts hierarchy and provide examples of how this feature will help you start
using Vena faster.
Before you begin
To complete the steps outlined on this page, you will need at least Modeler access.
You will also need to complete the first three steps of Quick Start; uploading your GL transaction,
matching dimensions and customizing your transaction table.
Table of contents
How to02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 2/20

How-To: Undo a Versioning ETL
Job Without Line-Item Details
How-To: Undoing a Versioning
ETL job with Line-Item Details
(LIDs)
How-To: Downloading All Vena
Data From Your Tenant or
Environment
Troubleshooting: The Bulk Copy
Parameters Were Invalid
Troubleshooting: This Member
Does Not Exist Error During
Modeler Search
Troubleshooting: ETL Error –
Cannot Increase the Number of
Members Beyond 400000
Troubleshooting: Encountered
More Than the Limit of 1000
Unmapped Members
Functions
Calcs (Scripts)
Data Transformation &
Integration
AdminAdd a child or sibling member
Assign range rules to your standard hierarchy
Operating Expenses example
Operating Expenses example outcome
Notes & limitations
How to
Part 1: Add a child or sibling member
You’ll notice when you land on this step, there is already a default standard hierarchy in place
with top-level members as a starting point. Your goal is to expand on the starting structure and
create additional levels to reflect your company’s account hierarchy for reporting. At the lowest
level parent of a group, you’ll want to set a range rule to define which group of account ranges
roll up to that parent.
For example:
1. Select the
vertical ellipsis icon in the Actions column next to the Member Name you
would like to add a child or sibling member.02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 3/20

Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates2. Select Add Sibling or Add Child.
3. Enter the Member Name.
4. Enter a Start Range and an End Range for your new member.
Note
Adding a sibling will create another member at the same level of the member and
adding a child will create another level below the member. 02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 4/20

5. If you want to add another child or sibling member, select Add Another Member.
6. Once you’re finished adding members, select Save Item.
Part 2: Assign range rules to your standard hierarchy
1. Under the Set Range Rule column, select the
Pencil icon in the Set Range Rule column
next to the Member Name you would like to assign a range rule.
2. Enter the Start Range and End Range for your member.
For example, if you are entering a range rule for your Cash accounts. Enter the account
numbers that correspond to your Cash member. If your Cash includes accounts 1000-1099
the start range would be 1000 and the end range would be 1099.02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 5/20

3. Select the check mark to save the range rule.
Part 3: Delete a member
1. Select the
vertical ellipsis icon in the Actions column next to the Member Name you
would like to delete.
2. Select Delete Member.
3. If you’re sure you want to delete the member, select Delete.02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 6/20

Operating Expenses example
You'll notice when you land on this step, there is already a default standard hierarchy. Your goal
is to expand on the starting structure and create additional levels to reflect your company’s
account hierarchy for reporting. At the lowest level parent of a group, set a range rule to define
which group of accounts (members) the numbers/ranges will roll up to.
This is the starting point for the income statement:
You’ll notice it goes as far as Operating Expenses. This is where we can use the tool to expand
and build out the hierarchy custom to your business needs.
Let’s say one level down from Operating Expenses, we need to add these nine account groups
(members):
Salaries & Related Costs
Workers Compensation02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 7/20

Benefits & Related Costs
Interest Expense
Depreciation & Amortization
Lease on Facilities
Marketing Expense
Corporate Overhead
Other Admin Expenses
To do this, right-click Operating Expenses and select Add Child to add members a level below
it.
This will open a side drawer where you can begin to add the new members:02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 8/20

If the GL Account codes roll up to this level directly, you can begin assigning the Account ranges.
If there is another level to be created, add the members, Save Changes and return to the table
to continue. For this example, that is what we will do.
Once changes are saved, you can see the new members are created and added in the table,
nested under Operating Expenses as its children.02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 9/20

Now let’s go one more level below for Benefits & Related Costs.
Right-click Benefits & Related Costs and select Add Child. The side drawer opens again and
you can now add children to the Benefits & Related Costs member. We’ll proceed to add the
next level groups as follows:02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 10/20

02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 11/20

Now, this is the lowest-level parent for this account group (member). Under these four buckets
are the actual, numeric GL account codes. Since this is the case, we can define the range of
accounts that roll up to each new parent.
It should look something like this - of course, the actual account codes will be unique to your
Chart of Accounts. You may receive an error message if you make an invalid input - see Notes &
Limitations for more information. You will need to fix them before changes can be saved. For
example:02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 12/20

02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 13/20

Once changes are saved, you can see the next level of account groups created under Benefits &
Related Costs and the corresponding ranges set for each one.
02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 14/20

If you need to make any changes, you can select the Pencil icon to edit a specific member name
or range.
You will then need to repeat this process for all the other account groupings.
When the data load process runs in Vena, we will place those numeric GL Account codes under
the corresponding parent set by the account ranges in this step. In short, we will build out the
rest of your hierarchy for you after your first data load, putting all the loaded account members
in their defined position.
Operating Expenses example outcome
Once you complete Quick Start, you’ll land on the Data Model page. You can explore the
hierarchy you just built by expanding the levels. Per the example we just walked through, you’d
see:
The 9 children/subgroups created under Operating Expenses.
The 4 children/subgroups created under Benefits & Related Costs.
The actual, bottom-level GL account codes nested under the parent as defined in your
account Range Rules.
Note
Only create members for the lowest-level parent/account group (member). The
individual numerical GL account codes only need to be defined within the ranges. A
generally easy way to think about this is that we only need to create up to the "text"
based levels in the hierarchy table view. 02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 15/20

If you matched the account alias in the Match Dimensions step of Quick Start, you’d also
see that reflected here.
Any members that did not fit in a defined range, would be placed in an Unmapped folder.
You can bulk select, drag and drop those members into their position.
Members and aliases can be edited in this table view.
02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 16/20

To edit your account ranges, select Manage > Ranges.
Notes & limitations
End ranges must be greater than start ranges. For example, if your start range is 1499, the
end range must be 1500 or higher.
Ranges cannot overlap. For example, the start range for your Cash account is 1000 and the
end range is 1499. When adding Accounts Receivable as the next child member, it cannot
have a start range of 1499. The start range cannot overlap with the Cash account.
Decimals are permitted for numeric ranges.
Character limit for the range input field is 15.
You cannot create two members with the same name.
Member names and ranges cannot contain invalid characters, only alphanumeric characters
are allowed.
A start or end range cannot be left blank, both must be entered to save your member.02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 17/20

Set ranges do not move existing bottom-level members in your model. This occurs as part of
the data load step. Once ranges are set, net new members that are uploaded will be placed
according to the ranges, or under Unmapped.
Have feedback for us?
Let us know how we can improve through the Feedback button located at the bottom-left side
of the Modeler navigation panel.
Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 18/20

Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Data Model Series (Part 1): Creating a
Data Model
How-To: Data Model Series (Part 2):
Hierarchies and Roll-Ups
Explainer: What is Data Model
Standardization?
How-To: Building Alternate Hierarchies
Reference: ETL Guide - 3 - Command Line ETLRecently viewed articles
Explainer: What is Data Model
Standardization?
Troubleshooting: Versioning Copy To and
Copy From Must Be Bottom-Level Members
Troubleshooting: Versioning Copy To and
Copy From must Contain the Same Set of
Dimensions
Troubleshooting: Error While Processing the
Model Slice Expression When Previewing
Intersections
Reference: Export Intersections and Line-Item
Details02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 19/20

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:14 How-To: Build Your Chart of Accounts Hierarchy in Quick Start – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15220805304717-How-To-Build-Your-Chart-of-Accounts-Hierarchy-in-Quick-Start 20/20
