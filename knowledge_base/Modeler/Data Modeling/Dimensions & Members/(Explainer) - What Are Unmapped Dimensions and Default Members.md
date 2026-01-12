# (Explainer)   What Are Unmapped Dimensions and Default Members

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Modeler/Data Modeling/Dimensions & Members Search
Getting Started
Manager
Contributor and Tasks
Modeler
Modeler Fundamentals
Data Modeling
Dimensions & Members
How-To: Assigning Dimension
Types and Standard Members
Explainer: What Is the
Maximum Number of
Dimension Members and
Member Name CharactersExplainer: What Are Unmapped
Dimensions and Default Members?
Not sure what an Unmapped Dimension or a Default Member is, or how to use
them? Read on to learn more.
What is the Default Member?
Vena Support Team
Updated 6 months ago
02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 1/12

How-To: Combining
Dimensions Using Multiple
Expressions for Slices to Clear
How-To: Restoring a Dimension
Member That Was Mistakenly
Deleted
How-To: Bulk Updating
Dimension or Hierarchy
Member Names
How-To: Bulk Attach/Detach
Attributes and Filter by
Attributes
How-To: Search for Members,
Attributes, Aliases and GL
Codes With the Modeler Search
Explainer: What’s the Difference
Between an Alternate Hierarchy
and Calculated Members?
How-To: Copy Data in Bulk and
Save Versioning Configurations
in Modeler
Explainer: What Are Linked
Dimensions?
Explainer: What Are Unmapped
Dimensions and Default
Members?While using the Data Modeler, you might have noticed a member—probably named Default
member—with an
icon next to it. You've may have seen the same icon appear next to a Pin
as Default Member option in the menu that appears when you right-click on any member:
02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 2/12

Reference: Creating a
Calculated Number That
Excludes a Member
Reference: Dynamic Member
Sets
How-To: Building a Custom
Roll-up Using Calculated
Members
Reference: Exporting
Hierarchies in Vena Using HQL
Reference: Naming Guidelines
for Dimension Members
How-To: Using Attribute
Aggregation
Reference: Export Intersections
and Line-Item Details
Troubleshooting: Error While
Processing the Model Slice
Expression When Previewing
Intersections
Troubleshooting: Versioning
Copy To and Copy From must
Contain the Same Set of
Dimensions
See all 21 articlesThe
icon indicates that this member is the current Default Member for this dimension. Pin
as Default Member gives you the option of changing that designation to any other member. But
what does this mean? To understand what the Default Member is, we first have to look at the
Unmapped Dimension feature, and the mechanics of mapping a Vena template.
 The "Default Member" vs.  The "Default member" member
In the screenshot below , there is a member named  "Default member" , and it also  is the
Default Member for its dimension. They're  not the same thing, so don't  confuse them!
A member named "Default member" is created whenever you set up a new
dimension. While it is also automatically the Default Member for a newly created
dimension, they are not always one and the same. Because you can use Pin as Default
Member to make any member the Default Member, it's possible to have a member
named "Default member" that is not actually the Default Member. Throughout this
article, whenever 'Default Member' is mentioned, it refers to the concept, not the
member with that name.
Also, don't worry if you don't have any member named "Default member" in your data
model. This is common because, historically, many Modelers would often delete this
member right after creating a dimension. Likewise, it's fairly likely that none  of your
members is currently set as the Default Member (i.e., no member has the
  icon). R ead
on below to learn why.02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 3/12

