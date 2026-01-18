# RAG Bot Response Formatting Guide

## Overview

This document outlines best practices for formatting RAG bot responses to improve readability, user experience, and information clarity.

## Current Implementation

The RAG bot currently returns responses as **plain text strings** with markdown formatting embedded. The frontend displays these as plain text (markdown is not rendered).

## Suggested Formatting Improvements

### 1. Markdown Structure (Already Supported in Prompts)

The system prompt already instructs the LLM to use markdown formatting. The frontend should render this markdown as HTML.

#### Headers

```markdown
# Main Topic (H1 - for major sections)

## Section Title (H2 - for subsections)

### Subsection (H3 - for detailed points)
```

**Best Practice:** Use H2 for major answer sections, H3 for subsections.

#### Lists

```markdown
## Steps to Follow

1. First step description
2. Second step description
3. Third step description

## Features

- Feature one
- Feature two
- Feature three
```

#### Code Blocks

````markdown
```venaql
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()
```
````

#### Emphasis

- **Bold** for important terms: `**Important Term**`
- *Italic* for emphasis: `*emphasis*`
- `Code` for technical terms: `` `dimension name` ``

### 2. Response Structure Patterns

#### Pattern A: Step-by-Step Instructions

```markdown
## How to Configure [Feature]

### Step 1: [Action]
Description of the step with specific details.

### Step 2: [Action]
Next step with configuration values.

### Step 3: [Action]
Final step with verification.

**Important:** Note any critical points here.
```

#### Pattern B: Troubleshooting Responses

```markdown
## Issue Analysis

### Problem
Description of the issue.

### Root Cause
Explanation of why the issue occurs.

### Solutions

**Option 1: [Solution Name]**
- Description
- Code example

**Option 2: [Solution Name]**
- Description
- Code example
```

#### Pattern C: Conceptual Explanations

```markdown
## Overview

[Concept] is [definition]. It works with [related system] because [explanation].

## Key Concepts

### [Concept 1]
Explanation with examples.

### [Concept 2]
Explanation with examples.

## Data Flow

1. Step 1 → Step 2 → Step 3
2. Result and outcome

## Configuration

To configure [feature]:
1. Navigate to [location]
2. Set [value] to [specific value]
3. Save and verify
```

#### Pattern D: Comparison Responses

```markdown
## Comparison: [Feature A] vs [Feature B]

### [Feature A]
- Characteristic 1
- Characteristic 2

### [Feature B]
- Characteristic 1
- Characteristic 2

### When to Use Each
[Feature A] is best for [use case].
[Feature B] is best for [use case].
```

### 3. Visual Formatting Elements

#### Code Blocks

Always use code blocks for:
- VenaQL scripts
- Configuration values
- File paths
- API endpoints
- Error messages

````markdown
```venaql
Scope {
  [Account.Travel Expenses],
  [Entity.All Entities],
  [Measure.Value]
}
```
````

#### Blockquotes for Important Notes

```markdown
> **Important:** You should set the Assumed Member to the parent account, not individual Line Item Details.

> **Note:** Parent members in Scope automatically include their nested children.
```

#### Horizontal Rules for Section Separation

```markdown
## Section 1
Content here.

---

## Section 2
Content here.
```

### 4. Consistent Response Structure

#### Standard Answer Template

```markdown
## [Answer Title]

[Brief overview/introduction paragraph]

### Key Points

- Point 1
- Point 2
- Point 3

### Detailed Explanation

[Detailed explanation with examples]

### Configuration Steps

1. Step 1
2. Step 2
3. Step 3

**Important:** [Critical note or warning]

### Related Information

[Additional context or related topics]
```

#### Troubleshooting Template

```markdown
## Issue Analysis

### Problem
[Description of the issue]

### Root Cause
[Technical explanation of why it occurs]

### Solutions

**Option 1: [Solution Name]**
[Description and steps]

\`\`\`venaql
[Code example]
\`\`\`

**Option 2: [Solution Name]**
[Description and steps]

\`\`\`venaql
[Code example]
\`\`\`

### Verification
[How to verify the fix works]
```

### 5. Typography and Emphasis

#### Use Bold for:
- Important terms (first mention)
- Warning messages
- Step numbers or labels
- Configuration values

```markdown
Set the **Assumed Member** to **'Travel Expenses'** (the parent account).
```

#### Use Italic for:
- Emphasis on specific points
- Notes or asides
- Example scenarios

```markdown
*Note:* This configuration applies to all child Line Item Details.
```

#### Use Code Inline for:
- Dimension names: `` `Account` ``, `` `Entity` ``
- Member names: `` `Travel Expenses` ``
- Configuration values: `` `Assumed Member` ``
- Error codes: `` `Error Code 1008` ``

```markdown
Set the `Account` dimension `Assumed Member` to `Travel Expenses`.
```

### 6. Information Hierarchy

#### Primary Information First
- Most important answer at the top
- Context and details follow
- Examples and references last

#### Progressive Disclosure
```markdown
## Quick Answer
[Brief, direct answer]

## Detailed Explanation
[Full explanation with context]

## Technical Details
[Advanced information for technical users]

## Examples
[Concrete examples with code]
```

### 7. Consistency Guidelines

#### Terminology
- Use consistent terms throughout (e.g., "Line Item Details" vs "LIDs")
- Define acronyms on first use: "Line Item Details (LIDs)"
- Use official Vena terminology from documentation

