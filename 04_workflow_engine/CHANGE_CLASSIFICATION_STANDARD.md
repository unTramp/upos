# Change Classification Standard — C0–C5

**ID:** UPOS-04-CLS-001  
**Type:** CLASSIFICATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** ROUTING_STANDARD.md, analysis/CLASSIFICATION_DIMENSION_AUDIT.md


## 1. Principle

Classification is based on impact/risk, not line count or diff size.

```text
RISK / IMPACT != DIFF SIZE
```

A one-line authorization change may be C5.

A large generated-documentation change may be low-risk.

## 2. Canonical classes

### C0 — MICRO

Typical intent:

- typo/copy correction;
- small spacing correction;
- simple documentation fix;
- trivial isolated null guard.

Characteristics:

- no durable Product/Domain/Architecture semantics change;
- no protected/high-risk concern;
- isolated and reversible;
- minimal orchestration depth.

### C1 — SMALL

Typical intent:

- isolated bug;
- small component behavior adjustment;
- minor API validation fix inside existing contract.

Characteristics:

- bounded impact;
- existing architecture/domain boundaries preserved;
- independent review normally required;
- validation may be lightweight.

### C2 — STANDARD

Typical intent:

- ordinary capability;
- feature/change inside existing architecture;
- UI behavior backed by existing domain.

Characteristics:

- normal product/implementation change;
- review + QA/validation expectations;
- documentation reconciliation when contract changes.

### C3 — CROSS_CUTTING

Typical intent:

- frontend + backend + data persistence;
- multiple bounded contexts;
- large shared component migration;
- integration-heavy change.

Characteristics:

- multiple ownership/dependency surfaces;
- integration risk;
- architecture impact check normally required;
- safe parallelization may be possible after shared contracts exist.

### C4 — ARCHITECTURAL

Typical intent:

- new service;
- new canonical storage owner;
- major routing architecture;
- multi-tenancy model;
- eventing model;
- durable structural ownership/boundary change.

Expected orchestration references include:

- RFC;
- Architecture review;
- human decision/approval reference;
- ADR;
- implementation/migration planning;
- independent review;
- QA;
- documentation reconciliation.

### C5 — HIGH_RISK

Typical intent:

- authentication/authorization;
- billing/money movement;
- destructive data change;
- privacy/retention;
- secrets;
- production migration;
- security boundary;
- irreversible AI action.

Expected orchestration references include:

- relevant specialist review;
- human approval;
- rollback/recovery strategy;
- strong external evidence;
- enhanced QA/verification.

AI-only merge/release SHOULD be prohibited by default through external Human/Security policy.

## 3. Risk override

Any high-risk signal may override low apparent size.

Classification MUST consider the highest material impact.

## 4. Classification dimensions

UPOS-004 v1 recognizes dimensions from the source audit:

| Dimension | Provenance | Workflow interpretation |
|---|---|---|
| Product semantics impact | TASK_DIRECTIVE_REFINEMENT supported by source | may increase process depth / Product participation |
| Domain semantics impact | TASK_DIRECTIVE_REFINEMENT supported by C3 bounded-context source | may require Domain participation and higher class |
| Architecture impact | SOURCE_DERIVED | durable architecture change drives C4 |
| Cross-module breadth | SOURCE_DERIVED | broad multi-surface change drives C3+ |
| Data/model migration impact | SOURCE_DERIVED | migration/destructive/prod data signals may drive C3–C5 |
| Security/privacy impact | SOURCE_DERIVED | security boundary/privacy/secrets signals may drive C5 |
| Authorization impact | SOURCE_DERIVED | auth/authz is C5 signal |
| Production blast radius | TASK_DIRECTIVE_REFINEMENT supported by prod migration/hotfix/release | increases risk depth |
| Irreversibility | SOURCE_DERIVED | destructive/irreversible behavior is high-risk |
| External API compatibility | SOURCE_DERIVED from API workflow | backward compatibility/versioning affects routing/risk |
| User-facing behavior impact | TASK_DIRECTIVE_REFINEMENT supported by feature/UI source | affects Product/UX/QA participation |
| Operational impact | SOURCE_DERIVED | hotfix/release/production change affects route |
| Deployment complexity | TASK_DIRECTIVE_REFINEMENT supported by migration/release source | affects release/migration checkpoints |
| Uncertainty / missing truth | SOURCE_DERIVED from missing/stale Source-of-Truth and reclassification rules | blocks or raises classification until resolved |

## 5. Consuming external signals

If a dimension's substantive meaning belongs elsewhere, Workflow classification consumes the signal rather than redefining it.

Example:

```text
Security owner determines security sensitivity
→ UPOS-004 consumes signal
→ routing/classification depth changes
```

## 6. Change-class monotonic safety

During execution:

- upward reclassification is always allowed when material new risk is discovered;
- downward reclassification requires explicit evidence;
- stale classification MUST NOT be silently retained.

## 7. Risk inheritance

If an inseparable critical sub-change is C5, the resolved Workflow configuration MUST treat the containing change as C5 for protected orchestration.

If sub-changes can be safely decomposed, they MAY be routed separately by coherent ownership/dependency.
