# (How To)   Saving Files to Vena Database Intersections

The Vena Help chatbot is currently only available in vena.io.
Vena Solutions/Contributor and Tasks/Performing Tasks Search
Getting Started
Manager
Contributor and Tasks
Contributor Fundamentals
Accessing Templates
Performing Tasks
How-To: Using Scratchpads in
Vena 365
Explainer: Date Formats in Vena
Templates
How-To: Using Scratchpads in
Vena DesktopHow-To: Saving Files to Vena
Database Intersections
Directly upload files to your V ena database (and download them again) right from Excel
using Intersection Files in Vena Desktop.
Why use this feature?
Vena Support
Updated 3 months ago
02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 1/14

How-To: Using a File With
Concurrent Contributor in the
Tasks Tab
How-To: Using Line-Item Details
(LIDs) as a Contributor
How-To: Commenting on
Templates in Excel Online
How-To: Checking Out a File With
Concurrent Checkout
How-To: Using Comments in a
Template or Report
How-To: Viewing Multiple
Datasets at the Same Time With
Cascade
Reference: Vena COM Functions
How-To: Switch Between
Dimensions Using the Choose
Box
How-To: Saving Files to Vena
Database Intersections
Explainer: Redesigned Choose
and Cascade Menus
Reference: GetValues() COM
Function and SingleGetValueYour Vena database not only stores numbers you input for reporting and analysis, but also full
documents like Word files, Excel sheets and PDFs through the Intersection Files feature.
The Intersection Files feature is built into Vena Desktop only (currently unavailable for Vena
365). Users can save and retrieve files from intersections just like with business data. Every file
save is tracked with Drill Saves, and even deleted or overwritten files remain downloadable as
historical versions.
This feature unlocks new possibilities, like using Vena as a document collection platform to track
submissions across your business processes.
In this article, you’ll learn how to:
Upload files to your database.
Retrieve files individually or in bulk.
Access historical versions of uploaded files.
Before you begin

To follow the instructions in this article , you need Manager  or Contributor  access plus permission to
the relevant V ena templates. If Data Permissions  are enabled, ensure you have access to the
database section containing  the files you require . 02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 2/14

Wrapper Function
Explainer: Using the Contributor
Connector for Office Online
Troubleshooting
Modeler
Admin
Vena Ad Hoc
Vena Insights
Vena for Microsoft
PowerPoint
Vena Copilot
Product UpdatesTable of contents

How to
Uploading a file to a Vena database intersection
Downloading files stored in database intersections
Moving files between intersections
Renaming files
Deleting files
Viewing an uploaded file's history and previous versions
Notes
How to
Uploading files to a Vena database
You can upload files to your database with any V ena-enabled input template. Unlike standard values,
files are saved immediately , so there's  no need to select  Save Data.
 Note02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 3/14

1. Open the Vena-enabled template on which you want to upload your file.
This must be an input template. If you are a Contributor, your Vena Manager will likely
have specified the file that you should use.
2. Select the input cell where you want to upload the file (input cells are typically shaded yellow
or a similar bright color).
3. Select Intersection Files in the Vena ribbon, then select Upload File to Intersection.
As with value inputs, files that you upload to Vena can only be saved to bottom-level
intersections (intersections with members at the bottom level of the hierarchy, with
no further child members below them).
Note
If you opened the template while logged in as a Vena Manager, select Edit Data to
toggle to the Contributor view of the Vena ribbon, where you’ll find the
Intersection Files option.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 4/14

4. Select the file from your file browser , then select Open.
5. (Optional) Enter a file description, which will appear in the input cell containing the file. This
description can be used to help you and other users identify the file stored in the cell. You
may change this text at any time. Select OK when finished.
6. Vena will upload the file. When finished, the input cell you selected will contain the file
description and the file ID. The file upload is automatically saved; you do not need to select
Save Data to save the upload.
What is a file ID?
When a file is uploaded to an intersection, Excel does not store the file within the cell
itself. Instead, Vena utilizes a file reference value, which is an alphanumeric string
that designates the file and its location.
This value has two parts, separated by a vertical bar (|):02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 5/14

