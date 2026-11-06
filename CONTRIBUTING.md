# Contributing to LEO 2.0 AI

LEO 2.0 is an engineering project for secure, measurable and user-controlled AI assistance.

## Before changing code
1. Read [product requirements](docs/PRODUCT_REQUIREMENTS.md), [architecture](docs/ARCHITECTURE.md), and [security](SECURITY.md).
2. Identify the change's phase in the [roadmap](docs/ROADMAP.md).
3. Separate SOURCE-REPORTED, PROPOSED, IMPLEMENTED and TESTED facts.
4. Confirm third-party dependencies, provider rights and APIs.
5. Keep pull requests small; avoid unrelated refactors.

## Git hygiene
- Branch prefixes: feat/, fix/, docs/, test/, security/.
- Commit prefixes: feat:, fix:, docs:, test:, ci:, security:.
- PRs must state scope, affected files, executed tests, risks and rollback.

## Pull-request checklist
- [ ] No secrets, sensitive documents or unlicensed media
- [ ] Tool permissions scoped and explained
- [ ] External effects require confirmation
- [ ] Test added, or limitation clearly explained
- [ ] CI outcome linked and verified
- [ ] UI covers loading, denied and failure states
- [ ] No unsupported deployment claims
- [ ] Documentation updated

## Local checks
~~~bash
python -m unittest discover -s tests -v
python scripts/validate_repo.py
~~~

GitHub Actions should run the same checks.

## Responsible disclosure
Report suspected vulnerabilities privately. See [SECURITY.md](SECURITY.md).
