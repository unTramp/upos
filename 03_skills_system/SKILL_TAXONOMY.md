# Skill Taxonomy

**ID:** UPOS-03-TAX-001  
**Type:** TAXONOMY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Purpose

Taxonomy exists for discovery and governance, not bureaucracy.

## 2. Primary categories

UPOS-003 v1 retains the frozen-source baseline because the categories are broad, non-overlapping enough for discovery, and do not encode Workflow sequence:

1. `classification`
2. `planning`
3. `analysis`
4. `specification`
5. `implementation`
6. `verification`
7. `governance`
8. `operations`

Each Skill MUST have exactly one primary category.

## 3. Capability tags

A Skill MAY additionally use lightweight capability tags.

Examples:

```text
decision-record
architecture
security
documentation
testing
git-interface
context-interface
learning-interface
incident
release
```

Tags MUST NOT become hidden categories with independent governance.

## 4. Category semantics

### classification
Transforms described work/material into a structured classification recommendation against an externally owned classification model.

### planning
Produces bounded execution/planning artifacts.

### analysis
Produces structured analysis/evidence without directly changing implementation.

### specification
Produces normative-candidate or proposal artifacts describing desired behavior/decisions.

### implementation
Creates or modifies implementation artifacts under an approved scope.

### verification
Checks an artifact/behavior against externally owned contracts/criteria.

### governance
Maintains governed documentation/decision/readiness relationships without acquiring the authority of those owners.

### operations
Prepares/analyzes operational execution such as releases or incidents without silently owning operational Workflow sequencing.

## 5. Anti-proliferation rule

Do not create a new primary category merely because one Skill is difficult to classify.

Prefer a stable primary category plus tags unless a recurring family with materially distinct governance semantics emerges.