Downloading files from a Vena database
Excel displays a special value  in cells linked to intersections where files are saved. You can download
these files one by one or collectively in a zip archive.
To download files from a Vena intersection (single or in bulk):
1. In the Vena template containing the uploaded file, select the cell carrying the file.
2. Select the Intersection Files in the Vena Ribbon, then Download File(s).
File description: A user-friendly label (e.g., filename).
File ID: A unique numeric identifier for the file.
Each upload generates a new file ID, even for identical files. The file ID is essential—it
acts as a direct proxy for the file. Any file-related actions (e.g., rename or delete) must
preserve the file ID to maintain the link.
Caution
Changing or deleting the file ID and saving it to Vena will break the link,
making the file inaccessible. To recover a lost file ID, use Drill Saves.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 6/14

3. Your file browser will appear. Select the file name to download (you can change it here if you
like, too), then Save.
Note
If you opened the template while logged in as a Vena Manager, select Edit Data to
toggle to the Contributor view of the Vena ribbon, where you’ll find the
Intersection Files option.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 7/14

4. Once the download is finished, the file browser will reappear again showing the location of
the downloaded file.
5. To download multiple files at once, highlight all the cells that contain files, then select
Intersection Files > Download File(s).02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 8/14

Moving files between intersections
A file uploaded to a Vena template is identified by its file ID, which serves as a stand-in for the
file in Excel. As long as the file ID stays the same, you can copy or move the file between
intersections simply by copying or cutting and pasting its reference value into a destination
intersection.
The destination intersection can even be on another file entirely, if needed.
Renaming files
Although the file ID can't be changed, you can edit the file description before the vertical bar
("|") to rename how it displays in Vena templates. The original filename remains unchanged
when the file is downloaded.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 9/14

In the example above, we can rename Intersection File.docx but not 1585853397240643584.
To rename the file:
1. Select the text that appears before the vertical bar ("|") and make your change. Ensure the
string of numbers remains the same.
2. Select Save Data in the Vena ribbon to save your change.
Deleting files
To delete an uploaded file, highlight the cell it resides it and select Delete or Backspace on your
keyboard.
Viewing an uploaded file's history and previous versions
Because Vena handles uploaded files just like any other intersection value, changes relating to
these files can be tracked with the Drill Saves feature. This includes the ability to download files
Note
Deleting a file reference value removes its link to the specific intersection, but does
not delete the file itself. The file remains stored in your Vena database and can still
be accessed from other intersections that reference it, via Drill Saves, or by restoring
the reference value.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 10/14

which were previously saved to the intersection, but have since been overwritten or deleted.
To view a file's history or download a previous version:
1. Open any Vena-enabled file (may be an input template or report) containing the intersection
where the file is stored.
2. Locate and select the file reference value, then select Drill>Savesin the Vena ribbon.
3. This will open the Save History - Intersection Point window, which shows a history of values
saved to the selected intersection. Deletions of the file, or changes to the file reference value,
are listed under the label Addin Save (instances where the file reference value was deleted are
marked by blanks in the Value column).02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 11/14

Notes
Files can be written to any bottom-level intersection in your database. However, any
intersection may only contain either a value or a file at one time, not both simultaneously.02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 12/14

Uploading a file to an intersection that already contains a value (or writing a value to an
intersection that contains a file) will overwrite the previous contents of that file.
There is no limit on the file type or size that you can upload to your Vena database.
When downloading files in bulk, the selection of cells containing the files to be downloaded
does not need to be continuous.
Was this article helpful?
1 out of 2 found this helpful
Related articles
Reference: Different Cell Types and How They
Affect Data Saves
How-To: Creating and Managing Application
Permissions
How-To: Enabling Line Item Details (LIDs) in a
Template or ReportRecently viewed articles
How-To: Switch Between Dimensions Using
the Choose Box
Reference: Vena COM Functions
How-To: Viewing Multiple Datasets at the
Same Time With Cascade02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 13/14

How-To: Using Drill Functions (Drill Down, Drill
Save and Drill Transactions)
Reference: ETL Guide - 2 - Vena.io ETLHow-To: Using Comments in a Template or
Report
How-To: Checking Out a File With Concurrent
Checkout
Copyright © 2011-2025 Vena Solutions Inc. All rights reserved. Privacy PolicyEnglish (US) Didn't find what you're looking for?
Our application support team is ready to help.
Submit a Request02/01/2026, 11:31 How-To: Saving Files to Vena Database Intersections – Vena Solutions
https://support.venasolutions.com/hc/en-us/articles/360000376311-How-To-Saving-Files-to-Vena-Database-Intersections 14/14
