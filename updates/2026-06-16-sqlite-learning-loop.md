# 2026-06-16 - SQLite Learning Loop and Safer Workflow Foundation

## Summary

The private Kourai build moved from a mostly linear PHINN prototype toward a stronger workflow platform foundation. The work centered on database-backed run context, account-aware records, historical post learning, safer task orchestration, and clearer public/private separation.

This public note documents the system progress without publishing production scripts, prompts, credentials, API details, raw account data, or local database files.

## What Changed

- Expanded the orchestrator concept so each workflow run can carry account, social account, platform connection, platform, autonomy level, status, and notes.
- Added more explicit task categories for account sync, historical post sync/import, historical post ranking, user voice analysis, and the existing PHINN dry-run content workflow.
- Added an analyze-only bootstrap flow that can connect the account learning steps before content generation.
- Kept live posting forced off during development, preserving a dry-run and approval-first operating model.
- Added a migration layer concept with numbered SQL files, migration tracking, checksum validation, and database backup behavior before applying pending schema changes.
- Extended the database model toward users, social accounts, platform connections, runs, strategy records, content drafts, reviews, target discovery, replies, post logs, query history, performance snapshots, historical posts, voice profiles, personality traits, products, and campaigns.
- Added a historical post ranking concept that can compare prior content by account, platform, time window, score, and engagement signals.
- Added a voice-learning concept that can turn owned historical posts into structured voice profiles and traits.
- Improved inspection and run-summary tooling so workflow state can be reviewed without opening the raw database manually.
- Added upload safety hygiene around database backups so local backup files are not treated as publishable project artifacts.

## Skills Demonstrated

- SQLite-backed workflow design
- Schema migration planning
- Account-aware product modeling
- Agent and platform context propagation
- Historical performance analysis
- Voice profile and trait extraction planning
- Human-in-the-loop automation design
- Safety-first publishing controls
- Public/private repo hygiene

## Public Safety Review

The public skill-tree update intentionally keeps the following private:

- production Python scripts
- API request logic and credentials
- prompt chains and exact generation instructions
- target selection details
- scoring implementation details
- raw historical posts
- local SQLite databases and backups
- real account identifiers beyond generic public-safe labels

Only architecture summaries, learning notes, fake examples, and high-level system descriptions belong in this repository.

## Project Direction After This Update

Kourai is now framed less like a one-off content generator and more like a learning workflow system. The next public-safe milestones are:

- clearer diagrams for the account learning loop
- fake examples of historical performance records
- a public-safe explanation of approval states
- a roadmap note for turning learned voice and performance data into recommendations
