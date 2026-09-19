# Migration from Universal Design System Standard Pack v1

**ID:** DOC-MIG-001  
**Type:** PLAN  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance + Design System  
**Version:** 1.0.0  
**Lifetime:** TEMPORARY  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Migration completed  
**Supersedes:** —  
**Related:** —


# Purpose

Reconcile the earlier Design System-only package into the full Universal Project Documentation System.

---

# 1. Keep in Design System

```text
Design System Operating Model
Design Handoff Standard
UI Kit Web Specification
Design System Registry Schema
Component Spec Template
Pattern Spec Template
Page Grammar Spec Template
```

---

# 2. Split

Old:

```text
PROJECT_DESIGN_CONSTITUTION
```

New:

```text
05_ux/UX_CONSTITUTION
06_design_system/DESIGN_SYSTEM_PROFILE
```

Reason:

Experience laws and visual system have different ownership/lifetimes.

---

# 3. Move out of Design System

```text
CONTENT_DESIGN_GUIDE
→ 05_ux/

SCREEN_SPEC
→ 04_product_specs/

FLOW_SPEC
→ 04_product_specs/ / 05_ux/

VISUAL_QA_REPORT
→ 11_quality_testing/

DESIGN_RFC
→ 14_decisions/

CURRENT_UI_CHANGE_PLAN
→ 15_plans/

UI_PR_CHECKLIST
→ 16_onboarding/
```

---

# 4. Add

```text
DDR template
Design System README template
Design System Documentation Integration
Document Manifest Schema
Docs-as-Code Standard
Project Documentation Catalog
Project Documentation Profiles
review/freshness metadata
traceability metadata
Open Questions section
```

---

# 5. Lifecycle correction

Do not use Design System object status as document status.

Example:

```text
Document status: ACTIVE
Object lifecycle: IMPLEMENTED
```

---

# 6. Registry upgrade

Upgrade Design System Registry to v1.1:

- review metadata;
- freshness;
- traceability;
- canonical relationships;
- parity.

---

# 7. Completion criteria

Migration is complete when:

```text
[ ] Project Documentation Operating Model adopted
[ ] DS module contains only DS-owned truth
[ ] UX Constitution separated from visual DS Profile
[ ] temporary UI plans moved to Plans
[ ] visual QA moved to Quality
[ ] design RFC/DDR moved to Decisions
[ ] DS Registry uses v1.1 schema
[ ] docs index/source-of-truth map updated
```
