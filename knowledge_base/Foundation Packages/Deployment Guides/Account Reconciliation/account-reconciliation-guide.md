# Account Reconciliation Pre-Configured Solution — Deployment & Template Walkthrough (Transcript)

> **Source:** Training/walkthrough transcript  
> **Primary speakers:** Jordan (Vena consultant), Shiv (technical overview)  
> **Scope covered:** Data model overview, Prepaid reconciliation, GL to Subledger reconciliation, Fixed Asset reconciliation, Bank reconciliation, Financial Close dashboard

---

## 1. Introduction & Purpose (Jordan)

- Jordan introduces a **quick deployment guide** for the **Account Reconciliation (Account Rec) solution**.
- He has implemented the solution multiple times and is familiar with the process required to get projects live.
- **Goal:** Get implementers up to speed on the assets in the template so they can implement the package themselves.

### Agenda (high level)
- Walk through the **data model** in this video.
- Cover templates/reports in subsequent videos:
  - Reconciliation Management template
  - Prepaid Expense
  - GL Subledger
  - Fixed Asset
  - Bank Reconciliation
  - Bad Debt
  - FCM Status Dashboard  
- Separate modular videos so users can watch only what’s in scope for their implementation.

---

## 2. Data Model Overview (Jordan)

### 2.1 Two-Model System
The Account Rec solution uses **two models**:
1. **Generic Account Rec Model** (reconciliation + GL data)
2. **Account Rec Management Model** (qualitative/management metadata)

Jordan notes there is differentiation and explains it below.

---

### 2.2 Generic Account Rec Model (Reconciliation Model)

#### Standard dimensions
- Entity
- Account
- Year
- Period  
(“No surprises there.”)

#### Special dimension: **Source**
Used to distinguish where data is coming from:
- GL
- Subsystem
- “No source” / undefined measure style
- Reconciliation source (used in various places)

#### Measures
- Multiple measures used throughout templates to store reconciliation values.

#### Special dimension: **Item**
- This is where **reconciliation item detail** is stored.
- Reconciling items (outstanding differences) are stored here to make the reconciliation balance.
- There is also the ability to store **journal entries** in this model (via specific item/measure usage).

#### Key point
- **All reconciliation happens here.**
- Reconciliation data (and often GL data) lives in this model.

---

### 2.3 Account Rec Management Model

#### Similar dimensionality, key difference
- Mostly the same dimensions as the reconciliation model **except the Item dimension is missing**.

#### What is stored here
Qualitative / management data such as:
- Preparer
- Reviewer
- Frequency
- Key account indicator
- Tolerances
- Other workflow/control metadata

#### How it is used
- These values appear in templates as **view-only** fields after being saved in the management template.
- They also populate fields in dashboards.

---

## 3. Prepaid Reconciliation Template (Jordan)

### 3.1 Certification Tab (common across templates)
Jordan explains the **Certification tab** is common to all reconciliations and will be referenced by other videos.

#### Retrieval of qualitative fields
Fields such as:
- Key account?
- Currency
- Frequency
- Variance tolerance
- Auto-reconciled indicator  
…are retrieved from the **management model** based on the selected entity and account intersection.

#### Validation summary (checkpoint)
A summary to confirm whether the reconciliation balances:
- Beginning balance
- Amortization (important for prepaid)
- Reconciling items (one-off adjustments)
- In-period additions
- Projected ending balance

This projected ending balance is compared to:
- **Balance per GL load** (retrieved from Vena / client GL system)

If there is a variance (example given: **$40,000**):
- Red highlighting and X’s indicate the reconciler should not submit until investigated.
- Variance threshold rules prevent submission when variance is material.

#### Certification checklist (internal control)
- Checklist item descriptions **flow through** from the management template (pure retrieval).
- Users click **Yes** to complete items and turn X’s into check marks.
- Validation rules can warn (soft or hard) if items are not completed.

#### Certification findings/comments
- A mapped cell for preparer notes to provide context for reviewer.

#### Workflow status (Preparer / Reviewer / Approver)
- Users select their role via measure selection.
- Based on role selection:
  - Certain cells lock/unlock
  - “Submitted / Reviewed / Approved” status is controlled
- Common pattern clients use for reconciliation cover pages.

---

### 3.2 Prepaid Reconciliation Schedule Tab

#### Purpose
Where the client inputs prepaid expenses that amortize over time.

#### Input + MDR retrieval pattern
- Existing prepaids are listed via MDR retrieval.
- A new item is entered in an **input row**:
  - Description
  - Dates (start/end)
  - Amount
  - Expense account (feeds journal entry creation)
- Based on dates, formulas calculate:
  - Monthly amortization amounts per period

