# Skill Candidate Classification

**ID:** UPOS-03-AN-004  
**Type:** ANALYSIS / CANDIDATE CLASSIFICATION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** ../SKILL_REGISTRY_STANDARD.md

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Classification vocabulary

```text
CANONICAL_UNIVERSAL_SKILL
INTERFACE_SKILL
SHOULD_SPLIT
DEFERRED_TO_OTHER_MODULE
PROJECT_SPECIFIC
REDUNDANT
```

## Results

| Candidate | Disposition | Primary category | Rationale |
|---|---|---|---|
| `classify-change` | INTERFACE_SKILL | `classification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `assemble-context` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `analyze-impact` | CANONICAL_UNIVERSAL_SKILL | `analysis` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-feature-spec` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-rfc` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-adr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-pdr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-ddr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-implementation-plan` | CANONICAL_UNIVERSAL_SKILL | `planning` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `reproduce-bug` | CANONICAL_UNIVERSAL_SKILL | `analysis` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `write-regression-test` | CANONICAL_UNIVERSAL_SKILL | `implementation` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `implement-change` | CANONICAL_UNIVERSAL_SKILL | `implementation` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-atomic-commit` | INTERFACE_SKILL | `implementation` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-diff` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-architecture` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-security` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `qa-validation` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `reconcile-documentation` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `assess-merge-readiness` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `prepare-release` | INTERFACE_SKILL | `operations` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `analyze-incident` | CANONICAL_UNIVERSAL_SKILL | `operations` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `capture-learning` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |

## Summary

- `CANONICAL_UNIVERSAL_SKILL`: 11
- `INTERFACE_SKILL`: 11
- `SHOULD_SPLIT`: 0
- `DEFERRED_TO_OTHER_MODULE`: 0 among the frozen starter candidates
- `PROJECT_SPECIFIC`: 0
- `REDUNDANT`: 0

No candidate was accepted mechanically. Interface Skills were deliberately bounded so they do not steal downstream ownership.
