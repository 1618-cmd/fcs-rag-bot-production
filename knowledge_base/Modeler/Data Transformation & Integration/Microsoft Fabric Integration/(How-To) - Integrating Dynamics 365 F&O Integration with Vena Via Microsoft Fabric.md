# (How To)   Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric

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
Integration
Explainer: Vena Fabric
Integration
How-To: Integrating Dynamics
365 F&O Integration with Vena
Via Microsoft Fabric
How-To: Configuring Fabric
Data Factory for VenaHow-To: Integrating Dynamics 365 F&O Integration with Vena
Via Microsoft Fabric
Automate financial data integration from Dynamics 365 F&O into Vena using Microsoft Fabric and Dataverse Link.
Why use this feature?
This integration automates the extraction of financial data from Dynamics 365 F&O for FP&A teams. Financial data is transformed and loaded into the Fabric
Lakehouse, streamlining reporting and planning processes in Vena. By minimizing manual data preparation, this integration delivers real-time access to financial
information for efficient planning and reporting.
Before you begin
To complete this setup, you’ll need:
System Administrator security role access to your F&O environment.
Microsoft Fabric enabled in your Azure tenant, plus permissions in Fabric to manage connections. Learn how to configure Microsoft Fabric for Vena
integration.
Modeler & Admin access in Vena.
Vena Support Team
Updated 1 month ago
02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 1/10

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
DestinationsTable of contents
How to
Part 1 – Accessing permissions to create Fabric lakehouses and artifacts
Part 2 – Integrating your Dynamics F&O environment with Power Platform
Part 3 – Creating the connection with Vena
API Notebook
What this notebook does
How Vena connects to F&O
Required setup
Configuration: Key Vault + API Setup
Changing the table
Script
Pulling from multiple endpoints
Output structure
Known Dynamics F&O "Link to Fabric” limitations
How to
Part 1 – Accessing permissions to create Fabric lakehouses and artifacts
To follow the steps in this article, your administrator must grant you the following access:  02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 2/10

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
Product UpdatesIn the Microsoft Fabric Admin Portal:
Creating Fabric items. Navigate to Tenant settings > Microsoft Fabric > Users can create Fabric items for access settings.
Creating workspaces. Navigate to Tenant settings > Workspace settings > Create workspaces for access settings.
OneLake data access. Navigate to Tenant settings > OneLake settings > Users can access data stored in OneLake with apps external to Fabric for
access settings.  02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 3/10

In Fabric’s Settings menu:
Manage connections permissions. Navigate to Settings > Manage connections and gateways for access settings.
Learn more about Microsoft Azure permissions.
Part 2 – Integrating your Dynamics F&O environment with Power Platform
Through this Fabric Workspace setup and connection process, you will link the Dynamics 365 F&O data to Microsoft Fabric via Dataverse Link.
1. Open the Dynamics Power Apps Environment. 02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 4/10

2. Select Analyze> Link to Microsoft Fabric.
Follow the steps in the guide for creating a connection:
Create a Fabric Workspace. This workspace will host your lakehouse – Fabric's unified data storage layer.
Create a Connection.
Wait for the data to sync.
3. Select Analyze > Link to Azure Synapse.
Part 3 – Creating the connection with Vena
1. Select Manage Tables.
02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 5/10

2. Select all Dynamics Tables containing data to integrate into Vena, then select Save.
3. Select Tables, then Refresh Fabric tables.
4. Select View in Microsoft Fabric to navigate directly to the linked workspace.
5. Create a notebook.02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 6/10

6. In the Explorer > Data Items tab, select Add data items > Existing data sources.
7. Select the lakehouse (the workspace created in Step 2) containing F&O data to integrate with Vena.
8. Modify the Notebook (refer to details in the API Notebooksection of this article) to pull specific tables and columns into Vena through the Public API.
API Notebook
What this notebook does
This notebook leverages an integration setup between F&O dynamics & Fabric that will allow F&O app data to be saved in a Fabric lakehouse that can be queried to
pull specific tables and fields.
How Vena connect to F&O
This integration leverages a special setup between Dynamics F&O, Power Apps and Fabric. You will create a data lakehouse in Microsoft Fabric that has your
selected F&O data automatically synced to Fabric. Learn more about linking your Dataverse environment to Microsoft Fabric.
Required setup
1. Follow the steps in the How-To section of this article.02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 7/10

