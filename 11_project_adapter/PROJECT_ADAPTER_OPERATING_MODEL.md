# Project Adapter Operating Model

**ID:** UPOS-11-PAOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## 1. Mission

UPOS-011 converts abstract U-POS requirements into explicit concrete bindings without changing their meaning.

```text
abstract requirement
→ project scope
→ binding resolution
→ provider/runtime implementation
→ validated resolved binding
```

## 2. Hard invariants

```text
PROJECT ADAPTER != PROJECT SOURCE OF TRUTH
PROJECT ADAPTER != WORKFLOW ENGINE
PROJECT ADAPTER != SECURITY POLICY
PROJECT ADAPTER != QUALITY POLICY
PROJECT ADAPTER != CONTEXT POLICY
PROJECT ADAPTER != PROVIDER BUSINESS LOGIC

PROVIDER CAPABILITY != ORGANIZATIONAL AUTHORITY
PROVIDER SCOPE != U-POS PERMISSION
TEST COMMAND != QUALITY CRITERION
TELEMETRY BACKEND != EVENT SEMANTICS
MANIFEST VALUE != CANONICAL PROJECT FACT unless backed by canonical_policy_ref/source_ref
```

## 3. Ownership

UPOS-011 owns concrete resolution, implementation bindings, provider adapter contracts, validation, compatibility, drift and binding health.

It consumes semantics from Modules 01–10 and MUST NOT reinterpret them.

## 4. Bootstrap

```text
load U-POS baseline
→ load Project Manifest
→ schema/static validation
→ resolve provider adapters
→ resolve required bindings
→ validate capabilities/resources
→ validate security-sensitive bindings
→ runtime validation where required
→ build immutable Resolved Adapter View
→ expose project-configured interfaces
```

Failure to complete a REQUIRED binding means the affected capability is unavailable. It does not authorize fallback by convenience.

## 5. Configuration layers

The normative precedence model is:

```text
U-POS non-semantic defaults
< organization adapter defaults
< project manifest
< environment-scoped binding
< execution-scoped override
```

A lower-level override MAY refine a configurable value but MUST NOT violate any upstream invariant or policy.

## 6. Fail-closed boundaries

Security-sensitive unresolved binding:

```text
→ no semantic permission inferred
→ report binding failure to UPOS-010 / UPOS-004 interface
```

Canonical source unresolved:

```text
→ no lower-authority source substitution
→ report source binding failure to UPOS-01 / UPOS-005 interface
```

## 7. Historical reproducibility

Every material execution SHOULD remain attributable to:

```text
project_id
project_manifest_version
project_adapter_version
binding refs used
provider_adapter_ref/version
```

Historical runs are not silently reinterpreted under newer bindings.

## 8. Out of scope

Runtime engine, event pipeline, dashboard UI, database schemas, CLI/installer, real provider integrations, deployment platform and code generation remain later implementation phases.
