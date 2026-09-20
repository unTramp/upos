# Phase 2C — Artist OS Manifest / Adapter Dogfooding

**ID:** UPOS-SCHEMA-P2C-DOGFOOD-ARTISTOS-001  
**Status:** CANDIDATE / EXPECTED INCOMPLETE CONFIGURATION  
**Date:** 2026-09-20  
**Artist OS branch:** feat/upos-adoption  
**Artist OS head inspected:** d8f5a4295952ec9f462649c366e451e7188fefd8

## Question

Can UPOS-011 machine contracts represent the real Artist OS adoption candidates without inventing production/provider/security/quality bindings?

## Expected result

~~~text
Project Manifest        → representable
Project Adapter         → representable
Repository bindings     → representable; formal Provider Adapter unresolved
Path bindings           → representable
Local/CI environments   → representable
Command bindings        → representable; formal runtime/provider binding unresolved
Production              → unresolved, not fabricated
Quality semantics       → unbound, not fabricated
Security permissions    → unbound, not fabricated
Observability           → unbound, not fabricated
Agent/workflow/skills   → unbound, not fabricated
~~~

Expected adapter state:

~~~text
validation_state = INCOMPLETE
configuration_completeness = PARTIALLY_CONFIGURED
~~~

This is correct fail-closed representation, not a failure.

## Provider Adapter rule

Artist OS identifies GitHub as provider, but no formal U-POS Provider Adapter identity/version is frozen for the project.

The machine instance therefore uses `UNRESOLVED` rather than inventing `github@1.0`.

## Namespace adoption drift

The human-readable Artist OS `.upos/PROJECT_ADAPTER.md` contains pre-Phase-2A conceptual labels such as `upos.execution.AgentRun` and `upos.execution.ContextBundle`.

The Core schema layer does not mutate Artist OS documents. Its machine instance uses owner-qualified namespaces from Phase 2A and records the human-document mismatch as project-side adoption drift.

## Ownership boundary

~~~text
Manifest/Adapter bindings → UPOS-011
Project truth             → Artist OS canonical sources / UPOS-01
Context selection         → UPOS-005
Quality verdict           → UPOS-007
Permission decision       → UPOS-010
Provider capability       → Provider Adapter only
~~~
