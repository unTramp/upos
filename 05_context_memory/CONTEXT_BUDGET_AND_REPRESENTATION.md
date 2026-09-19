# Context Budget & Representation

**ID:** UPOS-05-CBR-001  
**Type:** BUDGET / REPRESENTATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Context Budget

Context Budget is the bounded capacity available for one Context View/Bundle.

Budget semantics may consider:

```text
consumer Role
Stage
Skill
Task complexity
Change Class
required source size
optional evidence
model/provider capacity interface
cost/latency constraints
```

Concrete provider token limits/costs belong to UPOS-011/008.

## 2. Minimum sufficient principle

```text
maximum available context != optimal context
```

Budget optimization MUST prefer the smallest set that safely satisfies required information needs.

## 3. Required material is non-droppable

A required authoritative source/constraint MUST NOT be silently omitted because of budget.

When it cannot fit safely:

```text
safe summary/excerpt if permitted
incremental/staged retrieval
split execution
request larger-capability provider through external adapter
block / emit BUDGET_INSUFFICIENT
```

Arbitrary tail truncation is prohibited.

## 4. Priority levels

Priority is separate from requiredness.

Canonical v1 priority labels:

```text
P0_CONSTRAINT
= mandatory authoritative constraints/invariants

P1_DIRECT
= direct Task/Stage/decision context

P2_SUPPORTING
= supporting evidence/implementation/tests needed for the purpose

P3_HISTORICAL
= relevant historical/background context

P4_ENRICHMENT
= optional enrichment
```

Budget pressure removes/condenses the lowest-value optional material first.

## 5. Representation classes

### EXACT
Full exact content when wording/structure itself is needed.

### EXCERPT
Verbatim bounded subset retaining exact source reference/location.

### DERIVED_SUMMARY
Derived compression preserving provenance and explicitly noncanonical status.

### REFERENCE_ONLY
Pointer/reference when content need not be embedded or when policy requires restricted representation.

## 6. Exact/excerpt preference

Exact or tightly traceable excerpt SHOULD be preferred where semantic drift would be dangerous, including where applicable:

- canonical invariants;
- exact API/data/security contracts;
- lifecycle/state transitions;
- decision constraints;
- acceptance criteria whose wording materially affects interpretation.

## 7. Summary safety

Every `DERIVED_SUMMARY` MUST:

```text
be labeled derived
retain source_ref
retain source version/revision
retain derivation relationship
state material limitations where needed
be invalidated/revalidated when assumptions/source version change
```

A model-generated summary is never canonical merely because its source was canonical.

## 8. Sensitive minimization

When UPOS-010 returns sensitivity constraints, representation may use:

- minimum necessary excerpt;
- redacted representation;
- reference-only representation;
- Role-scoped isolation.

Module 05 applies constraints but does not define who is permitted.

## 9. Budget accounting

Bundle Manifest SHOULD report factual accounting:

```text
budget_limit_or_reference
budget_consumed
required_material_count/size
optional_material_count/size
summarized_material
omitted_optional_material
overflow_condition if any
```

Cost metrics/aggregation remain UPOS-008.
