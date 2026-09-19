# UPOS-003 — Skills System

**ID:** UPOS-03-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, frozen master design source


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-003 defines how reusable capabilities are represented, governed, versioned, discovered, evaluated, composed, and evolved inside the Universal Project Operating System.

The module answers:

> What is a reusable capability inside U-POS, how is it formally defined, versioned, evaluated, combined, evolved, and used by agents without becoming an Agent Role or Workflow?

## 1. Fundamental model

```text
ROLE / AGENT
= WHO is organizationally responsible

SKILL
= reusable bounded capability / procedure

WORKFLOW
= WHEN, WHY and IN WHAT ORDER
  roles and skills participate

POLICY
= what is allowed / required / forbidden

CONTEXT
= authoritative information provided to execution

TOOL
= technical capability used to act
```

These concepts MUST NOT be used interchangeably.

## 2. Skill identity model

```text
SKILL DEFINITION
= versioned canonical reusable procedure contract

SKILL IMPLEMENTATION
= executable/provider/tool-specific realization
  if/when such layer exists

SKILL INVOCATION
= one bounded execution/use of a Skill
  inside an Agent Run / Workflow

SKILL RESULT
= attributable output of that invocation
```

A Skill Definition is normative. A future Skill Implementation is not allowed to silently redefine it.

## 3. Module 03 owns

- Skill definition and identity;
- Skill Contract;
- Skill taxonomy/categories;
- reusable procedure semantics;
- inputs/outputs;
- preconditions and meaningful postconditions;
- source-class requirements;
- context/tool/permission interface requirements;
- procedural invariants;
- skill-level quality criteria;
- skill-specific failure modes and escalation triggers;
- applicable-role interface;
- applicability constraints;
- dependencies and composition;
- invocation semantics at contract level;
- registry/discovery;
- lifecycle/versioning/compatibility/deprecation/supersession;
- skill evaluation semantics;
- Skill evolution interface;
- universal reusable Skill catalog;
- Module 03 cross-module interfaces;
- Module 03 source traceability.

## 4. Module 03 does not own

```text
Role / authority / SoD / handoff              → UPOS-002
Workflow orchestration / C0-C5 / routing      → UPOS-004
Context retrieval / memory / budget           → UPOS-005
Git branch / commit / PR / merge policy       → UPOS-006
Review/QA evidence and gate verdict semantics → UPOS-007
Telemetry / traces / metrics / dashboard      → UPOS-008
Learning detection/promotion                  → UPOS-009 + UPOS-01
Permissions / secrets / production            → UPOS-010
Project paths / providers / overrides          → UPOS-011
Canonical project knowledge governance         → UPOS-01
```

Module 03 MAY define interface requirements toward these owners. It MUST NOT privately redefine their semantics.

## 5. Central invariant

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

A Role may be capable of invoking a Skill but still lack authority to use its result to decide a specific project fact.

Authority remains owned by UPOS-002.

## 6. Knowledge invariant

Skill output does not become canonical truth merely because the Skill completed successfully.

```text
Skill Result
→ epistemic class / evidence / proposal / finding / candidate
→ UPOS-01 Knowledge Lifecycle
→ explicit validation/promotion where applicable
```

## 7. Read order

1. `SKILLS_OPERATING_MODEL.md`
2. `SKILL_CONTRACT_STANDARD.md`
3. `SKILL_TAXONOMY.md`
4. `SKILL_REGISTRY_STANDARD.md`
5. `SKILL_LIFECYCLE.md`
6. `SKILL_VERSIONING.md`
7. `SKILL_DEPENDENCY_AND_COMPOSITION.md`
8. `SKILL_EVALUATION_STANDARD.md`
9. `SKILL_EVOLUTION_INTERFACE.md`
10. `CROSS_MODULE_INTERFACES.md`
11. relevant `skills/*.md`
12. `MODULE_03_TRACEABILITY.md`

## 8. Upstream dependencies

UPOS-003 consumes:

- UPOS-01 Documentation System;
- Project Source-of-Truth Model;
- Project Knowledge Lifecycle Model;
- frozen UPOS-002 Agent Organization v1.0.

It references these systems and does not duplicate their ownership.
