# Integration Request Standard

**ID:** UPOS-06-IRS-001  
**Type:** INTEGRATION REQUEST CONTRACT  
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
INTEGRATION REQUEST
= provider-neutral coherent repository change container
  for review, checks, approvals, and integration references
```

It may contain multiple related atomic commits.

Provider-specific review-container names/APIs belong to UPOS-011.

## 2. Commit vs Integration Request

```text
Commit
= one coherent logical engineering change unit

Integration Request
= one coherent deliverable/intention
  that may contain multiple related Commits
```

No universal rule requires one Integration Request = one Commit.

One Integration Request MUST NOT mix unrelated feature/fix/refactor/cleanup/dependency work without one justified common intention.

## 3. Identity/reference

Use:

```text
integration_request_ref
```

as the universal reference.

Do not manufacture a duplicate Module-06 identifier unless the underlying provider/runtime cannot supply a stable reference.

## 4. Contract

A governed Integration Request SHOULD declare/reference:

```text
integration_request_ref
repository_change_unit_id
engineering_change_id

task_id
routing_decision_id
workflow_instance_id
stage_id

purpose
scope
non_scope

repository_ref
base_revision_ref
head_revision_ref
change_branch_ref
target/integration reference

commit_set

Change Class reference
Concern/Profile references
Implementation Plan reference where applicable

implementation Context Bundle ID reference(s) (`context_bundle_id`)
review Context Bundle ID reference(s) (`context_bundle_id`) when review has occurred

check_ref values

review_result_ref
qa_result_ref
security_ref
documentation_ref

rollback/revert considerations
known limitations

dependency/order constraints
superseded_integration_request_ref
```

Quality/Security semantics remain external.

## 5. Cohesion / size

One Integration Request = one reviewable intention.

Raw LOC is not the primary validity metric.

A large coherent migration or generated change may be valid; unrelated combined intentions are not.

If too broad:

```text
identify independent intentions
→ split safely
→ preserve dependency order
```

Do not split if doing so creates an unsafe/invalid intermediate state.

## 6. Review artifact

Module 06 provides a reconstructible review artifact consisting of at least:

```text
repository_ref
base_revision_ref
head_revision_ref
commit_set
diff/change reference where available
engineering provenance
```

This artifact is distinct from Reviewer Context.

UPOS-005 supplies Reviewer Context through a Reviewer-scoped Context Request / Context Bundle.

There is no Module-06 `context_view_id`.

Review execution provenance SHOULD reference the exact Reviewer `context_bundle_id` actually consumed where available.

Critical invariant consumed from UPOS-005:

```text
producer context
!= reviewer authoritative context
```

The producer's implementation Context Bundle MUST NOT automatically become the Reviewer Context Bundle.

Module 06 does not define Reviewer Context contents, independence policy, freshness, or validity; it records the upstream Bundle reference and exact repository artifact reviewed.


## 7. Context reuse / artifact-change interface

If an Integration Request's head/base revision or relevant repository artifact materially changes and a prior Context Bundle is intended for reuse:

```text
repository artifact changes
→ UPOS-006 reports exact artifact change
→ UPOS-005 revalidates the prior Context Bundle
→ reassembly, when required, produces a new context_bundle_id
```

The prior sealed/consumed Bundle remains immutable historical provenance.

Module 06 MUST NOT label the Bundle `STALE` or `INVALIDATED` itself.

## 8. Evidence container boundary

An Integration Request may contain references to:

```text
tests_ref
review_ref
qa_ref
security_ref
docs_ref
```

It does not define evidence sufficiency or verdict semantics.

## 9. ready_for_review

`ready_for_review` MAY be a producer-intent flag.

It means:

> producer asserts the repository artifact is ready to enter review.

It does NOT mean Quality approval.

## 10. Stacked/dependent requests

Dependent Integration Requests are allowed when safe decomposition exists.

Each MUST explicitly declare dependency/order relationships.

## 11. Documentation in same request

Documentation changes may share an Integration Request when they are part of the same coherent intention.

Canonical documentation ownership remains UPOS-01.
