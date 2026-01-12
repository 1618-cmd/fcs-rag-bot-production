# (Reference)   Writing Expressions (MQL & HQL)

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Data Querying Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Calcs (Scripts)
Data Transformation &
Integration
ETL JobsReference: Writing Expressions (MQL
& HQL)
Learn how to create expressions in the MQL and HQL languages.
Overview
Vena Support Team
Updated 1 month ago
02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 1/24

Data Querying
How-To: Using the Query Agent
to Build MQL Expressions (Beta)
Reference: Writing Expressions
(MQL & HQL)
Reference: Using Wildcard in
Model Slice Expression
Troubleshooting: ETL Export
MQL Query Returning No Data
How-To: Creating Advanced
Integration Setups With VenaQL
Troubleshooting: MQL Invalid
Expression Syntax When
Creating a Calculated Member
Troubleshooting: ETL Error
Guide
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
QuickBooks IntegrationWhen working with certain Vena features (such as the ETL tool and the Expression Editor), you
may wish to narrow down the information in your database.
Choose to specify certain groups of intersections, Line-Item Details (LIDs), hierarchy members or
attributes using expressions. Expressions are like search queries that use a certain language to
return specific results from a database.
In Vena, these are called Model Slice Query Language (MQL) and Hibernate Query Language
(HQL). With them, you can define the data you want (or don’t want) returned to you, as broadly
or narrowly as you need.
This reference guide covers how and when to use MQL and HQL to build these expressions.
Info
Need help writing your MQL expression? Use Vena's Query Agent to generate
expressions in plain language with the help of AI. Simply write a prompt and Query
Agent will generate an MQL expression that references members in your data models
that is ready to be pasted wherever you need it.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 2/24

Power Automate
Integration
Power BI Integration
Sage Intacct Integration
Salesforce Integration
Troubleshooting Data
Transformation
How-to: Vena Integration: Part 1 -
Feature Overview
How-to: Vena Integration: Part 2
– Internal Sources
How-to: Vena Integration: Part 3
– External Sources – Data Feeds
& Connections
How-to: Vena Integration: Part 4
– Import and Export API
How-to: Vena Integration: Part 5 -
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
Table of contents
Choosing a Language
Where to Input Languages
Model Slice Query Language (MQL)
Overall Structure
Query Agent is now in beta and available in the Modeler > Export tab.
02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 3/24

How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesComponents
Functions
Operators
Examples
Hibernate Query Language (HQL)
Overall Structure
Components
Classes
Properties
Values
Operators
Examples
Choosing a language
Choose whether to use MQL or HQL based on the data you’re querying:
MQL: Intersections, LIDs, Hierarchy (incl. exports)
HQL: Attributes and Hierarchy (incl. exports)02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 4/24

Where to input languages
Both MQL and HQL expressions are entered in one of two ways:
1. Into a provided Query field within Vena (see below list).
2. By utilizing the --exportQuery (MQL) or --exportWhere (HQL) clauses when using Command Line
ETL.
In Vena, expressions are used in:
ETL Tool (Export)
Command Line ETL
Calculated Members
Expression Editor in Vena Desktop
Note
Historically, only HQL could be used for hierarchy exports. To simplify
expression writing in Vena, we expanded support for MQL to also include
this data type.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 5/24

Model Slice Query Language (MQL)
Overall Structure

The general structure of an MQL expression is:
dimension("Dimension Name": Member Expression)
Here is a simple example of a MQL expression:
dimension('Scenario': 'Budget') dimension('Year': 'Y2025')
This expression will return Budget data from the Scenario dimension and the Y2025 data from
the Year dimension, plus all members from every other dimension (see the fifth point in the
below list).
When writing MQL expressions, remember:
Expressions are NOT case-sensitive.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 6/24

A colon (:) separates the dimension name from member names, attributes, functions and
operators (collectively called the member expression).
Multiple components with an expression are separated by whitespace, which is inserted with
the spacebar on your keyboard.
Multiple dimension expressions are also separated by a whitespace, as in our above example.
Only write the dimensions from which you want (or don’t want) specific members; there is no
need to write every dimension in an expression. If a subset of a dimension is not specified, all
members of that dimension are included in your data return.
Calculated Members are created under a specified dimension. Therefore, when creating an
expression for a Calculated Member, you do not need to specify the dimension name as part
of the expression and can simply input the member expression portion.
Components
Five components may make up an MQL expression. Consider this example:
Component
NameUse Format02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 7/24

