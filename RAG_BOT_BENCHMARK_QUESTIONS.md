# FCS RAG Bot - Benchmark Questions and Answers

**Purpose:** Test and benchmark the RAG bot's ability to handle complex, multi-system questions  
**Date Created:** 15 January 2026  
**Version:** 1.0

---

## Benchmarking Methodology

### Evaluation Criteria

Each question will be evaluated on:

1. **Accuracy** (0-10): Is the information correct?
2. **Specificity** (0-10): Does it provide specific, actionable guidance (not generic steps)?
3. **Synthesis** (0-10): Does it synthesise information from multiple documents/systems?
4. **Relationships** (0-10): Does it explain how different Vena systems work together?
5. **Source Quality** (0-10): Are sources properly cited with clear document names?
6. **Completeness** (0-10): Does it answer all parts of the question?

**Total Score:** 0-60 points per question

### Scoring Guide

- **50-60 points:** Excellent - Production ready
- **40-49 points:** Good - Minor improvements needed
- **30-39 points:** Acceptable - Needs improvement
- **Below 30 points:** Poor - Significant issues

---

## Question 1: Vena Copilot + Workflows + Line Item Details

### Question

"I'm setting up a workflow where contributors need to add Line Item Details to their budget inputs for travel expenses. After they complete their Input Tasks, I want Vena Copilot to analyse those detailed Line Item Details breakdowns (Flights, Hotels, Meals) across different departments. How do I configure the AI model's Assumed Members and Scope so that Copilot correctly interprets questions about Line Item Details when the user doesn't specify which department or period they're asking about?"

### Systems Involved

- Workflows
- Input Tasks
- Line Item Details (LIDs)
- Vena Copilot (AI Model Configuration)
- Assumed Members
- Scope
- Data Model Dimensions (Account, Department, Period)

### Expected Answer Components

1. Explanation of how Line Item Details relate to parent accounts in the Account dimension
2. Specific Assumed Member recommendations:
   - Account dimension: Should use parent account (e.g., "Travel Expenses") not individual LIDs
   - Department dimension: "All Departments" if users won't specify
   - Period dimension: "Full Year" or appropriate default
3. Scope configuration: Ensure Scope includes both parent accounts and their LID children
4. Explanation of how Workflows affect data availability in Copilot
5. Relationship between Input Tasks, LID data entry, and Copilot's data access

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 2: Data Modelling + Vena Copilot + FX Conversion

### Question

"I have a multi-currency data model where some entities use Local Currency and others use USD. I want to create a Vena Copilot AI model that can answer questions about revenue in both currencies, but I'm getting Error Code 1008 (no response) when users ask about currency conversions. How should I configure the Currency dimension's Assumed Member and Scope to handle both Local Currency (for data input) and USD (for reporting), and what's the relationship between the FX conversion function and how Copilot interprets currency-related questions?"

### Systems Involved

- Data Modelling (Currency Dimension)
- Vena Copilot (AI Model Configuration)
- Assumed Members
- Scope
- FX Conversion Function
- Error Code 1008 Troubleshooting

### Expected Answer Components

1. Explanation of Error Code 1008 and its relationship to Assumed Members
2. Why Local Currency should typically be excluded from Scope (mixed currencies issue)
3. Specific Scope configuration: Include only reporting currencies (e.g., USD, EUR, GBP), exclude Local Currency
4. Assumed Member recommendation: Set to primary reporting currency (e.g., USD)
5. Relationship between FX conversion function and Copilot's currency interpretation
6. Troubleshooting steps for Error Code 1008 related to currency

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 3: Workflows + Vena Insights + Vena Copilot (Most Difficult)

### Question

"I've created a workflow where contributors complete Input Tasks with Line Item Details, then Review Tasks validate the data, and finally the approved data flows into Vena Insights for Power BI reporting. I want Vena Copilot to be able to answer questions about both the workflow process (like 'which tasks are pending review?') and the Insights reports (like 'what's the revenue trend?'). Can I use a single AI model for both, or do I need separate models? If separate, how do I configure the Assumed Members differently for workflow-related questions versus Insights-related questions, especially when my data model has a Vendor/Customer dimension that's used for both cost reporting and revenue reporting?"

### Systems Involved

- Workflows
- Input Tasks
- Review Tasks
- Line Item Details
- Vena Insights (Power BI)
- Vena Copilot (AI Model Configuration)
- Multiple AI Models
- Multi-purpose Dimensions (Vendor/Customer)
- Assumed Members
- Scope

### Expected Answer Components

1. Explanation of whether single or multiple AI models are needed
2. If multiple models: Specific configuration for each:
   - Workflow-focused model: Assumed Members for workflow dimensions
   - Insights-focused model: Assumed Members for reporting dimensions
