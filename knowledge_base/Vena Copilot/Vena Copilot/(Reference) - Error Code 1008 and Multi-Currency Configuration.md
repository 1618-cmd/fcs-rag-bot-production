# Error Code 1008 and Multi-Currency Configuration in Vena Copilot

## Overview

Error Code 1008 occurs when Vena Copilot cannot find intersection values for the Assumed Member or when the MQL query returns no data. In multi-currency data models, this error commonly occurs when Local Currency is included in Scope or when the Assumed Member is incorrectly configured.

## Error Code 1008: What It Means

Error Code 1008 appears with the message: "No results found for this prompt. Please identify specific members from your data model in your prompt."

### Common Causes

1. **Assumed Member has no intersection values**: The Assumed Member may have a rollup operator (~) that ignores all children, resulting in no data
2. **Local Currency in Scope**: Local Currency contains mixed currencies that cannot be meaningfully summed, causing Copilot to return no response
3. **MQL query returns no data**: The query may be looking at parent members instead of bottom-level values
4. **Data permissions**: User may not have access to the queried data

## Multi-Currency Data Models: Local Currency vs Reporting Currency

### The Problem with Local Currency

In multi-currency data models, the Currency dimension typically has two hierarchies:

```
Currency Dimension:
  ├── Local Currency
  │     ├── CAD (Canadian Dollar)
  │     ├── EUR (Euro)
  │     └── GBP (British Pound)
  └── Reporting Currency
        ├── USD (US Dollar) - Primary reporting currency
        └── GBP (British Pound)
```

**Why Local Currency Causes Issues:**

