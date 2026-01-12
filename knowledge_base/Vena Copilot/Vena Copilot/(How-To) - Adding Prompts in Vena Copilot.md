# (How To)   Adding Prompts in Vena Copilot

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
Vena CopilotHow-To: Adding Prompts in Vena
Copilot
Use Vena Copilot Prompts to tailor the chatbot’s responses to what is most relevant to your
company.
About Vena Copilot
In partnership with Microsoft, we’ve launched Vena Copilot, a cutting-edge AI-powered assistant
designed to enhance business planning and analysis. This conversational interface can answer
Sadaf Rahmanian
Updated 17 days ago
05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 1/36

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
Copilotusers’ questions with responses grounded in your data, while keeping that data safe and secure.
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
We’ve organized the Vena Copilot guide into seven articles. This article explains how AI Model
Managers can add prompts to train Vena Copilot to provide better responses and more accurate
reports. The articles most relevant to you depend on your user role and which stage of the Vena
Copilot process you’re at. The Vena Copilot articles are listed below:
Vena Copilot Overview
For Admins r esponsible for assigning user r oles:
Assigning the Vena Copilot user role
For Modelers responsible for setting up AI models:
Creating a Vena Copilot AI Model
Managing Vena Copilot AI Models and Conversations
Managing Scopes in Vena Copilot
Adding Prompts in Vena Copilot (you are here)
For all other V ena Copilot user s:
Using Vena Copilot
Vena Copilot Troubleshooting05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 2/36

Product UpdatesDifferences between Vena Copilot and Vena Help
Vena Copilot for FP&A Data Security and Privacy Brief
Why use this feature?
Use Vena Copilot Prompts to tailor the chatbot’s responses to what is most relevant to your
company. Vena Copilot builds on capabilities of ChatGPT by loading our own question bank into
Azure’s Open AI instance. This question bank is based on frequently asked FP&A questions and
use cases. However, you may track your own set of financial metrics that require unique
formulas.
Vena Copilot Prompts allows you to add your own tailored queries to this question bank. Once
these Prompts are saved, Vena Copilot can match future user prompts to them and determine
whether to use the associated answer key.
Vena Copilot is currently powered by two agents:
Analytics Agent: Responds to questions related to analytics and gaining insights into your
data. Questions like “What is my revenue per headcount in 2024?” will trigger the Analytics
Note
Vena Copilot Prompts were previously referred to as Rules.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 3/36

Agent.
Reporting Agent: Responds to queries asking for a report to be generated. Queries like
“Create a report showing Q3 2024 marketing expenses.” will trigger the Reporting Agent.
Before you begin
To follow the steps in this guide, you will need at least Modeler access and the Vena Copilot
license.
Before setting Prompts, you will need to first create an AI model. Visit the Creating an AI Model
article to learn how to do this.
Table of contents
How to
View Prompts
Manage Prompts
Create Prompts for Analytics Agent Queries
Create Prompts for Reporting Agent Queries
Delete Prompts
Edit Prompts
Example 1 - Analytics Agent
Example 2 - Reporting Agent
Analytics Agent Question Categories
Reporting Agent Question Categories05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 4/36

Glossary
Notes & limitations
How to
View Prompts
1. Navigate to the Copilot tab.
2. Select Builder from the sidebar.
3. Select the AI model name that you want to view.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 5/36

4. Select the Prompt Library tab.
This page displays all Prompts for this AI model. The Prompt, Prompt Theme, Author Type,
Agent Type (Analytics or Reporting), Date and Actions for this AI model are found here.
The Prompt Library Table
Column Function Filter
A Prompt The Promptsaved in
the PromptLibrary.Filter by entering keywords to
search for.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 6/36

