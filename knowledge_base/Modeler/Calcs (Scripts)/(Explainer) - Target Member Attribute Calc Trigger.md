# (Explainer)   Target Member Attribute Calc Trigger

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Calcs (Scripts) Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Functions
Calcs (Scripts)
Explainer: Target Member
Attribute Calc Trigger
Reference: Sparse CalcsExplainer: Target Member Attribute
Calc Trigger
With target member attribute calc triggers, attaching an attribute referenced in a
calc to a member is easier and more intuitive than ever! Read on to learn more about
this feature and how it can help keep your data current and accurate.
Laura Harris
Updated 1 year ago
02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 1/9

Reference: Vena Calcs - 1 -
Managing Scripts
Reference: Vena Calcs - 2 -
Notation and Syntax
Reference: Vena Calcs - 3 - Data
Types
Reference: Vena Calcs - 4 -
Operators
Reference: Vena Calcs - 5 -
Functions
Reference: Vena Calcs - 6 -
Conditional Statements
Reference: Vena Calcs - 7 -
Currency Conversions
Reference: Vena Calcs - 8 -
Examples
Reference: Vena Calcs - 9 -
Troubleshooting
Troubleshoot: Calc Target
Contains Data Even Though It
Shouldn’t
Troubleshooting: Calc Conversion
Not Working or Zero Values
AppearingWhat is a target member attribute calc trigger?
When writing calcs in vena.io, users can leverage Attribute functions to further scope out
member sets for calculations. Previously, when you added a new attribute to a member to
include it in the target scope of a calc, you had to manually deploy the calc to update values. Up
until now, Vena only triggered calcs automatically after data saves/changes.  With the target
member attribute calc trigger, you can now attach an attribute to a member to include it in
the scope of an existing calc, and Vena will automatically trigger the calc to run and run an ETL
job to calculate the affected scope.
Why should I use this feature?
Historically, when you attached an attribute referenced in a calc scope to a member (or
members), you had to deploy the calc manually to keep your intersections up to date. With the
target member attribute calc trigger, you don’t have to worry about manual deploys when
updating your members with new attributes. With the target member attribute calc trigger, you
can attach an attribute referenced in a cal to a member and Vena will automatically trigger the
calc to deploy via an ETL job. This feature ensures the maintenance of attributes referenced in
calc scopes are always up to date and data in your cube remain current and relevant.
How do I use the target member attribute calc trigger?
When you attach an attribute that’s referenced in the scope of a calc to a dimension member (or
members), Vena triggers the calc to start an ETL job that runs the calc and updates the new
target scope values.02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 2/9

Troubleshooting: Calc Is Not
Triggering or Calculating After
Data Load or Import
Troubleshooting: Calc Script
Using .BottomLevel() and
.Exclude() in a Tuple Not Working
Properly
Troubleshooting: No Values
Generate for a Reporting
Currency
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesIn the following example, the scope of this calc is based on the attribute (FX).
1. Identify the calc with the corresponding attribute in the calc scope. In the example below we
have a simple calc statement, including an .Attribute() calc function.
Scope {[Account.Balance Sheet].Leaves() .Attribute("FX") , [Year.2019]}
@this=[Year.2020] +1
End
Caution
In order for this feature to work, your calc must utilize this attribute function to
define a subset of members in scope.02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 3/9

2. Navigate to the Modeler tab and select the data model that corresponds to the data model
where the calc exists and where the relevant attribute can be found.
3. Select a dimension to manage the attributes associated with that dimension’s members.
4. Use the checkboxes to the left of the member names and select the members that you want
to update.
5. Select the Actions menu. Select Attach Attributes from the drop-down list.
02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 4/9

6. Use the drop-down list in the Attach Attributes pop-up to select your desired attribute that is
referenced in the calc script. In this instance, the attribute “FX” is included in the active calc
from step 1.
When you attach an attribute referenced in a calc scope to one or more members using bulk
attribute attach, you will see a message that will let you know that you are attaching an
attribute referenced in a calc.02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 5/9

If you want to continue with attaching the attribute(s), select Save.
7. Saving your selection will trigger Vena to start an ETL job to deploy the calc. You should see
two confirmation messages at the left corner of the screen:
One message will confirm that the attribute attachment was successful; the other will confirm
that an ETL job has begun. You can further click the hyperlink “ETL page” to go to the History
tab and see the progress of the calculation.
8. Other ways to update attributes (in addition to bulk attach attributes):02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 6/9

1. Single-member add/edit - You can also create or edit individual members and attach
attributes at that time and this feature will also be activated in the New Modeler if the
attribute is included in a calc scope:
2. ETL attribute upload - In both the New and Old Modeler, users that are updating
member Attributes through a .csv upload file will see an extra Calculating step in the ETL
job. This only occurs if the attachment of attributes brings any new members into the
target calc scope of an existing calc.
What if I want to detach an attribute referenced in a calc?
You can detach attributes in similar ways (bulk, single-member edit, ETL). However, they will not
“un-deploy” the portion of the calc that was previously run when that same attribute was
attached. This feature does not “undo” when you detach an attribute (in other words, we do not
remove data from intersections when attributes are detached). If you want to remove an
attribute from a member and revert the calculations, you must perform a full Undeploy from the
Scripts tab. If you choose to simply detach an attribute from a member, any future deployments
of the calc will no longer have that member in scope.
If you want to detach an attribute corresponding to a calc from a member, you must:
1. Detach the attributes on the Members page.02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 7/9

2. Do a full undeploy on the Scripts page. Simply detaching an attribute referenced in a calc
from a member via the Members page will not update the corresponding calc script.
Was this article helpful?
0 out of 0 found this helpful
Related articles
Reference: Sparse Calcs
Reference: Vena Calcs - 1 - Managing Scripts
Reference: Vena Calcs - 2 - Notation and
Syntax
Reference: Vena Calcs - 8 - ExamplesRecently viewed articles
How-To: Using Vena’s Foreign Exchange (FX)
Conversion Function
Reference: Vena’s Foreign Exchange (FX)
Conversion Function FAQs
Troubleshooting: Encountered More Than the
Limit of 1000 Unmapped Members02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 8/9

Reference: Vena Calcs - 5 - Functions Troubleshooting: ETL Error – Cannot Increase
the Number of Members Beyond 400000
Troubleshooting: This Member Does Not Exist
Error During Modeler Search
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:22 Explainer: Target Member Attribute Calc Trigger – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/4412728035341-Explainer-Target-Member-Attribute-Calc-Trigger 9/9
