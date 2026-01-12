# (How To)   Set Up a Sage Intacct Connector and Data Feed

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Transformation & Integration/Sage Intacct Integration Search
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
ETL JobsHow-To: Set Up a Sage Intacct
Connector and Data Feed
For more information about native connectors and data feeds (how to edit, delete, preview, etc.)
and links to other native connectors, please click here.
Table of contents
Laura Harris
Updated 1 year ago
05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 1/17

Data Querying
Vena Tables
Microsoft Fabric
Integration
Business Central
Integration
NetSuite Integration
QuickBooks Integration
Power Automate
Integration
Power BI Integration
Sage Intacct Integration
How-To: Finding an Object
Name in Sage Intacct
How-To: Set Up a Sage Intacct
Connector and Data Feed
Explainer: Sage Intacct
Connector Update
Troubleshooting: Sage Intacct
ETL Error There Are Too Many
Operations Running for This
CompanyHow to
Intacct connection
Create a Web Services Connection in Intacct
Set up an Intacct connector
Intacct data feed
Set up an Intacct data feed
Limitations
How to
Intacct connection
The Intacct connection allows you to set up your access credentials so that you do not need to
enter them each time the Integration tool queries Intacct.
If you would like to create an Intacct connection, you must also create a separate Web Services
Connection on the Intacct side, which is required for the Vena-side Intacct connection to
function.
Create a Web Services Connection in Intacct
Before you can create a working Intacct connection in Vena, you must first create a
corresponding Web Services Connection in your Intacct account.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 2/17

Troubleshooting: Sage Intacct
ETL Error There’s an Error With
the Value for Field STATE.
Value: [P]
Troubleshooting: Sage Intacct
ETL Error Unable to parse
Query value: X != 'X'
Troubleshooting: ETL – There
Are Missing Records in the
Batch
Troubleshooting: Sage Intacct
ETL Error - A Request’s Function
With the Control ID Is in
Process
Troubleshooting: Response
From Intacct – the Period Filter
Is Required
Troubleshooting: Sage Intacct
ETL Error Check the Fields Exist
and Try Again
Troubleshooting: Sage Intacct
ETL Error - The Service Is
Temporarily Offline
Troubleshooting: ResultID From
Sage Has X Fewer Remaining
Records Than ExpectedTo create a Web Services user:
1. Sign in to Sage Intacct.
2. Navigate to Company > Admin > Users, roles & groups, then click the (+) sign beside Web
Services users.
3. Enter a unique User ID.
You cannot reuse the user ID of an existing standard user for a Web Services user.
The user ID must be unique and cannot be changed once saved.
4. Enter the user's Last name and First name.
5. Enter the user's Email address.
This field is required whenever the admin initiates a password reset.
Because each user is related to only one contact record, this Email address must match
the Primary email address of the associated Contact name. If no contact in Contact
name is chosen, the automatically generated contact record will use this email address.
Before you can edit the Email address of a user, you must first edit the Primary email
address of the associated Contact name to avoid system errors. If you do not have an
associated contact assigned to this user, you can edit the email address as usual. Click the
View icon beside Contact name to edit the contact information directly from the User
Information page.
6. In Contact name, you can either select an existing contact, create a new contact, or allow a
contact to be automatically generated for you based on the User ID. Learn more about
Contacts.
If there is an existing contact record for the user, be sure to select that contact record.
Linking a Web Services users to an employee05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 3/17

Troubleshooting: Error With
Intacct Request: IP Address
Denied
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
Destinations
How-to: Vena Integration: Part 6
– Channels & Field Mappings
How-To: Restoring Data That Has
Been Accidentally Overwritten or
Deleted
How-To: Create Automatic
Channel Mapping With Map byIf there isn't an existing contact record that you can select, you can manually add one by
clicking the Contact name drop-down menu and then clicking Add.
If you do not choose a contact in Contact name, then a new contact name will
automatically be generated for this user. The new contact will use the user ID as the
Suggested contact name (also a unique ID field) of the new, associated contact record.
See Contacts for more information.
7. Enter a User name to identify the person in the Web Services Users list.
If the user is also an employee, the User name does not need to be the same as the name
used in the related employee record.
8. Select a User type for the user. User type controls the maximum features available to the
user, while permissions set what a user can actually do within those restrictions. Learn more
about what each user type can do.
9. For a Business user type, determine whether the user has Admin privileges. If you don't
want the user to be an administrator, click Off. Otherwise, select either Limited or Full.
A user with administrator privileges is given the highest possible level of system access,
including the ability to:
Configure and subscribe to applications
Create users
Assign permissions to users
A full administrator has complete administration privileges, including the ability to create
other full administrators as well as access to all features in Platform Services, which let
admins create and change pages in Intacct. Additionally, in role-based companies, full
administrators also have the ability to use the Try Role feature. Limited administrators
have all administration privileges, except for the aforementioned items.Learn more about
administrator privileges.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 4/17

