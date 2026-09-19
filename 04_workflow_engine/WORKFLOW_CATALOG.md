# Workflow Catalog

**ID:** UPOS-04-CAT-001  
**Type:** CATALOG / DISCOVERY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** workflows/*.md, profiles/*.md

## 1. Catalog contract

The Catalog is the canonical discovery/index layer for active and historical Workflow Definitions and Workflow Profiles.

It MUST NOT duplicate full Workflow/Profile contracts.

Explicit `none` means the field is applicable and currently has no value.

`—` means not applicable for that registry entry.

## 2. Base Workflow registry

| workflow_id | name | version | status | purpose | work_type | supported_change_classes | compatible_profiles | required_roles | required_skills | supersedes | replacement | contract_ref |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| `WFL-BUG-FIX` | bug-fix | 1.0.0 | ACTIVE | Orchestrate diagnosis and correction of an observed behavior defect. | `BUG_FIX` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller | SKL-CLASSIFY-CHANGE, SKL-REPRODUCE-BUG, SKL-WRITE-REGRESSION-TEST, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/bug-fix.md` |
| `WFL-DEPENDENCY-UPGRADE` | dependency-upgrade | 1.0.0 | ACTIVE | Orchestrate dependency version/interface change with explicit compatibility and regression consideration. | `DEPENDENCY_UPGRADE` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY | Orchestrator, Implementer, Reviewer, QA, Security when relevant, Merge Controller | SKL-ANALYZE-IMPACT, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-REVIEW-SECURITY (conditional), SKL-ASSESS-MERGE-READINESS | none | none | `workflows/dependency-upgrade.md` |
| `WFL-DOCUMENTATION-CHANGE` | documentation-change | 1.0.0 | ACTIVE | Orchestrate a documentation-primary change against canonical ownership without unnecessary code gates. | `DOCUMENTATION_CHANGE` | C0–C5 | WFP-DOCUMENTATION-IMPACT | Orchestrator, Documentation Guardian, Reviewer as required | SKL-CLASSIFY-CHANGE, SKL-RECONCILE-DOCUMENTATION, SKL-REVIEW-DIFF (when review required) | none | none | `workflows/documentation-change.md` |
| `WFL-FEATURE` | feature | 1.0.0 | ACTIVE | Orchestrate delivery of a new or materially changed capability. | `FEATURE` | C2–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Product, Implementer, Reviewer, QA, Documentation Guardian, Merge Controller | SKL-CREATE-FEATURE-SPEC, SKL-ANALYZE-IMPACT, SKL-CLASSIFY-CHANGE, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-RECONCILE-DOCUMENTATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/feature.md` |
| `WFL-GENERIC-CHANGE` | generic-change | 1.0.0 | ACTIVE | Orchestrate a bounded change that is not better represented by another primary Work Type. | `GENERIC_CHANGE` | C0–C3 by default; C4/C5 only when routing/profile/policy proves compatibility | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, Merge Controller | SKL-CLASSIFY-CHANGE, SKL-CREATE-IMPLEMENTATION-PLAN (C1+ or when needed), SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/generic-change.md` |
| `WFL-HOTFIX` | hotfix | 1.0.0 | ACTIVE | Orchestrate expedited recovery without treating urgency as permission to skip safety. | `HOTFIX` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller, Human approval reference as externally required | SKL-ANALYZE-INCIDENT, SKL-REPRODUCE-BUG (where possible), SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-PREPARE-RELEASE, SKL-ASSESS-MERGE-READINESS, SKL-CAPTURE-LEARNING (follow-up candidate) | none | none | `workflows/hotfix.md` |
| `WFL-REFACTOR` | refactor | 1.0.0 | ACTIVE | Orchestrate structural implementation change intended to preserve externally intended behavior. | `REFACTOR` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller | SKL-ANALYZE-IMPACT, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/refactor.md` |
| `WFL-RELEASE` | release | 1.0.0 | ACTIVE | Orchestrate release of a selected release candidate through required external operational/security/human checkpoints. | `RELEASE` | C2–C5 | WFP-API, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY | Orchestrator, DevOps / SRE or project release specialist, QA, Security when relevant, Human approval reference, Documentation Guardian as relevant | SKL-PREPARE-RELEASE, SKL-QA-VALIDATION, SKL-REVIEW-SECURITY (conditional), SKL-RECONCILE-DOCUMENTATION (conditional) | none | none | `workflows/release.md` |

## 3. Profile registry

| profile_id | concern | version | status | purpose | compatible_work_types | dependencies | conflicts | supersedes | replacement | contract_ref |
|---|---|---:|---|---|---|---|---|---|---|---|
| `WFP-API` | API | 1.0.0 | ACTIVE | Apply `API`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/api.md` |
| `WFP-ARCHITECTURE` | ARCHITECTURE | 1.0.0 | ACTIVE | Apply `ARCHITECTURE`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX | none | none | none | none | `profiles/architecture.md` |
| `WFP-DATABASE-MIGRATION` | DATABASE_MIGRATION | 1.0.0 | ACTIVE | Apply `DATABASE_MIGRATION`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/database-migration.md` |
| `WFP-DESIGN-SYSTEM` | DESIGN_SYSTEM | 1.0.0 | ACTIVE | Apply `DESIGN_SYSTEM`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR | none | none | none | none | `profiles/design-system.md` |
| `WFP-DOCUMENTATION-IMPACT` | DOCUMENTATION_IMPACT | 1.0.0 | ACTIVE | Apply `DOCUMENTATION_IMPACT`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | all base workflows | none | none | none | none | `profiles/documentation-impact.md` |
| `WFP-SECURITY` | SECURITY | 1.0.0 | ACTIVE | Apply `SECURITY`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/security.md` |
| `WFP-UI` | UI | 1.0.0 | ACTIVE | Apply `UI`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, HOTFIX | none | none | none | none | `profiles/ui.md` |

## 4. Discovery semantics

Registry entries support stable identity lookup, lifecycle/status discovery, compatibility discovery, required Role/Skill reference discovery, supersession/replacement discovery, and canonical contract resolution.

Full orchestration semantics remain in the referenced canonical contracts.

## 5. Supersession / replacement

When a Workflow/Profile is deprecated or superseded, the Catalog MUST explicitly identify:

```text
supersedes
replacement
```

Historical entries remain discoverable for provenance.

A blank/missing supersession field is not equivalent to `none`; the registry uses explicit values.
