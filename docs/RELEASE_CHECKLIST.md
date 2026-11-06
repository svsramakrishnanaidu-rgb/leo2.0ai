# LEO 2.0 release-readiness checklist

**Release state:** NOT READY. This checklist is a proposed launch gate, not a certificate.

## Identity, data and privacy

- [ ] Verified registration/login/logout and session revocation
- [ ] Per-user authorization and RLS or equivalent server-enforced ACL
- [ ] Consent grants enforced in server code before every tool
- [ ] Privacy notice matches actual data use and recipients
- [ ] Export, erase, and retention behavior tested across caches and backups
- [ ] API credentials server-only; scan frontend bundle and Git history
- [ ] Real data encrypted at rest where required and TLS in transit

## AI and integrations

- [ ] At least one provider tested using owner-issued credentials
- [ ] Provider contract, model ID, latency, error handling and quota measured
- [ ] Responses cite source passages when using retrieval
- [ ] Prompt injection cannot trigger external actions
- [ ] Model hallucinations and partial failures correctly labeled
- [ ] External writes and payments require explicit action preview and approval

## Android

- [ ] Real-device test on target SDK versions and hardware
- [ ] User-visible mic, foreground service and capture indicators
- [ ] MediaProjection requests valid OS consent for each session
- [ ] Stopping capture releases buffers, session and notifications
- [ ] Overlay works only when user-enabled and does not imply data access
- [ ] No blanket storage access or autonomous AccessibilityService misuse
- [ ] Microphone standby after speech, no feedback re-trigger

## Product and operational

- [ ] Every screen handles loading, empty, offline, error and retry states
- [ ] Accessible navigation and text scaling evaluated
- [ ] Reduced-motion and low-battery behavior tested
- [ ] Crash/error monitoring and redacted audit logs available
- [ ] Rate limits, spend caps and cancellation verified
- [ ] Backup/restore rehearsed with deletion non-resurrection test
- [ ] Rollback plan, owner and incident channel documented
- [ ] All T01–T20 test results attached with real evidence
- [ ] No unresolved P0 bugs; distribution policy reviewed at release time

If any mandatory gate fails or lacks evidence, keep launch blocked. Follow [TEST_PLAN.md](TEST_PLAN.md).
