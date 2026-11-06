# LEO 2.0 — premium UI/UX specification

**Status:** design proposal; the visuals in the source PDF are mockups, not a functioning product.

## Visual direction

LEO combines a dark productivity workstation with a distinctive **orange holographic assistant**. It should feel useful, trustworthy and responsive rather than visually noisy.

| Token | Value | Use |
| --- | --- | --- |
| Base / deep graphite | #101823 | App canvas, side navigation |
| Bright warm orange | #F27A27 | Primary actions, active orb |
| High contrast ivory | #EFF3F7 | Main text |
| Secondary slate | #A6B3C1 | Metadata and labels |
| Success | #2B8C72 | Verified completion |
| Danger | #C65353 | Errors, consent revocation |
| Grid | 4 / 8 / 12 / 16 / 24 / 32 dp | Consistent spacing |
| Cards | 18–24 dp corners | Soft-3D modular surfaces |

Avoid heavy animation when Reduced Motion is enabled; measure battery use on real phones.

## Core navigation

### Web layout

- Fixed/expandable left navigation: Home, Chat, Research, Knowledge, Media Studio, Tasks, Activity, Provider Status, Settings and Privacy.
- Primary region: active conversation or workflow, scrollable with keyboard-safe positioning.
- Optional right inspector: sources, tool approvals, task receipts and quota status.
- Header: project identity, model/connection badge, quick search, notifications, user menu.
- Mobile web: bottom nav for 3–5 destinations, single column, 44+ px touch targets and safe-area padding.

### Native Android shell

- Chat + push-to-talk, approved-file picker, consent center, notifications and settings.
- A **draggable orange orb** when overlay permission is explicitly enabled.
- Android intents for launching permitted app activities.
- Screen-sharing action must open OS consent UI and show active stop control.

## Floating assistant state specification

| State | Visual | Mic/screen behavior | User exit |
| --- | --- | --- | --- |
| IDLE | Soft ring, neutral | No listening | Tap to expand |
| LISTENING | Distinct waveform + mic indicator | User-triggered active mic | Stop/mute |
| THINKING | Sparse moving particles + activity label | Mic normally paused | Cancel |
| SPEAKING | Actual speech-synced waveform | No accidental ASR self-trigger | Interrupt |
| ACTING | Current task step + receipt | Only approved capabilities | Stop |
| CONFIRM | Action, target, consequences, Approve/Reject | Paused external action | Reject/confirm |
| STANDBY | Static/muted orb | No ambient capture | Explicit tap/wake |

**Orb dimensions (proposal):** 48–60 dp resting bubble, ~300–360 dp expansion, maximum 80% of height. Edge-snap drag with safe areas avoiding system bars and keyboard. Long press: Mute / Hide / Disable Overlay / Privacy Center.

## Screen-by-screen acceptance

| Screen | Minimum information and states |
| --- | --- |
| Onboarding | Feature overview, local/cloud explanation, no premature permission demands |
| Chat | Source citations, response streaming, copy, edit, retry, stop, visible uncertainty |
| Research | Query, original source, published/retrieved timestamp, validation caveat |
| Knowledge | Picker-granted files, ingestion state, delete/index controls, per-user scope |
| Media | Mode, prompt, supported provider, spend/size limits, job progress, result gallery |
| Tasks | Plan preview, AUTO/ASK/DENY, status timeline, verified receipt, cancel |
| Provider hub | Provider capability, **verified** status, quota remaining and last test |
| Memory | View/modify approved preferences, delete conversation, export, revocation |
| Settings/Privacy | Mic/screen/overlay status, active grants, connected account revocation |
| Usage | Real measured calls/cost/errors; placeholders clearly labeled |

## Interaction contracts

- No false success messages; show actual receipt ID or meaningful failure.
- Loading, empty, permission denied, offline, rate limit and low credit screens are first-class states.
- Errors should say what happened, whether user data was saved, and what to do next.
- Confirmation must describe the action before any external write.
- Caption all speech/video output where supported; make voice tasks accessible without audio.

## Design review checklist

- [ ] WCAG color contrast verified, not assumed from palette
- [ ] Small screen/safe areas/keyboard/landscape reviewed
- [ ] Touch target and text scaling reviewed
- [ ] Reduced-motion and low-battery alternatives
- [ ] All app states visible, including unavailable providers
- [ ] No sensitive data exposed in public screenshots
- [ ] No fictitious metrics shown as real

**Implementation reminder:** The GitHub banner is documentation artwork; not proof of an implemented web or native UI.