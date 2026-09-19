# Skill — classify-change

**ID:** SKL-CLASSIFY-CHANGE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `classification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CLASSIFY-CHANGE
name: classify-change
version: 1.0.0
status: ACTIVE
category: classification
```

## Purpose

Produce a structured change-classification recommendation against the canonical classification model.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- task/change description
- authoritative affected-domain context
- canonical change-classification model reference

## Outputs

- CLASSIFICATION_RECOMMENDATION with rationale, uncertainty, affected domains, referenced classification criteria

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Product/Feature Contract as relevant
- Domain/Architecture/Security contracts as relevant

## Optional Source Classes

- historical similar changes
- incident/review evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `source search/read`
- `structured analysis`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-authoritative-context`

This declaration does not grant permissions.

## Applicable Roles

- Orchestrator
- Product
- Architecture
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Normalize the requested change into one coherent intention.
2. Identify affected project scopes without deciding their ownership.
3. Read the externally owned classification criteria.
4. Compare the change against those criteria and risk signals.
5. Return recommendation plus uncertainty/escalation; do not route the Workflow.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- classification recommendation cites authoritative criteria
- affected scopes are explicit
- uncertainty is not hidden
- no routing/gate semantics are invented

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- canonical classification model unavailable
- conflicting authoritative context
- change description too ambiguous

## Escalation Conditions

- classification cannot be justified from owner model
- candidate crosses protected/high-risk semantics requiring owner decision

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.
