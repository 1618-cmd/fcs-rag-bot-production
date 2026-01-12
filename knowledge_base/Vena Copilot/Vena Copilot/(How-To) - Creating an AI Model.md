# (How To)   Creating an AI Model

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
Vena CopilotHow-To: Creating an AI Model
As an AI Model Manager, you will need to create an AI model before your users get started with
Vena Copilot. Learn more in this article.
About Vena Copilot
In partnership with Microsoft, we’ve launched Vena Copilot, a cutting-edge AI-powered assistant
designed to enhance business planning and analysis. This conversational interface can answer
users’ questions with responses grounded in your data, while keeping that data safe and secure.
Sadaf Rahmanian
Updated 2 months ago
05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 1/18

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
CopilotWith our latest release, Vena Copilot can generate reports based on your data, which open in
Vena Ad Hoc. With Vena Copilot, now everyone in your organization can:
Automate mundane tasks.
Quickly retrieve data from data models.
Perform data analysis to gain valuable insights.
Generate custom reports.
Get started with questions like, “What is my year-over-year revenue growth in May 2024 broken
down by Business Unit?” or “Create a report showing the monthly operating expenses broken
down by department in 2023.” and receive instant responses.
Want to learn more about Vena Copilot?
This article is part of a series of articles about Vena Copilot. We’ve organized Vena Copilot into
seven articles. This article explains how Admins can create an AI model. The articles most
relevant to you depend on your user role and which stage of the Vena Copilot process you’re at.
The Vena Copilot articles are listed below:
Vena Copilot Overview
For Admins r esponsible for assigning user r oles:
Assigning the Vena Copilot user role
For Modelers responsible for setting up AI models:
Creating a Vena Copilot AI Model (you are here)
Managing Vena Copilot AI Models and Conversations
Managing Scopes in Vena Copilot
Adding Prompts in Vena Copilot
For all other V ena Copilot user s:
Using Vena Copilot
Vena Copilot Troubleshooting
Differences between Vena Copilot and Vena Help
Vena Copilot for FP&A Data Security and Privacy Brief05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 2/18

Product Updates
Why use this feature?
As an AI Model Manager, creating a Vena Copilot AI model is the first step in getting your users
started with Vena Copilot. At this stage, you can select your model type, identify the data model
and configure questions.
Before you begin
To follow the steps in this guide, you will need at least Modeler access and the Vena Copilot
license.
You will also need either of the following Application Permissions settings:
Create Access Type for All of Vena (Except Admin Features), or
Create Access Type for Vena Copilot
Your data model requires specific Dimension Types and Standard Members to be compatible
with Vena Copilot. The table below indicates the necessary Dimension Types and Standard
Members.
Note05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 3/18

Dimension Type Standard Member
Account Net Income
Account Revenue
Account Operating Expenses
Year 2021
Year 2022
Year 2023
Period Full Year
Period January
Period February
Period March
Period April
Period May
You can apply Dimension Types and Standard Members before creating your AI
model(s), or complete the process in step 2.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 4/18

Period June
Period July
Period August
Period September
Period October
Period November
Period December
Scenario Actual
Measure Total Value
Table of contents
Create an AI Model
Glossary
Notes & limitations
How to05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 5/18

It is important to understand how the AI model works. Think of the AI model as a layer that sits
on top of your Vena CubeFlex data and allows us to leverage OpenAI models. The AI model you
create will contain dimension mappings, Prompts and chat history. This enables us to combine
the best of Vena’s technology with the latest advancements in large language models.
You can have multiple AI models on your tenant, each trained for a specific task. When users
open the chat interface, they see all the models that they have permissions for. To begin, they
can select a curated prompt or create their own by typing in the chat.
If there’s more than one AI model, they can select which model they want to interact with.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 6/18

Create an AI Model
1. Navigate to the Vena Copilot tab.
2. Select Builder from the sidebar.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 7/18

3. Select Create AI model. This opens the Create AI model drawer.
Step 1: Choose Theme
1. Select one of the three AI Model onboarding themes.
2. Press Select to begin building your AI model.
You can choose from one of three theme options:
Revenue Performance AI Model
Cost Insights AI Model
Start From Scratch
There are two pre-built theme options (Revenue Performance and Cost Insights) and a
third, custom theme (Start From Scratch). The Revenue theme is designed to answer
revenue-themed questions. The Cost theme is designed to answer cost-themed
questions. If it is your first time creating an AI model, it is recommended that you use one
of the pre-built themes instead of starting from scratch.
If you select the Revenue theme, we map to the Revenue member. If you select the Cost
theme, we map to the Operating Expenses member. The pre-built themes are designed to
make AI model creation faster, you will still be able to adjust the specifications for each05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 8/18

