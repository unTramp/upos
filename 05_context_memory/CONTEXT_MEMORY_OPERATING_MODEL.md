# Context & Memory Operating Model

**ID:** UPOS-05-CMO-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md, CONTEXT_BUNDLE_STANDARD.md


## 1. Governing principle

UPOS-005 is an execution-context system, not a knowledge-authority system.

It consumes governed knowledge and evidence, assembles bounded Context, and may retain noncanonical execution Memory.

## 2. Knowledge vs Context vs Memory

### Knowledge

Knowledge is governed under UPOS-01.

Module 05 may reference and represent Knowledge but cannot promote, demote, supersede, or re-own it.

### Context

Context is a consumer-specific selection.

The same canonical project may correctly produce different Context Views for Product, Architecture, Implementer, Reviewer, QA, Merge Controller, or Human decision-maker.

### Memory

Memory supports execution continuity.

Persistence duration does not create truth.

A persisted Task note remains noncanonical until separately governed.

## 3. Context is not a universal blob

Context MUST be bounded by:

```text
project
Task
Workflow Instance
Stage
Role
Agent Run
Skill Invocation where applicable
purpose
Change Class / concern implications
permission/security constraints
independence requirements
```

## 4. Context Request → Bundle

```text
Context Requirement
→ concrete Context Request
→ canonical source resolution
→ candidate retrieval
→ eligibility gate
→ relevance/priority
→ representation/budget
→ Context Manifest
→ immutable Context Bundle
```

## 5. Minimum sufficient context

The system SHOULD stop adding information when the bounded consumer has sufficient authoritative context to satisfy its contract safely.

More context is not automatically better.

## 6. Context policy version

Every production Context Request/Bundle MUST reference:

```text
context_policy_ref
context_policy_version
```

This explains why the same source universe can produce different valid bundles under different governed Context policies.

Context policy version is distinct from source versions and Bundle identity.

## 7. Determinism / explainability

Given the same:

```text
Task scope
Workflow/Stage
Role
Skill
source versions
policies
permissions
context policy version
```

assembly SHOULD be explainable and substantially reproducible.

Byte-identical retrieval is not required when a provider is nondeterministic.

Every material inclusion/exclusion/summary decision MUST remain justifiable.

## 8. No hidden learning

Private memory or repeated context patterns MUST NOT silently change policy, Skills, Workflows, or project truth.

Systemic finding flow:

```text
evidence
→ Learning Candidate
→ UPOS-009
→ UPOS-01 governance
→ proposed change to owned artifact
```

## 9. Provider independence

UPOS-005 Context semantics are provider-, model-, search-, storage-, and repository-platform independent.

Context semantics are independent from model, search engine, vector database, storage engine, repository host, or document platform.

Concrete bindings remain UPOS-011/runtime.
