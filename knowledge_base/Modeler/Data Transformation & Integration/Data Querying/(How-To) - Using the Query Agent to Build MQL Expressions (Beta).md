# (How To)   Using the Query Agent to Build MQL Expressions (Beta)

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Data Querying Search
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
ETL JobsHow-To: Using the Query Agent to
Build MQL Expressions (Beta)
Laura Harris
Updated 1 month ago
Note
This feature is currently in beta and is not generally available. If you want to
participate in the beta, please reach out to your Account Manager.
02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 1/9

Data Querying
How-To: Using the Query Agent
to Build MQL Expressions (Beta)
Reference: Writing Expressions
(MQL & HQL)
Reference: Using Wildcard in
Model Slice Expression
Troubleshooting: ETL Export
MQL Query Returning No Data
How-To: Creating Advanced
Integration Setups With VenaQL
Troubleshooting: MQL Invalid
Expression Syntax When
Creating a Calculated Member
Troubleshooting: ETL Error
Guide
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite IntegrationWhy use this feature?
Use Vena’s Query Agent to generate MQL expressions using plain language. Write a prompt
specifying what slice of data you want to retrieve and Vena will generate an MQL expression that
references precise members in your data models. Once generated, copy and paste the
expression to use in ETL exports, create scopes in channels and more.
Eliminate the need to manually filter large exports and save up to 10 minutes per query by
defining exactly what you’re looking for in plain language – no coding required.
Before you begin
You need to have at least Modeler access in Vena. You will also need Read Application
Permissions for the data model.
You will also need to accept the AI Product Terms & Conditions if you have not already. Once
accepted, all users with the necessary access and permissions can access the feature.
02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 2/9

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
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten orHow to
Use plain, conversational language to generate accurate MQL expressions.
Create an export query
1. Navigate to the Modelertab.
2. Select Data Modeler and then select Export from the sidebar.
3. Select the Learn More arrow.
4. The Query Agent chat will open on a split screen.
5. The Query Agent opens with a preliminary greeting and an example of how to ask the agent
for specific queries or slices of data you may be interested in generating expressions for.02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 3/9

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
Product Updates
6. Use plain language to describe what you’re looking for. In the following example, the user
asks the Query Agent to “write an export query for the full year 2021 budget for all entities
except undefined.”02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 4/9

The Query Agent will display the MQL expression.
7. Review the expression and use the Copy icon to copy the MQL expression.
02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 5/9

8. Paste your query in the field underExport if following condition is true.
Sample queries
9. Plain language query MQL response02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 6/9

Export all my net income
and balance sheet accounts.Dimension(‘Account’:union(bottomlevel(‘NetIncome’)
bottomlevel(‘Balance Sheet’)))
All department minus
subgroup.Dimension(‘Department’:subtract((bottomlevel(‘All
Departments’)bottomlevel(‘Sub Group’)))
I want to export all my
Actual data.Dimension(‘Scenario’:’Actual’)
Export all entities with ‘Fun
Dept’ attribute.Dimension(‘Entity’:intersection(bottomlevel (‘All
Entities’)attribute(@‘Fun Dept’)))
Notes & limitations
If you exit the Query Agent window, you will lose your chat history.
Query Agent is only available in the ETL Export page for the beta.
You don’t need a Vena Copilot license to access the Vena Query Agent.
You canexport different data types by pasting the query and using the dropdown menu
under Choose what you would like to exportto switch fromValues to other export types, such
as Hierarchy or Line Item Details.
02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 7/9

Query Agent requires Data Permissions to be ON in your environment.
Query Agent beta will be rolled out in stages.If you don’t currently see Query Agent and are
interested in accessing the feature, reach out to your Account Manager.
To disable Query Agent, reach out to Vena Support.
Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Writing Expressions (MQL & HQL)
How-To: Configuring Fabric Data Factory for
Vena Integration
How-To: Creating and Managing Data
Permissions
What's New in Vena: Summer '25 Release
How-To: Installing the Vena Suite Bundle for
NetSuiteRecently viewed articles
How-To: Checking the ETL Tool Version
How-To: Setting up Email Notifications for ETL
Jobs
How-To: Maintaining Dimension Member IDs
When Updating Existing Members
How-To: Use Clear Slices to Clear
Intersections During an ETL Load
How-To: Exporting CSV Files for ETL Job02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:49 How-To: Using the Query Agent to Build MQL Expressions (Beta) – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38480612756621-How-To-Using-the-Query-Agent-to-Build-MQL-Expressions-Beta 9/9
