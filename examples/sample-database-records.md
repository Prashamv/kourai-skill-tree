# Sample Database Records

This file shows mock database-style records. These are not real Kourai records.

## strategies

| id | agent | platform | topic | status |
|---|---|---|---|---|
| 1 | demo_agent | social | launch planning | completed |

## content_drafts

| id | strategy_id | draft_text | risk_level | status |
|---|---|---|---|---|
| 12 | 1 | AI can draft fast, but your brand still needs a checkpoint. | low | reviewed |

## content_reviews

| id | draft_id | quality_score | risk_score | decision |
|---|---|---|---|---|
| 31 | 12 | 8 | 2 | approve_with_human_review |

## post_logs

| id | draft_id | platform | status |
|---|---|---|---|
| 44 | 12 | social | dry_run_only |
