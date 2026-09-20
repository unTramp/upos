# Routing Runtime Contract

**ID:** UPOS-04-ROUTING-RUNTIME  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-04  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents a Routing evaluation request, optional immutable Routing Decision reference, and technical outcome without implementing the routing algorithm.

## Required boundaries

- `operation_request_key` is technical correlation only;
- `operation_request_key != routing_decision_ref`;
- `operation_request_key != runtime_outcome.owner_result_ref`;
- technical failure may exist before a Routing Decision exists;
- consume exact versioned Phase-2 Task/Routing refs.

## Machine representation

- schema: `schemas/04/workflow/routing-runtime.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `04_workflow_engine/ROUTING_STANDARD.md`
- `04_workflow_engine/FAILURE_RETRY_RECOVERY.md`
- `runtime/RUNTIME_OPERATION_AND_IDEMPOTENCY_STANDARD.md`
