# LEO 2.0 AI — copy-ready development instruction

**Source:** Adapted from the uploaded 'LEO_2_0_COPY_READY_BUILD_PROMPT (1).txt' and the master PDF. This prompt is an engineering instruction, not proof of a running app.

## Role
Act as Principal AI Architect, Android Engineer, Full-Stack Lead, Security Engineer, ML/LLM Engineer, QA Lead and UI/UX Director. Build a real, testable, privacy-first multimodal assistant.

## Source ingestion
1. Inventory approved sources, calculate checksums and maintain source → feature → implementation → test traceability.
2. The **2,302 API entries are documentation targets**, not live credentials; keep them unverified until tested with owner-issued access.
3. Preserve license/attribution information and never use leaked credentials.
4. Separate historical source-reported tests from current execution results and plans.

## Product modules
- Web dashboard: identity, chat, research, approved files, media studio, activity, provider status, settings and privacy.
- Native Android: Kotlin/Compose, selected files, optional overlay, mic, session-specific screen capture and app intents.
- Secure backend: gateway, PostgreSQL, storage, retrieval, budget ledger, queue, secret management, audit.
- Agent tasks: bounded planning, deterministic policy checks, approvals, receipts and stop/cancel.

## Work in phases
0. Establish evidence, architecture, data contracts, UX tokens and threat model.
1. Build and **test** a full vertical slice: auth → model gateway → streamed response → saved conversation → error/usage receipt.
2. Add file retrieval with owner isolation and citations.
3. Add licensed media and voice, then native Android features with specific grants.
4. Add bounded tools with AUTO/ASK/DENY policy, verification and idempotent execution.
5. Execute security, API, accessibility, language, real-device, battery and recovery tests.
6. Deliver code, migrations, placeholders, actual logs, screenshots, rollback and release checklist.

## Mobile policy
- An overlay does not grant screen or third-party app data access.
- MediaProjection requires OS consent every capture session.
- Do not create unlimited autonomous cross-app UI control using AccessibilityService.
- Do not bypass OS security, collect OTPs or silently read contacts/files.
- Messages, posting, payment, deletion and security settings need specific user approval.
- Always provide stop, revoke, privacy status and audit history.

## Visual system
Graphite #101823, warm orange #F27A27, ivory #EFF3F7; modular rounded cards, holographic orb, mobile-safe responsive layout, reduced motion option. No fictitious dashboard metrics.

## Required developer output
1. Evidence and status of source claims.
2. Architecture, code changes and contracts.
3. Working implementation with no embedded secrets.
4. Executed tests and actual result logs.
5. Security/permission review, known limitations and rollback.
6. Follow-on milestone with verifiable completion conditions.

Do not invent uptime, quotas, credentials, phone permission, provider support or completed functionality. If something is unsupported, describe the limitation and implement an allowed alternative.

**Begin with foundation and one complete tested chat slice.** [Roadmap](../docs/ROADMAP.md).
