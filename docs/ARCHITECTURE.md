# System architecture and trust boundaries

**State:** proposed architecture informed by the S1 master guide, not deployed software.

## High-level design

~~~mermaid
flowchart TD
  W[Responsive web dashboard] --> GW[Authenticated API gateway]
  A[Android Kotlin/Compose client] --> GW
  GW --> O[Task orchestrator]
  O --> PO{Policy engine}
  PO -->|AUTO: allowed| R[Provider/tool broker]
  PO -->|ASK| C[Approval + consent UI]
  PO -->|DENY| E[Explain denial]
  C -->|User confirms| R
  R --> L[LLM adapters / public data APIs]
  R --> F[Approved files / media jobs / OAuth tools]
  L --> V[Independent receipt verifier]
  F --> V
  V --> DB[(PostgreSQL + audit)]
  V --> GW
  GW --> W
  GW --> A
  O --> K[(Per-user knowledge + memory)]
~~~

## Bounded service layout

| Service/module | Responsibilities | Boundary |
| --- | --- | --- |
| leo-web | Chat, dashboard, approved file import, AI studio, status, consent, accessibility | No provider secrets in browser |
| leo-android | User-visible microphone, file picker, optional overlay and MediaProjection | Android permission checks per capability |
| api-gateway | Auth/session, rate limits, audit correlation, content size, service dispatch | Trust no client-provided user IDs |
| orchestrator | Task state, bounded steps, cancellation, retries and idempotency | Never run arbitrary model-generated shell commands |
| policy-engine | Deterministic AUTO/ASK/DENY by user/resource/action | Not a language-model prompt |
| model-broker | Licensed provider adapters, health, quota, language and fallback | Server-side owner-issued credentials |
| knowledge | Document validation, chunking, retrieval, citations and deletion | Owner filter before scoring |
| media-worker | Provider jobs, progress, cancellation and result retention | Scope/cost approval |
| observability | Redacted traces, error alerts and verified receipts | Minimize sensitive logging |

## Task lifecycle

~~~text
RECEIVED -> PLAN -> POLICY_CHECK -> [WAITING_APPROVAL] -> EXECUTING
          -> VERIFYING -> COMPLETED / FAILED / CANCELED
~~~

Record each transition with task ID, actor ID, allowed tool, scope, sanitized parameters, start/end time and verified result. Use idempotency keys for effects such as messages, exports or deletions.

## Contract sketch

~~~json
{
  "task_id": "uuid",
  "actor_id": "authenticated-user-id",
  "intent": "summarize_selected_file",
  "resource_ids": ["user-granted-file-id"],
  "policy_decision": "AUTO|ASK|DENY",
  "permission_scope": "read:document/file-id",
  "budget": {"max_calls": 4, "max_seconds": 30},
  "status": "planned",
  "receipt": null
}
~~~

This JSON illustrates data shape only. It does not constitute a running endpoint.

## Proposed API surface

| Operation | Direction | Required guard |
| --- | --- | --- |
| POST /v1/chat/stream | Client → gateway | Authentication, quota, schema |
| POST /v1/knowledge/import | Client → gateway | Scoped uploaded file, AV/MIME/size checks |
| POST /v1/knowledge/query | Client → gateway | Owner ACL + citation results |
| POST /v1/tasks | Client → gateway | Permission classification + idempotency |
| POST /v1/tasks/{id}/approve | Client → gateway | Verified actor, target, action and fresh approval |
| POST /v1/tasks/{id}/cancel | Client → gateway | Authorized task owner |
| GET /v1/tasks/{id} | Client → gateway | Per-user isolation |
| GET /v1/providers/status | Client → gateway | Sanitized health only; never reveal keys |
| POST /v1/media/video/jobs | Client → gateway | Validated capability, duration, spend approval |

## Secure data flow

1. Authenticate and map request to an immutable server-side actor identity.
2. Validate size/schema and classify sensitivity.
3. Choose a bounded plan and request policy verdict per tool.
4. If ASK, pause and require explicit approval of target, cost and scope.
5. Execute only schema-validated, allowlisted adapters.
6. Verify actual receipts and source citations.
7. Persist minimal outcome, permit cancellation and retention controls.

## Recommended technology (proposal)

Kotlin/Jetpack Compose for Android-specific capabilities; React or equivalent for web dashboard; FastAPI/Python for API and orchestration; PostgreSQL with row-level security where applicable; scoped object storage; optional pgvector only after search quality tests; Redis/jobs only when load requires it.

## Implementation caution

Web dashboards cannot create unrestricted Android overlays or gain access to all installed apps merely by being installed as a PWA. A native module and OS-approved interaction are required. For exact permissions, see [PERMISSIONS.md](PERMISSIONS.md).