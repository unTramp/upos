# Skill — analyze-incident

**ID:** SKL-ANALYZE-INCIDENT  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `operations`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ANALYZE-INCIDENT
name: analyze-incident
version: 1.0.0
status: ACTIVE
category: operations
```

## Purpose

Produce evidence-backed incident analysis separating observed facts, hypotheses, contributing causes and follow-up candidates.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- incident timeline/evidence
- affected system contracts
- analysis scope

## Outputs

- INCIDENT_ANALYSIS: observations, evidence, hypotheses/root-cause confidence, contributing factors, follow-up candidates

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Operations/Architecture/Security contracts
- logs/telemetry evidence
- relevant decisions

## Optional Source Classes

- deploy/change history
- similar incidents

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `logs/telemetry read`
- `repository/document read`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `incident evidence read as externally granted`

This declaration does not grant permissions.

## Applicable Roles

- DevOps / SRE
- Architecture
- Security
- Implementer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Establish timeline from evidence.
2. Separate confirmed observations from hypotheses.
3. Identify contract/system deviations and contributing conditions.
4. Assess root-cause confidence explicitly.
5. Produce follow-up candidates without self-promoting standards/skills/workflows.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- timeline/evidence attributable
- epistemic classes preserved
- root-cause confidence explicit
- follow-ups not silently canonized

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- evidence insufficient
- sensitive evidence inaccessible
- multiple plausible causes unresolved

## Escalation Conditions

- security/privacy impact
- material unresolved causal uncertainty

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
