# (How To)   Installing the Vena Suite Bundle for NetSuite

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/NetSuite Integration Search
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
ETL JobsHow-To: Installing the Vena Suite
Bundle for NetSuite
Perform Transaction Saved Searches and integrate data quickly and seamlessly with
the Vena Suite Bundle for NetSuite.
Laura Harris
Updated 1 month ago
05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 1/14

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
Reference: NetSuite Saved
Searches Configuration for
Different Use Cases and the
Role for the Vena Connector
How-To: Setting Up a NetSuite
Connector and Data Feed
How-To: Use the New RESTlet
for NetSuite
How-To: Installing the Vena
Suite Bundle for NetSuite
Explainer: Updating the Vena
Suite Bundle for NetSuite
Troubleshooting: Error
Receiving Data from NetSuite
Invalid Login Attempt
Troubleshooting: NetSuite Error
Caused By Not Having RequiredWhy use this feature?
The new Vena Suite Bundles provides users with the ability to easily install components that
make connecting to NetSuite and querying data easier.  The Suite Bundles provide the users
with a RESTlet that may be used to pull data from NetSuite, a transaction Saved Search template
that is a great starting point for what data to bring in and a role that allows users to connect to
NetSuite easily. This customization is seamlessly carried forward with NetSuite version
upgrades.
Before you begin
You must have Modeler access to set up Connectors in vena.io. Additionally, you must be an
Administrator of the NetSuite account to which you want to install the Suite Bundles.
Table of contents
Info
The Vena Suite Bundles for NetSuite have been updated. All tenants must have:
Vena (1) - Saved Searches and Roles (Bundle ID 315383) updated to version
v1.11
Vena (2) – RESTlets (Bundle ID 315424), updated to version v1.1
As part of this update, Consumer Key and Consumer Secret details are no longer
required.05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 2/14

Permission
Troubleshooting: NetSuite Has
Encountered an Error: "null"
During ETL
Troubleshooting: NetSuite
Script Execution Time Exceeded
Troubleshooting: NetSuite An
nlobjSearchFilter Contains an
Invalid Operator
Troubleshooting: Error
Receiving Data from NetSuite:
java.lang.Exception: An
Unexpected Error Has
Occurred
Troubleshooting: Error
Receiving Data from NetSuite:
NetSuite Encountered an
Unexpected Error
QuickBooks Integration
Power Automate
Integration
Power BI Integration
Sage Intacct Integration
Salesforce IntegrationHow to
Locate the Vena Suite Bundle
Modify the Saved Search
Notes & Limitations
How to
Locate the Suite Bundle
1. Log into NetSuite using your NetSuite Admin credentials.05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 3/14

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
Name
Admin
Vena Ad Hoc2. Navigate to Customization →  SuiteBundler →  Search & Install Bundles > List.
3. On the Search & Install Bundles page, search for “Vena Solutions”. The two Vena Suite
Bundles should appear.05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 4/14

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
4. Install both Vena(1) and Vena(2) by clicking on the blue hyperlinks.
05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 5/14

Vena (1) Saved Searches and Roles:
This includes a Transaction Saved Search and role.  The Transaction Saved Search
contains all of the fields that most of our clients need to bring in from NetSuite but it is
easy to adjust if you need more.  You do not need to use this saved search, you can use
your own, but you will have to use the Generic RESTlet and customized data feed flow.
See the "Saved Search Fields - NetSuite" Excel workbook attached to this article to view
the fields that are included in the saved search.
The role contains permissions that most clients need but may need to be adjusted.  You
can also create your own role from scratch and assign that to the account you are using to
connect to Vena.  If you change the fields you are requesting in the saved search it is more
likely that you could get an error when getting data from NetSuite and will need to adjust
the permissions in your role. See the "Permissions - NetSuite" Excel workbook attached to05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 6/14

this article to view the permissions that are included.
Vena (2) RESTlets Bundle
The RESTlet bundle contains two RESTlets.  The first RESTlet is called
venaNetSuiteUniqueKeyRestlet and can only be used for Transaction Saved Searches.
It is much faster than the other one because you can search for batches based on a
unique ID that Netsuite provides.
The second RESTlet is called the Vena Generic RESTlet script and can be used for any
type of saved search including a Transaction Saved Search. 05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 7/14

5. Wait until the installation is complete on both bundles before moving onto the next step.
Modify the Saved Search
1. Once the installation has finished, navigate to NetSuite > Reports > Saved Searches to locate
the saved search that was installed by the Suite Bundle and modify it to add any Line Unique
Key. Do not modify the sort order or existing fields. However, you can add additional fields
and filters if desired.
Caution_Icon_Small.png Caution
When updating or  reinstall ing the V ena (1) package after initial  installation, you run the
risk of overwriting the saved search/role.  To mitigate this risk, create a copy of your
changes  to the search or the role before updating the bundle (refer to the  screenshot
below for the area that should remain un-edited. ) 05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 8/14

05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 9/14

05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 10/14

2. Locate the file titled “Vena Transactions Search” and click Edit.
3. Adjust the search filters as needed.
05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 11/14

4. If you choose to add fields, be sure to add them to the bottom.
5. Once you have downloaded the Vena Suite Bundles and modified your search as needed, you
can move on to creating a NetSuite Data Feed in Vena. Learn more about setting up a
NetSuite Connector and Data Feed.
Notes & Limitations
Performance improvement for speed only applies to Transaction Saved Searches. (e.g
searches created using the NetSuite Suite Bundle.
If you need different data than that which would be brought in via the Transaction Saved
Search, then you can use the old way (Generic RESTlet).
If you need two separate Transactions Saved Searches, you have to use the Generic RESTlet.
To get P0 for Balance Sheet it’s best to load by CSV or you can make another saved search
with ‘Group By’ and ‘Sum’ and use the generic RESTlet.05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 12/14

The Saved Search needs to be ordered and added fields should be added to the bottom.
Permissions - NetSuite.xlsx20 KB
Saved Search Fields - NetSuite 2020.xlsx7 KB
Was this article helpful?
4 out of 4 found this helpful
Related articles
How-To: Setting Up a NetSuite Connector and
Data Feed
How-To: Use the New RESTlet for NetSuite
Explainer: Updating the Vena Suite Bundle for
NetSuiteRecently viewed articles
How-To: Use the New RESTlet for NetSuite
How-To: Setting Up a NetSuite Connector and
Data Feed
Reference: NetSuite Saved Searches
Configuration for Different Use Cases and the
Role for the Vena Connector05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 13/14

Reference: NetSuite Saved Searches
Configuration for Different Use Cases and the
Role for the Vena Connector
How-To: Getting Vena 365 for Windows or
Installing Vena DesktopTroubleshooting: The Record in Table Vena
Trial Balance Buffer Already Exists.
Identification Fields and Values
Troubleshooting: Vena Data Feed Not
Connecting to Business Central Extension
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:27 How-To: Installing the Vena Suite Bundle for NetSuite – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360038725592-How-To-Installing-the-Vena-Suite-Bundle-for-NetSuite 14/14
