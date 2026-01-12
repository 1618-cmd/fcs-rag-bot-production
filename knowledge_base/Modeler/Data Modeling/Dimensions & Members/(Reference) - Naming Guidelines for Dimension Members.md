# (Reference)   Naming Guidelines for Dimension Members

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
Member Name CharactersReference: Naming Guidelines for
Dimension Members
Refer to this article for a list of naming considerations for
dimension members used in Calcs, ETLs & Vena Copilot.
Overview
When naming dimension members, it’s important to follow specific character requirements to
ensure compatibility across Vena features, including Calcs, ETL and Vena Copilot. This article
Vena Support Team
Updated 2 months ago
02/01/2026, 14:10 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 1/5

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
Members?outlines supported characters, known limitations and considerations for multi-language
environments.
Calc Naming Rules
Dimension member names can begin with:
A letter
A number
An asterisk (*)
After the first character, member names can include:
Letters and numbers
Special characters : @ \ - , = < > + ' _ | *

ETL Naming Rules
Caution_Icon_Small.png Caution
Avoid using apostrophes (') in member names. Apostrophes can:
Cause errors when setting Data Permissions.
Split member names into separate words in staging queries.
Apostraphes can be wrapped in quotation marks (") to avoid the issues above.02/01/2026, 14:10 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 2/5

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
See all 21 articlesThere are two known issues with special characters in ETL:
Apostrophes (')
Member names containing apostrophes may fail during drill-across operations due to syntax
errors.
Leading Underscores (_)
If a member name in the first column of an upload file begins with an underscore, the ETL job
may fail to write or update data.
Workaround: Add a space before the underscore ( _). The ETL job will remove the space
during processing.
There are no other known issues with special characters in ETL for Vena Cloud.
Multi-Language and Vena Copilot Support
Unicode characters used in multi-language member names are currently not supported in Calcs
or ETL. The Vena team is actively working on a solution to support these characters.
Vena Copilot Limitation:
Vena Copilot cannot retrieve data from dimension members that contain special characters (e.g.,
ö, ç, ñ).
To ensure compatibility and accuracy, avoid using special characters in member names when
asking Copilot questions. As a best practice, design data models without special characters in
member names whenever possible.
Dimension Member Names Dos and Donts.pdf300 KB02/01/2026, 14:10 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 3/5

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
Product UpdatesWas this article helpful?
4 out of 6 found this helpful
Related articles
Reference: Mapping Efficiencies
Explainer: What Are Linked Dimensions?
How-To: Building Alternate Hierarchies
Explainer: What is Data Model
Standardization?
Reference: Auditability in VenaRecently viewed articles
Reference: Exporting Hierarchies in Vena
Using HQL
How-To: Building a Custom Roll-up Using
Calculated Members
Reference: Dynamic Member Sets
Reference: Creating a Calculated Number
That Excludes a Member
Explainer: What Are Unmapped Dimensions
and Default Members?
Didn't find what you're looking for?02/01/2026, 14:10 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 4/5

Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Our application support team is ready to help.
Submit a Request02/01/2026, 14:10 Reference: Naming Guidelines for Dimension Members – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/207371936-Reference-Naming-Guidelines-for-Dimension-Members 5/5
