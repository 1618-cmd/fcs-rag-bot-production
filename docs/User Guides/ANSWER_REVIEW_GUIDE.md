# Answer Review Guide: Best Practices for Reviewing RAG Bot Answers

**Last Updated:** [Update when bot features change]  
**Purpose:** Guide for reviewing and validating RAG Bot answers to ensure accuracy and quality

---

## What is This Guide

This guide explains how to review RAG Bot answers to verify they are accurate, complete, and properly grounded in the knowledge base. Use this guide when evaluating bot responses for quality assurance, training, or when users report issues.

---

## Review Checklist

Use this checklist when reviewing any bot answer:

### Accuracy Validation

**1. Factual Claims**
- Verify every factual claim is stated in the source documents cited
- Check that configuration values, dimension names, and technical details appear in sources
- Verify that no information is made up or hallucinated

**2. Source Verification**
- Confirm all cited sources actually contain the information referenced
- Verify sources are relevant to the question asked
- Check that sources are only cited if information from them was actually used

**3. Inference Validation**
- If the answer makes inferences, verify they are explicitly labeled (e.g., "Based on the context...")
- Check that inferences are reasonable and supported by the context
- Ensure inferences are not presented as facts

### Completeness Assessment

**4. Question Coverage**
- Verify the answer addresses all aspects of the question
- Check if any important details are missing
- Assess if the answer provides sufficient information for the user to act

**5. Uncertainty Handling**
- If information is partial or uncertain, verify this is explicitly stated
- Check that limitations are clearly communicated
- Ensure users know when information may be incomplete

### Source Citation Quality

**6. Source Relevance**
- Verify all sources are relevant to the question
- Check that sources are properly formatted (e.g., [Source: document_name])
- Ensure sources are listed at the end of the answer

**7. Source Completeness**
- If the bot refuses to answer, verify no sources are cited (citing sources means they were used)
- Check that all sources used in the answer are cited
- Verify sources are not missing if information was clearly used from them

### Format and Structure

**8. Answer Structure**
- For troubleshooting questions, verify the answer follows the mandatory STEP 1-6 format
- Check that complex questions explain HOW/WHY, not just WHAT
- Verify hierarchies and parent-child relationships are explained when relevant

**9. Actionability**
- Verify the answer provides specific, actionable steps (not generic instructions)
- Check that concrete values are provided (not placeholders like "appropriate member")
- Ensure configuration examples include actual dimension names, member names, and settings

**10. Code Examples**
- If VenaQL code is provided, verify it follows Vena constraints (no aliasing, explicit columns)
- Check that code examples are complete and syntactically correct
- Ensure code examples match the solutions provided

---

## Review Process

### Step 1: Initial Scan

Quickly review the answer for:
- Does it directly answer the question asked
- Are sources cited
- Is the format appropriate for the question type

### Step 2: Detailed Review

Follow the review checklist above to verify:
- Accuracy of factual claims
- Source relevance and verification
- Completeness and coverage
- Format and structure adherence

### Step 3: Source Verification

For critical answers, verify sources by:
- Checking if cited documents actually contain the information referenced
- Verifying source relevance to the question
- Ensuring all sources used are cited

### Step 4: Quality Assessment

Evaluate overall quality:
- Is the answer helpful and actionable
- Would a user be able to act on this answer
- Are any important details missing

### Step 5: Documentation

If issues are found:
- Document what was wrong
- Note which validation criteria failed
- Suggest improvements if applicable

---

## Common Issues to Watch For

### Hallucination (Incorrect Information)

**Symptoms:**
- Information not in source documents
- Configuration values not mentioned in sources
- Technical details not supported by context

**What to check:**
- Verify every claim against source documents
- Check that no training data knowledge is used to fill gaps
- Ensure inferences are explicitly labeled

### Missing Sources

**Symptoms:**
- Information provided but no sources cited
- Sources cited but not actually used in answer
- Sources cited when bot refused to answer

