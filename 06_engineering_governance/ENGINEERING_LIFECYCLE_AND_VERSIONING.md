# Engineering Lifecycle and Versioning

**ID:** UPOS-06-LCV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Distinct lifecycles

Module 06 maintains only repository-mechanical lifecycles.

They MUST remain distinct from Task, Workflow, Agent Run, Quality, release, deployment, and product lifecycles.

## 2. Engineering Change lifecycle

```text
ACTIVE
→ PARTIALLY_INTEGRATED   # only for multi-RCU changes where some required units are integrated
→ INTEGRATED

ACTIVE / PARTIALLY_INTEGRATED
→ ABANDONED

ACTIVE / PARTIALLY_INTEGRATED
→ SUPERSEDED
```

`INTEGRATED` means required repository integration contract is satisfied, not Workflow/Quality/release completion.

## 3. Repository Change Unit lifecycle

Defined in `REPOSITORY_CHANGE_UNIT_STANDARD.md`:

```text
PREPARED
ACTIVE
INTEGRATION_REQUEST_OPEN
INTEGRATED
ABANDONED
SUPERSEDED
```

## 4. Workspace lifecycle

```text
ALLOCATED
ACTIVE
READ_ONLY
RELEASED
ABANDONED
```

## 5. Integration Request lifecycle

```text
DRAFT
OPEN
CLOSED
MERGED
SUPERSEDED
```

No Quality verdict states are used.

## 6. Engineering Governance document versioning

Material changes to:

- entity identity semantics;
- atomic commit invariants;
- workspace isolation;
- Integration Request contract/lifecycle;
- collision/failure taxonomy semantics;
- merge/revert mechanics;
- provenance requirements;
- cross-module ownership boundaries

require version review.

## 7. Module status

UPOS-006 v1.0 completed its narrow reconciliation against FROZEN UPOS-005 Context & Memory v1.0.

```text
Status: ACTIVE
Canonical baseline: FROZEN v1.0
UPOS-005 interface reconciliation: COMPLETE
```

Future semantic changes require normal governed version review under UPOS-01.


## 8. Supersession

Future versions MUST preserve discoverability of superseded Module-06 standards and artifact semantics according to UPOS-01.
