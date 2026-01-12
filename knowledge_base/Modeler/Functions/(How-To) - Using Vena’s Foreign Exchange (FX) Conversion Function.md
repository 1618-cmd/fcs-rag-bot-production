# (How To)   Using Vena’s Foreign Exchange (FX) Conversion Function

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
FunctionHow-To: Using Vena’s Foreign
Exchange (FX) Conversion Function
Use Vena’s Foreign Exchange (FX) Conversion Function to accommodate for
international transactions by setting up calculations that will convert currencies
across your reports.
This article includes the steps on how to use Vena’s Foreign Exchange (FX) Conversion Function.
Visit this reference article for a list of frequently asked questions.
Sadaf Rahmanian
Updated 5 months ago
02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 1/14

Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesVisit this link for a demo.
Why use this feature?
The Foreign Exchange (FX) Conversion Function may be suitable for you if you report, or plan to
report, in multiple currencies and you have models without any existing FX Calcs.
Vena’s Foreign Exchange (FX) Conversion Function enables straightforward currency conversions
at the database level without advanced formula skills. You can easily set up automated
calculations across your data model. It automates calculations across your data model for faster
template performance, leveraging Vena’s engine. Follow the simple setup process using the step-
by-step wizard and save time by setting up automatic calculations.
This feature is easy to set up and use and you can configure it to include more currencies as
your company grows. Additionally, you can delete the function or undeploy it without impacting
your data model. This feature sets everything up for you - no need to create templates or
members.
Vena Academy E-Learning
To learn more about Vena's FX Function for Vena Desktop, take this interactive e-
learning course.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 2/14

Before you begin
To follow the instructions in this guide, you will need Modeler access. It is necessary that your
model has the following Dimension Types:
Account
Entity
Currency
Scenario
Year
Period
Visit this article for more information on tagging Dimension Types.
Additionally, you will need the following process variables:
PlanningMethod
FiscalStartMonth
PlanScenario
LastClosedMonth
We recommend setting up the FX function after your data model setup is complete.
To learn more about Vena's FX Function for Vena 365, take this interactive e-learning
course. 02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 3/14

Table of contents
How to
Use the Foreign Exchange Conversion
Deploy/Undeploy a Function
Notes & limitations
How to
Use the Foreign Exchange Conversion
1. Navigate to the Modeler tab.
2. Selection Functions from the sidebar.
3. Select + Create to create a new function.
4. Select Foreign Exchange Conversion as your type of function, followed by Next: Begin
Setup → to launch the FX Function Set Up Wizard.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 4/14

Step 1: Select Model
1. Choose the data model for the function from the drop-down menu.
2. Enter a name for the function or use the default suggested name. This must be a unique
name.
3. Select Next: Add Currencies →  to enter Step 2.
Step 2: Add Currencies
1. Ensure all the Entity members that you plan to convert currencies for are listed in this table.
All of the members from the Entity dimension will automatically appear in the table. You may
edit these members by selecting the Edit (
) icon next to Entity Members. Once in edit
mode, check or uncheck the box next to each specific member you want to include or
exclude.
2. To assign entities to a currency one at a time, choose the appropriate functional currency
from the drop-down menu.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 5/14

To assign multiple entities to the same currency, select the checkboxes next to entities you
want to assign the functional currency to. Once you've selected the entities, type or select a
currency in the drop-down menu, and then select Apply.
3. Choose the currency or currencies you will be reporting in from the drop-down menu.
4. You must set one of your reporting currencies as your reference currency. By default, the
first reporting currency will be set as the reference currency. You can assign another02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 6/14

reporting currency as the reference currency by selecting the vertical ellipsis (
 ), followed
by Set as R eference Curr ency .
5. Select Next: Specif y Rat e Types → .
Note02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 7/14

Step 3: Specify Rate Types
1. Ensure all the Chart of Account members that you plan to convert currencies for are listed in
this table. All of the bottom-level members of Balance Sheet and Net Income will automatically
appear in the table. You may edit these members by selecting the Edit (
) icon next to
Chart of Accounts Member. Once in edit mode, check and uncheck the checkbox next to each
specific member you want to include or exclude.
2. Choose the appropriate exchange rate type you want to match each chart of account
member to by using the drop-down menu. The options are either Month End Rate or Average
The reference currency is usually your main reporting currency. It is the currency that
will be used as a reference for calculating rates. For example, in a situation where
you would have three functional currencies: US Dollar, Canadian Dollar and British
Pound Sterling, and the US Dollar is set as your reference currency, you will only
need to enter the conversion rates for US Dollar and Canadian Dollar, as well as US
Dollar to British Pound Sterling. The rate between Canadian Dollar to British Pound
Sterling will be calculated automatically based on the reference currency.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 8/14

Rate.
3. Select Next: Build Template →  to continue.
Step 4: Build Template
1. Type or select the scenarios for the function.
2. Use the drop-down menu to choose how many years ahead you want to plan.
3. Choose the process files library the input template will be stored in from the drop-down
menu.
4. Select Create Function . This creates the function and takes you to a summary of your function.
You may choose to edit or make other changes to your function as you see fit. Now that your
function is created, you must enter the conversion rates in the FX For mula - Rat e Templat e
document, follow the steps below to complete this.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 9/14

Note
The function is not tied to the process, only the template is tied to the process. Even
if the process is changed, the template will still work.
Warning02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 10/14

Entering Conversion Rates
In this stage, you will enter the exchange rates. It is recommended that you enter the exchange
rates in the template before saving the values that need to be converted.
1. Navigate to the Manager tab.
2. Navigate to the Files Library of the process that you selected in Step 4.
3. Select FX Formula - Rate Templateto download the template.
4. Open the template and enter the conversion rates.
5. Select Save Data.
6. The function will now use the conversion rates you entered for calculations.
Deploy/Undeploy a function
When a function is deployed, members are created, data is calculated and when any target
scope is changed, the FX value is calculated. When a function is undeployed, the calculated data
Editing a function will redeploy the whole function and create all the artefacts again.
Avoid making any changes to your function unless it is absolutely necessary.
Note
If you would like a Contributor to enter rates instead, this template can be assigned
as an input task within a workflow.02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 11/14

is wiped out and the function does not run.
1. Navigate to the Modeler tab.
2. Select Functions from the sidebar.
3. Select the function that you want to deploy/undeploy.
4. Select Deploy or Undeploy .
Notes & limitations
You can only have one FX Function per data model.
If you exit the FX Function Wizard before completing all of the steps, it will be saved as a
draft. The draft will be saved up until the last step that was fully completed.
Each Entity can have one functional currency, but can have multiple reporting currencies. 1-
to-1 and 1-to-many are supported, but many-to-many is not.
For best results, we recommend that the rates be entered before the data.
Was this article helpful?
1 out of 2 found this helpful
Related articles Recently viewed articles02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 12/14

How-To: Assigning Dimension Types and
Standard Members
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 7 - Currency
Conversions
Explainer: Target Member Attribute Calc
Trigger
How-To: Setting up Data Validation RulesReference: Vena’s Foreign Exchange (FX)
Conversion Function FAQs
Troubleshooting: Encountered More Than the
Limit of 1000 Unmapped Members
Troubleshooting: ETL Error – Cannot Increase
the Number of Members Beyond 400000
Troubleshooting: This Member Does Not Exist
Error During Modeler Search
Troubleshooting: The Bulk Copy Parameters
Were Invalid
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 13/14

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 14:22 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 14/14
