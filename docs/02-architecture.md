# Architecture

Kourai is organized around account-aware workflows, structured memory, reporting, and human-controlled automation.

## 1. Account Context

Workflow records are connected through account context. This keeps users, social accounts, platform connections, runs, content records, reports, and future campaign data scoped to the right owner.

Support for multiple social accounts per user is part of the product direction and is being validated through the current database and workflow foundation.

## 2. Task Orchestrator

The task orchestrator routes work between local workflow steps such as account sync, historical-post preparation, ranking, strategy generation, drafting, review, replies, and logging.

Runs carry status, autonomy level, platform context, and notes so each workflow can be inspected after execution.

## 3. Agent and Platform Workflows

PHINN is the first working agent. X/Twitter is the first platform test case.

The architecture keeps agent behavior, platform-specific work, and core orchestration separate so future agents and platforms can be added without turning the system into one large script.

## 4. Gatekeeper and Approval Layer

Kourai is designed around approval-first operation. Drafts and replies are reviewed before they can move forward, and current testing remains analyze-only with live posting disabled.

Optional controlled automation is planned only after explicit authorization and stronger product controls exist.

## 5. SQLite Memory and Analytics Layer

Kourai now uses SQLite-backed structured memory rather than loose JSON artifact storage. The database stores workflow history, account-aware content records, historical posts, performance signals, voice data, and reporting inputs.

Migrations validate schema state before workflows run. Backups protect the local database during setup, testing, and schema changes.

Historical posts and rankings form the foundation of the learning loop. The learning engine is active development, not a finished autonomous recommendation system.

## 6. Reports and Inspection Tools

Human-readable exports, account reports, performance reports, a database viewer, and an analytics explorer make the stored workflow data easier to inspect without exposing raw private data in this public repo.

## 7. Future User Interface

The long-term interface direction is chat-based control with modular account, approval, analytics, campaign, and report tools. The current public repo documents that direction at a high level only.
