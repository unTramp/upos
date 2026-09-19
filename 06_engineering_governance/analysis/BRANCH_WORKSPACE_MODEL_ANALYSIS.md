# Branch / Workspace Model Analysis

**ID:** UPOS-06-AN-004  
**Type:** ANALYSIS / ISOLATION MODEL  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Problem

Frozen source preferred one task → one branch/worktree/sandbox, but universal Module 06 must support:

- multi-repository Tasks;
- multiple Agent Runs;
- direct-to-integration exceptions;
- provider-neutral workspaces;
- explicit writable-state isolation.

## Decision

Isolation boundary is Repository Change Unit + Workspace.

Default:

```text
concurrent writer A → workspace A
concurrent writer B → workspace B
```

Branch is a VCS relationship, not the workspace itself.

## Rejected assumptions

- one Task = one branch;
- branch = workspace;
- every change requires a branch + Integration Request;
- universal GitFlow;
- fixed branch names/prefixes.

## Direct mutation exception

Allowed only via explicit external policy/permission while preserving attribution/gates.

## Lifecycle

Workspace uses:

```text
ALLOCATED → ACTIVE → READ_ONLY → RELEASED
                     ↘ ABANDONED
```

No Workflow/Quality states are reused.
