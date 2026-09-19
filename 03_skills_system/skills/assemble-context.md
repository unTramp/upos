# Skill — assemble-context

**ID:** SKL-ASSEMBLE-CONTEXT  
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
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ASSEMBLE-CONTEXT
name: assemble-context
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Request and organize a task-appropriate context bundle through the canonical Context interface.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- task/skill purpose
- required source classes
- role identity
- UPOS-005 context interface

## Outputs

- CONTEXT_REQUEST or CONTEXT_BUNDLE_REFERENCE conforming to UPOS-005

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Source-of-Truth resolution interface metadata

## Optional Source Classes

- previous run artifact references

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `context/source resolver interface`
- `search/read capability`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-context according to external permission policy`

This declaration does not grant permissions.

## Applicable Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Architecture
- Product
- Security

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Derive required Source Classes from the consuming contract.
2. Request resolution through UPOS-005/UPOS-01 interfaces.
3. Organize returned references for the bounded task.
4. Report missing/stale/conflicting sources instead of compensating privately.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- no physical paths hard-coded
- required source classes covered or explicitly missing
- authority/freshness decisions delegated to owner interfaces

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- context resolver unavailable
- required source unresolved
- permission prevents required context

## Escalation Conditions

- missing canonical source blocks execution
- active sources conflict

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
