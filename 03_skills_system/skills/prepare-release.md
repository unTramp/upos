# Skill — prepare-release

**ID:** SKL-PREPARE-RELEASE  
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
**Category:** `operations`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-PREPARE-RELEASE
name: prepare-release
version: 1.0.0
status: ACTIVE
category: operations
```

## Purpose

Prepare a bounded release package/readiness set from an already selected release candidate without owning deployment Workflow sequencing.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- release candidate reference
- release requirements
- change/release notes inputs

## Outputs

- RELEASE_PREPARATION: release notes/checklist/artifact references/readiness gaps

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Operations/Release contracts
- Change/Decision records
- migration/runbook contracts

## Optional Source Classes

- CI/evidence summaries

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/artifact read`
- `document write`
- `build artifact inspection as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `release-preparation capabilities; deploy permission not implied`

This declaration does not grant permissions.

## Applicable Roles

- DevOps / SRE
- Implementer
- Documentation Guardian

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify release candidate and externally required release artifacts.
2. Assemble notes/migration/rollback references.
3. Check presence of required preparation items.
4. Report readiness gaps.
5. Do not deploy, merge, or define release gates/order.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- candidate/version unambiguous
- known migrations/rollback references surfaced
- no deployment authority assumed

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- release candidate unclear
- required operational source missing

## Escalation Conditions

- migration/rollback/security requirement unresolved

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
