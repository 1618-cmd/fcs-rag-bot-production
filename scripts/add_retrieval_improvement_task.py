"""
Add the retrieval improvement evaluation task to Jira.

This script creates a new task under the "Infrastructure & Code Quality Improvements" epic
(FRBP2-20) for evaluating retrieval improvement options.
"""

import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from src.services.jira import get_jira_client, get_epic_link_field_id
from src.utils.config import settings

def get_epic_link_field_id(jira, project_key: str) -> str:
    """Get the Epic Link field ID for linking tasks to epics."""
    try:
        # Get createmeta for Task issue type
        create_meta = jira.createmeta(
            projectKeys=project_key,
            issuetypeNames=["Task"],
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        fields = create_meta["projects"][0]["issuetypes"][0].get("fields", {})
        
        # Common Epic Link field names
        epic_link_names = ["Epic Link", "Parent Link", "Epic", "Parent"]
        
        for field_id, field_data in fields.items():
            field_name = field_data.get("name", "")
            if any(name in field_name for name in epic_link_names):
                return field_id
        
        # Fallback to common field IDs
        common_ids = ["customfield_10014", "customfield_10011"]
        for field_id in common_ids:
            if field_id in fields:
                return field_id
        
        return None
    except Exception as e:
        print(f"Error detecting Epic Link field: {e}")
        return None

def create_retrieval_task():
    """Create the retrieval improvement evaluation task in Jira."""
    jira = get_jira_client()
    if not jira:
        print("❌ Jira not configured. Please check your .env file.")
        return
    
    project_key = "FRBP2"  # FCS RAG Bot - Phase 2
    epic_key = "FRBP2-20"  # Infrastructure & Code Quality Improvements
    
    # Task details
    summary = "Evaluate and implement retrieval improvements (discussion)"
    
    description = """h2. Objective
Evaluate potential solutions to improve document retrieval for queries that don't match document phrasing well, even when relevant documents exist in the knowledge base.

h2. Current Status
* Query expansion implemented (top_k=20, keyword expansion)
* Issue: Some queries (e.g., "troubleshoot VenaQL incorrect results") not retrieving relevant documents despite them existing in knowledge base

h2. Potential Solutions to Evaluate

h3. Option 1: Hybrid Search (keyword + semantic)
* Combine semantic similarity with keyword matching (e.g., BM25)
* *Pros:* Better for exact term matches; can surface documents that rank lower semantically
* *Cons:* More complexity; requires tuning

h3. Option 2: Query Rewriting with LLM
* Use the LLM to rewrite the query into multiple variations before retrieval
* *Pros:* Can generate more specific queries that match document phrasing
* *Cons:* Extra LLM call; adds latency

h3. Option 3: Reranking
* Retrieve more (e.g., 50), then rerank with a cross-encoder
* *Pros:* Better final ordering
* *Cons:* More compute; requires a reranker model

h3. Option 4: Adjust Prompt Strictness
* Allow synthesis when documents are related but not exact matches
* *Pros:* More flexible answers
* *Cons:* Risk of over-interpretation

h3. Option 5: Multiple Retrieval Strategies
* Run multiple queries (original, simplified, keyword-focused) and merge results
* *Pros:* Broader coverage
* *Cons:* More complexity and cost

h2. Acceptance Criteria
* All options evaluated with pros/cons documented
* Best option(s) selected based on requirements
* Implementation plan created for selected solution(s)
"""
    
    try:
        # Get Epic Link field ID
        epic_link_field = get_epic_link_field_id(jira, project_key)
        if not epic_link_field:
            print("⚠️  Could not detect Epic Link field. Will try to create task without epic link.")
        
        # Prepare issue fields
        issue_dict = {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"},
            "labels": ["retrieval", "rag", "infrastructure"]
        }
        
        # Link to epic if we found the field
        if epic_link_field:
            issue_dict[epic_link_field] = epic_key
            print(f"✅ Will link to epic: {epic_key}")
        
        # Create the task
        new_issue = jira.create_issue(fields=issue_dict)
        
        issue_url = f"{settings.jira_server_url}/browse/{new_issue.key}"
        print(f"\n✅ Created task: {new_issue.key}")
        print(f"   Summary: {summary}")
        print(f"   URL: {issue_url}")
        
        if epic_link_field:
            print(f"   Linked to epic: {epic_key}")
        else:
            print(f"   ⚠️  Epic link not set. Please manually link to {epic_key}")
        
        return new_issue.key
        
    except Exception as e:
        print(f"❌ Error creating task: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("Creating retrieval improvement evaluation task in Jira...")
    print("=" * 60)
    create_retrieval_task()
