# Security policy — LEO 2.0 AI

## Project status
This is a research-backed engineering repository. The app, cloud integrations and native device features are **not production-certified or operational merely because they are documented here**.

## Credentials
- Never commit API tokens, service-account JSON, OAuth secrets, private keys, user passwords or unredacted device files.
- Never paste credentials from third-party repositories or PDFs.
- Store provider keys server-side in a secrets manager, not in Android APKs, frontend bundles or logs.
- Rotate any leaked token and audit logs, deployments and Git history.
- Use least-privilege GitHub Actions token permissions.

## AI tool trust boundaries
- Model output, web pages and uploaded documents are untrusted data.
- Enforce permission in deterministic application code, not only in a model prompt.
- Use per-tool scopes, usage budgets, approved destinations, typed arguments and independent receipts.
- No stealth phone surveillance or platform restrictions bypass.

## Mobile privacy
- Overlay is display-only permission, never automatic screen-reading authority.
- Screen capture uses OS consent per MediaProjection session and visible stop.
- Microphone is off by default; prefer push-to-talk.
- Files and photos are user-selected and revocable; no blanket harvesting.
- Do not collect OTP/password fields or ambient audio.

## Data protection
- Authenticate backend sessions; enforce owner access rules on knowledge, memory and task records.
- Implement privacy/export/delete before public launch.
- Test purge across caches, embeddings, backups and signed URLs.
- Protect sensitive logs and cap rate/cost.

## Reporting a vulnerability
Do not disclose active credentials, user data or exploitation steps in public issues. Contact the owner privately using their GitHub profile or GitHub private vulnerability reporting if enabled. Include a reproducible, sanitized description and impacted revision.

## Security gates
See [QA acceptance matrix](docs/TEST_PLAN.md). Block release for unresolved P0 issues in auth, consent, data isolation, deletion, external actions or secrets.

## Third-party rights
Uploaded PDFs and embedded ZIPs may contain content with distinct licenses. No broad republication or execution of third-party material without license and integrity review. See [source register](docs/SOURCES.md).
