# Event Emission Interface

**ID:** UPOS-08-EVENT-EMISSION  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-08  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Defines the Slice-1 Event representation/emission boundary. Event meaning, identity and correction/redelivery semantics remain UPOS-08-owned.

## Required boundaries

- same logical Event redelivery reuses `event_id`;
- correction uses a new `event_id` plus explicit correction relation;
- Trace/Span references may be carried when available;
- Event Store, trace propagation and span runtime are not implemented in Phase 3.

## Machine representation

- schema: `schemas/08/observability/event.schema.json`
- interface contract version: `0.1.0`
- frozen Event contract: `UPOS-08-EVT-001@1.0.0`

## Normative sources

- `08_observability/EVENT_STANDARD.md`
- `08_observability/OBSERVABILITY_LIFECYCLE_AND_VERSIONING.md`
