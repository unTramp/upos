# Separation of Duties Standard

**ID:** UPOS-02-STD-005  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AUTHORITY_MODEL.md`, `ROLE_CATALOG.md`, `HUMAN_GOVERNANCE.md`

## 0. Purpose

Prevent creation, verification, and readiness authority from collapsing into self-approval.

## 1. Core invariant

For any governed change requiring independent review:

```text
Implementer != Final Reviewer
```

An Implementer self-check is never a substitute for independent final review.

## 2. High-risk invariant

When downstream risk policy classifies work as high-risk:

```text
Implementer != Reviewer != Merge Controller
```

The three responsibilities must be logically separate.

## 3. Logical separation

Logical separation requires:

- distinct Role identity;
- distinct Agent Run;
- role-specific authority;
- role-appropriate context;
- role-specific output/evaluation;
- no reuse of self-approval result as independent evidence.

## 4. Same base model

Different Roles MAY use the same base model/provider.

That does not violate SoD if logical separation is preserved.

The system must not claim stronger statistical/model independence than actually exists.

## 5. Independent model diversity

Different providers/models MAY be used for stronger diversity.

This is optional and belongs to project/provider configuration (UPOS-11), not a universal Module 02 requirement.

## 6. Prohibited self-approval

The following pattern is invalid:

```text
Implementer
→ self-check
→ declares independent review passed
→ declares merge ready
```

unless downstream policy explicitly treats the change as not requiring independent review.

## 7. Reviewer independence

Reviewer should not silently implement its own blocking findings in the same review responsibility.

Default organizational loop:

```text
Reviewer finding
→ Implementer correction
→ independent re-review
```

Detailed review mechanics are UPOS-07.

## 8. Circular approval

Avoid:

```text
Agent A implements part A and approves B
Agent B implements part B and approves A
```

when both materially participated in the same coupled change and independence would be illusory.

Downstream Quality policy determines whether independence is sufficient.

## 9. Context separation

Independent verification should not depend on hidden implementation reasoning.

Module 02 requires role-level independence.

UPOS-05/UPOS-07 determine exact reviewer/QA context payload.

## 10. Role composition constraints

Compatible roles may be composed where independence is not required.

Examples that MAY be compatible by project policy:

```text
Product + UX
Domain + Architecture
QA + Documentation Guardian
```

Examples that are controlled/prohibited for the same change:

```text
Implementer + Final Reviewer
Implementer + Merge Controller for high-risk
Reviewer + Merge Controller for high-risk
```

## 11. Human participation

Human final authority does not remove the need for required independent agent verification.

Likewise, agent verification does not remove human approval where policy requires it.

## 12. Enforcement interface

Module 02 defines the SoD invariant.

Enforcement is consumed by:

- UPOS-04 workflow state/routing;
- UPOS-07 quality gates;
- UPOS-10 permission/approval enforcement;
- UPOS-08 audit/observability;
- UPOS-11 runtime/project bindings.

## 13. Exceptions

A project MUST NOT silently waive a universal SoD invariant.

If an exception mechanism exists, it must be:

- explicit;
- scope-bound;
- authorized;
- auditable;
- permitted by the owning governance/security policy.

High-risk universal constraints may be declared non-overridable by UPOS-10/project governance.

## Upstream governance dependencies

This document consumes, but does not redefine:

- **UPOS-01 Documentation System** — documentation ownership and durable project knowledge governance.
- **Project Source-of-Truth Model (`DOC-GOV-SOT-001`)** — canonical owner/source resolution and conflict semantics.
- **Project Knowledge Lifecycle Model (`DOC-GOV-KL-001`)** — epistemic states and promotion into canonical project knowledge.

When an active normative conflict exists in upstream canonical sources, the affected agent action MUST stop and escalate. Module 02 does not invent a compromise.

## Downstream interface boundary

Module 02 defines organizational contracts only. Detailed semantics remain owned by:

- **UPOS-03 Skills** — skill procedures, registry, versions, evaluation.
- **UPOS-04 Workflow Engine** — workflow definitions, change classification/routing, task/run state and retry mechanics.
- **UPOS-05 Context & Memory** — retrieval, context assembly, context budgets, memory implementation.
- **UPOS-06 Engineering Governance** — Git, branches, commits, PR mechanics, merge mechanics, worktrees/concurrency.
- **UPOS-07 Quality System** — review/QA procedures, evidence model, quality gates and result semantics.
- **UPOS-08 Observability** — events, traces, metrics, provenance and dashboard data.
- **UPOS-09 Learning** — learning detection/evolution; canonical promotion remains governed with UPOS-01.
- **UPOS-10 Security & Permissions** — permission taxonomy, protected actions, secrets, production access and approval enforcement.
- **UPOS-11 Project Adapter** — project-specific bindings, manifests, providers, concrete paths and commands.

Module 02 MAY require an interface from these modules. It MUST NOT duplicate or privately redefine their owned semantics.
