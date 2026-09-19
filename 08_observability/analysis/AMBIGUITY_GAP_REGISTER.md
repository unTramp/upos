# Ambiguity / Gap Register — UPOS-008

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

| ID | Issue | Module-08 resolution | Deferred owner | Severity | Reconciliation dependency | Status |
|---|---|---|---|---|---|---|
| `OBS-GAP-001` | Event vs Domain Entity | Event observes occurrence; owner entity remains external. | — | P1 | — | CLOSED |
| `OBS-GAP-002` | Event vs Domain State | Event history never automatically equals canonical current state. | — | P1 | — | CLOSED |
| `OBS-GAP-003` | Event vs Audit Record | Audit is a projection over Events/domain refs, not a second Event entity. | — | P2 | — | CLOSED |
| `OBS-GAP-004` | Trace vs Workflow/Task | Multiple Traces may exist per Task/Workflow. | — | P1 | — | CLOSED |
| `OBS-GAP-005` | Span vs Stage/Agent Run | Span is timed operation; may correlate with Stage/Run but not replace it. | — | P1 | — | CLOSED |
| `OBS-GAP-006` | Correlation vs Causation | Separate fields/semantics; causation requires explicit/governed basis. | — | P1 | — | CLOSED |
| `OBS-GAP-007` | occurred vs recorded vs ingested | Three time dimensions defined. | UPOS-011 clock binding | P1 | `OBS-011-REC-008` | CLOSED_INTERNAL |
| `OBS-GAP-008` | Event ordering | No global total order; partial/causal/owner order. | — | P1 | — | CLOSED |
| `OBS-GAP-009` | Event duplicate/idempotency | Stable event_id; at-least-once tolerant idempotent ingestion. | UPOS-011 backend | P1 | `OBS-011-REC-003` | CLOSED_INTERNAL |
| `OBS-GAP-010` | Agent Instance identity | Use agent_instance_ref; no invented ID. | UPOS-011 | P1 | `OBS-011-REC-002` | CLOSED_INTERNAL |
| `OBS-GAP-011` | Missing Event detection | Requires capture expectation; silence alone is UNKNOWN. | UPOS-011 runtime bindings | P1 | `OBS-011-REC-003` | CLOSED_INTERNAL |
| `OBS-GAP-012` | Observability provenance vs domain provenance | Projection indexes upstream identities; owners retain relation semantics. | — | P1 | — | CLOSED |
| `OBS-GAP-013` | Read Model vs Source of Truth | Rebuildable, eventually consistent; owner wins drift. | — | P1 | — | CLOSED |
| `OBS-GAP-014` | Metric Definition vs Observation | Definition stable/versioned; observation tuple-addressed. | — | P1 | — | CLOSED |
| `OBS-GAP-015` | Metric vs Quality Verdict | Metrics consume UPOS-007; never redefine verdict. | — | P1 | — | CLOSED |
| `OBS-GAP-016` | Metric vs Learning signal | Metric may be learning evidence only. | UPOS-009 | P1 | `OBS-009-REC-*` | PENDING_EXTERNAL |
| `OBS-GAP-017` | Lead vs cycle time | Exact Task/Workflow boundaries defined. | — | P1 | — | CLOSED |
| `OBS-GAP-018` | active vs wait vs blocked | Separate semantics; queue/wait conditional. | UPOS-011 | P1 | `OBS-011-REC-010` | CLOSED_INTERNAL |
| `OBS-GAP-019` | Retry vs Rework metrics | Explicit owner relations only; never inferred from repetition. | — | P1 | — | CLOSED |
| `OBS-GAP-020` | CI telemetry vs Quality result | Check status remains UPOS-006; Quality result UPOS-007. | — | P1 | — | CLOSED |
| `OBS-GAP-021` | Cost vs usage | Usage raw; cost needs price basis/currency/calculation. | UPOS-011 | P1 | `OBS-011-REC-006/007` | CLOSED_INTERNAL |
| `OBS-GAP-022` | Multi-currency cost | No implicit sum; explicit FX basis required. | UPOS-011/project | P2 | `OBS-011-REC-007` | CLOSED_INTERNAL |
| `OBS-GAP-023` | Capacity vs utilization/productivity | Capacity is execution system; no person score. | — | P1 | — | CLOSED |
| `OBS-GAP-024` | Saturation denominator | Must be real configured capacity, not observed max. | UPOS-011 | P2 | `OBS-011-REC-011` | CLOSED_INTERNAL |
| `OBS-GAP-025` | Human planned vs unplanned | Use Workflow/Human Governance refs, not inference. | UPOS-010 partly | P1 | `OBS-010-REC-005` | CLOSED_INTERNAL |
| `OBS-GAP-026` | Human wait vs work | Separate; active work requires explicit instrumentation. | UPOS-011 | P2 | — | CLOSED_INTERNAL |
| `OBS-GAP-027` | System health vs Product Quality | Explicitly separate. | — | P1 | — | CLOSED |
| `OBS-GAP-028` | Event retention vs security retention | Event immutable while retained; policy external. | UPOS-010/011 | P1 | `OBS-010-REC-003/008` | PENDING_EXTERNAL |
| `OBS-GAP-029` | Sensitive telemetry | Abstract policy refs/minimization only. | UPOS-010 | P1 | `OBS-010-REC-*` | PENDING_EXTERNAL |
| `OBS-GAP-030` | Security event vs incident | Reference only; no incident ontology. | UPOS-010/operations | P1 | `OBS-010-REC-004` | PENDING_EXTERNAL |
| `OBS-GAP-031` | Telemetry event vs Learning Candidate | Learning semantics deferred. | UPOS-009 | P1 | `OBS-009-REC-*` | PENDING_EXTERNAL |
| `OBS-GAP-032` | Provider telemetry vs universal semantics | Adapter maps provider data to Module-08 contracts. | UPOS-011 | P1 | `OBS-011-REC-*` | PENDING_EXTERNAL |
| `OBS-GAP-033` | Dashboard state vs canonical state | Projection only; PROJECTION_DRIFT and owner-wins rule. | — | P1 | — | CLOSED |
| `OBS-GAP-034` | Causal cycles | Invalid telemetry integrity; CAUSATION_CYCLE. | — | P1 | — | CLOSED |
| `OBS-GAP-035` | Exact-once assumption | Not required; idempotent event_id semantics. | UPOS-011 transport | P2 | `OBS-011-REC-003` | CLOSED_INTERNAL |
| `OBS-GAP-036` | Escaped defect | Deferred until owner incident/defect attribution exists. | future owner | P2 | UPOS-009/operations future | DEFERRED |

No unresolved **internal** P0/P1 gap remains. Pending P1 items are explicit downstream reconciliation dependencies and block final freeze, not provisional implementation.
