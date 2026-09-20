# Phase 3 / Slice 2 — Adapter Resolution Reconciliation

**ID:** UPOS-P3-S2-REC-001  
**Status:** CANDIDATE — TARGETED REMEDIATION APPLIED / FOCUSED INDEPENDENT RE-AUDIT PENDING  
**Canonical baseline:** `d65d1bc5d1e9df85e41aff1ec1a4cb3dcab9dfb4`  
**Planning authority:** `PHASE_3_SLICE_2_ADAPTER_RESOLUTION_SINGLE.md`

## 1. Ownership

```text
UPOS-11 → Adapter Resolution request/evaluation, binding selection,
          validation result, Adapter Failure, Resolved Adapter View
UPOS-04 → retry / rework / recovery / rerouting decisions (referenced, never imported)
UPOS-08 → Event semantics (referenced, schema unchanged)
UPOS-10 → Permission Decision / Security Policy (referenced only)
cross-cutting runtime → representation, compatibility, persistence, validation
```

No new semantic owner is introduced.

## 2. Identity reconciliation

`GLOBAL_IDENTITY_REFERENCE_REGISTRY` row 011 supplies every identity Slice 2 needs:

```text
project_id · binding_id · provider_adapter_ref + provider_adapter_version
command_binding_id · adapter_resolution_id
```

Slice 2 mints **zero** new domain identities.

`adapter_resolution_id` is success-only by frozen definition
(`PROJECT_ADAPTER_ONTOLOGY.md`: adopted for immutable execution-time Resolved
Adapter Views). A resolution terminating in an Adapter Failure produces no
Resolved Adapter View and therefore no `adapter_resolution_id`; attempt
correlation is carried solely by the infrastructure-only `operation_request_key`.
The material Adapter Failure physically retains the originating key; this reuses
the canonical common runtime-operation-control field and introduces no new identity.

Ten synthetic identities are mechanically rejected, including
`adapter_resolution_attempt_id`, `fallback_id`, `adapter_failure_id` and generic
`adapter_id` / `resolution_id`.

## 3. Vocabulary reconciliation

Validation uses the canonical UPOS-11 vocabulary only — `VALID`,
`VALID_WITH_WARNINGS`, `INCOMPLETE`, `INVALID` — with a separate
`configuration_completeness` axis. No PASS/FAIL is introduced, so an Adapter
Validation Result is neither a Quality Verdict nor a Security Decision.

Adapter Failure uses only the 17 canonical `ADAPTER_FAILURE_MODEL.md` classes.
`FALLBACK_EXHAUSTED` was deliberately **not** invented: an exhausted fallback
chain terminates in an existing canonical class carrying fallback provenance.

### S2-F08 pre-STABLE semantic decision

A Resolved Adapter View MAY exist with `validation_state = INCOMPLETE` only when
`missing_required_binding_refs = []`. This preserves P10 for incompleteness
limited to OPTIONAL/CONDITIONAL bindings.

`INCOMPLETE` with one or more `missing_required_binding_refs` MUST NOT produce a
Resolved Adapter View. It follows the Adapter Failure path using the applicable
existing canonical UPOS-11 failure class; no new failure code is introduced.
Focused evidence uses `BINDING_NOT_FOUND`.

## 4. Fallback reconciliation

Fallback is UPOS-11 alternate binding selection under an explicit chain, not a
UPOS-04 lifecycle concept. It creates no execution identity and no
`fallback_id`. Canonical provenance is retained exactly as
`BINDING_RESOLUTION_STANDARD.md` enumerates it: `requested_binding_ref`,
`resolved_binding_ref`, `fallback_reason`, `actual_provider_adapter_ref` /
`actual_provider_adapter_version`.

## 5. Slice-1 reuse

`runtime-operation-control`, `runtime-operation-outcome`,
`runtime-failure-envelope` and the Event schema are reused **unchanged**. No new
common runtime schema was added and no STABLE schema was modified.
`operation_kind` is a free string, so `ADAPTER_RESOLUTION` required no change to
the STABLE common control schema.

The STABLE Event schema needed no change: `domain_owner_module` already includes
`UPOS-11` and its generic carriers represent all six Slice-2 event kinds.

## 6. Version carriage

All four schemas **require** and all canonical fixtures **physically store**
`runtime_contract_ref`, `runtime_contract_version` and `runtime_schema_version`.
Positive evidence is read from stored content; the validator manufactures none.
Unsupported or unknown references fail closed through the same
`resolve_runtime_contract_reference()` the fixture walk uses.

## 7. Carried debt

F-09(a) is closed inside this slice: `RUNTIME_OPERATION_AND_IDEMPOTENCY_STANDARD.md`
section 3.1 now records Adapter Resolution as requiring a technical request key.

F-06 is closed incidentally by the bidirectional registry/file parity check the
Slice-2 validator plan required.

F-07, F-08, F-10, F-11, F-13, F-14 remain deferred or inherited and were not
reopened.

## 8. Independent blind audit remediation record

The independent Slice-2 blind audit at audited HEAD
`aac54bf6320676960e0a81453e7d43b7982fe8e5` returned:

```text
P0 = 0
P1 = 1
P2 = 10
SLICE-2 BLIND AUDIT: REMEDIATION REQUIRED
```

Blocking finding `S2-F01` was remediated by requiring every material Adapter
Failure to store the originating `operation_request_key` and by mechanically
checking request↔failure equality in composite failed-resolution evidence.

`S2-F08` received the explicit pre-STABLE decision recorded above and is
structurally enforced on Resolved Adapter View.

Remaining blind-audit P2 inputs are intentionally not broadly remediated here:
`S2-F02`, `S2-F03`, `S2-F04`, `S2-F05`, `S2-F06`, `S2-F07`, `S2-F09`,
`S2-F10`, and unrelated portions of `S2-F11`.

Independent focused re-audit is still required.

## 9. Authority boundary

This record states remediation evidence only. It does **not** declare focused
re-audit PASS, a Stability PASS, promotion authorization, Exit Acceptance or
merge authorization. Those belong to later independent stages.
