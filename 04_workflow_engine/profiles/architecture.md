# Workflow Profile — ARCHITECTURE

**ID:** WFP-ARCHITECTURE  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-ARCHITECTURE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `ARCHITECTURE`

## Purpose

Apply `ARCHITECTURE`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX

## Dependencies

none

## Conflicts

none

## Risk implications

Durable architecture boundary/ownership/topology change requires C4 minimum. High-risk security/production effects may drive C5.

## Added / Required Role references

- Architecture
- relevant Product/Domain/Security Roles
- Reviewer
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-CREATE-RFC`
- `SKL-REVIEW-ARCHITECTURE`
- `SKL-CREATE-ADR`
- `SKL-ANALYZE-IMPACT`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-ARCHITECTURE:RFC-ALTERNATIVES-CHECKPOINT-FOR-DURABLE` — RFC/alternatives checkpoint for durable architectural decision
- `stage_id: WFP-ARCHITECTURE:ARCHITECTURE-REVIEW` — Architecture review
- `stage_id: WFP-ARCHITECTURE:HUMAN-DECISION-APPROVAL-REFERENCE-WHERE` — human decision/approval reference where required
- `stage_id: WFP-ARCHITECTURE:ADR-AFTER-VALID-DECISION-AUTHORITY` — ADR after valid decision authority
- `stage_id: WFP-ARCHITECTURE:MIGRATION-IMPLEMENTATION-PLANNING-CHECKPOINT` — migration/implementation planning checkpoint

## External gate references

- Architecture review reference
- human approval reference for C4+ according to policy
- documentation reconciliation

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- new service/storage owner/routing/multitenancy/eventing boundary
- hidden durable decision found during implementation

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
