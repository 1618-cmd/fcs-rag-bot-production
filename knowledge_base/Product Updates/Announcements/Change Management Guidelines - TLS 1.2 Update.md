# Change Management Guidelines   TLS 1.2 Update

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Product Updates/Announcements Search
Getting Started
Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena CopilotChange Management Guidelines: TLS
1.2 Update
Overview
Laura Harris
Updated 1 month ago
06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 1/10

Product Updates
Vena Software Updates
Vena Desktop Software
Updates
Announcements
Product Release Announcement:
Suppress Zeros Now Available in
Vena Ad Hoc
Product Release Announcement:
SSO Now Available in Vena Ad
Hoc
What's New in Vena: Spring '25
Release
What's New in Vena: Winter '25
Release
What's New in Vena: Fall '24
Release
What's New in Vena: Summer '24
Release
What's New in Vena: Winter '24
What's New in Vena: Fall '23(November 2025) Vena supports TLS 1.2.  After February 16, 2021, users and applications that
continued to use TLS 1.0 or TLS 1.1 were unable to access specific Vena functionality.  Read on to
learn more about these changes and how they will impact you.
Table of contents
Q&A
What is TLS?
What is the change?
Why is this happening?
How can I avoid a service disruption?
Vena Add-in
How do I tell what version I'm currently on?
How do I update my Add-in?
ETL Command-Line Tool & Java Version
Overview of Required Versions
Excel Add-in & .NET
Internet Browsers
API Integrations06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 2/10

What's New in Vena: Fall '25
Release
What's New in Vena: Summer '25
Release
Resolved - Change Management:
Important Notice - Excel Version
Compatibility Issue with Vena 365
Whats New in Vena: Spring '24
Release
What's New in Vena: Summer '23
Release
What's New in Vena: Spring '23
Release
What's New in Vena: Winter '23
Release
What's New in Vena: Fall '22
Release
What's New in Vena: Summer '22
Release
Change Management Guidelines:
Microsoft Ending Support for
Internet Explorer
Change Management Guidelines:
User Audits & Vena Support UserQ & A
What is TLS?

TLS stands for “Transport Layer Security” (formerly known as SSL), which allows digital devices to
communicate over the internet securely without their transmissions being vulnerable to outside
parties. TLS ensures that a connection to a remote application is to the intended application
through encryption and identity verification.
What is the change?
Vena disabled support for TLS 1.0 and TLS 1.1 connections on February 16, 2021. Thereafter,
customers using applications that still use TLS 1.0 or TLS 1.1 will be unable to access Vena
functionality.
Why is this happening?
Vena is committed to helping customers improve their security by using modern, secure
protocols. This means ensuring you use up-to-date versions of all protocols and software. TLS
1.0 was released in 1999, and TLS 1.1 in 2006. Both were depreciated in 2020. By moving to the
TLS 1.2 encryption protocol, which aligns with PCI security compliance standards, we will
continue to ensure the highest security standards are maintained, and your data remains safe.06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 3/10

Tenant Access
What's New in Vena: Spring '22
Release
See all 30 articlesHow can I avoid a service disruption?
After Vena disables TLS 1.0 and TLS 1.1, any inbound connections to Vena that rely on TLS 1.0 or
TLS 1.1 will fail. The action required by your organization will depend on which Vena services you
use and which operating systems you use to do them. Below you will find information on how
the security updates will impact the Vena Add-in and the ETL Command Line Tool:
Vena Add-in
If you are a user (or you manage users) who works with the Vena Add-in, you will need to
confirm the following:
1. .NET Version - All users will need to be on .NET 4.5 or above
2. Add-in Version - All users must be on at least the Fall 2019 release (1.2019.1112.1204), which
was released November 12, 2019. We highly recommend that users update to the latest
version of the Add-in.
You can find all past and current Release Notes for the Vena Add-in by clicking here.
For MSI users, please reach out to Vena Support to get the latest MSI file.
Info_Icon_Small.png Info06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 4/10

How can I tell what version I’m currently on?
You can find out what version of the Vena Add-in you have installed on your desktop by
following the directions in this article.
How do I update my Add-in?
In order to update your Add-in, you can follow the instructions listed in this article.  If your Add-
in is not updated by the February 16th deadline, the only way to update after will be a complete
re-install of the Add-in, as connections to our update server will require TLS 1.2 connections as
well.
ETL Command-Line Tool & Java Version
If your organization uses the ETL Command-Line Tool, you will need to ensure that the Java
version that you are using supports TLS 1.2Click here for instructions on how to uninstall your
old version of Java.
Mac users who are using the Vena Connector do not need to take any action as
updates occur automatically. 06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 5/10

We also recommend you take this opportunity to download the latest version of the .jar file,
although this is not mandatory.  The newest .jar file can be found here: https://etl.vena.io/
If your ETL Command-Line Tool does not work even after you have confirmed that your .jar
version and Java version are up-to-date, please contact Vena Support.
Overview of Required Versions
Add-in & .NET
Version Compatibility Notes
.NET Version Users will need to be on .NET 4.5 or
above
Click hereto learn how you can find out
what version you have installed.
Add-in Version You will need to have (at minimum) the
Add-in version that was released on
November 12, 2019, installed on your
desktop.06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 6/10

You can find out what version of the
Vena Add-in you have installed on your
desktop by following the directions in
this article.
The version number for the Nov.
12/2019 release is as follows:
1.2019.1112.1204
We highly recommended users
update to the latest Add-in version.
Internet browsers
You and your users may experience issues accessing Vena if you are using an unsupported
browser or if you have disabled TLS 1.2. You can test whether your browser supports TLS 1.2
using Salesforce.com’s TLS test site:
https://tls1test.salesforce.com/s/
This test site has TLS 1.0 and TLS 1.1 disabled.
Browser Compatibility Notes
Microsoft Internet
Explorer (IE)Compatible with the most recent version (IE 11), regardless of the
operating system.06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 7/10

Google Chrome Compatible with the most recent version, regardless of the
operating system.
Mozilla Firefox Compatible with the most recent version, regardless of the
operating system.
 ETL Command-Line Tool - API Integrations
The ETL Command-Line Tool and API Integrations are interfaces or applications – including
mobile apps and desktop clients – that are separate from Vena but connect to Vena. If you have
any API Integrations or use the ETL Command-Line Tool, please ensure that TLS 1.2 encryption
protocols are enabled in those integrations.
Version Compatibility Notes
JDK 7 (versions 1.7.0_131-b31 and later)Minimum version required
Java 8 (version 1.8) Recommended version
OpenJDK 8Recommended version06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 8/10

Was this article helpful?
2 out of 2 found this helpful
Related articles
How-To: Updating Vena DesktopRecently viewed articles
What's New in Vena: Spring '20 Release
Change Management Guidelines: NetSuite
Saved Searches Export Update
What's New in Vena: Spring '21 Release
Change Management Guidelines: Numerical
Identifiers
What's New in Vena: Summer '2106/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 9/10

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request06/01/2026, 14:07 Change Management Guidelines: TLS 1.2 Update – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360041122871-Change-Management-Guidelines-TLS-1-2-Update 10/10
