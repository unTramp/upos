# Skill Lifecycle

**ID:** UPOS-03-LFC-001  
**Type:** LIFECYCLE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Skill Definition lifecycle

Canonical lifecycle:

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

Controlled alternate transitions MAY include:

```text
REVIEW → DRAFT
APPROVED → REVIEW
DEPRECATED → ACTIVE
```

if governance explicitly revalidates the Definition.

## 2. State meanings

### DRAFT
Contract is being authored and is not a production standard.

### REVIEW
Contract is under governance/technical review.

### APPROVED
Contract semantics are approved but may not yet be operationally adopted.

### ACTIVE
Contract is approved for production use.

### DEPRECATED
New invocation SHOULD stop where a supported replacement exists. Existing references may remain during migration.

### RETIRED
Skill Definition must not be selected for new governed work.

## 3. Separate invocation lifecycle

```text
Skill Definition lifecycle
!= Skill Invocation execution state
!= Agent Run lifecycle
!= Workflow lifecycle
```

Invocation states are runtime/workflow/observability concerns and are not defined here.

## 4. Deprecation

Deprecation MUST state:

- reason;
- replacement if any;
- migration compatibility;
- effective date/version where practical.

## 5. Retirement

A Skill MAY be retired only when active consumers can resolve a replacement or intentionally stop using the capability.

Historical contracts remain available for audit/provenance under Documentation governance.
