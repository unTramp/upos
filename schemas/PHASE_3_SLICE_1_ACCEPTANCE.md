# Phase 3 / Slice 1 — Execution Spine Remediation Evidence

**ID:** UPOS-P3-S1-ACC-001  
**Status:** REMEDIATED CANDIDATE — PENDING INDEPENDENT RE-AUDIT  
**Baseline:** U-POS v1.0.0  
**Canonical baseline:** `338692cb3677bf395e9c5f17dc3e2a3ff9793960`  
**Audited candidate:** `2a291aa5d8e76198205efbfec075bb0755dd4bfc`
**F-03 validated checkpoint:** `ac887a16848a5c34d9af5caec29214fe9e3ff89c`

This artifact records implementation evidence after remediation of blind-audit findings F-01 through F-05. It does **not** perform the independent acceptance, stability decision, merge decision, or CANDIDATE→STABLE promotion.

## 1. Remediation evidence

### F-01 — deterministic enforcement

The validator now performs actual cross-record conformance rejection rather than asserting that an illustrative negative fixture still contains the forbidden shape.

Focused checks cover:

- full bounded retry: `successor_ref != predecessor_ref`;
- Routing: `operation_request_key != routing_decision_ref`;
- Routing/runtime outcome: `operation_request_key != runtime_outcome.owner_result_ref`;
- Permission/Adapter examples: `operation_request_key != owner_result_ref`;
- Event correction: `event_id != correction_of_event_id`;
- persisted private reasoning: recursive forbidden-field rejection;
- transport redelivery must not be represented as UPOS-04 `RETRY_OF`.

Each former false-negative path has a focused reject path. Corresponding valid cases are also exercised.

### F-02 — positive Execution Attempt / retry evidence

Positive fixtures now cover:

- COMPLETED;
- FAILED with `failure_ref` and `terminal_at`;
- CREATED;
- CANCELLED with `terminal_at`.

The Agent Run retry chain is anchored as:

```text
AR-1 / FAILED / failure_ref
→ RETRY_OF(trigger_ref == predecessor.failure_ref)
→ AR-2 / CREATED
```

The predecessor and successor references must match the corresponding Execution Attempt subjects, while the bounded execution identity must change.

### F-04 — runtime contract resolution

Owner-bound Slice-1 runtime contract artifacts now exist under `runtime/contracts/`.

Validator resolution is fail-closed for runtime/Event/producer contract references used by runtime fixtures:

- unknown contract reference → reject;
- unsupported referenced contract version → reject;
- referenced artifact missing or ID/version mismatch → reject.

### F-03 — version carriage and fail-closed compatibility

The six durable schema families identified by the blind audit can now carry separate:

- `runtime_contract_ref`;
- `runtime_contract_version`;
- `runtime_schema_version`.

Supported values are constrained by the corresponding schema contract. A supported version fixture passes; an unsupported runtime-contract version fixture is required to reject.

These axes remain distinct; the implementation does not assert that semantic-contract and serialization versions must evolve together.

### F-05 — evidence truthfulness

Traceability and reconciliation now distinguish:

- JSON Schema structural rejection;
- deterministic cross-record conformance rejection;
- positive conformance evidence.

No illustrative negative fixture is described as rejection evidence unless a validator path actually rejects it.

## 2. Registry / scope state to verify at exact remediation HEAD

Required end-state:

```text
27 pre-existing Phase-2 schemas = STABLE
11 Slice-1 schemas = CANDIDATE
CANDIDATE→STABLE promotion = NONE
Slice 2 = NOT STARTED
Phase 4/5/6/7 implementation = NOT STARTED
frozen UPOS-001—011 sources = UNCHANGED
```

## 3. Validation gate

The remediation is not considered ready for re-audit until the exact remediation HEAD has:

- Baseline Integrity PASS;
- full Schema Validation PASS;
- focused F-01 reject/pass evidence;
- F-02 positive lifecycle/retry evidence;
- F-03 supported-version PASS and unsupported-version REJECT;
- F-04 contract-reference resolution PASS.

## 4. Authority boundary

This document does not close the blind-audit findings on behalf of the independent auditor.

Required next action after an exact-HEAD green gate:

```text
STOP
→ independent blind re-audit
→ independent finding closure / stability decision
```

No merge or STABLE promotion is authorized here.

## 5. Recovery checkpoint chain

```text
F-01 core enforcement       e3fd4543c2c92eb2288d7b0cbb92d0d6a44d3df0  PASS
F-02 lifecycle/retry        e6346115a3a196ee575207fd97b1772a57d1fae7  PASS
F-04 contract artifacts     bf3a65d83a1c5faddc223caac1fef1d93d7eb5fb  PASS
F-04 fail-closed resolver   253a3a2c4bf3a79b6cc8804543977c4d06a20db6  PASS
F-03 carriage proof         ac887a16848a5c34d9af5caec29214fe9e3ff89c  PASS
```

The F-05 commit that updates this evidence must itself pass the same exact-HEAD gates before handoff.
