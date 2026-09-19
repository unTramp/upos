# Definition of Ready & Definition of Done — Quality Semantics

**ID:** UPOS-07-DOR-001  
**Type:** QUALITY READINESS CRITERIA STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_GATE_STANDARD.md


## 1. Boundary

UPOS-007 defines how applicable DoR/DoD Quality criteria are evaluated.

UPOS-004 decides when a DoR/DoD checkpoint is required and what Workflow transition follows.

## 2. Quality Definition of Ready

Possible criteria, when made applicable by Workflow/Policy:

- authoritative requirements available;
- acceptance criteria sufficiently defined;
- blocking canonical conflicts resolved;
- required architecture/design decision exists;
- required Context can be assembled;
- applicable quality/evidence plan is identifiable.

No criterion above is universally mandatory for every C0–C5 Task.

## 3. DoR result

DoR is evaluated using a Quality Assessment/Gate.

It does not create a new Workflow entry state.

## 4. Quality Definition of Done

Possible applicable criteria:

- required requirements/acceptance criteria satisfied;
- required Review completed with acceptable verdict;
- required QA completed with acceptable verdict;
- required check evidence sufficient/fresh;
- blocking Findings resolved or covered by valid exception;
- documentation conformance satisfied where required;
- known limitations recorded;
- required external quality-related result references satisfied.

## 5. Exclusions

DoD does not inherently mean:

```text
merge occurred
release occurred
deployment occurred
Workflow completed
```

unless a specific post-integration/post-release Assessment scope explicitly evaluates those facts.

## 6. Critical invariant

```text
Quality DoD satisfied != Workflow completed
```

Workflow may still require authority, permission, merge, release preparation, Security/Human gates, or other external steps.
