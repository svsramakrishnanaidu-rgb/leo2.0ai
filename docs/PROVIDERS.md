# API provider and resource strategy

**Status:** proposal, not proof of connected accounts or working AI API keys.

## Important correction

The supplied 2026 resource research reports **2,310 directory rows, 2,302 normalized documentation targets, 57 curated records and 19/20 tested public endpoint examples**. These are **documentation/resource research findings**. They are not 2,302 privately owned API credentials and do not establish that every endpoint still works.

Do not attempt to collect leaked keys or test credentials belonging to others. Get legitimate owner-issued keys and use official OAuth for user-connected services.

## Capability-first adapters

| Capability | Candidate technologies named in supplied sources | Activation status |
| --- | --- | --- |
| Chat / reasoning | Groq, Gemini, OpenRouter, Cloudflare Workers AI | Unverified / owner setup required |
| Current research | Tavily, Brave, vetted official sources | Unverified |
| Web public data | Open-Meteo, Wikipedia, Crossref, OpenAlex, USGS, World Bank, Open Food Facts, GBIF | Endpoint/usage rules need check |
| Speech recognition | Deepgram, Handy/faster-whisper or other approved STT | Evaluation pending |
| Speech synthesis | OmniVoice, Piper or licensed TTS provider | Evaluation pending |
| Vision | Model with verified vision capability, Android ML Kit | Evaluation pending |
| Media images/videos | Verified capability-matched paid/free provider | Not implemented |
| Retrieval embeddings | pgvector + chosen legal embedding model | Not implemented |
| Optional avatar | Duix-Avatar with license review | Research only |

## Provider record schema

~~~json
{
  "provider_id": "official-provider-slug",
  "capability": "chat|vision|speech_in|speech_out|image|video|search",
  "docs_url": "https://example.org/official-documentation",
  "auth_type": "server_secret|oauth|none",
  "secret_ref": null,
  "license": "review_pending",
  "supported_languages": [],
  "quota_policy": {"status": "unknown"},
  "max_cost_usd_per_task": 0,
  "last_tested_at": null,
  "test_evidence": null,
  "status": "unverified"
}
~~~

Example keys are placeholders only. Never commit credentials or token-bearing request logs.

## Registry selection

1. Match requested capability and language.
2. Reject missing license/authorization/consent/quota.
3. For private data, prefer permitted local providers or ask for explicit cloud processing consent.
4. Rank eligible providers by **measured** quality, availability, latency and cost.
5. Send a schema-validated bounded request; enforce timeout, budget and rate limit.
6. Save sanitized HTTP status, provider response ID and test timestamp; never log credentials.
7. Fallback only when user consent and privacy constraints are preserved.
8. On provider outage, present **unknown/error**, not an invented answer.

## Qualification checklist

- [ ] Official documentation and license confirmed
- [ ] Own account/OAuth granted
- [ ] Key stored server-side in a secret manager
- [ ] Allowed request/response schemas validated
- [ ] Test result and timestamp recorded
- [ ] Quota/rate limits and costs verified
- [ ] PII handling reviewed
- [ ] Tool/API marked enabled only after successful controlled test

## Public knowledge and third-party code

Imported pages, external instructions and security-skills repositories are untrusted **data** for retrieval. Respect licenses/attribution and never auto-run external code or elevate source text into system policy.

## First-provider strategy

Start with **one** chat provider and a simple local fallback; prove authenticated streaming and cost caps. Add a second provider only after failure-state and security tests pass. Do not optimize for raw provider count.

[Architecture](ARCHITECTURE.md) · [Source caveats](SOURCES.md) · [Test plan](TEST_PLAN.md).