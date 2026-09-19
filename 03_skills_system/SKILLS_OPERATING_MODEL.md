# Skills Operating Model

**ID:** UPOS-03-SOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SKILL_CONTRACT_STANDARD.md, CROSS_MODULE_INTERFACES.md


## 1. Definition

A **Skill** is:

> a versioned reusable bounded procedure/capability that transforms defined inputs into defined outputs under explicit preconditions, constraints, quality criteria, and failure/escalation rules.

A production Skill MUST be reusable beyond one single task instance and MUST have semantic value beyond simply wrapping one tool command.

## 2. A Skill is not

A Skill is not:

- a Role;
- an Agent persona;
- a Workflow;
- a Task;
- a Policy;
- a Tool;
- a prompt fragment;
- an arbitrary checklist;
- a hidden multi-role process;
- a substitute for canonical project knowledge.

## 3. Skill disposition classes

UPOS-003 defines two normative Skill disposition classes for the v1 universal library.

### CANONICAL_UNIVERSAL_SKILL

A reusable bounded Skill whose core procedural semantics are fully owned by UPOS-003 and are broadly project-independent.

This classification means:

- the reusable procedure can be defined completely inside Module 03;
- correct execution does not depend on another U-POS module owning a central part of the procedure's semantic truth;
- the Skill may still consume external authoritative project context, policies, tools, or permissions through interfaces.

### INTERFACE_SKILL

A reusable bounded Skill owned as a Skill Definition by UPOS-003, but whose correct execution depends on authoritative semantics provided by another U-POS module through an explicit interface.

Examples include:

```text
classify-change
→ INTERFACE_SKILL
because classification/routing semantics belong to UPOS-004

assemble-context
→ INTERFACE_SKILL
because retrieval/budget/memory semantics belong to UPOS-005

create-atomic-commit
→ INTERFACE_SKILL
because Git/commit policy belongs to UPOS-006

review-diff / qa-validation
→ INTERFACE_SKILL
because evidence/verdict/quality semantics belong to UPOS-007

capture-learning
→ INTERFACE_SKILL
because systemic learning/promotion belongs to UPOS-009 + UPOS-01
```

`INTERFACE_SKILL` is classification/disposition metadata only.

```text
INTERFACE_SKILL
!= lifecycle status
!= lower-quality Skill
!= temporary Skill
!= authority delegation
```

A Skill's disposition MUST NOT be used to infer organizational authority, maturity, lifecycle state, or execution priority.

## 5. Boundedness

A Skill MUST have a bounded purpose.

A Skill becomes suspect when it:

- coordinates multiple organizational roles;
- silently decides workflow order;
- embeds broad project policy;
- owns a whole feature lifecycle;
- absorbs multiple unrelated outputs;
- requires unrelated authorities to complete.

Example:

```text
implement-change
= bounded execution capability against an approved Change Plan segment

build-entire-feature
= likely hidden Workflow / mega-skill and SHOULD be rejected or split
```

## 5. Reuse

Skills SHOULD be reusable across projects when the underlying capability is universal.

Project-specific details MUST enter through:

- Source Classes;
- Context interfaces;
- Tool interfaces;
- Permission interfaces;
- project/provider bindings owned by UPOS-011.

## 6. Skill invocation

A Skill Invocation is a bounded use of one Skill Definition within an Agent Run/Workflow.

A Skill Invocation MUST be attributable to:

- Skill ID;
- Skill version;
- invoking Role/Agent Run;
- task/work item;
- input/context references;
- produced Skill Result.

Exact runtime state/event representation is deferred to UPOS-004/08 and the cross-cutting machine-readable schemas layer.

## 7. Skill result

A Skill Result MUST preserve the output class required by its contract.

Typical classes include:

```text
ANALYSIS
PROPOSAL
PLAN
DECISION_RECORD_DRAFT
IMPLEMENTATION_CHANGE
TEST_CHANGE
REVIEW_FINDING
QA_OBSERVATION
READINESS_ASSESSMENT
DOCUMENTATION_CHANGE
LEARNING_CANDIDATE
RELEASE_PREPARATION
INCIDENT_ANALYSIS
```

A result class does not imply canonicality.

## 8. Authority separation

Applicable Roles describe capability compatibility.

They MUST NOT be interpreted as authority grants.

Example:

```text
Architecture Role may invoke create-adr
Security Role may invoke create-adr
Domain Role may invoke create-adr
```

but authority over the decision scope remains determined by UPOS-002 and UPOS-01 Source-of-Truth ownership.

## 9. Procedure ownership

A Skill MAY own its reusable procedure.

It MUST NOT own full cross-role orchestration.

```text
reproduce-bug         → Skill
write-regression-test → Skill
implement-change      → Skill
review-diff           → Skill
qa-validation         → Skill

Bug Fix sequencing and required gates
→ UPOS-004 Workflow Engine
```

## 10. Tool independence

A Skill MAY require abstract capabilities such as:

```text
repository-read
diff-inspection
test-execution
document-write
search
commit-capable-interface
```

Universal Skill Contracts SHOULD NOT hard-code a model/provider/repository vendor when an abstract capability is sufficient.

## 11. Context boundary

A Skill declares what Source Classes and Context interfaces it requires.

UPOS-003 does not define retrieval ranking, freshness rules, context budgets, or physical project paths.

## 12. Failure behavior

Skill-level failure semantics cover only execution of the bounded capability.

Cross-step retry/recovery sequencing belongs to UPOS-004.

Permission denial belongs to UPOS-010.

Provider/tool failure translation belongs to runtime/adapters.

## 13. Minimalism rule

The Skill library SHOULD remain intentionally small.

A candidate Skill must justify:

- repeatability;
- boundedness;
- reusable semantic procedure;
- meaningful contract;
- independent evaluation value.

Naming an action with a verb is not sufficient reason to create a Skill.
