# Skill Dependency and Composition

**ID:** UPOS-03-DEP-001  
**Type:** DEPENDENCY / COMPOSITION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Relationship types

UPOS-003 defines:

```text
REQUIRES
OPTIONALLY_USES
COMPOSES_WITH
SUPERSEDES
CONFLICTS_WITH
```

## 2. REQUIRES

The Skill cannot satisfy its contract without the dependency capability/result.

`REQUIRES` does not automatically define Workflow order. UPOS-004 owns organizational sequencing.

## 3. OPTIONALLY_USES

The dependency can improve execution but is not required for contract conformance.

## 4. COMPOSES_WITH

Two Skills are explicitly compatible for bounded composition.

The relation does not imply either is mandatory.

## 5. SUPERSEDES

A newer/different Skill replaces the semantic capability of another Skill.

Supersession must align with lifecycle/versioning.

## 6. CONFLICTS_WITH

Two Skill Definitions cannot safely be applied to the same responsibility/result under stated conditions.

## 7. Composition rules

Composition MUST be:

- explicit;
- bounded;
- traceable;
- contract-compatible;
- non-circular where a cycle makes responsibility/execution ambiguous.

## 8. No hidden Workflow

Skill composition MUST NOT be used to encode a full multi-role Workflow.

If composition requires:

- organizational role routing;
- human gates;
- cross-role handoffs;
- merge/release sequencing;
- retry/recovery across stages;

the structure belongs in UPOS-004.

## 9. Mega-skill guardrail

A candidate mega-skill such as `build-entire-feature` SHOULD be rejected or split when its procedure merely hides:

```text
specification
→ implementation
→ independent review
→ QA
→ merge
```

That is organizational composition, not one bounded capability.