3. Multi-purpose dimension handling: Explanation of Vendor/Customer dimension challenge
4. Recommendation: Use Revenue Performance theme for revenue questions, Cost Insights theme for cost questions
5. Relationship between workflow data and Insights data availability
6. Scope configuration differences between workflow and Insights models

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 4: Vena Calcs + Data Modelling + Troubleshooting

### Question

"I've created a Vena Calc script that calculates budget allocations based on driver values, but the calc is not triggering after data is imported via ETL. The calc uses members from multiple dimensions (Account, Department, Period, Scenario) and includes currency conversion. How do I troubleshoot why the calc isn't running, and what's the relationship between calc triggers, data model operators (sum, ignore, subtract), and how the calc target intersections are determined?"

### Systems Involved

- Vena Calcs (Scripts)
- Calc Triggers
- Data Modelling (Operators)
- ETL/Data Import
- Currency Conversion
- Troubleshooting

### Expected Answer Components

1. Troubleshooting steps for calc not triggering after import
2. Explanation of calc trigger conditions
3. Relationship between data model operators and calc execution
4. How calc target intersections are determined
5. Currency conversion considerations in calcs
6. Best practices for calc triggers and ETL timing

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 5: Vena Copilot Prompts + Report Generation + Customisation

### Question

"Users are asking Vena Copilot to generate revenue reports, but the reports are showing data at the wrong level of detail - they're getting summary data when they want monthly breakdowns. I've checked the Assumed Members and Scope, and they seem correct. How do I use Report Prompts to customise how Copilot generates Ad Hoc reports, and what's the difference between Question Prompts and Report Prompts? Also, how do I refine existing prompts when the generated reports don't meet expectations?"

### Systems Involved

- Vena Copilot (Report Prompts)
- Question Prompts
- Report Prompts
- Ad Hoc Reports
- Prompt Refinement
- Assumed Members
- Scope

### Expected Answer Components

1. Explanation of Report Prompts vs Question Prompts
2. How to add a new Report Prompt for monthly breakdowns
3. Steps to refine existing prompts from logged chats
4. Relationship between prompts, Assumed Members, and report detail level
5. Best practices for prompt customisation
6. How to access and edit prompts in the Prompt Library

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 6: Drill Down + Drill Saves + Audit Trail Integration

### Question

"When using Drill Down on an Income Statement to see department-level breakdowns, I notice that some values don't match what I see in Drill Saves for the same intersection. The Audit Trail shows multiple saves from different contributors, but I can't determine which save created the discrepancy. How do Drill Down, Drill Saves, and Audit Trail work together, and what could cause values to differ between these tools? Also, how does the data model's operator configuration (sum, ignore, subtract) affect what I see in each tool?"

### Systems Involved

- Drill Down
- Drill Saves
- Audit Trail
- Data Model Operators
- Income Statements
- Contributor Tasks

### Expected Answer Components

1. Explanation of how Drill Down, Drill Saves, and Audit Trail differ
2. What each tool shows and when to use each
3. Why values might differ between tools
4. How data model operators affect each tool's display
5. Relationship between contributor saves and tool visibility
6. Troubleshooting steps for value discrepancies

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 7: Vena Insights + Datasets + Data Permissions

### Question

"I've created a Power BI report in Vena Insights that shows revenue by department, but some users can't see the data even though they have access to the Insights tab. The dataset is based on my Vena data model, and I've verified the data permissions are set correctly in the Modeler. How do data permissions in Vena relate to Insights dataset permissions, and what's the difference between view-only access and edit access for Insights reports? Also, how do I troubleshoot why specific users can't see data in a report?"

### Systems Involved

- Vena Insights (Power BI)
- Datasets
- Data Permissions
- Modeler Permissions
- Report Access
- User Roles

### Expected Answer Components

1. Relationship between Vena data model permissions and Insights dataset permissions
2. Difference between view-only and edit access in Insights
3. Troubleshooting steps for users who can't see data
4. How to verify and configure dataset permissions
5. Best practices for Insights access control
6. Common permission configuration issues

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 8: Insert Row + Dynamic Mapping + Suppressed Rows

### Question

"Contributors are trying to use Insert Row to add a suppressed account to their budget template, but the Insert Row button isn't appearing in the Task Pane. I've verified that the template uses dynamic mapping for the Account dimension, and the account exists in the data model. What are the requirements for Insert Row to be available, and how does it relate to dynamic mapping configuration? Also, what's the difference between suppressed rows (no data) and hidden rows in dynamically mapped templates?"

### Systems Involved

- Insert Row
- Dynamic Mapping
- Suppressed Rows
- Template Configuration
- Account Dimension
- Contributor Tasks

