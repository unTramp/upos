# Acceptance Criteria Evaluation

**ID:** UPOS-07-ACE-001  
**Type:** ACCEPTANCE CRITERIA EVALUATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Ownership

Acceptance criteria are project/Task truth owned/governed through UPOS-01.

UPOS-007 owns their evaluation semantics.

## 2. Applicability

Each acceptance criterion must resolve to:

```text
APPLICABLE
NOT_APPLICABLE
UNRESOLVED
```

## 3. Evaluation states

For each criterion:

```text
SATISFIED
UNSATISFIED
BLOCKED
NOT_EVALUATED
NOT_APPLICABLE
```

Do not use binary PASS when the criterion cannot actually be evaluated.

## 4. Evidence

A SATISFIED state requires sufficient applicable evidence for the exact target.

An Implementer assertion is not automatically sufficient.

## 5. Unknown or ambiguous criterion

If criterion meaning is ambiguous/conflicting:

```text
applicability/evaluation = UNRESOLVED / BLOCKED
→ source/owner decision interface
```

UPOS-007 does not invent requirement meaning.

## 6. Criteria change

If acceptance criteria/source version changes materially after an Assessment, prior evidence/Assessment must be revalidated for applicability.

Historical Assessment remains linked to the old criterion version.
