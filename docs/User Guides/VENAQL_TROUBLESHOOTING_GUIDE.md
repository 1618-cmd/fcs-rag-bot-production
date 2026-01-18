# VenaQL Troubleshooting Guide: Using the RAG Bot to Diagnose Scripts

**Last Updated:** [Update when bot features change]  
**Purpose:** Guide for using the RAG Bot to troubleshoot and fix VenaQL script issues

---

## What is This Guide

This guide explains how to use the RAG Bot to diagnose and resolve issues with VenaQL scripts. The bot analyzes your scripts, identifies problems, and provides step-by-step solutions.

---

## How to Use This Guide

When you encounter a VenaQL script issue:

1. Copy your script into the bot
2. Ask a specific troubleshooting question (see examples below)
3. Review the bot's diagnosis and solutions
4. Apply the recommended fixes

---

## Common VenaQL Issues

### Script Not Returning Values

**Problem:** Your VenaQL script is returning empty results or no values.

**Ask the bot:**
- "Why isn't this VenaQL script returning any values?"
- "Why is my script returning empty results?"
- "What's wrong with this VenaQL script: [paste your script]"

**What the bot will check:**
- Multiple Scope statements and conflicts
- Members referenced outside active scope
- Empty intersections between scopes
- Missing dimensions or members

**Example Question:**
```
Why isn't this VenaQL script returning any values?

Scope { [Account.Sales], [Period.Q1] }
Scope { [Account.Expenses], [Period.Q2] }
@total = { [Account.Sales], [Period.Q1] }.Sum()
@this = @total
```

### Multiple Scope Statements

**Problem:** Your script has multiple Scope statements and the last one is overriding previous ones.

**Ask the bot:**
- "I have multiple Scope statements in my script. Is that causing issues?"
- "Why does my script only use the last Scope statement?"
- "How do I combine multiple Scope statements?"

**What the bot will explain:**
- How the last Scope statement overrides previous ones
- How to combine Scope statements into one
- How to restructure your script to use a single Scope

### Members Not in Active Scope

**Problem:** Your calculation references members that are not included in the active scope.

**Ask the bot:**
- "Why can't my script access [member name]?"
- "My calculation references [member] but it's not in the scope. What should I do?"
- "How do I add members to the active scope?"

**What the bot will explain:**
- Which members are missing from the active scope
- How to add missing members to the scope
- Why certain members are required for the calculation

### Scope Configuration Issues

**Problem:** Your scope is not configured correctly for parent-child hierarchies.

**Ask the bot:**
- "How do I configure Scope for parent-child hierarchies?"
- "Should I include parent or child members in Scope?"
- "How do hierarchies affect my Scope configuration?"

**What the bot will explain:**
- How parent members automatically include children in Scope
- When to use parent vs child members
- How hierarchies affect query results

### Syntax and Notation Errors

**Problem:** Your script has syntax errors or incorrect notation.

**Ask the bot:**
- "What's wrong with the syntax in this VenaQL script: [paste script]"
- "Is this VenaQL notation correct?"
- "What are the syntax rules for VenaQL?"

**What the bot will explain:**
- Syntax rules and notation requirements
- Common syntax mistakes
- How to fix notation errors

---

## How to Ask Troubleshooting Questions

### Format 1: Direct Question with Script

```
Why isn't this VenaQL script returning any values?

[paste your complete script here]
```

### Format 2: Specific Error Question

```
I'm getting empty results from this script. What's wrong?

[paste your script here]
```

### Format 3: General Troubleshooting Question

```
How do I troubleshoot a VenaQL script that's not working?

[paste your script here]
```

### Format 4: Step-by-Step Diagnosis Request

```
Can you analyze this VenaQL script step by step and tell me what's wrong?

[paste your script here]
```

---

## What the Bot Will Provide

When you ask about a VenaQL script issue, the bot will:

1. **Identify the Problem:** Analyze your script and identify specific issues
2. **Explain the Root Cause:** Explain why the issue is occurring
3. **Provide Solutions:** Offer multiple solution options with code examples
4. **Explain the Fix:** Explain how each solution addresses the problem

### Example Bot Response Structure

The bot will follow this format when troubleshooting:

- **STEP 1:** Count and analyze Scope statements
- **STEP 2:** Identify the active (last) Scope
- **STEP 3:** List members referenced in calculations
- **STEP 4:** Identify missing members from active scope
- **STEP 5:** Explain the root cause
- **STEP 6:** Provide solution options with code examples

---

## Tips for Best Results

1. **Include the Complete Script:** Paste your entire script, not just part of it

2. **Describe the Expected Behavior:** Tell the bot what you expect the script to do

3. **Mention Any Error Messages:** If you see specific errors, include them in your question

4. **Ask Follow-up Questions:** If a solution is not clear, ask the bot to explain further

5. **Try Different Approaches:** If one solution does not work, ask the bot for alternative approaches

---

## Advanced Troubleshooting

### Debugging Complex Scripts

**Ask the bot:**
- "How do I debug a complex VenaQL script with multiple calculations?"
- "How do I test individual parts of my VenaQL script?"
- "What are best practices for writing maintainable VenaQL scripts?"

### Understanding Data Flow

**Ask the bot:**
- "How does data flow through my VenaQL script?"
- "What is the order of execution in VenaQL scripts?"
- "How do I verify data is available for my calculations?"

### Performance Optimization

**Ask the bot:**
- "How do I optimize my VenaQL script for performance?"
- "What are common performance issues in VenaQL scripts?"
- "How do I reduce calculation time in VenaQL?"

---

## When the Bot Cannot Help

If the bot cannot diagnose your script issue:

1. The problem may be related to data availability rather than the script itself
2. The issue may require knowledge of your specific data model configuration
3. The problem may be client-specific or environment-specific

**What to do:**
- Verify that data exists in your data model for the dimensions and members referenced
- Check your data model configuration and hierarchy setup
- Create a Jira ticket with your script and error details
- Ask a colleague or escalate to your manager

---

## Recent Bot Updates

*[Update this section when the bot gets new features]*

**Current Features:**
- Diagnoses VenaQL script issues and identifies root causes
- Provides step-by-step troubleshooting following a structured format
- Offers multiple solution options with code examples
- Explains how each solution addresses the problem

**Coming Soon:**
- [Add upcoming features here as they are developed]

---

## Need Help

- **Questions About VenaQL Scripting:** Ask the bot first, then create a Jira ticket if needed
- **Technical Issues with the Bot:** [Contact information]
- **Feedback on This Guide:** [Contact information or feedback link]

---

**Remember:** The bot is trained to troubleshoot VenaQL scripts using our knowledge base. Always include your complete script when asking for help, and review the bot's step-by-step analysis carefully.
