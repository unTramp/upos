# Skill — create-feature-spec

**ID:** SKL-CREATE-FEATURE-SPEC  
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
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-FEATURE-SPEC
name: create-feature-spec
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Draft or update a bounded feature specification from approved Product intent and authoritative constraints.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved feature intent
- scope/non-goals
- authoritative constraints
- specification template/standard

## Outputs

- PROPOSAL/SPEC_CANDIDATE feature specification

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Product Vision/Principles
- relevant Domain/Architecture/UX/Security contracts

## Optional Source Classes

- research evidence
- existing feature specs
- analytics learnings

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `document-write capability if authorized externally`

This declaration does not grant permissions.

## Applicable Roles

- Product
- Domain
- Architecture
- UX

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Resolve feature scope and owning product intent.
2. Collect relevant constraints by source class.
3. Draft behavior, acceptance intent, non-goals, edge cases, dependencies and open questions.
4. Mark unresolved semantics explicitly.
5. Return proposal for owner review/promotion.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- scope/non-goals explicit
- canonical constraints referenced
- unknowns not fabricated
- does not redefine upstream global contracts

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- feature intent not approved/clear
- critical owner conflict
- required canonical sources missing

## Escalation Conditions

- new domain/architecture/security decision required

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
