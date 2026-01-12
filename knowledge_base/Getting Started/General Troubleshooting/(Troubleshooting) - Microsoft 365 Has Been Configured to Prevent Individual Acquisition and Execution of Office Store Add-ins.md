# (Troubleshooting)   Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add ins

Vena Solutions/Getting Started/General Troubleshooting Search
Getting Started
Fundamentals
User Account Management
Support
Product & IT Information
Resources
General Troubleshooting
Troubleshooting: Vena Text
Appears in Heavy Italic Font
Troubleshooting: Microsoft 365
Has Been Configured to Prevent
Individual Acquisition and
Execution of Office Store Add-ins
ManagerTroubleshooting: Microsoft 365 Has
Been Configured to Prevent Individual
Acquisition and Execution of Office
Store Add-ins
Issue summary
Microsoft or Office 365 has been configured to prevent individual acquisition and execution of
Office Store Add-ins.
Olalekan Adebayo
Updated 8 months ago
31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 1/9

Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
Suggested solution
Solution 1: Enabling store access
Your Microsoft IT or Admin can follow the steps below:
1. Login to admin.microsoft.com.
2. On the left pane, select Show All > Settings > Org settings.
3. Select User owned apps and services.
4. Check the box next to Let users access the Office Store.
5. Select Save.
31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 2/9

Solution 2: Centralized Deployment
Your IT or Admin can also deploy the Vena Add-in centrally. This is a 4-step process.
Step 1: Determine if the Centralized Deployment of the Add-ins works for your
organization.
You can skip this step and move to Step 2. If Step 2 fails, you can come back to this step and
verify if you’re eligible.
Step 2: Deploy the Vena Desktop centrally.
1. Log in to admin.microsoft.com31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 3/9

2. On the left pane, select Show All > Settings > Integrated apps.
31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 4/9

3. Select Add-ins.
4. Select Deploy Add-in.
5. Select Choose from the Store. The rest of the instructions are specific to Vena.
For Vena 365 or Vena Ad Hoc
Vena 365 is hidden, to find it you will need to input the exact ID - WA200002235
Select Continue, specify the Users you want to have access to the Add-in and Deploy.31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 5/9

Step 3: Verify that it was installed successfully.
1. Open Excel as an assigned user.
2. Navigate to the Insert tab, and select Get Add-ins .
3. Navigate to the Admin Managed tab, and select the appropriate Add-in.
4. Select Add. You should see an Excel notification that the Add-in has been successfully
installed and is added to your Insert ribbon.
Step 4: Toggle Centralized Deployment
1. Log in to Vena.
2. Navigate to the Admin tab.
3. Select the Policies page.31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 6/9

4. Select Server Properties from the sidebar.
5. Add the property toggleCentralDeployment.
6. Set the toggle to true.
Step 5: Download a Vena template and use it
When you download a Vena template, we inject some information in the Excel file, including the
property that decides whether the file is trying to access the Central or Store Add-in. This means
that after Step 4, you will need to download a new template to have the settings applied.
Cause
This happens when your Company or IT does not allow end users to install Add-ins directly from
the Microsoft Store.31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 7/9

Keywords
acquisition, execution, office, 365. Microsoft, individual, store, Add-ins
Was this article helpful?
0 out of 1 found this helpful
Related articles
How-To: Using Vena Ad Hoc To View Your
Data and Make Simple Reports
Reference: ETL Guide - 3 - Command Line ETL
Reference: Writing Expressions (MQL & HQL)
Troubleshooting: Intermittent Issue With Vena
365 Panel Not Loading
How-To: Updating Your SSO Certificate in
VenaRecently viewed articles
Troubleshooting: Vena Text Appears in Heavy
Italic Font
Resource: Vena SAML Integration Setup Guide
Resource: Vena Cheat Sheets
Power User Guide for Users with ALL of
Admin, Manager, Modeler and Contributor
Permissions
Guide to Vena Resources31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 8/9

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request31/12/2025, 13:07 Troubleshooting: Microsoft 365 Has Been Configured to Prevent Individual Acquisition and Execution of Office Store Add-ins – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14021500830477-Troubleshooting-Microsoft-365-Has-Been-Configured-to-Prevent-Individual-Acquisition-and-Execution-of-Office-Store-Add-ins 9/9
