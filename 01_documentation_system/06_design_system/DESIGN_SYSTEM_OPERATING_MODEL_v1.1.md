# Design System Operating Model v1.1

**ID:** DS-STD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System  
**Version:** 1.1.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Design-system governance, lifecycle, token, registry, or contribution model changes  
**Supersedes:** —  
**Related:** DS-STD-002, DS-STD-003, DS-STD-004


# 0. Scope boundary

This standard governs reusable visual and interaction language.

It does NOT own:

```text
Product/business truth
Domain lifecycles
Full feature behavior
Global UX Constitution
Content Design
Whole user flows
Visual QA reports
Current migration plans
Decision history
```

Those belong to other project documentation layers.

---

# 1. Canonical design-system hierarchy

```text
FOUNDATION
↓
PRIMITIVE
↓
COMPONENT
↓
PATTERN
↓
PAGE GRAMMAR
```

Screens consume the system but are owned by Product/UX specs.

Flows are Product/UX cross-cutting artifacts, not Design System objects.

A Screen MAY be designated a Design System benchmark, but its canonical screen contract remains outside the Design System module.

---

# 2. Three synchronized truths

For important reusable objects:

```text
VISUAL TRUTH
→ approved board

BEHAVIORAL TRUTH
→ object spec

IMPLEMENTATION TRUTH
→ code + stories/tests
```

For `IMPLEMENTED`:

```text
visualVersion
=
specVersion
=
codeVersion
```

Material drift must be explicit.

---

# 3. Roles

## Product

Owns product value and major UX trade-offs.

## Design System Owner

Owns:

- taxonomy;
- registry;
- lifecycle;
- reusable visual/interaction coherence;
- token governance;
- deprecation.

## Product Design

Owns:

- visual/interaction design intent;
- boards;
- hierarchy;
- states/variants;
- responsive intent.

## UI Engineering

Owns:

- accessible implementation;
- public API;
- performance;
- tests;
- token consumption.

## Domain / Architecture

Owns domain semantics.

## AI agent

Contributor only; must search registry and preserve semantics.

---

# 4. Design-system object lifecycle

```text
EXPERIMENTAL
→ CANDIDATE
→ REVIEW
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ DEPRECATED
→ REMOVED
```

This is not the document lifecycle.

Every object spec therefore SHOULD expose both:

```text
Document status
Object lifecycle status
```

---

# 5. Change classes

## Class 0 — local cosmetic correction

No contract change.

## Class 1 — existing object revision

Update spec/board/tests as needed.

## Class 2 — new reusable object

Requires registry search + spec + accessibility + implementation.

## Class 3 — new Pattern / Page Grammar

Requires Design RFC and benchmark/reference usage.

## Class 4 — project-wide experience/IA direction change

Escalates to UX Constitution / Product governance.

Design System MUST NOT approve a Class-4 product decision alone.

---

# 6. Reuse decision tree

```text
Need UI
│
├─ Same user job?
│   └─ reuse candidate
│
├─ Same hierarchy + interaction?
│   └─ variant/state extension
│
├─ Existing Pattern?
│   └─ reuse
│
├─ Existing Page Grammar?
│   └─ compose with it
│
├─ Feature-local one-off?
│   └─ keep local
│
└─ Recurring reusable job?
    └─ propose new system object
```

---

# 7. Token architecture

Use:

```text
Primitive token
↓
Semantic token
↓
Component token (only when justified)
```

Feature UI SHOULD primarily consume semantic tokens.

Recommended families:

```text
color.*
surface.*
text.*
border.*
action.*
status.*
spacing.*
radius.*
size.*
type.*
shadow.*
motion.*
breakpoint.*
z.*
focus.*
density.*
```

---

# 8. Registry

Canonical metadata:

```text
REGISTRY.json
```

Registry SHOULD drive:

- UI Kit inventory;
- search;
- status;
- version;
- relationships;
- deprecation;
- parity;
- ownership;
- review/freshness;
- traceability links.

Metadata is authored once.

---

# 9. Traceability

Registry MAY link design-system objects to:

```text
requirements
feature specs
UX docs
architecture refs
decision records
tests
telemetry
evidence
screens
```

This is optional for simple objects but valuable in complex systems.

---

# 10. Review metadata

Objects SHOULD support:

```text
lastReviewed
reviewTrigger
freshness
```

Freshness is not lifecycle status.

---

# 11. Versioning

## Major

Breaking object contract.

## Minor

Backward-compatible addition.

## Patch

Non-contract polish/fix.

Registry stores semantic contract version.

---

# 12. Design debt vs permanent exception

## Design debt

Temporary known deviation.

## Approved exception

Intentional permanent scoped exception.

Do not confuse them.

Repeated exceptions may indicate a missing rule/pattern.

---

# 13. Deprecation

```text
Mark DEPRECATED
→ replacement
→ migration notes
→ prevent new use
→ migrate
→ remove
→ preserve historical metadata
```

---

# 14. Required gates

Reusable object reaches `IMPLEMENTED` only when relevant:

```text
[ ] registry entry exists
[ ] visual contract exists
[ ] behavioral contract exists
[ ] code exists
[ ] version parity reconciled
[ ] token use compliant
[ ] states implemented
[ ] environment behavior verified
[ ] accessibility verified
[ ] localization stress verified where applicable
[ ] story/live example exists
[ ] tests pass
[ ] visual QA evidence exists where required
```

Visual QA evidence is stored in Quality, not as canonical DS truth.

---

# 15. Contribution flow

```text
NEED
↓
USER JOB
↓
SEARCH REGISTRY
↓
REUSE / EXTEND / CREATE?
↓
CONCEPT
↓
VISUAL CONTRACT
↓
BEHAVIORAL CONTRACT
↓
IMPLEMENTATION
↓
TESTS
↓
VISUAL QA
↓
ACCESSIBILITY QA
↓
PROMOTION
↓
REGISTRY / UI KIT / CHANGELOG
```

---

# 16. Design RFC

Class 3 changes use:

```text
14_decisions/design/rfcs/
```

After acceptance, a durable Design Decision Record MAY be created.

The Design System module links the decision; it does not own the decision-history folder.

---

# 17. Governance cadence

Per meaningful UI PR:

- reuse;
- token compliance;
- semantics;
- parity;
- accessibility;
- environment behavior.

Milestone audit:

- duplicates;
- hardcoded values;
- deprecated usage;
- debt;
- missing specs/boards/stories;
- registry drift;
- benchmark regressions.

---

# 18. Health measures

Use concrete signals:

```text
objects with board/spec/story
accessibility coverage
visual-regression coverage
deprecated usages
open design debt
duplicate families
hardcoded-token violations
registry/code mismatches
```

No fake aggregate design-system score.

---

# 19. Anti-patterns

Avoid:

- generic Card for every grouping;
- visual-reference architecture;
- code-only design truth;
- Figma-only truth;
- global domain status invented by UI;
- speculative component library detached from product use;
- silently divergent implementation;
- Design System owning UX/content/feature truth.

---

# 20. Final principle

> **The Design System is a governed reusable subsystem of the project documentation architecture, not the project documentation architecture itself.**