**What to check:**
- Verify sources are cited for all information used
- Check that sources are only cited if actually used
- Ensure no sources cited when bot refuses to answer

### Incomplete Answers

**Symptoms:**
- Question only partially answered
- Important details missing
- User cannot act on the answer

**What to check:**
- Verify all aspects of question are addressed
- Check if critical information is missing
- Ensure answer provides actionable steps

### Format Issues

**Symptoms:**
- Troubleshooting questions not following STEP 1-6 format
- Generic instructions instead of specific steps
- Placeholders instead of actual values

**What to check:**
- Verify mandatory format for troubleshooting questions
- Check that specific values are provided
- Ensure actionable configuration steps are included

### Uncertainty Not Communicated

**Symptoms:**
- Partial information presented as complete
- Inferences presented as facts
- Limitations not stated

**What to check:**
- Verify uncertainty is explicitly stated
- Check that inferences are labeled as such
- Ensure limitations are clearly communicated

---

## Quality Standards

### Excellent Answer

- All factual claims verified in source documents
- All sources cited are relevant and verified
- Complete answer addressing all aspects of question
- Specific, actionable steps with concrete values
- Proper format and structure for question type
- Uncertainty explicitly stated if applicable

### Good Answer

- Most factual claims verified in sources
- Sources mostly relevant and verified
- Answer addresses main aspects of question
- Generally actionable but may lack some specificity
- Mostly proper format with minor issues
- Some uncertainty may not be explicit

### Needs Improvement

- Some factual claims not verified
- Some sources not relevant or verified
- Answer incomplete or missing important details
- Lacks specificity or actionability
- Format issues or missing structure
- Uncertainty not communicated

### Poor Answer

- Significant factual inaccuracies
- Sources irrelevant or not verified
- Answer does not address question
- Not actionable or uses placeholders
- Major format or structure issues
- Inferences presented as facts

---

## When to Escalate

Escalate for review or correction if:

1. **Hallucination detected:** Bot provides information not in knowledge base
2. **Critical inaccuracy:** Technical details are wrong and could cause issues
3. **Missing critical information:** Answer lacks information needed to act
4. **Format violations:** Troubleshooting questions do not follow mandatory format
5. **Source issues:** Sources cited but not used, or sources missing when used

---

## Review Frequency

### Routine Reviews

- Review random sample of answers periodically (e.g., 5-10% of queries)
- Focus on high-risk queries (troubleshooting, configuration, code examples)
- Review answers when users report issues

### Targeted Reviews

- Review all answers for specific question types (e.g., VenaQL troubleshooting)
- Review answers after knowledge base updates
- Review answers when prompt engineering changes are made

### Quality Assurance

- Spot-check answers during training or onboarding
- Review answers used in documentation or examples
- Validate answers before sharing with stakeholders

---

## Tips for Effective Reviews

1. **Start with sources:** Verify sources first, then check accuracy
2. **Read the question:** Ensure answer actually addresses what was asked
3. **Check for placeholders:** Look for generic terms that should be specific
4. **Verify format:** Ensure mandatory formats (e.g., STEP 1-6) are followed
5. **Assess actionability:** Could someone act on this answer without additional information

---

## Common Questions

### What if an answer is partially correct?

If an answer is partially correct:
- Note which parts are accurate
- Identify what is missing or incorrect
- Document the issue for correction or improvement

### What if sources are relevant but answer is incomplete?

If sources are relevant but answer incomplete:
- Verify if information is missing from knowledge base
- Check if bot failed to synthesize information correctly
- Consider if knowledge base needs enhancement

### What if answer format is wrong but content is correct?

If format is wrong but content correct:
- Note the format issue
- Verify content accuracy separately
- Consider if format requirements need clarification

---

## Additional Resources

- **RAG Bot User Guides:** [Link to other user guides]
- **Knowledge Base Documentation:** [Link if applicable]
- **Support Resources:** [Contact information]

---

**Remember:** The goal of review is to ensure answers are accurate, complete, and helpful. Use this guide to systematically validate bot responses and maintain quality standards.