A - 'Account' DimensionDefines a dimension.Enclosed in a single (') or
double (") quotation marks
and followed by a colon (:).
B -subtract Operator Keywords to perform
operations on
combinations of
members, attributes
and functions.Placed before a list of
members, attributes, or
functions enclosed in
parentheses.
C - bottomlevel Function Keywords used to
specify dynamic
grouping of members.Placed before a member
enclosed in parentheses.
D - 'Net Income' Member Defines a member. Enclosed in single (') or
double (") quotation marks.
E -
attribute(@'Static
accounts')Attribute Defines an attribute.Enclosed in single (') or
double (") quotation marks
preceded by the word
attribute and the @ symbol.
Let's look at the available options for Functions and Operators.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 8/24

Functions
Functions define groupings of members in relation to a given member. The following functions
are available:
Function Action
children Returns the children of a member.
ichildren Returns the member and then its children.
descendantsReturns the descendants of the member with parents before their children.
idescendantsReturns the member and then the descendants of the member with parents
before their children.
bottomlevelReturns the bottom-level members under the member.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 9/24

ancestorsReturns the ancestors of the member.
iancestorsReturns the member itself and then the ancestors of the member.
parents Returns the parents of the member.
Operators
Operators allow you to specify sets of members, attributes, functions or even whole expressions.
The following operators are available:
OperatorFunction Syntax Example Return
unionReturns a
combination
of two sets.union(A B C
...)
A, B, C, etc.
can beunion('5001' '5003' ) Data belonging to
5001 plus data
belonging to 5003
members.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 10/24

members,
attributes,
functions or
expressions.
intersectionReturns a
set of the
elements
that belong
to both sets.intersection(A
B C ...)
A, B, C, etc.
can be
members,
attributes,
functions or
expressions.intersection(children('Net
Income')
children('Revenue' ))Data belonging to
members that are
within bothNet
IncomeandRevenue.
subtractReturns the
first set
after the
second set
has been
removed
from it.subtract(A B)
A and B can
be members,
attributes,
functions or
expressions.subtract(children('Cost of
Revenue') 'Taxes')Data belonging to
members of Cost of
Revenue, except
data belonging to
the Taxes member.
not Returns a
subset of
the
dimension
that does
not follow anot(condition)
The condition
can be a
member,
attribute ornot(children('Balance
Sheet')All data belonging to
members of the
Widgets dimension,
except data
belonging to02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 11/24

certain
condition.function. members of Balance
Sheet.
Examples
Example 1: Combined individual members
dimension('Account': union('5001' '5003'))
Return:
Within the Account dimension, the member 5001 plus the member 5003.
The members of all other dimensions.
This example demonstrates how to pull specific member datasets from one dimension using
the union operator.
Example 2: Combined Bottom Levels, two dimensions with exclusion02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 12/24

 
 dimension('Account': union(bottomlevel('Assets') bottomlevel('Liabilities'))) dimension('Peri
Return:
Within the Account dimension, all members at the bottom level of Assets plus all members at
the bottom level of Liabilities.
All members of the Period dimension except children of Q1 as well as the member itself.
The members of all other dimensions.
This example shows how different criteria may be used on different dimensions.
Example 3: Intersection with an exclusion
dimension('Account': intersection(descendants('Net Income') not(children('Cost of Revenue')))
Return:
Within the Account dimension, all members that are descendants of Net Income, except for
children of Cost of Revenue.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 13/24

The members of all other dimensions.
This example illustrates how the intersection operator can be used as a filter to include all
members under a given parent except the children of one of its children. The same could also be
achieved with the union and not operators.
Hibernate Query Language (HQL)
Overall Structure
The general structure of an expression is:
class.property = value
Here is a simple example of an HQL expression:
dimension.name = ‘Year’
When writing HQL expressions, remember:
Expressions ARE case-sensitive, including the values being queried.
HQL expressions written in Vena completes an overall query; what you write forms the
WHERE part of the query. Therefore, you need only to enter the class, property, value(s) and
operators (if needed). 02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 14/24

The value entered may be a name (dimension, member, attribute, etc.) or a number.
String together multiple values or class.property combinations with operators. For example:
dimension.name = 'Year' AND NOT _member.name = 2025

Components
Four components may make up an HQL expression. Consider this example:
A = Class
B = Property
C = Value
D = Operator
Each component has various options available, which are outlined below.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 15/24

Classes
Classes and properties are always used together, separated by a period.
Class Properties Example Return
_member name
alias
numPositions
numChildren
memberKind
expression_member.name = 2025All members whose
name matches 2025
exactly, including shared
members.
dimension namedimension.name = 'Year'All members belonging
to the dimension Year.
position operator
parentMemberId
previousMemberIdposition.operator = 1All members whose
operator in the Data
Model is +.
attribute name
attribute.name = 'Blue'Depending on the data
type, returns either:
Members with the
attribute Blue
(Hierarchy), or02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 16/24

Attributes with the
name Blue
(Attributes)
Properties
Property Function Notes
_member.name Identifies members by name. Values are case-sensitive.
_member.alias Identifies members by alias. Values are case-sensitive.
_member.numPositionsIdentifies shared members
(those appearing more than
once in the hierarchy under
different parents).Requires a numeric value, as
Positions refers to the number
of times a member appears in
different places.
For example,
_member.numPositions > 1
returns all shared members in
the database.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 17/24

_member.numChildrenIdentifies members with a
given number of children.Requires a numeric value.
_member.id Identifies members by their
member ID.Shared members also share a
member ID.
_member.expression Identifies calculated
members.Used to return pre-determined
calculated members with
_member.expression IS NOT
NULL.
For help creating calculated
members, visit this article.
dimension.name Identifies dimension by
name, returning all members
in that dimension.Values are case-sensitive.
position.operator Identifies members based on
their operator.Numeric; only accepts the
values 1, 0, -1:
1 is for the + operator.
0 is for the ~ operator.
-1 is for the - operator02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 18/24

position.parentMemberIdIdentifies children of a
member based on the
member ID.Can be used to identify a
specific instance of a shared
member with _member.name =
'SharedMember' AND
position.parentMemberId = '[ID of
desired parent]'
position.previousMemberIdIdentifies members 'below' a
member based on the 'top'
member's ID (i.e., members
listed below a member in the
hierarchy view of the
Modeler).Works like parentMemberId.
Both parentMemberId and
previousMemberId return a list of
children of a specific member.
attribute.name Identifies members by
attribute, or attributes by
name.Works differently depending on
whether the data type is
hierarchy (all members with the
attribute) or attribute (a list of
matching attribute names).Values
Values can either be alphabetic or numeric and are separated from the class.property
combination by an operator (see below). Alphabetic values must be enclosed within quotation
marks, while numeric values do not:
_member.name = 'Feb'
_member.numChildren = 5
Operators02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 19/24

Vena supports the standard HQL WHERE clause operators:
Operator Function Example Return
= Equal_member.numChildren = 5Members with
exactly 5
children.
<> Not equal_member.numChildren <> 5Members with
any number of
children except
5.
> Greater than_member.numChildren > 5Members with 6
children or
more.
< Less than_member.numChildren < 5Members with 4
children or
fewer.
>= Greater than or
equal_member.numChildren >= 5Members with 5
children or
more.
<= Less than or equal_member.numChildren <= 5Members with 5
children or
fewer.02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 20/24

BETWEENWithin an inclusive
range (with AND)_member.numChildren BETWEEN 1 AND 3Members with 1,
2 or 3 children.
LIKE Works like = (see
note)_member.alias LIKE 'Account'Members whose
alias matches
Account exactly.
IN Specify multiple
values (in
parentheses)_member.name IN ('Jan', 'Feb', 'Mar')Members whose
name matches
Jan, Feb, or Mar
exactly.
 Note
Usually, you would use the LIKE operator in conjunction with a wildcard ( _ or %) to find
results matching a given pattern.
For example,
_member.alias LIKE 'The %'
This expression should return members which have an alias beginning with The, like
The Original Keyboard or The Keyboard 2.0. However, as Vena does not support
wildcards in HQL, the LIKE operator in effect functions identically to the = operator02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 21/24

and only returns exact matches. In the example above, only members whose actual
alias is The would be returned.
The WHERE clause can also be combined with logical operators:
OperatorFunction Example Return
ANDReturns
results if
all
conditions
separated
by AND are
true._member.numChildren = 5 AND attribute.name = 'Blue'Members
with
exactly 5
children
and
possess
the Blue
attribute.
ORReturns
results if
any of the
conditions
separated
by OR are
true._member.numChildren = 5 OR attribute.name = 'Blue'Members
with either
exactly 5
children or
possess
the Blue
attribute.
NOTReturns
results if
the
condition
following_member.numChildren = 5 NOT attribute.name = 'Blue'Members
with
exactly 5
children,
and do
not also02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 22/24

NOT is not
true.possess
the Blue
attribute.
Examples
In the vast majority of cases, hierarchy exports will consist of the entire dimension. For example,
dimension.name = 'Account'
For examples of how this may be narrowed down in specific cases, please refer to the tables
above.
Was this article helpful?
14 out of 26 found this helpful
Related articles
Reference: Vena Calcs - 1 - Managing Scripts
Reference: ETL Guide - 3 - Command Line ETLRecently viewed articles
How-To: Using the Query Agent to Build MQL
Expressions (Beta)
How-To: Checking the ETL Tool Version02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 23/24

How-To: Visualizing Data in the Power BI
Connector on Desktop by Creating a Rollup
Value Measure
How-To: Mapping Data From Multiple Data
Models on a Single Template (Vena Desktop
Only)
How-To: Set Up a Business Central Connector
and Data FeedHow-To: Setting up Email Notifications for ETL
Jobs
How-To: Maintaining Dimension Member IDs
When Updating Existing Members
How-To: Use Clear Slices to Clear Intersections
During an ETL Load
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:49 Reference: Writing Expressions (MQL & HQL) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/212073046-Reference-Writing-Expressions-MQL-HQL 24/24
