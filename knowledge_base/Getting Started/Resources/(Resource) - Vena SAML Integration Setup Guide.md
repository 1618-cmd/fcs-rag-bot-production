# (Resource)   Vena SAML Integration Setup Guide

Vena Solutions/Getting Started/Resources Search
Getting Started
Fundamentals
User Account Management
Support
Product & IT Information
Resources
Guide to Vena Resources
Power User Guide for Users with
ALL of Admin, Manager, Modeler
and Contributor Permissions
Resource: Vena Cheat Sheets
Resource: Vena SAML Integration
Setup Guide
General TroubleshootingResource: Vena SAML Integration
Setup Guide
Introduction
SAML is an XML standard that allows secure web domains to exchange user authentication and
authorization data. With Vena, you can leverage SAML as a method of secure authentication to
Vena.
The Vena SAML integration requires setup on both the customer and Vena environments. In this
article, you will learn how to set up SAML integration for your Vena environment.
Vena Support Team
Updated 6 months ago
31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 1/13

Manager
Contributor and Tasks
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesPrerequisites
To follow the instructions in this article, you will need:
A SAML 2.0 Identity Provider (IdP) Server
A unique sub-domain name that will be appended to vena.io. For example: "companyabc".
Vena SAML Integration Overview
The diagram below describes how SAML 2.0 authentication with Vena is performed:31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 2/13

1. The user attempts to connect to Vena via a browser (i.e., https://<customer
subdomain>.vena.io)
2. Based on the supplied sub-domain name, Vena will generate a SAML authentication request.
The SAML request is encoded and embedded into the URL for the customer’s SSO service.
3. Vena sends a redirect to the user's browser. The redirect URL includes the encoded SAML
authentication request that should be submitted to the customer’s SSO service.31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 3/13

4. The customer decodes the SAML request and authenticates the user.
5. The customer generates a SAML response that contains the authenticated user's username
in accordance with the SAML.
6. The customer encodes the SAML response and returns that information to the user's
browser.
7. After logging in, the user will be redirected back to vena.io, by using the assertion consumer
service endpoint URL. In case this is the first time the user is logging in to vena.io, the user
will be created in Vena and given access only to their profile.
8. Following the user creation in Vena, the customer’s Vena administrator must assign the
required permissions for the user so that the user can access the appropriate Vena
resources.
Guides for different SAML 2.0 IdP
In this guide, we will cover the setup steps for three types of SAML 2.0 IdP:
How-To: Setting Up Azure AD or Microsoft Entra ID SSO With Vena
How-To: Setting Up Azure AD FS SSO With Vena
How-To: Setting Up Okta SSO With Vena
 Note
If you supply a “mail” attribute in your SAML 2.0 authentication response attributes,
the email domain name must be a valid domain alias on vena.io. If the “mail”
attribute is not supplied, the user email will be created based on the “uid” attribute
and attached to the first domain name registered for this customer in vena.io.31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 4/13

How-to: Setting Up Google GSuite SSO With Vena
How-to: Setting Up DUO SSO With Vena
How-to: Setting Up JumpCloud SSO With Vena
How-To: Setting Up PingFederate SSO With Vena
How-to: Setting Up LastPass SSO With Vena
General Configuration: Vena (vena.io)
Follow these steps to set up SAML in Vena:
1. Log in to vena.io with your client credentials.
2. Navigate to the Admin page.
3. Navigate to the Policies page.
4. Select Single Sign-On.
5. On the right-hand side, you must configure your subdomain (i.e., clientname). This will create
a subdomain on vena.io, such as vena.io. Vena will automatically configure DNS settings for
this subdomain.
6. Include Entity ID in SAML Response. Please see this article for more details.
7. Add your SSO URL (the IdP URL that you have configured internally).
8. Add your SSO Identifier (also known as the "Issuer").
9. Add your Signing Certificate (in text format, without the ---BEGIN CERTIFICATE--- and ---END
CERTIFICATE--- lines).
10. Select Disable email/password login for SSO users option if you want to restrict your users
from logging in with their usernames and passwords. This option will force all your end users
to use SSO login.
11. The screenshot below illustrates a sample configuration:31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 5/13

Troubleshooting
If you receive an "Unauthorized" error message when trying to sign in using Single Sign-on, this
is likely because the SAML metadata sent from your Identity provider does not match the
Metadata setup on the Vena Single Sign On Settings page:31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 6/13

If you are encountering this issue, please follow the instructions below to retrieve the SAML
assertion (SAML response), which will help with troubleshooting the problem.31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 7/13

1. To start, you will need to download and install Fiddler, which is a free Windows application
that will allow you to retrieve the SAML response. You can download it here.
2. After installing Fiddler, launch the program and it will immediately begin capturing all your
web traffic. You can press F12 to toggle the capture on or off.
3. Ensure Fiddler is capturing, then switch to your web browser and sign in to Vena using Single
Sign-on. Fiddler will capture the SSO process in the background.
4. When you see the Unauthorized error message on the Vena login page, you can return to
Fiddler and stop the capture (with F12).
5. Review the trace provided by Fiddler, and you should see the entry displayed in the
screenshot below ("302 HTTPS vena.io /auth/saml"):31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 8/13

6. In the pane on the right side of the Fiddler window, select the WebForms tab and then right-
click the SAMLResponse Value field. In the menu that appears, select Send to TextWizard.
7. TextWizard will open and display the SAML assertion in Base64 format. To decode this to
XML, find the drop-down menu next to Transform: and select From Base64:31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 9/13

8. The assertion will then be displayed in the lower pane in XML format: from here, you can
extract the metadata to see what information is not being sent to Vena, causing the log-in
issue.
9. Look through the assertion for the <X509Certificate> attribute, which contains the signing
certificate of your identity provider. Compare the text contained in this tag to the Certificate
field on the Vena Single Sign-on Settings page: these must match exactly.
Look through the assertion for the Issuer attribute. This should exactly match the Issuer
field on the Vena Single Sign-on Settings page.
10. In addition, ensure that the user's email address is being passed as a claim rule. The email
address is very important, as it acts as the user identifier in Vena. In the assertion, this will31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 10/13

look like:
<Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress">
<AttributeValue>testman@vena.cloud</AttributeValue></Attribute><Attribute>
11. To resolve the Unauthorized login issue, modify the settings on the Vena Single Sign-on
Settings page to match what is returned in the SAML assertion. If you need assistance with
doing this, please contact Vena Support for help.
Notes and Limitations
1. If you are using ADFS, the SSO "Identifier" field needs to be set to http:// protocol not
https:// protocol.
2. The following attributes are what we use for email and name.
for email -> `mail`, `e-mail`, `uid`
for first name -> `givenName`, `FirstName`,
for last name -> `sn`, `LastName`
for full name -> `cn`
31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 11/13

Was this article helpful?
3 out of 5 found this helpful
Recently viewed articles
Resource: Vena Cheat Sheets
Power User Guide for Users with ALL of Admin, Manager, Modeler and Contributor Permissions
Guide to Vena Resources
Reference: Restricted File Types in Vena
How-To: Clearing Your Browser Cache
Didn't find what you're looking for?
Our application support team is ready to help.31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 12/13

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request31/12/2025, 13:06 Resource: Vena SAML Integration Setup Guide – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/201874959-Resource-Vena-SAML-Integration-Setup-Guide 13/13
