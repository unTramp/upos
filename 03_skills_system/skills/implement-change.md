# Skill — implement-change

**ID:** SKL-IMPLEMENT-CHANGE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact, write-regression-test


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-IMPLEMENT-CHANGE
name: implement-change
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Execute one bounded approved implementation change while preserving scope and authoritative contracts.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved Change Plan segment
- authoritative context
- current implementation/tests

## Outputs

- IMPLEMENTATION_CHANGE plus implementation evidence references

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant Product/Domain/Architecture/API/Engineering/UX/Design/Security contracts

## Optional Source Classes

- related decisions
- existing tests

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository read/write`
- `test/lint/build capabilities as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `code-write capabilities externally granted`

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

1. Confirm bounded intention/non-scope.
2. Inspect existing implementation and tests.
3. Make the minimum coherent change satisfying the approved contract.
4. Update/add tests appropriate to the change.
5. Run relevant checks through available interfaces.
6. Report unexpected required scope/semantic changes instead of silently adopting them.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- approved intent satisfied
- scope preserved
- unrelated refactor excluded
- tests/checks appropriate
- unknowns/escalations explicit

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- plan conflicts with canonical source
- required scope expands materially
- tool/test capability unavailable

## Escalation Conditions

- new domain/product/architecture/security decision required
- protected permission needed

## Dependencies

- `OPTIONALLY_USES analyze-impact`
- `OPTIONALLY_USES write-regression-test`

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
- `write-regression-test`

## Replacement / Supersession

None in v1.0.
