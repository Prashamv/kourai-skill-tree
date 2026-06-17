# Lessons Learned

## AI Systems Need Structure

Strong prompts are useful, but workflows need structure around them. A good AI product needs clear inputs, outputs, review states, and logging.

## Safety Should Be Designed Early

Approval gates, risk scoring, and dry-run behavior are easier to design early than to bolt on later.

## Files Are Good for Prototypes

JSON files are useful while learning. But as soon as workflows become multi-step, structured database records become more important.

## Product Thinking Matters

The technical system only matters if it solves a real workflow problem. Kourai became stronger when it shifted from "AI persona" to "marketing workflow system."

## Public and Private Work Should Be Separated

The real product code should stay private. A public case study can still show learning, architecture, product thinking, and technical growth without leaking the implementation.

## Learning Systems Need Ownership Context

Once Kourai started storing account, social account, platform, run, and performance context together, the product became easier to reason about. A useful AI workflow needs to know which account generated the data, which platform it came from, and which run created or used it.

## Updates Need Structure Too

A public case-study repo becomes more useful when progress is added through a repeatable update pattern. Dated notes, fake examples, and high-level diagrams make it easier to show growth without exposing private product logic.
