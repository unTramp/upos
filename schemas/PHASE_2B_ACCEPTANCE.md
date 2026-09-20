# Phase 2B Acceptance — Documentation Authority

**ID:** UPOS-SCHEMA-P2B-ACCEPT-001  
**Status:** PENDING FINAL CI  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20

## Required contracts

- [x] Document Manifest normalized from frozen UPOS-01 schema.
- [x] Source-of-Truth Entry represented without synthetic entry identity.
- [x] Source-of-Truth Registry operational profile defined.
- [x] Registry composes canonical versioned schema references.
- [x] Document status/normativity/lifetime vocabularies preserved.
- [x] ACTIVE authority requires authority-bearing normativity.
- [x] Structural authority ambiguity checks implemented.
- [x] SOT-C4 semantic conflict is not auto-resolved by schema validation.

## Verification

- [x] positive/negative Document Manifest fixtures.
- [x] positive/negative Source-of-Truth Entry fixtures.
- [x] duplicate authority negative fixture.
- [x] multiple ACTIVE owner ambiguity negative fixture.
- [x] ACTIVE informative authority negative fixture.
- [x] cross-schema offline reference resolution.
- [x] real Artist OS Document Manifest dogfooding instance.
- [x] real Artist OS Source-of-Truth Registry dogfooding instance.
- [x] Artist OS expected multi-source warning asserted by CI.
- [ ] final Baseline Integrity PASS on reconciliation HEAD.
- [ ] final Schema Validation PASS on reconciliation HEAD.

## Ownership

~~~text
Document authority semantics        → UPOS-01
Machine-readable representation     → schemas/
Project/provider/path binding       → UPOS-011 where applicable
Runtime context selection           → UPOS-005
~~~

No ownership has moved.

## Exit

Phase 2B is COMPLETE only after the two final CI checks above pass on the exact reconciliation HEAD.
