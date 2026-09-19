# UPOS-008 Interface Reconciliation Register

**ID:** UPOS-11-AN-R008-001  
**Type:** INTERFACE RECONCILIATION REGISTER  
**Status:** ACTIVE  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** TEMPORARY  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Baseline

```text
UPOS-008 SHA-256: e6eed6e9d7e006a5bf3a3d9baa300d8917f6d9ccb3e76c6301a9fcef1b25a0ba
UPOS-011 side: RESOLVED
```

| Need from UPOS-008 | Module-11 binding | Status |
|---|---|---|
| project_ref | Project Manifest `project_id` / source binding | RESOLVED |
| agent_instance_ref | identity/runtime provider binding | RESOLVED |
| event sink / Event Store | Observability Binding | RESOLVED |
| trace backend/exporter | Observability Binding | RESOLVED |
| trace carrier | Observability Binding | RESOLVED |
| metric backend/query | Observability Binding | RESOLVED |
| projection store/datasource | Observability Binding | RESOLVED |
| provider usage | provider usage adapter binding | RESOLVED |
| pricing basis | pricing source binding | RESOLVED |
| clock source | clock binding | RESOLVED |
| repository/CI/provider events | provider event adapter binding | RESOLVED |
| queue/capacity signals | runtime/provider signal binding | RESOLVED |
| sampling | observability implementation binding | RESOLVED |
| projection watermark | projection backend binding | RESOLVED |

## Boundary

UPOS-008 remains owner of Event/Trace/Metric/Read Model semantics.

## Closure

```text
MATERIAL UPOS-008 ↔ UPOS-011 CONFLICTS = 0
UPOS-011-SIDE RECONCILIATION = COMPLETE
```

Current UPOS-008 pending register still requires a narrow canonical status/traceability update before coordinated freeze.
