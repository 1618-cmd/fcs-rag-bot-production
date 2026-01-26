"""Check for duplicates in the Jira CSV file."""

import csv
from collections import defaultdict
from pathlib import Path

csv_path = Path("docs/fcs_rag_bot___phase_2_2026-01-26_07.06am.csv")

# Read CSV
rows = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print("=" * 80)
print("CHECKING FOR DUPLICATES IN CSV")
print("=" * 80)
print()

# Check for duplicate summaries
summary_counts = defaultdict(list)
for i, row in enumerate(rows, start=2):  # Start at 2 because row 1 is header
    summary = row.get('Summary', '').strip()
    if summary:
        summary_counts[summary].append({
            'row': i,
            'key': row.get('Key', ''),
            'issue_type': row.get('Issue Type', ''),
            'parent': row.get('Parent', '')
        })

# Find duplicates
duplicates = {summary: entries for summary, entries in summary_counts.items() if len(entries) > 1}

if duplicates:
    print(f"Found {len(duplicates)} duplicate summaries:")
    print()
    for summary, entries in sorted(duplicates.items()):
        print(f"Summary: {summary}")
        print("-" * 80)
        for entry in entries:
            print(f"  Row {entry['row']}:")
            print(f"    Key: {entry['key']}")
            print(f"    Issue Type: {entry['issue_type']}")
            print(f"    Parent: {entry['parent']}")
        print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    total_duplicate_rows = sum(len(entries) for entries in duplicates.values())
    print(f"Total duplicate summaries: {len(duplicates)}")
    print(f"Total rows with duplicates: {total_duplicate_rows}")
    print(f"Would need to remove: {total_duplicate_rows - len(duplicates)} rows")
else:
    print("No duplicate summaries found!")
    print()
    print(f"Total rows in CSV: {len(rows)}")
    print(f"Unique summaries: {len(summary_counts)}")

# Also check for duplicate keys (if any keys are present)
key_counts = defaultdict(list)
for i, row in enumerate(rows, start=2):
    key = row.get('Key', '').strip()
    if key:
        key_counts[key].append({
            'row': i,
            'summary': row.get('Summary', '')
        })

duplicate_keys = {key: entries for key, entries in key_counts.items() if len(entries) > 1}

if duplicate_keys:
    print()
    print("=" * 80)
    print("DUPLICATE KEYS FOUND")
    print("=" * 80)
    for key, entries in duplicate_keys.items():
        print(f"Key: {key}")
        for entry in entries:
            print(f"  Row {entry['row']}: {entry['summary']}")
        print()
