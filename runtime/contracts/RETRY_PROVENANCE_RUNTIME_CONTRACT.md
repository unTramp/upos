# Retry Provenance Runtime Contract

**ID:** UPOS-04-RETRY-PROVENANCE  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-04  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents the UPOS-04-owned `RETRY_OF` provenance relation between bounded Agent Run or Skill Invocation execution identities. It introduces no retry identity.

## Required boundaries

- predecessor and successor bounded identities are explicit;
- successor identity differs from predecessor identity for a full bounded-operation retry;
- trigger and orchestration attribution are retained;
- RETRY remains distinct from transport redelivery, REWORK and RECOVERY;
- nested technical retry does not automatically create a new parent Run/Invocation identity.

## Machine representation

- schema: `schemas/04/workflow/retry-provenance.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `04_workflow_engine/FAILURE_RETRY_RECOVERY.md`
- `runtime/RUNTIME_OPERATION_AND_IDEMPOTENCY_STANDARD.md`
- `runtime/RUNTIME_COMPATIBILITY_AND_VERSIONING.md`
