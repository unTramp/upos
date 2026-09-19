# Skill — capture-learning

**ID:** SKL-CAPTURE-LEARNING  
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
skill_id: SKL-CAPTURE-LEARNING
name: capture-learning
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Transform an evidence-backed recurring/systemic observation into a structured Learning Candidate without promoting it.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- outcome/failure/review/incident evidence
- candidate systemic pattern
- UPOS-009 Learning interface

## Outputs

- LEARNING_CANDIDATE

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant evidence and affected contracts

## Optional Source Classes

- historical similar findings
- metrics references

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document/evidence read`
- `structured write`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `learning-candidate write if externally authorized`

This declaration does not grant permissions.

## Applicable Roles

- Documentation Guardian
- Reviewer
- QA
- Architecture
- Security
- Orchestrator

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. State trigger and evidence.
2. Explain why the issue may be systemic rather than one-off.
3. Identify affected standards/skills/workflows/tests as candidates only.
4. Record uncertainty/counterevidence.
5. Submit candidate to UPOS-009/UPOS-01 promotion process.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- evidence linked
- systemic claim justified
- promotion target remains proposal
- no hidden canonical update

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- evidence too weak
- pattern is task-specific
- candidate duplicates active learning

## Escalation Conditions

- candidate would change protected universal policy/authority

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
