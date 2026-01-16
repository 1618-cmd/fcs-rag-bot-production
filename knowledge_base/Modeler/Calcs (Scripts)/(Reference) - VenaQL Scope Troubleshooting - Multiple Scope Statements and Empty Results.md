# (Reference) VenaQL Scope Troubleshooting - Multiple Scope Statements and Empty Results

## Overview

This document provides comprehensive guidance on troubleshooting VenaQL scripts that return no values, with a specific focus on multiple Scope statement conflicts and calculation scope mismatches.

## Understanding Scope Statement Behavior

### Single Scope Statement

A VenaQL script typically starts with a single Scope statement that defines the slice of the data model the calculation will operate on:

```
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Department.Undefined],
  [Measure.Value]
}

@this = [Account.7300].Sum()
```

### Multiple Scope Statements - Critical Behavior

**IMPORTANT: When multiple top-level Scope statements are present in a VenaQL script, the last Scope statement takes precedence and overrides all previous Scope statements.**

This means:
- The first Scope statement is effectively ignored
- Only the last Scope statement defines the active scope for calculations
- Any calculations defined after the last Scope will operate within that scope only

### Example of Scope Override

```
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}

@source1 = [Account.7300].Sum()
@this = @source1
```

**Problem:** The calculation `@source1` references `[Account.7300]`, but the active scope (from the second Scope statement) only includes `[Account.9300]`. Since `[Account.7300]` is not in the active scope, the calculation may return no values or fail.

**Why this happens:**
1. The second Scope statement overrides the first
2. The calculation tries to access `[Account.7300]` which is not in the active scope
3. The script returns no values because the calculation cannot find data for members outside the active scope

## Common Causes of Empty Results

### 1. Scope Statement Conflicts

**Symptom:** Script has multiple Scope statements, calculation references members not in the last Scope.

**Diagnosis:**
- Identify all Scope statements in the script
- Check which Scope is the last one (this is the active scope)
- Verify that all members referenced in calculations are included in the active scope

**Solution:**
- Combine scopes into a single Scope statement if they should work together
- Move calculations before the second Scope if they need the first Scope's context
- Add missing members to the last Scope statement
- Use nested Scope statements if you need different scopes for different calculations

### 2. Member Not in Active Scope

**Symptom:** Calculation references a member that exists in the data model but isn't in the active Scope.

**Example:**
```
Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}

@source1 = {
  [Entity.Homelink],  // NOT in active scope
  [Account.7300],     // NOT in active scope
  [Counterparty.EI]  // NOT in active scope
}.Sum()
```

**Solution:**
- Add the missing members to the active Scope statement
- Or restructure the script to use the correct scope for the calculation

### 3. Empty Intersections

**Symptom:** Scope is correctly defined, but the intersection of all members has no data.

**Diagnosis:**
- Check if data exists for the specific intersection
- Verify that all dimension members in the scope have data
- Use Vena's data inspection tools to verify data availability

**Solution:**
- Verify source data exists for the intersection
- Check if data needs to be imported or calculated first
- Ensure all prerequisite calculations have run

### 4. Incorrect Scope Nesting

**Symptom:** Nested Scope statements don't inherit or override as expected.

**Important:** Nested Scope statements inherit context from parent Scope, but can override specific members. However, calculations defined after nested scopes operate within the innermost active scope.

**Example:**
```
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations]
}

Scope {
  [Account.9300]  // This overrides [Account.7200] from parent scope
}

@this = [Account.7300].Sum()  // This calculation operates in the scope with [Account.9300]
```

**Solution:**
- Understand that nested scopes can override parent scope members
- Ensure calculations reference members that exist in the active (innermost) scope
- Consider using separate calculations for different scopes if needed

## Troubleshooting Steps

### Step 1: Identify All Scope Statements

1. Locate all `Scope { }` statements in the script
2. Count how many top-level (non-nested) Scope statements exist
3. Identify which Scope statement is the last one (this is the active scope)

### Step 2: Map Calculation Dependencies

1. List all members referenced in calculations (variables, functions, etc.)
2. Check if each referenced member is included in the active Scope
3. Identify any members referenced outside the active scope

