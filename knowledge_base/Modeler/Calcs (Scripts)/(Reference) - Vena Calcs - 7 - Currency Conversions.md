# (Reference)   Vena Calcs   7   Currency Conversions

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
Reference: Sparse Calcs
Reference: Vena Calcs - 1 -
Managing ScriptsReference: Vena Calcs - 7 - Currency
Conversions
About this series
This series is about how to use Vena Calculation Scripts. Vena Calculations Scripts (or Vena Calcs), is a
scripting language designed for Vena data models. Vena Calcs provides a powerful and flexible way to run
calculations and simulations for business rules at the database level for all dimensions and members.
We've broken down Vena Calcs into nine articles, can be read consecutively or browsed as needed.
Vena Support Team
Updated 1 year ago
02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 1/29

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
Appearing
Troubleshooting: Calc Is Not
Triggering or Calculating After
Data Load or ImportPart 1: Managing Scripts
Part 2: Notation and Syntax
Part 3:Data Types
Part 4: Operators
Part 5:Functions
Part 6:Conditional Statements
Part 7: Currency Conversions- You are here
Part 8:Examples
Part 9:Troubleshooting
Table of contents
 Best Practices
FX Conversions
One Local, One Reporting
Multiple Local, One Reporting
One Local, Multiple Reporting
Multiple Local, Multiple Reporting
How to Optimize your Calc02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 2/29

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
Product UpdatesCurrency Conversions
The following article contains information on currency conversions (FX conversions) in Vena calcs.
FX Conversions
There are four standard types of FX Conversions Calculations, characterized by the number of local
currencies involved and the number of reporting currencies involved. The type you select will depend on
your business needs. In this section, we will describe the recommended data model hierarchy and the
necessary calculations to do FX Conversions for those four types.
For the following examples, assume the model has the following three dimensions:
Account
Period
Year
Example 1
Dimension: Account
  ── All_Accounts
        ├── Account001
        ├── Account002
        ... <etc>02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 3/29

  ── No_Account
Example 2
Dimension: Period
  ── All_Periods
        ├── Q1
        │   ├── Jan
        │   ├── Feb
        │   └── Mar
        ├── Q2
        │   ├── Apr
        │   ├── May
        │   └── Jun
        ... <etc>
  ── No_Period02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 4/29

Example 3
Dimension: Year
  ── All_Years
        ├── 2014
        ├── 2015
        └── 2016
  ── No_Year
One Local, One Reporting
This is the most straightforward type of FX Conversion: one local currency and one reporting currency. For
this kind of conversion, your model should have a Currency dimension with members for your local and
reporting currencies, and a third member for the rate to convert between the two. In this example, our
local currency is USD and our reporting currency is EUR.
Dimension: Currency
  ── All_Currencies
        ├── USD02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 5/29

        └── EUR
  ── FX_Rate
  ── No_Currency
Then, the calculation to do the FX Conversion is very simple:
Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.EUR]
}
    @local  = ([Currency.USD])
    @rate  = ([Currency.FX_Rate], [Account.No_Account])  // include other No_ members here
    @this = @local * @rate
End
This assumes that you have different FX Rates per period and per year, but within a single period and year
the rate is the same for all accounts. For other dimensions for which the rate will be constant, such as02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 6/29

department, product, etc. (the specifics will depend on your business case), include that dimension's
"No_" member in the @rate variable. Note that this calculation should be put into sparse mode. Sparse
mode is an optimization designed specifically for FX Conversions.
In this case, our sheets would look like this:
Page options:
Account: No_Account
Year: 2015
FX_Rate
Jan1.5
Feb1.6
Mar1.7
Account: Account001
Year: 2015
USDEUR
Jan10001500
Feb1000160002/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 7/29

USDEUR
Mar10001700
Multiple Local, One Reporting
This type of FX Conversion is used when you have many local currencies and a single reporting currency.
The best way to handle this scenario is, like the one-to-many case, use two dimensions: Currency and
Measure. In this example, we're converting from inputs in both USD, GBP, and EUR, and we're reporting in
GBP, these dimensions will look like:
Dimension: Currency
  ── All_Currencies
        ├── USD
        ├── GBP
        └── EUR
  ── No_Currency