1. **Mixed Currencies**: Local Currency contains a mix of all currencies used across different entities. For example:
   - Entity A: 100 CAD
   - Entity B: 50 EUR
   - Entity C: 75 GBP
   - Local Currency total: 225 (meaningless - can't add CAD + EUR + GBP)

2. **Cannot Be Summed**: Adding different currencies together produces meaningless results. Local Currency is typically used for data input, not reporting.

3. **Error Code 1008**: When Copilot tries to query Local Currency, it may return no response because the mixed currency data cannot be meaningfully analyzed.

### The Solution: Exclude Local Currency from Scope

**Correct Configuration:**

1. **Scope Configuration**:
   - Set Scope to "iDescendants of Reporting Currency" or "All Reporting Currencies"
   - This includes: USD, GBP, EUR (or your reporting currencies)
   - This EXCLUDES: Local Currency and its children (CAD, EUR, GBP in local context)

2. **Assumed Member Configuration**:
   - Set Assumed Member to your primary reporting currency (e.g., "USD")
   - NOT "All Currencies" or "Local Currency"
   - This ensures Copilot defaults to reporting currency when currency isn't specified

3. **Why This Works**:
   - Reporting currencies are converted to a common currency (usually USD)
   - All values in Reporting Currency hierarchy are in the same currency
   - Copilot can meaningfully analyze and sum these values
   - Users can still specify other reporting currencies (GBP, EUR) if they're in Scope

## Example Configuration

### Currency Dimension Structure

```
Currency Dimension:
  ├── All Currencies (Parent)
  │     ├── Local Currency (EXCLUDE from Scope)
  │     │     ├── CAD
  │     │     ├── EUR
  │     │     └── GBP
  │     └── Reporting Currency (INCLUDE in Scope)
  │           ├── USD (Set as Assumed Member)
  │           └── GBP
  └── No Currency
```

### Correct Scope and Assumed Member Settings

**Scope:**
- Include: "iDescendants of Reporting Currency" or "All Reporting Currencies"
- This includes: USD, GBP (reporting currencies)
- This excludes: Local Currency, CAD, EUR, GBP (in local context)

**Assumed Member:**
- Set to: "USD" (primary reporting currency)
- NOT: "All Currencies" or "Local Currency"

### How It Works

1. **User asks: "What is revenue in 2023?"**
   - Copilot uses Assumed Member: USD
   - Returns revenue in USD (reporting currency)

2. **User asks: "What is revenue in 2023 in GBP?"**
   - User specified GBP
   - Copilot returns revenue in GBP (if GBP is in Scope)

3. **User asks: "What is revenue in 2023 in local currency?"**
   - Local Currency is NOT in Scope
   - Copilot responds: "Cannot access that data because it falls outside the Scope"

## Relationship to FX Conversion Function

### How FX Conversion Works

1. **Data Input**: Contributors input data in their local currencies (CAD, EUR, GBP)
2. **FX Conversion**: The FX conversion function converts local currencies to reporting currency (USD)
3. **Data Storage**: Converted data is stored in the Vena data model in reporting currency
4. **Copilot Queries**: Copilot queries the converted data, not the raw local currency data

### Key Points

- **Copilot doesn't perform conversions**: It queries already-converted data
- **FX conversion happens before Copilot queries**: Data must be converted and saved first
- **Copilot queries reporting currency data**: The data model contains converted values in reporting currencies
- **Local Currency is for input only**: Not for reporting or Copilot queries

## Troubleshooting Error Code 1008 in Multi-Currency Models

### Step 1: Check Scope Configuration

1. Navigate to Vena Copilot → Builder → Select AI Model → Manage Dimensions
2. Select Currency dimension
3. Verify Scope includes ONLY reporting currencies
4. Verify Local Currency is EXCLUDED from Scope

### Step 2: Check Assumed Member

1. In Manage Dimensions, select Currency dimension
2. Verify Assumed Member is set to a reporting currency (e.g., "USD")
3. Verify Assumed Member is NOT "All Currencies" or "Local Currency"

### Step 3: Verify Data Model Structure

1. Check Currency dimension hierarchy in Modeler
2. Verify Reporting Currency parent exists
3. Verify Local Currency is separate from Reporting Currency

### Step 4: Check Rollup Operators

1. If Error Code 1008 persists, check rollup operators
2. Assumed Member should have children with (+) operator (sum), not (~) operator (ignore)
3. If all children are ignored (~), Assumed Member will have no intersection values

### Step 5: Verify Data Permissions

1. Ensure user has Data Permissions to view reporting currency data
2. Check if data permissions are restricting access to currency data

## Best Practices

1. **Always exclude Local Currency from Scope** in multi-currency models
2. **Set Assumed Member to primary reporting currency** (usually USD)
3. **Include all reporting currencies in Scope** (USD, GBP, EUR, etc.)
4. **Test queries** after configuration to verify Error Code 1008 is resolved
5. **Document currency configuration** for future reference

## Common Mistakes

1. **Including Local Currency in Scope**: Causes Error Code 1008 because mixed currencies can't be analyzed
2. **Setting Assumed Member to "All Currencies"**: May not have intersection values, causing Error Code 1008
3. **Setting Assumed Member to "Local Currency"**: Contains mixed currencies, causes meaningless results
4. **Not setting Assumed Member**: Copilot may default to wrong currency or return Error Code 1008

## Summary

- **Error Code 1008**: Occurs when Copilot can't find intersection values for Assumed Member
- **Local Currency**: Should be EXCLUDED from Scope in multi-currency models
- **Reporting Currency**: Should be INCLUDED in Scope
- **Assumed Member**: Should be set to primary reporting currency (e.g., USD)
- **FX Conversion**: Happens before Copilot queries; Copilot queries converted data
- **Scope Configuration**: "iDescendants of Reporting Currency" excludes Local Currency automatically

## Related Documentation

- Troubleshooting: Vena Copilot Error Code 1008 or CSV Report Downloaded Is Blank/Empty
- How-To: Managing Scopes in Vena Copilot
- How-To: Managing Assumed Members in Vena Copilot
- Reference: Vena's Foreign Exchange (FX) Conversion Function