B Prompt Theme The categorization of
Promptsby a common
theme.Filter by selecting the checkbox
next to the themes.
C Author Type This shows whether Vena
or a User was the author
of the training Prompt.
When AI models are
created, they come with a
set of Vena-authored
Prompts. Filter by Vena or User.
D Agent Type Indicates which Vena
Copilot Agent the Prompt
is for. Filter by the Reporting or
Analytics Agent.
E Date The date that the Prompt
was created.Sort by ascending or
descending order.
F Actions Edit, preview, refine or
delete a Prompt.N/A
Manage Prompts
Prompts can be added to any user query. User queries do not have to be identically worded for
the Prompt to apply. When a user asks a question, Vena Copilot searches for similar questions
and applies any associated Prompts when determining its response.
Create Prompts for Analytics Agent Queries
You can create prompts in two ways; one option allows you to create a prompt directly in the
Copilot chat. The other option is through the Builder tab. 05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 7/36

Option A: Create a Prompt from a Vena Copilot Chat
If you receive a response from Vena Copilot, you can easily save it as a Prompt to your Prompt
Library without leaving the chat.
1. Navigate to the Vena Copilot tab.
2. Start a new chat with Vena Copilot.
3. If required, select theAI modelyou want to use.
4. After Vena Copilot responds, select View slices behind response.
5. Review the slices to review the members from the data model associated with this response.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 8/36

6. Select Improve Response.
This opens the Improve Response drawer.
7. Select Create New Prompt. Selecting Closest Match allows you to edit an existing Prompt in
your Prompt Library.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 9/36

8. Select Next: Select Members.
9. Select + Dimensions to add dimensions to your Prompt that are referenced in your query. In
the example pictured above, the query mentions Revenue, Department and Years as the
dimensions.
10. For each dimension, use the search bar to find members. Select the vertical ellipses next to
the member you want Vena Copilot to reference and then select the member level.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 10/36

11. You can also remove selected members by selecting the X icon at any time.
12. When you're finished adding or removing members and dimensions, select Next: Prompt
Theme & Instructions.
13. Select a Prompt Theme using the dropdown menu that most closely matches your Prompt
and then add custom instructions for Vena Copilot to follow.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 11/36

14. When you’re finished, selectSave Changes.
Option B: Create a Prompt from the Builder Tab
Creating a Prompt from the Builder tab can be helpful in two scenarios: when you want to
directly train your AI model on a query submitted by an end user or when you want to create a
Prompt from scratch using the + Create Prompt button.
1. Navigate to the Vena Copilot tab.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 12/36

2. Select Builder from the sidebar.
3. Select the AI model name that you want to view.
4. In the Chats tab, either right-click the row or select the vertical ellipsis for the Chat you want
to create a Prompt for.
You can also select + Create Prompt in the Chats and Prompt Library tabs to create a Prompt
from scratch. If using this option, skip to step 7.
05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 13/36

5. Select View Chat to see the full conversation between your user and Vena Copilot.
6. Select the Create Prompt icon under the user query that you want to set a Prompt for.
7. Select +Dimensions. For each dimension, use the search bar to find members. Select the
vertical ellipses next to the member you want Vena Copilot to reference and then select the05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 14/36

member level.
Note
You can add more than one member mapping per dimension when setting
Prompts. For example, if the question is, "Which category of my Operating
Expenses is the highest as a percentage of Revenue?” You should select
Children('Operating Expenses') and Revenue (Member Itself).
When the question is asking about a group of Departments, for example,
“Which department is showing the highest year-over-year revenue growth in05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 15/36

8. When you're finished adding or removing members and dimensions, select Next: Prompt
Theme & Instructions.
9. Select a Prompt Theme using the dropdown menu and then add custom instructions for
Vena Copilot to follow. For example, custom instructions to help answer the prompt above
may be:
Step 1: Retrieve Revenue by department for 2022.
Step 2: Retrieve Revenue by department for 2023.
Step 3: Calculate the difference at each individual department level.
10. When you’re finished, selectSave Changes.
11. The Prompt is now created for your AI model. Prompts apply to all similar questions.
Create Prompts for Reporting Queries
To improve Vena Copilot’s ability to answer more specific queries related to your business, you
may want to create more Prompts. End users are unable to create Prompts themselves, but they
can mark Vena Copilot responses as Correct or Incorrect. This feedback appears in the Chats
table for a Vena Copilot AI Model Manager to review.  We highly recommend that AI Model
Managers periodically review the chat status for prior chats to further train their AI Model and
add Prompts for commonly generated reports.
There are two options for creating Prompts for Reporting Agent queries: from end user chats
and directly from a chat that an AI Admin has started.
Option A: Create Prompts from Reporting Agent End User Chats
2023?”, select the Descendants of All Departments. This will provide a more
consistent experience than selecting all departments one by one.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 16/36

