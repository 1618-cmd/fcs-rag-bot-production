# Knowledge Base Best Practices & Document Upload Requirements

## Overview

This document outlines best practices for formatting and metadata when uploading documents to the FCS RAG Bot knowledge base. Following these guidelines ensures optimal retrieval and response quality.

## Supported File Formats

The knowledge base supports the following file formats:

- **Markdown (.md)** - **Recommended** for text-based documentation
- **Text (.txt)** - Plain text documents
- **PDF (.pdf)** - For documents that need to preserve formatting

## File Naming Conventions

### Recommended Naming Pattern

Use descriptive filenames with optional prefixes to categorize document types:

```
(Prefix) - Document Title.md
```

### Prefix Categories

- **(Reference)** - Reference materials, glossaries, definitions
  - Example: `(Reference) - Vena Glossary.md`
  
- **(How-To)** - Step-by-step instructions and guides
  - Example: `(How-To) - Access Vena's Training Platform.md`
  
- **(Explainer)** - Conceptual explanations and overviews
  - Example: `(Explainer) - Vena User Roles.md`
  
- **(Troubleshooting)** - Problem-solving guides and error solutions
  - Example: `(Troubleshooting) - Error Code 1008.md`

### Naming Best Practices

✅ **Good:**
- `(How-To) - Creating a VenaQL Script.md`
- `(Reference) - VenaQL Scope Troubleshooting.md`
- `vena_vs_anaplan.md` (for comparison documents)

❌ **Avoid:**
- `document1.md` (not descriptive)
- `Guide (Final) (2).md` (version numbers, special chars)
- `My Document!!.md` (unnecessary special characters)

## Document Structure & Formatting

### Markdown Formatting

#### 1. Headers

Use proper heading hierarchy:

```markdown
# Main Title (H1 - one per document)

## Section Title (H2)

### Subsection (H3)
```

**Best Practice:** Start with a single H1 title, use H2 for major sections, H3 for subsections.

#### 2. Paragraph Breaks

Use blank lines between paragraphs to help the chunking algorithm:

```markdown
This is paragraph one. It contains complete thoughts.

This is paragraph two. It has a clear blank line separation from paragraph one.
```

**Why it matters:** The chunking system uses `\n\n` (double newlines) as the primary separator. Clear paragraph breaks improve chunk quality.

#### 3. Lists

Use proper list formatting:

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

#### 4. Code Blocks

Use code fences for code examples:

````markdown
```venaql
Scope {
  [Account.7200],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}
```
````

#### 5. Emphasis

- **Bold** for important terms: `**Important Term**`
- *Italic* for emphasis: `*emphasis*`
- `Code` for technical terms: `` `code` ``

### Content Organization

#### Document Sections

Organize content with clear sections:

```markdown
# Document Title

## Overview
Brief introduction to the topic.

## Key Concepts
Main concepts explained.

## Step-by-Step Instructions
1. Step one
2. Step two

## Troubleshooting
Common issues and solutions.

## Related Resources
Links or references to related documents.
```

## Metadata Best Practices

### Document Metadata (Implicit)

The system extracts metadata from:
- **File path** - Used for categorization and source citation
- **File name** - Used for display and searching
- **File size** - Used for processing decisions
- **Last modified date** - Used for version tracking

### Folder Organization

Organize documents in logical folders:

```
knowledge_base/
├── Getting Started/
│   ├── Fundamentals/
│   └── Resources/
├── Modeler/
├── Contributor and Tasks/
├── Troubleshooting/
└── Vena Copilot/
```

**Best Practice:** Use folder structure to reflect document categories and topics.

## Content Quality Guidelines

### 1. Clarity and Specificity

✅ **Good:**
```markdown
To configure Line Item Details, set the Assumed Member to 'Travel Expenses' 
(the parent account) in the Account dimension configuration.
```

❌ **Avoid:**
```markdown
Set the appropriate member to the right value in the settings.
```

### 2. Complete Information

Provide full context:
- **What** - What is being configured/explained
- **Why** - Why it matters or when to use it
- **How** - Step-by-step instructions
- **Examples** - Concrete examples with actual values

### 3. Code Examples

Include complete, working code examples:

````markdown
## Example VenaQL Script

