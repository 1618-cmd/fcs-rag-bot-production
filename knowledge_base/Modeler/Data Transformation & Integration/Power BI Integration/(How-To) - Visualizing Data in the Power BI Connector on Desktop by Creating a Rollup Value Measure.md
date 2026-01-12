# (How To)   Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Power BI Integration Search
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
ETL JobsHow-To: Visualizing Data in the Power
BI Connector on Desktop by Creating a
Rollup Value Measure
Why use this feature?
When working with Vena data in Power BI, you may notice that simply dragging fields into a
visual doesn’t always give you the numbers you expect. That’s because of how Vena stores data
Laura Harris
Updated 6 months ago
05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 1/22

Data Querying
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
How-To: Use Power BI
Connector
How-To: Visualizing Data in the
Power BI Connector on Desktop
by Creating a Rollup Value
Measure
Explainer: Power BI Connector
Member Aliases
How-To: Clear or Refresh
Permissions in Power BI
Troubleshooting: Vena Insights
Connector Table Relationship Is—and how Power BI reads it.
Vena vs. Power BI: different data structures
Vena stores data in a multi-dimensional OLAP cube, where each dimensions like Account, Period
and Scenario are layered.
Power BI on the other hand, processes data in flat 2D tables. To bring Vena data into Power BI,
the cube must be “flattened” into separate tables—one for each dimension, and one for the
values.
This flattening process is necessary, but it also introduces a challenge. Power BI doesn’t
automatically know how to roll up values across dimensions the way Vena does.
What happens without rollups?
Let’s say you want to create a bar chart showing total values for Account Level 1 over each
period.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 2/22

Not Auto-Detected
Troubleshooting: Vena Insights
Connector Invalid Application
Token Provided
Troubleshooting: Vena Insights
Connector SigntoLevel Column
Not Available
Troubleshooting: Vena Insights
Connector Failed to Update
Data Source Credentials
Troubleshooting: Vena Insights
Connector Users Able To See
Data Models They Don’t Have
Access To
Troubleshooting: Vena Insights
Connector Load and Transform
Data Buttons Grayed Out
Troubleshooting: Vena Insights
Connector Data Model
Intersections or Values Table Is
Blank
Troubleshooting: Vena Insights
Connector Intersection Values
Showing as Zero
Troubleshooting: Unable To
Connect to Vena Insights
If you just drag Account_Level1 into a visual and use the raw values:
Power BI might count the number of records instead of summing the actual values.
05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 3/22

Connector
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
& Connections
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
NameYou’ll see how many entries exist—not the total value for each account.
But what you really want is to see the true financial total for each account.A rollup measure
solves this by:
Summing the correct values from the value table.
Applying signs (positive or negative) based on account and measure logic.
Respecting hierarchy levels, so totals are accurate whether you’re looking at high-level
summaries or detailed breakdowns.
Automatically adjusting based on what the user is viewing or filtering.
This ensures your visuals show true financial totals, not just counts or partial data.
What is an operator?05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 4/22

Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesOperators in Power BI define how values should behave in a rollup:
+ means add the value.
means subtract the value.
~ means ignore the value.
These operators are part of the DAX (Data Analysis Expressions) language used in Power BI to
build custom calculations.Operators are especially useful for financial logic. For example, you
want to calculate Net Income, which is:
Revenue - Cost of Goods Sold - Expenses - Taxes
With operators, you can assign:
+ to Revenue
to COGS, Expenses, and Taxes
This ensures your rollup measure automatically subtracts the right values—no manual tweaking
needed.
In Vena, dimensions not explicitly configured for rollups use the + operator by default.
What is a measure?
A measure is a calculated field in Power BI. It uses DAX to define how values should be
aggregated or calculated.
In this case, your Rollup Value is a measure that:
Uses operators to apply the correct signs.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 5/22

