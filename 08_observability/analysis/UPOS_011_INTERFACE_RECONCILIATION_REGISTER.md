# UPOS-011 Interface Reconciliation Register

**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Result

```text
UPOS-008 ↔ UPOS-011 = RECONCILED
Material unresolved items = 0
```

| ID | Abstract need | Final Module-11 binding interface | Status |
|---|---|---|---|
| `OBS-011-REC-001` | project identity | canonical `project_id` from Project Manifest | RESOLVED |
| `OBS-011-REC-002` | Agent Instance runtime identity | identity/provider binding for `agent_instance_ref` | RESOLVED |
| `OBS-011-REC-003` | Event sink/Event Store | Observability Binding / provider adapter | RESOLVED |
| `OBS-011-REC-004` | Trace propagation | trace carrier/exporter/provider binding | RESOLVED |
| `OBS-011-REC-005` | Metric/read-model execution | metric/query backend, projection store, Control Plane datasource | RESOLVED |
| `OBS-011-REC-006` | provider usage | provider usage API/source mapping | RESOLVED |
| `OBS-011-REC-007` | pricing basis | pricing source + effective version/date + currency binding | RESOLVED |
| `OBS-011-REC-008` | clock/time source | clock/time-source binding | RESOLVED |
| `OBS-011-REC-009` | repository/CI/provider Events | provider event adapter preserving raw provenance | RESOLVED |
| `OBS-011-REC-010` | queue boundaries | queue/capacity signal-source binding | RESOLVED |
| `OBS-011-REC-011` | capacity denominator | runtime/provider capacity signal binding | RESOLVED |
| `OBS-011-REC-012` | sampling | concrete sampler respecting capture policy/importance | RESOLVED |
| `OBS-011-REC-013` | projection watermark | projection watermark/cursor source | RESOLVED |
| `OBS-011-REC-014` | OTel-like compatibility | optional provider mapping; OpenTelemetry is not U-POS ontology | RESOLVED |

UPOS-011 owns physical binding/resolution only; UPOS-008 retains Observability semantics.
