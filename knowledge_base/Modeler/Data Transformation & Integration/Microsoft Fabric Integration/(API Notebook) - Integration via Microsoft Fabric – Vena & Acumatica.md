# (API Notebook)   Integration via Microsoft Fabric – Vena & Acumatica

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
Microsoft Fabric – Vena & Acumatica
What this notebook does
This notebook describes how to securely connect to the Acumatica ERP environment and pull
data from the API endpoints using the Acumatica REST API.
Logs in using a secure session.
Vena Support Team
Updated 2 months ago
02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 1/7

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
Deltek VantagepointPulls ledger data with nested fields (Branches, Companies).
Flattens the result into tabular format.
Saves the results to the Fabric Lakehouse.
How we connect to Acumatica
Vena uses the Acumatica REST API, available per tenant instance (e.g.
https://customername.acumatica.com).
Acumatica REST API Documentation
The endpoint used in this notebook as a starting point is:
/entity/Default/{version}/Ledger?$expand=<fields>
Each request requires a secure login using company, branch, username and password, after
which a cookie-based session is used.
Required setup
1. Set up an Azure key vault.
2. Store SAP API key as a secret (SAP-APIkey).
3. Update vault_url in the script.
4. Modify the URL1 variable to target a new SAP API endpoint.
5. Optionally extend the script to process multiple endpoints.02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 2/7

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
DestinationsConfiguration: Key Vault + API Setup
Before running this notebook:
1. Provision an Azure key vault
Secures Acumatica credentials.
You'll retrieve secrets directly within the Fabric notebook.
2. Add the following secrets:
Username - Acumatica login username
Password - Acumatica password
3. Set this variable in the script:
vault_url = "https://<your-key-vault-name>.vault.azure.net/"
These credentials are injected using:
USER = mssparkutils.credentials.getSecret(vault_url, 'username')
PASSWORD = mssparkutils.credentials.getSecret(vault_url, 'password')
 02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 3/7

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
Product UpdatesRuntime parameters
Before running the notebook, you’ll need to configure the following variables (manually or
passed from a pipeline):
Variable Example Description
base_url https://customername.acumatica.comAcumatica instance URL.
company "DemoTenant" Target company in Acumatica.
branch "CAPITAL" Acumatica branch name.
api_version "24.200.001" API version used in Acumatica.
output_folder"acumatica/ledger" Output location in Fabric Lakehouse.
api_select_query"LedgerID,Branches,Companies" Fields to expand in the query.
Changing the API endpoint
This script pulls from the Ledger endpoint by default. To pull from a different endpoint:
1. Update this line:02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 4/7

ledger_endpoint = f"/entity/Default/{api_version}/<NEW_ENDPOINT>?$expand=
{api_select_query}"
For example, to pull from Sales Orders:
ledger_endpoint = f"/entity/Default/{api_version}/SalesOrder?$expand={api_select_query}"
2. Adjust the flattening logic accordingly:
Each Acumatica endpoint returns a different structure, so the script block for Step 5: Flatten
Data must be customized for the new schema.
Pulling from multiple endpoints
To process multiple endpoints in one run:
Create a list of endpoint configurations (URL + flattening logic).
Iterate through them using a loop.
Store each result in a separate folder or file path.
Let me know if you’d like a pre-built version of this.
Known Acumetica REST API limitations02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 5/7

Field-level control: Not all nested data is flattened automatically; nested collections (like
Shipments, Details) require manual handling.
Throttling: API rate limits may apply depending on tenant configuration.
Authentication: Session tokens expire—this notebook handles login per run.
Paging: This example assumes responses are not paged. For larger datasets, you’ll need to
implement paging (e.g., using $top and $skip).
Paging logic can be added using Acumatica’s $top, $skip, or custom filters for incremental loads.
Was this article helpful?
0 out of 0 found this helpful
Related articles
API Notebook: Integration via Microsoft Fabric
– Vena & SAP S/4HANA
API Notebook: Integration via Microsoft Fabric
- Vena & Deltek Vantagepoint
Explainer: Vena Fabric Integration
How-To: Set Up a Quickbooks Connector and
Data FeedRecently viewed articles
API Notebook: Integration via Microsoft Fabric
– Vena & SAP S/4HANA
API Notebook: Integration via Microsoft Fabric
– Vena & Xero
How-To: Configuring Fabric Data Factory for
Vena Integration
How-To: Integrating Dynamics 365 F&O
Integration with Vena Via Microsoft Fabric02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 6/7

How-To: Getting Vena 365 for Windows or
Installing Vena DesktopExplainer: Vena Fabric Integration
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:58 API Notebook: Integration via Microsoft Fabric – Vena & Acumatica – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/38921800097805-API-Notebook-Integration-via-Microsoft-Fabric-Vena-Acumatica 7/7