### Step 3: Verify Data Availability

1. Check if data exists for the intersection defined by the active Scope
2. Use Vena's drill-down or data inspection tools to verify
3. Ensure prerequisite calculations have completed

### Step 4: Check for Scope Conflicts

1. Compare the first Scope with the last Scope
2. Identify which members are in the first but not the last Scope
3. Determine if calculations need those members

### Step 5: Apply Appropriate Fix

Based on your analysis, choose one of these solutions:

**Option A: Combine Scopes**
```
Scope {
  [Account.7200],
  [Account.9300],  // Include both accounts
  [Entity.EI Group Eliminations],
  [Measure.Value],
  [Measure.Automated Eliminations]
}
```

**Option B: Move Calculation Before Second Scope**
```
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()  // Calculate before second scope

Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}

@this = @source1
```

**Option C: Add Missing Members to Active Scope**
```
Scope {
  [Account.7200],
  [Account.9300],
  [Account.7300],  // Add missing account
  [Entity.EI Group Eliminations],
  [Entity.Homelink],  // Add missing entity
  [Counterparty.EI],  // Add missing counterparty
  [Measure.Value],
  [Measure.Automated Eliminations]
}
```

**Option D: Use Nested Scopes for Different Calculations**
```
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()

Scope {
  [Account.9300],
  [Measure.Automated Eliminations]
}

@this = @source1  // Uses value calculated in first scope context
```

## Best Practices

### 1. Use Single Scope When Possible

If all calculations need the same scope, use a single Scope statement:

```
Scope {
  [Account.7200],
  [Account.9300],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()
@this = @source1
```

### 2. Comment Your Scopes

Add comments explaining why each scope is needed:

```
Scope {
  // First scope: Define base context for source calculation
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()

Scope {
  // Second scope: Target scope for final calculation
  [Account.9300],
  [Measure.Automated Eliminations]
}

@this = @source1
```

### 3. Verify Member Existence

Before writing calculations, verify that:
- All referenced members exist in the data model
- All referenced members are in the active scope
- Data exists for the intersection

### 4. Test Incrementally

1. Test with a single Scope first
2. Add additional scopes one at a time
3. Verify each calculation works before adding the next

## Common Error Patterns

### Pattern 1: Multiple Top-Level Scopes

**Problem:**
```
Scope { [Account.A] }
Scope { [Account.B] }
@this = [Account.C].Sum()  // Account.C not in active scope (Account.B)
```

**Fix:** Add Account.C to the second Scope, or combine scopes.

### Pattern 2: Calculation After Scope Override

**Problem:**
```
Scope { [Entity.A], [Account.X] }
@source = [Account.Y].Sum()  // Calculated in first scope
Scope { [Entity.B], [Account.Z] }  // Overrides first scope
@this = @source  // But source was calculated for Entity.A, not Entity.B
```

**Fix:** Ensure calculations use the correct scope context, or restructure.

### Pattern 3: Missing Dimension in Scope

**Problem:**
```
Scope {
  [Account.7200],
  [Measure.Value]
  // Entity dimension missing - will use all entities
}

@this = [Entity.SpecificEntity].Sum()  // May not work as expected
```

**Fix:** Explicitly include the Entity dimension in the Scope.

## Related Topics

- **Vena Calcs - 2 - Notation and Syntax:** Detailed explanation of Scope statement syntax and nesting
- **Vena Calcs - 9 - Troubleshooting:** General troubleshooting guide for VenaQL scripts
- **Vena Calcs - 8 - Examples:** Examples of Scope statements in various scenarios

## Summary

When troubleshooting VenaQL scripts that return no values:

1. **Check for multiple Scope statements** - The last Scope overrides previous ones
2. **Verify calculation members are in active scope** - Calculations can only access members in the active Scope
3. **Check data availability** - Ensure data exists for the intersection
4. **Understand scope precedence** - Last Scope wins, nested scopes inherit but can override
5. **Use appropriate fix** - Combine scopes, restructure, or add missing members

Remember: In VenaQL, the active scope is always defined by the last top-level Scope statement, and all calculations after that Scope operate within that scope only.
