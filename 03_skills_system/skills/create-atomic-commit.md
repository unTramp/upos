# Skill — create-atomic-commit

**ID:** SKL-CREATE-ATOMIC-COMMIT  
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
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-ATOMIC-COMMIT
name: create-atomic-commit
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Assess a staged logical change against the external atomic-commit standard and prepare a commit request/metadata.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- staged/selected change set
- bounded change intention
- UPOS-006 atomic commit policy

## Outputs

- COMMIT_PREPARATION: validated logical change set + proposed commit metadata/message, or SPLIT_REQUIRED

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Engineering/Git governance

## Optional Source Classes

- Change Plan expected commits

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `diff inspection`
- `git/commit-capable interface`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `commit-capable interface requirement only; grant external`

This declaration does not grant permissions.

## Applicable Roles

- Implementer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify the single logical intention represented by the change set.
2. Compare against external atomic-commit policy.
3. Detect unrelated/multi-purpose changes.
4. Recommend split when necessary.
5. Prepare commit metadata without redefining branch/commit policy.
6. Invoke commit interface only if externally authorized.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- one logical intention
- no unrelated changes
- metadata describes why/what
- external policy referenced

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- change set not coherent
- working tree ambiguous
- commit permission unavailable

## Escalation Conditions

- policy conflict or protected repository rule blocks commit

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