To create Prompts for Reporting Agent queries from an end user chat, you need to identify the
Reporting Agent query in the Chats table from a previous conversation with Vena Copilot:
1. Navigate to the Vena Copilot tab.
2. Select Builder from the sidebar.
3. Select the AI model name that you want to view.
4. Either right-click the row or select the vertical ellipsis for the Chat you want to create a
Prompt for.
5. Select View Chat to see the full conversation between your user and Vena Copilot.
6. Select the Create Prompt icon under the Reporting prompt that you want to set a Prompt
for.
7. A pop-up confirms the report has been downloaded. Open the report from your downloads
folder.
8. Once the report opens, a feedback message appears. Select Keep if this report looks correct.
The Prompt has been added and can be viewed in the Prompt Library table.
9. If the report looks incorrect, select Modify to make changes.
Note
Selecting Modify doesn't save the Prompt.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 17/36

10. Make the necessary changes to the report and select Refresh Data.
11. Select Vena Copilot with the notification icon.
12. If the changes match your expectations for the Vena Copilot query, select Yes. This adds the
query as a Prompt.
13. If the changes still don’t match your expectations for the Vena Copilot query, select Modify.
Continue making changes to the report until it matches your expectations for the query.  05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 18/36

14. The Prompt will now appear in the Prompt Library table and can be modified if necessary.
Option B: Create Prompts from Reporting Agent Admin Chats
As a Vena Copilot Admin chatting with the Reporting Agent, you can easily create Prompts from
your queries directly within the generated report from your Vena Copilot chat.
1. Start a chat with Vena Copilot.
2. Ask Vena Copilot to create a report.
3. Select Download Report and open the report in Vena Ad Hoc.
4. If your report matches your expectations for the Vena Copilot query, select Keep. This
directly trains your AI model and ensures it can answer similar report requests with more
accuracy
5. A Prompt is created and the query is added to the Prompt Library for future use.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 19/36

6. If the report doesn’t match your expectations for the Vena Copilot query, select Modify.
7. Make the necessary adjustments to the report to better match your expectations for the
query and select Refresh Data.
Note
The Prompt is not yet created.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 20/36

8. Select Vena Copilot with the notification icon.
9. If the changes match your expectations for the Vena Copilot query, select Keep. This adds the
query as a Prompt.
10. If the changes still don’t match your expectations for the Vena Copilot query, select Modify.
This query is marked as incorrect in the Chats table.
Delete Prompts
Deleting a Prompt removes it from the entire AI model. This means your AI model will no longer
be trained on that Prompt and similar questions may be less accurate or could provide different05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 21/36

answers. Alternatively, you can edit the Prompt by following the steps in the next section.
1. Follow Viewing Prompts steps 1-5 to get to your list of Prompts.
2. Either right-click on the row or select the vertical ellipsis for the Prompt that you want to
delete.
3. Select Delete from the drop-down menu.
4. Confirm you want to Delete the Prompt by selecting Delete Prompt.
5. The Prompt is now deleted.
Edit Prompts
After you’ve created a Prompt, you can always go back to edit it. There are two options for
editing prompts, in the chat or from the Builder tab.
Option A: Edit a Prompt from a Vena Copilot Chat
1. Navigate to the Vena Copilot tab.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 22/36

2. Select one of thePrompts that exist in the Prompt Library.
3. If required, select the AI model you want to use.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 23/36

4. Select View slices behind response.
05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 24/36

5. Select Improve Response.
6. FollowCreate Prompt from a Vena Copilot Chat steps 6-11 to make changes to the Prompt.
Option B: Edit a Prompt from the Builder Tab
1. Follow Viewing Prompts steps 1-5 to get to your list of Prompts.
2. Either right-click on the row or select the vertical ellipsis for the Prompt that you want to
edit.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 25/36

