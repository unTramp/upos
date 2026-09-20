# Phase 3 / Slice 2 — Adapter Resolution Traceability

**ID:** UPOS-P3-S2-TRACE-001  
**Status:** CANDIDATE — TARGETED REMEDIATION APPLIED / FOCUSED INDEPENDENT RE-AUDIT PENDING  
**Canonical baseline:** `d65d1bc5d1e9df85e41aff1ec1a4cb3dcab9dfb4`

## 1. Evidence taxonomy

- **SCHEMA REJECT** — JSON Schema validation rejects the instance.
- **CONFORMANCE REJECT** — a deterministic cross-record rule rejects an otherwise structurally valid instance.
- **POSITIVE PASS** — schema and applicable conformance checks accept stored fixture content as-is.

An illustrative bad fixture alone is not rejection evidence. Every negative below
was asserted to produce exactly one error at a pinned validator keyword.

## 2. Contract traceability

| Contract / invariant | Positive evidence | Negative evidence |
|---|---|---|
| Adapter Resolution Request | stored request with `operation_request_key`, `operation_kind: ADAPTER_RESOLUTION` — POSITIVE PASS | missing request key — SCHEMA REJECT `required`; invented attempt id — SCHEMA REJECT `additionalProperties`; generic `resolution_id` — SCHEMA REJECT `additionalProperties` |
| Adapter Validation Result | `VALID`, `VALID_WITH_WARNINGS`, `INCOMPLETE` stored results — POSITIVE PASS | Security `DENY` / Quality `PASS` — SCHEMA REJECT `enum`; warnings concealing a missing REQUIRED binding — SCHEMA REJECT `maxItems` |
| Adapter Failure | `BINDING_CONFLICT` physically stores originating `operation_request_key` and no resolution identity — POSITIVE PASS | missing failure request key — SCHEMA REJECT `required`; `adapter_resolution_id` on a failure — SCHEMA REJECT `additionalProperties`; `FALLBACK_EXHAUSTED` — SCHEMA REJECT `enum` |
| Resolved Adapter View | success-only view with candidates, precedence, selected binding, provider ref/version; P10 `INCOMPLETE` with no REQUIRED missing binding remains POSITIVE PASS | `INVALID` validation yielding a view — SCHEMA REJECT `not`; `INCOMPLETE` plus missing REQUIRED binding — SCHEMA REJECT `maxItems`; fabricated scope — SCHEMA REJECT `required` |
| Fallback provenance | four canonical refs retained, chain position recorded — POSITIVE PASS | `fallback_id` — SCHEMA REJECT `additionalProperties`; `RETRY_OF` inside a resolution — SCHEMA REJECT `additionalProperties` and CONFORMANCE REJECT |
| Request/result separation | failed composite carries no resolution identity and stores the same `operation_request_key` on request and Adapter Failure — POSITIVE PASS | `adapter_resolution_id` injected on a failed composite — CONFORMANCE REJECT; request/failure key mismatch — CONFORMANCE REJECT |
| Provider boundary | composites free of provider execution fields — POSITIVE PASS | `api_endpoint` — SCHEMA REJECT; injected `credentials` — CONFORMANCE REJECT |
| Technical redelivery | two requests sharing one `operation_request_key` — POSITIVE PASS | — |
| Event representation | six Event kinds on the **unchanged** STABLE Event schema — POSITIVE PASS | — |
| Version carriage | all four families require and store three version fields — POSITIVE PASS | each field removed in turn — SCHEMA REJECT `required`; unsupported version — SCHEMA REJECT `const` |
| Runtime contract resolution | stored `UPOS-11-ADAPTER-RESOLUTION@0.1.0` resolves — POSITIVE PASS | unknown ref and unsupported version — fail-closed through `resolve_runtime_contract_reference()` |
| Registry/file parity | 42 registered, 42 discovered — POSITIVE PASS | unregistered schema file — REJECT |

## 3. Artifacts

```text
runtime/contracts/ADAPTER_RESOLUTION_RUNTIME_CONTRACT.md   UPOS-11-ADAPTER-RESOLUTION @ 0.1.0

schemas/11/project_adapter/adapter-resolution-request.schema.json
schemas/11/project_adapter/adapter-validation-result.schema.json
schemas/11/project_adapter/adapter-failure.schema.json
schemas/11/project_adapter/resolved-adapter-view.schema.json

schemas/fixtures/runtime/project_adapter/   original P1–P10 / N1–N14 evidence plus focused S2-F01/S2-F08 remediation fixtures
```

## 4. Reuse rather than redefinition

The canonical binding `scope` shape is reused by JSON pointer into the STABLE
`upos.11.project_adapter.binding` schema rather than redefined. The STABLE
`adapter-resolution-reference` schema supplies `adapter_resolution_id`. Thirteen
existing STABLE UPOS-11 schemas are referenced and none is modified.

## 5. Phase boundary

Not implemented:

```text
adapter resolver runtime · provider execution · provider adapters
live capability probing · provider health runtime · credentials · secrets
IAM / authentication execution · Event Store · trace propagation / span runtime
Slice 3 Context runtime · Phase 4/5/6/7
```

## 6. Handoff

Independent blind audit at `aac54bf6320676960e0a81453e7d43b7982fe8e5`
reported `P0=0 / P1=1 / P2=10` and required remediation. S2-F01 has been
remediated and S2-F08 explicitly resolved before STABLE consideration.

This document records remediation evidence only. Independent focused re-audit is
still required; this does not substitute for focused closure, a Stability
Decision, promotion, Exit Acceptance or merge.
