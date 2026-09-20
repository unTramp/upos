# Phase 2C Reconciliation — Project Manifest & Project Adapter

**ID:** UPOS-SCHEMA-P2C-REC-001  
**Status:** RESOLVED — PENDING FINAL CI  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20

## Scope

Narrow reconciliation of the Phase 2C machine-readable UPOS-011 contracts against the frozen Project Adapter module and the real Artist OS adoption candidates.

Frozen UPOS-011 files were not modified.

## Resolved findings

### P1-01 — Manifest baseline compatibility was not fail-closed

The initial candidate schema accepted any non-empty `upos_baseline.version`.

That contradicted the schema registry binding to U-POS v1.0.0 and UPOS-011's requirement to reject incompatible baselines rather than silently reinterpret them.

Resolution:

~~~text
project-manifest.schema.json@0.1.0
→ upos_baseline.version = v1.0.0
~~~

A dedicated unsupported-baseline negative fixture was added.

### P1-02 — Artist OS dogfood pointed canonical_project_source_ref at an audit overlay

The first machine translation used `.upos/SOURCE_OF_TRUTH_MAP.md`.

That file is an adoption/audit authority overlay and is not yet itself Artist OS canonical product truth.

Resolution:

~~~text
canonical_project_source_ref
→ docs/artist-os/00_governance/MASTER_ARCHITECTURE_v1.4.md

authority_overlay_ref
→ .upos/SOURCE_OF_TRUTH_MAP.md
~~~

The latter remains project extension metadata, not Product Source of Truth.

### P2-01 — Dogfooding reference graph validation was incomplete

Initial checks resolved Manifest refs but did not fully verify:

- duplicate binding identities;
- repository → path binding refs;
- Command Binding → repository refs;
- Command Binding → environment binding refs.

Resolution: all are now checked by the dogfooding validator.

### P2-02 — Artist OS human adapter namespace labels predate Phase 2A

The project candidate still uses conceptual examples such as `upos.execution.AgentRun`.

Phase 2A now defines owner-qualified schema namespaces.

Resolution in U-POS Core:

- machine dogfooding instance uses the current owner-qualified convention;
- no project file is silently rewritten;
- project-side adoption drift remains explicit until Artist OS reviews/finalizes its Manifest/Adapter.

### P2-03 — Formal Provider Adapter identity/version is unresolved

Artist OS knows GitHub as provider, but no project U-POS Provider Adapter identity/version has been frozen.

Resolution:

~~~text
provider_adapter_ref = UNRESOLVED
provider_adapter_version = UNRESOLVED
validation_state = INCOMPLETE
configuration_completeness = PARTIALLY_CONFIGURED
~~~

No fictitious `github@1.0` was introduced.

## Contract boundaries preserved

~~~text
Manifest != Project Knowledge
Binding != Policy
Capability != Permission
CI result != Quality Verdict
Provider Adapter != Domain Owner
Resolved Adapter View != Source of Truth
~~~

## Identity reconciliation

~~~text
Project Manifest = project_id + manifest_version
Project Adapter  = project_id + project_adapter_version

project_manifest_id: NOT INTRODUCED
project_adapter_id:  NOT INTRODUCED
~~~

## Secret boundary

Core Manifest/Binding schemas expose references only; they contain no raw-secret value field.

Opaque project extensions remain subject to the frozen invariant that raw secret values are forbidden and to project/security scanning. Phase 2C does not weaken that invariant or claim that JSON Schema can identify arbitrary secret material by value.

## Current unresolved findings

~~~text
P0: 0
P1: 0
P2: 0
~~~

Status:

~~~text
READY FOR FINAL CI REVALIDATION
~~~