3. Select Refine Prompt from the drop-down menu.
4. The Refine Prompt drawer opens for Vena Copilot Analytics Agent Prompts.
1. Make any changes you want to the dimensions and members that Vena Copilot should
focus on when retrieving data for responses to similar questions.
2. Select Next: Prompt Theme & Instructionsand make any changes to the Prompt Theme
and custom instructions.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 26/36

3. Select Save Changes to finish editing the Prompt.
5. For Vena Copilot Reporting Agent Prompts, a modal appears. Open the report and choose
Keep to retain the Prompt or Modify to make changes.
6. Select Refresh Data and then select Vena Copilot with the notification icon.
7. If the Prompt looks correct after making changes to the report, select Yes. The Prompt is
updated with your changes.
8. If it still doesn't match your expectations, select Modify. The changes to the Prompt are not
saved.
Example 1 - Analytics Agent
I am building a Prompt for the query “What is my revenue per headcount in 2024?”
1. Select Revenue Analysis for the Question Category.
2. Select + Dimension.
3. Select the checkbox next to Year.
4. Select the vertical ellipsis next to 2024 and select Member Itself.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 27/36

5. Select + Dimension.
6. Select the checkbox next to Account.
7. Select the vertical ellipsis next to Headcount and select Member Itself.
8. Select the vertical ellipsis next to Revenue and select Member Itself.
At this point, I have given the model instructions on where to look in the cube to retrieve the
relevant data.
Now I will instruct the model on how to use this data by filling in the Custom Instructions with
the following:
Step 1: Retrieve the actual data for Revenue for 2024.
Step 2: Retrieve the actual data for Headcount for 2024.
Step 3: Then, Calculate Revenue by Headcount. Divide the total revenue for 2024 by the total
headcount for the same period.
Step 4: Then, Analyze the result to understand the revenue generated per employee for 2024. 05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 28/36

Now that I’m done, I select Apply Changes to save the Prompt.
Example 2 - Reporting Agent
I am building a Prompt for the query “Build me a report showing my full year revenue for 2024.”
1. Select View Chat for the query you want to build a Prompt for.
2. Select the Create Prompt icon.
3. Open the report in Vena Ad Hoc and a feedback message appears.
4. If the report looks correct, select Yes.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 29/36

5. If the report shows Full Year as a summarized column and you want it broken down by
month, select Modify.
6. Change the Period from ‘full year’ to bottomlevel(‘full year’).
7. Select Refresh Data.
8. Select Vena Copilot with the notification and then select Keep in the feedback message.
Analytics Agent Prompt Themes
This is a summary of the Analytics Agent Prompt Themes, their explanation and an example.
Prompt Theme Explanation Example
Scenario Variance Analysis Analyzing the differences
between planned (budgeted)
and actual financial results toWhere did we see the largest
expense variances between
Actuals and Plan in 2022?05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 30/36

understand the reasons for
variances.
Revenue Analysis Examining and managing
revenues associated with
operations, products or
services to identify areas for
revenue improvements.Which projects are showing
the highest growth in 2023?
Expense Analysis Examining and managing
costs associated with
operations, products or
services to identify areas for
cost savings or efficiency
improvements.What is my largest operating
expense as a % of revenue in
January of 2021?
Profitability Analysis Evaluating the profitability of
products, services, business
units or customer segments to
identify areas for
improvement.What are my most profitable
projects in 2023?
Trend Analysis Providing financial insights
and analysis to support the
development and execution of
strategic plans and initiatives.Is there any seasonality in my
cost of goods sold?
Balance Sheet Analysis Analysis involving working
capital, long-term solvency or
any activity ratios involving
balance sheet metrics.What was my Return on Equity
in 2023?05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 31/36

Key Performance Indicator
(KPI) AnalysisDefining and analyzing KPIs to
measure and track the
organization's performance
against strategic objectives.There is no example, as these
are meant to be customer
specific.
Key Influencer IdentificationDetermining the key factors
influencing a particular metric.Does Entity or Department
influence my Profit more?
Reporting Agent Prompt Themes
This is a summary of the Reporting Agent Prompt Themes, their explanation and an example.
Prompt Theme Explanation Example
Revenue Report A report that
examines revenues associated
with operations, products or
services to identify areas for
revenue improvements. Create a high level 2024 report
showing revenue for all
projects.
Expense Report A report that examines costs
associated with operations,
products or services to
identify areas for cost savings
or efficiency improvements.Create a report showing the
monthly operations expenses
broken down by department
in 2023.
Profitability Report Report that evaluates the
profitability of products,
services, business units orGenerate a monthly profit and
loss statement broken down
by entity. 05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 32/36

