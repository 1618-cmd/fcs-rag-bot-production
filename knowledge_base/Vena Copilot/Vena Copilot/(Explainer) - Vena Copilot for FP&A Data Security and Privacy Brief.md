# (Explainer)   Vena Copilot for FP&A Data Security and Privacy Brief

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Vena Copilot/Vena Copilot Search
Getting Started
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena CopilotExplainer: Vena Copilot for FP&A Data
Security and Privacy Brief
Azure Cloud Infrastructure and Services Used
We leverage the following services on Azure:
Azure App Service: This is the backbone of our Azure posture; we use prompt flow to create
a robust workflow that can answer sophisticated user questions by using techniques such as
Sadaf Rahmanian
Updated 8 months ago
05/01/2026, 16:26 Explainer: Vena Copilot for FP&A Data Security and Privacy Brief – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823158080525-Explainer-Vena-Copilot-for-FP-A-Data-Security-and-Privacy-Brief 1/5

Vena Copilot
Explainer: Vena Copilot Tab
Explainer: Vena Copilot Overview
How-To: Using Vena Copilot
Explainer: Vena Copilot for FP&A
Data Security and Privacy Brief
Explainer: Vena’s Chatbots – Vena
Copilot and Vena Help
How-To: Assigning the Vena
Copilot User Role
How-To: Creating an AI Model
How-To: Managing Vena Copilot
AI Models & Conversations
How-To: Managing Scopes in
Vena Copilot
How-To: Adding Prompts in Vena
Copilot
Vena Copilot in Microsoft
Teams
Troubleshooting Vena
Copilotprompt engineering in an intelligent, automated way. We also leverage this technology to
ensure Vena Copilot respects content safety and monitors for inappropriate content. Learn
more about prompt flow here.
Azure AI Cognitive Search Service: This implements our prompt engineering strategy. Azure
Cognitive Search allows us to identify relevant examples from a bank of questions that then
get appended to the user prompt and give Vena Copilot a 'hint’ of how to answer the
question. Learn more about Cognitive Search here.
Azure Content Safety: This is designed to filter for inappropriate content and focus on a
manner to address the questions you would expect Vena Copilot to answer. Learn more
about Azure AI Content Safety here.
Azure Open AI Service: This hosts our Open AI models. Learn more about Azure Open AI
here.
Azure Compliance Certificates
SOC: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-soc-2
ISO: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001#azure-
and-isoiec-27001
GDPR: https://learn.microsoft.com/en-us/legal/gdpr
Azure OpenAI notes: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-
privacy
Geographical Data Residency Requirements05/01/2026, 16:26 Explainer: Vena Copilot for FP&A Data Security and Privacy Brief – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823158080525-Explainer-Vena-Copilot-for-FP-A-Data-Security-and-Privacy-Brief 2/5

Product UpdatesWe operate in 3 distinct geographical regions at Vena: Europe, Canada and the US. To ensure we
are compliant with various data residency requirements such as GDPR and industry-specific
limitations, we have set up Azure hubs in each of these regions.
Data and Model Privacy
Data privacy is a central concern when dealing with AI models. We have instituted several
policies so that your data stays your data, and your Personally Identifiable Information (PII) does
not leave your tenant:
By using Azure Open AI, we are compartmentalizing your data so that it is not used to train
Open AI’s models.
We do not train models across customer tenants on PII. Training done on a model remains
attached to only that model, even if a customer tenant has more than one AI model.
We are also applying:
Application permissions that have been set up on your existing data models.
Data permissions that are built for the data models.
Application permissions for individual AI models, so users must be granted explicit AI
model access to ask Vena Copilot questions.
Turning Vena Copilot On
Vena Copilot is considered turned on when Modeler users can see the AI Builder sidebar tab
under the Data Transformations sidebar. For this to happen:05/01/2026, 16:26 Explainer: Vena Copilot for FP&A Data Security and Privacy Brief – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823158080525-Explainer-Vena-Copilot-for-FP-A-Data-Security-and-Privacy-Brief 3/5

Vena Support needs to set the toggle for the feature flag to ON in our Tenant Management
system.
Users need to accept the in-app notification notifying them they have signing authority and
would like to start the free trial.
Someone with a Vena Admin license assigns the Vena Copilot user role to a Modeler user
who will complete the initial setup.
The Enable Data Permissions for all users policy must be turned on from the Admin tab.
At this point, no data has been pushed from AWS servers into Azure. Hierarchical data from the
selected model will be pushed into Azure when the AI model is created. This data can be deleted
upon customer request.
When the trial period is nearing its end, customers will be able to upgrade to a paying license by
contacting their Account Manager.
Was this article helpful?
0 out of 0 found this helpful
Recently viewed articles
How-To: Using Vena Copilot
Explainer: Vena Copilot Overview
Explainer: Vena Copilot Tab05/01/2026, 16:26 Explainer: Vena Copilot for FP&A Data Security and Privacy Brief – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823158080525-Explainer-Vena-Copilot-for-FP-A-Data-Security-and-Privacy-Brief 4/5

Troubleshooting: Vena for Microsoft PowerPoint Unexpected Error Occurred
Troubleshooting: Vena for Microsoft PowerPoint Authentication Failed
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 16:26 Explainer: Vena Copilot for FP&A Data Security and Privacy Brief – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823158080525-Explainer-Vena-Copilot-for-FP-A-Data-Security-and-Privacy-Brief 5/5
