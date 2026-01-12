# (Reference)   Vena’s Foreign Exchange (FX) Conversion Function FAQs

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Functions Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Reference: Vena’s Foreign
Exchange (FX) Conversion
Function FAQs
How-To: Using Vena’s Foreign
Exchange (FX) Conversion
FunctionReference: Vena’s Foreign Exchange
(FX) Conversion Function FAQs
Learn more about Vena’s Foreign Exchange (FX) Conversion Function through
some of our frequently asked questions.
Overview
Sadaf Rahmanian
Updated 1 year ago
02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 1/9

Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesThis article features FAQs about Vena’s Foreign Exchange (FX) Conversion Function. For more
information, see this how-to article on using Vena's Foreign Exchange Conversion Function.  For
a demo, also visit this link.
Reference Guide
What dimensions and members do I need in my model to use the FX
Function?
You will need the dimensions and members listed in the table below for your data model to be
compatible with the FX Function. They will need to be matched by name, or if you'd like to name
them something else, they need to be tagged to the dimension type. Visit this article for more
information on tagging Dimension Types.
Dimension Member Notes
Currency Local Include your report data in
this currency. It will later be
converted to the reporting
currency based on the FX
configuration. This will be
used by the underlying Calc
script.
Account Other Accounts This is for your organization
for miscellaneous use.02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 2/9

Account Net Income
OR
Balance SheetAt least one of the two is
mandatory, Net Income or
Balance Sheet.
Entity This is used to populate Step 2
of the Wizard and assign
currencies.
Measure Other Measures This is for your organization
for miscellaneous usages.
Year All Years This is used in calculations.
Period Full Year This is used in calculations.
Scenario Plan Scenarios This is used in calculations, as
well as in templates in the
Choose Box.02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 3/9

*(All dimensions) Undefined It is assumed that all
dimensions would have a
member called, Undefined.
Particularly we need those for
the following dimensions:
Placeholder * (as it’s in a
setting of a template)
Entity (as it used in rate
lookup)
Department (as it used in
rate lookup)
Which process variables do I need to use the FX Function?
You will need the following process variables: PlanningMethod, FiscalStartMonth, PlanScenario and
LastClosedMonth.
When should I set up the FX function?
We recommend setting up the FX function after your data model setup is complete. At this point,
you can set up the FX function - this will generate a template where you can enter the exchange
rates. It is recommended that you enter the rates in the template before saving the values that
need to be converted.
Why do I get an error when selecting a model?02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 4/9

You may be getting an error when selecting a model due to two reasons:
1. You don’t have the appropriate permissions to select the model type.
2. The data model that you selected doesn’t have the required members/dimensions.
How is the Entity list populated?
The Entity list is populated by the Dimension named Entity or the dimension tagged with the
Entity type.
How is the Account table populated?
The Account table is populated by Net Income and Balance Sheet.
How can I exclude specific Entities or Accounts from the function?
You can specify Entities in Step 2 and Accounts in Step 3 of the Set up Wizard. You may edit
these members by selecting the Edit (
) icon next to Entity Members or Chart of Accounts
Member. Once in edit mode, check and uncheck the checkbox next to each specific member you
want to include or exclude.
What scope does the function apply to?
The scope of the function applies to all departments, plan scenarios, all placeholders, FX
reporting currencies, years and periods.02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 5/9

What happens on deployment of a function?
When a function is deployed, members are created, data is calculated and when any target
scope is changed, the FX value is calculated.
What happens on undeployment of function?
When a function is undeployed, the calculated data is wiped out and the function does not run.
What does deployment time represent?
The deployment time is the time it took for your function to deploy. This does not display the
expected time. Therefore, it is empty when the function is deployed for the first time.
What happens when I remove a function?
When you delete a function, the values that were calculated by the function are deleted and any
future values that are converted to different currencies won’t be calculated.
What happens to the function when I copy my process?
When you copy your process, the function should work as expected. Functions are tied to data
models and not processes, so the function should not be effected.
What happens to function when I remove the process?02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 6/9

When you remove a process, the function should work as expected. Functions are tied to data
models and not processes, so the function should not be effected.
What members does the FX function create?
The table displays all of the members that the FX function creates.
Dimension Member
Currency All Currencies →  FX Reporting Currencies
Note: All currencies and reporting currencies will be
created by the FX function
Currency (multiple) FX Reporting Currencies →  FX - Reporting <CODE>
Account Other Accounts →  FX Rates
Account FX Rates →  FX - Average Rate
Account FX Rates →  FX - Month End Rate
Measure Other Measures →  FX Currency Measures
Measure FX Currency Measures →  FX - Rate <CODE>02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 7/9

What other artifacts does the FX function create?
The FX function will create a rate template. This template is where you will enter the conversion
rates. The FX function will also create two process variables: Max year and Ref currency. These
process variables will be added to the process that you choose in the function.
Are functions part of the Migration Package?
Functions aren't part of the migration package. Functions are set to be easy to use and self-serve
so that you can use them easily out of the box.
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Using Vena’s Foreign Exchange (FX)
Conversion Function
Troubleshooting: Dataset Type Defaults to
“Custom”Recently viewed articles
Troubleshooting: Encountered More Than the
Limit of 1000 Unmapped Members
Troubleshooting: ETL Error – Cannot Increase
the Number of Members Beyond 40000002/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 8/9

Explainer: Target Member Attribute Calc
Trigger
Reference: ETL Guide - 3 - Command Line ETL
Vena Insights Series (Part 1) - Introduction to
Vena InsightsTroubleshooting: This Member Does Not Exist
Error During Modeler Search
Troubleshooting: The Bulk Copy Parameters
Were Invalid
How-To: Downloading All Vena Data From
Your Tenant or Environment
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:21 Reference: Vena’s Foreign Exchange (FX) Conversion Function FAQs – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14848148062093-Reference-Vena-s-Foreign-Exchange-FX-Conversion-Function-FAQs 9/9
