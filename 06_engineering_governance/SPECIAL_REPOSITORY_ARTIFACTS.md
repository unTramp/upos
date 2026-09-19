# Special Repository Artifacts

**ID:** UPOS-06-SRA-001  
**Type:** SPECIAL ARTIFACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Generated artifacts

Generated files are first-class repository artifacts when required by their source change.

Governance SHOULD ensure:

- source/generator relationship is attributable;
- generated output is reproducible where practical;
- unrelated generated noise is excluded;
- manual edits to generated output are prohibited unless the project explicitly permits them;
- generator/source mismatch is surfaced;
- generated artifacts are included in the same coherent Commit/Integration Request when they are required for the source change.

Generator commands/provider bindings belong to UPOS-011.

Quality verification belongs to UPOS-007.

## 2. Lockfiles / dependency manifests

Dependency-related lockfiles/manifests are first-class artifacts when required for a dependency change.

Avoid unrelated dependency churn.

Dependency classification/routing remains UPOS-004.

## 3. Database migration files

UPOS-006 governs repository mechanics:

- ordering references;
- file/sequence collision detection;
- change attribution;
- commit/branch/Integration Request handling.

Database/data migration safety semantics remain external to Module 06.

## 4. Documentation artifacts in engineering change

Documentation MAY live in the same Integration Request when it is part of the same coherent intention.

Canonical documentation truth/ownership remains UPOS-01.

Documentation Guardian authority remains UPOS-002.

Quality semantics remain UPOS-007.
