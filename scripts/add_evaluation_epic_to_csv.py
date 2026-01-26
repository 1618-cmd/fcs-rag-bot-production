"""Add RAG Evaluation Framework epic and tasks to existing CSV."""

import csv
from pathlib import Path

# Path to CSV file
csv_path = Path("docs/fcs_rag_bot___phase_2_2026-01-26_07.06am.csv")

# Read existing CSV
rows = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# New Epic
epic_summary = "RAG Evaluation Framework & Quality Metrics"
epic_description = """Implement a math-driven RAG evaluation pipeline that measures retrieval quality, prompt quality, hallucination risk, drift, latency, and cost. The output must be machine-readable (CSV) and suitable for regression testing.

Key Features:
* Retrieval Metrics (pre-LLM): cosine similarity, recall@k
* Output Quality Metrics (post-LLM): self-consistency entropy, output variance
* Hallucination & Grounding: sentence-level support analysis
* Drift Metrics: KL divergence for time-based comparison
* Latency & Cost Tracking
* CSV Export for machine-readable results

This epic supports EPIC-4 (Prompt Engineering & Optimization) and EPIC-1 (A/B Testing)."""

# New Tasks
tasks = [
    {
        "summary": "Implement similarity score logging",
        "description": "Compute top_1_similarity, mean_top_k_similarity, similarity_gap. Hook into RAGPipeline.retrieve() to capture Qdrant scores. Log before LLM call.",
        "phase": "Phase 1"
    },
    {
        "summary": "Implement recall@k for gold queries",
        "description": "Create gold test set structure (JSON format). Implement binary recall check (does gold chunk appear in top-k?).",
        "phase": "Phase 1"
    },
    {
        "summary": "Add latency & cost tracking",
        "description": "Enhance query logging with tokens_in, tokens_out. Implement cost estimation (OpenAI/Anthropic pricing).",
        "phase": "Phase 1"
    },
    {
        "summary": "Create evaluation service module",
        "description": "Create backend/src/services/evaluation.py with pure functions for metric computation. No dependencies on FastAPI/DB. Testable functions.",
        "phase": "Phase 1"
    },
    {
        "summary": "Implement self-consistency entropy (CE proxy)",
        "description": "Run same query N times (configurable, default N=3). Compute semantic similarity between outputs. Calculate variance/entropy as uncertainty proxy. Log ce_proxy and output_variance.",
        "phase": "Phase 2"
    },
    {
        "summary": "Implement hallucination detection",
        "description": "Split answer into sentences. Embed each sentence and compare with retrieved chunks. Classify: fully supported / partially supported / unsupported. Compute hallucination_rate and context_overlap_ratio.",
        "phase": "Phase 2"
    },
    {
        "summary": "Create gold test set",
        "description": "Define 20-30 representative queries. Include expected sources and answer keywords. Store in backend/tests/evaluation/gold_test_set.json.",
        "phase": "Phase 2"
    },
    {
        "summary": "Implement drift metrics",
        "description": "Create backend/src/services/drift_analyzer.py. Load historical CSV logs. Compute KL divergence for similarity and CE-proxy distributions. Compare time windows.",
        "phase": "Phase 3"
    },
    {
        "summary": "Create evaluation runner script",
        "description": "Create backend/scripts/run_evaluation.py. Load gold test set. Execute queries with evaluation hooks. Collect all metrics.",
        "phase": "Phase 3"
    },
    {
        "summary": "Implement CSV export",
        "description": "Define required columns (query_id, top_1_similarity, etc.). Export to backend/evaluation_results/evaluation_YYYY-MM-DD_HHMMSS.csv. Include metadata (llm_provider, model_name, prompt_version).",
        "phase": "Phase 3"
    },
    {
        "summary": "Integration with RAG pipeline",
        "description": "Modify RAGPipeline to support evaluation_mode. Add evaluation hooks (pre-LLM and post-LLM). Return metrics alongside response.",
        "phase": "Phase 3"
    },
    {
        "summary": "Document metric definitions",
        "description": "Clear docstrings explaining each metric mathematically. Document approximations (CE proxy, hallucination detection). Explain thresholds and interpretation.",
        "phase": "Phase 4"
    },
    {
        "summary": "Create unit tests",
        "description": "Test evaluation functions in isolation. Test gold test set loading. Test CSV export format.",
        "phase": "Phase 4"
    },
    {
        "summary": "Integration testing",
        "description": "Test full evaluation pipeline end-to-end. Validate CSV output format. Test with sample gold queries.",
        "phase": "Phase 4"
    }
]

# Add Epic (no key, Jira will assign)
epic_row = {
    "Key": "",  # Empty - Jira will assign
    "Issue Type": "Epic",
    "Parent": "",
    "Summary": epic_summary,
    "Status": "To Do",
    "Assignee": "",
    "Start date": "",
    "Inferred start date": "",
    "Due date": "",
    "Inferred due date": "",
    "Issue color": "purple"
}
rows.append(epic_row)

# Add Tasks (no keys, will link to epic via Parent)
for task in tasks:
    task_row = {
        "Key": "",  # Empty - Jira will assign
        "Issue Type": "Task",
        "Parent": epic_summary,  # Link to epic via summary
        "Summary": task["summary"],
        "Status": "To Do",
        "Assignee": "",
        "Start date": "",
        "Inferred start date": "",
        "Due date": "",
        "Inferred due date": "",
        "Issue color": "purple"
    }
    rows.append(task_row)

# Write back to CSV
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added RAG Evaluation Framework epic and {len(tasks)} tasks to CSV")
print(f"   Epic: {epic_summary}")
print(f"   Total rows in CSV: {len(rows)}")
