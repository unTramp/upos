# Phase 2B Acceptance — Documentation Authority

**ID:** UPOS-SCHEMA-P2B-ACCEPT-001  
**Status:** COMPLETE  
**Baseline:** U-POS v1.0.0  
**Completed:** 2026-09-20

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
- [x] Baseline Integrity PASS after reconciliation fixes.
- [x] Schema Validation PASS after reconciliation fixes.

## Final CI evidence before close

Exact verified implementation HEAD:

~~~text
0aa30c3f27d718f02f292639990b0da5a3d994a9
~~~

Results:

~~~text
Baseline Integrity   PASS
Schema Validation   PASS
~~~

The validator also caught two fixture/tooling regressions during reconciliation before merge:

~~~text
stale negative fixtures missing required normativity
missing path constant for the new ACTIVE-INFORMATIVE fixture
~~~

Both were fixed without weakening the authority contract.

## Ownership

~~~text
Document authority semantics        → UPOS-01
Machine-readable representation     → schemas/
Project/provider/path binding       → UPOS-011 where applicable
Runtime context selection           → UPOS-005
~~~

No ownership moved.

## Exit decision

~~~text
PHASE 2B
Documentation Authority
COMPLETE
~~~

Candidate schemas remain versioned machine-readable representations of U-POS v1.0.0. Completion of Phase 2B does not rewrite frozen UPOS-01 semantics.
