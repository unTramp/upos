# Telemetry Capture Standard

**ID:** UPOS-08-TCS-001  
**Type:** CAPTURE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Capture classes

Canonical v1 importance classes:

```text
REQUIRED_AUDIT
REQUIRED_OPERATIONAL
OPTIONAL_DIAGNOSTIC
```

The class determines minimum capture expectations, not retention duration or access policy.

## 2. Required Audit

`REQUIRED_AUDIT` telemetry is required when a governed flow declares it necessary for audit/provenance reconstruction.

It MUST NOT be silently sampled away.

Loss/unavailability must be surfaced as telemetry-integrity degradation.

## 3. Required Operational

`REQUIRED_OPERATIONAL` telemetry is necessary for defined operational/metric/read-model functions.

If unavailable, affected metrics/projections must report `INCOMPLETE`/`UNKNOWN` rather than invent values.

## 4. Optional Diagnostic

`OPTIONAL_DIAGNOSTIC` telemetry may be sampled, dropped, or retained for shorter periods subject to external policy.

Its absence MUST NOT invalidate audit reconstruction unless an external policy explicitly upgraded it.

## 5. Capture expectation source

Every required capture expectation MUST be traceable through one or more:

```text
capture_policy_ref
capture_policy_version
producer_contract_ref/version
event_contract_ref/version
owner-domain contract ref
```

Without such expectation, silence alone does not justify `MISSING_REQUIRED_EVENT`.

## 6. Sampling

Sampling is permitted only when it does not break:

- required audit reconstruction;
- required provenance;
- a canonical Metric Definition's declared source completeness requirement;
- a mandatory trace completeness contract.

Where sampling applies, retained data SHOULD preserve:

```text
sampling_policy_ref
sampling_decision_ref
sampling rate/probability where meaningful
```

Concrete sampling implementation is UPOS-011/runtime.

## 7. Payload minimization

Default capture SHOULD use:

```text
stable IDs
versions
small structured attributes
reason codes
hashes/revision refs
result refs
```

Avoid copying:

```text
full Context Bundles
full documents
full diffs
full prompts
private user data
credentials/secrets
unbounded logs
```

unless a separate governed requirement makes that copy necessary and UPOS-010 policy allows it.

## 8. Hidden reasoning

Telemetry MUST NOT require or store hidden chain-of-thought.

Externally reportable model usage categories such as a provider's `reasoning_tokens` MAY be recorded as numeric usage if exposed by the provider; this does not authorize reasoning-content capture.

## 9. Sensitive telemetry interface

After UPOS-010 reconciliation, Events MAY carry policy-scoped security handling metadata:

```text
security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

UPOS-010 owns the substantive security/privacy handling constraints. UPOS-008 owns capture/storage/projection mechanics under those constraints. UPOS-011 binds concrete provider/runtime enforcement.

## 10. Secret-safe default

Secrets, raw credentials and secret values MUST NOT be written to telemetry by default.

A provider/tool adapter discovering such material must prefer redacted/reference representation.

Final redaction/retention/access enforcement semantics are pending UPOS-010.

## 11. High-cardinality discipline

Domain identities are legitimate Event/trace references.

Metric label/dimension use is separate: high-cardinality fields such as `task_id`, `commit_ref`, raw user IDs, arbitrary error strings, or full URLs SHOULD NOT become universal metric dimensions unless a specific Metric Definition justifies them.

## 12. Capture failure

Failure to emit/record required telemetry does not automatically fail the underlying domain operation unless an external owner policy says so.

It creates an Observability/data-quality condition that downstream audit/metric consumers must see.