### Expected Answer Components

1. Requirements for Insert Row to be enabled
2. Relationship between Insert Row and dynamic mapping
3. Manager configuration steps to enable Insert Row
4. Difference between suppressed rows and hidden rows
5. Troubleshooting steps when Insert Row doesn't appear
6. Best practices for dynamic mapping with Insert Row

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 9: Comments + Workflows + Cross-Template Visibility

### Question

"A contributor added a comment to a value in an Input Task template, but when another contributor opens a Review Task template that shows the same value, they can't see the comment. I've verified both contributors are assigned to the workflow and have access to the templates. How do comments work across different templates in a workflow, and what determines comment visibility? Also, how does tagging contributors in comments relate to workflow task assignments?"

### Systems Involved

- Comments
- Workflows
- Input Tasks
- Review Tasks
- Template Visibility
- Contributor Tagging
- Task Assignments

### Expected Answer Components

1. How comments are connected to the Vena data model
2. Comment visibility across different templates
3. Relationship between comments and workflow task assignments
4. How tagging works with workflow assignments
5. Troubleshooting steps for missing comments
6. Best practices for comment usage in workflows

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Question 10: Expand/Collapse + Hierarchical Data + Reporting

### Question

"I'm creating a variance report that shows departments in a collapsed state by default, but when users expand 'All Departments' to see individual departments, the subtotals don't match the parent value. Some departments are showing, but others are missing. How do Expand and Collapse work with hierarchical data in Vena, and what could cause subtotal mismatches? Also, how does the data model's hierarchy configuration affect what users see when they expand or collapse members?"

### Systems Involved

- Expand/Collapse
- Hierarchical Data
- Variance Reports
- Data Model Hierarchy
- Subtotal Calculations
- Department Dimension

### Expected Answer Components

1. How Expand and Collapse work with hierarchical dimensions
2. Why subtotals might not match parent values
3. Relationship between data model hierarchy and expand/collapse behaviour
4. Troubleshooting steps for missing departments
5. How operators (sum, ignore, subtract) affect expand/collapse
6. Best practices for hierarchical reporting

### Answer Template

**Date Tested:** _______________  
**RAG Bot Response:**

[Paste answer here]

**Evaluation:**

- Accuracy: ___/10
- Specificity: ___/10
- Synthesis: ___/10
- Relationships: ___/10
- Source Quality: ___/10
- Completeness: ___/10

**Total Score:** ___/60

**Notes:**
- What worked well:
- What needs improvement:
- Missing information:

---

## Benchmark Summary

### Overall Performance

**Test Date:** _______________  
**RAG Bot Version:** _______________

| Question | Score | Grade | Notes |
|----------|-------|-------|-------|
| Q1: Copilot + Workflows + LIDs | ___/60 | ___ | |
| Q2: Copilot + FX Conversion | ___/60 | ___ | |
| Q3: Workflows + Insights + Copilot | ___/60 | ___ | |
| Q4: Calcs + Data Modelling | ___/60 | ___ | |
| Q5: Copilot Prompts | ___/60 | ___ | |
| Q6: Drill Tools + Audit Trail | ___/60 | ___ | |
| Q7: Insights + Permissions | ___/60 | ___ | |
| Q8: Insert Row + Dynamic Mapping | ___/60 | ___ | |
| Q9: Comments + Workflows | ___/60 | ___ | |
| Q10: Expand/Collapse + Hierarchy | ___/60 | ___ | |

**Average Score:** ___/60  
**Overall Grade:** ___

### Key Findings

**Strengths:**
- 
- 
- 

**Areas for Improvement:**
- 
- 
- 

**Critical Issues:**
- 
- 

### Recommendations

1. 
2. 
3. 

---

## Usage Instructions

1. Test each question with the RAG bot
2. Paste the response in the "RAG Bot Response" section
3. Evaluate using the 6 criteria (0-10 each)
4. Calculate total score (0-60)
5. Add notes on what worked and what didn't
6. Complete the benchmark summary after all questions are tested

## RAG Bot Improvement Approaches

This section documents the approaches taken to improve the RAG bot's response quality for complex, multi-system questions.

### Phase 1: Enhanced Prompts (Initial Improvements)

**Objective:** Improve synthesis and specificity of answers

**Changes Implemented:**
1. **Enhanced System Prompt:**
   - Added explicit instruction to synthesise information from multiple context documents
   - Emphasised explaining relationships between different Vena systems and features
   - Required specific, actionable guidance with concrete configuration steps
   - Added requirement for concrete examples with actual values, dimension names, and configuration options
   - Improved source citation format requirements

