# Improvement Opportunity Model

**ID:** UPOS-09-IOM-001  
**Type:** IMPROVEMENT OPPORTUNITY MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Definition

An Improvement Opportunity is a bounded location where governed system behavior may be improved.

Examples:

```text
a Skill Definition
a Workflow/Profile
a Context policy/source-selection rule
an Engineering Governance standard
a Quality criterion/policy
an Observability definition
an Agent Contract / organizational handoff
a Security/permission policy
a Project Adapter binding
a canonical project document/standard
a test/guardrail owned by an appropriate module/project layer
```

## 2. No independent ID

An Improvement Opportunity is represented within Learning Candidate / Improvement Proposal records through:

```text
canonical_owner_ref
target_artifact_ref
target_version
opportunity_summary
scope
```

No `improvement_opportunity_id` exists in v1.

## 3. Owner resolution

Every material opportunity MUST resolve the canonical owner before an actionable Improvement Proposal can be handed off.

If owner resolution is unresolved:

```text
CANONICAL_OWNER_UNRESOLVED
```

and the proposal cannot be treated as actionable owner change.

## 4. Examples

```text
review-diff Skill improvement → UPOS-003
FEATURE Workflow improvement → UPOS-004
Context selection improvement → UPOS-005
atomic commit standard improvement → UPOS-006
Quality criterion improvement → UPOS-007
measurement definition improvement → UPOS-008
Security policy improvement → UPOS-010
provider/project mapping improvement → UPOS-011
project truth/documentation change → UPOS-01 / project canonical owner
```

## 5. Boundary

Classification of an opportunity never makes UPOS-009 the owner of the target behavior.
