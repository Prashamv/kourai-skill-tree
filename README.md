# Kourai Skill Tree

Kourai is an early-stage AI marketing workflow prototype for social content strategy, content generation, review, reporting, and performance learning.

PHINN is the first working agent, and X/Twitter is the first platform test case. The private product codebase uses a modular Python workflow system with SQLite-backed memory, account-aware records, schema migrations, reporting tools, and approval-first automation.

This public repository is a sanitized portfolio case study. It documents the product thinking, architecture, skills, roadmap, and lessons learned without exposing production source code, prompts, credentials, API logic, databases, account data, or proprietary implementation details.

## Current Progress

### Implemented Foundation

- Modular Python workflow orchestration
- SQLite-backed structured memory
- Account-aware schema and workflow records
- Migrations, schema tracking, validation, and database backups
- Human-readable exports, reports, database inspection, and analytics exploration
- Strategy, draft, review, reply, logging, run, and historical-ranking records
- Validated PHINN bootstrap workflow
- Analyze-only operation with live posting disabled

### In Development

- Historical-post importing
- Voice and personality analysis
- Adaptive voice profiles
- Performance-based recommendations
- Account memory and strategy-history interfaces

### Planned Product Expansion

- Chat-based product interface
- Approval dashboard
- Richer marketing intelligence
- Instagram and TikTok support
- Multi-platform campaigns
- Optional controlled automation after explicit authorization

## Repo Map

- [docs/](docs/00-reading-guide.md) explains the product, architecture, roadmap, skill tree, and public/private boundary
- [updates/](updates/README.md) contains sanitized dated build notes
- [examples/](examples/sample-database-records.md) contains fictional public-safe records and outputs
- [diagrams/](diagrams/system-architecture.md) contains high-level Mermaid diagrams
- [mock-code/](mock-code/mock_task_orchestrator.py) contains simplified examples only

## Privacy Statement

This repo is intentionally not the production Kourai codebase. Public material is limited to sanitized architecture, documentation, diagrams, mock examples, and progress summaries.

## Achievement Statement

Kourai has grown from an experimental AI persona into an account-aware AI marketing workflow prototype with structured memory, migration-backed SQLite storage, reporting tools, human-controlled review, and a path toward analytics-informed multi-platform content operations.
