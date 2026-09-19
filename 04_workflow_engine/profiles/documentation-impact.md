# Workflow Profile — DOCUMENTATION_IMPACT

**ID:** WFP-DOCUMENTATION-IMPACT  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DOCUMENTATION-IMPACT`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DOCUMENTATION_IMPACT`

## Purpose

Apply `DOCUMENTATION_IMPACT`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

all base workflows

## Dependencies

none

## Conflicts

none

## Risk implications

Does not independently raise Change Class; documents the fact that durable contract/documentation reconciliation is required.

## Added / Required Role references

- Documentation Guardian
- affected canonical owner Role

Role authority remains UPOS-002.

## Skill references

- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DOCUMENTATION-IMPACT:DOCUMENTATION-IMPACT-CHECKPOINT` — documentation impact checkpoint
- `stage_id: WFP-DOCUMENTATION-IMPACT:CANONICAL-OWNER-SOURCE-RECONCILIATION` — canonical owner/source reconciliation
- `stage_id: WFP-DOCUMENTATION-IMPACT:DOCUMENTATION-UPDATE-REVIEW-BEFORE-COMPLETION` — documentation update/review before completion as required

## External gate references

- documentation consistency/reference gate as defined by UPOS-01/07

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- implementation changes a documented contract
- decision/spec/source is superseded or becomes stale

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
