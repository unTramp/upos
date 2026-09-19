# Repository Workspace and Isolation

**ID:** UPOS-06-WSI-001  
**Type:** WORKSPACE / ISOLATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Definition

```text
REPOSITORY WORKSPACE
= isolated writable repository environment assigned to a bounded Repository Change Unit/execution
```

Possible realizations include separate working trees, clones, sandboxes, or remote isolated workspaces.

Concrete realization belongs to UPOS-011/runtime.

## 2. Identity

Every Workspace MUST have stable:

```text
workspace_id
```

## 3. Isolation invariant

```text
two independent concurrent writers
MUST NOT silently share
the same writable workspace
```

If multiple writers must touch one workspace, explicit coordination/serialization MUST make the ownership transition safe and attributable.

Conversational discipline is not sufficient isolation.

## 4. Attribution

Workspace SHOULD be attributable to:

```text
workspace_id
repository_ref
repository_change_unit_id
engineering_change_id
task_id
branch_ref
assigned Role reference
assigned Agent Run reference
lifecycle state
```

Where execution Context attribution is required, Workspace MAY reference the specific upstream:

```text
context_bundle_id
```

supplied to the assigned Role / Agent Run.

UPOS-005 v1.0 defines Context View as a bounded projection but does not introduce a separate global `context_view_id`. Module 06 therefore MUST NOT manufacture one.

Workspace attribution does not define or copy Context isolation/View semantics.

## 5. Lifecycle

```text
ALLOCATED
→ ACTIVE
→ READ_ONLY
→ RELEASED
```

Alternate terminal:

```text
ALLOCATED / ACTIVE / READ_ONLY
→ ABANDONED
```

Semantics:

- `ALLOCATED`: isolated environment reserved but not yet mutating.
- `ACTIVE`: currently writable under declared ownership.
- `READ_ONLY`: retained for inspection/provenance; mutation prohibited.
- `RELEASED`: no longer allocated for active work; retained references remain.
- `ABANDONED`: work stopped without successful integration; provenance retained.

Workspace lifecycle is distinct from Workflow, Agent Run, RCU, and Integration Request lifecycles.

## 6. Ownership transfer

Writable ownership transfer MUST be explicit.

Before transfer:

- current mutation stops;
- current repository state is attributable;
- new owner/Agent Run is declared;
- contamination risk is checked.

## 7. Contamination checks

Workspace validation SHOULD detect:

- unrelated untracked/staged/modified files;
- wrong RCU/Task changes;
- unexpected base/reference changes;
- branch mismatch;
- generated-artifact drift;
- residual state from another writer.

## 8. Completion/abandonment

Workspace cleanup MUST NOT silently delete provenance required to reconstruct commits, Integration Requests, or unresolved change state.
