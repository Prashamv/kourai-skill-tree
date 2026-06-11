# System Architecture

```mermaid
flowchart LR
    U[User / Brand Goal] --> O[Workflow Orchestrator]
    O --> S[Strategy Agent]
    O --> D[Draft Agent]
    O --> R[Review Gatekeeper]
    O --> P[Platform Layer]
    S --> M[(Structured Memory)]
    D --> M
    R --> M
    P --> M
    M --> A[Analytics and Future Recommendations]
```
