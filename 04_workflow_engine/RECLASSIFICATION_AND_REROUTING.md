# Reclassification and Rerouting

**ID:** UPOS-04-RCR-001  
**Type:** RECLASSIFICATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Mandatory reclassification rule

A Workflow MUST NOT silently continue under stale classification after material new risk/impact is discovered.

## 2. Reclassification triggers

Triggers include:

- new architecture decision required;
- previously unknown database/data migration;
- security/auth/privacy/protected-action impact;
- expanded Product/Domain semantics;
- new external API compatibility impact;
- discovered cross-module breadth;
- production blast radius materially higher than known;
- irreversibility/destructive action discovered;
- missing/conflicting canonical truth affecting risk;
- scope expansion beyond current route;
- plan material change.

## 3. Upward reclassification

Always permitted when justified by new evidence.

Current Workflow Instance MUST pause or block before executing stages invalid under the higher class.

## 4. Downward reclassification

Requires explicit evidence that the higher-risk signal no longer applies.

Downward reclassification MUST NOT be used to bypass required gates/approvals already materially triggered.

## 5. What remains valid

After reclassification, completed outputs may be reused only if:

- their producing contract/version is still compatible;
- required sources remain valid;
- stronger SoD/gates do not invalidate independence;
- no changed assumption affects correctness.

Otherwise they MUST be rechecked/reworked.

## 6. Rerouting

Reclassification may cause:

```text
same base workflow + deeper class
same base workflow + added profiles
different base workflow
task decomposition
terminal escalation
```

Old routing provenance remains preserved.

## 7. Scope expansion

When execution discovers extra work:

```text
pause
→ classify discovered work
→ decide:
   required for current task?
   separate follow-up?
   new concern?
   higher change class?
   different base work type?
```

No silent scope expansion.

## 8. Risk inheritance

If an inseparable sub-change is C5, the containing route inherits C5 protected orchestration.

If it can be safely separated, split by coherent ownership/dependency rather than arbitrary file count.
