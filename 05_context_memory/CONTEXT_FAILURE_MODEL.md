# Context Failure Model

**ID:** UPOS-05-CFM-001  
**Type:** FAILURE / RESULT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 Workflow Engine


## 1. Boundary

UPOS-005 emits Context result/failure semantics.

UPOS-004 owns the orchestration response.

Example:

```text
UPOS-005:
MISSING_REQUIRED_SOURCE — Architecture Contract unresolved

UPOS-004:
block Stage / escalate / request owner decision
```

## 2. Failure taxonomy

| Failure | Context meaning | Executable Bundle? | Degraded/diagnostic Bundle? | Required external interface |
|---|---|---|---|---|
| `MISSING_REQUIRED_SOURCE` | required source class/material is unsatisfied | no | yes, `INCOMPLETE` | UPOS-01 owner resolution + UPOS-004 |
| `SOURCE_RESOLUTION_FAILURE` | canonical scope/owner/source resolution could not complete | no | diagnostic only | UPOS-01 / UPOS-011 |
| `CANONICAL_CONFLICT` | active authoritative sources conflict | no | yes, conflict-labeled | UPOS-01 + UPOS-004 |
| `STALE_REQUIRED_CONTEXT` | required material is stale/not applicable enough for current execution | no until revalidated | yes, `STALE` | freshness/reassembly + UPOS-004 |
| `PERMISSION_BLOCKED` | required material cannot be delivered under current access constraints | no | metadata-only diagnostic if allowed | UPOS-010 + UPOS-004 |
| `BUDGET_INSUFFICIENT` | required material cannot be represented safely within budget | no | yes for diagnosis | budget response + UPOS-004/011 |
| `REPRESENTATION_UNSAFE` | no safe representation satisfies semantic/security need | no | possibly metadata-only | UPOS-010/004 |
| `PROVENANCE_MISSING` | candidate lacks provenance needed for trusted inclusion | no if required; optional excluded otherwise | yes if required gap exposed | UPOS-01/011 |
| `CROSS_SCOPE_CONTAMINATION` | material from wrong project/task/version/role boundary entered candidate/Bundle | no until rebuilt | invalidated snapshot retained for audit | isolation + UPOS-004 |
| `INVALID_MEMORY_REUSE` | stale/out-of-scope/noncanonical memory was proposed for reuse | exclude memory; Bundle depends on remaining context | yes if requirements still satisfied | memory policy + UPOS-004 if blocking |
| `PROVIDER_RETRIEVAL_FAILURE` | physical retrieval/search provider failed | unknown; must not infer absence | diagnostic | UPOS-011/runtime + UPOS-004 if blocking |

## 3. Source lookup outcomes

`SOURCE_NOT_FOUND` is a retrieval outcome and may lead to `MISSING_REQUIRED_SOURCE`.

It MUST NOT be equated with `SOURCE_DOES_NOT_EXIST` without upstream governance evidence.

## 4. Degraded Context rule

A Bundle may be `VALID_WITH_WARNINGS` only when all required source requirements remain satisfied and no blocking conflict exists.

Optional source omission may be a warning.

Missing required authoritative source cannot be represented as `VALID`.

## 5. Context health signals

Factual non-metric health signals include:

```text
required_sources_satisfied
canonical_conflict_present
stale_required_source
unknown_source_version
budget_overflow
summary_used
context_rebuilt
unauthorized_source_excluded
cross_project_leak_detected
missing_provenance
permission_transformation_applied
```

UPOS-008 may later measure/aggregate them.

## 6. Failure result explainability

A Context failure/result SHOULD identify:

```text
context_request_id
failure class
affected requirement/source class
relevant source/provider/permission refs
why executable Bundle could/could not be produced
recommended external interface to invoke
```

It MUST NOT prescribe Workflow transition semantics beyond returning the condition.
