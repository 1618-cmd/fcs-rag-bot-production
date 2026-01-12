# (How To)   Managing Scopes in Vena Copilot

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
Vena CopilotHow-To: Managing Scopes in Vena
Copilot
Manage Scopes in Vena Copilot to identify which members you want the AI model to
retrieve information from.
About Vena Copilot
Sadaf Rahmanian
Updated 2 months ago
05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 1/11

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
CopilotIn partnership with Microsoft, we’ve launched Vena Copilot, a cutting-edge AI-powered assistant
designed to enhance business planning and analysis. This conversational interface can answer
users’ questions with responses grounded in your data, while keeping that data safe and secure.
With our latest release, Vena Copilot can generate reports based on your data, which open in
Vena Ad Hoc. With Vena Copilot, now everyone in your organization can:
Automate mundane tasks.
Quickly retrieve data from data models.
Perform data analysis to gain valuable insights.
Generate custom reports.
Get started with questions like, “What is my year-over-year revenue growth in May 2024 broken
down by Business Unit?” or “Create a report showing the monthly operating expenses broken
down by department in 2023.” and receive instant responses.
Want to learn more about Vena Copilot?
This article is part of a series of articles about Vena Copilot. We’ve organized Vena Copilot into
seven articles. This article explains how Admins can manage the scope and assumed members
in their AI models. The articles most relevant to you depend on your user role and which stage of
the Vena Copilot process you’re at. The Vena Copilot articles are listed below:
Vena Copilot Overview
For Admins r esponsible for assigning user r oles:
Assigning the Vena Copilot user role
For Modelers responsible for setting up AI models:
Creating a Vena Copilot AI Model
Managing Vena Copilot AI Models and Conversations
Managing Scopes in Vena Copilot (you are here)
Adding Prompts in Vena Copilot
For all other V ena Copilot user s:05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 2/11

Product UpdatesUsing Vena Copilot
Vena Copilot Troubleshooting
Differences between Vena Copilot and Vena Help
Vena Copilot for FP&A Data Security and Privacy Brief
Why use this feature?
Now that your AI model has been created, it’s important to identify which members you want
the AI model to retrieve data from when users interact with it. To retrieve data from your cube,
Vena Copilot queries at least one member from each dimension. There are three ways these
members are identified:
1. By analyzing the user prompt.
2. By using Scopes and Assumed Members.
3. The entire hierarchy is returned (if neither the user prompt nor Assumed Members return a
member for a specific dimension).
While using members from user prompts is the optimal option, users may not always specify a
member for each dimension. That’s what Scopes and Assumed Members are for. Scopes limit
the AI model to seeing only a portion of the hierarchy that is present in the data model.
Assumed Members specify a particular member for the AI model to retrieve the data from.
Scopes are helpful to prevent matching incorrect members and double-counting figures when
dealing with very complicated dimensions that contain:
Alternate hierarchies
Multi-purpose dimensions
Similarly named members05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 3/11

For example, some Currency dimensions have two alternate hierarchies: one for local currency
and one for all the reporting currencies. Without specifying which currency to return results in,
numbers may come in counted twice or multiple times. In this example, you could set the Scope
to iDescendants of Reporting Currency. This means that the AI model is limited to Reporting
Currency, USD and GBP:
Local Currency
CAD
Reporting Currency
USD
GBP
However, this may still lead to duplication in results since it could return both USD and GBP in its
responses if it returned the ‘Reporting Currency’ member. To prevent this, you can assign a
specific currency as the Assumed Member. Since the company’s default currency for reporting is
USD, setting this as the Assumed Member ensures results are consistent with what is published
in reports.
Local Currency
CAD
Reporting Currency
USD (Assumed Member)
GBP
Now that USD is set as the Assumed Member, the model will assume this member for the
Currency dimension, unless the user specifies a different member in their prompt. Users can
specify a different currency, such as GBP, in their prompt. The AI model will return the specified
currency since GBP is within the Scope identified. The user prompt (GBP) takes precedence over
the Assumed Member (USD). If users specify a member not in scope (CAD), they will receive an
error message.05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 4/11

