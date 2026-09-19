# Skill — write-regression-test

**ID:** SKL-WRITE-REGRESSION-TEST  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** reproduce-bug


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-WRITE-REGRESSION-TEST
name: write-regression-test
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Create a focused automated test that proves a known defect/contract regression and protects the corrected behavior.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- reproduction/evidence
- expected behavior contract
- test framework interface

## Outputs

- TEST_CHANGE: focused regression test(s)

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant behavior/test/engineering contracts

## Optional Source Classes

- existing neighboring tests

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository read/write`
- `test execution`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `code/test write as externally granted`

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

1. Translate the reproduced contract violation into a deterministic assertion.
2. Choose the narrowest appropriate test layer.
3. Make the test fail for the defect when safely verifiable.
4. Avoid overspecifying unrelated implementation details.
5. Run relevant test evidence through external quality tooling.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- test protects behavior, not accident
- failure mode represented
- test is maintainable and scoped

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- defect not reproducible
- test layer cannot observe contract
- expected behavior ambiguous

## Escalation Conditions

- test requires architectural seam/change outside scope

## Dependencies

- `OPTIONALLY_USES reproduce-bug`

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

- `reproduce-bug`

## Replacement / Supersession

None in v1.0.
