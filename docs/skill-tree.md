# Skill Tree

## AI and Context Engineering

Kourai now uses context-aware voice and generation guidance instead of relying on a single fixed persona instruction.

Skills demonstrated:

- Persona and brand-voice design
- Historical voice learning
- Content-type-specific voice analysis
- Layered effective-voice composition
- User-controlled voice overrides
- Context-aware generation
- Safety precedence
- Generation traceability

Kourai example: original posts, replies, quote/commentary-style writing, and strategy generation can use related but context-appropriate voice guidance.

## Backend and Python Development

Kourai has grown from isolated scripts into a modular local backend prototype.

Skills demonstrated:

- Modular Python architecture
- Task orchestration
- Shared core services
- Error handling
- Configuration management
- Refactoring and technical-debt removal
- Local service integration

Kourai example: workflows route through reusable orchestration layers rather than one-off scripts.

## Databases and Data Pipelines

SQLite is the source of truth for workflow memory, learning inputs, chat persistence, and validation.

Skills demonstrated:

- SQLite schema design
- Account-linked records
- Database migrations
- Backups and fresh-database testing
- Historical post ingestion
- Content classification
- Ranking and performance data
- Conversation persistence
- Human-readable exports

Kourai example: historical posts can be imported, classified, connected to performance signals, and used in later learning workflows.

## Automation and Safety

Kourai is designed around approval-based automation rather than unsupervised posting.

Skills demonstrated:

- Dry-run workflows
- Gatekeeper review
- Approval-required actions
- Action allowlists
- Confirmation before modifying or external tasks
- Live-posting protection
- Auditable run and action records

Kourai example: chat-confirmed generation actions route into existing workflows while live-posting protection remains active.

## Testing and Validation

The project now includes validation across database, voice, orchestration, and safety behavior.

Skills demonstrated:

- Compilation checks
- Database setup tests
- Migration-state validation
- Risk-setting tests
- Voice-learning tests
- Effective-voice tests
- Chat-orchestration tests
- Temporary isolated databases
- Mock task runners for safe orchestration testing

Kourai example: validation scripts check effective voice merging, resets, fallback behavior, safety precedence, chat intent routing, persistence, and response shape.

## Product and Business Skills

Kourai reflects a shift from a single bot toward a broader marketing workflow platform.

Skills demonstrated:

- Product reframing from bot to platform
- Marketing workflow design
- Human-in-the-loop product strategy
- Multi-account architecture planning
- Public/private repository strategy
- Intellectual-property awareness
- MVP prioritization
- Technical documentation

Kourai example: the public skill-tree repo communicates product and technical growth without mirroring the private implementation.
