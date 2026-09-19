# Finding Standard

**ID:** UPOS-07-FND-001  
**Type:** FINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/FINDING_TEMPLATE.md


## 1. Finding

A Finding is an attributable Quality observation representing one of:

```text
nonconformance
defect
risk
missing evidence
ambiguity
advisory improvement
```

Every Finding MUST have stable:

```text
finding_id
```

## 2. Contract

```text
finding_id
quality_assessment_id

target_ref
target_state_ref

criterion_ref
criterion_key
evidence_record_refs

location_or_scope
description

severity
category
status

producer_role_ref
producer_agent_run_ref
created_at

resolution_refs
verification_assessment_ref
quality_exception_id

limitations
```

Non-applicable references use `N/A`.

## 3. Severity

Canonical universal severity:

```text
BLOCKING
MAJOR
MINOR
ADVISORY
```

### BLOCKING

The evaluated Quality condition cannot currently be accepted under applicable Quality rules, absent a valid externally authorized exception where policy allows.

### MAJOR

A material Quality issue requiring explicit resolution/evaluation; normally incompatible with SATISFIED for the affected required criterion.

### MINOR

A bounded non-blocking issue or improvement unless a governed criterion explicitly makes it required.

### ADVISORY

Optional improvement/guidance that does not by itself fail a required criterion.

The frozen-master `NIT` concept is normalized to `ADVISORY`.

## 4. Separation

```text
severity
!= confidence
!= finding status
!= Quality Verdict
```

No mandatory numerical scoring.

## 5. Categories

Canonical core categories:

```text
CORRECTNESS
REQUIREMENT
ARCHITECTURE
REGRESSION
TESTING
DOCUMENTATION
MAINTAINABILITY
ACCESSIBILITY
PERFORMANCE
RELIABILITY
SECURITY_REFERENCE
EVIDENCE_GAP
SCOPE
OTHER
```

Categories describe; they do not re-own Architecture/Security/Product semantics.

Governed extensions are allowed.

## 6. Finding lifecycle

```text
OPEN
RESOLVED
WAIVED
INVALID
SUPERSEDED
```

A completed Assessment may contain `OPEN` Findings.

The Assessment itself remains immutable.

## 7. Resolution

`RESOLVED` means:

```text
underlying issue corrected
+
resolution verified sufficiently
```

Producer assertion alone is insufficient.

Resolution SHOULD reference the new target and verification/re-review Assessment.

## 8. Waiver

`WAIVED` requires a valid `quality_exception_id` with external authority/decision reference.

```text
WAIVED != NEVER EXISTED
```

The original Finding remains historically visible.

## 9. Advisory discipline

Reviewer preferences MUST NOT be converted into mandatory failures without governed criterion authority.
