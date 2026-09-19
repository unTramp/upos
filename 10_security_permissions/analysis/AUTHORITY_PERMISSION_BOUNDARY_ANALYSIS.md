# Authority vs Permission Boundary Analysis

**ID:** UPOS-10-AN-APB-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Core decision

```text
ORGANIZATIONAL AUTHORITY != TECHNICAL PERMISSION
```

UPOS-002 answers whether a Role/Human/Agent is authorized organizationally to decide/act in scope.

UPOS-010 answers whether the concrete protected use is security-permitted now.

A technical provider credential or Grant cannot create organizational authority.

A Role's organizational authority cannot bypass a technical Security DENY.

## Merge example

```text
Merge Controller authority                     → UPOS-002
mechanically mergeable repository state        → UPOS-006
Quality readiness                              → UPOS-007
permission to execute protected merge now      → UPOS-010
provider branch-protection/IAM mapping          → UPOS-011
```

## Human approval

Human approval is an external organizational decision ref. UPOS-010 may require it as a condition but does not own who may approve.