Here are a few examples:
A user asks, “What is my revenue growth in 2023?”. The model will return results in Reporting
USD.
A user asks, “What is my revenue growth in 2023 in GBP?”. The model will return results in
Reporting GBP.
A user asks, “What is my revenue growth in 2023 in local currency?”. The model will respond
indicating that it cannot access that data because it falls outside the Scope. This is because
the Local Currency member sits outside the All Reporting Currencies parent member.
Before you begin
To follow the steps in this guide, you will need at least Modeler access and the Vena Copilot
license. Before setting a Scope and Assumed Members, you will need to first create an AI model.
Visit the Creating an AI Model article to learn how to do this.
Table of contents
How to
Setting Scopes
Setting Assumed Members
Glossary
Notes & limitations05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 5/11

How to
Setting Scopes
1. Navigate to the Vena Copilot tab.
2. Select Builder from the sidebar.
3. Either the AI model you want to view.
4. Select Manage Dimensions in the top-right corner.
5. The Manage AI Model Dimensions drawer opens where you can set Scopes and Assumed
Members for the AI Model.05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 6/11

6. Select the dimension that you want to assign a Scope for. Scroll to the right by selecting the
arrow button to see all dimensions.
7. Either right-click on the row or select the vertical ellipsis of the member that you want to
create the Scope for.05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 7/11

8. Select Add to Scope.
9. Add as many members as you want to the Scope. All selected members appear under the
Selected Scope section.
10. Select Apply Changes to save your changes.
Setting Assumed Members
You must first have a Scope identified to set Assumed Members.
1. Either right-click on the row or select the vertical ellipsis of the member that you want to
make the Assumed Member.
2. Select Assumed Member from the drop-down menu. The Assumed Member icon will appear
next to that member.
If you select an Assumed Member outside of an existing Scope, a new Scope will be added to
the dimension.
3. Select Apply Changes to save your changes.05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 8/11

Glossary
Builder: Located in the Vena Copilot tab. Modelers with Edit/Delete application permissions
for AI Models will be able to create, edit and refine AI models.
Assumed Member: Specify a particular member for the AI model to retrieve the data from.
Users may not always reference all dimensions in their prompt. Adding an Assumed Member
helps the AI know which dimension to draw information from.
For example, setting the ‘Value’ member as the default for the Measure dimension is very
helpful for the AI model. This dimension is unlikely to be referenced in user prompts. By
setting it as the Assumed Member, it informs the AI to focus on that dimension.
Scope: A feature that limits the AI model to seeing only a portion of the hierarchy that is
present in the data model. Scopes are helpful to prevent matching incorrect members and
double-counting figures.
Notes & limitations
If users ask questions about members outside of a Scope, they will receive an error message.
You can use Scopes to prevent users from accessing parts of the hierarchy you do not want
them to access in Vena Copilot. However, this should not be used in lieu of data permissions.
Scopes are required for the Scenario and Currency dimension. They are optional for all other
dimensions.
Assumed Members must be within the selected Scope.
If you set an Assumed Member outside of an existing Scope, a new Scope will be added to
the dimension.
User prompts can override Assumed Members.
When users ask questions about performance, they are usually asking about the Actual
scenario. It’s recommended to set Actual as the Assumed Member for Scenario. Then users05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 9/11

won't have to specify that in their prompt. In this case, it’s best practice to set the scope to a
parent member that contains the Actual scenario and any other scenario that users may be
interested in.
Setting Assumed Members to be the current year and the last month of actuals prevents
users from having to specify the fiscal period in their prompt. Setting the assumed member
to be Full Year will by default return financial results for the entire year unless otherwise
specified by the user.
Vena Copilot cannot retrieve data from dimension members that contain special characters
(e.g., ö, ç, ñ). To ensure compatibility and accuracy, avoid using special characters in member
names when asking Copilot questions. As a best practice, design data models without special
characters in member names whenever possible.
Was this article helpful?
2 out of 2 found this helpful
Related articles
How-To: Adding Prompts in Vena Copilot
How-To: Creating an AI Model
How-To: Managing Vena Copilot AI Models &
Conversations
How-To: Using Vena CopilotRecently viewed articles
How-To: Managing Vena Copilot AI Models &
Conversations
How-To: Creating an AI Model
How-To: Assigning the Vena Copilot User Role
Explainer: Vena’s Chatbots – Vena Copilot and05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 10/11

Reference: Vena Calcs - 1 - Managing ScriptsVena Help
Explainer: Vena Copilot for FP&A Data
Security and Privacy Brief
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 16:28 How-To: Managing Scopes in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823029289101-How-To-Managing-Scopes-in-Vena-Copilot 11/11
