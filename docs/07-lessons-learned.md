# Lessons Learned

## AI Systems Need Structure

Strong prompts are useful, but workflows need clear inputs, outputs, review states, logs, and failure points. Kourai became easier to reason about once PHINN work was routed through repeatable tasks.

## Relational Memory Changes the Product

Moving from JSON files to a relational database made the project feel more like a product system. Account context, run history, content records, performance data, and voice learning can now connect instead of living as separate artifacts.

## Migrations Should Start Early

Schema migrations are easier to introduce before the database becomes large and hard to change. Version tracking, validation, and migration history make future changes less risky.

## Temporary Databases Make Testing Safer

Disposable temporary databases are useful for validating setup and bootstrap behavior without risking the active local database. They make end-to-end workflow testing more repeatable.

## Backups Need Their Own Boundary

Backups protect the local database, but they should not be confused with public artifacts. Keeping backups separate from active databases also makes repository safety easier.

## Every Workflow Record Needs Ownership Context

Connecting workflow records to account context is essential for a product that may support multiple users, social accounts, campaigns, and platforms.

## Validate the Whole Bootstrap

Testing isolated scripts is helpful, but the real confidence comes from validating the full bootstrap path: database setup, migrations, backup creation, account sync, workflow execution, reports, and safety mode.

## AI Coding Tools Still Need Review

Codex can inspect, modify, validate, and document a codebase quickly, but architecture decisions, test results, public/private boundaries, and product claims still need careful human review.
