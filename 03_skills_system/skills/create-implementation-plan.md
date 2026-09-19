# Skill — create-implementation-plan

**ID:** SKL-CREATE-IMPLEMENTATION-PLAN  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `planning`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-IMPLEMENTATION-PLAN
name: create-implementation-plan
version: 1.0.0
status: ACTIVE
category: planning
```

## Purpose

Translate an approved bounded change into a coherent implementation plan without changing approved semantics.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved change/spec/decision
- authoritative technical context
- engineering constraints

## Outputs

- PLAN: bounded Change Plan candidate

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Feature/Product Contract
- Domain/Architecture/API/Engineering contracts
- relevant decisions

## Optional Source Classes

- existing code/tests
- migration/runbook info

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `search`
- `analysis`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-authoritative-context`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Implementer
- Orchestrator

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Restate approved outcome and non-scope.
2. Identify affected components/contracts.
3. Order intrinsic implementation dependencies without defining organizational Workflow.
4. Define validation needs and risk notes.
5. Propose logical change slices/expected commits by reference to UPOS-006 policy.
6. Record unknowns and owner decisions required.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- plan preserves approved semantics
- non-scope explicit
- logical dependencies visible
- no opportunistic refactor hidden

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- approved intent ambiguous
- critical technical source missing
- plan would require unapproved architecture/domain change

## Escalation Conditions

- new durable decision required

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
