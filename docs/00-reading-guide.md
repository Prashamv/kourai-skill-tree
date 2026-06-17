# Reading Guide

This repo is organized as a public case study for Kourai. It is designed to be readable without exposing the private product codebase.

## Fast Path

1. Read [Project Overview](01-project-overview.md) for the product idea.
2. Read [Architecture](02-architecture.md) for the system model.
3. Read [Workflow Breakdown](03-workflow-breakdown.md) for the main pipeline.
4. Read [Skill Tree](04-skill-tree.md) for the builder skills developed.
5. Read [Updates](../updates/README.md) for dated progress notes.
6. Read [Private vs Public](08-private-vs-public.md) before adding anything new.

## Folder Purpose

- `docs/` contains durable explanations of the product, architecture, roadmap, and lessons
- `updates/` contains dated build notes that can be appended over time
- `diagrams/` contains safe high-level Mermaid diagrams
- `examples/` contains fake example records and outputs
- `mock-code/` contains simplified examples only

## Update Pattern

When a private build milestone happens, add a short file under `updates/` and link it from `updates/README.md`. Keep the update focused on:

- what changed at the system level
- what skill or product lesson it represents
- what remains private
- what the next public-safe milestone is

Do not copy private source code, prompts, credentials, real account data, database files, database backups, or raw social content into this repo.
