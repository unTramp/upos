# Skill — review-security

**ID:** SKL-REVIEW-SECURITY  
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
skill_id: SKL-REVIEW-SECURITY
name: review-security
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Assess a bounded change for security risks and contract conformance using externally owned Security authority/policy.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/diff/design
- security context
- threat/review scope
- UPOS-010/07 interfaces

## Outputs

- ANALYSIS/REVIEW_FINDING candidates tagged security

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Security/Privacy contracts
- Auth/AuthZ rules
- data classification
- relevant architecture

## Optional Source Classes

- scanner output
- threat model
- incident history

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `security scanner results as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `security review/read capabilities`

This declaration does not grant permissions.

## Applicable Roles

- Security
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify protected/security-relevant surfaces.
2. Compare behavior against canonical security constraints.
3. Analyze abuse/misuse/privilege/data exposure paths.
4. Validate scanner findings rather than blindly trust/suppress them.
5. Return scoped evidence-backed findings; veto/approval semantics remain external.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- security scope explicit
- findings actionable/evidence-backed
- false certainty avoided
- no permission/veto policy invented

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- security source unavailable
- protected evidence inaccessible
- scope exceeds bounded review

## Escalation Conditions

- potential material vulnerability
- required Security authority decision

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
