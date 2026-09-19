# <Project> Design System

## Purpose

This directory contains the governed reusable visual and interaction system.

## Read first

1. `DESIGN_SYSTEM_OPERATING_MODEL.md`
2. `DESIGN_HANDOFF_STANDARD.md`
3. `REGISTRY.json`
4. `DESIGN_SYSTEM_PROFILE.md`
5. UI Kit Web

## Authority

- Product/domain truth lives outside this module.
- UX navigation/content truth lives in `05_ux/`.
- Reusable UI contracts live here.
- Current migration plans live in `15_plans/`.
- Visual QA reports live in `11_quality_testing/`.
- Design decisions live in `14_decisions/`.

## Before creating UI

1. Search Registry.
2. Search feature-local implementation.
3. Check Patterns.
4. Check Page Grammars.
5. Reuse if user job + hierarchy + interaction match.
6. Extend only with an explicit variant/state contract.
7. Create a new reusable object only when justified.

## Object lifecycle

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

## Canonical metadata

`REGISTRY.json`

## UI Kit

`<url / command>`

## Tokens

`<path>`

## Changelog

`CHANGELOG.md`
