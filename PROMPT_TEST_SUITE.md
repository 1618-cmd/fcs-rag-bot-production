# Prompt Test Suite - 5 Hardest Questions

**Purpose:** Test these 5 questions every time we change the prompt to ensure improvements don't break existing functionality.

**Last Updated:** 19 January 2026

---

## Test Protocol

1. **Before changing prompt:** Test all 5 questions and record baseline scores
2. **After changing prompt:** Test all 5 questions again
3. **Compare results:** Ensure no regressions and improvements are working
4. **Only deploy if:** All 5 questions maintain or improve scores

---

## The 5 Hardest Questions

### Question 1: VenaQL Code Generation (Syntax Critical)
**Question:** "How do I write a VenaQL script that calculates rolling 12-month averages for revenue accounts, handles missing months with null checks, applies different calculation rules for parent vs subsidiary entities, and includes error handling for division by zero?"

**What to check:**
- ✅ Code shown FIRST (not explanations)
- ✅ Uses `venaql` language tag (not `plaintext`)
- ✅ NO ForEach loops (use aggregation functions)
- ✅ NO curly braces {} (use If/ElseIf/Else/End)
- ✅ Correct syntax: If/ElseIf/Else/End structure
- ✅ Error checking with comparison operators (e.g., `!= 0`, not `IsNull()`)

**Expected Score:** 50-60/60

---

### Question 2: Multi-System Synthesis (Most Difficult)
**Question:** "I've created a workflow where contributors complete Input Tasks with Line Item Details, then Review Tasks validate the data, and finally the approved data flows into Vena Insights for Power BI reporting. I want Vena Copilot to be able to answer questions about both the workflow process (like 'which tasks are pending review?') and the Insights reports (like 'what's the revenue trend?'). Can I use a single AI model for both, or do I need separate models? If separate, how do I configure the Assumed Members differently for workflow-related questions versus Insights-related questions, especially when my data model has a Vendor/Customer dimension that's used for both cost reporting and revenue reporting?"

**What to check:**
- ✅ Synthesizes information from multiple systems (Workflows, Insights, Copilot)
- ✅ Explains relationships between systems (HOW/WHY)
- ✅ Provides specific configuration steps with actual values
- ✅ Explains hierarchies and data flow
- ✅ Cites all sources used

**Expected Score:** 50-60/60

---

### Question 3: Copilot + Workflows + Line Item Details
**Question:** "I'm setting up a workflow where contributors need to add Line Item Details to their budget inputs for travel expenses. After they complete their Input Tasks, I want Vena Copilot to analyse those detailed Line Item Details breakdowns (Flights, Hotels, Meals) across different departments. How do I configure the AI model's Assumed Members and Scope so that Copilot correctly interprets questions about Line Item Details when the user doesn't specify which department or period they're asking about?"

**What to check:**
- ✅ Explains parent-child hierarchy (LIDs under parent accounts)
- ✅ Specific Assumed Member recommendations (parent account, not LIDs)
- ✅ Scope configuration explanation
- ✅ Data flow explanation (Workflows → Copilot)
- ✅ Specific values (not placeholders)

**Expected Score:** 50-60/60

---

### Question 4: Copilot + FX Conversion + Error Code
**Question:** "I have a multi-currency data model where some entities use Local Currency and others use USD. I want to create a Vena Copilot AI model that can answer questions about revenue in both currencies, but I'm getting Error Code 1008 (no response) when users ask about currency conversions. How should I configure the Currency dimension's Assumed Member and Scope to handle both Local Currency (for data input) and USD (for reporting), and what's the relationship between the FX conversion function and how Copilot interprets currency-related questions?"

**What to check:**
- ✅ Explains Error Code 1008 and its relationship to Assumed Members
- ✅ Specific Scope configuration (exclude Local Currency)
- ✅ Explains relationship between FX conversion and Copilot
- ✅ Troubleshooting steps
- ✅ Specific configuration values

**Expected Score:** 50-60/60

---

### Question 5: VenaQL Intercompany Eliminations
**Question:** "How do I write a VenaQL script that handles intercompany eliminations with multiple entity relationships, includes error checking for missing data, and uses nested IF statements to apply different elimination rules based on entity type?"

**What to check:**
- ✅ Code shown FIRST (not explanations)
- ✅ Uses `venaql` language tag
- ✅ NO ForEach loops
- ✅ NO curly braces {}
- ✅ Correct If/ElseIf/Else/End syntax
- ✅ Error checking with comparison operators
- ✅ Complete working code example

**Expected Score:** 50-60/60

---

## Test Results Template

### Test Date: _______________
### Prompt Version: _______________
### Tester: _______________

| Question | Code First? | Correct Syntax? | Synthesis? | Specificity? | Sources? | Score | Notes |
|----------|-------------|-----------------|-----------|-------------|---------|-------|-------|
| Q1: Rolling 12-Month | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | __/60 | |
| Q2: Multi-System | ✅/❌ | N/A | ✅/❌ | ✅/❌ | ✅/❌ | __/60 | |
| Q3: Copilot + LIDs | ✅/❌ | N/A | ✅/❌ | ✅/❌ | ✅/❌ | __/60 | |
| Q4: FX + Error Code | ✅/❌ | N/A | ✅/❌ | ✅/❌ | ✅/❌ | __/60 | |
| Q5: Intercompany | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | __/60 | |

**Average Score:** __/60

**Regressions Found:** Yes/No
**Improvements Found:** Yes/No

**Decision:** ✅ Deploy / ❌ Fix Issues First

---

## Quick Test Checklist

Before deploying any prompt change:

- [ ] Test Q1 (VenaQL rolling averages) - Check syntax, no ForEach
- [ ] Test Q2 (Multi-system) - Check synthesis, relationships
- [ ] Test Q3 (Copilot + LIDs) - Check hierarchy explanation
- [ ] Test Q4 (FX + Error) - Check troubleshooting, specificity
- [ ] Test Q5 (Intercompany) - Check syntax, code completeness
- [ ] All 5 questions maintain or improve scores
- [ ] No regressions in critical areas (syntax, synthesis, specificity)

---

## Notes

- These 5 questions cover: Code generation (2), Multi-system synthesis (2), Troubleshooting (1)
- Focus areas: Syntax correctness, synthesis capability, specificity, relationship explanations
- If any question scores below 40/60, investigate and fix before deploying
