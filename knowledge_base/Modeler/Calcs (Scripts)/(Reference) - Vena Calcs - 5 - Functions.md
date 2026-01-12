# (Reference)   Vena Calcs   5   Functions

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
Managing Scripts
Reference: Vena Calcs - 2 -
Notation and Syntax
Reference: Vena Calcs - 3 - Data
Types
Reference: Vena Calcs - 4 -
Operators
Reference: Vena Calcs - 5 -
FunctionsReference: Vena Calcs - 5 - Functions

About this series
This series is about how to write and use Vena Calculation Scripts. You are on Part 5, which provides an overview of Calc functions.
Vena Calculations Scripts (or Vena Calcs) is a scripting language designed for Vena data models. Vena Calcs provides a powerful and flexible way to run
calculations and simulations for business rules at the database level for all dimensions and members.
You can apply calcs for a variety of uses, including calculating financial ratios and percentages, departmental/employee allocations or FX currency
conversions.
We've broken down Vena Calcs into nine articles. They can be read consecutively or browsed as needed.
Part 1: Managing Scripts
Part 2: Notation and Syntax
Vena Support Team
Updated 5 months ago
02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 1/32

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
PowerPointPart 3:Data Types
Part 4: Operators
Part 5: Functions - You are here
Part 6:Conditional Statements
Part 7: Currency Conversions
Part 8:Examples
Part 9: Troubleshooting
Table of contents
Functions
Functions - Argument Invocation
Suffix Dot Notation
Named Arguments
Optional Arguments
Available Functions
Leaves Bottom Level
Descendants/IDescendants
Children/IChildren
Exclude
Attribute
Attributes and Empty Sets
Aggregation Functions
Sum
Avg
Count
Min
Max
StdDev
StdDevp
Var
VarP
Time Series Functions
TimeScale02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 2/32

Vena Copilot
Product UpdatesPeriodsToDate
YTD
QTD
NextPeriod
PrevPeriod
NextPeriods
PrevPeriods
Limitations - Time Series Functions
Other
Round
Exists
Functions
In Vena Calculations, functions can be invoked using two styles: Function-Argument notation and Suffix Dot notation. Functions can apply to a set of
intersection values or aggregate a set of intersection values. The complete list of functions and operators can be viewed in the Functions/Operators
topic, later in the guide.
Functions - Argument Invocation
Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. Add as many
arguments as needed and separate them with a comma.
Examples:
1. Rounds values in the Year 2021 to 2 decimal places:
@this = Round([Year. 2021], 2)
2. Rounds values in data slice for the Year 2021 and Sales measure to 2 decimal places:
@this = Round(([Year. 2021], [Measure.Sales]), 2)02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 3/32

3. Sums Sales data for the Year 2021 and 2022 and Rounds values to 2 decimal places:
@this = Round(Sum({[Year. 2021], [Year.2022], [Measure.Sales]}), 2)
Suffix Dot Notation
Members, Tuples and Sets often use a more concise syntax known as Suffix Dot notation. In this style, the function is appended directly to the
intersection value. The expression begins with the first argument (as it would appear in Function-Argument Invocation), followed by a dot (.), then the
function name. Any additional arguments are passed within parentheses after the function name.
Examples (the exact same results as Function-Argument Invocation):
1. Rounds values in the Year 2021 to 2 decimal places:
@this = [Year. 2021].Round( 2)
2. Rounds values in data slice for the Year 2021 and Sales measure to 2 decimal places:
@this = ([Year. 2021], [Measure.Sales]).Round( 2)
3. Sums Sales data for the Year 2021 and 2022 and Rounds values to 2 decimal places:
@this = {[Year. 2021], [Year. 2022], [Measure.Sales]}.Sum().Round( 2)
Named Arguments
Some functions support named arguments, which allow you to specify argument names when calling the function. Named arguments can be provided
in any order.
Examples:
1. Named argument = Precision. NOTE: This is equivalent to Round([Year.2021], 2)02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 4/32