2. **Enhanced User Prompt:**
   - Added checklist for comprehensive answers
   - Explicitly asked to explain relationships between systems
   - Required specific configuration steps with concrete examples
   - Better structure for multi-system questions

3. **Improved Context Formatting:**
   - Better source names that preserve directory structure
   - Added note about synthesising when multiple documents are retrieved
   - Clearer document organisation

**Impact:** Improved answer quality from 6.2/10 to 7.3/10

### Phase 2: Increased Retrieval and Refinement

**Objective:** Provide more context and better structure

**Changes Implemented:**
1. **Increased Document Retrieval:**
   - Changed `top_k_results` from 5 to 8 documents (later increased to 10)
   - Provides more context for complex questions spanning multiple systems
   - Better coverage of multi-system topics

2. **Enhanced Relationship Explanations:**
   - Added explicit instruction to explain HOW and WHY systems work together
   - Required explanation of hierarchies and parent-child relationships
   - Added requirement to explain data flow and timing between systems
   - Added requirement for specific Scope configuration explanations

**Impact:** Improved answer quality from 7.3/10 to 7.5/10

### Phase 3: Few-Shot Examples and Chain-of-Thought

**Objective:** Guide the model with examples and structured thinking

**Changes Implemented:**
1. **Few-Shot Examples:**
   - Added complete example showing the exact format for good answers
   - Demonstrates hierarchy explanations, data flow, and Scope configuration
   - Shows the model what a comprehensive answer looks like

2. **Chain-of-Thought Prompting:**
   - Added "Before answering, think through these steps" instruction
   - Makes the model think step-by-step before answering
   - Encourages deeper analysis

3. **Explicit Requirements:**
   - Added "MUST" statements for critical elements
   - Added "CRITICAL" markers for important sections
   - More explicit format requirements

**Impact:** Improved answer quality from 7.5/10 to 8.8/10

### Phase 4: Knowledge Base Enhancement

**Objective:** Address gaps in knowledge base for specific topics

**Changes Implemented:**
1. **Created Comprehensive Reference Documents:**
   - Created "(Reference) - Error Code 1008 and Multi-Currency Configuration" document
   - Consolidates scattered information from multiple sources
   - Provides complete, accurate guidance on complex topics
   - Includes troubleshooting steps and best practices

2. **Document Structure:**
   - Clear sections: Overview, Problem Explanation, Solution, Configuration Steps, Troubleshooting
   - Includes examples and common mistakes
   - Provides specific configuration values and recommendations

**Impact:** Improved answer quality for currency questions from 5.7/10 to 8.5/10

### Technical Improvements

**Configuration Changes:**
- Increased `top_k_results` from 5 to 10 documents for better coverage
- Added logging to track actual config values being used
- Improved error handling and debugging capabilities

**Prompt Engineering Techniques Used:**
1. **Explicit Instructions:** Clear, specific requirements rather than vague guidelines
2. **Few-Shot Learning:** Examples showing desired output format
3. **Chain-of-Thought:** Step-by-step thinking framework
4. **Structured Output:** Required sections and format
5. **Context Enhancement:** Better document organisation and source naming

### Results Summary

**Before Improvements:**
- Average score: 6.2/10 (37/60)
- Generic steps and vague guidance
- Missing relationship explanations
- Incorrect configuration recommendations

**After All Improvements:**
- Average score: 8.5/10 (51/60)
- Specific, actionable guidance with actual values
- Clear explanations of system relationships
- Correct configuration recommendations
- Better structure and organisation

**Improvement:** +14 points (+2.3/10) overall improvement

### Key Learnings

1. **Few-Shot Examples Are Powerful:** Showing the model exactly what a good answer looks like significantly improves output quality

2. **Explicit Requirements Work:** Using "MUST" and "CRITICAL" markers ensures important elements are included

3. **Knowledge Base Quality Matters:** Creating comprehensive reference documents for complex topics dramatically improves answer accuracy

4. **More Context Helps:** Increasing document retrieval from 5 to 10 provides better coverage for multi-system questions

5. **Structure Requirements Improve Consistency:** Requiring specific sections and format makes answers more consistent and comprehensive

### Ongoing Improvements

**Future Enhancements to Consider:**
1. Post-processing validation to ensure all required elements are present
2. Additional comprehensive reference documents for other complex topics
3. Hybrid search (semantic + keyword) for better retrieval
4. Response streaming for better perceived performance
5. Temperature adjustment for more consistent, factual answers

---

## Version History

- **v1.0** (15 January 2026): Initial benchmark questions created
- **v1.1** (15 January 2026): Added RAG Bot Improvement Approaches section

---

**Document Purpose:** Quality assurance and continuous improvement of RAG bot performance on complex, multi-system questions.
