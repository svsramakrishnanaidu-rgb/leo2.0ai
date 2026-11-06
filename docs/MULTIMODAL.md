# Multimodal AI, voice and the floating companion

**Status:** proposed feature specifications, not deployed integrations.

## Text / voice experience

~~~text
Explicit tap / supported wake
 -> check mic permission and show capture indicator
 -> bounded recording and speech recognition
 -> normalize Telugu / English code-switching
 -> determine intent and policy
 -> generate / retrieve verified answer
 -> optional text-to-speech playback
 -> standby with microphone inactive
~~~

- Languages to test: Telugu, English, Hindi and Telugu-English mixed speech.
- Make it possible to use all major actions without speaking.
- Default to **push-to-talk**; no hidden recording or ambient listening.
- While LEO speaks, prevent its output from retriggering recognition. Enable barge-in only after audio feedback tests.
- Record WER/CER by language/device for ASR, response language adherence, streaming delays, and user corrections.
- Local speech model downloads require storage/compute prompts and license review.

## Floating companion

An orange orb can optionally overlay supported Android apps when users enable overlay permission. It is a **user interface**, not authority to access other apps' data. Keep it draggable, edge-snapping and one-hand usable. Explicit stop/mute/privacy controls must be accessible.

### State transitions

~~~text
STANDBY -> IDLE -> LISTENING -> THINKING -> SPEAKING -> STANDBY
                             \-> ACTING -> CONFIRM -> VERIFY -> IDLE
Any state --(Stop / revoke)--> STANDBY
~~~

## Image features

Planned modes: text-to-image, selected-image editing, result gallery, upscale where supported. Before sending private images to cloud providers, show where data goes and request explicit approval. Preserve original files; do not overwrite unless approved. Validate provider licensing, supported image dimensions and quota.

## Video work

Use long-running verified jobs rather than pretending video is generated synchronously.

~~~json
{
  "prompt": "An orange holographic LEO orb in a dark lab",
  "duration_seconds_requested": 8,
  "aspect_ratio": "16:9",
  "source_asset_id": null,
  "max_cost_usd": 0,
  "user_approved": false
}
~~~

This is a **contract example**, not an operational service. Display provider max duration, cost estimates, progress, cancellation, and exact produced file receipts. Long videos may need multiple short renders; a free API cannot be assumed to satisfy every duration.

## Screen explanation

Only after Android MediaProjection session consent: select app/window or screen, disclose cloud processing, show persistent capture indicator, sample minimally, and terminate capture and transient buffers when stopped. Do not capture or infer protected/DRM views.

## Release criteria

- [ ] Real provider-backed speech output tested on supported devices
- [ ] Code-mixed Telugu-English test evidence
- [ ] Voice stop/mute works without unintended re-listening
- [ ] Overlay never implies screen or contact access
- [ ] Screen capture always requires OS consent
- [ ] Media spend, retention and third-party rights documented
- [ ] Real user-accessible result assets and task receipts

[UI/UX specification](UI_UX.md) · [permissions](PERMISSIONS.md) · [testing](TEST_PLAN.md).