theme afterwards. Your users will not be limited to asking questions about revenue or
costs when they use one of these themes.
3. Select Next: Configure AI Model Settings to confirm your selection.
Info
Ensure you have the appropriate Data Permissions for the data model you selected.
If you don't have the proper Data Permissions, contact your Vena Admin.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 9/18

Step 2: Configure AI Model Settings
1. For Revenue Performance & Cost Insights models: Select your Finance data model.
For the custom models: Select the data model that you want your chatbot to answer
questions about.
Note05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 10/18

2. Select a default currency for your AI model. This is the currency your AI model provides
answers in if not specified by the user.
3. Enter a name for your AI model. This name helps users identify the purpose of the model. It’s
important to use a descriptive name, especially if there are multiple AI models set up in your
tenant.
4. Enter a description for your AI model. It is recommended that your description includes
information to help users identify the data model associated with this chatbot.
5. Select Next: Configure Training Question.
You'll see an error if your model does not have the required Standard Members and Dimension
Types tags. This message will disappear after you tag the required Standard Members. The best
practice is to tag as many of the members as possible to ensure your model has sufficient
training data. You can also apply tags in the Modeler tab before using Vena Copilot to create an
AI model.
Step 3: Configure Training Question
For Revenue Performance & Cost Insights:
1. Choose one of the three pre-selected questions from the drop-down menu. Vena Copilot will
respond to this question at the end of the onboarding to gauge how well the model is
trained.
The model is not restricted to answering questions that are similar to this one. Once users
You can only use Vena Copilot for models that have the appropriate Dimension
and Member Types tagged. See the Before you begin section of this article for
more details.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 11/18

launch the chatbot, they can ask any question.
2. Navigate to the dimension you want to set an Assumed Member for. You can set Assumed
Members to indicate which members the AI model should query from your dimensions. You
must set an Assumed Member for the Scenario Dimension. An Assumed Member for the
Currency dimension is only mandatory if it's assigned in your Data Model. Setting Assumed
Members for all other dimensions is optional.
Assumed Members specify a member for the AI model to retrieve data from. Users may not
always specify specific members in their prompt. Adding an Assumed Member helps the AI
know which member to draw information from. For example, if you have multiple currencies,
CAD, USD and GBP. Setting USD as the Assumed Member will return responses in USD only,
unless otherwise specified by the user.
3. Select the Assumed Member icon next to the member you want to identify as the Assumed
Member.
4. If you want to add Assumed Members for additional dimensions that aren’t listed:
Select + Dimensions to expand the drop-down menu.
Select the checkbox next to the additional dimension(s) you want to define Assumed
Members for.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 12/18

When setting Assumed Members, you must set an Assumed Member for the Scenario
Dimension. An Assumed Member for the Currency dimension is only mandatory if it's
assigned in your Data Model. It is optional to set Assumed Members for the Account, Year,
Period and Measure dimensions. If you want to set an Assumed Member for any
dimension that is not listed here, you will have to do that from the model management
flow. You can find instructions for that in the Managing Scopes in Vena Copilot article.
5. Select Create AI Model.
6. Now that your AI model is created, you can continue training it or Publish.
7. For next steps, visit the Managing AI Models and Conversations or Managing Scopes in Vena
Copilot article.
For Custom Models:
If it is your first time creating an AI model, it is recommended that you use one of the pre-built
Revenue or Cost themes instead of starting from scratch.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 13/18

1. Enter a sample question that users could enter to begin the conversation. The model will not
be restricted to answering questions that are similar to this one. After you have completed
the AI model configuration, you will be able to adjust these pre-sets and use the model as
you see fit.
2. Navigate to the dimension you want to set an Assumed Member for. Assumed Members
indicate which members the AI model should query from your dimensions. You must set an
Assumed Member for the Scenario Dimension. An Assumed Member for the Currency
dimension is only mandatory if it's assigned in your Data Model. Setting Assumed Members
for all other dimensions is optional.
Assumed Members specify a member for the AI model to retrieve data from. Users may not
always specify specific members in their prompt. Adding an Assumed Member helps the AI
know which member to draw information from. For example, if you have multiple currencies,
CAD, USD and GBP. Setting USD as the Assumed Member will return responses in USD only,
unless otherwise specified by the user.
3. Select the Assumed Member icon next to the member you want to identify as the Assumed
Member.
4. If you want to add Assumed Members for additional dimensions that aren’t listed:
Select + Dimensions to expand the drop-down menu.
Select the checkbox next to the additional dimension(s) you want to define Assumed
Members for.
you must set an Assumed Member for the Scenario Dimension. An Assumed Member for
the Currency dimension is only mandatory if it's assigned in your Data Model. It is optional05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 14/18

