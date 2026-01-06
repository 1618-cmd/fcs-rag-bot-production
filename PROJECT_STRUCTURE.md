# Project Structure

Production folder structure for the Vena RAG Bot.

## Root Level

```
FCS RAG Bot Production/
├── backend/              # FastAPI backend application
├── frontend/             # Next.js frontend application
├── knowledge_base/       # Vena documentation (markdown/text files)
├── infrastructure/       # Deployment and infrastructure configs
├── scripts/              # Utility scripts (deployment, migration)
├── docs/                 # Project documentation
├── tests/                # Root-level tests (if needed)
└── [Documentation files] # README.md, PROJECT_CONTEXT.md, etc.
```

## Backend Structure

```
backend/
├── src/
│   ├── api/              # FastAPI application
│   │   ├── routes/       # API route handlers
│   │   └── __init__.py
│   ├── core/             # Core RAG logic
│   │   ├── rag.py        # RAG pipeline
│   │   ├── ingestion.py  # Document ingestion
│   │   └── retrieval.py  # Vector retrieval
│   ├── services/         # Business logic layer
│   │   ├── cache.py      # Redis caching service
│   │   ├── logging.py    # Query logging service
│   │   └── analytics.py  # Analytics service
│   ├── models/           # Data models
│   │   ├── database.py   # Database models (SQLAlchemy)
│   │   └── schemas.py    # Pydantic schemas
│   ├── utils/            # Utility functions
│   │   ├── config.py     # Configuration management
│   │   └── helpers.py    # Helper functions
│   └── __init__.py
├── tests/
│   ├── unit/             # Unit tests
│   ├── integration/     # Integration tests
│   └── __init__.py
├── requirements.txt      # Python dependencies
└── README.md
```

## Frontend Structure

```
frontend/
├── src/
│   ├── app/              # Next.js app directory
│   ├── components/       # React components
│   ├── lib/              # Utilities and helpers
│   └── styles/           # CSS/styling
├── public/               # Static assets
├── package.json
└── README.md
```

## Infrastructure Structure

```
infrastructure/
├── docker/
│   ├── Dockerfile        # Backend Docker image
│   └── docker-compose.yml
└── railway/
    ├── railway.json      # Railway configuration
    └── Procfile          # Process definitions
```

## Scripts Structure

```
scripts/
├── deployment/
│   └── deploy.sh         # Deployment scripts
└── migration/
    └── migrate_kb.sh     # Knowledge base migration
```

## Knowledge Base Structure

```
knowledge_base/
├── issue_resolutions/    # Historical issue resolutions
├── patterns/             # Code patterns and examples
├── concepts/             # Vena concepts and explanations
└── troubleshooting/      # Troubleshooting guides
```

## Notes

- **Old POC code**: The `src/` folder at root level contains the original POC code. This will be refactored and moved into `backend/src/core/` during migration.
- **Tests**: Unit and integration tests are organized under `backend/tests/`.
- **Configuration**: Environment variables and configs will be managed through `.env` files (not committed to git).

