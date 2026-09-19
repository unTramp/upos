# Independent Verification

**ID:** UPOS-07-IVS-001  
**Type:** INDEPENDENT VERIFICATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-002 SoD, UPOS-005 Context isolation


## 1. Organizational independence

Consume from UPOS-002:

```text
Implementer != Final Reviewer
```

For high-risk:

```text
Implementer != Reviewer != Merge Controller
```

UPOS-007 does not redefine these authority rules.

## 2. Verification independence

When independent verification is required, Quality evidence must demonstrate that the verifier:

- satisfies applicable UPOS-002 SoD/Role constraints;
- receives authoritative Role-appropriate Context through UPOS-005;
- evaluates the actual exact target via UPOS-006 refs;
- produces its own criterion evaluations/Findings/Evidence rather than ratifying producer claims.

## 3. Independence states

Assessment records:

```text
SATISFIED
VIOLATED
UNRESOLVED
NOT_REQUIRED
```

with `independence_basis_refs`.

## 4. Independence violation

If a prohibited same Role/Run relationship performed required independent verification:

```text
independence evidence = invalid for that requirement
```

The work may still contain useful self-check evidence, but it does not count as independent evidence.

## 5. Self-check

Implementer self-check is useful Quality evidence when attributable.

```text
SELF_CHECK != INDEPENDENT_REVIEW
```

It cannot replace required independent verification.

## 6. Reviewer Context

UPOS-007 consumes `context_bundle_id`.

It does not retrieve or assemble Context.

Producer private scratch/chain-of-thought is not required for Reviewer verification and is not independent evidence.

## 7. Reviewer fixes

Default separation remains:

```text
Reviewer finds
→ Implementer fixes
→ Reviewer re-reviews
```

Workflow/rework sequencing remains UPOS-004.