Dimension: Measure02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 8/29

  ── All_Measures
        ├── FX_Rate
        ├── Local
        └── Reporting
  ── No_Measure
And the calc will be as follows:
Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.All_Currencies].Leaves(),
        [Measure.Reporting]
}

    @local  = ([Measure.Local])
    @rate  = ([Measure.FX_Rate], [Account.No_Account])
      @this = @local * @rate
End02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 9/29

Notice that this operates on all currencies; the @local and @rate variables will both have the same
member in the currency dimension. This calc tells Vena to take the value at a given currency and account
and at the Local measure, and multiply by the value at the same currency but at the
special No_Accountmember and the FX_Rate measure, and to store the product in the intersection at the
given currency and account at the Reporting measure. If we have multiple values in the same account
from different local currencies, we will find the aggregate of all of the converted values in
the All_Currencies parent member.
Again, like the one-to-one case, the assumption is made that the rates vary across period and year but
remain constant across account, and again, this calculation should be in sparse mode.
On the sheets, our data would look like:
Page options:
Account: No_Account
Year: 2015
Measure: FX_Rate
USD EUR GBP
Jan 1.5 2.0 1.0
Feb 1.6 2.1 1.0
Mar 1.7 1.9 1.0
Account: Account001
Year: 2015
Measure: Local02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 10/29

USD EUR GBP
Jan 1000 1000 1000
Feb 1000 1000 1000
Mar 1000 1000 1000
Account: Account001
Year: 2015
Measure: Reporting
USD EUR GBP All_Currencies
Jan 1500 2000 1000 4500
Feb 1600 2100 1000 4700
Mar 1700 1900 1000 4600
So, in this case, the reporting value for a given account in a given year and period is at
the ([Measure.Reporting], [Currency.All_Currencies])intersection. Also, notice that since we have inputs in
GBP and are reporting in GBP, the values at ([Measure.FX_Rate], [Currency.GBP]) are always 1.0.
One Local, Multiple Reporting02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 11/29

This kind of FX Conversion should be used if you have a single local currency and multiple reporting
currencies. In this case, your model would need two dimensions: a Currency dimension and a Measure
dimension. In this example, we are inputting in GBP and reporting in GBP and USD.
Dimension: Currency
  ── All_Currencies
        ├── GBP
        └── Reporting
            ├── GBP_rpt
            └── USD_rpt
  ── No_Currency
Dimension: Measure
  ── All_Measures
        ├── FX_Rate
        └── Value
  ── No_Measure
In this case, we want to convert the values stored under the two local currencies into the single reporting
currency. Our calc would be:02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 12/29

Scope { [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.Reporting].Leaves(),

        [Measure.Value]
}

    Scope { [Currency.GBP_rpt] }
        @local = ([Currency.GBP], [Measure.Value])
        @rate  = ([Measure.FX_Rate], [Account.No_Account], [Currency.GBP_rpt])

        @this = @local * @rate
    End
    Scope { [Currency.USD_rpt] }
         @local = ([Currency.GBP], [Measure.Value])
         @rate  = ([Measure.FX_Rate], [Account.No_Account], [Currency.USB_rpt])02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 13/29

        @this = @local * @rate
    End
End
The obvious difference is that we now need multiple subscopes for each reporting currency. This is
because, like the previous calcs, our calc is in sparse mode, so we need the local value to have a one-to-
one relationship with the reporting value. If we used one scope for all of the reporting currencies, both
the local value and the rate would have a one-to-many relationship with the reporting value.
If we set the calc in non-sparse mode, we could use the one scope for all of the reporting currencies, but
this runs the risk of flooding the entire cube with 0 values and will make saves, calculation deploys, and
rollups far slower. Running FX Conversions from a non-sparse calc is not recommended.
In this case, our sheets would look like
Page options:
Account: No_Account
Year: 2015
Measure: FX_Rate
GBPGBP_rptUSD_rpt
Jan11.5 2.0
Feb11.6 2.1
Mar11.7 1.902/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 14/29