After entry:
- User clicks **Save Data**
- Item moves into the MDR list and begins contributing to subtotals.

#### Header summary goal
Target: **zero variance** (GL balance reconciles to prepaid schedule)
Process:
- Start with prior ending balance
- Subtract amortization
- Subtract adjustments
- Add additions
- Derive expected GL balance
- Compare to GL retrieval (grey line pulling from Vena/GL)

#### Reconciling item schedule (similar pattern)
- Used to record known differences so the schedule balances to GL.
- Works like prepaid schedule: input row + retrieval list.

#### Implementation note
Some clients prefer a **flat list** instead of MDR retrieval + separate input row; mapping can be simplified accordingly.

---

### 3.3 Journal Entries Tab (Prepaid)
- Populated from prepaid schedule inputs using **SUMIFs** to calculate:
  - Amount per account/entity per month
- End users post entries in source system.

#### Optional export to source system
- Possible to export from Vena for import to ERP/GL, but Jordan notes it’s not typical and may be out of scope.
- Suggests discussing with the Solution Architect (SA) if required.

#### Validation note
- Debits should equal credits (example indicates a demo may not balance).

#### Prepared status
- Dropdown status (e.g., “Submitted”) can be saved with timestamp for reviewer visibility.

#### Adjusting entry section
- For recording adjustments separately (like reconciling item schedule)
- Provides an audit trail for preparer and reviewer.

---

### 3.4 Hidden Tabs (Prepaid): Lists, Lookups, Mapping Key
Jordan unhid tabs for demo purposes:
- **Lists tab**
  - Provides data validation sources:
    - Entity choices
    - GL account choices
    - Process variables
    - Preparer/Reviewer/Approver lists
- **Lookups tab**
  - Standard template support tab; may not be referenced directly in this template.
- **Mapping Key**
  - Recommended for implementers to understand whether a mapping points to:
    - Management model vs Reconciliation model

---

### 3.5 Mapping & Model Notes (Prepaid)

#### Certification tab mapping
- **All certification tab data points map to the Management model**
  - Includes settings, validation summary, checklist, findings, workflow status.

#### Checklist mapping nuance
- Checklist item labels are retrieved.
- Checklist responses are saved (e.g., to a “Certification Response” measure).
- Some are **column mappings** (B1/B2/B3/B4 patterns) — watch the mapping structure.

#### Validation rules
- If rules are false and user tries Save Data, user receives warning.
- Can be configured as soft or hard warnings.

#### Reconciliation tab mapping
- Ending balance retrieval may need adjustment depending on balance sheet method.
- Even formula-based values are saved for dashboard reporting.

#### Item dimension usage
- Prepaid schedule uses Item dimension and increments item ID to avoid overwriting.
- Reconciling items use a separate rollup (recitem) and similarly increment.

#### Journal entries mapping
- Row mappings capture entity/account/items.
- Measures store JE lines.

---

## 4. GL to Subledger Reconciliation Template (Jordan)

### 4.1 Certification tab (summary)
- Same concept as prepaid:
  - Pulls settings (frequency, key account, currency) from management model
  - Completeness check produces projected ending balance
  - Compared to GL balance retrieval
- In the example, difference is zero → reconciles “to the cent”.

**Important:** Certification tab sections map to the **Account Rec Management model**.

---

### 4.2 GL to Subledger Compare Tab (Core reconciliation)

#### Can reconcile multiple GL accounts at once
- Yes — template supports multiple accounts across columns.
- Example shown: Inventory group account.

#### Dynamic row behaviour by account group
Changing selection (e.g., Inventory → Accounts Receivable):
- Changes measures/rows displayed:
  - Inventory: receipts/transfers etc.
  - AR: new invoices, settled invoices, write-offs, recoveries, etc.

Jordan notes:
- In practice, many clients may not have data sources that tie neatly to this full structure.
- If they do, the template can work very well.

#### Projected ending balance components
- Beginning balance
- Net activity (subsystem)
- Journal entries (formula from JE tab)
- Reconciling items (from reconciling items tab)
- Compared to ending GL balance retrieval

---

### 4.3 Mapping notes (GL to Subledger)

#### Dynamic expression across multiple accounts
- Uses a dynamic expression based on a “select count” on the List tab.
- Likely needs tweaking per implementation.
- Enables multi-account column layout.

#### Measure switching logic
- Each account group has a set of measures in the data model.
- Member-cell + MDR logic maps selected account group to appropriate measures.

#### Reconciling items
- Used for known differences, flows to certification tab as well.

#### Alternative usage
Jordan has also used this template as a “catch-all” reconciliation:
- A place to build up a balance from transactions/items
- Helps clients understand what makes up the ending balance