to set Assumed Members for the Account, Year, Period and Measure dimensions. If you
want to set an Assumed Member for any dimension that is not listed here, you will have to
do that from the model management flow. You can find instructions for that in the
Managing Scopes in Vena Copilot article.
5. Select Create AI Model.
6. Now that your AI model is created, you can continue training it or Publish.
7. For the next steps, visit the Managing AI Models and Conversations or Managing Scopes in
Vena Copilot article.
Glossary
Builder: Located on the Vena Copilot tab. Modelers with Edit/Delete application permissions
for AI models will be able to create, edit and refine AI models.
AI model: The AI model exists as a layer on top of your existing data model. It contains
additional information that allows Azure OpenAI to give responses to user queries. One AI
model is best suited for each use case (e.g., OpEx analysis). End users can switch between
different models to ask questions from each model. Depending on how your data is
organized, you can have more than one AI model per data model, each tailored for a specific
use case.
Assumed Member: Assumed Members specify a particular member from which the AI
model retrieves the data. Users may only sometimes reference all dimensions in their
prompt. Adding an Assumed Member helps the AI know which dimension to draw
information from.05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 15/18

For example, setting the ‘Value’ member as the default for the Measure dimension is very
helpful for the AI model. Since this dimension is unlikely to be referenced in user prompts,
setting it as the default informs the AI to focus on that dimension.
Model Theme: This is a concept specific to creating your AI model. There are three model
theme options. The first two use a pre-set list of onboarding questions. The third theme is
customized. The Model Theme does not limit the questions users can ask from the model.
The three Model Themes are:
Revenue Theme answers revenue-specific questions.
Cost Theme answers operating expenses-specific questions.
Custom Theme allows users to start with a broader AI model.
Notes & limitations
Vena Copilot only has access to data stored in a Vena Data Model, so it does not have access
to data stored in Vena Tables or Line-Item Details (LIDs). Specifically, it cannot query
transactional data.
Vena Copilot can access one Data Model at a time.
Vena Copilot cannot take Attributes into consideration when generating responses to user
prompts.
Vena Copilot does not consider Process Variables when generating responses to user
prompts.
Vena Copilot considers Data Permissions when generating responses, but it does not
consider access limitations imposed by Task Bindings.
Vena Copilot uses cube data directly. It cannot answer questions for data models which have
cross-dimensional dependencies. For example, if you have one account that houses labor
expenses (Account 100), and for the Manufacturing department, that cost ends up in COGS,
while for the Marketing department, that cost ends up in OpEx for your reporting purposes,05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 16/18

Vena Copilot would not be able to determine Gross Margin. In this case, please reach out to
your CSM to explore alternatives.
Setting Assumed Members to be the current year and the last month of actuals prevents
users from having to specify the fiscal period in their prompt. Setting the Assumed Member
to be Full Year will, by default, return financial results for the entire year unless otherwise
specified by the user.
When a data model that is used in Vena Copilot changes, you must select Refresh Model
Data on the AI Models page. This keeps the AI model in sync with the underlying data model.
A data model is considered to have changed when:
Members are added, removed, or renamed.
Dimensions are added, removed, or renamed.
Vena Copilot cannot retrieve data from dimension members that contain special characters
(e.g., ö, ç, ñ). To ensure compatibility and accuracy, avoid using special characters in member
names when asking Copilot questions. As a best practice, design data models without special
characters in member names whenever possible.
Was this article helpful?
2 out of 2 found this helpful
Related articles Recently viewed articles
How-To: Assigning the Vena Copilot User Role05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 17/18

How-To: Assigning Dimension Types and
Standard Members
How-To: Managing Vena Copilot AI Models &
Conversations
How-To: Using Vena Copilot
Explainer: Vena Copilot Overview
How-To: Adding Prompts in Vena CopilotExplainer: Vena’s Chatbots – Vena Copilot and
Vena Help
Explainer: Vena Copilot for FP&A Data
Security and Privacy Brief
How-To: Using Vena Copilot
Explainer: Vena Copilot Overview
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 16:27 How-To: Creating an AI Model – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/24723253669133-How-To-Creating-an-AI-Model 18/18
