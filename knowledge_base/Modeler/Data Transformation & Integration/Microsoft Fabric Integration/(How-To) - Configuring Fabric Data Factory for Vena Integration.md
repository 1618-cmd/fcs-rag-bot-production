# (How To)   Configuring Fabric Data Factory for Vena Integration

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Microsoft Fabric Integration Search
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
ETL JobsHow-To: Configuring Fabric Data
Factory for Vena Integration
This article helps ensure you are prepared for Vena-assisted integration with Fabric
Data Factory.
Why use this feature?
Vena Support Team
Updated 4 months ago02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 1/10

Data Querying
Vena Tables
Microsoft Fabric
Integration
Explainer: Vena Fabric
Integration
How-To: Integrating Dynamics
365 F&O Integration with Vena
Via Microsoft Fabric
How-To: Configuring Fabric
Data Factory for Vena
Integration
API Notebook: Integration via
Microsoft Fabric – Vena & Xero
API Notebook: Integration via
Microsoft Fabric – Vena & SAP
S/4HANA
API Notebook: Integration via
Microsoft Fabric – Vena &
Acumatica
API Notebook: Integration via
Microsoft Fabric - Vena &
Deltek VantagepointThis article offers a clear, step-by-step guide to setting up your Microsoft Fabric Data Factory
environment. Once you have Fabric established, your Account Manager will assist with the Vena
integration.
To ensure a smooth process, you can configure Microsoft Fabric before meeting with Vena. This
guide explains how to purchase necessary Microsoft services, details essential setup steps and
shares security and integration best practices.
Before you begin
To follow the instructions in this article, you need an Azure subscription with one of the
following roles: Owner role, Reservation Purchaser or Reservation Owner. To move forward
with Vena Integration, you must have at least Modeler access.
Table of contents
How to
Purchasing Microsoft Fabric
Enabling Microsoft Fabric
Configuring Fabric tenant settings
Configuring a Fabric Data Factory workspace for integrating with Vena
Inviting a Vena consultant to your Azure tenant02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 2/10

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
DestinationsHow to
Purchasing Microsoft Fabric
Contact Microsoft for help getting started with Microsoft Fabric.
Learn more about Microsoft Fabric stock keeping units.
When purchasing Fabric, keep the following in mind:
1. Capacity
Vena recommends purchasing an F2 capacity if you expect to send and receive average
amounts of data from Vena.
For other scenarios, review Microsoft’s guidance on pricing for data capacities in Fabric.
You may set up a trial to test usage and performance, but note that the trial account
utilizes an F64 Fabric capacity, which has higher capabilities and costs compared to what
may be necessary for integration with Vena.
2. Payment models
Microsoft offers two payment models:
1. Pay As You Go pricing – Recommended for most customers just starting out, as you
only pay for what you use. You can also pause the capacity when it is not being used.
Note
Skip this step if you already have a Microsoft Fabric Capacity SKU or a Power BI
Premium subscription.
02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 3/10

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
Product UpdatesLearn more about Fabric pay-as-you-go pricing.
2. Reserved capacity pricing – For those customers with regularly scheduled pipelines
running. You ‘reserve’ capacity ahead of time at a lower monthly cost, but you must
fulfill that cost whether you use the full capacity or not.
Vena also recommends scheduling pause and resume for capacities to reduce usage
costs. Learn more about pausing and resuming capacity in Microsoft Fabric.
Alternatively, here is Microsoft’s guidance:
To gain access to Microsoft Fabric you have three paths.
1. Leverage your existing Power BI Premium subscription by turning on the Fabric
preview switch. All Power BI Premium capacities are instantly capable of powering all
the Fabric workloads with no additional action required.
2. Start a Fabric trial if your tenant supports trials.Learn more about starting a
Microsoft Fabric trial.
3. Purchase a Fabric pay-as-you-go capacity from the Azure portal.Learn more about
purchase a Fabric subscription.
For additional information, check out Microsoft’s announcement on Microsoft Fabric
capacities available for purchase.
Enabling Microsoft Fabric
Follow Microsoft’s instructions to enable Microsoft Fabric in this article.
Configuring Fabric tenant settings
Set the following tenant settings for the Fabric administrator user role established above.
1. Users can create Fabric items.
2. Enable granular access control for all data connections.02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 4/10

