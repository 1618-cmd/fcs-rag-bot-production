# (API Notebook)   Integration via Microsoft Fabric   Vena & Deltek Vantagepoint

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
Microsoft Fabric - Vena & Deltek
Vantagepoint
What this notebook does
This notebook explains how to securely connect to a Deltek Vantagepoint ERP environment and
pulls data from the GL transaction endpoints using the Deltek REST API.
Vena Support Team
Updated 2 months ago
02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 1/8

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
Deltek VantagepointAuthenticates securely with OAuth and session handling.
Loops through key GL transaction types (AP, JE, etc.).
Joins master-detail records into a single flat table.
Saves the results to the Fabric Lakehouse.
This notebook is preconfigured for General Ledger (GL) data but is reusable across other Deltek
API endpoints with minimal changes.
How Vena connects to Deltek Vantagepoint
Vena usesDeltek’s REST API, authenticated via OAuth 2.0 with client ID/secret + user credentials.
Deltek REST API base URL example
https://vantagepointpartner.deltekfirst.com/Venacorp/api
Token endpoint for authentication
/token
All subsequent data requests are authorized via bearer tokens.
Required setup02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 2/8

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
Destinations1. Set up an Azure key vault.
2. Store Deltek secrets (client ID, client secret, username, password).
3. Update vault_url in the script.
4. Modify API version and base URL as needed.
5. Optionally extend to support other endpoints.
Configuration: Key vault + API setup
Before running this notebook:
1. Provision an Azure Key Vault
Securely stores Deltek credentials. Retrieved directly from the Fabric notebook.
2. Add the Following Secrets:
Deltek-username - Deltek login username
Deltek password - Deltek login password
Deltek clientID - OAuth client ID
Deltek clientSecret - OAuth client secret
3. Set This Variable in the Script:
vault_url = "https://<your-key-vault-name>.vault.azure.net/"02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 3/8

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
Product UpdatesThese credentials are injected using:
USERNAME = mssparkutils.credentials.getSecret(vault_url, 'Deltek-username')
PASSWORD = mssparkutils.credentials.getSecret(vault_url, 'Deltek-password')
CLIENT_ID = mssparkutils.credentials.getSecret(vault_url, 'Deltek-clientId')
CLIENT_SECRET = mssparkutils.credentials.getSecret(vault_url, 'Deltek-clientSecret')
Runtime parameters
Before running the notebook, you’ll need to configure the following variables (manually or
passed from a pipeline):
Variable Example Description
BASE_URL https://vantagepointpartner.deltekfirst.com/Venacorp/apiBase API URL
DATABASE"P0000052948P_1_VENACORP000" Customer's Deltek
database ID
CULTURE "en-US" API culture setting
output_folder"deltek/ledger" Lakehouse output
path02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 4/8

Changing the API endpoint
To use this notebook for non-GL endpoints (e.g., Projects, Timesheets):
1. Update the API endpoint paths:
endpoint = f"/{DATABASE}/{CULTURE}/{new_entity_type}/landing"
1. Modify the schema parsing logic in the flatten_json and row extraction sections to match the
structure of the new endpoint’s response.
Pulling from multiple endpoints
This notebook supports a loop through multiple GL transaction types (e.g., in, ap, je, cr, etc.).
To expand this logic:
Add new types to the TRANSACTION_TYPES dictionary.
Implement or update flattening logic for the new data structures.
Save each output into a logically named Lakehouse folder or file.
Output structure
The output is flattened and saved in CSV format in your Fabric Lakehouse:02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 5/8

/lakehouse/default/Files/deltek/ledger/GL_data_<timestamp>.csv
Sample columns include:
Account, AccountName, CreditAmount, DebitAmount
WBS1, WBS2, WBS3 (Project structure)
Posted, TransDate, FunctionalCurrencyCode
Known Deltek API limitations
OAuth - Token lifespan is short-lived; must refresh per run (handled in notebook).
Scheme - Master/Detail schemas vary by transaction type.
Volume - Paging may be required for large result sets.
Throttling - No official rate limit is published, but retries are handled.
Internalization - Culture codes (e.g., en-US) must be set correctly.
Was this article helpful?
0 out of 0 found this helpful
Related articles
Explainer: Vena Fabric IntegrationRecently viewed articles02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 6/8

How-To: Set Up a Business Central Connector
and Data Feed
Explainer: How Vena Assigns Licenses to Your
Users
How-To: Configuring Fabric Data Factory for
Vena Integration
Explainer: Set Staging or Transactions Tables
When Building a Vena TableAPI Notebook: Integration via Microsoft Fabric
– Vena & Acumatica
API Notebook: Integration via Microsoft Fabric
– Vena & SAP S/4HANA
API Notebook: Integration via Microsoft Fabric
– Vena & Xero
How-To: Configuring Fabric Data Factory for
Vena Integration
How-To: Integrating Dynamics 365 F&O
Integration with Vena Via Microsoft Fabric
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 7/8

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric - Vena & Deltek Vantagepoint – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921438875277-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Deltek-Vantagepoint 8/8