2. Set up an Azure key vault. Add Vena application token info.
3. Update vault_url in the script.
Configuration: Key Vault + API setup
Before running this notebook:
Set the following secrets in Azure Key Vault:
venaApiUser – Vena application token apiUser
VenaApiKey – Vena application token apiKey
vault_url = "https://<your-key-vault-name>.vault.azure.net/"
API_USER = mssparkutils.credentials.getSecret(vault_url, 'venaApiUser')
API_KEY = mssparkutils.credentials.getSecret(vault_url, 'venaApiKey)
Changing the table
To pull from a different Dataverse table, update this line:
df = spark.read.table("ledger").select("Id","name","description","createdby","createddatetime","partition","recid","tableid","isDelete","fiscalcalendar","chartofacc
Update the query logic to reflect the schema of the new table.
Script
hub = "us1" # Vena Hub Customer ie. us1,us2,us3,us4,us5,eu1,eu2,eu3,ca3,ca4
import_template_id = "1337596877012467713" # ETL Template ID from Vena UX
vault_url = "https://{KEY_VAULT_NAME}.vault.azure.net/" # Azure Key Vault URL
LAKEHOUSE_FOLDER_PATH = "Files/dynamics" # Lakehouse folder path with the CSV File to upload to Vena
from vepi import VenaETL
API_USER = mssparkutils.credentials.getSecret(vault_url, 'venaApiUser') # venaApiUser is the secret name in the Key Vault
API_KEY = mssparkutils.credentials.getSecret(vault_url, 'venaApiKey') # venaApiKey is the secret name in the Key Vault
# Initialize the Vena client
vena_etl = VenaETL(
hub=hub,
api_user=API_USER,
api_key=API_KEY,02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 8/10

template_id=import_template_id,
)
# Read from linked Dynamics F&O table(Modify table & select fields to pull the data you need)
df = spark.read.table("ledger").select("Id", "name", "description", "createdby", "createddatetime", "partition", "recid", "tableid", "isDelete", "fiscalcalendar",
"chartofaccounts", "budgetexchangeratetype")
# Write to lakehouse path as CSV
df.coalesce(1).write.mode("overwrite").option("header", False).csv(LAKEHOUSE_FOLDER_PATH)
# Find the CSV file
files = mssparkutils.fs.ls(LAKEHOUSE_FOLDER_PATH)
csv_file = [f.name for f in files if f.path.endswith(".csv")][0]
# Start ETL Job in Vena
vena_etl.start_with_file("/lakehouse/default/" + LAKEHOUSE_FOLDER_PATH + "/" + csv_file)
Pulling from multiple endpoints
To process multiple tables:
Create a list of table configurations.
Loop through each and apply transformation logic.
Save each result in a separate folder.
Output structure
The output is saved as Delta tables in Fabric Lakehouse. Each table is flattened and normalized for reporting.
Known Dynamics F&O "Link to Fabric” limitations
Refresh Frequency Constraints: Near real-time sync is supported for key entities, but large datasets refresh at scheduled cadences.
Throttling: API rate limits may apply depending on tenant configuration.
Was this article helpful?
0 out of 0 found this helpful02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 9/10

Related articles
How-To: Configuring Fabric Data Factory for Vena Integration
How-To: Using Vena Ad Hoc To View Your Data and Make Simple Reports
API Notebook: Integration via Microsoft Fabric – Vena & SAP S/4HANA
Explainer: Vena Fabric Integration
API Notebook: Integration via Microsoft Fabric – Vena & XeroRecently viewed articles
Explainer: Vena Fabric Integration
How-To: Managing and Deleting Data Using Vena Tables
How-To: Exporting Data From a Vena Table
Explainer: Set Staging or Transactions Tables When Building a Vena Table
Troubleshooting: ETL Error Guide
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 16:56 How-To: Integrating Dynamics 365 F&O Integration with Vena Via Microsoft Fabric – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/40419173641229-How-To-Integrating-Dynamics-365-F-O-Integration-with-Vena-Via-Microsoft-Fabric 10/10
