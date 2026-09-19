# Skill — reconcile-documentation

**ID:** SKL-RECONCILE-DOCUMENTATION  
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
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-RECONCILE-DOCUMENTATION
name: reconcile-documentation
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Identify documentation impact of a bounded change and update/propose updates to the correct canonical owners without redefining project truth.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/spec/decision
- documentation Source-of-Truth map
- documentation impact scope

## Outputs

- DOCUMENTATION_CHANGE and/or DOCUMENTATION_IMPACT_REPORT

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- UPOS-01 documentation governance
- affected canonical documents

## Optional Source Classes

- diff/PR evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`
- `link validation`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `document-write if externally authorized`

This declaration does not grant permissions.

## Applicable Roles

- Documentation Guardian
- Implementer
- Product
- Architecture

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify changed fact scopes/contracts.
2. Resolve canonical documentation owners via UPOS-01.
3. Update only owned/authorized documentation or produce proposed changes.
4. Preserve provenance/supersession links.
5. Report unresolved doc-vs-code conflicts rather than choosing silently.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- canonical owner targeted
- no duplicated truth introduced
- temporary/current state not injected into stable truth
- conflicts visible

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- canonical owner cannot be resolved
- active normative docs conflict
- write authority unavailable

## Escalation Conditions

- product/domain/architecture meaning is ambiguous

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
