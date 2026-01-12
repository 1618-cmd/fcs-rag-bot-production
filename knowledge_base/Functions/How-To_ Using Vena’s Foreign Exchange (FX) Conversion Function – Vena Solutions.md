# How To  Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions

How-To: Using Vena’s Foreign
Exchange (FX) Conversion Function
Use V ena’s  Foreign Ex change (FX) Conv ersion Function  to accommodate for
international transactions by setting up calculations that will convert currencies across
your reports .
This article includes the steps on how to use V ena’s Foreign Exchange (FX) Conversion Function.
Visit this reference article for a list of frequently asked questions.
Visit this link for a demo.
Why use this feature?
The Foreign Exchange (FX) Conversion Function may be suitable for you if you report, or plan to
report, in multiple currencies and you have models without any existing FX Calcs.
Vena’s Foreign Exchange (FX) Conversion Function enables straightforward currency conversions at
the database level without advanced formula skills. Y ou can easily set up automated calculations
across your data model. It automates calculations across your data model for faster template
performance, leveraging V ena’s engine. Follow the simple setup process using the step-by-step
wizard and save time by setting up automatic calculations.
This feature is easy to set up and use and you can configure it to include more currencies as your
company grows. Additionally, you can delete the function or undeploy it without impacting your
data model. This feature sets everything up for you - no need to create templates or members.
Sadaf Rahmanian
Updated  5 months ago

Vena Academy E-Lear ning29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 1/8


Before you begin
To follow the instructions in this guide, you will need  Modeler  access. It is necessary that your
model has the following Dimension T ypes:
Account
Entity
Currency
Scenario
Year
Period
Visit this article for more information on tagging Dimension T ypes.
Additionally, you will need the following process variables:
PlanningMethod
FiscalStartMonth
PlanSc enario
LastClos edMonth
We recommend setting up the FX function after your data model setup is complete.

Table of contents
How to
Use the Foreign Exchange Conversion
Deploy/Undeploy a Function
Notes & limitations

How to
Use the Foreign Exchange ConversionTo learn more about V ena's FX Function for V ena Desktop, take this interactive e-
learning course.
To learn more about V ena's FX Function for V ena 365, take this interactive e-learning
course. 29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 2/8

1. Navigate to the  Modeler  tab.
2. Selection  Functions  from the sidebar.
3. Select  + Create to create a new function.
4. Select  Foreign Ex change Conv ersion as your type of function, followed by  Next: Begin Setup
→ to launch the FX Function Set Up Wizard.
Step 1: Select Model
1. Choose the data model for the function from the drop-down menu.
2. Enter a name for the function or use the default suggested name. This must be a unique name.
3. Select  Next: Add Curr encies →  to enter S tep 2.

Step 2: Add Currencies
1. Ensure all the  Entity  members that you plan to convert currencies for are listed in this table. All
of the members from the  Entity  dimension will automatically appear in the table. Y ou may edit
these members by selecting the  Edit (
 ) icon next to  Entity Member s. Once in edit mode,
check or uncheck the box next to each specific member you want to include or exclude.
2. To assign entities to a currency one at a time, choose the appropriate functional currency from
the drop-down menu.29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 3/8

To assign multiple entities to the same currency, select the checkboxes next to entities you want
to assign the functional currency to. Once you've selected the entities, type or select a currency
in the drop-down menu, and then select  Apply .
3. Choose the currency or currencies you will be reporting in from the drop-down menu.
4. You must set one of your reporting currencies as your reference currency. By default, the first
reporting currency will be set as the reference currency. Y ou can assign another reporting
currency as the reference currency by selecting the vertical ellipsis (
 ), followed by  Set as
Reference Curr ency .
29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 4/8

5. Select  Next: Specif y Rat e Types → .

Step 3: Specify Rate T ypes
1. Ensure all the  Char t of Account members that you plan to convert currencies for are listed in this
table. All of the bottom-level members of  Balanc e Sheet  and Net Inc ome will automatically
appear in the table. Y ou may edit these members by selecting the  Edit (
 ) icon next to  Char t
of Accounts Member . Once in edit mode, check and uncheck the checkbox next to each specific
member you want to include or exclude.
2. Choose the appropriate exchange rate type you want to match each chart of account member
to by using the drop-down menu. The options are either Month End Rate or A verage Rate.Note
The reference currency is usually your main reporting currency. It is the currency that
will be used as a reference for calculating rates. For example, in a situation where you
would have three functional currencies: US Dollar, Canadian Dollar and British P ound
Sterling, and the US Dollar is set as your reference currency, you will only need to enter
the conversion rates for US Dollar and Canadian Dollar, as well as US Dollar to British
Pound S terling. The rate between Canadian Dollar to British P ound S terling will be
calculated automatically based on the reference currency.29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 5/8

3. Select  Next: Build T emplat e → to continue.
Step 4: Build T emplate
1. Type or select the scenarios for the function.
2. Use the drop-down menu to choose how many years ahead you want to plan.
3. Choose the process files library the input template will be stored in from the drop-down menu.
4. Select  Create Function . This creates the function and takes you to a summary of your function.
You may choose to edit or make other changes to your function as you see fit. Now that your
function is created, you must enter the conversion rates in the  FX For mula - Rat e
Templat e document, follow the steps below to complete this.
Note29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 6/8


Entering Conv ersion Rat es
In this stage, you will enter the exchange rates. It is recommended that you enter the exchange
rates in the template before saving the values that need to be converted.
1. Navigate to the  Manager  tab.
2. Navigate to the  Files Librar y of the process that you selected in S tep 4.
3. Select  FX For mula - Rat e Templat e to download the template.
4. Open the template and enter the conversion rates.
5. Select  Save Data .
6. The function will now use the conversion rates you entered for calculations.
Deploy/Undeploy a function
When a function is deployed, members are created, data is calculated and when any target scope is
changed, the FX value is calculated. When a function is undeployed, the calculated data is wiped
out and the function does not run.
1. Navigate to the  Modeler  tab.
2. Select  Functions  from the sidebar.
3. Select the  function  that you want to deploy/undeploy.
4. Select  Deploy  or Undeploy .

Notes & limitationsThe function is not tied to the process, only the template is tied to the process. Even if
the process is changed, the template will still work.
Warning
Editing a function will redeploy the whole function and create all the artefacts again.
Avoid making any changes to your function unless it is absolutely necessary.
Note
If you would like a Contributor to enter rates instead, this template can be assigned as
an input task within a workflow.29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 7/8

You can only have one FX Function per data model.
If you exit the FX Function Wizard before completing all of the steps, it will be saved as a draft.
The draft will be saved up until the last step that was fully completed.
Each Entity can have one functional currency, but can have multiple reporting currencies. 1-to-1
and 1-to-many are supported, but many-to-many is not.
For best results, we recommend that the rates be entered before the data.29/12/2025, 08:06 How-To: Using Vena’s Foreign Exchange (FX) Conversion Function – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14847952948877-How-To-Using-Vena-s-Foreign-Exchange-FX-Conversion-Function 8/8
