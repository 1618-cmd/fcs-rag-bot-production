# (API Notebook)   Integration via Microsoft Fabric – Vena & SAP S 4HANA

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
ETL Jobs
Data Querying
Vena Tables
Microsoft Fabric
IntegrationAPI Notebook: Integration via Microsoft Fabric –
Vena & SAP S/4HANA
What this notebook does
This notebook describes how to retrieve SAP S/4HANA data via the OData v4 API. It's designed to:
Connect securely using Azure Key Vault for API keys.
Access and extract data from the SalesOrder endpoint.
Handle pagination via @odata.nextLink.
Save the results to the Fabric Lakehouse.
Vena Support Team
Updated 4 months ago
02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38927804963213-API-Notebook-Integration-via-Microsoft-Fabric-Vena-SAP-S-4HANA 1/5

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
Deltek Vantagepoint
Business Central
Integration
NetSuite Integration
QuickBooks Integration
Power Automate
Integration
Power BI Integration
Sage Intacct Integration
Salesforce IntegrationHow we connect to SAP/4HANA
Vena uses the SAP OData v4 APIs available through SAP API Business Hub.
Example: For Sales Orders, the reference is: Sales Order (A2X) API - SAP API Hub
SAP OData APIs expose business entities (like Sales Orders, Business Partners, GL Items) in a RESTful format, suitable for
direct integration with analytics and data platforms like Fabric.
Required setup
1. Setup of Azure key vault.
2. Update vault_url in the script.
3. Modify the URL1 variable to terget a new SAP API endpoint.
4. Optionally extend the script to process multiple endpoints.
Configuration: Key Vault + API Setup
Before running this notebook:
1. Provision an Azure key vault
This secures your SAP API key.
The name of the key vault will be used in the vault_url.
2. Add a secret to your key vault
Secret name: SAP-APIkey
Value: Your SAP API Business Hub API key or customer-specific SAP API key if connecting to a private tenant.02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38927804963213-API-Notebook-Integration-via-Microsoft-Fabric-Vena-SAP-S-4HANA 2/5

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
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPointThe notebook retrieves the key securely using mssparkutils.credentials.getSecret().
3. Set this variable in the script:
vault_url = "https://<your-key-vault-name>.vault.azure.net/"
This secures your SAP API key.
Changing the API endpoint
By default, this script pulls from the SalesOrder entity. To extract data from a different endpoint:
Update the url1 value:
url1 = "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata4/sap/api_<object>/srvd_a2x/sap/<object>/0001"
For example, to pull Business Partners:
url1 =
"https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata4/sap/api_business_partner/srvd_a2x/sap/businesspartner/0001"
Make sure to verify the object name from the SAP API Hub.
Pulling from multiple endpoints
To pull from multiple SAP OData entities, you can:
1. Duplicate the request block (starting from response1 = requests.get(...)) for each new endpoint, or
2. Restructure the script to loop over a list of endpoint base URLs, like this:02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38927804963213-API-Notebook-Integration-via-Microsoft-Fabric-Vena-SAP-S-4HANA 3/5

Vena Copilot
Product Updatesendpoints = {
    "salesOrder": "api_salesorder/srvd_a2x/sap/salesorder",
    "businessPartner": "api_business_partner/srvd_a2x/sap/businesspartner" }
And iterate through endpoints.items() to process each one.
Known SAP Odata limitations
Not all data entities in SAP S/4HANA are exposed through the OData APIs.
Many APIs return paged results, often limited to 100–1,000 records per call.
OData does not support complex joins (e.g., Sales Order Header + Items in one call).
Some modules (like Controlling, Payroll) or custom fields may not be available unless exposed via custom CDS Views.
Not all APIs support delta queries or change tracking natively.
In these cases, you may need to ask your SAP admin to expose a custom OData service or extract via an alternate method
(e.g., CDS, SLT, or SAP Integration Suite).
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
API Notebook: Integration via Microsoft Fabric – Vena & Xero
How-To: Configuring Fabric Data Factory for Vena Integration02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38927804963213-API-Notebook-Integration-via-Microsoft-Fabric-Vena-SAP-S-4HANA 4/5

How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric
Explainer: Vena Fabric Integration
How-To: Managing and Deleting Data Using Vena Tables
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38927804963213-API-Notebook-Integration-via-Microsoft-Fabric-Vena-SAP-S-4HANA 5/5