Uses hierarchy depth to determine the right level of aggregation.
Uses logic to show or hide rows based on what the user is viewing.
Why should I use operators and measures in Power BI?
Operators are helpful for performing calculations that include things like negative rollups. For
example, you have a parent-level member (Net Income) where the total value is determined by
subtracting the value of the children. In this scenario, you could use a negative operator to
subtract the cost of goods sold, depreciation/amortization, interest, taxes, etc. from the total
value.
Visit this page for more information on Power BI DAX operators. Visit this page for more
information about Power BI measures.
Before you begin
To follow the instructions in this article, you must have access to Power BI and the
appropriateApplication Permissions to access the data models you want to analyze.

Table of contents05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 6/22

How to
Set up your Power BI connector
Set up your measures for operators
Notes and limitations
How to
Set up your Power BI connector
If you are using Power BI for the first time, follow the instructions in this article to import a data
model hierarchy.
Set up your measures for operators
If you have already set up your Power BI connector, make sure that your endpoint is up to
date, If you need to update your endpoint, follow the first 5 steps in the Power BI connector
article.
 Once your connector is up to date, set up your operators by following these steps:
1. Open Power BI on your desktop.
2. Select Account and select New measure from the drop-down menu.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 7/22

3. Begin by creating two measures for each dimension table:
1. BrowseDepth
2. RowDepth
Make sure to add the dimension name as a prefix (in the examples below, the
dimension name is “Account”).
Caution05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 8/22

