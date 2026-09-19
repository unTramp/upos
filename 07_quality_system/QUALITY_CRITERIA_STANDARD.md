# Quality Criteria Standard

**ID:** UPOS-07-QCS-001  
**Type:** CRITERIA STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/QUALITY_CRITERIA_SET_TEMPLATE.md


## 1. Criterion

A Quality Criterion is an evaluable condition whose normative meaning is attributable to an authoritative origin.

A criterion entry MUST contain:

```text
criterion_key
criterion_ref
criterion_class
requirement_level

criterion_summary
source_ref
canonical_owner_ref
source_version_or_revision

applicability_conditions
required_evidence_classes
evaluation_method_or_interface_ref
default_unsatisfied_consequence where governed
exception_eligibility_ref
```

`criterion_summary` is a projection for evaluation convenience and MUST NOT silently replace the source requirement.

## 2. Criterion classes

Minimum universal classes:

```text
GOVERNED_REQUIREMENT
ACCEPTANCE_CRITERION
UNIVERSAL_QUALITY_INVARIANT
PROJECT_QUALITY_STANDARD
EXTERNAL_GATE_REQUIREMENT_REFERENCE
ADVISORY_GUIDANCE
```

External gate requirement entries carry references only.

## 3. Requirement level

```text
REQUIRED
ADVISORY
```

Reviewer preference or ungoverned style preference MUST NOT become `REQUIRED`.

## 4. Criteria Set

A Quality Criteria Set MUST include:

```text
quality_criteria_set_id
name
version
status
purpose

quality_policy_ref
quality_policy_version

applicability_scope
target_types
change_class_conditions
work_type_conditions
concern_conditions

source_resolution_refs
criteria

supersedes
replacement
```

## 5. Criteria Set is not Source of Truth

Criteria Set is an evaluable projection.

It combines references to authoritative sources such as:

- universal UPOS quality invariants;
- project quality standards;
- Task acceptance criteria;
- Architecture/Product/Domain constraints;
- Workflow/Profile-required verification criteria;
- external Security/permission requirements by reference.

If the source requirement changes, the Criteria Set must be revalidated/versioned as appropriate.

## 6. Source priority

Mandatory criteria resolve through UPOS-01 fact-scope/canonical-owner rules.

Do not promote to mandatory:

```text
Reviewer preference
personal style
unreviewed chat suggestion
stale/superseded spec
```

Advisory improvements MAY cite nonmandatory rationale if clearly labeled.

## 7. Applicability

Each criterion in an Assessment receives:

```text
APPLICABLE
NOT_APPLICABLE
UNRESOLVED
```

`NOT_APPLICABLE` requires rationale when not self-evident.

A mandatory criterion MUST NOT be silently skipped.

`UNRESOLVED` prevents a valid PASS until resolved or governed exception/policy makes it nonrequired.

## 8. Criterion evaluation states

For an applicable evaluation:

```text
SATISFIED
UNSATISFIED
BLOCKED
NOT_EVALUATED
NOT_APPLICABLE
```

`NOT_EVALUATED` is not equivalent to SATISFIED.

## 9. Versioned criteria

Historical Assessments retain their original Criteria Set/version.

New criteria versions do not silently rewrite old verdicts.

## 10. Concern-specific criteria

Where governed requirements exist, criteria may cover:

```text
UX / Design / Accessibility
Performance
Reliability
Load / Latency / Resilience
Documentation
Architecture
Data / Migration
```

UPOS-007 evaluates them only through authoritative criterion references.

It MUST NOT invent subjective Design truth or arbitrary universal performance/coverage thresholds.

Security substantive semantics remain an external result/reference boundary.

## 11. No universal thresholds

Coverage percentage, reviewer count, device/browser matrix, performance thresholds and testing doctrine are policy/project-specific unless an authoritative universal policy explicitly defines them.