```venaql
Scope {
  [Account.7200],
  [Account.9300],
  [Entity.EI Group Eliminations],
  [Measure.Value]
}

@source1 = [Account.7300].Sum()
@this = @source1
```
````

### 4. Technical Details

Include specific technical information:
- Dimension names: `Account`, `Entity`, `Measure`
- Member names: `Travel Expenses`, `EI Group Eliminations`
- Configuration values: Exact settings and options
- Error codes: Specific error codes like `Error Code 1008`

## Chunking Behavior

Understanding how documents are chunked helps optimize formatting:

### Chunking Parameters

- **Chunk Size:** 1000 characters (default)
- **Chunk Overlap:** 200 characters (default)
- **Separators (in order):**
  1. `\n\n` (paragraph breaks)
  2. `\n` (line breaks)
  3. ` ` (spaces)
  4. Empty string

### Optimization Tips

1. **Use paragraph breaks** (`\n\n`) between major concepts
2. **Keep related information together** within paragraphs
3. **Use headings** to separate major sections (helps with context)
4. **Break long paragraphs** into shorter, focused paragraphs
5. **Use lists** for step-by-step instructions (better chunking)

## Common Issues to Avoid

### ❌ Poor Formatting

```markdown
This is one long paragraph with no breaks that goes on and on making it hard to chunk properly and may result in incomplete information being split across chunks.
```

### ✅ Good Formatting

```markdown
This is a well-formatted paragraph with clear ideas.

This is another paragraph with related but distinct information.

The chunking algorithm works best with clear paragraph separation.
```

### ❌ Missing Context

```markdown
Set the member to the correct value.
```

### ✅ Complete Context

```markdown
To configure Line Item Details in Vena Copilot:

1. Navigate to the Account dimension configuration
2. Set the Assumed Member to 'Travel Expenses' (the parent account)
3. Include 'Travel Expenses' in the Scope configuration

This works because LIDs roll up to their parent account in the hierarchy, and Copilot queries work at the parent account level.
```

## Upload Requirements

### Required

- ✅ File format: `.md`, `.txt`, or `.pdf`
- ✅ Encoding: UTF-8 (for text files)
- ✅ File size: Under 10MB (recommended)
- ✅ Content: Non-empty, readable content

### Recommended

- ✅ Descriptive filename with prefix
- ✅ Clear heading structure (H1, H2, H3)
- ✅ Paragraph breaks between concepts
- ✅ Complete, specific information
- ✅ Code examples in proper format
- ✅ Technical details (dimension names, error codes, etc.)

### Optional but Helpful

- ✅ Table of contents (for long documents)
- ✅ Related resources section
- ✅ Version/update date in content
- ✅ Clear section headers

## Example: Well-Formatted Document

```markdown
# (How-To) - Configuring Line Item Details in Vena Copilot

## Overview

Line Item Details (LIDs) allow you to track granular transactions within parent accounts. This guide explains how to configure LIDs for use with Vena Copilot.

## Key Concepts

LIDs are nested under parent accounts in the Account dimension hierarchy. For example, LIDs like 'Flights', 'Hotels', and 'Meals' would be children of the parent account 'Travel Expenses'.

## Configuration Steps

### Step 1: Set Assumed Member

Navigate to the Account dimension configuration and set the Assumed Member to 'Travel Expenses' (the parent account), NOT to individual LIDs like 'Flights' or 'Hotels'.

**Important:** You should set the Assumed Member to the parent account, not individual LIDs, because:
1. LIDs roll up to their parent account in the hierarchy
2. Copilot queries work at the parent account level
3. When users ask about LIDs, Copilot searches within the parent account's scope

### Step 2: Configure Scope

Include the parent account 'Travel Expenses' in Scope. This automatically includes all its LID children (Flights, Hotels, Meals) because parent members in Scope always include their nested children.

## Example Configuration

```venaql
Scope {
  [Account.Travel Expenses],
  [Entity.All Entities],
  [Measure.Value]
}
```

## Related Documents

- (Reference) - Vena Glossary
- (Explainer) - Account Dimension Structure
- (Troubleshooting) - LID Not Appearing in Copilot Results
```

## Additional Resources

- [Markdown Guide](https://www.markdownguide.org/)
- [Vena Support Portal](https://support.venasolutions.com/)

---

**Last Updated:** 2025-01-XX
**Version:** 1.0
