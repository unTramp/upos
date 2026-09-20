# Phase 2C Acceptance — Project Manifest & Project Adapter

**ID:** UPOS-SCHEMA-P2C-ACCEPT-001  
**Status:** PENDING FINAL CI  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20

## Machine contracts

- [x] Generic Binding schema.
- [x] Repository Binding schema.
- [x] Command Binding schema.
- [x] Project Manifest schema.
- [x] Project Adapter aggregate schema.
- [x] Canonical schema registry entries.
- [x] Composite Manifest/Adapter identity preserved.
- [x] Synthetic Manifest/Adapter IDs rejected.
- [x] Unsupported U-POS baseline rejected fail-closed.

## Validation

- [x] positive/negative Generic Binding fixtures.
- [x] positive/negative Repository Binding fixtures.
- [x] positive/negative Command Binding fixtures.
- [x] positive/negative Project Manifest fixtures.
- [x] unsupported-baseline Manifest fixture.
- [x] positive/negative Project Adapter fixtures.
- [x] cross-project Manifest/Adapter mismatch check.
- [x] binding/reference graph checks.

## Artist OS dogfooding

- [x] real Manifest candidate translated.
- [x] real Adapter candidate translated.
- [x] repository bindings represented.
- [x] path/environment bindings represented.
- [x] command bindings represented.
- [x] unresolved formal Provider Adapter preserved as unresolved.
- [x] production/security/quality/observability gaps are not fabricated.
- [x] expected INCOMPLETE / PARTIALLY_CONFIGURED state asserted.
- [x] pre-Phase-2A namespace drift recorded for project-side reconciliation.

## Ownership

~~~text
Project bindings / resolution / validation → UPOS-011
Project truth                           → UPOS-01 / project canonical owners
Context selection                       → UPOS-005
Engineering semantics                   → UPOS-006
Quality verdict                         → UPOS-007
Observability semantics                 → UPOS-008
Learning semantics                      → UPOS-009
Permission decision                     → UPOS-010
~~~

- [ ] final Baseline Integrity PASS on reconciliation HEAD.
- [ ] final Schema Validation PASS on reconciliation HEAD.

## Exit

Phase 2C is COMPLETE only after both final checks pass on the exact reconciliation HEAD.
