# Module 03 Cross-Module Interfaces

**ID:** UPOS-03-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-003 provides**
- Source Class requirements in Skill Contracts;
- Skill Result epistemic/output class;
- governed Skill Definition artifacts.

**UPOS-003 consumes**
- canonical owner/source resolution;
- provenance;
- document lifecycle;
- explicit knowledge promotion/supersession.

**MUST NOT redefine**
- project truth;
- canonicality;
- promotion rules.

## 2. UPOS-002 — Agent Organization

**Provides**
- applicable-role compatibility for Skills.

**Consumes**
- Role identity;
- Agent Definition skill interface;
- authority/delegation/SoD.

**MUST NOT redefine**
- Role responsibility or authority.

Invariant:

```text
Skill capability != organizational authority
```

## 3. UPOS-004 — Workflow Engine

**Provides**
- Skill IDs/contracts usable by Workflow definitions;
- applicability constraints;
- dependency information that may inform validation.

**Consumes**
- canonical C0–C5 classification model;
- workflow sequencing/routing;
- retry/recovery sequencing.

**MUST NOT redefine**
- change classes;
- Workflow order/gates.

## 4. UPOS-005 — Context & Memory

**Provides**
- Required/Optional Source Classes;
- Required Context Interface characteristics.

**Consumes**
- retrieval/resolution/context assembly;
- context budget/freshness/memory rules.

**MUST NOT redefine**
- retrieval algorithms or context policy.

## 5. UPOS-006 — Engineering Governance

**Provides**
- engineering-oriented reusable Skills such as `create-atomic-commit` and `implement-change`.

**Consumes**
- Git/branch/commit/PR/merge standards;
- Change Plan semantics.

**MUST NOT redefine**
- Git policy or merge strategy.

## 6. UPOS-007 — Quality System

**Provides**
- verification Skill procedures and Skill-level success criteria.

**Consumes**
- evidence semantics;
- finding severity;
- QA/review/readiness verdict semantics;
- quality gate interfaces.

**MUST NOT redefine**
- final quality verdict authority or evidence model.

## 7. UPOS-008 — Observability

**Provides**
- stable Skill identity/version/result references suitable for telemetry correlation.

**Consumes**
- event/trace/metric semantics.

**MUST NOT redefine**
- event model, cost metrics, retention.

## 8. UPOS-009 — Learning System

**Provides**
- versioned evolution target for Skills;
- Skill-evolution interface.

**Consumes**
- learning detection;
- repeated failure analysis;
- promotion proposals.

**MUST NOT redefine**
- organizational learning detection/promotion.

## 9. UPOS-010 — Security & Permissions

**Provides**
- abstract permission-interface requirements declared by Skills.

**Consumes**
- permission taxonomy/grants;
- protected-action rules;
- secrets/production policy.

**MUST NOT redefine**
- who is permitted to execute protected actions.

## 10. UPOS-011 — Project Adapter

**Provides**
- abstract tool/context/source/permission interface requirements.

**Consumes**
- project paths;
- provider bindings;
- concrete tool implementations;
- project-specific overrides/extensions.

**MUST NOT redefine**
- provider-specific wiring.

## 11. Cross-cutting machine-readable schemas layer

A future schema layer may encode Skill Definition/Invocation/Result structures.

Schemas MUST trace back to Module 03 normative Markdown and MUST NOT create independent Skill semantics.
