# Source register and evidence policy

**Reviewed:** 2026-11-06. **Purpose:** map uploaded material to actionable LEO 2.0 documentation without inventing a running app or disclosing secrets.

## Directly supplied sources

| ID | User-provided file | Role | SHA-256 |
| --- | --- | --- | --- |
| S1 | LEO_2_0_COMPLETE_MASTER_BUILD_BLUEPRINT_2026(3).pdf | 311-page integrated engineering specification, appendices and references | b1694a5fb0b2c65181a8c2cdc305d76c728ad808a9ef651b2913c9b54446f2ef |
| S2 | details full.docx | Earlier full build guide: tools, rough code examples, Android/backend plan and tests | 2c4adcee9c0027e45ba8853c2c7bd97e784d275835396e52b6fa2d5df9b376ad |
| S3 | LEO_2_0_COPY_READY_BUILD_PROMPT (1).txt | Concise engineering instruction and implementation order | 2f68887b036e60e30bd3e70ba2a95ab5d95b414ca4ebf1a4b0d7a3f3e4281179 |
| S4 | image(20261106-135020).png | GitHub profile screenshot showing target repo; NOT proof of LEO app functionality | Not required for software requirements |

### PDF organization

Pages **1–29**: integrated master guide covering sources, vision, architecture, policy, APIs, Android, floating orb, screen context, memory, voice/media, UI, data and acceptance gates.

Pages **30–43**: source-provided master instruction with 16 implementation phases.

Pages **44–311**: bundled appendix/reference reports, including API-resource research and autonomous AI architecture. The PDF also contains **eight embedded files**, among them ZIP catalogs, original instruction text, a source manifest and design references. Their presence does not establish deployable models, licensed redistribution, test coverage or working credentials.

### Transformed output in this repository

| Sources | Derived GitHub artifacts | Evidence class |
| --- | --- | --- |
| S1 + S3 | PRODUCT_REQUIREMENTS.md, ROADMAP.md | Specification / proposed |
| S1 | ARCHITECTURE.md, DATA.md, PROVIDERS.md | Architecture / contracts proposed |
| S1 + S2 | PERMISSIONS.md, MULTIMODAL.md, UI_UX.md | Policy-oriented design proposal |
| S1 + S3 | TEST_PLAN.md, WORKFLOWS.md | Acceptance specification |
| S1 + S2 + S3 | prompts/LEO_2_BUILD_INSTRUCTION.md | Adapted task instruction |
| S4 | Repo/project identification only | Screenshot evidence |

## Evidence vocabulary

- **SOURCE-REPORTED:** documented in uploaded material; NOT rerun against the current app.
- **PROPOSED:** requirements, architecture, schema or configuration intended for implementation.
- **TEST PENDING:** can only be accepted after a controlled run produces logs/receipts.
- **VERIFIED IN THIS REPOSITORY:** only for files and GitHub Actions results actually created/executed here.
- **UNAVAILABLE/RESTRICTED:** unsupported by current connector, OS or consent state.

## Resource catalog and credential caution

The master PDF describes **2,310 public directory rows -> 2,302 normalized API documentation targets**, **57 curated integration records**, **19 of 20 source-reported public endpoint examples passing**, **818 community security-skill descriptions**, and **76 model metadata entries**. Those numbers are **research inventory counts, not 2,302 working API keys, 818 safe agents, or verified LEO 2.0 integrations**.

- Do not publish tokens, harvested credentials, full private file content or user-specific sensitive data.
- Do not automatically execute third-party community scripts or imported PDF instructions.
- A model or service can be enabled only with a legitimate owner-issued credential, terms/license review, and successful current test.
- All usage limits and provider models require fresh validation.

## Raw-source publishing status

The original PDF, DOCX, embedded ZIPs and referenced third-party images were **not uploaded to GitHub** during this change. This repository contains **newly authored, source-informed Markdown and project files**, not a verbatim redistribution of the complete 311-page publication. This avoids accidental secrets exposure and unreviewed redistribution of third-party content.

## Source correction priority

When references disagree, preserve the difference in a decision log. Treat old pricing, usage quotas, product policies and timelines as time-sensitive and unverified. For implementation acceptance, rely on current controlled tests, not only document text.