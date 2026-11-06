# Navigation map for the uploaded 311-page engineering master

This is a **reference locator**, not a verbatim copy or an assertion that attached source files are committed to GitHub.

| Source PDF pages | Main content | Repository counterpart |
| --- | --- | --- |
| 1–3 | Publication cover, evidence legend, source register | [SOURCES.md](SOURCES.md) |
| 4–5 | Product vision, success criteria, trust boundaries | [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| 6–9 | Agent policy, API resource atlas and provider selection | [PERMISSIONS.md](PERMISSIONS.md), [PROVIDERS.md](PROVIDERS.md) |
| 10–12 | Android capabilities, overlay, screen-sharing and UI states | [PERMISSIONS.md](PERMISSIONS.md), [UI_UX.md](UI_UX.md) |
| 13–14 | Knowledge/RAG/memory and voice/media | [DATA.md](DATA.md), [MULTIMODAL.md](MULTIMODAL.md) |
| 15–18 | Visual design language and screen specification | [UI_UX.md](UI_UX.md) |
| 19–20 | Data model and backend interfaces | [DATA.md](DATA.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| 21–23 | Reliability, security and compliance | [SECURITY.md](../SECURITY.md), [TEST_PLAN.md](TEST_PLAN.md) |
| 24–26 | Delivery plan, T01–T20 acceptance tests, release gates | [ROADMAP.md](ROADMAP.md), [TEST_PLAN.md](TEST_PLAN.md) |
| 27–29 | Copy-ready instruction and source reference links | [Development prompt](../prompts/LEO_2_BUILD_INSTRUCTION.md), [SOURCES.md](SOURCES.md) |
| 30–43 | Original 16-phase master instruction | [Product requirements](PRODUCT_REQUIREMENTS.md), [Roadmap](ROADMAP.md), [Prompt](../prompts/LEO_2_BUILD_INSTRUCTION.md) |
| 44–311 | Embedded research reports and extensive appendices | Source-reference overview only, not full replicated appendices |

## Embedded source package caveats

The PDF has eight embedded resources including two ZIP research packages, three referenced design JPGs, one dashboard PNG, a text prompt and a JSON manifest. These are **source evidence**, not working model weights or deployed software. The GitHub connector used for these commits can publish authored text, but the original PDF/DOCX/ZIP and third-party visual binaries have **not** been uploaded.

## Original build guide

The separate Word document supplies illustrative FastAPI, Kotlin/Compose and backend examples, testing ideas, tools and budgets. That code was not copied verbatim into production modules because API models, dependencies, costs and security assumptions need independent review.

## How to turn an entry into a shipped feature

1. Find source claim and version.
2. Confirm license/current official policy.
3. Write contract and unit tests.
4. Integrate with owner-issued credentials and valid permission.
5. Execute tests; attach logs and receipts.
6. Update the status only when verified.

[Return to source register](SOURCES.md).