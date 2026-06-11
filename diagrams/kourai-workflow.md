# Kourai Workflow

```mermaid
flowchart TD
    A[Campaign Goal / Topic] --> B[Strategy Generator]
    B --> C[Content Drafts]
    C --> D[Enhancement Step]
    D --> E[Gatekeeper Review]
    E --> F{Approved?}
    F -->|Yes| G[Ready for Posting / Scheduling]
    F -->|No| H[Revise or Reject]
    G --> I[Post Log]
    I --> J[Performance Data]
    J --> B
```
