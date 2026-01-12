# (Reference)   Vena Calcs   6   Conditional Statements

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
Reference: Sparse CalcsReference: Vena Calcs - 6 - Conditional
Statements
About this series
This series is about how to write and use Vena Calculation Scripts. You are on Part 6, which
provides an overview of conditional statements.
Vena Support Team
Updated 1 year ago
02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 1/6

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
Part 3:Data Types
Part 4: Operators
Part 5:Functions
Part 6: Conditional Statements - You are here
Part 7: Currency Conversions
Part 8:Examples
Part 9:Troubleshooting
 02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 2/6

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
Product UpdatesConditional Statements
A statement that starts with “If” (If statements)s is the primary conditional statement.
An If statement:
Requires a boolean expression as its conditional test and may optionally be followed by one
or more ElseIf statements.
Is terminated by an End statement.
Performs conditional tests within a formula. Using the IF statement, you can define a boolean
test, as well as formulas to be calculated if the test returns either a TRUE or FALSE value.
An ELSEIF statement:
Defines a conditional test and conditions that are performed if the preceding IF test
generates a value of FALSE. For this reason, multiple ELSEIF commands are allowed following
a single IF.
Example 1:
If ( [Measure.Sales] > 100 )
    // do something02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 3/6

ElseIf ( [Measure.Sales] > 10 )
    // do something else
Else
    // do some third thing
End
Example 2:
If (( [Measure.Sales] > 100 ) && ( [Measure.Sales] < 200 ))
    // do something
ElseIf (( [Measure.Sales] > 201 ) && ( [Measure.Sales] < 300 ))
    // do something else
Else
    // do some third thing
End
The parenthesis around boolean expressions for If and ElseIf statements are always required.02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 4/6

Was this article helpful?
5 out of 12 found this helpful
Related articles
Reference: Vena Calcs - 8 - Examples
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 7 - Currency
Conversions
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 4 - OperatorsRecently viewed articles
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 4 - Operators
Reference: Vena Calcs - 3 - Data Types
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 1 - Managing Scripts
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 14:25 Reference: Vena Calcs - 6 - Conditional Statements – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027974231-Reference-Vena-Calcs-6-Conditional-Statements 6/6
