# Single vs Multiple AI Models and Multi-Purpose Dimensions in Vena Copilot

## Overview

When configuring Vena Copilot, you may need to decide whether to use a single AI model or create multiple AI models. This decision is critical when dealing with multi-purpose dimensions, different query types (workflow vs Insights), or complex data models with alternate hierarchies. This guide explains when and how to use multiple AI models effectively.

## Key Concepts

### Single AI Model

A single AI model can handle multiple types of questions if:
- Your data model has clear, distinct hierarchies
- Questions can be answered using the same Assumed Members and Scope
- There are no conflicting requirements for the same dimension

**Example:** A simple finance data model where all questions relate to revenue, expenses, and financial reporting using the same currency, period, and entity assumptions.

### Multiple AI Models

You need multiple AI models when:
- A dimension serves multiple purposes (multi-purpose dimensions)
- Different query types require different Assumed Members for the same dimension
- You want to separate workflow questions from data analysis questions
- Different user groups need access to different data scopes

**Example:** A Vendor/Customer dimension used for both cost reporting (vendors) and revenue reporting (customers) requires separate models because you can only set one Assumed Member per dimension per model.

## Multi-Purpose Dimensions: The Vendor/Customer Dimension Case Study

### The Problem

One of the most common multi-purpose dimensions is the **Vendor/Customer dimension**. This dimension contains:
- **Customer hierarchy**: Used for revenue reporting (e.g., "All Customers" → "Customer A", "Customer B")
- **Vendor hierarchy**: Used for cost reporting (e.g., "All Vendors" → "Vendor X", "Vendor Y")

**Why This Is a Problem:**
- You can only set **one Assumed Member per dimension** in each AI model
- If you set Assumed Member to "All Customers", cost-related questions won't work
- If you set Assumed Member to "All Vendors", revenue-related questions won't work
- Users would have to specify the member in every question, creating a poor user experience

### The Solution: Separate AI Models

**Create Two Separate AI Models:**

1. **Revenue Performance AI Model** (using Revenue Performance theme):
   - **Vendor/Customer Dimension Assumed Member**: Set to "All Customers" (or the parent member for customers)
   - **Vendor/Customer Dimension Scope**: Include "All Customers" and its children
   - **Account Dimension Assumed Member**: Set to "Revenue" (or primary revenue account)
   - **Purpose**: Answers revenue-related questions about customers

2. **Cost Insights AI Model** (using Cost Insights theme):
   - **Vendor/Customer Dimension Assumed Member**: Set to "All Vendors" (or the parent member for vendors)
   - **Vendor/Customer Dimension Scope**: Include "All Vendors" and its children
   - **Account Dimension Assumed Member**: Set to "Operating Expenses" (or primary expense account)
   - **Purpose**: Answers cost-related questions about vendors

### Configuration Steps for Vendor/Customer Dimension

#### Revenue Performance AI Model Configuration

1. **Navigate to Vena Copilot → Builder → Create AI Model**
2. **Select Theme**: Choose "Revenue Performance AI Model"
3. **Configure Settings**: Select your Finance data model
4. **Set Assumed Members**:
   - **Vendor/Customer Dimension**: Set Assumed Member to "All Customers"
   - **Account Dimension**: Set Assumed Member to "Revenue"
   - **Other Dimensions**: Set appropriate Assumed Members (Period, Year, Scenario, etc.)
5. **Set Scope**:
   - **Vendor/Customer Dimension**: Include "All Customers" in Scope (automatically includes all customer children)
   - **Account Dimension**: Include revenue-related accounts in Scope
   - **Other Dimensions**: Configure Scope as needed

#### Cost Insights AI Model Configuration

1. **Navigate to Vena Copilot → Builder → Create AI Model**
2. **Select Theme**: Choose "Cost Insights AI Model"
3. **Configure Settings**: Select your Finance data model (can be the same data model)
4. **Set Assumed Members**:
   - **Vendor/Customer Dimension**: Set Assumed Member to "All Vendors"
   - **Account Dimension**: Set Assumed Member to "Operating Expenses"
   - **Other Dimensions**: Set appropriate Assumed Members (Period, Year, Scenario, etc.)
5. **Set Scope**:
   - **Vendor/Customer Dimension**: Include "All Vendors" in Scope (automatically includes all vendor children)
   - **Account Dimension**: Include expense-related accounts in Scope
   - **Other Dimensions**: Configure Scope as needed

### Why This Configuration Works

- **Separate Assumed Members**: Each model can have different Assumed Members for the same dimension
- **Clear Purpose**: Users know which model to use for revenue vs cost questions
- **Better User Experience**: Users don't need to specify customer/vendor in every question
- **Leverages Pre-built Themes**: Revenue Performance and Cost Insights themes are designed for this use case

## Workflow Questions vs Insights Questions

### Understanding the Difference

**Workflow Questions** (Task Management):
- Focus on task status, completion, and process flow
- Examples:
  - "Which Input Tasks are pending review?"
  - "What tasks are assigned to the Sales department?"
  - "Show me tasks that are overdue"
- **Data Source**: Workflow metadata, task assignments, task status

