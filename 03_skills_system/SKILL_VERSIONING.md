# Skill Versioning

**ID:** UPOS-03-VER-001  
**Type:** VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

Skill Definitions MUST be versioned when behavior materially changes.

U-POS v1 uses semantic versioning as a governance convention, independent of package-manager technology.

## 2. MAJOR

Increment MAJOR when compatibility is broken, including:

- incompatible input contract change;
- incompatible output contract/result class change;
- fundamental procedure semantic change;
- removal/reinterpretation of mandatory precondition;
- breaking change to dependencies/composition;
- breaking downstream expectation;
- changed failure/escalation behavior that invalidates existing consumers.

## 3. MINOR

Increment MINOR for backward-compatible capability expansion, including:

- optional input;
- optional source class;
- backward-compatible procedure refinement;
- additional validation that does not invalidate conforming consumers;
- new compatible applicable Role.

## 4. PATCH

Increment PATCH for non-semantic/editorial correction, clarification, typo, example repair, or wording that does not change execution obligations.

## 5. Material-change rule

When uncertain whether a change is PATCH or MINOR/MAJOR, evaluate whether a conforming existing invoker or evaluator could observe different required behavior.

If yes, it is not a PATCH.

## 6. Version and lifecycle

A new MAJOR version may coexist temporarily with a deprecated prior version.

Registry/supersession must make active recommendations explicit.
