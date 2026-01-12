# (Reference)   Vena Calcs   3   Data Types

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Calcs (Scripts) Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Calcs (Scripts)
Explainer: Target Member
Attribute Calc Trigger
Reference: Sparse CalcsReference: Vena Calcs - 3 - Data Types

About this series
This series is about how to write and use Vena Calculation Scripts. You are on Part 3, which
provides a description of various Calc Scripts data types.
Vena Support Team
Updated 6 months ago
02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 1/6

Reference: Vena Calcs - 1 -
Managing Scripts
Reference: Vena Calcs - 2 -
Notation and Syntax
Reference: Vena Calcs - 3 - Data
Types
Reference: Vena Calcs - 4 -
Operators
Reference: Vena Calcs - 5 -
Functions
Reference: Vena Calcs - 6 -
Conditional Statements
Reference: Vena Calcs - 7 -
Currency Conversions
Reference: Vena Calcs - 8 -
Examples
Reference: Vena Calcs - 9 -
Troubleshooting
Troubleshoot: Calc Target
Contains Data Even Though It
Shouldn’t
Troubleshooting: Calc Conversion
Not Working or Zero Values
AppearingVena Calculations Scripts (or Vena Calcs) is a scripting language designed for Vena data models.
Vena Calcs provides a powerful and flexible way to run calculations and simulations for business
rules at the database level for all dimensions and members.
You can apply calcs for a variety of uses, including calculating financial ratios and percentages,
departmental/employee allocations or FX currency conversions.
We've broken down Vena Calcs into nine articles. They can be read consecutively or browsed as
needed.
Part 1: Managing Scripts
Part 2: Notation and Syntax
Part 3: Data Types - You are here
Part 4: Operators
Part 5:Functions
Part 6:Conditional Statements
Part 7: Currency Conversions
Part 8:Examples
Part 9:Troubleshooting02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 2/6

Troubleshooting: Calc Is Not
Triggering or Calculating After
Data Load or Import
Troubleshooting: Calc Script
Using .BottomLevel() and
.Exclude() in a Tuple Not Working
Properly
Troubleshooting: No Values
Generate for a Reporting
Currency
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesTable of contents
Data Types
Dedicated Type Table
Data Types
Various data types are used in Vena Calcs for intersection value assignment, function/expression
return values and conditional statements.
Dedicated Type Table
Type Example Description
Bool true, false Boolean value
Current
Member[Year._] A special notation of a member,
returning the current Member String
for that dimension
Global
Variable&CurrentYear, [&CurrentYear]A variable returning the Member string
or Member in the corresponding
metadata variable02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 3/6

Type Example Description
Member String'2010' A sequence of characters representing
a member name, wrapped in single
quotes
Member [Sales], [Jan], [USD, Rate] A name of a data model member
Member Set{Sales, Jan, Feb, Mar,
[Rates].Leaves()}A set of members representing their
cross product
Number 1234 An arbitrary size number precise to 16
decimal places
String "abcd" A sequence of characters wrapped in
double quotes
Tuple (Sales, Jan, [USD, Rate]) An intersection of a sequence of
members
Tuple Set [Sales].YTD() A set of tuples returned from the cube02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 4/6

Was this article helpful?
2 out of 2 found this helpful
Related articles
Reference: Vena Calcs - 4 - Operators
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 8 - ExamplesRecently viewed articles
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Sparse Calcs
Explainer: Target Member Attribute Calc
Trigger
How-To: Using Vena’s Foreign Exchange (FX)
Conversion Function
Didn't find what you're looking for?02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 14:24 Reference: Vena Calcs - 3 - Data Types – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027593532-Reference-Vena-Calcs-3-Data-Types 6/6