**Insights Questions** (Data Analysis):
- Focus on financial data, trends, and analysis
- Examples:
  - "What was our revenue growth in Q1?"
  - "Show me operating expenses by department"
  - "Compare actuals vs budget for the current year"
- **Data Source**: Vena data model, financial data, Power BI datasets

### Can You Use a Single Model for Both?

**Generally, Yes** - if:
- Your data model includes workflow-related dimensions (Task Status, Task Type, etc.)
- Workflow questions can be answered using the same Assumed Members as Insights questions
- Users don't need separate access controls

**Consider Separate Models** - if:
- Workflow questions require different Assumed Members than Insights questions
- You want to restrict access (some users see workflow model, others see Insights model)
- Workflow and Insights queries are fundamentally different in structure

### Configuration for Combined Workflow + Insights Model

If using a single model for both:

1. **Set Assumed Members** for dimensions used in both contexts:
   - **Account Dimension**: Set to primary account (e.g., "Revenue" or "Operating Expenses")
   - **Period Dimension**: Set to current period or "Full Year"
   - **Scenario Dimension**: Set to "Actual"
   - **Task Status Dimension** (if exists): Set to most common status (e.g., "Pending")

2. **Set Scope** to include:
   - All relevant accounts (revenue, expenses, etc.)
   - All relevant periods
   - All relevant scenarios
   - All task statuses (if workflow dimensions exist)

3. **Train the Model** with examples of both workflow and Insights questions

## Decision Framework: Single vs Multiple Models

### Use a Single AI Model When:

✅ **Simple data model** with clear hierarchies
✅ **No multi-purpose dimensions** that require conflicting Assumed Members
✅ **Same Assumed Members work** for all question types
✅ **Same user group** needs access to all queries
✅ **Workflow and Insights** can share the same configuration

**Example:** A finance team that only asks revenue and expense questions, with no vendor/customer dimension complexity.

### Use Multiple AI Models When:

✅ **Multi-purpose dimensions** exist (e.g., Vendor/Customer, Geography/Project)
✅ **Conflicting Assumed Member requirements** for the same dimension
✅ **Different user groups** need different access (e.g., revenue team vs cost team)
✅ **Pre-built themes** align with your needs (Revenue Performance, Cost Insights)
✅ **Workflow and Insights** require fundamentally different configurations

**Example:** An organization with a Vendor/Customer dimension used for both revenue (customers) and costs (vendors) needs separate Revenue Performance and Cost Insights models.

## Other Multi-Purpose Dimension Examples

### Geography/Project Dimension

If your data model has a dimension that serves as both Geography and Project:

**Solution:** Create separate models:
- **Geography-focused model**: Set Assumed Member to "All Geographies"
- **Project-focused model**: Set Assumed Member to "All Projects"

### Account Dimension with Alternate Hierarchies

If your Account dimension has alternate hierarchies (e.g., by function vs by nature):

**Solution:** Use Scope to limit each model to one hierarchy:
- **Model 1**: Scope includes "Revenue" hierarchy only
- **Model 2**: Scope includes "Expenses" hierarchy only

## Best Practices

1. **Start with Pre-built Themes**: Use Revenue Performance or Cost Insights themes if they match your use case
2. **Name Models Clearly**: Use descriptive names like "Revenue Analysis Model" or "Cost Management Model"
3. **Document Model Purpose**: Add clear descriptions so users know which model to use
4. **Test Both Models**: Ensure each model answers questions correctly in its domain
5. **Monitor User Feedback**: Review chat logs to see if users are selecting the correct model
6. **Consider User Training**: Educate users on when to use which model

## Troubleshooting

### Issue: Users Getting Wrong Results

**Problem:** Users are asking revenue questions but getting cost results (or vice versa)

**Solution:** 
- Ensure models are clearly named and described
- Check that Assumed Members are set correctly for each model
- Verify Scope includes the correct members

### Issue: Error Code 1008 with Multi-Purpose Dimensions

**Problem:** Copilot returns no response when querying a multi-purpose dimension

**Solution:**
- Verify the Assumed Member is set to a parent that contains data
- Check that the Assumed Member is within Scope
- Ensure the queried member is in the correct hierarchy (customer vs vendor)

### Issue: Users Confused About Which Model to Use

**Problem:** Users don't know which model to select

**Solution:**
- Use clear, descriptive model names
- Add detailed descriptions explaining each model's purpose
- Provide user training on model selection
- Consider creating a "general" model that routes to specific models based on question type

## Summary

- **Multi-purpose dimensions** (like Vendor/Customer) require multiple AI models because you can only set one Assumed Member per dimension per model
- **Pre-built themes** (Revenue Performance, Cost Insights) are designed for common multi-purpose dimension scenarios
- **Workflow and Insights questions** can typically share a single model unless they require different configurations
- **Decision framework**: Use multiple models when dimensions serve conflicting purposes or require different Assumed Members
- **Best practice**: Start with pre-built themes, use clear naming, and document model purposes

By following this guide, you can effectively configure Vena Copilot to handle complex data models with multi-purpose dimensions and different query types.
