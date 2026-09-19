# Module 04 Cross-Module Interfaces

**ID:** UPOS-04-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth

**Provides:** Workflow-required Source Class declarations and orchestration references.  
**Consumes:** canonical owner/source resolution, normative conflict behavior, knowledge lifecycle.  
**Must not redefine:** project truth/canonical promotion.

## UPOS-002 — Agent Organization

**Provides:** Role participation/routing requirements and stage responsibility references.  
**Consumes:** Role identity, authority, delegation, SoD, handoff contract, human governance.  
**Must not redefine:** Role authority or handoff semantics.

Required invariants:

```text
Implementer != Final Reviewer
high-risk: Implementer != Reviewer != Merge Controller
```

## UPOS-003 — Skills System

**Provides:** when/where Skill invocation is required by reference.  
**Consumes:** stable Skill IDs/versions/contracts.  
**Must not redefine:** Skill procedure/evaluation.

## UPOS-005 — Context & Memory

**Provides:** source/context requirements per Workflow/Stage.  
**Consumes:** retrieval, assembly, memory, budget/freshness semantics.  
**Must not redefine:** how context is retrieved/ranked.

## UPOS-006 — Engineering Governance

**Provides:** orchestration points requiring engineering actions/results.  
**Consumes:** branch/commit/PR/merge/worktree/collision mechanics.  
**Must not redefine:** Git policy.

## UPOS-007 — Quality System

**Provides:** which external review/QA/evidence/readiness gates are required and where.  
**Consumes:** gate/evidence/finding/verdict semantics.  
**Must not redefine:** what PASS/FAIL/BLOCKED means.

## UPOS-008 — Observability

**Provides:** stable semantic identity references suitable for future provenance/telemetry correlation:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

**Consumes:** event/trace/metric/retention semantics.  
**Must not redefine:** telemetry/event/trace model, occurrence/event identity, retention, metrics, or dashboard semantics.

Stable identity belongs to UPOS-004; observability semantics remain UPOS-008.

## UPOS-009 — Learning

**Provides:** orchestration completion/failure/rework signals that may become learning inputs.  
**Consumes:** learning detection/evolution proposals.  
**Must not redefine:** learning promotion.

## UPOS-010 — Security & Permissions

**Provides:** protected checkpoint/approval references required by classification/profiles.  
**Consumes:** permissions, protected actions, secrets, human/security approval semantics.  
**Must not redefine:** grants/veto/security truth.

## UPOS-011 — Project Adapter

**Provides:** abstract requirements for commands/providers/project-specific stricter policies.  
**Consumes:** concrete bindings, commands, paths, provider/runtime adapters.  
**Must not redefine:** universal Workflow semantics.

## Cross-cutting schemas/runtime

Future machine-readable WorkflowDefinition/Task/RoutingDecision/WorkflowInstance representations must trace to this normative Markdown and must not create independent semantics.
