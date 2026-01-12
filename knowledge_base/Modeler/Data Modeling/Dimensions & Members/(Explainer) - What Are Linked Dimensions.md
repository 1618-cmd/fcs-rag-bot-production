# (Explainer)   What Are Linked Dimensions

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
Member Name CharactersExplainer: What Are Linked
Dimensions?
Linked Dimensions are denoted by a chain link icon () next to the dimension name in the
Modeler tab:
Laura Harris
Updated 6 months ago
02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 1/10

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
Members?By linking a dimension, it can appear in multiple data models simultaneously. In other words, the
dimension exists once within your Vena environment but is associated with several different
data models.
Why link a dimension?
Vena environments often contain multiple data models tailored to specific functions, such as
operational expenses and personnel costs. These models may share common dimensions like
Entity, which outlines company divisions or departments.
Maintaining identical Entity dimensions across multiple models can be time-consuming due to
manual updates. This manual work is prone to errors, causing inconsistencies between models.
Linking dimensions eliminates this issue by synchronizing changes across all linked models. Any
modification—such as adding, renaming or deleting members—automatically updates the
dimension across all models, ensuring consistency and saving time.
Are there any constraints to linking dimensions?
There are a few notes and limitations when utilizing linked dimensions:
Once dimensions are linked, they cannot be unlinked. The only way to revert a linked
dimension is to delete all but one of the linked data models. This reverts the dimension to a
standalone state but also results in data loss from the deleted models. Therefore, linking a
dimension should be considered a permanent action.
You cannot "unlink" a dimension by deleting it and replacing it with a copy.  Deleting a
linked dimension will destroy all intersection data in that data model. If you were to do this,
and then re-add the dimension, all historical data will need to be re-uploaded to the data02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 2/10

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
See all 21 articlesmodel.
Linked dimensions cannot have different granularity between data models. Linked
dimensions are always identical, meaning they have identical member hierarchies across the
models in which they are linked.
Hierarchy changes to the linked dimension in one data model affect all the data
models with which it is linked. Ensure Modelers within your Vena environment are aware
of any linked dimensions and understand that changes to them affect multiple data models.
Linking a dimension affects all linked data models. When you link a dimension, it
becomes connected to all linked data models immediately. Ensure the "linked from" data
model is correct, as this action also applies to any other linked data models.
Linked dimensions respect Application Permissions but may seem otherwise due to
linking mechanics. Only users with specific permissions can modify a data model and its
dimensions. However, if a user can modify all dimensions in a model with a linked dimension,
or the linked dimension itself, changes will reflect in other models that include the linked
dimension, even ones without explicit permissions.
A user can indirectly modify a data model via the linked dimension. This is not a permission
gap but rather an effect of linking. You can set permissions for linked dimensions to allow
modifications by certain users while keeping them read-only for others.
Deleting a data model with linked dimensions does not affect other models. Linked
dimensions remain after deletion, but if the deleted model shared dimensions exclusively
with one other model, the linked dimension icon will vanish from that remaining model.
Deleting a data model with linked dimensions does not affect other models. Normal
dimensions and members are deleted, but linked dimensions remain intact in other models.02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 3/10

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
Product UpdatesProceed with caution when running ETL jobs concurrently from multiple data models
with linked dimensions. Running these jobs at the same time can cause calculation errors
and data conflicts.
How do I link a dimension?
1. Navigate to the Modeler tab, then select Data Modeler > Members.
2. Choose a data model from the drop-down menu, then select the pencil icon (
)to open the
Dimensions sidebar.
 Warning
Linking dimensions cannot be reversed without data loss. Ensure you’ve read the
notes in the previous section before continuing to prevent significant negative effects
on your data models.
It is strongly recommended that you only link dimensions when setting up a new data
model. Linking a dimension with an existing data model is functionally identical to
adding a new dimension, in that doing so will break all previously mapped templates
attached to that data model. This is because every dimension in a data model must
be mapped in the Page, Row or Column mappings for a template to function. When
you link a new dimension, you must update mappings for all affected templates, as
well as any channels that have the data model as a source or destination.02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 4/10

3. Select + Add Dimension to open the drop-down menu.
4. Select Link Dimension.
02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 5/10

5. Select a data model, then select the dimension that you wish to link to your model.
If you have existing data in the data model that you are linking a dimension to, Vena will
automatically extend the model to the ‘Undefined’ member of the new dimension. This is
necessary because an intersection must reference each dimension that exists in the data
model. When linking a new dimension, existing data within intersections must also be
attributed to a member within the newly linked dimension.02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 6/10

6. Select Link.
02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 7/10

7. Select Link Dimension in the pop-up to confirm.
8. Your newly linked dimension will now be listed in the Dimensions section for the selected
data model, marked with a link symbol () .
Which dimensions are suitable for linking?
Link dimensions only when appropriate. Suitable ones often include Accounts, Entity and Year,
which are common in reports across models.
For example, link the Department dimension in Financial and Workforce data models to
synchronize department codes. Similarly, linking the Product dimension across sales and
inventory models ensures consistency in product updates.
Aside from being applicable to multiple data models, dimensions suitable for linking typically
also have the following characteristics:
No variability in structure between data models: Linked dimensions must be identical in
all data models. They work best for dimensions that naturally stay the same over time. For
example, an Entity dimension will usually consist of the same entities, such as 1 - Canada and
2 - USA, regardless of the data model. If a dimension is likely to need specific changes for
different models in the future, it is not suitable for linking because it cannot be unlinked.
02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 8/10

Tendency to require hierarchy changes: Hierarchy changes refer to modifications in the
structure or levels within a dimension, such as adding new departments or changing
department names. Linked dimensions are useful if such adjustments are needed because
the change only needs to be made once, and it will automatically apply to all data models
that use the linked dimension. However, dimensions that rarely or never require changes,
such as a Period dimension (e.g., months of the year), may not benefit from being linked.
In all cases, you should carefully consider the potential downsides before linking a dimension,
remembering that the process is irreversible.
Was this article helpful?
4 out of 4 found this helpful
Related articles
Explainer: What Are Unmapped Dimensions
and Default Members?
How-To: Assigning Dimension Types and
Standard Members
How-To: Data Model Series (Part 1): Creating a
Data Model
How-To: Building Alternate HierarchiesRecently viewed articles
How-To: Copy Data in Bulk and Save
Versioning Configurations in Modeler
Explainer: What’s the Difference Between an
Alternate Hierarchy and Calculated Members?
How-To: Search for Members, Attributes,
Aliases and GL Codes With the Modeler
Search02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 9/10

How-To: Bulk Attach/Detach Attributes and
Filter by AttributesHow-To: Bulk Attach/Detach Attributes and
Filter by Attributes
How-To: Bulk Updating Dimension or
Hierarchy Member Names
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 14:08 Explainer: What Are Linked Dimensions? – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360055067111-Explainer-What-Are-Linked-Dimensions 10/10
