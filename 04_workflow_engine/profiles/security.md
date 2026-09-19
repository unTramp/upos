# Workflow Profile — SECURITY

**ID:** WFP-SECURITY  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-SECURITY`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `SECURITY`

## Purpose

Apply `SECURITY`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

Auth/authz/security-boundary/privacy/secrets/protected-action changes are C5 signals. Other security-relevant changes are classified by actual impact.

## Added / Required Role references

- Security
- relevant Architecture/Domain/Product Roles
- Reviewer
- QA

Role authority remains UPOS-002.

## Skill references

- `SKL-REVIEW-SECURITY`
- `SKL-ANALYZE-IMPACT`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-SECURITY:SECURITY-THREAT-IMPACT-CHECKPOINT` — security/threat-impact checkpoint
- `stage_id: WFP-SECURITY:SECURITY-DESIGN-CONSTRAINT-CHECKPOINT-IF` — security design/constraint checkpoint if needed
- `stage_id: WFP-SECURITY:SECURITY-REVIEW-STAGE` — security review stage
- `stage_id: WFP-SECURITY:HUMAN-SECURITY-APPROVAL-REFERENCE-WHERE` — human/security approval reference where required
- `stage_id: WFP-SECURITY:AUDIT-EVIDENCE-REFERENCE-CHECKPOINT` — audit/evidence reference checkpoint

## External gate references

- Security review/veto interface reference
- human approval reference for protected/high-risk action

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- new auth/authz path
- security boundary change
- secret/privacy/retention impact
- protected action discovered

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
