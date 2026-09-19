# Workflow Profile / Overlay Standard

**ID:** UPOS-04-PRF-001  
**Type:** PROFILE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** profiles/*.md


## 1. Definition

A Workflow Profile is a reusable orchestration modifier applied to a compatible Base Workflow.

It represents a cross-cutting concern, not a competing primary Workflow.

## 2. A Profile may add

- Role participation references;
- Skill references;
- stages/checkpoints;
- stage dependencies;
- external gate references;
- approval references;
- handoff references;
- reclassification triggers;
- conditional minimum Change Class rules;
- completion requirements attributable to the concern.

## 3. A Profile may not

- redefine Role authority;
- copy Skill procedures;
- define Context retrieval;
- define Git mechanics;
- define Quality verdict/evidence semantics;
- grant permissions;
- bind concrete providers/commands/paths.

## 4. Profile compatibility

A Profile MUST declare:

```text
profile_id
version
compatible_work_types
conflicts
dependencies
risk implications
added roles
added skill references
added/modified stages
external gate references
reclassification triggers
```

## 5. Composition

Multiple Profiles MAY compose if:

- their stage dependencies are non-contradictory;
- Role/SoD constraints remain satisfiable;
- no profile conflicts are declared;
- required gates/approvals can all be represented;
- resulting workflow remains bounded and understandable.

## 6. Precedence

Profiles can only tighten the Base Workflow.

They MUST NOT remove a mandatory base requirement unless the base contract explicitly declares that requirement conditional and the profile resolves it safely.

Higher Change Class requirements override weaker profile/base defaults.

## 7. Conflict handling

Profile conflict:

```text
pause routing
→ identify conflicting orchestration requirements
→ reclassify / choose compatible base / decompose / escalate
```

No silent precedence guessing.
