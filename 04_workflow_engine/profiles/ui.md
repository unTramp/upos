# Workflow Profile — UI

**ID:** WFP-UI  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-UI`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `UI`

## Purpose

Apply `UI`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, HOTFIX

## Dependencies

none

## Conflicts

none

## Risk implications

No automatic class floor. Material user-facing/Product/Accessibility impact may raise classification.

## Added / Required Role references

- UX
- Design System when reusable components/patterns affected
- QA
- Reviewer

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-UI:UX-INTENT-IMPACT-CHECKPOINT-BEFORE` — UX intent/impact checkpoint before implementation when behavior/flow changes
- `stage_id: WFP-UI:VISUAL-ACCESSIBILITY-EXTERNAL-EVIDENCE-CHECKPOINT` — visual/accessibility external evidence checkpoint after implementation
- `stage_id: WFP-UI:UI-FOCUSED-QA-PARTICIPATION` — UI-focused QA participation

## External gate references

- visual evidence reference as defined by Quality/Design tooling
- accessibility gate when externally required

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- unexpected domain/product behavior change
- Design System primitive/pattern change discovered

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.
