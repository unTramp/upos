# Workflow Profile — API

**ID:** WFP-API  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-API`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `API`

## Purpose

Apply `API`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

No universal class floor. Breaking external compatibility materially increases risk and may require C3/C4+ depending breadth/ownership.

## Added / Required Role references

- Architecture
- Domain when semantics affected
- Implementer
- Reviewer
- QA
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-ARCHITECTURE (conditional)`
- `SKL-QA-VALIDATION`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-API:CONTRACT-IMPACT-CHECKPOINT` — contract impact checkpoint
- `stage_id: WFP-API:BACKWARD-COMPATIBILITY-VERSIONING-CHECKPOINT` — backward-compatibility/versioning checkpoint
- `stage_id: WFP-API:CONTRACT-INTEGRATION-VALIDATION-CHECKPOINT` — contract/integration validation checkpoint
- `stage_id: WFP-API:CONSUMER-DOCUMENTATION-CHECKPOINT` — consumer/documentation checkpoint

## External gate references

- contract-test/integration evidence reference where defined externally

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- breaking consumer contract discovered
- versioning/compatibility assumption invalidated

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
