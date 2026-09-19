# Skill — review-architecture

**ID:** SKL-REVIEW-ARCHITECTURE  
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
skill_id: SKL-REVIEW-ARCHITECTURE
name: review-architecture
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Evaluate a proposed/implemented change for conformance with canonical architecture contracts and decision boundaries.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/RFC/diff
- canonical architecture context
- review scope

## Outputs

- ANALYSIS/REVIEW_FINDING candidates tagged architecture

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Master Architecture
- ADRs
- Domain ownership boundaries
- relevant NFRs

## Optional Source Classes

- implementation diff
- performance/security evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `diagram/search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read/review capability`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify architecture contracts affected.
2. Check boundary/ownership/data-flow/integration conformance.
3. Detect new durable decisions hidden in implementation.
4. Separate architecture violations from optional improvements.
5. Return evidence-backed findings/proposals.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- canonical architecture referenced
- new boundary decisions surfaced
- no Product/Domain authority assumption

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- architecture source unresolved
- change requires architecture decision not yet made

## Escalation Conditions

- material architecture conflict or missing ADR/RFC decision

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
