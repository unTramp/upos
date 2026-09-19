# Workflow Operating Model

**ID:** UPOS-04-WOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CHANGE_CLASSIFICATION_STANDARD.md, ROUTING_STANDARD.md


## 1. Definition

A Workflow Definition is a versioned canonical orchestration contract describing when, why, under what conditions, and in what order organizational Roles and Skill references participate in a class of work.

A Workflow owns orchestration.

It does not own the detailed procedure of a Skill, organizational authority of a Role, or semantics of external gates.

## 2. Why three axes are required

The frozen source contains dedicated examples for:

```text
UI Change
Design System Change
Architecture Change
API Change
Database Migration
Security Change
```

Those concerns are not mutually exclusive.

One feature may be simultaneously:

```text
Feature
+ UI
+ API
+ Database
+ Security
```

Treating each combination as a separate Workflow Definition creates combinatorial explosion and ambiguous routing.

Therefore UPOS-004 normalizes them as:

```text
Primary Work Type → Base Workflow
Cross-cutting impact → Concern Profiles
Risk/impact depth → Change Class
```

## 3. Base Workflow

A Base Workflow expresses the primary intention.

v1 base Work Types:

```text
GENERIC_CHANGE
BUG_FIX
FEATURE
REFACTOR
DEPENDENCY_UPGRADE
DOCUMENTATION_CHANGE
HOTFIX
RELEASE
```

`MICRO` is not a Work Type. It is Change Class C0 and normally resolves through `GENERIC_CHANGE`.

## 4. Concern Profile

A Concern Profile modifies orchestration without replacing the Base Workflow.

v1 profiles:

```text
UI
DESIGN_SYSTEM
ARCHITECTURE
API
DATABASE_MIGRATION
SECURITY
DOCUMENTATION_IMPACT
```

Profiles may:

- add required Role participation references;
- add Skill references;
- add stages/checkpoints;
- add external gate references;
- add reclassification triggers;
- impose conditional risk floors where normative criteria justify them.

Profiles MUST NOT redefine external owners' semantics.

## 5. Resolved Workflow Configuration

A Routing Decision resolves:

```text
task
→ work type
→ concerns
→ change class
→ base workflow
→ compatible profiles
→ required organizational constraints
→ external gates/approvals by reference
```

The result is attributable and reproducible.

## 6. Risk determines process depth

Frozen-source principle:

```text
Risk / impact
!=
diff size
```

Process depth is adjusted by classification/profile/policy.

## 7. No every-agent swarm

Workflow routing MUST choose only Roles/Skills justified by the resolved configuration.

The existence of a Role or Skill in the U-POS catalog is not a reason to run it for every Task.

## 8. No hidden workflow in Skills

Workflow stages reference Skill IDs.

They do not embed Skill procedures.

## 9. No hidden authority in Workflow

Workflow may require participation or approval references.

It cannot create authority a Role does not possess.

## 10. No hidden canonical truth

Workflow status/results do not automatically become canonical project knowledge.

Project truth remains governed by UPOS-01.
