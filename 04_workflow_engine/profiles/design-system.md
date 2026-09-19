# Workflow Profile — DESIGN_SYSTEM

**ID:** WFP-DESIGN-SYSTEM  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DESIGN-SYSTEM`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DESIGN_SYSTEM`

## Purpose

Apply `DESIGN_SYSTEM`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR

## Dependencies

none

## Conflicts

none

## Risk implications

No automatic class floor. Large shared migration may drive C3; durable architecture/security impacts classify separately.

## Added / Required Role references

- Design System
- UX
- Reviewer
- QA
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DESIGN-SYSTEM:REGISTRY-REUSE-EXTEND-CREATE-DECISION` — registry/reuse-extend-create decision checkpoint by Design System owner
- `stage_id: WFP-DESIGN-SYSTEM:COMPONENT-PATTERN-CONTRACT-CHECKPOINT` — component/pattern contract checkpoint
- `stage_id: WFP-DESIGN-SYSTEM:VISUAL-QA-DOCUMENTATION-DEPRECATION-CHECKPOINT` — visual QA/documentation/deprecation checkpoint

## External gate references

- Design System review reference
- visual/accessibility evidence reference where required

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- shared component migration expands breadth
- new reusable primitive/pattern affects multiple surfaces

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
