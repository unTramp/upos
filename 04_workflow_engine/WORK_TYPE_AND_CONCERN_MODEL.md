# Work Type and Concern Model

**ID:** UPOS-04-WTC-001  
**Type:** TAXONOMY / ROUTING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Work Type

Work Type represents the primary intention.

Canonical v1 Work Types:

| Work Type | Meaning | Base Workflow |
|---|---|---|
| `GENERIC_CHANGE` | bounded change not better classified below | `WFL-GENERIC-CHANGE` |
| `BUG_FIX` | correct observed behavior defect | `WFL-BUG-FIX` |
| `FEATURE` | add/change intended capability | `WFL-FEATURE` |
| `REFACTOR` | change internal structure while preserving intended behavior | `WFL-REFACTOR` |
| `DEPENDENCY_UPGRADE` | update external/internal dependency version/interface | `WFL-DEPENDENCY-UPGRADE` |
| `DOCUMENTATION_CHANGE` | documentation is the primary deliverable | `WFL-DOCUMENTATION-CHANGE` |
| `HOTFIX` | expedited recovery-oriented change | `WFL-HOTFIX` |
| `RELEASE` | orchestrate release of an already selected release candidate | `WFL-RELEASE` |

## 2. Concern

Concern is orthogonal to primary intention.

Canonical v1 concerns:

| Concern | Profile |
|---|---|
| `UI` | `WFP-UI` |
| `DESIGN_SYSTEM` | `WFP-DESIGN-SYSTEM` |
| `ARCHITECTURE` | `WFP-ARCHITECTURE` |
| `API` | `WFP-API` |
| `DATABASE_MIGRATION` | `WFP-DATABASE-MIGRATION` |
| `SECURITY` | `WFP-SECURITY` |
| `DOCUMENTATION_IMPACT` | `WFP-DOCUMENTATION-IMPACT` |

## 3. Why UI/API/DB/Security are concerns

They frequently coexist.

Example:

```text
Work Type: FEATURE
Concerns:
- UI
- API
- DATABASE_MIGRATION
- SECURITY
Change Class: C5
```

The resolved configuration is one Feature Workflow plus four compatible concern profiles, not four competing workflows.

## 4. Source-workflow normalization

Frozen examples are preserved as follows:

```text
Micro Change         → GENERIC_CHANGE + C0
Bug Fix              → BUG_FIX
New Feature          → FEATURE
UI Change            → base work type + UI profile
Design System Change → base work type + DESIGN_SYSTEM profile
Architecture Change  → base work type + ARCHITECTURE profile; durable architecture change => C4
API Change           → base work type + API profile
Database Migration   → base work type + DATABASE_MIGRATION profile
Security Change      → base work type + SECURITY profile
Refactor             → REFACTOR
Dependency Upgrade   → DEPENDENCY_UPGRADE
Hotfix               → HOTFIX
Documentation Change → DOCUMENTATION_CHANGE
Release              → RELEASE
```

## 5. Primary-intention rule

A Task MUST have one primary Work Type for routing.

A Task MAY have multiple Concerns.

If two independent primary intentions exist, the Task SHOULD be decomposed unless doing so would create an invalid intermediate system.

## 6. Concern detection

Concern detection is an orchestration classification.

It does not transfer authority to UPOS-004.

Concern-specific meaning remains with the relevant owner module/Role.
