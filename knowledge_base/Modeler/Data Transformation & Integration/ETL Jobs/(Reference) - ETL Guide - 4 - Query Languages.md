# (Reference)   ETL Guide   4   Query Languages

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs Search
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
ETL JobsReference: ETL Guide - 4 - Query
Languages
Part 1:Overview
Part 2:Vena.io ETL
Part 3:Command Line - ETL
Part 4:Query Languages  -You are here
Vena Support Team
Updated 7 months ago
02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 1/10

ETL Job Errors &
Troubleshooting
Reference: ETL Guide - 1 -
Overview
Reference: ETL Guide - 2 -
Vena.io ETL
Reference: ETL Guide - 3 -
Command Line ETL
Reference: ETL Guide - 4 -
Query Languages
Reference: ETL Guide - 5 - SQL
Staging Environment
Reference: ETL Guide - 6- Using
Staging Data
How-To: Exporting Data From a
SQL Staging Table
How-To: Create and Manage a
Data Model Hierarchy Using
ETL Import
How-To: Exporting a Subset of
Data From Your Data Model or
Cube
Reference: Additional Security
Restrictions to the SQL WHEREPart 5:SQL Staging Environment
Part 6:Using Staging Data
Table of contents
Chapter 4: Query Languages
Hibernate Query Language
Model Slice Query Language
Chapter 4: Query Languages
Both the vena.io and cmd interfaces allow the use of query expressions to filter the exported or
imported data. The specific syntax of these expressions depends on the type of import or
export:
For hierarchy and attribute operations, the Hibernate Query Language (HQL) is used.
For intersection and LID operations, the Model Slice Query Language (MQL) is used.
Regardless of the type of data being exported/imported, the query is supplied in the provided
"Query" field on vena.io or by applying the--exportQuery clause on the command line.
For more information on MQL and HQL, read the Writing Expressions (MQL & HQL) article.02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 2/10

Clause
Explainer: ETL Export Feature
Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Using
Command-Line ETL
How-To: Automatically Run ETL
Templates Using the ETL
Scheduler
How-To: Checking if My File Has
a Header Row or Not
How-To: Exporting CSV Files for
ETL Job
How-To: Use Clear Slices to
Clear Intersections During an
ETL Load
How-To: Maintaining
Dimension Member IDs When
Updating Existing Members
How-To: Setting up Email
Notifications for ETL Jobs
How-To: Checking the ETL Tool
Version
Data QueryingHibernate Query Language
The Hibernate Query Language is designed for selecting members or attributes from a given
hierarchy. It is based on SQL and the syntax is very similar to SQL. The supplied query will be
used as in the WHERE clause of a SQL query.
For instance, the following HQL query, in a hierarchy export, would return all positions of all
members named 2010.
_member.name =  '2010'
Likewise, the following query in a hierarchy export would return all members whose aliases
begin with "the".
_member. alias LIKE 'The %'
Identifiers can be one of _member, dimension, position, or attribute.
Each of these have the following properties which can be queried:
_member:
name
alias
numPositions
numChildren
dimension:
name02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 3/10

Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
QuickBooks Integration
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
& Connectionsposition:
operator (1 for +, 0 for ~, -1 for -)
attribute:
name
Model Slice Query Language
The Model Slice Query Language allows you to write expressions that represent a slice of the
cube. These expressions can be used to define Calculated Members, or in data operations like
exporting or deleting values. A model slice expression is composed of one or more dimension
expressions, where each dimension expression defines a subset of that dimension's members.
The members can be named directly in the expression, or they can be referred to with hierarchy
or attribute operators. The syntax is not case-sensitive. Below is a breakdown of these
components and examples of how to put together an expression.
Consider the following hierarchy:
Dimension: Food
  Member: Fruit
Member: Citrus
          Member: Oranges
  Member: Navel Orange02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 4/10

How-to: Vena Integration: Part 4
– Import and Export API
How-to: Vena Integration: Part 5 -
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates    Member: Blood Orange
  Member: Lemons
      Member: Non Citrus
  Member: Apples
  Member: Granny Smith Apple  (Attributes: Green)
  Member: Mcintosh Apple      (Attributes: Red)
Member: Vegetable
    Member: Carrots
Member: Celery
Much like Excel, Member Expressions are written like Excel Functions, with a general form of:
operator (<parameter 1> <parameter 2> ...). A Model Slice Query consists of a list of dimension
expressions separated by whitespace. Each dimension expression looks like this:
dimension ("<dimension name>" : <member expression> )
For instance, to refer to the member "Carrots" in the hierarchy given above, we would write
dimension("Food": "Carrots").
In some contexts, such as when defining a Calculated Member, the dimension is implied, and
only the member expression is needed. A member expression can consist of Members,
Attributes, Functions and Operators.
A member is defined by its name enclosed in single or double quotations. E.g.,'Navel Orange'02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 5/10

An attribute is defined by its name enclosed in single or double quotations preceded by
attribute and an @ character. E.g.,: attribute(@'Red')
An operator can be performed on combinations of members, attributes and functions. The
following list describes the chief expression operators and their syntax.
OperatorReturns Syntax Example Example
Return
Union Returns a
combination
of two sets.union(A B),
where A and B
can be
members,
attributes,
functions, or
expressions.union('Granny Smith Apple'
'Navel Orange')The data
comprised of
the Granny
Smith Apple +
Navel Orange
members.
IntersectionReturns a set
of the
elements
that belong
to both sets. intersection(A
B), where A and
B can be
members,
attributes,
functions, or
expressions.intersection(children('Fruits')
children('Citrus'))The data
comprised of
the members
that are both
Fruits and
Citrus.02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 6/10

SubtractReturns the
first set after
the second
set has been
removed
from it. subtract(A B),
where A and B
can be
members,
attributes,
functions, or
expressions.subtract(children('Fruits')
'Navel Orange')The data
comprised of
the members
under Fruits
omitting the
Navel Orange
member.
Not Returns a
subset of the
dimension
that does
not follow a
certain
condition.
This
condition
can be a
member,
attribute, or
function.not(condition)not(children('Vegetable')The data
comprised of
the members
of Food that
are not
Vegetables.
Here is a full list of all the functions that can be used in a member expression:
Children
IChildren
Descendants02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 7/10

IDescendants
BottomLevel
Ancestors
IAncestors
Parents
Ascendants
Additionally, we can reference members by attribute. For instance, the following expression
would return all fruit which do not have the red attribute:
dimension('Food': intersection( children ('Fruit') not( attribute (@'red'))))
Was this article helpful?
1 out of 2 found this helpful
Related articles Recently viewed articles02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 8/10

Reference: ETL Guide - 5 - SQL Staging
Environment
Reference: ETL Guide - 3 - Command Line ETL
Reference: ETL Guide - 6- Using Staging Data
Reference: Vena Calcs - 5 - Functions
How-To: Use Clear Slices to Clear
Intersections During an ETL LoadReference: ETL Guide - 3 - Command Line ETL
Reference: ETL Guide - 2 - Vena.io ETL
Reference: ETL Guide - 1 - Overview
Troubleshooting: No Values Generate for a
Reporting Currency
Troubleshooting: Calc Script Using
.BottomLevel() and .Exclude() in a Tuple Not
Working Properly
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 16:42 Reference: ETL Guide - 4 - Query Languages – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360028321091-Reference-ETL-Guide-4-Query-Languages 10/10
