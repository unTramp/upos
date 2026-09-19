# Context Assembly Standard

**ID:** UPOS-05-CAS-001  
**Type:** ASSEMBLY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CONTEXT_BUNDLE_STANDARD.md, CONTEXT_ISOLATION_AND_VIEWS.md


## 1. Assembly sequence

```text
1. validate bounded Context Request
2. resolve canonical owner/source universe through UPOS-01
3. apply permission/security constraints
4. retrieve physical candidates via abstract provider interface
5. apply project/scope/version/lifecycle eligibility
6. evaluate freshness/applicability
7. preserve epistemic/source labels
8. satisfy required sources
9. rank optional/supporting candidates
10. choose safe representation
11. fit Context Budget
12. build Context View for consumer
13. build Context Manifest
14. seal immutable Context Bundle
```

## 2. Assembly order from frozen master

The frozen sequence:

```text
task / issue
project manifest
relevant source of truth
relevant specification
relevant decisions
relevant implementation
relevant tests
current plan
```

is preserved as a useful assembly heuristic but is subordinate to UPOS-01 ownership, concrete Context Requirements, permissions, and current applicability.

## 3. Epistemic class preservation

Context MUST preserve UPOS-01 knowledge classes where applicable:

```text
Signal
Observation
Evidence
Hypothesis
Proposal
Decision
Canonical knowledge
Learning
Historical knowledge
```

Other artifacts such as Review Findings may retain artifact subtype without inventing a competing truth hierarchy.

## 4. Context contamination guard

Assembly MUST guard against:

- unverified Agent speculation presented as fact;
- stale summary presented as current source;
- wrong-project material;
- wrong-version design/spec;
- Implementer justification treated as independent Reviewer evidence;
- historical/superseded decision treated as active;
- private model memory used as project truth;
- implementation evidence silently overriding normative source.

## 5. Context Manifest

Manifest is mandatory for production Bundles and records requirement satisfaction, source resolution refs, included items, exclusions/reasons, representations, freshness, budget, conflicts and unknowns.

## 6. Skill interface

`SKL-ASSEMBLE-CONTEXT` is an UPOS-003 `INTERFACE_SKILL`.

Formal separation:

```text
SKL-ASSEMBLE-CONTEXT
= bounded Skill-level capability to request/use Context assembly

UPOS-005
= canonical retrieval/resolution/budget/freshness/memory/assembly semantics
```

## 7. Workflow Stage interface

A Stage can declare Context needs.

UPOS-004 owns stage timing/order.

UPOS-005 resolves what Context the bounded Stage consumer receives.

## 8. Rework Context

On rework/re-review, original Bundle MUST be revalidated against:

```text
new finding
changed artifact
changed canonical source
new decision
new scope
new Change Class/Profile/route
permission changes
```

Reuse is allowed only if validity remains demonstrated.

## 9. Human decision package

When a Workflow requires Human Governance, Module 05 MAY assemble focused Context containing:

- decision needed;
- scope;
- canonical sources;
- options/proposals;
- evidence;
- risks;
- conflicts/unknowns;
- affected artifacts;
- prior decisions.

Human authority remains external.

## 10. No context dumping

`all docs → all agents` is an anti-pattern.

Assembly SHOULD terminate when minimum sufficient context is reached.
