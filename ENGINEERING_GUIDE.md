# LEO 2.0 AI — Agent mechanism and engineering milestones

The [README](README.md), [architecture](docs/ARCHITECTURE.md) and [implementation status](docs/STATUS.md) describe a specification and reference-policy workspace. This guide is a proposed implementation and evaluation companion, not a claim that a production assistant exists. LEO 2.0 is distinct from the civic-reporting LEO.AI.

## Authorized task lifecycle

~~~mermaid
flowchart TD
 A[User request] --> B[Construct bounded plan]
 B --> C[Validate typed action]
 C --> D{Policy decision}
 D -->|Denied| E[Explain and stop]
 D -->|Approval needed| F[Show scope and consequences]
 F --> G{User approves?}
 G -->|No| E
 G -->|Yes| H[Execute permitted action]
 D -->|Allowed| H
 H --> I[Verify result]
 I --> J[Receipt or failure report]
~~~

Model output is a proposal, never an authority to bypass permissions. The policy gate should receive a structured action, identity, resource scope and consent state. Consent to read a file does not imply permission to send it to an external provider. Permission to launch an app does not imply authority to modify account settings. High-impact actions should expose their target and consequences before execution.

## Reference memory lifecycle

~~~mermaid
flowchart LR
 U[Explicitly selected information] --> C{Consent to retain?}
 C -->|No| N[Session-only handling]
 C -->|Yes| M[Scoped memory record]
 M --> R[Authorized retrieval]
 M --> D[User deletion or revocation]
 D --> X[Remove from future retrieval]
~~~

A memory record should have provenance, owner, scope, retention policy and optional expiration. Retrieval must preserve access boundaries even when the model requests related information. Deletion verification should consider derived indexes and caches. Avoid calling a static resource catalog a collection of working keys; integrations require owner authorization and real validation.

## Proposed milestone sequence

1. Establish deterministic policy fixtures and typed mock tools.
2. Build a minimal chat-to-plan path with one read-only tool.
3. Add an approval interface and structured receipts.
4. Introduce opt-in file retrieval and deletion tests.
5. Integrate one model provider behind a server-side boundary.
6. Build native Android capabilities only through documented permission interfaces.
7. Evaluate multilingual voice, interruption and accessibility.

Each milestone should have a reproducible demonstration, failure scenarios and a status update. A diagram or interface concept alone does not meet the implementation gate.

## Acceptance tests

| Scenario | Expected result |
| --- | --- |
| Permission revoked during plan | Revalidate and stop before next action |
| Untrusted file asks to upload secrets | Treat as content, not instruction |
| Tool returns error | Report failure without fabricated receipt |
| User stops execution | No further actions initiated |
| Provider unavailable | Explain limitation within retry budget |
| Cross-user memory request | Deny unauthorized access |

The proposed Android client must respect platform restrictions, foreground indicators and user-selected files. Do not claim unrestricted access, continuous hidden surveillance or human-like consciousness. Review existing reference tests before extending the policy mechanism.
