# Learning Backlog

**ID:** UPOS-09-LBL-001  
**Type:** BACKLOG SEMANTICS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Definition

The Learning Backlog is a governed discovery/projection layer for open learning work.

It may index:

```text
Learning Candidates
Improvement Proposals
Validation Plans/work
Learning Outcome follow-up
owner-resolution blockers
reconsideration triggers
```

## 2. Not project Task backlog

```text
LEARNING BACKLOG != PROJECT TASK BACKLOG
```

Creating a Learning Candidate does not automatically create or prioritize a project Task.

Mapping to project work is owned by Workflow/project-adapter/project governance.

## 3. Backlog item references

The backlog reuses stable IDs of tracked objects. It does not create `learning_backlog_item_id` in v1.

## 4. Ordering

Backlog views MAY sort/filter by explainable dimensions:

```text
priority dimensions
age
owner
risk/severity refs
status
evidence sufficiency
validation readiness
affected module
```

There is no universal hidden composite priority score.

## 5. Rejected/historical visibility

Rejected, duplicate, consolidated and superseded items remain discoverable for provenance and recurrence prevention, but may be excluded from active default views.

## 6. Reconsideration

A rejected item SHOULD record what new evidence/change would justify reconsideration where useful.
