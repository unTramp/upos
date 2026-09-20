# Phase 3 / Slice 1 — Pre-Stable Ratification Record

**ID:** UPOS-SCHEMA-P3-S1-STABILITY-001  
**Status:** PRE-STABLE RATIFICATIONS RECORDED — PENDING INDEPENDENT STABILITY CONFIRMATION  
**Date:** 2026-09-20  
**Baseline:** U-POS v1.0.0  
**Canonical main:** `338692cb3677bf395e9c5f17dc3e2a3ff9793960`  
**Stability-decision input HEAD:** `ad4e84e343bd646d257218f0677bbcd906a0b47d`  
**F-17a remediation checkpoint:** `0513585876efd23e9468b86e3139a13383504781`

## 1. Purpose and authority boundary

This record captures the two governance ratifications required by the independent Slice-1 Stability Decision before an independent stability confirmation.

It does **not**:

- declare Slice-1 Stability PASS;
- promote any schema from CANDIDATE to STABLE;
- perform Exit Acceptance;
- authorize merge of PR #6;
- start Slice 2 or Phase 4/5/6/7 implementation;
- modify frozen owner authority.

The Phase-2 precedent separates the stability decision from the later registry-only promotion and from exit acceptance. Slice 1 preserves that separation.

## 2. F-16 — eighth owner-bound runtime contract ratification

### Determination

`UPOS-04-RETRY-PROVENANCE` is formally ratified as the **eighth owner-bound Phase-3 / Slice-1 runtime contract** proposed for the Slice-1 stable contract set.

Artifact:

```text
runtime/contracts/RETRY_PROVENANCE_RUNTIME_CONTRACT.md
ID: UPOS-04-RETRY-PROVENANCE
semantic owner: UPOS-04
```

### Reconciliation of planning enumeration

SINGLE §8.3 enumerated seven owner-bound runtime contracts during planning.

SINGLE §8.4 separately authorized a Retry Provenance schema, while canonical UPOS-04 ownership already assigns retry/rework/recovery semantics to UPOS-04.

The implemented Retry Provenance durable record declares a `runtime_contract_ref`. For that reference to remain reconstructable and fail closed, the already-authorized Retry Provenance family requires a resolvable owner-bound runtime contract artifact.

Therefore the Slice-1 owner-bound contract set proposed for stability is eight contracts rather than the seven-item planning enumeration.

The eighth contract:

- materializes already-authorized Retry Provenance semantics;
- introduces no new semantic owner;
- introduces no new domain identity;
- remains semantically owned by UPOS-04;
- introduces no `retry_id`, retry-attempt identity, or universal attempt identity;
- does not expand Slice-1 behavioral scope;
- does not implement retry execution, scheduling, rework, recovery, or orchestration.

This is a ratification of the implemented representation boundary, not a redesign of frozen owner semantics.

## 3. F-17b — infrastructure version-axis ratification

### Determination

The following NONE_INFRASTRUCTURE primitives may be conditionally durable for persistence/reconstruction purposes:

```text
upos.common.runtime_operation_control
upos.common.runtime_operation_outcome
```

For the present Slice-1 contract design, both require the **runtime contract version axis**:

```text
runtime_contract_ref
runtime_contract_version
```

They do **not** require a separate mandatory `runtime_schema_version` field in Slice 1.

This is an intentional stability determination, not an accidental omission.

### Interpretation

For these two common infrastructure primitives:

- runtime contract reference/version carriage is sufficient for the persistence and reconstruction semantics currently authorized by Slice 1;
- the registered JSON Schema URI/version remains independently governed by the schema registry;
- owner semantic versions, Phase-2 schema versions, Event versions, implementation versions, persistence-format versions, and provider/adapter versions remain separate axes;
- absence of a stored `runtime_schema_version` field does not collapse or redefine those axes.

### Future compatibility rule

Introducing a new **mandatory** `runtime_schema_version` field into either stable primitive would change the accepted instance shape.

Such a change is compatibility-significant and must be handled as a **MAJOR / breaking contract change** under the applicable schema/runtime compatibility governance. It must not be introduced silently as a patch-level hardening change.

This ratification does not prohibit a future explicitly versioned redesign; it records the current stable-design intent so that such a redesign receives the required compatibility treatment.

## 4. Pre-stable remediation context

F-17a is implemented separately in checkpoint:

```text
0513585876efd23e9468b86e3139a13383504781
fix(runtime): version durable failure envelope
```

That checkpoint adds required `runtime_contract_ref` and `runtime_contract_version` to the common runtime failure envelope and its four canonical fixtures without adding `runtime_schema_version`.

This record does not independently confirm F-17a closure; exact-HEAD machine evidence and independent stability confirmation remain required.

## 5. Registry and promotion boundary

Current registry state remains:

```text
27 STABLE
11 CANDIDATE
38 TOTAL
```

No Slice-1 CANDIDATE entry is promoted by this record.

If independent stability confirmation later authorizes promotion, registry reconciliation must remain a separate registry-only change and must pass the exact-HEAD validation gates before any distinct Exit Acceptance step.

## 6. Required next action

```text
pre-stable remediation + ratifications
→ exact-HEAD validation
→ STOP
→ focused independent stability confirmation
```

No Stability PASS is declared by this record.
