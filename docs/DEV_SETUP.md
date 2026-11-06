# Developer setup — LEO 2.0

**This repository currently contains a specification, reference policy module and repo tests.** It is NOT a functioning web dashboard, Android client or hosted AI server.

## Requirements for current files

- Git, Python 3.11+ for reference code and unit checks.
- No API keys and no external Python dependencies are needed for the existing checks.

~~~bash
git clone https://github.com/svsramakrishnanaidu-rgb/leo2.0ai.git
cd leo2.0ai
python scripts/validate_repo.py
python -m unittest discover -s tests -v
~~~

The checks validate repository links and example consent logic only. They do not measure AI response quality or mobile compliance.

## Recommended future implementation stack

| Layer | Candidate | State |
| --- | --- | --- |
| Web | React/TypeScript, responsive design system | Not implemented |
| Android | Kotlin + Jetpack Compose | Not implemented |
| API | Python/FastAPI, authenticated gateway | Not implemented |
| Data | PostgreSQL, per-user ACL / RLS | Not implemented |
| Retrieval | Full text first, optional pgvector | Not implemented |
| AI | One verified owner-authorized provider via backend | Not connected |
| Observability | Sanitized traces, error capture, usage ledger | Not implemented |

## Environment design (for future backend)

When a secure backend is created, define its secrets in the hosting platform or local git-ignored environment file. Example **names only**:

~~~dotenv
# SERVER SIDE ONLY — placeholders, never commit live values
DATABASE_URL=replace-with-server-owned-database-url
AI_PROVIDER_API_KEY=replace-with-owner-issued-secret
ALLOWED_ORIGINS=https://your-verified-frontend.example
LOG_LEVEL=INFO
~~~

Do not embed secret values in browser VITE_ variables, APK assets or GitHub Actions logs. Set the real environment schema when backend code exists.

## Work sequence

1. Confirm service boundaries and threat model.
2. Implement authentication and migrations.
3. Add one provider adapter behind a secure authenticated gateway.
4. Test failure, quotas and streaming.
5. Build a mobile-first front end with real states.
6. Add selected file indexing with owner-filtered citations.
7. Test native capabilities on real Android hardware.

Consult [Roadmap](ROADMAP.md), [Architecture](ARCHITECTURE.md), [Security](../SECURITY.md), and [Source register](SOURCES.md).

## CI

GitHub's **Repository quality** workflow should run on pushes and PRs. Green means the executed repository validation and policy unit tests passed. It does not mean the planned product is deployed or production-ready.
