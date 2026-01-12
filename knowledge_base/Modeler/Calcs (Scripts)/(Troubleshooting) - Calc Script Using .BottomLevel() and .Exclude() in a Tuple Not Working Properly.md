# (Troubleshooting)   Calc Script Using .BottomLevel() and .Exclude() in a Tuple Not Working Properly

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
Reference: Sparse CalcsTroubleshooting: Calc Script Using
.BottomLevel() and .Exclude() in a
Tuple Not Working Properly
Issue summary
You may create a Calc script with a formula that is using .Bottomlevel() in conjunction with
.Exclude() but it doesn’t calculate properly.
Olalekan Adebayo
Updated 2 years ago
02/01/2026, 14:46 Troubleshooting: Calc Script Using .BottomLevel() and .Exclude() in a Tuple Not Working Properly – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15551712180237-Troubleshooting-Calc-Script-Using-BottomLevel-and-Exclude-in-a-Tuple-Not-Working-Properly 1/4

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
Appearing 
 Suggested solution
You may have an expression in your Calc that uses .BottomLevel() and .Exclude() together as
shown below:
Scope{[Movement.OTH]}
@this = [Movement.CLO] - [Movement.OPE] - ([Movement.TOT].BottomLevel().Exclude([Movement.OT
If it’s not calculating properly, in this case, add the .SUM() function to the end of the expression
or tuple as shown below:
Scope{[Movement.OTH]}
@this = [Movement.CLO] - [Movement.OPE] - [Movement.TOT].BottomLevel().Exclude([Movement.OTH
Once updated, save the script and re-upload the source file or deploy the script.
Keywords
calc, calc, bottomlevel, exclude, calc not working02/01/2026, 14:46 Troubleshooting: Calc Script Using .BottomLevel() and .Exclude() in a Tuple Not Working Properly – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15551712180237-Troubleshooting-Calc-Script-Using-BottomLevel-and-Exclude-in-a-Tuple-Not-Working-Properly 2/4

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
Product UpdatesWas this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 2 - Notation and
Syntax
Troubleshooting: No Values Generate for a
Reporting Currency
Explainer: Target Member Attribute Calc
TriggerRecently viewed articles
Troubleshooting: Calc Is Not Triggering or
Calculating After Data Load or Import
Troubleshooting: Calc Conversion Not
Working or Zero Values Appearing
Troubleshoot: Calc Target Contains Data Even
Though It Shouldn’t
Reference: Vena Calcs - 9 - Troubleshooting
Reference: Vena Calcs - 8 - Examples02/01/2026, 14:46 Troubleshooting: Calc Script Using .BottomLevel() and .Exclude() in a Tuple Not Working Properly – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15551712180237-Troubleshooting-Calc-Script-Using-BottomLevel-and-Exclude-in-a-Tuple-Not-Working-Properly 3/4

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:46 Troubleshooting: Calc Script Using .BottomLevel() and .Exclude() in a Tuple Not Working Properly – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15551712180237-Troubleshooting-Calc-Script-Using-BottomLevel-and-Exclude-in-a-Tuple-Not-Working-Properly 4/4
