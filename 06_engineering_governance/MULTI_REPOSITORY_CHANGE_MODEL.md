# Multi-Repository Change Model

**ID:** UPOS-06-MRC-001  
**Type:** MULTI-REPOSITORY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

```text
one Task
→ one Engineering Change
→ one or more Repository Change Units
```

One Task is not assumed to equal one repository.

## 2. Unit independence

Each RCU may have:

```text
separate repository_ref
separate workspace_id
separate branch_ref
separate commit history
separate integration_request_ref
separate merge_operation_id
separate integrated_revision_ref
```

They share the parent:

```text
engineering_change_id
task_id
workflow_instance_id
```

## 3. Engineering dependency constraints

Module 06 may declare relationships such as:

```text
RCU-B depends_on RCU-A integrated revision
RCU-C consumes package/revision produced by RCU-A
RCU-D cannot integrate before migration artifact RCU-B
```

These are repository integration constraints.

Overall Workflow ordering remains UPOS-004.

## 4. Merge/integration order

Integration order MUST be explicit when repository artifacts depend on each other.

Module 06 does not own deployment/release sequencing.

## 5. Partial integration

An Engineering Change may be mechanically `PARTIALLY_INTEGRATED` when some required RCUs are integrated and others are not.

This state MUST NOT be interpreted as Workflow completion or release success.

## 6. Cross-repository provenance

Future reconstruction should answer:

- which RCUs implement one Engineering Change;
- which revisions were integrated in each repository;
- their dependency/order relationships;
- whether a later revert/backout affected one or many RCUs.
