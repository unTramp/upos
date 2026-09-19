# Finding Severity Analysis

**ID:** UPOS-07-AN-007  
**Type:** ANALYSIS / FINDING SEVERITY  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-007 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 07 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-007 v1.0 decomposition/implementation/audit state at freeze time. It is not timeless normative truth. Current Quality semantics are owned by canonical Module 07 normative artifacts; `MODULE_07_TRACEABILITY.md` remains the canonical coverage artifact.


## Frozen source

Frozen master proposes:

```text
BLOCKING
MAJOR
MINOR
NIT
```

## v1 normalization

Accepted:

```text
BLOCKING
MAJOR
MINOR
ADVISORY
```

`NIT` becomes `ADVISORY` because universal Quality semantics should describe consequence rather than code-review slang.

## Separation

```text
severity != confidence
severity != status
severity != verdict
```

No numeric score is canonical.
