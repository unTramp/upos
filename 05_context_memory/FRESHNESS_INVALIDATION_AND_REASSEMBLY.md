# Freshness, Invalidation & Reassembly

**ID:** UPOS-05-FIR-001  
**Type:** FRESHNESS / INVALIDATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Freshness != canonicality

A source may be:

- authoritative but stale for this execution;
- relevant but superseded;
- historical and valid as history;
- recent but noncanonical/incorrect.

UPOS-005 consumes source lifecycle/status from UPOS-01 and derives execution applicability.

## 2. Freshness assessment

Freshness evaluation may consider:

```text
source lifecycle/status
source version/revision
baseline applicability
time-sensitive TTL supplied by policy
Task/Workflow changes
known canonical revision
upstream artifact replacement
```

Module 05 MUST NOT invent upstream lifecycle status.

## 3. Bundle validity states

Canonical Context Bundle validity states:

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
STALE
INVALIDATED
```

### VALID
Required sources satisfied, no blocking conflict, current for request.

### VALID_WITH_WARNINGS
Required sources satisfied; non-blocking optional/history/representation warning exists.

### INCOMPLETE
One or more required requirements are unsatisfied. Bundle may exist for diagnosis but MUST NOT be presented as fully valid execution context.

### STALE
Previously valid Bundle has detected freshness/assumption change and requires revalidation before continued material use.

### INVALIDATED
Bundle is no longer acceptable for active execution under the request because a material assumption/source/permission/route changed or contamination was discovered.

`BLOCKED` is an assembly/request outcome, not a Bundle content state.

## 4. Invalidation/revalidation triggers

Where applicable:

```text
canonical source version/revision changes
canonical owner changes
source becomes superseded/retired
normative conflict appears
Task scope changes
Workflow reclassification
Workflow rerouting
Stage materially changes
Skill version changes
Role changes
permission/security constraints change
time-sensitive source expires
upstream artifact replaced
material source changes during Agent Run
```

## 5. Reclassification/rerouting interface

Example:

```text
C1 Bug Fix
→ CB-100

database migration discovered
→ UPOS-004 reclassifies/reroutes
→ DATABASE_MIGRATION profile added
→ CB-100 revalidation fails
→ CB-101 assembled
→ CB-101 supersedes CB-100
```

Module 05 reports Context validity/reassembly result.

UPOS-004 decides orchestration response.

## 6. Reassembly

Reassembly creates a new `context_bundle_id`.

It MUST NOT mutate the old consumed Bundle.

## 7. Context Delta

A reassembly MAY include a Context Delta report:

```text
prior_context_bundle_id
new_context_bundle_id
reassembly_reason
changed_requirements
changed_source_versions
reused items
replaced items
removed items
new items
changed exclusions/conflicts
```

Context Delta is an audit/reassembly artifact, not a mutable Context object or new Source of Truth.

## 8. Source changes during an Agent Run

If a material required source changes during execution:

```text
mark Bundle STALE / INVALIDATED as appropriate
→ notify Workflow interface
→ revalidate/reassemble
```

Agent MUST NOT silently finish high-impact execution using invalidated critical Context.

Exact pause/restart/retry action remains UPOS-004.

## 9. Reuse

Before reusing a prior Bundle/Item/Memory:

```text
check project/scope
check source version
check provenance
check freshness
check permissions
check role/independence
check current applicability
```

No blind nearest-memory reuse.
