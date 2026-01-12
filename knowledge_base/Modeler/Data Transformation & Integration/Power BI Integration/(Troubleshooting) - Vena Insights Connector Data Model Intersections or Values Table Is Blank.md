# (Troubleshooting)   Vena Insights Connector Data Model Intersections or Values Table Is Blank

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
ETL JobsTroubleshooting: Vena Insights
Connector Data Model Intersections
or Values Table Is Blank
Issue summary
When working with your Vena data models in the Vena Insights desktop application, you may
notice the intersection or values table is blank or empty.
Olalekan Adebayo
Updated 1 year ago
05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 1/6

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
Connector Table Relationship Is
Suggested solution 1
Option 1
1. Check and confirm that the required data permission is enabled in your environment.
2. If data permission is enabled and the application token was taken from the Admin tab (i.e.
Admin > Application Tokens), make sure the necessary data permission has been configured.
In the example below, you can see that no data permission is configured yet.
3. Select Add Permission and add the necessary permission to the appropriate data models.
4. Refresh the connection in Vena Insights Connector.05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 2/6

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
Connect to Vena InsightsOption 2
1. Confirm that data permission is enabled in your environment.
2. If the application token was taken from a user's profile, this will inherit the user's data
permission in Vena.
3. Since the user's data permission will be inherited, inform your Vena Admin and ask them to
ensure that the affected user's user group has the necessary data permission to the
appropriate data models.
They can check this by following these steps:
a. Navigate to the Admin tab.
b. Select the Permissions page.
c. Find the user group.
d. Select View/Edit on Data Permissions.05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 3/6

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
Namee. Review and update as required.
4. Once updated, the affected user can refresh the connection in Vena Insights Connector.
Cause
This may happen if the application token that was used to establish the connection to Vena does
not have the necessary data permission in an environment where data permission is enabled.
Keywords
power bi connector values table blank, blank or empty intersections in power bi, power bi
Was this article helpful?05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 4/6

Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates0 out of 0 found this helpful
Recently viewed articles
Troubleshooting: Vena Insights Connector Load and Transform Data Buttons Grayed Out
Troubleshooting: Vena Insights Connector Users Able To See Data Models They Don’t Have
Access To
Troubleshooting: Vena Insights Connector Failed to Update Data Source Credentials
Troubleshooting: Vena Insights Connector SigntoLevel Column Not Available
Troubleshooting: Vena Insights Connector Invalid Application Token Provided
Didn't find what you're looking for?
Our application support team is ready to help.05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 5/6

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request05/01/2026, 12:44 Troubleshooting: Vena Insights Connector Data Model Intersections or Values Table Is Blank – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/15620873786893-Troubleshooting-Vena-Insights-Connector-Data-Model-Intersections-or-Values-Table-Is-Blank 6/6