Managing Your Model
Functions
Calcs (Scripts)
Data Transformation &
Integration
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesWhat is an Unmapped Dimension?
In the past, whenever you mapped a Vena template, you had to make sure to map at least one
member from every dimension manually. This is because mappings point at specific data
intersections in your Vena database, and you can only successfully describe an intersection if
you reference all of the dimensions in the data model.
Think of this as being like sending a letter : even if you included the recipient's name, street, city , state
and zip code on the address label, the delivery fails if you leave out the house number . It's the same
way with intersections in your database, as Vena Desktop needs details from every dimension in
your data model to "deliver" the data you want.
Filling unmapped dimensions on Vena Desktop
Vena Desktop's Unmapped Dimension feature relaxes this requirement. While it's still true that
every intersection must be described by using a member from every dimension, you no longer
have to map each of those members manually.
Benefits:
Speeds up template creation, especially for Ad Hoc reports .
Simplifies data model updates —adding a new dimension won’t  break old templates, since it’s
auto-filled with a Default Member .
When you don't explicitly map a dimension, the Unmapped Dimension feature automatically
fills in a member for you to create a valid (complete) mapping. The member it uses for this
purpose is the Default Member.02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 4/12

What is the Pin as Default  option used for?
Now that you know how Unmapped Dimension works, it's logical to conclude that this is where
Pin as Default Member comes in. Is it used to tell Vena Desktop which member to use as the
Default Member?
The answer is both yes and no, because it depends on when the dimension was created. For any
dimension that was created after the Default Member feature first entered beta (March 26,
2018), the automatically created first member (the one named Default member) will also be set as
the Default Member, so there is no need to set it as such (see note).
However, for dimensions that existed before these features became available, none of the
members in the dimension are automatically set as the Default Member. For these dimensions
where no Default Member exists, Unmapped Dimension simply uses a fallback in its place: this
"Default Member by default" is the All Member, a virtual member that represents a parent of all
members in the dimension (it's a "virtual" member because it's an abstraction, rather than a real
member that is listed in the Data Modeler).
 Mapping with Unmapped Dimension
With Unmapped Dimension, you can leave any dimension unmapped while building a
template, in any section or block, and the template will still work. Keep in mind that
you must still map at least one dimension to each row and column, as this defines
where the intersections are located on the template. If you don't do this, Vena
Desktop won't know where to place the data.02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 5/12

This All Member fallback allows Unmapped Dimension to work with all pre-existing dimensions,
but there is an important consideration to bear in mind when you leave a dimension unmapped
that has no set Default Member. Since the All Member will be used in place of the Default
Member in this case, the resulting template can't be used to save data. This is because the All
Member is a parent member, but intersections on an input template must be comprised solely of
members that are at the bottom-level of the member hierarchy.
Therefore, the Pin as Default Member option actually functions as an override:
For old dimensions without a set Default Member, it allows you to specify a bottom-level
member to be used as the Default Member in place of the All Member. This enables input
templates to be created using Unmapped Dimensions.
For new dimensions, it allows you to set a Default Member other than the one that was
automatically set when you created the dimension. This is useful if there is another member
that you would rather use.
You can use Pin as Default Member to make any other member in a dimension the Default
Member, whenever you like. One thing to keep in mind is that, if you make any parent member
the Default Member, you will not be able to create input templates with Unmapped Dimension,
for the reason outlined above.
Important Note
For dimensions created after March 26, 2018 (when the Default Member feature
entered beta), the first member (usually named "Default member") is automatically set
as the Default Member. There's no need for any manual action. (see note).
For dimensions created before March 26, 2018, no Default Member is automatically
set.02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 6/12

What happens if I change or delete the member that is
currently set as the Default Member?
At any time, you can select another member and make it the Default Member using Pin as
Default Member. You can also delete the member that is currently designated as the Default
Member, which will, of course, also unset it as the Default Member as a consequence.
General rules:
If you delete the Default Member and do not set a new Default Member, then the All Member
will become the de facto Default Member.
If you change the member designated as the Default Member, this will take effect
immediately.
All templates will automatically use the new Default Member anytime the relevant
dimension is left unmapped.
If the current Default Member has ever been used to "fill in" for an unmapped dimension on an
input template, and that template has been used to input and save data, then the Default
Member will be associated with intersection values. This means that changing the Default
Member in this case will affect any templates and reports that relied on the old Default Member.
If you created a new dimension between March 26, 2018, and May 16, 2018, you
should check the dimension to see if any member that you are using for another
purpose (i.e., as a "real" dimension member) may be unexpectedly set as the Default
Member. If this is the case, we recommend that you unset it (see the note below for
more information).02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 7/12

