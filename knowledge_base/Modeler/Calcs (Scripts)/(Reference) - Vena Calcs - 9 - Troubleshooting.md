# (Reference)   Vena Calcs   9   Troubleshooting

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
Reference: Sparse CalcsReference: Vena Calcs - 9 -
Troubleshooting
About this series
This series is about how to use Vena Calculation Scripts. Vena Calculations Scripts (or Vena
Calcs), is a scripting language designed for Vena data models. Vena Calcs provides a powerful
and flexible way to run calculations and simulations for business rules at the database level for
all dimensions and members.
Vena Support Team
Updated 6 months ago
02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 1/7

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
AppearingWe've broken down Vena Calcs into nine articles, can be read consecutively or browsed as
needed.
Part 1: Managing Scripts
Part 2: Notation and Syntax
Part 3:Data Types
Part 4: Operators
Part 5:Functions
Part 6:Conditional Statements
Part 7: Currency Conversions
Part 8:Examples
Part 9: Troubleshooting - you are here.
Table of contents
 Calcs Troubleshooting FAQ
Why is my calc not calculating?
Why is my calc slower than usual?
Why is the total number of intersections incorrect?
 02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 2/7

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
Product UpdatesCalcs Troubleshooting FAQ
1.) Why is my calc not calculating?
Are the members new?
Although in scope, any newly added members require a deploy.
Is there source data?
Export the data in the source intersections to see if the cube is actually populated or if the
data has not been saved due to a mapping issue on the template.
Use the drill calc feature.
Is it an Allocation calc?
If the first source of the calc is not populated, the calc will not recalculate even if the
second source has changed.
                 Eg. A x B = Target,
                 5 x 10 = 50
                 If A or B change, then target will be recalculated.
               If Blank x 10 = 0
               Any change to 10 (B) will not trigger recalculation (Target).02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 3/7

               Any change to Blank (A) will trigger a recalculation (Target).
              If 5 x Blank = 0
              Any change to 5 (A) will trigger a recalculation (Target).
             Any change to Blank(B) will trigger a recalculation (Target).
Is it a Read calc?
A Read Calc will not show results if the server property below has not been set to True:
EnableReadCalcsSSSEmptyTargets
Have you overwritten calc target data?
Drill saves on the answer that you are expecting. Do past saves include a non-calc
template or ETL saves?
If the answer is yes to either, consider excluding the members from the calc’s target
scope. If logic requires an override:
Template save - use an over-ride member instead to separate the two data paths.
ETL- Use an over-ride member to load data into a separate member and map this
member in the template as an override.
2.) Why is my calc slower than usual?
Have you added a significant amount of members?
Adding members adds to the sparsity of the cube and adds to the number of intersections
that require scanning. The higher the number of dimensions, the larger the stress on the
calc.02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 4/7

Refer to this article for how to optimize your calc.
Are you having to deploy a calc often?
Please reach out to our support or services team for more calc optimization tips.
3.) Why is the total number of intersections incorrect?
Have you accidentally written to the calc parent?
Check the calc revisions to see if there are parent members in the target scope. This could
happen for a couple of reasons:
1.The calc may have been a read calc to the parent that has accidentally been saved
without the .Read appended to the calc.
2.The calc was saved and deployed with an iDescendents,  iChildren or without
.Leaves() notation.
To remedy, you may undeploy the calc. Please note if there are any intersections
overwriting calc targets, undeploying will remove those values. If you are unsure, please
reach out to support before undeploying.
To verify whether it's safe to undeploy:
Drill into the calculated intersection.
Review the save history.
Confirm that all writes are labeled as calc or calc deploy.02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 5/7

If any save is labeled differently (e.g., a manual data entry), undeploying will remove
that value.
Was this article helpful?
1 out of 1 found this helpful
Related articles
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 8 - Examples
Troubleshoot: Calc Target Contains Data Even
Though It Shouldn’t
Reference: Writing Expressions (MQL & HQL)Recently viewed articles
Reference: Vena Calcs - 8 - Examples
Reference: Vena Calcs - 7 - Currency
Conversions
Reference: Vena Calcs - 6 - Conditional
Statements
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 4 - Operators02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 6/7

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:45 Reference: Vena Calcs - 9 - Troubleshooting – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360047724411-Reference-Vena-Calcs-9-Troubleshooting 7/7
