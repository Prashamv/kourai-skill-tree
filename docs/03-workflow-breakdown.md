# Workflow Breakdown

Kourai is built around multi-step workflows rather than one-shot AI generation.

## Core Workflow

1. Account, campaign, topic, or chat context starts the workflow.
2. Kourai retrieves relevant database context instead of loading every record.
3. Strategy, draft, reply, enhancement, review, synchronization, or learning tasks run through the orchestrator.
4. Gatekeeper and approval controls decide whether an output can move forward.
5. Records are persisted for later inspection, reporting, and learning.

## Learning Workflow

1. Import or synchronize owned historical content.
2. Classify content as original posts, replies, or quote/commentary-style posts.
3. Connect historical content with performance signals.
4. Build learned voice sections for different writing contexts.
5. Compose an effective voice for each generation context.
6. Store metadata so outputs can be traced back to the context that informed them.

## Chat-Orchestrated Workflow

1. A user asks a question or requests an action.
2. The chat orchestrator classifies intent using deterministic rules, with optional model-assisted classification.
3. The system selects relevant database context.
4. Questions return structured answers.
5. Actions require confirmation when they are modifying, external, or expensive.
6. Confirmed actions route into existing Kourai task workflows while live-posting protections remain in place.

This public description omits prompts, source code, exact scoring formulas, and internal decision rules.