Learn more about Microsoft Fabric tenant settings.
Configuring a Fabric Data Factory workspace for
integrating with Vena
As you follow the steps below to configure your Fabric Data Factory workspace, refer to
Microsoft’s documentation on administrating Microsoft Fabric for further guidance. We also
recommend familiarizing yourself with security concepts in Fabric and following Microsoft’s
security baseline.
Step 1: Create a workspace.
Follow these instructions to set up a workspace in Fabric Data Factory.
Step 2: Create a connection between Fabric Data Factory and the source system.
1. Generate an appropriate token for accessing the public API(s) of your source system by
following its documentation.
Vena recommends providing the minimum access necessary to facilitate the integration
with Vena with this API token. For example, if data will only flow one way from the source
system to Vena, then restrict the token for the source system to allow only for data
export.
2. Sign in to Microsoft Fabric and navigate to Settings by selecting the gear icon (
) in the
header.
3. Select Manage connections and gateways.
4. Select New to open the panel for creating a new connection.02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 5/10

5. Select Cloud.
6. Name the connection (e.g. Great Plains GL export)
7. Select Web v2 for connection type.
8. Set up the appropriate base URL for the source system.
9. Select the appropriate authentication method.
10. Set the Privacy level to None.
11. Select Create.
Step 3: Create a connection between Fabric Data Factory and Vena.
1. Generate an appropriate token for accessing Vena by following Vena’s API documentation.
Vena recommends providing the minimum access necessary to facilitate the integration
with Vena with this API token. For example, if data will only flow one way from the source
system to Vena, then restrict the token for Vena to allow only for data import.
2. Sign in to Microsoft Fabric and navigate to Settings by selecting the gear icon (
) in the
header.
3. Select Manage connections and gateways.
4. Select New to open the panel for creating a new connection.
5. Select Cloud.
6. Name the connection (e.g. Vena GL import).
7. Select Web v2 as the connection type.
8. Set up the appropriate base URL for Vena.
The format of this URL for Vena will be https://{hub}.vena.io/api/public/v1/ where the {hub}
parameter is your region.
9. Select Basic as the authentication method.
10. Enter your apiUser and apiKey as the username and password.
11. Set the Privacy level to None.
12. Select Create.02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 6/10

Inviting a Vena consultant to your Azure tenant
Step 1: Create a new user.
1. In your Microsoft Azure Portal, select Manage Microsoft Entra ID.
2. Navigate to the Users page and select New user > Create new user drop-down menu
(Note: external users are unable to use the Fabric feature).
3. Create an email for Vena consultants, a display name and optionally add them to a security
group under the Assignments tab.
4. Save the username and password.
5. Select Review + create, then select Create.
6. Securely send the username and password to your Vena consultant to allow them to login to
the tenant.02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 7/10

Step 2: Invite a Vena consultant to your Fabric Data Factory workspace.
1. Select Manage Access within the workspace you created.
2. Select Add people or groups.
3. Search for the Vena consultant by name or email, then select.
4. Select Viewer to open the drop-down menu for role selection, then select Contributor.
5. Select Add to invite the user.
Step 3: Invite a Vena consultant to use the connections you set up.
1. In Fabric, navigate to Settings > Manage connections and gateways.
2. Highlight the appropriate connection, then select the ellipses (...) next to the Connection Type.
3. Select Manage users.
4. Search for the Vena consultant by name or email.
5. Select the consultant’s name from the drop-down menu.
6. Select the consultant from the “New users” section.
7. Select User as the permission level.
8. Select Share.
9. The workspace is now ready for the Vena consultant to begin implementing the integration!
Note
Complete this step for both the source system connection and the Vena
connection.02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 8/10

Step 4: Deactivate the Vena consultant’s Azure access
Once the integration is complete and ready for use, deactivate the Vena consultant’s access
to your Azure tenant.
Was this article helpful?
0 out of 0 found this helpful
Related articles
API Notebook: Integration via Microsoft Fabric
– Vena & Xero
API Notebook: Integration via Microsoft Fabric
– Vena & SAP S/4HANA
How-To: Use Power BI Connector
How-To: Map a Process Variable to a
Template (Vena 365 Only)
API Notebook: Integration via Microsoft Fabric
- Vena & Deltek VantagepointRecently viewed articles
How-To: Integrating Dynamics 365 F&O
Integration with Vena Via Microsoft Fabric
Explainer: Vena Fabric Integration
How-To: Managing and Deleting Data Using
Vena Tables
How-To: Exporting Data From a Vena Table
Explainer: Set Staging or Transactions Tables
When Building a Vena Table02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:57 How-To: Configuring Fabric Data Factory for Vena Integration – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38583648823693-How-To-Configuring-Fabric-Data-Factory-for-Vena-Integration 10/10
