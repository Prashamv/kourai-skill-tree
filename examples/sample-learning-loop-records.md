# Sample Learning Loop Records

This file uses fake records to show the kind of structured memory Kourai is moving toward. These are not real Kourai records.

## social_accounts

| social_account_id | platform | handle | status |
|---|---|---|---|
| social_demo_x | x | demo_handle | active |

## historical_posts

| id | social_account_id | platform | content_type | topic | posted_at |
|---|---|---|---|---|---|
| 101 | social_demo_x | x | original_post | product positioning | 2026-06-01 |
| 102 | social_demo_x | x | reply | customer insight | 2026-06-04 |

## post_performance

| historical_post_id | likes | replies | reposts | impressions | captured_at |
|---|---|---|---|---|---|
| 101 | 42 | 8 | 5 | 2400 | 2026-06-07 |
| 102 | 18 | 11 | 2 | 1200 | 2026-06-07 |

## historical_post_rankings

| rank_position | window_type | topic | performance_score | reason |
|---|---|---|---|---|
| 1 | weekly | product positioning | 86.4 | Strong engagement and broad reach |
| 2 | weekly | customer insight | 73.1 | High reply rate and useful discussion |

## voice_profiles

| profile_name | source | summary |
|---|---|---|
| demo_voice_profile | historical_posts | Concise, direct, lightly playful, and opinionated |
