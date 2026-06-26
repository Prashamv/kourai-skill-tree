# Lessons Learned

## AI Systems Need Structure

Strong prompts are useful, but product behavior needs clear inputs, outputs, review states, logs, and failure paths. Kourai became easier to reason about once PHINN work was routed through repeatable tasks and persisted records.

## Relational Memory Changes the Product

Moving from loose artifacts to SQLite made the project feel more like a real workflow system. Account context, run history, content records, performance data, voice learning, and chat sessions can now connect across workflows.

## Voice Needs Context

Original posts, replies, and quote/commentary-style posts are not the same writing task. Separating those contexts makes learned voice more useful and reduces the risk of flattening every output into one generic style.

## User Control Needs Guardrails

Voice overrides are useful only if they cannot weaken core safety behavior. Kourai's effective-voice direction keeps user preferences layered under safety precedence.

## Chat Is a Backend Orchestration Problem

The important chat milestone is not visual interface polish. The harder backend problem is intent classification, context selection, approval routing, persistence, and safe task execution.

## Validation Should Follow the Workflow

Testing isolated scripts helps, but confidence improves when validation covers database setup, migrations, backups, learning behavior, effective voice, chat orchestration, and live-posting protection.
