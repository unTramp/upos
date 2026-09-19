# Design System Documentation Integration v1.0

**ID:** DS-STD-004  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System + Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Ownership boundary between Design System and adjacent project documentation changes  
**Supersedes:** —  
**Related:** DOC-STD-001, DS-STD-001, DS-STD-002, DS-STD-003


# Purpose

Resolve the question:

> Where does a UI-related fact belong?

---

# Ownership map

| Fact | Canonical owner |
|---|---|
| Product goal | `01_product/` |
| Domain lifecycle | `02_domain/` |
| Service/data ownership | `03_architecture/` |
| Feature behavior | `04_product_specs/` |
| Screen job / whole-screen experience | `04_product_specs/` + `05_ux/` |
| User flow | `04_product_specs/` / `05_ux/` |
| Navigation semantics | `05_ux/` |
| Product language / CTA grammar | `05_ux/CONTENT_DESIGN.md` |
| Reusable visual token | `06_design_system/` |
| Primitive/component | `06_design_system/` |
| Reusable interaction pattern | `06_design_system/` |
| Page Grammar | `06_design_system/` |
| Visual board for DS object | `06_design_system/boards/` |
| Why a pattern was chosen | `14_decisions/design/` |
| Visual QA result | `11_quality_testing/` |
| Visual regression policy | `11_quality_testing/` |
| Current redesign/migration sequence | `15_plans/` |
| PR workflow/checklist | `16_onboarding/` |

---

# Examples

## Phrase discovery

```text
Feature behavior
→ 04_product_specs/phrase-discovery/

Navigation / educational flow
→ 05_ux/

PhraseCard reusable contract
→ 06_design_system/components/phrase-card/

Why mobile details use Bottom Sheet
→ 14_decisions/design/DDR-...

Visual QA after implementation
→ 11_quality_testing/reports/
```

## Dashboard

```text
Metric definition
→ 12_analytics/

Dashboard feature behavior
→ 04_product_specs/

Dashboard IA
→ 05_ux/

MetricCard
→ 06_design_system/

Current dashboard redesign sequence
→ 15_plans/
```

---

# Rule

> **A Design System object may reference upstream Product/UX contracts, but it must not silently absorb their ownership.**
