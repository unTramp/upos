# Skill — assess-merge-readiness

**ID:** SKL-ASSESS-MERGE-READINESS  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ASSESS-MERGE-READINESS
name: assess-merge-readiness
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Collect and assess whether required readiness evidence appears present, deferring final readiness semantics/authority to UPOS-007/002/010.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/PR reference
- required gate set from external Workflow/Quality policy
- available evidence/approvals

## Outputs

- READINESS_ASSESSMENT input for MergeReadiness contract

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- UPOS-007 Quality contracts
- UPOS-004 Workflow requirements
- UPOS-010 approval policy
- UPOS-006 merge policy

## Optional Source Classes

- review/QA/security/doc outputs

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `PR/CI/evidence read interfaces`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-evidence; merge capability not implied`

This declaration does not grant permissions.

## Applicable Roles

- Merge Controller
- Reviewer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Resolve externally required gates/approvals for this work.
2. Collect references to their results.
3. Detect missing/stale/conflicting evidence.
4. Return readiness assessment without inventing PASS semantics or exercising merge authority.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- all externally required evidence accounted for
- missing evidence explicit
- no self-approval inference

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- required gate model unavailable
- evidence cannot be resolved

## Escalation Conditions

- conflicting verdicts/approvals
- human approval required but absent

## Dependencies

- `None`

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

- None

## Replacement / Supersession

None in v1.0.
