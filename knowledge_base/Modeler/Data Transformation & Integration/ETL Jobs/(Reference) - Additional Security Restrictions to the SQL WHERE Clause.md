# (Reference)   Additional Security Restrictions to the SQL WHERE Clause

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/ETL Jobs Search
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
ETL Jobs
ETL Job Errors &Reference: Additional Security
Restrictions to the SQL WHERE Clause
Refer to this article for a list of accepted SQL functions in your “where”
clauses.
Overview
As part of our data security initiative, we are hardening all our endpoints that allow you to specify your
own "where" clause. This includes: Hierarchy exports (HQL), Attribute exports (HQL) and staging
Vena Support Team
Updated 1 year ago
02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 1/6

Troubleshooting
Reference: ETL Guide - 1 -
Overview
Reference: ETL Guide - 2 -
Vena.io ETL
Reference: ETL Guide - 3 -
Command Line ETL
Reference: ETL Guide - 4 -
Query Languages
Reference: ETL Guide - 5 - SQL
Staging Environment
Reference: ETL Guide - 6- Using
Staging Data
How-To: Exporting Data From a
SQL Staging Table
How-To: Create and Manage a
Data Model Hierarchy Using
ETL Import
How-To: Exporting a Subset of
Data From Your Data Model or
Cube
Reference: Additional Security
Restrictions to the SQL WHERE
Clause
Explainer: ETL Export Featurequeries.
Reference Guide
Vena has restricted the usable SQL functions and only the allow-listed SQL functions can be used.
Please make sure you replace/remove functions that are not part of the following list:
"ABS"
"ACOS"
"ADDDATE"
"ADDTIME"
"AND"
"ASCII"
"AVG"
"BETWEEN"
"BIT_AND"
"BIT_COUNT"
"BIT_LENGTH"
"BIT_OR"
"BIT_XOR"
"CAST""DATETIMEOFFSETFROMPARTS"
"SMALLDATETIMEFROMPARTS"
"DENSE_RANK"
"TIMEFROMPARTS"
"DAY"
"DAYNAME"
"DAYOFMONTH"
"DAYOFWEEK"
"DAYOFYEAR"
"DIV"
"ELT"
"EXP"
"EXPORT_SET"
"EXTRACT""LTRIM"
"MAKE_SET"
"MAKEDATE"
"MAKETIME"
"MAX"
"MID"
"MIN"
"MINUTE"
"MOD"
"MONTH"
"MONTHNAME"
"NOT"
"NOW"
"NCHAR""STR_TO_DATE"
"STRCMP"
"SUBDATE"
"SUBSTR"
"SUBSTRING_INDEX"
"SUBSTRING"
"SUBTIME"
"SUM"
"TIME_FORMAT"
"TIME_TO_SEC"
"TIME"
"TIMEDIFF"
"TIMESTAMP"
"TIMESTAMPADD"02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 2/6

Updates
How-To: Scheduling Ongoing
ETL Jobs at Exact Times Using
Command-Line ETL
How-To: Automatically Run ETL
Templates Using the ETL
Scheduler
How-To: Checking if My File Has
a Header Row or Not
How-To: Exporting CSV Files for
ETL Job
How-To: Use Clear Slices to
Clear Intersections During an
ETL Load
How-To: Maintaining
Dimension Member IDs When
Updating Existing Members
How-To: Setting up Email
Notifications for ETL Jobs
How-To: Checking the ETL Tool
Version
Data Querying
Vena Tables
Microsoft Fabric
Integration"CEIL"
"CEILING"
"CHAR_LENGTH"
"CHAR"
"CHARINDEX"
"CHARACTER_LENGTH"
"COALESCE"
"CONCAT"
"CONV"
"CONVERT_TZ"
"CONVERT"
"COUNT"
"CURDATE"
"CURRENT_DATE"
"CURRENT_TIME"
"CURRENT_TIMESTAMP"
"CURTIME"
"DATALENGTH"
"DATE_ADD"
"DATE_FORMAT""FIELD"
"FIND_IN_SET"
"FLOOR"
"FORMAT"
"FROM_BASE64"
"FROM_DAYS"
"FROM_UNIXTIME"
"GETDATE"
"GETUTCDATE"
"GREATEST"
"GROUP_CONCAT"
"HOUR"
"IF"
"IFNULL"
"IN"
"INSERT"
"INSTR"
"INTERVAL"
"IS"
"ISDATE""NULLIF"
"NTILE"
"ORD"
"PARSE"
"PERIOD_ADD"
"PERIOD_DIFF"
"POSITION"
"POW"
"POWER"
"PATINDEX"
"QUARTER"
"QUOTENAME"
"RANK"
"REPEAT"
"REPLACE"
"REVERSE"
"RIGHT"
"RLIKE"
"ROUND"
"RPAD""TIMESTAMPDIFF"
"TO_DAYS"
"TO_SECONDS"
"TRIM"
"TRUNCATE"
"UCASE"
"UNIX_TIMESTAMP"
"UPPER"
"UTC_DATE"
"UTC_TIME"
"UTC_TIMESTAMP"
"VAR_POP"
"VAR_SAMP"
"VARIANCE"
"WEEK"
"WEEKDAY"
"WEEKOFYEAR"
"WEIGHT_STRING"
"XOR"
"YEAR"02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 3/6

Business Central
Integration
NetSuite Integration
QuickBooks Integration
Power Automate
Integration
Power BI Integration
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
Destinations"DATE_SUB"
"DATE"
"DATEDIFF"
"DATENAME"
"DATEPART"
"DATEADD"
"DIFFERENCE"
"EOMONTH"
"SWITCHOFFSET"
"TODATETIMEOFFSET"
"DATEFROMPARTS"
"DATETIME2FROMPARTS"
"DATETIMEFROMPARTS""ISNULL"
"LAST_DAY"
"LCASE"
"LEAST"
"LEFT"
"LENGTH"
"LEN"
"LIKE"
"LOCATE"
"LOCALTIME"
"LOCALTIMESTAMP"
"LOWER"
"LPAD""RTRIM"
"SEC_TO_TIME"
"SECOND"
"SPACE"
"SQRT"
"SQUARE"
"SOUNDEX"
"STD"
"STR"
"STUFF"
"STDDEV_POP"
"STDDEV_SAMP"
"STDDEV""YEARWEEK"
Was this article helpful?02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 4/6

How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map by
Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates1 out of 1 found this helpful
Recently viewed articles
How-To: Exporting a Subset of Data From Your Data Model or Cube
How-To: Create and Manage a Data Model Hierarchy Using ETL Import
How-To: Exporting Data From a SQL Staging Table
Reference: ETL Guide - 6- Using Staging Data
Reference: ETL Guide - 5 - SQL Staging Environment
Didn't find what you're looking for?02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 16:44 Reference: Additional Security Restrictions to the SQL WHERE Clause – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/206535003-Reference-Additional-Security-Restrictions-to-the-SQL-WHERE-Clause 6/6
