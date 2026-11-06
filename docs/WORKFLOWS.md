# LEO 2.0 workflows: product + engineering automation

This document describes **planned agent execution flows** and **repository automation** separately.

## 1. Safe goal execution

~~~mermaid
flowchart LR
  A[User goal] --> B[Validate session + intent]
  B --> C[Bounded plan]
  C --> D{Policy check per step}
  D -->|AUTO| E[Execute typed tool]
  D -->|ASK| F[Approval preview]
  D -->|DENY| X[Explain and stop]
  F -->|Confirm| E
  F -->|Reject| X
  E --> G[Verify external receipt]
  G --> H[Record auditable state]
  H --> I[Report true outcome]
~~~

- Cap total tool calls, runtime, cost and outbound destinations.
- Task states: received, planning, waiting_approval, executing, verifying, completed, failed, canceled.
- Tool outputs are not treated as automatically successful; independent verification is required.
- Persist checkpoints and idempotency keys on consequential writes.
- Cancel/Stop should revoke active local work and provide task status.

## 2. Example workflows

| Goal | Allowed sequence | Approval gate |
| --- | --- | --- |
| Summarize PDF | Picker grant → parse → user-filtered retrieval → cite | Read grant |
| Find research | Query official/public sources → compare → cite with date | Read-only provider auth |
| Organize documents | Propose categories → preview changes | Ask before move/rename |
| Send an email | Compose draft → show recipient + text → send OAuth | Ask immediately before send |
| Explain screen | User taps → OS MediaProjection prompt → sample → explain → stop | Per-session system consent |
| Make image/video | Select authorized provider → show data/cost → queue → verify output | Media rights and spend authorization |
| Use a voice command | Push-to-talk → ASR → intent → policy → TTS → standby | Mic permission and each tool scope |

These are **design specifications**; no implementation is asserted by this document.

## 3. Repository automation

| GitHub file | Trigger | Intended check |
| --- | --- | --- |
| .github/workflows/repo-quality.yml | Push, pull request, manual | Validate repository documentation, test policy helpers, scan example files for obvious placeholder errors |
| .github/dependabot.yml | Scheduled updater | Review GitHub Actions dependency updates via PRs |

Green CI demonstrates only the checks that were executed. It is **not** evidence that the Android app or external models work.

## 4. Verification receipts

Every release-grade external action should produce a record:

~~~json
{
  "task_id": "uuid",
  "action": "read_selected_document",
  "policy_result": "AUTO",
  "state": "verified",
  "executed_at": "ISO-8601",
  "duration_ms": null,
  "evidence_refs": ["authorized-file-id-and-range"],
  "error": null
}
~~~

No real execution timestamps or receipts should be fabricated.

## 5. Workflow safeguards

- Never use user-provided raw documents as trusted workflow instructions.
- Do not expose API credentials in Actions logs, PR comments, or repository files.
- Restrict GitHub workflow token permissions to contents: read unless a task explicitly needs more.
- Avoid deployment steps until there is a production-ready artifact and separate approval.
- Do not make empty commits simply to keep the activity graph green.

## 6. Next operational workflow

Build a first real backend *vertical slice* and add a dedicated backend test workflow only when backend files exist. Implement native Android build checks once an Android project and Gradle wrapper exist; do not create decorative CI that claims to test nonexistent code.