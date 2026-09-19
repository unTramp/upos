# Project Extension Standard

**ID:** UPOS-11-EXT-001  
**Type:** EXTENSION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Purpose

Allow project/company-specific configuration without polluting the universal namespace.

## Namespace

```text
extensions.<namespace>
```

The namespace owner defines its schema.

## Prohibited extension behavior

Extensions MUST NOT redefine:

```text
core U-POS invariants
canonical owner semantics
permission meaning
Quality Verdict meaning
Workflow transition meaning
Context truth boundaries
Observability truth boundaries
Learning promotion semantics
```

## Unknown extensions

Runtime/schema policy MUST explicitly choose:

```text
PRESERVE
IGNORE_IF_SAFE
REJECT
```

Unknown extension data is never silently reinterpreted as a canonical field.
