# Learning Lifecycle and Versioning

**ID:** UPOS-09-LLV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Separate lifecycles

Module 09 distinguishes:

```text
Pattern Candidate lifecycle
Learning Candidate lifecycle
Root Cause Assessment lifecycle
Improvement Proposal lifecycle
Validation Plan lifecycle
Learning Outcome lifecycle
target artifact lifecycle (owned elsewhere)
canonical knowledge lifecycle (UPOS-01)
```

Do not collapse them.

## 2. Immutability / append-only history

Completed Assessments/Outcomes preserve historical conclusions as-of their evaluation time.

Lifecycle status changes SHOULD preserve append-only history where the object evolves.

Substantive replacement uses supersession/new identity rather than silent rewriting when historical audit would otherwise be lost.

## 3. Pattern Candidate lifecycle

```text
OPEN
INVESTIGATING
CONFIRMED
NOT_CONFIRMED
DUPLICATE
CONSOLIDATED
SUPERSEDED
ARCHIVED
```

## 4. Learning Candidate lifecycle

```text
OPEN
TRIAGED
INVESTIGATING
VALIDATED
REJECTED
PROMOTED_TO_PROPOSAL
DUPLICATE
CONSOLIDATED
SUPERSEDED
ARCHIVED
```

## 5. Root Cause Assessment lifecycle

```text
OPEN
ASSESSING
COMPLETED
INCONCLUSIVE
SUPERSEDED
```

## 6. Improvement Proposal lifecycle

```text
DRAFT
OWNER_RESOLUTION_PENDING
VALIDATION_PLANNED
VALIDATING
READY_FOR_OWNER_REVIEW
HANDED_OFF_TO_OWNER
CLOSED
REJECTED
WITHDRAWN
SUPERSEDED
```

No state named `APPROVED_CHANGE` exists because owner approval/change lives externally.

## 7. Validation Plan lifecycle

```text
DRAFT
READY
ACTIVE
COMPLETED
INVALIDATED
SUPERSEDED
```

## 8. Learning Outcome lifecycle

```text
DRAFT
ASSESSING
COMPLETED
SUPERSEDED
```

The outcome classification (`IMPROVED`, etc.) is separate from lifecycle state.

## 9. Module/version evolution

Material semantic changes to Learning System standards require reviewed versioning under UPOS-01 documentation governance.

UPOS-009 v1.0 is frozen in the coordinated UPOS-008–011 interface-stable baseline; material semantic change requires a new reviewed version.

## 10. Historical rejected items

Rejected/superseded objects remain discoverable historical evidence; deletion/archival follows Documentation governance.
