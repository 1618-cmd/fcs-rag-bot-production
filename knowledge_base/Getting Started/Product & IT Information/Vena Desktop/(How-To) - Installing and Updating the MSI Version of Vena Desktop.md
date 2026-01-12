# (How To)   Installing and Updating the MSI Version of Vena Desktop

Vena Solutions/Getting Started/Product & IT Information/Vena Desktop Search
Getting Started
Fundamentals
User Account Management
Support
Product & IT Information
Vena and Excel
Vena Desktop
How-To: Validating the
Authenticity of Your Installed
Vena Desktop Add-in
How-To: Removing the V365
Task Pane From Vena Desktop
How-To: Installing and
Updating the MSI Version of
Vena DesktopHow-To: Installing and Updating the
MSI Version of Vena Desktop
Install or update the MSI version of Vena Desktop to deploy the application to single
or multiple users in the organization.
Why use this feature?
The MSI version of the Desktop allows you to mass deploy/silently install the application to single
or multiple users in your organization. This application can also be deployed just like any other
Olalekan Adebayo
Updated 1 year ago
31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 1/10

Reference Guide: Vena Desktop
Keyboard Shortcuts
How-To: Customizing the Vena
Desktop Menu Ribbon
How-To: Updating Vena
Desktop
How-To: Disabling Vena
Desktop Reference in Outlook
and Word
Reference: Vena Desktop
Settings & Properties
How-To: Restoring a Missing
Vena Desktop
How-To: Checking Your Version
of Vena Desktop
Troubleshooting: Unable to
Install Vena Desktop
Troubleshooting: Access to the
path 'Vena Installer.exe' is
denied
Troubleshooting: Vena Desktop
Requires the URLs To Be Added
to Your Internet Trusted Sites
Troubleshooting: Vena Desktop
Requires Higher Version of .NETMSI application.
Before you begin
You must either have administrator rights on your computer or reach out to your IT team to
complete this on your behalf.
Table of contents
Installing the MSI Version of Vena Desktop
Determine if Vena Desktop was installed with the MSI Version
Updating the MSI Version of Vena Desktop
Notes & Limitations
How to
Install the MSI version of Vena Desktop
1. Download the latest MSI version.
2. Save the downloaded file in the C:\Downloads folder. Make sure the name is Venasetup.msi
3. Open the Command prompt.31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 2/10

Framework During Installation
Troubleshooting: Formatting
and Formulas are Not
Displaying as Expected in Vena
Templates
Troubleshooting: Vena Desktop
Application Download Did Not
Succeed
Troubleshooting: Vena Desktop
Application Cannot Be Started
Vena 365
Explainer: What is Central
Deployment?
Resource: System Requirements
for All Vena Platforms and Add-
Ins
How-To: Getting Vena 365 for
Windows or Installing Vena
Desktop
How-To: Using Vena on a Mac or
Office Online With the Tasks Tab
How-To: Getting Vena for Mac or
Office Online
Explainer: What Are Vena
Desktop and Vena 365?4. Select Run as administrat or.
5. Navigate to the folder where the most recent .msi was downloaded.
6. Copy the file’s address directory by right-clicking the address bar.
31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 3/10

How-To: Adding Vena To Trusted
Sites
How-To: Accessing Your Sandbox
Environment
How-To: Using Vena on a Citrix
Machine or Environment
How-to: Checking and Installing
.NET Framework
How-To: Clearing Your Browser
Cache
Reference: Restricted File Types
in Vena
Resources
General Troubleshooting
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc7. Type cd and one space in the Command Prompt.
8. Paste the address you copied in step 6 and press Enter on the keyboard.
9. Type the following command: msiexec /i VenaSetup.msi
msiexec /i VenaSetup.msi - This will bring up a GUI.
msiexec /i VenaSetup.msi /qn - This will be a quiet install.
10. An installer window will open. Select Next.
11. Select Install to complete the installation.
Determine if Vena Desktop was installed with the MSI Version
1. Open Excel.
2. Select Settings in the Vena ribbon.
3. Navigate to the Standard tab.
4. If the Installation type is Not web-installed, this means the Desktop was installed with the MSI
version. Follow the steps below to update the Desktop. 31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 4/10

Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates
5. If the Installation type is Release, this means the Desktop was installed through the Vena
website. Follow the steps in this article to update the Desktop.31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 5/10


Update the MSI version of Vena Desktop
1. Check your current Vena Desktop version by opening Excel and navigating to the Vena tab.
You do not need to be logged in to Vena to do this, you can simply open any Excel document
from your desktop.31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 6/10

2. Select Settings in the Vena ribbon.
In the pop-up window in the top right-hand corner, you will see your current Desktop version.
3. Check the latest version of the Desktop here.
4. If your Desktop is out of date, navigate to the Programs and Features or Add or remove
programs tool.31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 7/10

5. Select all instances of Vena and uninstall them.
6. Once uninstalled, close all Microsoft applications (Excel, Outlook, PowerPoint and Word).
7. Follow the steps to install the MSI Version of Vena Desktop again.
Notes & limitations
The MSI version of Vena Desktop does not automatically update or inform you of any new
updates. We suggest you subscribe to our Desktop Software Updates by selecting FOLLOW,
to be notified when there are new versions of the Desktop.
The MSI version can be used to install the Vena Desktop if you are unable to use the
ClickOnce or exe (executable) version or if you would like to deploy the Desktop to multiple
users in your organization.
Was this article helpful?31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 8/10

4 out of 4 found this helpful
Related articles
How-To: Getting Vena 365 for Windows or
Installing Vena Desktop
Troubleshooting: Unable to Install Vena
Desktop
How-To: Customizing the Vena Desktop Menu
Ribbon
Vena Desktop Software Updates June 24,
2024
How-To: Set Up a Business Central Connector
and Data FeedRecently viewed articles
How-To: Removing the V365 Task Pane From
Vena Desktop
How-To: Validating the Authenticity of Your
Installed Vena Desktop Add-in
Troubleshooting: Enable Content Warning
Appears in Excel When Opening Templates
Reference: Supported and Restricted Excel
File Types
How-To: Enabling the Developer Tab in Excel
Didn't find what you're looking for?
Our application support team is ready to help.31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request31/12/2025, 12:34 How-To: Installing and Updating the MSI Version of Vena Desktop – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/14086937113485-How-To-Installing-and-Updating-the-MSI-Version-of-Vena-Desktop 10/10