customer segments to identify
areas for improvement.
Scenario Variance Report Reporting on the differences
between planned (budgeted)
and actual financial results to
understand the reasons for
variances. Create a report showing the
variances between Actuals
and Plan for total OpEx in
2024.
Financial Statements Produces core financial
statement reports to support
the development and
execution of strategic plans
and initiatives. Create a high-level balance
sheet by entity for 2025.
Make a report showing the
YoY changes in my income
statement.
Balance Sheet Accounts
ReportReport involving key balance
sheet account metrics,
including assets, liabilities and
equity groupings. Create a detailed planned
assets report.
Key Performance Indicator
(KPI) ReportOutlining KPIs in a report to
measure and track the
organization's performance
against strategic objectives.Generate a monthly report for
headcount by department.
Glossary
AI Builder: A feature on the Data Transformations page of the Modeler tab. Modelers with
Edit/Delete Application Permissions for AI models can perform training and model
management tasks.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 33/36

AI model: A layer on top of your existing data model that contains additional information to
allow Azure OpenAI to respond to user queries. One AI model is best suited for each use case
(e.g., OpEx analysis). End users can switch between different models to ask questions from
each model. Depending on how your data is organized, you can have more than one AI
model per data model, each tailored for a specific use case.
Question Category: A selection feature to help Vena Copilot use Prompts in a more
systematic way. Setting a category improves how effectively the Prompt can be matched to
semantically similar questions in the future. This also helps users track the themes for past
Prompts on the Prompt Management page.
Prompts: Additional context to improve accuracy for specific questions. Prompts are set for
questions that users have asked.
Scope: A limit on the AI model, refining it to a portion of the hierarchy present in the data
model. Scopes are helpful to prevent matching incorrect members and double-counting
figures.
Agent Type: A new column in the Prompt Library table. Vena Copilot has two types of agents,
Reporting and Analytics. The Reporting Agent answers prompts asking for reports and the
Analytics Agent answers queries for insights into your data.
Author Type: A new column in the Prompt Library table. Shows which queries were created
by a user and which were part of Vena’s set of FP&A training Prompts in all AI models.
Notes & limitations
Prompts only apply to the AI model that they are created in. This is to prevent sharing of
Prompts that make one model better, but that may also deteriorate the quality of another
model.
Prompts are distinct for Reporting vs Analytics Agents.
You cannot create a Prompt for a query if there’s already an identical prompt with a Prompt.
Doing so will cause an error as we do not want to give the model two different sets of
instructions for the same query.05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 34/36

Reporting Agent Prompts currently do not have the option for custom instructions.
Formatting and formulas/calculations are not yet available for Reporting Agent Prompts.
Deleting a chat will delete any Prompts associated within the conversation.
Archiving a chat retains any Prompts associated with the conversation.
Reporting Agent Prompts will always have the Custom Report Question Theme. Future
enhancements will enable modifying Prompt themes for the Reporting Agent.
Reporting Agent Prompts can’t be created from Scratch using the + Create Prompt button.
Was this article helpful?
0 out of 0 found this helpful
Related articles
How-To: Using Vena Copilot
How-To: Assigning the Vena Copilot User Role
How-To: Setting up Data Validation Rules
Troubleshooting: Unable to Install Vena
Desktop
Explainer: What Comprises a Dataset that is
Generated Through Vena Insights?Recently viewed articles
How-To: Managing Scopes in Vena Copilot
How-To: Managing Vena Copilot AI Models &
Conversations
How-To: Creating an AI Model
How-To: Assigning the Vena Copilot User Role
Explainer: Vena’s Chatbots – Vena Copilot and
Vena Help05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 35/36

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 16:29 How-To: Adding Prompts in Vena Copilot – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/25823072646413-How-To-Adding-Prompts-in-Vena-Copilot 36/36
