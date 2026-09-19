# Skill — qa-validation

**ID:** SKL-QA-VALIDATION  
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
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-QA-VALIDATION
name: qa-validation
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Exercise intended behavior against acceptance/user/regression scenarios and return observations/evidence for the external QA verdict model.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- acceptance intent/spec
- build/change under test
- QA scope
- UPOS-007 evidence/verdict interface

## Outputs

- QA_OBSERVATION / evidence references for QAResult

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
- bug reproduction
- risk/user scenarios
- relevant UX/API contracts

## Optional Source Classes

- test suite results
- historical regressions

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `application/test execution`
- `logs/screenshots as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `test environment access externally granted`

This declaration does not grant permissions.

## Applicable Roles

- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Derive scenarios from authoritative acceptance/bug/risk context.
2. Exercise happy, negative and relevant edge paths.
3. Record observed results and reproducible evidence.
4. Separate observation from externally owned QA verdict semantics.
5. Report blocked coverage explicitly.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- scenario coverage tied to contract/risk
- evidence attributable
- blocked areas visible
- does not equal 'tests passed'

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- environment unavailable
- acceptance contract missing
- test data/access unavailable

## Escalation Conditions

- material behavior ambiguous
- required protected access unavailable

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
