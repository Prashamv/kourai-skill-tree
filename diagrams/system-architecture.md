# System Architecture

```mermaid
flowchart LR
    U[User / Brand Goal] --> O[Workflow Orchestrator]
    AC[Account Context] --> O
    O --> S[Strategy Agent]
    O --> D[Draft Agent]
    O --> R[Review Gatekeeper]
    O --> P[Platform Layer]
    O --> L[Learning Loop]
    S --> M[(Structured Memory)]
    D --> M
    R --> M
    P --> M
    L --> M
    M --> A[Analytics and Future Recommendations]
```