Example 1:  a data model with four dimensions
If you map a template using this data model, every intersection would have to be defined by all
four of these dimensions. Now, consider a template on which you mapped dimensions 1, 2 and
3 with specific members, but left dimension 4 unmapped. The Default Member would be used to
complete the mapping. If you now use this template to input and save data, each value you save
will be defined by a set of four members, one of which is always the dimension 4 Default
Member, like this:
Dim 1 Dim 2 Dim 3Dim 4 (unmapped) Value
Widget 1.0 January Sales Default Member 15,000
Widget XL January Sales Default Member 7,200
These values are now tied to these specific sets of members. As long as you don't change either
the mapping of the template or dimension 4's Default Member, these same values will appear
every time you open the template.
However, if you change the Default Member in dimension 4 to a different member and then
open up the same template again, the values you saved previously will no longer appear. Why?
Since dimension 4 now has a new Default Member, all of the intersections on the template will
automatically be defined using that member, like this:
Dim 1 Dim 2 Dim 3Dim 4 (unmapped) Value02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 8/12

Widget 1.0 January SalesNew Default Member
Widget XL January SalesNew Default Member
The only way to retrieve the previous values would be to add a mapping to the template for
dimension 4, setting it to the member that was previously the Default Member.
Changing the Default Member can be problematic, but more importantly, deleting a Default
Member associated with intersection values will also destroy the relevant intersections, resulting
in the loss of that data. As a result, you should always be careful if you're thinking about
changing or deleting a Default Member.
 Best Practices for using the Default Member
Given the potential risks of setting, changing or deleting the Default Member, here
are some recommendations for using this feature:
In general, you should only set a Default Member if not doing so would break
existing templates. The most common case for this would be adding a new
dimension in an existing Vena environment. Here, adding the dimension will
automatically set a Default Member as well. This allows all existing input
templates to keep working without needing to be remapped with the new
dimension (and means you don't have to remember to set a Default Member on
the new dimension).02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 9/12

Questions? Comments? Reach out to us directly at support@venasolutions.com.
(Please include the link to the article for reference.)
Was this article helpful?
If you rely on a Default Member to enable input templates when expanding a data
model, we recommend that you do NOT change it to another member at any
point.
You should only change or delete a Default Member if absolutely necessary, and if
you are confident that it is not associated with any intersection values. This will
typically be the case only if you have just created a new dimension, and the
automatically set Default Member is brand new (and therefore hasn’t been used
on a template yet).
For existing dimensions created prior to March 26, 2018, no Default Member will
be set. We recommend not setting a Default Member on these dimensions and
therefore relying on the All Member when using the Unmapped Dimension feature
on a template. This will reduce the risk of associating intersection values with a
Default Member, at the expense of not being able to leave these dimensions
unmapped on input templates (only reports can be created if you leave a
dimension unmapped that defaults to the All Member).
Templates that rely on Unmapped Dimension are not compatible with the
Contributor Connector Add-In for Mac and Office 365 , Report Books  or Template
Automation .02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 10/12

2 out of 2 found this helpful
Related articles
Explainer: What Are Linked Dimensions?
How-To: Building a Custom Roll-up Using
Calculated Members
How-To: Data Model Series (Part 3): Attributes
and Versioning
How-To: PowerPoint Series (Part 1): Getting
Started With Vena for Microsoft PowerPoint
Troubleshooting: ETL Job Is Stuck in Waiting
for SQL TransformationRecently viewed articles
Explainer: What Are Linked Dimensions?
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Search for Members, Attributes,
Aliases and GL Codes With the Modeler
Search
How-To: Bulk Attach/Detach Attributes and
Filter by Attributes
Didn't find what you're looking for?
Our application support team is ready to help.02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 11/12

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Submit a Request02/01/2026, 14:08 Explainer: What Are Unmapped Dimensions and Default Members? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360002809851-Explainer-What-Are-Unmapped-Dimensions-and-Default-Members 12/12