Name
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product Updates10. You can disable the user's ability to sign in by changing the Status from active to locked-out
or inactive. Learn more about the meaning of each status.
New users can only be created with a status of Active or Locked out. You can edit a user after
creation to change its status to Inactive.
11. In the Roles Information tab, be sure to assign a role that has access to the general ledger
subscription. This must be done in order for the API to work correctly:
12. Click Save when you are done entering the user's information.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 5/17

When the Verify your identity pop-up appears, enter your own password as verification of your
identity. Your new Web Services user will receive an email with their user ID information.
When you are prompted for a Sender ID, enter the following (case-sensitive):
VenaSolutionsMPP*
          *See instructions, below, on where to enter the Sender ID.
Navigate to the Company tab and select the Company option. Select the Setup tab and then click
on Company.
05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 6/17

On the Company Information page, click on the Security tab.
05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 7/17

Scroll down to Web Services Authorizations and add VenaSolutionsMPP (case sensitive).
Complete the instructions (above) to finish setting up the Web Services Connection in Intacct,
then return to Vena.
Set up an Intact Connector
After completing the preceding steps, you can create the Intacct connection in Vena.
1. Open the Modeler tab in vena.io.  and select Data Transformations in the sidebar.
2. Select the Connections option in the sidebar tab.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 8/17

3. Once you've opened the page, select the +New Account button:
05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 9/17

4. Using the Select Account Type drop-down menu, select Intacct as the account type.
5. Once you have the Intacct Web Services Connection in place, you can create the Intacct
connection in Vena. When you create a new connection and select Intacct as the account
type, additional fields will appear.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 10/17

For help completing the fields, see below:
AName field:Type in a name of your choice. This name will be displayed in the Available
Accounts section to help you identify this connection.
BIntacct Company ID field:In this field, type in your Intacct Company ID (which you can
obtain from Intacct).
CIntacct Username field:Type in your username to log in to Intacct.
DIntacct Password field:Type in your password to log in to Intacct.
Once you have completed all the fields, select Connect to complete the connection setup. The
new Intacct connection will now appear under your Available Accounts list. 05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 11/17

Intacct data feed
Set up an Intact data feed
1. Open the Modeler tab in vena.io.  and select Data Transformations in the sidebar.
2. Select the Data Feeds option in the sidebar tab.
3. Once you've opened the page, select the +Add New button.
4. In the Add New Data Feed sidebar, you will be guided through a four-step integration
process that begins with selecting your source. Once you have selected your source,
click Next: Select Connection:
05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 12/17

In the Select Connection box, use the radio buttons to select the connection you wish to use.
Once you have done this, click Next: Select Data:
Enter a query to retrieve the Intacct data of your choice*:
*The Intacct query must be performed for any Intacct feeds created prior to August 2019. For
Intacct feeds created after August 2019, see below for details:05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 13/17

1. Name: Use this field to create a unique identifier for your data feed.
2. Object: Defines the Intacct table object from which you want to draw data, e.g. GLACCOUNT.
You can find more information about Intacct object codes by selecting this link.
You can find more information about Intacct Relationship Diagrams by selecting this link.05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 14/17

3. Fields: Specifies the names of fields within the Intacct object to include, e.g. ACCOUNTTYPE,
RECORDNO, etc. Multiple fields can be included by separating them with a comma. You can
also specify * to include all fields present in the object.
4. Query: Used to specify the WHERE query to define what data to draw from the specified
object and fields.
5. Add Another Feed (optional): Used to create additional feeds from the same Intacct source.

Limitations
      Vena can only pull data from Intacct into Vena.io, it cannot push data back to Intacct.
Was this article helpful?
2 out of 2 found this helpful
Related articles Recently viewed articles05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 15/17

How-To: Set Up a Business Central Connector
and Data Feed
How-To: Installing the Vena Suite Bundle for
NetSuite
How-To: Using Scratchpads in Vena 365
Vena Insights Series (Part 1) - Introduction to
Vena Insights
How-To: Setting up Data Validation RulesHow-To: Finding an Object Name in Sage
Intacct
Troubleshooting: Unable To Connect to Vena
Insights Connector
Troubleshooting: Vena Insights Connector
Intersection Values Showing as Zero
Troubleshooting: Vena Insights Connector
Data Model Intersections or Values Table Is
Blank
Troubleshooting: Vena Insights Connector
Load and Transform Data Buttons Grayed Out
Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 16/17

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) 05/01/2026, 12:45 How-To: Set Up a Sage Intacct Connector and Data Feed – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360034562112-How-To-Set-Up-a-Sage-Intacct-Connector-and-Data-Feed 17/17
