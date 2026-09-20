# Phase 2 — Schema Stability Decision

**ID:** UPOS-SCHEMA-P2-STABILITY-001  
**Status:** APPROVED FOR PROMOTION  
**Date:** 2026-09-20  
**Baseline:** U-POS v1.0.0  
**Decision HEAD:** `6a92be5e7534e8ada23ec65647bd1a5967905f7f`

## Gate

A family is eligible only with frozen semantic source, schema representation, registry entry, positive fixture, negative fixture where appropriate, validator coverage, cross-reference validation, traceability, reconciliation, independent audit and P0/P1=0.

## Decisions

| Family | Decision | Evidence basis |
|---|---|---|
| upos.common.schema_registry | STABLE | governance + meta-schema + positive/negative registry fixtures + owner/URI/dependency checks |
| UPOS-01 Documentation schemas | STABLE | frozen UPOS-01 sources + Phase 2B fixtures + semantic ambiguity checks + Artist OS dogfooding |
| UPOS-11 Binding/Command/Manifest/Adapter | STABLE | frozen UPOS-11 standards + structural/semantic fixtures + Phase 2C dogfooding |
| UPOS-11 Repository/Path/Environment | STABLE | owner standards + Project Adapter / Artist OS instance coverage + semantic reference checks |
| UPOS-11 Identity/Resource/Secret/Capability/Provider Adapter | STABLE | owner standards + direct positive/negative branch fixtures added after independent audit |
| UPOS-02 identity references | STABLE | owner sources + owner fixtures |
| UPOS-03 identity references | STABLE | versioned Skill semantics + fixtures |
| UPOS-04 identity references | STABLE | frozen Workflow identities + negative anti-generic-workflow fixture |
| UPOS-05 identity references | STABLE | Context identities + Context View anti-identity fixture |
| UPOS-06 identity references | STABLE | Engineering identities + native reference boundary fixture |
| UPOS-07 identity references | STABLE | Quality identities + no Quality Readiness ID fixture |
| UPOS-08 identity references | STABLE | Observability identities + no Metric Observation ID fixture |
| UPOS-09 identity references | STABLE | six adopted identities + rejected embedded/projection checks |
| UPOS-10 identity references | STABLE | Security identities + versioned policy negative fixture |
| UPOS-11 Adapter Resolution reference | STABLE | frozen adapter_resolution_id + positive/negative fixture |
| cross-module conformance harness | STABLE | infrastructure-only exact-URN positive/negative imported-constraint proof |

## Open P2

AUD-P2-001 remains non-blocking hardening for future provider/native schema evolution. Current schema corpus has no lexical collision requiring an exception, owner semantics remain authoritative, and no current schema is invalidated.

## Decision

All 27 registered Phase-2 schema entries are approved for CANDIDATE → STABLE.

Promotion must be a separate registry-only commit and must pass exact-HEAD Baseline Integrity and Schema Validation before Phase-2 exit acceptance.
