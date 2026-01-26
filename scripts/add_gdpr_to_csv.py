"""
Script to add GDPR Compliance epic and stories to Phase Jira.csv
"""

import csv
from datetime import datetime
from pathlib import Path

# GDPR Requirements
GDPR_REQUIREMENTS = [
    {
        "req_id": "REQ-001",
        "title": "Data Subject Rights Implementation",
        "priority": "Highest",
        "phase": "Phase 1",
        "gdpr_articles": "15, 17, 20",
        "description": "Users must be able to exercise their fundamental GDPR rights: access to their data, deletion of their data, and export of their data in a portable format. Right of Access (Article 15), Right of Erasure (Article 17), Right to Data Portability (Article 20).",
    },
    {
        "req_id": "REQ-002",
        "title": "Automated Data Retention and Deletion",
        "priority": "Highest",
        "phase": "Phase 1",
        "gdpr_articles": "5(1)(e)",
        "description": "The Privacy Policy commits to specific data retention periods: query logs for 90 days, user accounts for active period plus 30 days, and cached data for 24 hours. Implement automated deletion scripts.",
    },
    {
        "req_id": "REQ-003",
        "title": "Consent Mechanism",
        "priority": "Highest",
        "phase": "Phase 1",
        "gdpr_articles": "7",
        "description": "The Privacy Policy states that users acknowledge reading and understanding the policy by using the service. However, there is no mechanism to track or record this consent.",
    },
    {
        "req_id": "REQ-004",
        "title": "Third-Party Data Processing Agreement Verification",
        "priority": "Highest",
        "phase": "Phase 1",
        "gdpr_articles": "28",
        "description": "The Privacy Policy states that all third-party processors are bound by data processing agreements. However, these agreements have not been verified.",
    },
    {
        "req_id": "REQ-005",
        "title": "Right to Restriction of Processing",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "18",
        "description": "Users have the right to request restriction of processing in certain circumstances. Implement restriction mechanism with user table field and processing logic.",
    },
    {
        "req_id": "REQ-006",
        "title": "Right to Object",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "21",
        "description": "Users have the right to object to processing based on legitimate interests. For query logging, users may object if logging is not essential.",
    },
    {
        "req_id": "REQ-007",
        "title": "Data Breach Notification Procedures",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "33, 34",
        "description": "GDPR requires notification of data breaches to supervisory authorities within 72 hours and to affected users if high risk. Create breach detection and notification procedures.",
    },
    {
        "req_id": "REQ-008",
        "title": "Security Verification and Documentation",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "32",
        "description": "The Privacy Policy lists security measures including encryption, access controls, and monitoring. These measures must be verified and documented.",
    },
    {
        "req_id": "REQ-009",
        "title": "Processing Activities Register (ROPA)",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "30",
        "description": "GDPR requires organisations to maintain a record of processing activities documenting all personal data processing. Create comprehensive ROPA document.",
    },
    {
        "req_id": "REQ-010",
        "title": "Data Minimisation Review",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "5(1)(c)",
        "description": "GDPR requires data minimisation: only collect and process data that is necessary. Review current data collection and implement minimisation where possible.",
    },
    {
        "req_id": "REQ-011",
        "title": "Audit Logging",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "30, 32",
        "description": "Audit logs are required to track data access, modifications, and security events. These logs must be retained for 7 years for compliance purposes.",
    },
    {
        "req_id": "REQ-012",
        "title": "Data Protection Impact Assessment (DPIA)",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "35",
        "description": "A DPIA is required for high-risk processing activities. The system processes personal data using AI/ML technologies, which may constitute high-risk processing.",
    },
]

def add_gdpr_to_csv():
    csv_path = Path("docs/Phase Jira.csv")
    
    # Read existing CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    now = datetime.now().strftime('%d/%b/%y %I:%M %p')
    base_user_id = "70121:94969bbc-eef7-4b93-99d7-210bad207087"
    
    # Create Epic
    epic_row = {k: '' for k in fieldnames}
    epic_row.update({
        'Summary': 'GDPR Compliance Implementation',
        'Issue Type': 'Epic',
        'Status': 'To Do',
        'Project key': 'FRBP2',
        'Project name': 'FCS RAG Bot - Phase 2',
        'Project type': 'software',
        'Project lead': 'Miles Waite',
        'Project lead id': base_user_id,
        'Priority': 'Highest',
        'Reporter': 'Miles Waite',
        'Reporter Id': base_user_id,
        'Creator': 'Miles Waite',
        'Creator Id': base_user_id,
        'Created': now,
        'Updated': now,
        'Labels': 'gdpr;compliance;legal;critical',
        'Description': 'This epic covers all GDPR compliance requirements for the FCS RAG Bot system, as outlined in the GDPR Compliance Business Requirements Document. The requirements are organized into three phases: Phase 1 (Critical), Phase 2 (High Priority), and Phase 3 (Medium Priority). Reference: GDPR/GDPR_COMPLIANCE_BUSINESS_REQUIREMENTS.md',
        'Watchers': 'Miles Waite',
        'Watchers Id': base_user_id,
        'Status Category': 'To Do',
    })
    rows.append(epic_row)
    epic_key = 'GDPR-EPIC'  # Placeholder - will be assigned by Jira
    
    # Create Stories for each requirement
    for req in GDPR_REQUIREMENTS:
        story_row = {k: '' for k in fieldnames}
        story_row.update({
            'Summary': f"{req['req_id']}: {req['title']}",
            'Issue Type': 'Task',
            'Status': 'To Do',
            'Project key': 'FRBP2',
            'Project name': 'FCS RAG Bot - Phase 2',
            'Project type': 'software',
            'Project lead': 'Miles Waite',
            'Project lead id': base_user_id,
            'Priority': req['priority'],
            'Reporter': 'Miles Waite',
            'Reporter Id': base_user_id,
            'Creator': 'Miles Waite',
            'Creator Id': base_user_id,
            'Created': now,
            'Updated': now,
            'Labels': f"gdpr;compliance;{req['phase'].lower().replace(' ', '-')}",
            'Description': f"*Requirement ID:* {req['req_id']}\n*Priority:* {req['priority']}\n*Phase:* {req['phase']}\n*GDPR Articles:* {req['gdpr_articles']}\n\n{req['description']}\n\n---\n_This story is part of the GDPR Compliance Implementation epic._",
            'Parent': epic_key,
            'Parent key': epic_key,
            'Parent summary': 'GDPR Compliance Implementation',
            'Watchers': 'Miles Waite',
            'Watchers Id': base_user_id,
            'Status Category': 'To Do',
        })
        rows.append(story_row)
    
    # Write back to CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Added GDPR Compliance epic and {len(GDPR_REQUIREMENTS)} stories to {csv_path}")
    print(f"   Epic: GDPR Compliance Implementation")
    print(f"   Stories: {len(GDPR_REQUIREMENTS)} requirements (REQ-001 through REQ-012)")

if __name__ == "__main__":
    add_gdpr_to_csv()
