# Ambiguity / Gap Register

**ID:** UPOS-11-AN-012  
**Type:** AMBIGUITY REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


| ID | Issue | Resolution | Status |
|---|---|---|---|
| PAD-GAP-001 | Manifest vs Project Knowledge | manifest only binds/configures; knowledge remains UPOS-01 | RESOLVED |
| PAD-GAP-002 | Adapter vs Runtime | adapter defines binding contracts; runtime executes later | RESOLVED |
| PAD-GAP-003 | Binding vs Policy | binding references/implements policy, never owns it | RESOLVED |
| PAD-GAP-004 | Provider capability vs U-POS Capability | provider capability is implementation mapping | RESOLVED |
| PAD-GAP-005 | Provider permission vs UPOS Permission | explicit inequality; UPOS-010 decides | RESOLVED |
| PAD-GAP-006 | Role vs provider identity | identity binding does not create authority | RESOLVED |
| PAD-GAP-007 | Quality criterion vs test command | command only produces evidence | RESOLVED |
| PAD-GAP-008 | Grant vs IAM scope | IAM scope enforces; Grant semantics remain 010 | RESOLVED |
| PAD-GAP-009 | secret_ref vs value | only ref in config; value excluded | RESOLVED |
| PAD-GAP-010 | Event vs provider event | normalized mapping preserves raw provenance | RESOLVED |
| PAD-GAP-011 | Metric definition vs backend query | query implements versioned 008 definition | RESOLVED |
| PAD-GAP-012 | Learning threshold vs configured value | value bound only by policy ref | RESOLVED |
| PAD-GAP-013 | project override vs invariant | invariant non-overridable | RESOLVED |
| PAD-GAP-014 | fallback vs reroute | adapter fallback is configured binding behavior; Workflow reroute remains 004 | RESOLVED |
| PAD-GAP-015 | provider failure vs domain failure | adapter failure remains owner-scoped | RESOLVED |
| PAD-GAP-016 | validation vs Quality | adapter validation != Quality Verdict | RESOLVED |
| PAD-GAP-017 | adapter health vs system health | distinct; 008 may observe adapter health | RESOLVED |
| PAD-GAP-018 | Manifest vs Adapter version | manifest config version vs semantic binding implementation version | RESOLVED |
| PAD-GAP-019 | binding drift vs source drift | provider/config realization drift only | RESOLVED |
| PAD-GAP-020 | Adapter vs Source of Truth | adapter never owns project truth | RESOLVED |
| PAD-GAP-021 | Adapter vs Control Plane | adapter exposes state; UI/read model remains consumer | RESOLVED |
| PAD-GAP-022 | 008–010 cyclic freeze dependency | two-phase interface convergence + coordinated freeze | RESOLVED |

```text
UNRESOLVED P0/P1 MODULE-11 GAPS = 0
```
