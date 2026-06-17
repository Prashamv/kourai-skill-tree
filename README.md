# Kourai Skill Tree

Kourai is an AI-assisted social media workflow system designed to help brands generate platform-specific strategies, draft content, review AI outputs, and learn from performance data over time.

The project began as PHINN, an experimental AI persona for X/Twitter, and has evolved into a modular product concept focused on AI agents, content workflows, approval systems, database-backed memory, and marketing automation.

This repository is a public case study documenting the skills, architecture, and product thinking developed while building Kourai. The production codebase is private to protect the product logic, prompt chains, API integrations, and automation workflow.

## Start Here

- [Reading Guide](docs/00-reading-guide.md) gives the fastest path through the repo
- [Project Overview](docs/01-project-overview.md) explains what Kourai is
- [Architecture](docs/02-architecture.md) explains the system shape
- [Workflow Breakdown](docs/03-workflow-breakdown.md) explains the main pipeline
- [Skill Tree](docs/04-skill-tree.md) tracks the skills developed through the project
- [Updates](updates/README.md) keeps dated progress notes without exposing private code
- [Private vs Public](docs/08-private-vs-public.md) defines what stays out of this repo

## Current Progress

- Built an early AI persona system through PHINN
- Designed platform-specific social media workflows
- Created a local dry-run task pipeline
- Added approval-first automation logic
- Moved the prototype toward SQLite-backed workflow memory
- Developed a modular architecture around agents, platforms, and core orchestration
- Added early account, platform, performance, historical post, ranking, and voice-profile concepts
- Created a product roadmap for expanding toward TikTok, Instagram, analytics, and brand strategy tools

## Why This Repo Exists

This repo documents what I have learned while building Kourai, including AI workflow design, Python scripting, prompt engineering, product thinking, database planning, and marketing automation strategy.

The goal is to show my growth as a builder and demonstrate how business, AI, and software systems can connect into a real product.

## Repo Map

- `docs/` explains the product concept, architecture, roadmap, and lessons learned
- `updates/` contains sanitized dated build notes
- `examples/` shows mock outputs using fake data
- `diagrams/` contains Mermaid workflow and architecture diagrams
- `mock-code/` contains safe simplified examples, not production Kourai code

## Public Safety Rules

- Do not publish production scripts, prompt chains, API integrations, credentials, local databases, database backups, or raw account data
- Use summaries, diagrams, fake examples, and sanitized learning notes instead of private implementation details
- Keep this repo useful for portfolio reading without turning it into a copy of the private product repo

## Achievement Statement

I built Kourai from an experimental AI persona into an early-stage AI marketing workflow system with agent-based content generation, approval-first automation, database-backed memory, historical performance learning, and a roadmap toward multi-platform social media strategy.