Account: Account001
Year: 2015
Measure: Value
GBPGBP_rptUSD_rpt
Jan10001500 2000
Feb10001600 2100
Mar10001700 1900
Multiple Local, Multiple Reporting
This is the most complex of FX Conversion types: multiple local currencies, and multiple reporting
currencies. In cases like this, you will need to have two dimensions: Local Currency and Measure. In the
example below, we have USD and GBP as locals, and are reporting in GBP and EUR.
Dimension: Local Currency
  ── All_Local_Currencies
        ├── USD_loc
        └── GBP_loc02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 15/29

  ── No_Currency
Dimension: Measure
  ── All_Measures
        ├── Value
        └── Reporting
            ├── GBP_rpt
            └── EUR_rpt
  ── No_Measure
One obvious difference is that we now do not have any reporting currencies in the "Local Currency"
dimension. Instead, we use the combination of the two dimensions to describe the intersections.
Value GBP_rpt EUR_rpt
USD_loc Literal value in
USDUSD value converted into GBP USD value
converted into EUR
GBP_loc Literal value in
GBPGBP value converted into GBP (should be
identical to previous column)GBP value
converted into EUR02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 16/29

Value GBP_rpt EUR_rpt
All_local_currencies(meaningless)Total in GBP Total in EUR
This way, when looking at a converted value, we always know where that value came from. Essentially, the
"Measures" department is a "Reporting Currencies" department and the "Value" member could be
renamed "Local value".
In this scenario, the calc should look like the following:
Scope {
        [Account.All_Accounts].Leaves(),
        [Period.All_Periods].Leaves(),
        [Year.All_Years].Leaves(),
        [Currency.All_Local_Currencies].Leaves(),
        [Measure.Reporting].Leaves()
}

    Scope { [Measure.GBP_rpt]}
        @local = ([Measure.Value])
        @rate = ([Account.No_Account], [Measure.GBP_rpt])
        @this = @local * @rate02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 17/29

    End
    Scope { [Measure.EUR_rpt]}
        @local = ([Measure.Value])
        @rate  = ([Account.No_Account], [Measure.EUR_rpt])

        @this  = @local * @rate
    End

End
Again, this calc should be in sparse mode and, just like the case with multiple local currencies and one
reporting currency, has separate scopes for each reporting currency.
On the sheet, our data will look like so:
Page options:
Account: No_Account
Year: 2015
Period: Jan02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 18/29

USD_Loc GBP_Loc
GBP_rpt 1.5 1.0
EUR_rpt 1.6 1.0
Account: Account001
Year: 2015
Measure: Value
USD_Loc GBP_Loc
Jan 1000 1000
Account: Account001
Year: 2015
Measure: GBP_rpt
USD_Loc GBP_Loc All_Local_Currencies
Jan 1500 1000 2500
Account: Account001
Year: 2015
Measure: EUR_rpt02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 19/29

USD_Loc GBP_Loc All_Local_Currencies
Jan 3000 2000 5000
Notice that in this design, like in the many-to-one, the end result is the aggregation of all of the values
from the local currencies, after they have each been converted appropriately.
How to Optimize your Calc
1.) Form
1. Comment: Add commentary using the double slash (//) to provide context to others reading your
calc. Rule of thumb: Add a comment for each scope.
2. Proper indentation via Tab key and align each nested scope.
2.) Define every dimension
Defining all dimensions in your target scope will help our support team and other users at your company
follow the scope. This includes both stating the dimension and applicable members. Excluding a
dimension increases the calc scope drastically as it will ask the calc to calculate based on all the members
in that dimension.02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 20/29

3.) Manage Scope Size
Make sure to check your .Leaves() notation and ensure bottom level members under .Leaves() parents are
relevant. If they are not consider .Exclude sources members that are not likely to be populated.
4.) Manage your Number of Scopes
Scopes can be reduced by checking if the same members are applicable across scopes. For example, in
the following calc, there is only one Entity Parent. This can be moved to the Target Scope:
Scope   {
     [Department.All Departments].Leaves(),
     [Year.All Years].Leaves(),
     [Period.Full Year].Leaves(),
     [Placeholder 1.Not Placeholder 1 Specific],
     [Placeholder 2.Not Placeholder 2 Specific],
     [Placeholder 3.Not Placeholder 3 Specific],02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 21/29

     [Placeholder 4.Not Placeholder 4 Specific],
     [Scenario.Actual],[Scenario.Forecast],[Scenario.Budget],
     [Currency.All Reporting Currencies].Leaves()
    }
    //CONVERSION FOR ENTITIES WHERE LOCAL CURRENCY IS USD
    Scope {[Entity.All Entities in Local USD].Leaves()} //<<--- list of entities which have USD as lo
          //Define FX Rates. Include Placeholders if they are in use.
          @rate  = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific],
          [Department.Not Department Specific])

        Scope {[Account.Net Income]}.Leaves()
          //Define local values
          @local = ([Currency.Local])

          //Reporting value = FX Rates * local value
          @this =  @Local * @rate
          02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 22/29

        End
