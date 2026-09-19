# Quality Operating Model

**ID:** UPOS-07-QOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_ONTOLOGY.md, QUALITY_ASSESSMENT_STANDARD.md


## 1. Governing principle

A change is not correct because an Agent, Reviewer, QA Role, CI system, or Merge Controller claims it is correct.

Quality acceptance requires criterion-specific evidence appropriate to the target, scope and risk.

## 2. Quality is evaluation, not truth creation

UPOS-007 evaluates:

```text
Does the target satisfy the applicable governed criteria?
```

It MUST NOT decide:

```text
What should Product/Domain/Architecture mean?
```

Criterion meaning resolves through UPOS-01 canonical owners/sources.

## 3. Minimal-friction objective

Optimize for:

```text
right criteria
+
right evidence
+
right independence
+
exact artifact attribution
+
explicit uncertainty
+
reproducible verdicts
+
minimal unnecessary friction
```

Not for maximum tests/reviewers/findings/gates.

## 4. Evidence before verdict

Evidence is support.

Verdict is a conclusion produced by an Assessment.

```text
EVIDENCE != VERDICT
```

Large volumes of irrelevant or stale evidence do not produce stronger quality.

## 5. Risk-aware depth

UPOS-007 consumes Change Class and Concern Profile references from UPOS-004.

Higher-risk work MAY require stronger:

- evidence diversity;
- independence;
- specialist/external results;
- acceptance-criteria precision;
- regression protection;
- freshness requirements.

UPOS-007 MUST NOT reclassify the change.

## 6. Quality Policy decision

UPOS-007 v1 adopts a **Quality Policy** concept, not a Quality Profile concept.

```text
Workflow Profile
→ WHEN / WHO / stages / orchestration

Quality Policy
→ WHAT criteria/evidence/independence are required
```

This prevents duplication of UPOS-004 profiles.

## 7. No universal testing dogma

UPOS-007 does not universally mandate:

```text
coverage percentage
reviewer count
test pyramid
specific browser/device matrix
specific performance threshold
specific CI provider/tool
```

Such requirements must come from governed universal/project policy and UPOS-011 mappings.

## 8. Provider independence

Quality semantics remain independent of Git hosting, CI vendor, test framework, scanner, browser tool, or programming language.

## 9. Quality result is not organizational authority

A `PASS` or quality readiness result does not grant permission, authority, or merge capability.

It is one governed input to downstream orchestration/authority.