See below for an example of a set for BrowseDepth, AccountDepth and RowDepth.
BrowseDepth: This measure determines how deep the user is currently looking into a
hierarchy (like Account levels) in a visual (e.g., a matrix or table). This is required for all
dimensions.
AccountBrowseDepth =
VAR L1 = IF ( ISINSCOPE ( Account[Account_Level1] ), 1, 0)
VAR L2 = IF ( ISINSCOPE ( Account[Account_Level2] ), 2, 0)
VAR L3 = IF ( ISINSCOPE ( Account[Account_Level3] ), 3, 0)
VAR L4 = IF ( ISINSCOPE ( Account[Account_Level4] ), 4, 0)
VAR L5 = IF ( ISINSCOPE ( Account[Account_Level5] ), 5, 0)
VAR L6 = IF ( ISINSCOPE ( Account[Account_Level6] ), 6, 0)
VAR L7 = IF ( ISINSCOPE ( Account[Account_Level7] ), 7, 0)
VAR L8 = IF ( ISINSCOPE ( Account[Account_Level8] ), 8, 0)
RETURN
MAX(L1, MAX(L2, MAX(L3, MAX(L4, MAX(L5, MAX(L6, MAX(L7, L8)))))))
If a dimension has a keyword (e.g., Measure or Currency) you must use single ('
') quotation marks.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 9/22

ISINSCOPE checks if a specific level is being shown in the visual. It returns the deepest
level currently visible. This helps the report know what level of detail you are viewing.
AccountDepth:Create an Account_depth column if you don’t have it in the account
section. If you have more than 8 levels, copy the lines of code to add more levels.
Account_depth =
SWITCH(
    TRUE(),
    NOT(ISBLANK(Account[Account_Level8])), 8,
    NOT(ISBLANK(Account[Account_Level7])), 7,
    NOT(ISBLANK(Account[Account_Level6])), 6,
    NOT(ISBLANK(Account[Account_Level5])), 5,
    NOT(ISBLANK(Account[Account_Level4])), 4,
    NOT(ISBLANK(Account[Account_Level3])), 3,
    NOT(ISBLANK(Account[Account_Level2])), 2,05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 10/22

    NOT(ISBLANK(Account[Account_Level1])), 1,
    0
)
RowDepth: This measure returns the maximum depth of the current level. This is
required for all dimensions.
It looks at the Account_depth column and returns the highest level present. This is used to
compare against BrowseDepth to decide whether a row should be shown.
 AccountRowDepth = VALUE ( MAX ( Account[Account_depth] ) )
4. Next, create a third measure (MinFilterDepth) for each dimension that will need to support
negative (-) or ignore (~) operators (recommended 2 dimensions max.)
MinFilterDepth: This detects which level is being displayed when the dimension is not
mapped onto a visual, but just filtering it. This measure is only required if the dimension
needs to support negative operators or ignore them.
Adjust the account levels based on how many account levels you have in the account
section.
Note
[Account_depth] can be replaced with any depth column name.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 11/22

 AccountMinFilterDepth = VAR L1 = IF ( ISFILTERED ( 'Account'[Account_level1] ), 1, 100
VAR L2 = IF ( ISFILTERED ( 'Account'[Account_level2] ), 2, 100)
VAR L3 = IF ( ISFILTERED ( 'Account'[Account_level3] ), 3, 100)
VAR L4 = IF ( ISFILTERED ( 'Account'[Account_level4] ), 4, 100)
VAR L5 = IF ( ISFILTERED ( 'Account'[Account_level5] ), 5, 100)
VAR L6 = IF ( ISFILTERED ( 'Account'[Account_level6] ), 6, 100)
VAR L7 = IF ( ISFILTERED ( 'Account'[Account_level7] ), 7, 100)
VAR L8 = IF ( ISFILTERED ( 'Account'[Account_level8] ), 8, 100)
VAR L9 = IF ( ISFILTERED ( 'Account'[Account_level9] ), 9, 100)
RETURN
MIN(MIN(MIN(MIN(MIN(MIN(MIN(MIN(L1, L2), L3), L4), L5), L6), L7), L8), L9)
ISFILTERED checks if a level is being filtered. If it is, it returns the level number. If not, it
returns 100 (a placeholder for “not filtered”).
The MIN function finds the shallowest level being filtered. This is useful for supporting
negative or ignore filters (like “exclude this account”).
5. After you’ve created your BrowseDepth, RowDepth and MinFilterDepth, you need to
create one measure (Sum Amount) for the values table.
See below for an example of the Sum Amount measure:
1. Sum Amount
Sum Amount = SUM ( 'values'[[Values]]] ) 05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 12/22

Sum Amount totals the numbers in the [Values] column of the 'values' table. This is the
base number used in the Rollup Value calculation.
6. Next, you will build your Rollup Value. It will be used to show a total or summary amount,
but only when certain conditions are met. It also adjusts how it calculates that total
depending on how deeply someone is exploring the data.
Select 2 dimensions to support negative ( - ) and ignore (~) operators.
In the example below, the 2 dimensions are Account and Measure.
In CombinedDepth = (AccountDepth - 1) * 4 + MeasureDepth the multiplied number is the
depth of the second dimension (in this case, * 4 for MeasureDepth)
The switch will have the depths of the dimensions multiplied (in this case, 8 for
AccountDepth X 4 for MeasureDepth = 32 total)
Rollup Value =
VAR AccountDepth = COALESCE( [AccountBrowseDepth], [AccountMinFilterDepth], 1 )
VAR MeasureDepth = COALESCE( [MeasureBrowseDepth], [MeasureMinFilterDepth], 1 )
VAR AccountShowRow = [AccountBrowseDepth] <= [AccountRowDepth]
VAR MeasureShowRow = [MeasureBrowseDepth] <= [MeasureRowDepth]
VAR EntityShowRow = [EntityBrowseDepth] <= [EntityRowDepth]
VAR DepartmentShowRow = [DepartmentBrowseDepth] <= [DepartmentRowDepth]
VAR YearShowRow = [YearBrowseDepth] <= [YearRowDepth]
VAR PeriodShowRow = [PeriodBrowseDepth] <= [PeriodRowDepth]
VAR ScenarioShowRow = [ScenarioBrowseDepth] <= [ScenarioRowDepth]
VAR CurrencyShowRow = [CurrencyBrowseDepth] <= [CurrencyRowDepth]
VAR Result =
IF (AccountShowRow && CurrencyShowRow && DepartmentShowRow && EntityShowRow && Measure
 SWITCH (
  AccountDepth,
1,
 SWITCH(
  MeasureDepth,  05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 13/22

   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel1] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel1] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel1] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel1] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel1] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel1] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel1] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel1] *
