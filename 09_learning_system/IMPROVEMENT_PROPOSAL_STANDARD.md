# Improvement Proposal Standard

**ID:** UPOS-09-IPS-001  
**Type:** IMPROVEMENT PROPOSAL STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/IMPROVEMENT_PROPOSAL_TEMPLATE.md



## 1. Identity

Every Improvement Proposal has stable:

```text
improvement_proposal_id
```

## 2. Contract

```text
improvement_proposal_id
status

learning_candidate_refs
root_cause_assessment_refs

canonical_owner_ref
target_artifact_ref
target_version

problem_statement
proposed_change
expected_effect

impact_dimensions
risk_refs
compatibility_impact
migration_impact

validation_plan_ref
required_reviewer_or_authority_refs

owner_resolution_ref
external_decision_ref
external_change_ref

created_by_ref
created_at

supersedes
replacement
```

## 3. Direct-mutation prohibition

```text
Improvement Proposal
MUST NOT
mutate the target artifact directly.
```

Required boundary:

```text
proposal
→ canonical-owner resolution
→ owner-module/project change workflow
→ review / validation / decision
→ new target version if accepted
```

UPOS-009 may draft, validate and recommend; it does not approve/publish the target change.

## 4. Proposal lifecycle

```text
DRAFT
→ OWNER_RESOLUTION_PENDING
→ VALIDATION_PLANNED
→ VALIDATING
→ READY_FOR_OWNER_REVIEW
→ HANDED_OFF_TO_OWNER
→ CLOSED
```

Alternative terminal/non-success states:

```text
REJECTED
WITHDRAWN
SUPERSEDED
```

Owner acceptance/change decisions remain external refs and MUST NOT be disguised as Module-09 lifecycle states.

## 5. Proposal actionability

A Proposal is actionable only when:

- the problem is supported by Candidate/evidence;
- canonical owner is resolved;
- target is identifiable/versioned where applicable;
- proposed change is sufficiently bounded;
- expected effects are explicit;
- compatibility/migration risks are addressed;
- validation plan is adequate to risk;
- required external reviewer/authority references are known or explicitly unresolved.

## 6. Promotion recommendation

A Module-09 promotion recommendation MAY state:

```text
READY_FOR_OWNER_REVIEW
NOT_READY
BLOCKED
INCONCLUSIVE
```

It is not approval and does not grant authority.
