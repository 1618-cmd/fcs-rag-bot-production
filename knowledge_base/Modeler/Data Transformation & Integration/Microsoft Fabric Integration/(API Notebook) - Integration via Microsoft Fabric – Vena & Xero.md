# (API Notebook)   Integration via Microsoft Fabric – Vena & Xero

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
ETL JobsAPI Notebook: Integration via
Microsoft Fabric – Vena & Xero
What this notebook does
This notebook describes how to retrieve accounting data from Xero via the Xero API. It's
designed to:
Connect securely to Xero using Azure Key Vault for API credentials.
Vena Support Team
Updated 2 months ago
02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 1/7

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
Deltek VantagepointAuthenticate via Xero’s client credentials OAuth2 flow.
Extract journals from Xero’s accounting dataset.
Flatten nested journal line data into a tabular structure.
Save the results as a Delta table in the Microsoft Fabric Lakehouse.
How we connect to SAP S/4HANA
Vena uses the Xero Accounting API, part of Xero’s REST API suite, to pull financial data for a
given tenant.
For this example, the endpoint GET /api.xro/2.0/Journals is used.
Other Xero Accounting API endpoints (e.g., Invoices, Contacts, Accounts) can be used by
adjusting the script.
Data is retrieved in paged batches using the offset parameter until all records are fetched.
Xero’s APIs require:
An access token obtained via the OAuth 2.0 Client Credentials flow.
The Xero-tenant-id header to specify the organization for which you are retrieving data.
Required setup
1. Set up an Azure key vault.
2. Store Xero API credentials (client ID, client secret, tenant ID) as secrets.
3. Update vault_url in the script with your key vault name.
4. Replace placeholders for client_id and xero_tenant_id with your values.02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 2/7

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
Destinations5. Adjust the modified_after date filter or dataset endpoint as needed.
Configuration: Key Vault + API Setup
Before running this notebook:
1. Provision an Azure key vault
Securely stores your Xero credentials.
The Key Vault name will be used in the vault_url.
2. Add a secret to your key vault
Secret name: xero_client_secret.
Retrieve this in the notebook with:
mssparkutils.credentials.getSecret(vault_url, '<xero_client_secret>')
3. Set this variable in the script:
vault_url = https://<your-key-vault-name>.vault.azure.net/02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 3/7

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
Product UpdatesChanging the API endpoint
By default, this script pulls from the Journals endpoint. To pull from another Xero dataset:
Identify the desired endpoint from Xero API Documentation.
Replace the URL in the fetch_journals() function with the endpoint you want to call.
Adjust the flattening function to match the data structure of the new endpoint.
Example – Pull Invoices:
url = https://api.xero.com/api.xro/2.0/Invoices
Pulling from multiple endpoints
To pull from multiple Xero datasets in a single run:
Create separate fetch and flatten functions for each endpoint, or
Store endpoints in a dictionary and iterate over them:02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 4/7

endpoints = {
    "Journals": "https://api.xero.com/api.xro/2.0/Journals",
    "Invoices": "https://api.xero.com/api.xro/2.0/Invoices" }
for name, url in endpoints.items():
    # Call API, flatten, and save to Lakehouse
Known Xero API limitations
Pagination— Most Xero endpoints limit results to 100 records per request; you must loop
using offset until all records are fetched.
Rate Limits— Xero enforces limits (typically 60 API calls/minute per org and 5,000/day).
Large datasets may require multiple runs or scheduling.
Delta / Change Tracking— Xero supports filtering via If-Modified-Since headers, but not all
objects have efficient delta support.
Data Coverage— Not all Xero objects or fields are available via API; some may require
additional scopes or cannot be retrieved programmatically.
Custom Fields / Add-ons— Certain custom fields or 3rd-party add-ons may not be
accessible without additional API calls.
Was this article helpful?02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 5/7

0 out of 0 found this helpful
Related articles
How-To: Configuring Fabric Data Factory for
Vena Integration
API Notebook: Integration via Microsoft Fabric
– Vena & SAP S/4HANA
Explainer: Vena Fabric Integration
How-To: Integrating Dynamics 365 F&O
Integration with Vena Via Microsoft Fabric
Guide to Vena ResourcesRecently viewed articles
How-To: Configuring Fabric Data Factory for
Vena Integration
How-To: Integrating Dynamics 365 F&O
Integration with Vena Via Microsoft Fabric
Explainer: Vena Fabric Integration
How-To: Managing and Deleting Data Using
Vena Tables
How-To: Exporting Data From a Vena Table
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 6/7

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 16:57 API Notebook: Integration via Microsoft Fabric – Vena & Xero – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38928762275341-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Xero 7/7
