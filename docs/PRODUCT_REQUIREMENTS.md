# LEO 2.0 product requirements

**Status:** specification; no production features claimed. Based on S1/S2/S3 in [SOURCES.md](SOURCES.md).

## Vision

Build a user-directed, responsive personal AI assistant that can discuss goals, retrieve cited information, use verified third-party services and perform **explicitly authorized** tasks across a web dashboard and native Android companion.

The assistant may decide how to sequence permitted low-risk operations; it must not grant itself permission or make irreversible personal decisions.

## User jobs

| ID | User need | Expected user-visible outcome | Release |
| --- | --- | --- | --- |
| PR-01 | Chat and research | Stream grounded replies; surface source date and errors | A |
| PR-02 | Ask about selected documents | User selects files; answers cite authorized passages | A/B |
| PR-03 | Know what the AI is doing | Step progress, receipts, cancel, pending approval | A/C |
| PR-04 | Work in Telugu and English | Text support first; code-mixed voice tested on devices | B/C |
| PR-05 | Use AI with a phone | Official Android intents, user-selected files and opt-in overlay | B |
| PR-06 | Understand a shared screen | OS prompt every capture, persistent indicator and stop | B |
| PR-07 | Create media | Real provider jobs with costs, license rules and status | C |
| PR-08 | Control privacy and memory | Per-user settings, access review, export and deletion | A/C |

## Capability tiers

1. **L0 — Suggest only:** no external operations.
2. **L1 — Read within approved scopes:** public research and specifically selected files.
3. **L2 — Reversible local changes:** draft, tag or preview in authorized workspace.
4. **L3 — External write:** explicit per-action approval and receipt.
5. **L4 — High impact:** fresh confirmation; some operations categorically blocked.

Levels do not override Android restrictions, provider scopes or platform policy.

## Baseline experience (Release A)

- Passwordless or verified authentication option; server-validated sessions.
- Streamed responses from one successfully tested provider using server-only secrets.
- Clear loading, empty, partial, failure, retry and offline states.
- Conversation save/delete/retention preferences and source citations.
- Per-user usage limits and task audit.
- Keyboard navigation, screen-reader naming, reduced motion and mobile safe areas.
- Provider unavailable fallback: truthful explanation, not fabricated output.

## Explicitly out of scope for launch

- Any promise of invisible screen recording, persistent microphone capture, blanket device storage access or protected third-party app data.
- OTP/password harvesting, unrestricted background surveillance, or bypassing OS dialogs.
- Unbounded autonomous app interaction via AccessibilityService.
- Claims that all public APIs are available, free, healthy, unlimited or authenticated.
- Any AI model training on private conversations/documents without separate rights and consent.

## MVP evidence

The first valid demo must show **a real, reproducible chat vertical slice**: authorized request → gateway auth and quota → provider response → streamed UI state → persisted conversation → trace/receipt → graceful failure. A screenshot, hardcoded sample answer or API URL alone does not meet this condition.

## Non-functional acceptance targets to define and test

Report actual baseline and p95 response times, provider error rate, citation support, privacy boundary outcomes, request cost, crash rate and battery consumption. No target in this document is presented as an achieved benchmark.

## Decision rules

- User grants only the minimum scope needed for a concrete feature.
- Each tool operation rechecks identity, resource ownership, scope, expiration, destination, impact and quota.
- Sensitive or irreversible actions require fresh visible approval.
- Unknown provider state is **unknown**, not healthy.
- Features without end-to-end evidence remain **planned**.

See [ROADMAP.md](ROADMAP.md) for milestone gates and [TEST_PLAN.md](TEST_PLAN.md) for acceptance cases.