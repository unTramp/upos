# Module 11 Cross-Module Interfaces

**ID:** UPOS-11-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## UPOS-01 — Documentation / Source of Truth

**Consumes:** canonical source ownership, source refs, policy refs, project knowledge.  
**Provides:** concrete source/provider/path bindings.  
**MUST NOT redefine:** canonicality, truth, knowledge promotion.

## UPOS-002 — Agent Organization

**Consumes:** Role/Agent/Agent Run identities and authority.  
**Provides:** runtime/provider identity bindings.  
**MUST NOT redefine:** authority, delegation, SoD.

## UPOS-003 — Skills

**Consumes:** Skill IDs/versions, capability/tool requirements.  
**Provides:** Skill implementation/tool/provider bindings.  
**MUST NOT redefine:** Skill procedure/result semantics.

## UPOS-004 — Workflow

**Consumes:** runtime/orchestration interface needs.  
**Provides:** scheduler/state persistence/callback/runtime bindings where implemented.  
**MUST NOT redefine:** routing, stages, transitions, retry/rework.

## UPOS-005 — Context & Memory

**Consumes:** abstract source classes/provider resolution needs.  
**Provides:** physical source/provider bindings.  
**MUST NOT redefine:** authority order, retrieval, freshness, Context/Memory semantics.

## UPOS-006 — Engineering Governance

**Consumes:** repository/workspace/branch-role/command/CI implementation needs.  
**Provides:** repository/provider/path/workspace/command bindings.  
**MUST NOT redefine:** atomicity, branch requirement, merge mechanics, engineering policy.

## UPOS-007 — Quality

**Consumes:** Quality evidence/check/tool requirements.  
**Provides:** test/analyzer/evidence-provider bindings and policy-backed project values.  
**MUST NOT redefine:** criteria, sufficiency, verdict, readiness.

## UPOS-008 — Observability

**Consumes:** Event/Trace/Metric/read-model abstract interfaces.  
**Provides:** Event Store/sink, trace exporter/carrier, metric/query backend, projection store, provider usage/pricing/clock/event-adapter bindings.  
**MUST NOT redefine:** Event/Trace/Metric/projection semantics.

## UPOS-009 — Learning

**Consumes:** Learning policy/source/validation/owner-routing binding needs.  
**Provides:** project-specific thresholds by policy ref, evidence-source bindings, validation environments, artifact locations and owner routing.  
**MUST NOT redefine:** Pattern, Root Cause, Learning Candidate, Proposal, Promotion.

## UPOS-010 — Security & Permissions

**Consumes:** Security Subject/Capability/Resource/Grant/Protected Action binding needs.  
**Provides:** provider identity, IAM/capability mapping, resource/environment, secret store/injection, approval/elevation/break-glass enforcement and telemetry/audit handling-constraint bindings.  
**MUST NOT redefine:** Permission Decision, Grant semantics, Security Policy, veto/exception authority.

## Schemas/runtime

Schemas MAY encode these contracts. Runtime MAY execute them. Neither may invent independent semantics.

## Control Plane

Control Plane may display Project Adapter configuration/health/read models. Actions route to owner interfaces; projection state is not domain truth.
