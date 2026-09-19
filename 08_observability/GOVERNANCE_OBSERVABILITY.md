# Governance Observability

**ID:** UPOS-08-GOB-001  
**Type:** GOVERNANCE OBSERVABILITY INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Principle

Governance Observability measures governed occurrences without acquiring governance authority.

## 2. Observable governance occurrences

When owner modules expose them, projections/metrics may include:

```text
scope expansion
reclassification
rerouting
escalation
Human Governance decision/override refs
canonical conflict refs
Quality Exception refs
permission denied refs
security veto/result refs
documentation drift refs
```

## 3. Owner-required semantics

A metric may only use a category when the owning module supplies a governed semantic signal/reference.

Examples:

```text
UPOS-004 says reclassification occurred
→ Observability may count it

UPOS-010 says permission denied
→ Observability may count it after reconciliation
```

Do not infer `policy violation` or `security incident` from generic failure patterns.

## 4. Late reclassification

`late_reclassification` cannot be a universal metric until “late” is defined for the relevant Workflow/Stage/policy cohort.

A Metric Definition must specify the boundary.

No single universal Stage is assumed.

## 5. Scope-expansion rate

A scope-expansion metric consumes explicit UPOS-004/006 scope-expansion signals.

It must define denominator (Tasks, Workflow Instances, Engineering Changes, etc.).

## 6. Manual override

Manual/Human override counts must distinguish:

- required planned approval;
- explicit exceptional override;
- ordinary Human participation.

Only owner-provided Human Governance semantics can label an action an override.

## 7. Permission/security observability

Permission-denied, protected-action and Security metrics consume the reconciled UPOS-010 Permission/Security semantics and remain Observability-derived measurements.

## 8. Governance health != policy correctness

High/low counts are signals.

They do not automatically mean governance should be loosened/tightened.

Interpretation/promotion belongs to owners and UPOS-009.
