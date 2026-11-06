# Android permissions, autonomy and tool-use policy

**Status:** policy specification; features must be tested against supported Android versions and current distribution rules.

## Principle: a language model is not an authorization service

Allow a model to propose tasks; enforce authorization using **deterministic backend and native code**. Every action checks user identity, named capability, resource owner, permission scope, consent age, target, data sensitivity and cost.

~~~mermaid
flowchart LR
  A[User request] --> B[Plan]
  B --> C{Policy}
  C -->|AUTO| D[Approved scoped tool]
  C -->|ASK| E[Visible approval preview]
  C -->|DENY| F[Explain refusal]
  E -->|Approve| D
  D --> G[Verify receipt]
  G --> H[Audit + user-visible result]
~~~

## Action classification

| Level | Example | Policy |
| --- | --- | --- |
| L0 | Explain how to find a file | Text only, no tool |
| L1 | Summarize a user-selected PDF | AUTO only if file grant is valid |
| L2 | Draft a suggested filename list | Reversible preview |
| L3 | Send a message or publish a post | ASK with specific destination and preview |
| L4 | Delete a file, change account security or spend money | Fresh confirmation; deny when unsupported |

## Device capability matrix

| User goal | Supported engineering path | Required limitation |
| --- | --- | --- |
| Open a webpage or compatible app | Explicit Android intents/deep links | No hidden navigation of protected views |
| Choose documents | Storage Access Framework picker | Only selected URIs, honor revocation |
| Choose photos | System Photo Picker | Not full-gallery scraping |
| Show floating orb | TYPE_APPLICATION_OVERLAY after user enablement | Overlay cannot read screen contents |
| Explain visible screen | MediaProjection with OS consent per capture session | Active indicator, foreground service when required, stop |
| Speak/listen | RECORD_AUDIO runtime permission | Push-to-talk default, mute/standby |
| Optional contacts | Contact picker or narrowly justified official permission | Never silently upload all contacts |
| Calendar/email | User-authorized OAuth integrations/system intents | Confirm external writes |
| Notifications | Narrow optional notification listener | Disclosure, clear opt-in and retention |
| Cross-app autonomous taps | Do **not** implement general-purpose AccessibilityService agent | Review actual Play policy; prefer visible intents |

## Screen sharing contract

1. User taps **Explain this screen**.
2. Show app/window scope, cloud transfer warning and retention policy.
3. Request OS MediaProjection consent **for this session**.
4. Start foreground capture service and persistent visible indicator.
5. Stop and erase transient buffers on explicit stop, revocation, process restriction or projection callback.
6. Redact sensitive elements when possible; never claim redaction is infallible.

## Audio contract

Only activate after supported input action or opted-in, policy-compliant trigger. Do not automatically restart listening during synthesized speech. Distinguish listening/processing/speaking/standby. Provide a visible mute/stop control.

## Tool authorization pseudocode

~~~text
authorize(user, action, resource, consent, policy):
  if not authenticated(user): return DENY
  if resource.owner != user and not explicitly shared: return DENY
  if consent.expired or not covers(action, resource): return DENY
  if action is forbidden_by_platform_or_provider: return DENY
  if action is external_write or high_impact: return ASK
  if action is read_only and within time/usage budget: return AUTO
  return DENY
~~~

A prompt saying "yes, I have permission" is not a substitute for an authenticated grant.

## Abuse cases to test

Expired grant, guessed object ID, external link exfiltration, prompt-injected PDF that says "send secrets", upload without approval, capture running in background, overlay enabled without screen consent, voice feedback loop, and stop button not terminating jobs.

## Policy references

- [Android document picker](https://developer.android.com/training/data-storage/shared/documents-files)
- [Android MediaProjection](https://developer.android.com/media/grow/media-projection)
- [Android overlay window parameters](https://developer.android.com/reference/android/view/WindowManager.LayoutParams)
- [Google Play Accessibility guidance](https://support.google.com/googleplay/android-developer/answer/10964491)

Provider and platform policies change. Review them at implementation and release time, not only from the source PDF.