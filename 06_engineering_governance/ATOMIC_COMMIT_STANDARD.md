# Atomic Commit Standard

**ID:** UPOS-06-COM-001  
**Type:** COMMIT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SKL-CREATE-ATOMIC-COMMIT


## 1. Definition

```text
COMMIT
= smallest coherent logical repository change
  that is understandable, reviewable, attributable,
  and revertable as a semantic unit where practical
```

Atomic means one coherent engineering intent.

It does NOT mean:

```text
one edited line
one tool action
one Agent turn
one file
```

## 2. Core invariants

A governed Commit SHOULD:

- have one logical purpose;
- exclude unrelated cleanup;
- preserve approved/routed scope;
- be understandable independently;
- be reviewable;
- be attributable;
- be revertable where practical;
- keep the repository coherent where practical;
- separate mechanical and semantic changes where safely possible;
- avoid unnecessary generated/noise changes.

```text
COMMIT SIZE != COMMIT QUALITY
```

No universal LOC threshold exists.

## 3. Small coherent commits

Prefer small coherent commits because they improve reviewability, blame, revert, provenance, and risk reasoning.

Reject the anti-pattern:

```text
commit after every action
```

Use semantic checkpoints:

```text
one coherent logical change
→ self-check
→ atomic commit
```

## 4. Unrelated cleanup

```text
No opportunistic unrelated cleanup inside a governed change.
```

Discovered unrelated improvement becomes a separate Task/Engineering Change unless required to safely complete current scope.

## 5. Mechanical vs semantic changes

Where practical separate:

```text
mechanical refactor / rename / formatting
```

from:

```text
behavioral or semantic change
```

Do not force separation if it creates unsafe or invalid intermediate states.

## 6. Regression protection

Regression protection SHOULD be created before or with a bug fix where practical.

Valid project-policy forms include:

```text
test + fix in one atomic green commit
```

or, when history policy permits:

```text
failing-test commit
→ fix commit
```

Module 06 does not require universally red intermediate history.

Quality sufficiency remains UPOS-007.

## 7. Review-fix commits

Do not create one commit per review comment.

Group corrections by coherent engineering intent.

## 8. Commit identity

Use:

```text
commit_ref
```

as the universal reference to the VCS-native immutable commit identity.

Do not invent a redundant universal commit ID.

## 9. Message semantics

A commit message SHOULD communicate:

- intent;
- affected scope where useful;
- reason/context where useful.

Universal Module 06 does not force a string syntax or commit taxonomy.

Project-specific syntax belongs to UPOS-011.

## 10. History integrity

If a commit set reviewed/checked earlier is rewritten, old associations remain attributable to the old artifact identity.

They MUST NOT silently attach to new commit identities.
