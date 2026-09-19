# Source Section Disposition

**ID:** UPOS-10-AN-DISP-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Frozen master disposition

| Frozen source area | Disposition |
|---|---|
| Human Governance / authority | DEFERRED_TO_UPOS_002, consumed by 010 |
| Least privilege | EXTRACTED_TO_MODULE_10 |
| Security Agent authority | MIXED: authority → 002; security permission semantics → 010 |
| Permissions model | EXTRACTED_TO_MODULE_10 |
| Role permission philosophy | MIXED: Role/authority → 002; capability/permission → 010 |
| Human approval model | MIXED: authority → 002; approval-condition semantics → 010 |
| Security gate | MIXED: placement → 004; security result → 010 |
| Guardrails / permission change / production deploy | MIXED: workflow/mechanics external; permission rule → 010 |
| Escalation | DEFERRED_TO_UPOS_004/002; 010 emits reason/result |
| Secrets safety | EXTRACTED_TO_MODULE_10; provider implementation → 011 |
| Production access | EXTRACTED_TO_MODULE_10; operation workflow/provider implementation external |
| Protected files | EXTRACTED as resource/protected-action semantics; concrete paths → 011 |
| Authority conflict resolution | DEFERRED_TO_UPOS_002/01; 010 consumes authority refs |
| Security veto | MIXED: veto authority → 002; DENY/veto enforcement semantics → 010 |
| Human override | MIXED: override authority → 002; policy exception/override applicability → 010 |
| Observability/metrics | DEFERRED_TO_UPOS_008 |
| Learning/evolution | DEFERRED_TO_UPOS_009 + 01 |
| Project manifest/provider scopes | DEFERRED_TO_UPOS_011 |

## Directive disposition

Sections `0–89` were reviewed. Requirements owned by Module 10 are implemented in normative artifacts. Cross-module mechanics are referenced/deferred to their declared owner. The only intentional provisional items are the explicit 008/009/011 interface reconciliations.
