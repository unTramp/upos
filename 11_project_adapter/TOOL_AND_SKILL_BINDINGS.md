# Tool and Skill Bindings

**ID:** UPOS-11-TSB-001  
**Type:** BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Skill boundary

UPOS-003 owns Skill Definition/procedure.

UPOS-011 MAY bind:

```text
skill_id/version
→ concrete Skill implementation ref
```

and:

```text
Skill-required capability
→ tool/provider/runtime binding
```

## Tool classes

Examples of abstract tool capabilities:

```text
repository
filesystem
browser
database
CI
issue tracker
documentation source
artifact store
```

These are categories, not mandatory providers.

## Prohibition

A tool being technically available MUST NOT imply:

```text
organizational authority
permission
workflow eligibility
quality approval
```
