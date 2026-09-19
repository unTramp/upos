# Ambiguity & Gap Register

**ID:** UPOS-10-AN-AGR-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


| Topic | Resolution | Status |
|---|---|---|
| Authority vs Permission | UPOS-002 authority; UPOS-010 current technical permission | RESOLVED |
| Role vs Security Subject | Role is organizational attribute; executing subject is referenced identity, usually Agent Run/Human/Service | RESOLVED |
| Capability vs Tool | Capability is semantic power; Tool is technical mechanism | RESOLVED |
| Capability vs Permission | Capability availability does not authorize current use | RESOLVED |
| Permission Request vs Grant | Request asks for decision; Grant is bounded reusable allowance | RESOLVED |
| Permission Decision vs Grant | Decision is exact current evaluation; Grant is one decision input | RESOLVED |
| Grant vs delegation | Grant technical; delegation organizational UPOS-002 | RESOLVED |
| Grant vs authority | Grant cannot create authority | RESOLVED |
| Protected Action vs Workflow Gate | action security instance vs orchestration condition | RESOLVED |
| Human Approval vs Permission | approval is condition ref; current ALLOW still required | RESOLVED |
| Security Review vs Permission Decision | review assesses risk; decision authorizes/denies action | RESOLVED |
| Security Veto vs Quality Fail | independent owners/states | RESOLVED |
| Secret access vs Context inclusion | security access directive vs UPOS-005 representation | RESOLVED |
| Secret use vs disclosure | separate capabilities/effects | RESOLVED |
| Production access vs deployment Workflow | permission vs orchestration | RESOLVED |
| Break-glass vs exception | emergency route; exception only if policy departure | RESOLVED |
| Exception vs policy change | exception bounded; policy remains active | RESOLVED |
| Grant expiry vs revocation | natural end vs early authorized termination | RESOLVED |
| Technical permission vs provider IAM scope | universal semantics vs UPOS-011 mapping | RESOLVED/PENDING BINDING |
| Security Audit vs Observability Event | audit requirement semantics vs UPOS-008 projection | RESOLVED/PENDING INTERFACE |
| Learning signal contract | security outcome refs vs UPOS-009 semantics | PENDING RECONCILIATION |

```text
Unresolved internal P0/P1 Module-10 gaps = 0
External freeze blockers = UPOS-008 / UPOS-009 / UPOS-011 reconciliation only
```
