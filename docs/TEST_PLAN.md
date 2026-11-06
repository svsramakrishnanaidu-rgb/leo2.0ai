# QA and acceptance matrix

**Current app-level result:** **NOT EXECUTED**. The supplied PDF provides test cases and expected evidence; it does not prove a built LEO 2.0 app passed them.

## Master acceptance cases

| ID | Test | Severity | Expected evidence |
| --- | --- | --- | --- |
| T01 | Account separation | P0 | User A cannot read User B document/task |
| T02 | Expired/revoked permission | P0 | Next read denied after grant revoked |
| T03 | Overlay without permission | P0 | Bubble does not appear |
| T04 | Screen capture consent | P0 | Fresh Android consent every session |
| T05 | Stop screen capture | P0 | Active projection/buffers released |
| T06 | PDF prompt injection | P0 | Untrusted file text cannot authorize tool |
| T07 | External write approval | P0 | No send/write without specific confirmation |
| T08 | Provider rate limit | P1 | HTTP 429 bounded retry and visible state |
| T09 | Provider outage | P1 | Unknown/error, never invented result |
| T10 | Idempotent write | P0 | Retried effect not duplicated |
| T11 | RAG citations | P1 | Claims cite permission-filtered passages |
| T12 | Telugu-English speech mix | P1 | Measured ASR/response behavior |
| T13 | Low-battery behavior | P1 | Lower workload without losing data |
| T14 | Task survival/cancellation | P1 | Queued operation safely restored/stopped |
| T15 | Media cost and duration | P0 | Provider and budget hard caps respected |
| T16 | Account/document deletion | P0 | Chunks, vectors and caches purged |
| T17 | Secrets scan | P0 | No real keys in frontend bundle or Git history |
| T18 | Android Accessibility restrictions | P0 | No unrestricted general UI agent |
| T19 | Device matrix | P1 | Android versions, OEMs and screens tested |
| T20 | Backup restore | P0 | Recovery works without resurrecting deleted users |

## Test-evidence record

~~~json
{
  "test_id": "T04",
  "build_sha": "actual-commit-sha",
  "device": "real-device-model",
  "android_version": "actual-version",
  "executed_at": null,
  "expected": "system permission displayed for each new projection",
  "actual": null,
  "result": "NOT_RUN",
  "owner": null,
  "issue_id": null
}
~~~

Update fields only after a real test. The example above is a schema illustration, not a test result.

## CI vs end-to-end proof

Repository checks can validate Markdown structure, link destinations, and any unit tests for future code. They cannot establish speech accuracy, Android consent, cloud privacy, model quality, or Play Store compliance. Those require controlled integration, real devices and human review.

## Release gate

- Zero open P0 issues affecting auth, privacy, consent, deletion, payment or security.
- At least one verified working authorized provider with real streaming results.
- All sensitive tool actions checked by deterministic policy and independently verified.
- Backend tenant ACLs, RLS where applicable, and revocation tested.
- Real Android device evidence for overlay/capture/stop where those features ship.
- Backups and restoration measured, including deleted-data non-resurrection.
- Privacy/Terms/account deletion reflect actual data processing and pass review.
- Accessibility, multilingual, performance and failure-state evidence attached.

## Testing priority

**First:** repository sanity tests and contract model unit tests. **Then:** staging auth and chat provider integration. **Finally:** multimodal, cross-app, Android real-device and release tests.

Never use test-plan completeness as a proxy for an implemented application.