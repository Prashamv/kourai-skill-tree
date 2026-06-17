# Architecture

Kourai is designed around a modular workflow architecture.

## Main Concepts

- Agents: AI personalities or brand assistants that perform specialized work
- Workflows: ordered task sequences such as strategy, drafting, review, and logging
- Gatekeepers: review layers that score content before it can move forward
- Memory: structured records used to track strategies, drafts, reviews, targets, replies, logs, historical posts, performance, and voice profiles
- Account Context: user, social account, platform connection, and campaign ownership data that keeps workflow records organized
- Platforms: social channels such as X/Twitter, TikTok, Instagram, and future integrations

## High-Level Flow

1. A campaign goal or topic starts the workflow.
2. A strategy step creates platform-specific directions.
3. A drafting step turns strategy into content options.
4. An enhancement step improves tone or format.
5. A gatekeeper step reviews content for quality, safety, and brand fit.
6. Approved content becomes eligible for scheduling or posting.
7. Logs and performance records improve future recommendations.

## Learning Loop

Kourai is also moving toward a learning loop:

1. Sync or import owned historical posts.
2. Store post and performance records in structured memory.
3. Rank prior content by time window and performance signals.
4. Analyze historical content for voice and style traits.
5. Use those signals to improve future strategy and recommendations.

## Design Values

- Keep humans in control
- Prefer approval-first automation
- Store structured records instead of loose files
- Keep live publishing behind explicit future authorization
- Separate private production logic from public case-study material
- Build around repeatable workflows, not isolated prompts
