# Skill — review-diff

**ID:** SKL-REVIEW-DIFF  
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
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REVIEW-DIFF
name: review-diff
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Perform a bounded technical review of a change diff against authoritative contracts and externally owned quality semantics.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- diff/change artifacts
- authoritative context
- review scope/dimensions
- UPOS-007 review/evidence interface

## Outputs

- REVIEW_FINDING candidates / structured review analysis for UPOS-007 verdict semantics

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant Product/Domain/Architecture/Engineering/Security/UX/Quality contracts

## Optional Source Classes

- tests/CI evidence
- Change Plan

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `diff/repository inspection`
- `search`
- `test-result read`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read/review capability externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Reviewer
- Architecture
- Security
- Domain
- UX / Product Design
- Design System

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm review scope and independence requirements from upstream contracts.
2. Read authoritative expectations before judging implementation.
3. Inspect changed behavior and relevant neighboring code.
4. Identify concrete defects/risks with evidence and owner dimension.
5. Return structured findings without issuing unauthorized final verdict semantics.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- findings specific/evidence-backed
- scope-aware
- no style-only noise presented as blocking
- authority boundaries preserved

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- required context/evidence missing
- review independence invalid
- diff too broad to review reliably

## Escalation Conditions

- blocking uncertainty
- scope/authority conflict
- quality system requires additional gate

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
