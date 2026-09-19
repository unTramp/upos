# Skill — reproduce-bug

**ID:** SKL-REPRODUCE-BUG  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `analysis`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REPRODUCE-BUG
name: reproduce-bug
version: 1.0.0
status: ACTIVE
category: analysis
```

## Purpose

Produce a controlled, evidence-backed reproduction of an observed defect or explicitly report that reproduction was not achieved.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- bug report/symptom
- environment/context
- expected behavior contract

## Outputs

- EVIDENCE/ANALYSIS: reproducible steps/fixture and observed vs expected result, or NOT_REPRODUCED result

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant feature/API/domain/test contracts

## Optional Source Classes

- logs
- incident evidence
- prior regressions

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `runtime/test execution as available`
- `repository read`
- `logs/search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `test/runtime access as externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Implementer
- Reviewer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Define expected behavior from canonical source.
2. Isolate minimal reproduction conditions.
3. Execute/observe without altering production truth.
4. Capture deterministic steps/inputs/evidence where possible.
5. Separate reproduction from root-cause hypothesis.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- expected vs observed explicit
- reproduction evidence attributable
- no false certainty when non-reproducible

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- environment unavailable
- expected behavior unspecified
- non-deterministic reproduction

## Escalation Conditions

- cannot establish expected contract
- reproduction needs protected production access

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