#### GL detail and Subledger detail tabs
- Pull from staging tables (periods configurable via staging query logic)
- Useful when clients already have drill-through transaction tables
- Subledger detail may or may not be available depending on client systems

#### Journal entry tab
- Similar to other templates:
  - Select JE line count (drives hide/show)
  - Record JE number and lines (may need customization to match ERP numbering)

---

### 4.4 Certification Status tab (hidden but important)
Purpose:
- Values are saved at **group account** level on certification tab.
- Management views often need **bottom-level account** visibility.

How it works:
- A dynamic expression allocates group-level values down to individual accounts.
- Particularly important for GL balances.
- Certification responses are group-wide (yes/no applies to entire group).

**Implementation tip:**  
If the dynamic expression changes in GL/Subledger compare, replicate updates in **Certification Status** logic to keep allocations consistent.

---

### 4.5 List tab logic (group vs single account)
- Pulls entity/account selections and is mapped to management model.
- Feeds staging queries via “my query” tags.
- Contains logic to distinguish:
  - Grouped accounts (multiple accounts)
  - Single account reconciliations (one-to-one)

If no map/match is found, it assumes grouped account and adjusts selection logic accordingly.

---

## 5. Fixed Asset Reconciliation (Shiv)

### 5.1 Purpose
Reconcile fixed asset accounts from subledger to GL using a continuity (roll-forward) schedule:
- Opening balance
- + Additions
- − Disposals
- (+ Transfers, if applicable)
- +/− Depreciation
- + Reconciling/adjustment items
= Closing balance

---

### 5.2 Certification tab
#### Summary section
Shows:
- Beginning balance (subledger)
- Additions
- Disposals
- Intercompany transfers
- Depreciation
- Reconciling/adjustment entries

#### Green search icons
- Provide references to source cells driving each summary value.

#### Comparison / unidentified difference
- Compares calculated reconciliation balance to GL balance (from GL file load)
- Unidentified difference indicates whether reconciliation work is required.

#### Certification summary panel (workflow)
- Preparation / Review / Approval stages
- Shows roles, users, timestamps, status

#### Activity settings
- Key account
- Frequency (monthly/quarterly/yearly)
- Auto reconcile
- Tolerance

#### Certification checklist + comments
- Checklist ensures steps aren’t skipped (compliance/internal control)
- Comments allow context handoff across workflow steps

---

### 5.3 Schedule tab
Consistent structure:
- Certification tab
- Schedule tab
- Journal entry tab

#### Sections
- Reconciling items (timing/rounding/prior-period adjustments)
- Adjustment items (current-month adjustments requiring journal entries)
- Subledger and GL sections
- Reconciliation section (ties to certification summary)

#### Example adjustment
- $60,000 item (Ford Bronco) recorded prematurely in July, received in August.
- Removing the adjustment causes the unidentified difference to turn red; adding back resolves it.

#### Asset sections
- Asset value
- Accumulated depreciation
- Net book value (asset value + depreciation)

---

### 5.4 Subledger / General Ledger tabs
- Reference tabs populated by staging queries.
- Data is preloaded into separate Vena tables:
  - FA Subledger
  - FA General Ledger
- Not required to populate schedules, but helpful for viewing source data without drill-to-transactions.

---

### 5.5 Journal Entry tab
- Captures journal entries created from reconciliation.
- Supports manual additions via “Insert Row”.
- System-generated entries include depreciation and adjusting entries (e.g., the $60k correction).
- Entries can be exported and posted back to ERP/GL.

---

### 5.6 Controls tab and mappings
- Controls govern entity/source/account/year/period/measure selections.
- Includes sections for certification mappings, checklist mappings, reconciliation mappings.
- Users can adjust/hide mappings per client needs.

---

## 6. Bank Reconciliation (Shiv)

### 6.1 Purpose
Reconcile cash GL accounts to bank statements and identify differences.

#### Matching approach
- Uses a transaction matching algorithm supporting:
  - One-to-one matches
  - One-to-many matches (based on depth)
- Implemented using **Microsoft Power Query** in native Excel.
- Transformations and matching run in the background via refresh.

> Note: As staging queries in Vena 365 become available in table format, further automation is possible.

---

### 6.2 Certification tab (Bank)
#### Summary
- GL balance vs Bank statement balance
- Difference (delta)
- Expected GL balance derived from:
  - Prior period additions
  - Manual reconciliations
  - Algorithmic reconciliations (Power Query)
- Unidentified difference = expected GL vs bank statement

#### Thresholds
- Example thresholds: $12k and 1% (configurable in Activity Settings)

#### Workflow panel
- Shows stage (example: review)
- Reviewer can accept/reject (status reflects red cross for reject, green tick for accept)

#### Activity settings, checklist, comments
- Same pattern as other templates (SOC compliance mentioned)

