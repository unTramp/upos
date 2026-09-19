# Learning Failure Model

**ID:** UPOS-09-LFM-001  
**Type:** FAILURE MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Failure taxonomy

Canonical v1 learning-analysis failure classes:

```text
INSUFFICIENT_EVIDENCE
PATTERN_NOT_CONFIRMED
CONFOUNDING_UNRESOLVED
ROOT_CAUSE_UNRESOLVED
CANONICAL_OWNER_UNRESOLVED
PROPOSAL_NOT_ACTIONABLE
VALIDATION_PLAN_INSUFFICIENT
PROMOTION_REJECTED
OWNER_CHANGE_NOT_OBSERVED
OUTCOME_INCONCLUSIVE
DEPENDENCY_INTERFACE_UNRESOLVED
SENSITIVE_EVIDENCE_ACCESS_BLOCKED
DUPLICATE_OR_CONSOLIDATED
```

These are Learning failure/result conditions, not Workflow states.

## 2. Responses

Typical responses:

```text
INSUFFICIENT_EVIDENCE
→ gather evidence / wait / close candidate / owner decision

PATTERN_NOT_CONFIRMED
→ reject/archive Pattern Candidate

CONFOUNDING_UNRESOLVED
→ collect comparison evidence / mark inconclusive

ROOT_CAUSE_UNRESOLVED
→ retain multiple hypotheses / do not assert fact

CANONICAL_OWNER_UNRESOLVED
→ UPOS-01 owner resolution / escalation

PROPOSAL_NOT_ACTIONABLE
→ rework proposal, not target artifact

VALIDATION_PLAN_INSUFFICIENT
→ revise plan before claiming expected effect

PROMOTION_REJECTED
→ preserve reason; no target mutation

OUTCOME_INCONCLUSIVE
→ extend evidence only if policy justifies; avoid fake conclusion
```

## 3. Escalation

Workflow sequencing/escalation mechanics remain UPOS-004/002-owned.

UPOS-009 reports the learning condition and required external resolution.

## 4. No infinite analysis

Pattern/root-cause/proposal analysis MUST NOT loop indefinitely.

Project/Workflow policy may bound cycles/time. Exhaustion requires controlled outcome such as:

```text
INCONCLUSIVE
REJECTED
OWNER_DECISION_REQUIRED
DEFERRED_WITH_TRIGGER
```

rather than silent recursion.
