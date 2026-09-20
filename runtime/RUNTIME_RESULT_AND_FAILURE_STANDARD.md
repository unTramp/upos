# Runtime Result and Failure Standard

**ID:** UPOS-RUNTIME-RES-001  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Baseline:** U-POS v1.0.0

## 1. Technical outcome

The common technical outcome vocabulary is:

```text
COMPLETED
FAILED
CANCELLED
```

It describes whether a runtime operation technically completed.

It MUST NOT be interpreted as an owner-domain verdict.

Examples:

```text
runtime outcome = COMPLETED
Security Decision = DENY
→ valid

runtime outcome = COMPLETED
Quality Verdict = FAIL
→ valid
```

## 2. Failure envelope

A common failure envelope MAY carry:

- failure owner module;
- operation kind;
- subject reference;
- owner failure code;
- owner failure reference;
- cause reference;
- safe provider-error reference;
- retryability hint;
- details reference;
- provenance references.

Allowed retryability hints:

```text
SAFE_RETRY
CONDITIONALLY_RETRYABLE
NOT_RETRYABLE
UNKNOWN
```

```text
retryability_hint
!=
Workflow retry decision
```

## 3. Prohibited identities and semantics

The common failure contract MUST NOT introduce:

```text
runtime_error_id
error_id
failure_id
```

as universal U-POS domain identities.

It MUST NOT define Quality verdicts, Security decisions, Context validity or Workflow failure taxonomy.

## 4. Timeout

Timeout is represented as a technical failure reason where applicable. It MUST NOT be added automatically to every owner lifecycle.

## 5. Normative sources

- `04_workflow_engine/FAILURE_RETRY_RECOVERY.md`
- `05_context_memory/CONTEXT_FAILURE_MODEL.md`
- `06_engineering_governance/ENGINEERING_FAILURE_MODEL.md`
- `07_quality_system/QUALITY_FAILURE_MODEL.md`
- `10_security_permissions/SECURITY_FAILURE_MODEL.md`
- `11_project_adapter/ADAPTER_FAILURE_MODEL.md`
