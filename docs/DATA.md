# LEO 2.0 data, memory and retrieval design

**Status:** schema and ingestion proposal; no database has been provisioned by these documents.

## Data boundaries

Separate (1) session working memory, (2) conversation records, (3) user-approved preferences, (4) selected-file knowledge, (5) workflow receipts and (6) evaluated reusable procedures. These have **different retention and deletion rules** and are not automatically model training data.

## Proposed entities

| Table | Key fields | Required privacy control |
| --- | --- | --- |
| users | id, created_at, settings_version | Authenticated owner |
| conversations | id, owner_id, title, retention_until | Owner access / export / delete |
| messages | id, conversation_id, role, content_ref, created_at | Conversation owner ACL |
| consent_grants | id, actor_id, capability, scope, expires_at, revoked_at | Revocation effective before tool use |
| document_sources | id, owner_id, source_hash, filename, consent_id, indexed_at | Source deletion + owner ACL |
| document_chunks | id, source_id, offsets, content_ref, embedding_ref | Retrieval only after owner filter |
| tasks | id, owner_id, intent, state, idempotency_key, max_calls | Per-user query isolation |
| task_events | id, task_id, status, sanitized_details, timestamp | Minimize sensitive log content |
| provider_catalog | provider_id, capability, auth_type, license, test_state | No raw keys |
| provider_usage | id, owner_id, request_id, tokens, estimated_cost | Redacted ledgers |
| media_assets | id, owner_id, mode, content_ref, expires_at | Signed access + purge |

A real schema migration must be reviewed for the chosen database and deployed in staging before marking this implemented.

## Memory and knowledge pipeline

~~~mermaid
flowchart LR
  A[User selects file] --> B[Validate size/MIME + consent]
  B --> C[Parse and preserve provenance]
  C --> D[Chunk + deduplicate]
  D --> E[Index under owner ACL]
  E --> F[Owner-filtered retrieval]
  F --> G[Cited answer]
  H[Delete / revoke grant] --> I[Delete chunks, embeddings, caches]
~~~

## Retrieval guarantees

- Authenticate every request; derive user identity from session, not request body.
- Filter by owner and valid grant **before** vector or lexical ranking.
- Store original source URL/file ID, hash, chunk offsets, parser version, language and indexed_at.
- Cite exact retrieved passages; mark unsupported answers as uncertain.
- Never execute an instruction embedded in an uploaded PDF.
- Deleting a source revokes derived vectors, caches, generated links and access grants.

## Sensitive data policy

- Local-first for selected phone data when feasible.
- Cloud upload requires purpose and transfer disclosure.
- Do not silently index all device storage, contacts, photos or chats.
- Encrypt sensitive device and server storage appropriately; restrict backup/restore.
- Privacy/export/delete UI must match real backend behavior.
- Retention periods must be specified before launch and tested end-to-end.

## Schema/quality tests to implement

1. User A cannot fetch or search User B's document or task, including guessed UUIDs.
2. Revoke a grant and verify the next tool call is denied.
3. Delete document and prove chunks, embeddings and caches are purged.
4. Failed upload does not leave visible partial data or orphaned storage.
5. Restore backup without resurrecting previously deleted accounts.
6. Prompt injection inside document remains inert.

For a first MVP, basic text search may be sufficient. Add vector embeddings only if evaluated retrieval quality improves enough to justify data flow and cost.