#### Formatting
- Always use code blocks for VenaQL (```` ```venaql ````)
- Always use numbered lists for sequential steps
- Always use bullet lists for feature lists
- Always use H2 for major sections

#### Tone
- Professional but approachable
- Clear and direct
- Specific with examples
- Helpful and supportive

### 8. Frontend Rendering Recommendations

The frontend should render markdown to HTML for better presentation:

#### Required Markdown Support
- Headers (H1, H2, H3)
- Lists (ordered and unordered)
- Code blocks with syntax highlighting
- Inline code
- Bold and italic
- Blockquotes
- Horizontal rules

#### Visual Styling
- Code blocks: Dark background, monospace font
- Inline code: Light gray background, monospace
- Headers: Clear hierarchy with spacing
- Lists: Proper indentation and spacing
- Blockquotes: Left border, italic text

### 9. Response Length Guidelines

#### Short Answers (< 200 words)
- Direct question → Direct answer
- Single concept
- Simple configuration

#### Medium Answers (200-500 words)
- Multiple concepts
- Step-by-step instructions
- Troubleshooting with one solution

#### Long Answers (500+ words)
- Complex multi-system configurations
- Multiple solution options
- Comprehensive troubleshooting
- Detailed conceptual explanations

**Best Practice:** Use progressive disclosure - provide quick answer first, then detailed sections.

### 10. Examples of Well-Formatted Responses

#### Example 1: Configuration Question

```markdown
## Configuring Line Item Details in Vena Copilot

Line Item Details (LIDs) like 'Flights', 'Hotels', and 'Meals' are nested under parent accounts in the Account dimension hierarchy.

### Configuration Steps

1. Navigate to the Account dimension configuration
2. Set the **Assumed Member** to `Travel Expenses` (the parent account), **NOT** to individual LIDs
3. Include `Travel Expenses` in the Scope configuration

### Why This Works

Parent members in Scope automatically include their nested children. When Copilot queries LID data, it searches within the parent account's scope because:
- LIDs roll up to their parent account in the hierarchy
- Copilot queries work at the parent account level
- The hierarchy ensures all child LIDs are accessible

### Example Configuration

\`\`\`venaql
Scope {
  [Account.Travel Expenses],
  [Entity.All Entities],
  [Measure.Value]
}
\`\`\`

> **Important:** Always configure at the parent level, not individual LID level.
```

#### Example 2: Troubleshooting Question

```markdown
## VenaQL Script Troubleshooting

### Problem
Your script has **2 Scope statements**. The calculation references members that aren't in the active scope.

### Root Cause
In VenaQL, the last Scope statement overrides all previous ones. Your calculation references `[Entity.Homelink]` and `[Account.7300]`, but these aren't in the active (last) Scope.

### Solutions

**Option 1: Combine the Scopes**

\`\`\`venaql
Scope {
  [Account.7200],
  [Account.9300],
  [Account.7300],  // Add missing account
  [Entity.EI Group Eliminations],
  [Entity.Homelink],  // Add missing entity
  [Measure.Value],
  [Measure.Automated Eliminations]
}
\`\`\`

**Option 2: Move Calculation Before Second Scope**

\`\`\`venaql
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
@this = @source1
\`\`\`

### Verification
After applying the fix, verify the script returns expected values for all referenced members.
```

## Implementation Recommendations

### 1. Add Markdown Rendering to Frontend

Install a markdown library:
```bash
npm install react-markdown remark-gfm
```

Update Chat component to render markdown:
```tsx
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

// In message rendering:
<ReactMarkdown remarkPlugins={[remarkGfm]}>
  {message.content}
</ReactMarkdown>
```

### 2. Add Syntax Highlighting for Code Blocks

Install syntax highlighter:
```bash
npm install react-syntax-highlighter @types/react-syntax-highlighter
```

### 3. Update System Prompt (Optional)

The current system prompt already includes markdown formatting instructions. You can enhance it with:

```
RESPONSE FORMATTING:
- Use markdown for all responses
- Use H2 for major sections, H3 for subsections
- Use code blocks (```venaql) for all code examples
- Use bold (**text**) for important terms
- Use lists for step-by-step instructions
- Use blockquotes (>) for important notes
```

### 4. Response Validation

Add validation to ensure responses include:
- Proper markdown structure
- Code blocks for technical examples
- Clear section headers
- Source citations at the end

## Summary

### Key Principles

1. **Structure First:** Use headers, lists, and sections to organize information
2. **Visual Hierarchy:** Make important information stand out (bold, code blocks, headers)
3. **Code Examples:** Always use code blocks for VenaQL and configuration
4. **Progressive Disclosure:** Quick answer first, then detailed sections
5. **Consistency:** Use consistent formatting patterns across all responses

### Quick Checklist

- [ ] Use H2 for major sections
- [ ] Use code blocks for all code examples
- [ ] Use bold for important terms and values
- [ ] Use lists for step-by-step instructions
- [ ] Use blockquotes for important notes
- [ ] Include specific configuration values (not placeholders)
- [ ] Cite sources at the end
- [ ] Keep responses scannable (headers, spacing)

### Next Steps

1. **Add markdown rendering to frontend** (high priority)
2. **Add syntax highlighting for code blocks** (high priority)
3. **Test formatting across different response types** (medium priority)
4. **Add formatting validation** (low priority)
