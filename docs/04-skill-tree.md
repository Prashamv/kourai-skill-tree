# Kourai Skill Tree

## 1. AI Behavior and Prompt Systems

Designing PHINN helped turn AI output from generic text into controlled agent behavior.

Skills:

- Persona design
- Brand voice control
- Output constraints
- Tone and safety rules
- Platform-specific writing
- Context-aware generation

Kourai example: PHINN uses structured behavior and review expectations for X/Twitter strategy, drafts, and replies.

## 2. Python Application Development

Kourai moved from small scripts into a more organized Python application.

Skills:

- Modular file organization
- Reusable task runners
- Environment and dependency debugging
- Error handling
- Refactoring JSON workflows into SQLite workflows
- Separating core logic from local workflow scripts

Kourai example: The private build uses a modular task orchestrator instead of isolated one-off scripts.

## 3. Workflow Orchestration and Automation

Kourai is built as a sequence of inspectable workflow steps.

Skills:

- Task orchestration
- Sequential workflow design
- Run status tracking
- Analyze-only execution
- Human-in-the-loop approval
- Reproducible bootstrap testing

Kourai example: The PHINN bootstrap workflow validates database setup, migrations, account sync, ranking, and reporting while live posting remains disabled.

## 4. SQLite Database Engineering

The project now uses SQLite-backed structured memory for workflow state and learning inputs.

Skills:

- Relational schema design
- Foreign-key-based account scoping
- Structured content records
- Historical performance storage
- Voice profile storage
- Querying workflow history

Kourai example: Runs, content records, account records, historical posts, and performance signals can be connected through account-aware storage.

## 5. Schema Migrations, Backups, and Data Safety

The database foundation includes migration tracking and backup behavior.

Skills:

- Migration development
- Schema version tracking
- Database validation
- Automated backups
- Temporary test databases
- Separating backups from active databases

Kourai example: The private workflow validates schema state before running and creates backups during setup and testing.

## 6. Analytics, Reporting, and Inspection Tools

Kourai needs human-readable ways to inspect stored workflow data.

Skills:

- Report generation
- Human-readable database exports
- Account reports
- Performance reports
- Database viewing
- Analytics exploration

Kourai example: Reports and inspection tools help review account, workflow, and performance state without exposing raw private data publicly.

## 7. Account-Aware Software Architecture

The product direction requires records to belong to the right account and platform context.

Skills:

- Account-aware workflow design
- Social account modeling
- Platform connection modeling
- Run context propagation
- Multi-account planning
- Campaign and product ownership modeling

Kourai example: Workflow runs carry account, social account, platform, autonomy, and status context.

## 8. AI Learning-System Design

The learning engine is being built around owned historical content and performance signals.

Skills:

- Historical post importing
- Historical post ranking
- Writing-style analysis
- Tone and personality trait detection
- Adaptive voice profiles
- Performance-based recommendation planning

Kourai example: Historical posts and rankings provide the foundation for future strategy recommendations.

## 9. Product and Marketing Strategy

Kourai connects AI system design with a real marketing workflow problem.

Skills:

- Product positioning
- Marketing workflow design
- Brand safety thinking
- Campaign planning
- Approval workflow design
- Multi-platform roadmap planning

Kourai example: Kourai is positioned as a middle layer between social platforms, marketing teams, analytics, and future advertising workflows.

## 10. Git, GitHub, Documentation, and Repository Security

The public repository is intentionally separate from the private product codebase.

Skills:

- Repository cleanup
- Public-safe documentation
- Sanitized examples
- GitHub portfolio presentation
- Separating public material from private intellectual property
- Avoiding credential, prompt, database, and account-data leaks

Kourai example: The skill-tree repo documents progress through summaries, diagrams, fake examples, and dated updates instead of production code.

## 11. AI-Assisted Development with Codex

Codex has been used as a coding collaborator while keeping architecture and safety decisions human-reviewed.

Skills:

- Inspecting an existing codebase
- Modifying docs and code safely
- Validating changes with local commands
- Reviewing git status and diffs
- Debugging environment issues
- Turning private progress into public-safe documentation

Kourai example: Codex helped inspect, modify, validate, and document the project while preserving the public/private boundary.
