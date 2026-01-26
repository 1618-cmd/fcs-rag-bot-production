"""Create Phase 1 epic in FRBP and link GDPR epic to it."""

import os
from dotenv import load_dotenv
from jira import JIRA

env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

jira = JIRA(
    server=os.getenv("JIRA_SERVER_URL"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

def get_epic_name_field_id(jira_client, project_key):
    """Auto-detect Epic Name field ID."""
    try:
        create_meta = jira_client.createmeta(
            projectKeys=project_key,
            issuetypeNames=["Epic"],
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        project_meta = create_meta["projects"][0]
        if not project_meta.get("issuetypes"):
            return None
        
        epic_meta = project_meta["issuetypes"][0]
        fields = epic_meta.get("fields", {})
        
        # Search for Epic Name field
        for field_id, field_data in fields.items():
            if "Epic Name" in field_data.get("name", ""):
                return field_id
        
        # Fallback to common field IDs
        for field_id in ["customfield_10011", "customfield_10014", "customfield_10015"]:
            if field_id in fields:
                return field_id
        
        return None
    except Exception as e:
        print(f"Error detecting Epic Name field: {e}")
        return None

def create_phase1_epic():
    """Create 'FCS RAG Bot - Phase 1' epic in FRBP project."""
    project_key = "FRBP"
    epic_name = "FCS RAG Bot - Phase 1"
    
    # Check if it already exists
    jql = f'project = {project_key} AND summary ~ "{epic_name}" AND issuetype = Epic'
    existing = jira.search_issues(jql, maxResults=1)
    
    if existing:
        print(f"Phase 1 epic already exists: {existing[0].key}")
        return existing[0].key
    
    # Get Epic Name field ID
    epic_name_field_id = get_epic_name_field_id(jira, project_key)
    if not epic_name_field_id:
        epic_name_field_id = "customfield_10011"  # Fallback
    
    # Create epic
    issue_dict = {
        "project": {"key": project_key},
        "summary": epic_name,
        "issuetype": {"name": "Epic"},
        epic_name_field_id: epic_name
    }
    
    try:
        new_epic = jira.create_issue(fields=issue_dict)
        print(f"✅ Created Phase 1 epic: {new_epic.key}")
        return new_epic.key
    except Exception as e:
        print(f"❌ Error creating Phase 1 epic: {e}")
        return None

def link_epics(source_key, target_key, link_type="relates to"):
    """Link two epics together."""
    try:
        # Create a link between the two issues
        jira.create_issue_link(
            type=link_type,
            inwardIssue=source_key,
            outwardIssue=target_key
        )
        print(f"✅ Linked {source_key} to {target_key} ({link_type})")
        return True
    except Exception as e:
        error_msg = str(e)
        if "already linked" in error_msg.lower():
            print(f"ℹ️  {source_key} and {target_key} are already linked")
            return True
        print(f"❌ Error linking epics: {error_msg}")
        return False

print("=" * 80)
print("LINKING GDPR EPIC TO PHASE 1")
print("=" * 80)
print()

# Step 1: Create Phase 1 epic
print("Step 1: Creating 'FCS RAG Bot - Phase 1' epic in FRBP project...")
phase1_key = create_phase1_epic()

if not phase1_key:
    print("❌ Failed to create Phase 1 epic. Exiting.")
    exit(1)

print()

# Step 2: Link FRBP2-105 to Phase 1 epic
print("Step 2: Linking FRBP2-105 (GDPR Compliance) to Phase 1 epic...")
gdpr_key = "FRBP2-105"

# Try different link types
link_types = ["relates to", "relates", "is related to"]
linked = False

for link_type in link_types:
    try:
        linked = link_epics(gdpr_key, phase1_key, link_type)
        if linked:
            break
    except:
        continue

if not linked:
    print(f"⚠️  Could not create automatic link. You may need to manually link:")
    print(f"   {gdpr_key} → {phase1_key}")
    print(f"   Or add FRBP2-105 as a child of {phase1_key} if cross-project linking is enabled.")

print()
print("=" * 80)
print("COMPLETE")
print("=" * 80)
print(f"Phase 1 Epic: {phase1_key}")
print(f"GDPR Epic: {gdpr_key}")
print(f"Link: {'✅ Created' if linked else '⚠️  Manual link may be required'}")
