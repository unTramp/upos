# Event Model Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Key decisions

- Event is immutable observation, not domain state.
- `event_id` is the idempotency/dedup identity.
- Corrected telemetry creates a new Event; old Event is not mutated.
- Event producer is separate from action initiator and semantic domain owner.
- Event envelope is a semantic superset with optional upstream references.
- `event_schema_version` + event/producer contract versions are sufficient for v1; no extra `event_type_version`.
- Namespaced Event type is occurrence-oriented, not command-oriented.
- Event Store need not provide exactly-once transport; idempotent at-least-once ingestion is sufficient semantically.
- Required missing Event can only be asserted against explicit capture expectation.

## Risk avoided

Without producer/initiator/domain-owner separation, adapter webhooks would falsely appear to be the organizational actor or owner.

Without capture expectation, telemetry silence would be misclassified as failure.
