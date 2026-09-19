# Workflow Lifecycle and Versioning

**ID:** UPOS-04-LFV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Workflow Definition lifecycle

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

This lifecycle is separate from Workflow Instance execution state.

## 2. Deprecation

Deprecated Definitions SHOULD NOT be selected for new routing when a supported replacement exists.

Historical executions remain attributable to their original Workflow version.

## 3. Versioning principle

Workflow Definition version MUST change when required gates, required stage sequence, routing applicability, mandatory profiles/roles/skills, terminal semantics, or failure/reclassification behavior changes materially.

## 4. Semantic versioning convention

### MAJOR
Breaking orchestration compatibility:

- removed/reordered mandatory stage in a way that changes consumers;
- incompatible entry/exit conditions;
- new mandatory gate/approval invalidating old assumptions;
- changed routing/work-type semantics;
- incompatible terminal result meaning.

### MINOR
Backward-compatible orchestration expansion:

- optional concern support;
- optional stage;
- compatible new Skill/Role reference;
- additional non-breaking validation/checkpoint.

### PATCH
Editorial/non-semantic correction only.

## 5. Supersession

Registry/catalog MUST point from deprecated Workflow/Profile to its replacement when one exists.

## 6. Instance pinning

A Workflow Instance is pinned to a resolved Workflow/Profile version set.

A material Definition change does not mutate an in-flight instance silently.

Migration/rerouting requires an explicit decision with provenance.