End
End
Your new calc should look like the following:
Scope   {
[Entity.All Entities in Local USD].Leaves()
[Department.All Departments].Leaves(),
[Year.All Years].Leaves(),
[Period.Full Year].Leaves(),
[Placeholder 1.Not Placeholder 1 Specific],
[Placeholder 2.Not Placeholder 2 Specific],
[Placeholder 3.Not Placeholder 3 Specific],
[Placeholder 4.Not Placeholder 4 Specific],
[Scenario.Actual],[Scenario.Forecast],[Scenario.Budget],
 [Currency.All Reporting Currencies].Leaves()
    }02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 23/29

           //Define FX Rates.
  @rate  = ([Account.Average Rate], [Measure.Local Rate USD], [Entity.Not Entity Specific],
          [Department.Not Department Specific])

        Scope {[Account.Net Income]}.Leaves()

 //Define local values
          @local = ([Currency.Local])

          //Reporting value = FX Rates * local value
          @this = @Local * @rate

        End
End
5.) Consider your Allocation Mode
Allocation mode is useful for calcs with a multiplication (eg. Target = A x B) or divide calculation (eg. Target
= A / B) . During deploy, the allocation mode detects all populated source intersections and only calculates
those intersections. If the source intersection is not populated, data will not recalculate.02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 24/29

Signs that your calc should be in Allocation mode:
1Multiplication or division calculation. This is
most common in Driver based planning,
allocations, KPI calculations, and Foreign
Exchange.
2View script details for potential fan-out ratio.
Example: Bad potential fan-out ratio
Example: Efficient potential fan-out ratio:02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 25/29

3Move the larger variable to the front of the
value statement.
4Append .Allocation to the name of the calc
6.) User Variables
Define @rate = slice instead of only stating the slice in the value statement.02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 26/29

For example:
Correct:
@Localvalues = [Currency.Local]
@rate = [Account.Average Rate],[Measure.Local Rate USD]
@This = @Localvalues * @rate
Incorrect:
@localvalues = slice
@This = @localvalues *  [Account.Average Rate],[Measure.Local Rate USD]
7.) Consider using an Attribute
Using an attribute for Year and/or Period allows the calc to only recalculate values from that year. If the
calc wrote to previous years when you change the members attached to the attribute the values will
remain. Note, when attribute changes (eg. if a new cycle is beginning) then the calc will have to be
redeployed.
8.) Consider splitting your calc into multiple calcs
Smaller scopes in multiple calcs will increase performance. Note, this may differ if there are dependent
calcs. Common logic is splitting calcs up by:02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 27/29

Financial Statement type (ie. Income statement/Balance Sheet). This is common in FX rates as the two
statements reference different rates.
Subsidiary
Scenario
Was this article helpful?
1 out of 3 found this helpful
Related articles
Reference: Vena Calcs - 8 - Examples
Reference: Vena Calcs - 2 - Notation and Syntax
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 9 - Troubleshooting
Reference: Vena Calcs - 6 - Conditional StatementsRecently viewed articles
Reference: Vena Calcs - 6 - Conditional Statements
Reference: Vena Calcs - 5 - Functions
Reference: Vena Calcs - 4 - Operators
Reference: Vena Calcs - 3 - Data Types
Reference: Vena Calcs - 2 - Notation and Syntax02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 28/29

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:44 Reference: Vena Calcs - 7 - Currency Conversions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027695452-Reference-Vena-Calcs-7-Currency-Conversions 29/29
