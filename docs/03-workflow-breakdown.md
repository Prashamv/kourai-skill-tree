# Workflow Breakdown

Kourai is built around multi-step workflows rather than one-shot AI generation.

## Strategy Generation

The system starts by creating content directions based on a persona, brand, platform, campaign goal, or topic.

Expected output:

- topic
- angle
- content type
- risk level
- reason the idea fits

## Draft Generation

The draft step turns strategy into possible posts, replies, or campaign assets.

Expected output:

- draft text
- platform
- topic
- tone tags
- character count
- risk level

## Enhancement

The enhancement step improves the best drafts without changing the core idea.

Possible actions:

- sharpen the wording
- reduce filler
- improve platform fit
- add subtle brand voice

## Gatekeeper Review

The gatekeeper step reviews drafts before they become eligible for scheduling or posting.

Review fields:

- quality score
- risk score
- decision
- reason
- final text

## Logging and Memory

Every important workflow step should create structured records. This makes future analytics, approvals, audits, and recommendations possible.