@this = Round([Year. 2021], Precision= 2)
2. Named argument = Precision.
@this = Round(([Year. 2021], [Measure.Sales]), Precision= 2)
3. Named argument = Precision.
@this = Round(Sum({[Year. 2021], [Year. 2022], [Measure.Sales]}), Precision= 2)
Optional Arguments
Some functions allow optional named arguments: if the argument is present, the function uses the value given. If it is not present, the function uses a
default value.
Example:
Scope {[Period.Mar]}
  @optional  = [Measure.Sales].PrevPeriod(Lag=1) // Uses (Sales, Jan)
 @default  = [Measure.Sales].PrevPeriod()      // Uses (Sales, Feb)
End
Available Functions
Data Model Functions
Functions used to indicate specific OLAP member set ranges within a dimension hierarchy. They can be used in Scope statements and value
assignment statements.02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 5/32

Leaves/Bottom Level
Function
NameLeaves() or BottomLevel()
Primary
Argument
TypeMember or Member Set
Optional
ArgumentsNone
ReturnsMember Set
Notes This command accepts either a Member or Member Set as the primary argument and returns a set
of all bottom-level members of the member(s) given as the primary argument.
Example[Period.Q1].Leaves() // Returns {[Jan], [Feb], [Mar]}
{[Period.Q1, [Period.Q2]}.BottomLevel() // Returns {[Jan], [Feb], [Mar], [Apr], [May], [Jun]}02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 6/32

Descendants/IDescendants
Function
NameDescendants() or IDescendants()
Primary
Argument
TypeMember or Member Set
Optional
ArgumentsInclusive (Type: Bool )
ReturnsMember Set
Notes This command accepts either a Member or Member Set as the primary argument and returns
a set of all descendant members of the member(s) given as the primary argument.
If the value of the argument Inclusive is true, the member(s) given in the primary argument
are included in the result. Alternatively, you can also use IDescendants() instead
of Descendants() as the primary argument function, which has the same effect as
using Inclusive=true.
Example[Period.H1].Descendants()  // Returns {[Q1], [Jan], [Feb], [Mar],  [Apr], [May], [Jun]}
[Period.H1].Descendants(Inclusive=true) or
[Period.H1].
        ()  // Returns {[H1], [Q1], [Jan], [Feb], [Mar], [Apr], [May], [Jun]}02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 7/32

Children/IChildren
Function
NameChildren() or IChildren()
Primary
Argument
TypeMember or Member Set
Optional
ArgumentsInclusive (Type: Bool )
ReturnsMember Set
Notes This command accepts either a Member or Member Set as the primary argument and returns a set
of all descendant members of the member(s) given as the primary argument.
If the value of the argument Inclusive is true, the member(s) given in the primary argument are
included in the result. Alternatively, Alternatively, you can also use IChildren() instead of Children() as
the primary argument function, which has the same effect as using Inclusive=true.
Example[Period.H1].Children() // Returns {[Q1], [Q2]}
[Period.H1].Children(Inclusive=true) or [Period.H1].IChildren()  // Returns {[H1], [Q1], [Q2]}02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 8/32

Exclude
Function
NameExclude()
Primary
Argument
TypeMember Set
Required
ArgumentsMember orMember Set
Optional
ArgumentsNone
ReturnsMember Set
Notes This command accepts a Member Set and an addition Member or Member Set and returns the set of members contained
in the first Member Set but not contained in the second argument.
Example[Period.Q1].Leaves().Exclude([Period.Jan])                                 // Returns {[Feb], [Mar]}
{[Period.Q1], [Period.Q2]}.Leaves().Exclude({[Period.Jan], [Period.Feb]})  // Returns {[Mar], [Apr], [May], [Jun]}02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 9/32

Attribute
Function
NameAttribute()
Primary
Argument TypeMember Set
Required
ArgumentsAttribute (Type: String case-insensitive)
Optional
ArgumentsValue (Type: String case-sensitive, Numeric and Date not supported)
Returns Member Set
Notes This command accepts a Member Set and an addition Attribute as the primary argument and returns the set of
members which have that attribute. If the argument Value is included, only members with the primary
argument attribute and the specified value are returned.
Example[All Entities].Leaves().Attribute("EUR") // Returns {[Ireland Entity], [Germany Entity], [France Entity]}
[All Products].Leaves().Attribute("Size", Value="Large")   // Returns {[Widget XL], [Jumbo Widget]}

Attributes and Empty Sets
To ensure calculations remain unaffected by changes to Attributes, referencing a non-existent attribute in a calculation does not produce an error.
Instead, the expression resolves to an empty set—a set with no members.
If this causes the entire Scope statement to resolve to an empty set, the calculation will not run. This is because Scope defines the portion of the cube
the calculation modifies; if it targets nothing, the calculation is skipped. Similarly, in read mode, if the Scope includes only members with non-existent02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 10/32

attributes, the calculation will also not run.
This behavior also impacts a common Scope shortcut: placing a single data model function at the end of the statement instead of after each member.
If that function resolves to an empty set, the entire Scope becomes empty, and the calculation is skipped.
For example, this:
Scope {
  [Year.All Years].Leaves(),
  [Period.All Periods].Leaves(),
  [Measure.Actuals].Leaves()
}
Can be simplified to:
Scope {
  [Year.All Years],
  [Period.All Periods],
  [Measure.Actuals]
}.Leaves()
However, when writing a Scope statement that includes Attribute, do not to use this simplified format:
Scope {
  [Year.All Years],
  [Period.All Periods],
  [Measure.Actuals]
}.Leaves().Attribute(" CurrentYear ")
This format will apply the Attribute function to the whole Scope statement. Therefore, if no members with the specified attribute are returned
for any part of the Scope statement, this will make the whole Scope statement resolve to an empty set. Consequently, the calc would never run.02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 11/32

Aggregation Functions
For the examples given below, the following sample data will be used:
JanFebMar
Account
01101520
Account
02121314
Assume that [Jan], [Feb], and [Mar] all share a common parent [Q1].
Sum
Function
NameSum()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the sum of the values stored at the
intersections represented by the set given. If the value of the optional
argument IgnoreEmpty is true, the calc will disregard intersections that
do not contain a value.02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 12/32

ExampleScope {[Account.Account 01], [Period.Apr]}
  @this = [Period.Q1].Leaves().Sum() // returns 10 + 15 + 20 = 45
End
Avg
Function
NameAvg()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the average of the values stored
at the intersections represented by the set given. If the
value of the optional argument IgnoreEmpty is true, the
calc will disregard intersections that do not contain a
value.
ExampleScope {[Account.Account 01], [Period.Apr]}
   @this = [Period.Q1].Leaves().Avg()  // returns 15
End02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 13/32

Count
Function
NameCount()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the number of intersections containing the set given. If
the value of the optional argument IgnoreEmpty is true, the calc will disregard
intersections that do not contain a value.
Example{[Period.Jan], [Period.Feb], [Period.Q1].Leaves()}.Count()  // Returns 5
Min
Function
NameMin()02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 14/32

Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the minimum of the values
stored at the intersections represented by the set
given. If the value of the optional argument
IgnoreEmpty is true, the calc will disregard
intersections that do not contain a value.
ExampleScope {[Account.Account 01], Apr}
@this = {[Period.Q1].Leaves()}.Min() // Returns 10
End
Max
Function
NameMax()
Primary
Argument
TypeSet02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 15/32

Max
Function
NameMax()
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the maximum of the values
stored at the intersections represented by the set
given. If the value of the optional argument
IgnoreEmpty is true, the calc will disregard
intersections that do not contain a value.
ExampleScope {[Account.Account 01], Apr}
@this = {[Period.Q1].Leaves()}.Max() // Returns 20
End02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 16/32

StdDev
Function
NameStdDev()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the standard deviation of the set
of intersections given, treating the set as a sample of a
population. If the value of the optional argument
IgnoreEmpty is true, the calc will disregard intersections
that do not contain a value.
ExampleScope {[Account.Account 01], Apr}
@this = {[Period.Q1].Leaves()}.StdDev() // Returns 5
End02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 17/32

StdDevP
Function
NameStdDevP()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the standard deviation of the set of
intersections given, treating the set as an entire population.
If the value of the optional argument IgnoreEmpty is true,
the calc will disregard intersections that do not contain a
value.
ExampleScope {[Account.Account 01], Apr}
@this = {[Period.Q1].Leaves()}.StdDevP() // Returns 4.1
End02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 18/32

Var
Function
NameVar()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the variance of the set of
intersections given, treating the set as a sample of a
population. If the value of the optional argument
IgnoreEmpty is true, the calc will disregard intersections
that do not contain a value.
ExampleScope {[Account.Account 01], Apr}
  @this = {[Period.Q1].Leaves()}.Var() // Returns 2502/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 19/32

VarP
Function
NameVarP()
Primary
Argument
TypeSet
Optional
ArgumentsIgnoreEmpty (Type: Bool)
ReturnsNum
Notes This command returns the variance of the set of
intersections given, treating the set as an entire population.
If the value of the optional argument IgnoreEmpty is true,
the calc will disregard intersections that do not contain a
value.
ExampleScope {[Account.Account 01], Apr}
@this = {[Period.Q1].Leaves()}.VarP()  // Returns 16.67
End
Time Series Functions
Time Series Functions generate sets of time-based intersections (e.g., Year, Quarter, Month). To use them, first calibrate your Vena Calcs script using
the TimeScale function. This function aligns your code with the structure of your time dimensions and must appear as the first line after the Scope
statement. It is a standalone statement and is not assigned to any intersection.02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 20/32

Example:
TimeScale([2010], [Q1], [Jan])
The three members can belong to a single dimension or be split across dimensions (e.g., Year in one, Quarter and Month in another). The specific
members used in TimeScale do not need to appear elsewhere in the script—they only need to exist in the model.
Once calibrated, the following time series functions become available for use. These functions return sets of intersections and must be paired with an
aggregation function (e.g., Sum()).
Example:
Scope {[Year.Y2014],[Scenario.Budget],[Measure.Total Revenue],[Product.All Products].Leaves(),[Period.Q1]}
    TimeScale ([Year.Y2015], [Period.Q1], [Period.Jan])
    @this = [Period.Mar].YTD().Sum()
End
For the below examples, the following sample data will be used.
2010 JanFebMar
Account 01 101520
Account 02
Assume that [Jan], [Feb], and [Mar] all share a common parent [Q1], and that the Year dimension contains the members [2010], [2011], and [2012].02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 21/32

TimeScale
Function
NameTimeScale()
Primary
Argument
Type3 Member
Optional
ArgumentsNone
ReturnsNone
Notes This command configures the time scale for
time series operations in the current calc.
Example// Years level contains the member `2010`
// Quarters level contains the member `Q1`
// Months level contains the member `Jan`
TimeScale([2010], [Q1], [Jan])02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 22/32

PeriodsToDate
Function
NamePeriodsToDate()
Primary
Argument
TypeMember or Tuple or MemberSet
Optional
ArgumentsLevel (Type Num )
ReturnsTuple Set
Notes This command returns a set of intersections in the period level given. Level=1 represents Years, Level=2 represents
Quarters, Level=3 represents Months. Level has the default value of 1.
Example[Year.2012].PeriodsToDate(Level=1)                        // returns {[2010], [2011], [2012]}

([Account.Account 1], [Period.Mar], [Year.2010]).PeriodsToDate(Level=3) // returns {[Jan], [Feb], [Mar]}
{[Account.Account 1], [Account.Account 2], [Period.Apr]}.PeriodsToDate(Level=2) // returns {([Account 1], [Q1]), ([Account 2], [Q2])}
YTD
Function Name YTD()
Primary Argument TypeMember or Tuple or Memberset02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 23/32

YTD
Function Name YTD()
Optional Arguments Level (Type Num )
Returns Tuple Set
Notes This command functions as a
shortcut to using
PeriodsToDate(Level=1).
QTD
Function Name QTD()
Primary Argument Type Member or Tuple or Memberset
Optional Arguments Level (Type Num )
Returns Tuple Set02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 24/32

QTD
Function Name QTD()
Notes This command functions as a
shortcut to using
PeriodsToDate(Level=2).
NextPeriod
Function
NameNextPeriod()
Primary
Argument
TypeMember or Tuple (forward in time)
Optional
ArgumentsLag (Type Num ) value of 1
ReturnsTuple
Notes The Lag commandrepresents the number of periods to step forward before returning.
Example[Period.Feb].NextPeriod()                              // returns [Mar]
([Period.Jan], [Account.Account 1]).NextPeriod(Lag=2)
// returns ([Mar], [Account 1])
// Note that the Lag argmuent is just a shortcut, the two following lines are equivalent:02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 25/32

[Period.Jan].NextPeriod(Lag=2)
[Period.Jan].NextPeriod().NextPeriod()
PrevPeriod
Function
NamePrevPeriod()
Primary
Argument
TypeMember or Tuple (Month level)
Optional
ArgumentsLag (Type Num ) value of 1
ReturnsTuple
Notes The Lag commandrepresents the number of periods to step forward before returning.
Example[Period.Feb].PrevPeriod()                              // returns [Jan]
([Period.Mar], [Account.Account 1]).PrevPeriod(Lag=2) // returns ([Jan], [Account 1])
// Note that the Lag argmuent is just a shortcut, the two following lines are equivalent:
[Period.Mar].PrevPeriod(Lag=2)
[Period.Mar].PrevPeriod().PrevPeriod()02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 26/32

NextPeriods
Function
NameNextPeriods()
Primary
Argument
TypeMember or Tuple
Additional
Required
ArgumentsNumber (Type Num)
Optional
ArgumentsLag (Type Num )
ReturnsTuple Set
Notes This command returns a set of the next Member or Tuple forward in time, in the Month level. The additional required
argument specifies how many to include in the set. Optional argument Lag has a default value of 1. Lag represents the
number of periods to step forward before returning.
Example[Period.Jan].NextPeriods(2)                   // returns {[Feb], [Mar]}
([Period.Jan], [Account.Account 1]).NextPeriods(2, Lag=2)   // returns {([Mar], [Account 1]), ([Apr], [Account 1])}02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 27/32

PrevPeriods
Function
NamePrevPeriods()
Primary
Argument
TypeMember or Tuple
Additional
Required
ArgumentsNumber (Type Num)
Optional
ArgumentsLag (Type Num )
ReturnsTuple Set
Notes This command returns a set of the previous Member or Tuple in time, in the Month level. The Number argument specifies
how many to include in the set. Optional argument Lag has a default value of 1. Lag represents the number of periods to
step forward before returning.
Example[Period.Mar].PrevPeriods(2) // returns {[Feb], [Jan]}
([Period.Apr], [Account.Account 1]).PrevPeriods(2, Lag=2)   // returns {([Feb], [Account 1]), ([Jan], [Account 1])}
Limitations - Time Series Functions
When using Time Series Calcs for Shared Members, there are a few limitations to keep in mind:
1. A first-level Time Series member cannot be shared02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 28/32

2. If a member is going to be shared, it cannot exist under two parents that are both used in a Time Series.
For example, January can belong under FullYear->Q1->Jan and under Alt->JanYTD->Jan, but not under FullYear->Q1->Jan and FullYear->Q2->Jan.
This assumes any leaf-level members used in Time Series are not root-level Time Series members.
Other
For the examples given below, the following sample data will be used:
JanFebMarApr
Account 011015
Round
Function
NameRound()
Primary
Argument
TypeNum
Required
ArgumentsNum
Optional
ArgumentsNone
ReturnsNum02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 29/32

Round
Function
NameRound()
Notes This command returns the first argument, rounded to the
appropriate precision. The second argument determines
the number of decimal places in the result.
ExampleScope {[Account.Account 01], Apr}
@this = [Jan]/[Feb]            // Returns 0.6666666...
    @this = Round([Jan]/[Feb], 2)  // Returns 0.67
 @this = Round([Jan]/[Feb], 5) // Returns 0.66667
End

Exists
Function NameExists()
Primary Argument
TypeMember or Tuple
Optional
ArgumentsNone02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 30/32

Exists
Function NameExists()
Returns Bool
Notes This command takes a Member or
Tuple, resolves that to an
intersection, and then
returns True if that intersection
exists in the cube. This is typically
most useful as the condition in
an If statement.
Example[Feb].Exists()   // Returns True
[Mar].Exists() // Returns False
Was this article helpful?
5 out of 7 found this helpful
Related articles
Reference: Vena Calcs - 6 - Conditional Statements
Reference: Vena Calcs - 8 - Examples
Reference: Vena Calcs - 2 - Notation and SyntaxRecently viewed articles
Reference: Vena Calcs - 4 - Operators
Reference: Vena Calcs - 3 - Data Types
Reference: Vena Calcs - 2 - Notation and Syntax02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 31/32

Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 4 - OperatorsReference: Vena Calcs - 1 - Managing Scripts
Reference: Sparse Calcs
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:25 Reference: Vena Calcs - 5 - Functions – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360027924251-Reference-Vena-Calcs-5-Functions 32/32
