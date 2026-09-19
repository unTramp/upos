# Workflow Profile — DATABASE_MIGRATION

**ID:** WFP-DATABASE-MIGRATION  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DATABASE-MIGRATION`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DATABASE_MIGRATION`

## Purpose

Apply `DATABASE_MIGRATION`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

Migration concern normally increases process depth. Destructive/production/irreversible data migration is C5.

## Added / Required Role references

- Architecture
- Domain
- Database/DevOps specialist where project defines it
- Implementer
- QA
- Security when relevant

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DATABASE-MIGRATION:DATA-IMPACT-CHECKPOINT` — data-impact checkpoint
- `stage_id: WFP-DATABASE-MIGRATION:MIGRATION-COMPATIBILITY-PLAN` — migration/compatibility plan
- `stage_id: WFP-DATABASE-MIGRATION:BACKUP-RECOVERY-STRATEGY-REFERENCE` — backup/recovery strategy reference
- `stage_id: WFP-DATABASE-MIGRATION:MIGRATION-IMPLEMENTATION-STAGE-BY-EXTERNAL` — migration implementation stage by external engineering mechanics
- `stage_id: WFP-DATABASE-MIGRATION:VERIFICATION` — verification
- `stage_id: WFP-DATABASE-MIGRATION:ROLLBACK-FORWARD-FIX-CHECKPOINT` — rollback/forward-fix checkpoint

## External gate references

- backup/recovery evidence reference
- migration verification reference
- human approval reference according to class

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- destructive data operation
- production migration
- irreversible transformation
- unexpected compatibility/data-loss risk

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
