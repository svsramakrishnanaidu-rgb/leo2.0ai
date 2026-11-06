# Engineering roadmap and release gates

**Status as of repository initialization:** Source-informed documentation created. There is **no verified running LEO 2.0 backend, Android APK, web app, model gateway, RAG or agent**.

The master PDF recommends a phased delivery sequence, not a promise to build the full app in a few days.

| Phase | Build objective | Exit criterion | Status |
| --- | --- | --- | --- |
| **P0 — Foundation** | Source provenance, repository, requirements, permissions, architecture, CI, contracts | Traceable specifications and basic repository tests pass | In progress |
| **P1 — Core vertical slice** | Auth, session, backend gateway, one chat provider, server-held secret, streaming, saved conversation | Real signed user request → observed provider output → saved record and error tests | Not started |
| **P2 — Knowledge** | Selected-file upload, source hashes, indexed chunks, owner-filtered retrieval, citations | Gold-file Q&A; no cross-user access | Not started |
| **P3 — Voice and media** | Authorized STT/TTS, multilingual tests, real image provider or media queue | Real outputs and usage receipts, no invented status | Not started |
| **P4 — Native Android** | Kotlin/Compose, picker, overlay, microphone and MediaProjection consent | Real-device permission/revoke/stop tests | Not started |
| **P5 — Scoped agent tasks** | Typed tools, bounded plan graph, approval/verification, OAuth connectors | Per-tool policy checks; external writes explicitly confirmed | Not started |
| **P6 — Production hardening** | Monitoring, secrets review, backup, disaster recovery, privacy and release checks | No unresolved P0, audited restores and rollback | Not started |
| **P7 — Scale/evaluate** | Extra adapters, caching, model choice, optional on-device inference | Every new capability passes license/privacy/quality gates | Not started |

## P0 implementation tasks

- [x] Inventory supplied master PDF, DOCX and prompt (metadata and provenance)
- [x] Publish repo README and organized foundational specs
- [ ] Establish shared API schema validation with executable tests
- [x] Add isolated reference policy decision function and unit tests (not integrated with API auth)
- [x] Run and verify repository document / policy checks in GitHub Actions
- [ ] Adopt issue templates, review rules and release status tracking
- [ ] Run initial threat model and privacy risk review
- [ ] Confirm deployment target and SDK/API versions

These checkboxes are updated only after observable evidence exists.

## P1 build sequence (next implementation work)

1. Create backend skeleton with health/readiness endpoints and strict request schemas.
2. Configure auth and account separation; enforce ownership server-side.
3. Implement an AI provider gateway with server-only secret and per-user rate limiting.
4. Stream one response with cancellation, error boundaries and provider receipt.
5. Save permitted messages and support deletion/export.
6. Test quota exhaustion, provider outage, cross-user ID attempts and account logout.
7. Create a mobile-first web chat screen with streaming status and error handling.
8. Attach build/test logs, a staging URL and an honest release note.

## Completion definition for every feature

- Design + contract
- Actual implementation
- Non-sensitive reproducible test data
- Executed tests and CI evidence
- UX and accessibility verification
- Security/permissions review
- Documentation and rollback notes
- Explicit status: planned / prototype / staging-verified / production

## Risk register

| Risk | Severity | Response |
| --- | --- | --- |
| 2,302 API docs misrepresented as ready providers | High | Unverified registry; owner-keys and real probes |
| Android permission overreach | Critical | Native SDK consent; restrictive defaults |
| Prompt injection via public docs | Critical | Retrieval as data, code-level authorization |
| Leaked provider secret | Critical | Server-only secret manager, rotation and scanning |
| Sensitive data sync without consent | Critical | Explicit transfer and revocation, tenant ACL |
| Quota or video cost overrun | High | Hard spend cap, bounded retries, clear estimate |
| Heavy animations harming phones | Medium | Reduced motion and battery-aware quality tier |
| Provider schema drift | Medium | Contract tests and circuit breakers |

## Important release decision

No app-store submission or production announcement before the [test gates](TEST_PLAN.md), user-data disclosures, backup restore and actual external integration checks pass. A design mockup is not a shipped application.