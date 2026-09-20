# Phase 3 / Slice 2 — Adapter Resolution Candidate Evidence

**ID:** UPOS-P3-S2-ACC-001  
**Status:** CANDIDATE — TARGETED REMEDIATION APPLIED / FOCUSED INDEPENDENT RE-AUDIT PENDING  
**Baseline:** U-POS v1.0.0  
**Canonical baseline:** `d65d1bc5d1e9df85e41aff1ec1a4cb3dcab9dfb4`

This artifact records candidate and targeted-remediation evidence for Phase 3 /
Slice 2. The independent blind audit has occurred and returned remediation
required; this artifact does **not** perform the pending focused re-audit, the
Stability Decision, registry promotion, Exit Acceptance or the merge decision.

## 1. Candidate Completion Gate

| # | Requirement | Evidence |
|---|---|---|
| 1 | four Slice-2 schemas exist | `schemas/11/project_adapter/` — request, validation-result, failure, resolved-view |
| 2 | all four registered CANDIDATE | registry 38 STABLE / 4 CANDIDATE / 42 TOTAL |
| 3 | `UPOS-11-ADAPTER-RESOLUTION` resolves fail-closed | registered in `RUNTIME_CONTRACT_ARTIFACTS`; unknown ref, unsupported version and deleted artifact all reject |
| 4 | P1–P10 regression basis preserved | original stored P1–P10 fixtures remain in place; P10 OPTIONAL/CONDITIONAL `INCOMPLETE` remains allowed |
| 5 | N1–N14 regression basis preserved | original N1–N14 negative fixtures remain in place and are not weakened; focused remediation adds missing-key, key-mismatch and REQUIRED-INCOMPLETE rejection evidence |
| 6 | version fields required and stored | three fields `required` in all four schemas and physically present in every canonical fixture |
| 7 | Baseline Integrity | `verify_frozen_baseline.py` PASS, 498 files, exit 0 |
| 8 | Schema Validation | `validate_schemas.py` PASS, 42 documents, exit 0 |
| 9 | candidate evidence truthful | this record plus reconciliation and traceability, all marked pending |
| 10 | F-09(a) incorporated | idempotency standard section 3.1 |
| 11 | no frozen source modified | `00_system/` and UPOS-001—011 untouched |
| 12 | no Phase-2 STABLE schema modified | none |
| 13 | no Slice-1 STABLE schema modified | none |
| 14 | no provider execution | representation only; execution fields rejected |
| 15 | no Slice 3 / Phase 4/5/6/7 leakage | none |

## 2. Validator quality

Positive evidence is read from stored fixture content; no field is manufactured
in validator memory before a positive check. Each negative is asserted to yield
exactly one error at a pinned validator keyword naming the offending field, so
no negative can pass by incidental rejection. Contract fail-closed proofs call
the same `resolve_runtime_contract_reference()` the fixture walk uses.

Eight mutation probes were run against an isolated copy and all failed closed:
broken positive fixture, repaired negative fixture, unregistered schema file,
injected `RETRY_OF`, injected `credentials`, `adapter_resolution_id` on a
failure, deleted contract artifact, forbidden identity declared in a schema.

## 3. Independent blind audit and targeted remediation

Independent blind audit at audited HEAD
`aac54bf6320676960e0a81453e7d43b7982fe8e5`:

```text
P0 = 0
P1 = 1
P2 = 10
SLICE-2 BLIND AUDIT: REMEDIATION REQUIRED
```

- `S2-F01` — remediated: material Adapter Failure now physically retains the
  originating infrastructure-only `operation_request_key`; missing correlation
  is a schema reject and request↔failure mismatch is a conformance reject.
- `S2-F08` — explicit pre-STABLE decision recorded and structurally enforced:
  OPTIONAL/CONDITIONAL `INCOMPLETE` with no missing REQUIRED binding may resolve;
  `INCOMPLETE` with any missing REQUIRED binding cannot yield a Resolved Adapter
  View and follows an existing canonical Adapter Failure class.

No re-audit PASS is declared here. Independent focused re-audit remains pending.

## 4. Authority boundary

This document records the targeted remediation but does not close S2-F01/S2-F08
on behalf of the independent focused re-auditor and authorizes no Stability
Decision, promotion, Exit Acceptance or merge.

Required next action:

```text
TARGETED REMEDIATION APPLIED
→ exact-head validation / CI
→ STOP
→ focused independent re-audit
```