'Measure'[Measure_signToLevel4])
 ),
2,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel2] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel2] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel2] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel2] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel2] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel2] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel2] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel2] *
'Measure'[Measure_signToLevel4])
 ),
3,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel3] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel3] *
'Measure'[Measure_signToLevel1]),05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 14/22

   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel3] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel3] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel3] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel3] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel3] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel3] *
'Measure'[Measure_signToLevel4])
 ),
4,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel4] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel4] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel4] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel4] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel4] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel4] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel4] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel4] *
'Measure'[Measure_signToLevel4])
 ),
5,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel5] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel5] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel5] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel5] *
'Measure'[Measure_signToLevel2]),05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 15/22

   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel5] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel5] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel5] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel5] *
'Measure'[Measure_signToLevel4])
 ),
6,
 SWITCH(
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel6] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel6] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel6] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel6] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel6] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel6] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel6] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel6] *
'Measure'[Measure_signToLevel4])
  ),
7,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel7] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel7] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel7] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel7] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel7] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel7] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel7] ), VALUES (05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 16/22

'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel7] *
'Measure'[Measure_signToLevel4])
 ),
8,
 SWITCH(
  MeasureDepth,
   1, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel8] ), VALUES (
'Measure'[Measure_signToLevel1] ) ), [Sum Amount] * Account[Account_signToLevel8] *
'Measure'[Measure_signToLevel1]),
   2, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel8] ), VALUES (
'Measure'[Measure_signToLevel2] ) ), [Sum Amount] * Account[Account_signToLevel8] *
'Measure'[Measure_signToLevel2]),
   3, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel8] ), VALUES (
'Measure'[Measure_signToLevel3] ) ), [Sum Amount] * Account[Account_signToLevel8] *
'Measure'[Measure_signToLevel3]),
   4, SUMX (CROSSJOIN ( VALUES ( Account[Account_signToLevel8] ), VALUES (
'Measure'[Measure_signToLevel4] ) ), [Sum Amount] * Account[Account_signToLevel8] *
'Measure'[Measure_signToLevel4])
  )
 )
)
RETURN
 Result
If you do not see “Account_signToLevel1” in the data pane, follow the instructions in this05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 17/22

article.
7. Once you have finished building your operator measures, you can graph and chart using
the new operators. In the screenshot below, the user has created hierarchies to view all
levels at once.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 18/22

8. Add a measure filter to Filter on all pages for the level that the “Value” member is on in
Vena. This will be for the whole report.05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 19/22

Notes and limitations05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 20/22

We recommend that you only use operators in 1 or 2 dimensions. Any more than that and
the DAX code will significantly slow down the performance of the Power BI software.
Was this article helpful?
1 out of 1 found this helpful
Related articles
How-To: Use Power BI Connector
Reference: Writing Expressions (MQL & HQL)
Explainer: Power BI Connector Member
Aliases
Vena Insights Series (Part 4) - Managing
Calculations: Measures, Calculated Tables &
Columns
Vena Insights Series (Part 2) - Building
Dashboards With Vena InsightsRecently viewed articles
How-To: Use Power BI Connector
Troubleshooting: Power Automate Flow Error
Automated Template X Not Found
How-To: Exporting Data from Vena With
Power Automate Connector
How-To: Importing Data to Vena with
Microsoft Power Automate Connector
Troubleshooting: QuickBooks Data Feed
Column Names Not Working in Data Feed05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 21/22

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:40 How-To: Visualizing Data in the Power BI Connector on Desktop by Creating a Rollup Value Measure – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4406377020173-How-To-Visualizing-Data-in-the-Power-BI-Connector-on-Desktop-by-Creating-a-Rollup-Value-Measure 22/22
