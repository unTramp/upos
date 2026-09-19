# UPOS-004 — Workflow Engine

**ID:** UPOS-04-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, UPOS-003, frozen master design source


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-004 defines how U-POS classifies work, selects a Workflow, composes concern-specific orchestration requirements, sequences Roles/Skills/stages, handles transitions/rework/retry/recovery/reclassification, and reaches a terminal orchestration result.

It does this without taking ownership from Agent Organization, Skills, Context & Memory, Engineering Governance, Quality, Security, Observability, Learning, or Project Adapter.

## 1. Fundamental model

```text
TASK / CHANGE REQUEST
= work entering the operating system

CHANGE CLASS
= canonical impact/risk classification

WORK TYPE
= primary nature/intention of the work

CONCERN
= cross-cutting impact affecting orchestration

WORKFLOW DEFINITION
= versioned canonical base orchestration contract

WORKFLOW PROFILE
= reusable concern-specific orchestration overlay

RESOLVED WORKFLOW CONFIGURATION
= Base Workflow + Profiles + Change Class + external policy references

WORKFLOW INSTANCE
= one concrete execution of one resolved Workflow configuration

WORKFLOW STAGE
= bounded orchestration phase

TRANSITION
= allowed movement between stages/states

GATE REFERENCE
= reference to an externally owned condition/result

ROUTING DECISION
= attributable selection of the resolved configuration

WORKFLOW RESULT
= terminal orchestration outcome
```

These concepts MUST NOT be used interchangeably.

## 2. Three-axis routing model

UPOS-004 adopts the following normalized model:

```text
1. CHANGE CLASS
   C0–C5
   = impact / risk depth

2. WORK TYPE
   = primary intention

3. CONCERNS / PROFILES
   = cross-cutting orchestration impacts
```

Resolution:

```text
Base Workflow
+
Concern Profiles
+
Change Class
+
External policy/gate references
=
Resolved Workflow Configuration
```

This model preserves frozen-source workflows while avoiding combinatorial explosion.

## 3. Critical boundaries

```text
Role / authority / SoD / handoff contract → UPOS-002
Skill procedure / registry / evaluation   → UPOS-003
Context retrieval / memory / budgets      → UPOS-005
Git / commit / PR / merge mechanics       → UPOS-006
Quality evidence / verdict / gate meaning → UPOS-007
Telemetry / traces / dashboard            → UPOS-008
Learning detection / promotion            → UPOS-009 + UPOS-01
Permissions / protected actions           → UPOS-010
Project/provider/runtime bindings          → UPOS-011
Canonical project truth                    → UPOS-01
```

Workflow definitions reference those interfaces; they do not redefine them.

## 4. Organizational invariants consumed from UPOS-002

```text
Implementer != Final Reviewer
```

For high-risk work:

```text
Implementer != Reviewer != Merge Controller
```

The Workflow Engine MUST route/compose stages so these constraints can be satisfied.

## 5. Skill boundary consumed from UPOS-003

```text
ROLE / AGENT
= WHO

SKILL
= reusable bounded HOW

WORKFLOW
= WHEN, WHY, UNDER WHAT CONDITIONS,
  and IN WHAT ORDER
```

Workflow definitions reference stable Skill IDs/versions. They MUST NOT copy Skill procedures.

## 6. Read order

1. `WORKFLOW_OPERATING_MODEL.md`
2. `CHANGE_CLASSIFICATION_STANDARD.md`
3. `WORK_TYPE_AND_CONCERN_MODEL.md`
4. `WORKFLOW_PROFILE_STANDARD.md`
5. `WORKFLOW_CONTRACT_STANDARD.md`
6. `ROUTING_STANDARD.md`
7. `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`
8. `WORKFLOW_STATE_MODEL.md`
9. `RECLASSIFICATION_AND_REROUTING.md`
10. `FAILURE_RETRY_RECOVERY.md`
11. `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md`
12. `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`
13. `WORKFLOW_CATALOG.md`
14. `CROSS_MODULE_INTERFACES.md`
15. relevant `workflows/*.md`
16. relevant `profiles/*.md`
17. `MODULE_04_TRACEABILITY.md`
