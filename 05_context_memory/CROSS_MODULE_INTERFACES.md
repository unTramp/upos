# Module 05 Cross-Module Interfaces

**ID:** UPOS-05-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-005 provides**
- Source Class requirements/queries for execution;
- Bundle provenance/source references;
- Memory candidate/promotion inputs.

**UPOS-005 consumes**
- fact scope;
- canonical owner/source resolution;
- active normative source status;
- decisions/refinements;
- knowledge lifecycle/supersession;
- epistemic classes/provenance.

**MUST NOT redefine**
- truth, ownership, precedence, promotion, conflict resolution.

## UPOS-002 — Agent Organization

**Provides**
- Role/Run-specific Context Views;
- Context isolation supporting independent Roles.

**Consumes**
- Role identity;
- Agent Definition/version;
- Agent Run;
- authority/SoD;
- handoff/Human Governance constraints.

**MUST NOT redefine**
- authority, delegation, SoD, veto, approval.

Invariant supported:

```text
Implementer context != automatically Reviewer context
```

## UPOS-003 — Skills System

**Provides**
- resolved Context for Skill Invocation;
- follow-up bounded Context interface.

**Consumes**
- Required/Optional Source Classes;
- Required Context Interface;
- Skill identity/version.

**MUST NOT redefine**
- Skill procedure/evaluation.

## UPOS-004 — Workflow Engine

**Provides**
- Stage-aware Context Bundles;
- Context validity/invalidation/reassembly results.

**Consumes**
- task_id;
- routing_decision_id;
- workflow_instance_id;
- stage_id;
- Change Class/concerns;
- reclassification/rerouting information.

**MUST NOT redefine**
- routing, state, transitions, retry/rework/recovery sequencing.

## UPOS-006 — Engineering Governance

**Provides**
- Context requirements/references needed for engineering execution/review.

**Consumes**
- abstract repository/diff/commit/PR artifact interfaces when they exist.

**MUST NOT redefine**
- Git, branch, commit, PR, merge, worktree policy.

## UPOS-007 — Quality System

**Provides**
- independent Reviewer/QA Context Views;
- Bundle provenance usable by evidence consumers.

**Consumes**
- Quality-owned evidence/context requirements;
- finding/gate outputs only as labeled external artifacts.

**MUST NOT redefine**
- PASS/FAIL/BLOCKED, finding severity, evidence/gate semantics.

## UPOS-008 — Observability

**Provides stable semantic references**
- context_request_id;
- context_bundle_id;
- memory_item_id;
- task/workflow/stage/agent/skill refs;
- source refs/versions;
- validity/freshness states;
- budget summary;
- Context health signals.

**Consumes**
- event/trace/metric/retention semantics.

**MUST NOT redefine**
- event_id, trace_id, span_id, metric schema, dashboard, telemetry retention.

## UPOS-009 — Learning

**Provides**
- Context/Memory failure evidence and candidate inputs.

**Consumes**
- learning detection/promotion proposals affecting Context policies.

**MUST NOT redefine**
- learning promotion/evolution or silently evolve policy.

## UPOS-010 — Security & Permissions

**Provides**
- execution surface for permission-aware retrieval, minimization, redaction/reference-only/isolation.

**Consumes**
- access grants;
- sensitive/secret/protected-data policy;
- permission/security constraint decisions.

**MUST NOT redefine**
- who is allowed access or Security veto substance.

## UPOS-011 — Project Adapter

**Provides abstract requirements**
- source mapping needs;
- search/retrieval capability needs;
- storage/cache capability needs;
- model capacity interface needs.

**Consumes concrete bindings**
- physical source paths/IDs;
- search provider;
- repository/document provider;
- storage/cache backend;
- model/provider capacity;
- project-specific policy refinements.

**MUST NOT hard-code**
- provider/vendor/path choices in universal Module-05 semantics.

## Cross-cutting machine-readable schemas/runtime layer

Future machine-readable ContextRequest, ContextBundle, MemoryItem and related schemas MUST trace to these normative Markdown contracts.

Schemas/runtime MUST NOT invent independent Context/Memory semantics.