---

### 6.3 Configuration section (matching criteria)
Expandable configuration used to define matching:
- Match types: one-to-one and one-to-many
- Criteria fields: amount, date, text
- Index: unique record ID
- Tolerance: acceptance threshold (e.g., 0.05%)
- Weighting: emphasis on criteria (must total 100)
  - Example: 80% amount, 20% date, 0% text

#### Depth and runtime estimation
- Depth controls match combinations:
  - Depth 1: only 1-to-1
  - Depth 2: 1-to-1 and 1-to-2
  - Depth 3: increases combinations substantially
- Tool shows estimated runtime and flags long runs in red.

#### Exceptions setup
- Predefined reasons for unmatched transactions (e.g., hold check, accrual, bank charges)
- Can indicate whether a journal entry is needed and which accounts should be used.

---

### 6.4 Backend tables (staging queries)
Two required tables:
1. **GL Detail** (“one” table)
2. **Bank Statement** (“many” table)

Minimum required columns for algorithm:
- Amount
- Date
- Text (optional)
- Unique ID (Index)

Dropdown fields in configuration reflect available headers in these tables.

---

### 6.5 Matches tab (results of algorithm)
Shows:
- GL record (ID, date, description, amount)
- Matched bank statement record IDs
- Strength scores:
  - Amount strength
  - Date strength
  - Total strength
- User can accept/reject match (green tick when accepted)

#### Examples
- Exact match: 100% strength
- Near match: 99% strength accepted within tolerance
- One-to-many: one GL record matched to two bank statement records (enabled by depth = 2)

---

### 6.6 Exception report
- Lists GL items with no match found.
- User assigns a reason via dropdown (driven by configuration “reasons” list).
- Determines whether a journal entry is needed.

---

### 6.7 Journal entries (Bank)
- Journal entry tab aggregates values from:
  - Matches tab
  - Exception report
- Reasons map to accounts (e.g., Bank charges & fees account)
- Debit/credit lines auto-balance based on configured accounts.
- Manual JE lines can be inserted as needed.
- Reviewer status can be updated and then reflected back on certification tab.

#### Power Query visibility
- Queries & connections show:
  - Sources (one table / many table)
  - Transformations
  - Functions for matching
  - Final “suggested matches” output query

---

### 6.8 Controls tab
- Selection controls (source/account/entity/year/period/measure)
- Hide/show logic for sheets
- Mapping blocks for configuration, certification, checklist, etc.
- Users can modify mappings as required.

---

## 7. Financial Close Dashboard (Shiv)

### 7.1 Purpose
Central report to oversee the full financial close process:
- Activity task list (with status)
- Reconciliation dashboard
- Journal entry report

---

### 7.2 Activity Dashboard
#### Top visuals
- Entity and period selection (example: July 2022)
- Pie chart: % steps completed
- Activities by business day
- Activities by stage (prep/review/approval)

#### Task list detail
Columns include:
- Business day (1–6)
- Activity name (account reconciliation activities)
- Description
- Accounts
- Priority (high/medium/low)
- Frequency
- Preparer / Reviewer / Approver
- Prepared/reviewed/approved dates and statuses
- Overall activity status (in process / complete)

**Note:** Dashboard includes tasks done in Vena and outside Vena (e.g., posting entries), but task management remains in Vena.

---

### 7.3 Reconciliation Dashboard
Bird’s eye view of balance sheet reconciliations:
- Assets, liabilities, equity groupings
- Status of tasks (completed / in progress / not started)
- Expected GL vs actual GL balance
- Reconciling items, differences, unposted journals
- Certification comments (from individual templates)
- Settings (auto reconcile, frequency, key account)

---

### 7.4 Journal Dashboard
Consolidated view of journal entries created across templates:
- Account and entity
- Debit/credit entries for upload back to ERP/GL
- Posted status
- Reconciliation status
- Prepared/reviewed/approved statuses

Example reference:
- Prepaid reconciliation entries tie back to the prepaid template totals and balance (equal debit and credit).

---

## 8. Notes & Implementation Reminders (Consolidated)

- The solution uses **two models**:
  - Reconciliation model: holds reconciliation detail, GL balances, item-level detail, journal storage.
  - Management model: holds workflow and qualitative metadata that is retrieved into templates and dashboards.
- Certification tab data is frequently **mapped to the Management model**.
- Many templates rely on:
  - Input row + MDR retrieval patterns
  - Incrementing item IDs to avoid overwriting intersections
  - Validation rules (soft/hard warnings)
- Bank reconciliation relies heavily on:
  - Proper staging tables (one/many)
  - Unique IDs
  - Power Query refresh workflow
  - Configuration weights/tolerance/depth trade-offs

---
