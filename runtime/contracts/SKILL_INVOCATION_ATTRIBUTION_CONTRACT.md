# Skill Invocation Attribution Contract

**ID:** UPOS-03-SKILL-INVOCATION-ATTRIBUTION  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-03  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents Skill/version, bounded SkillInvocationRef, AgentRunRef, Task/Workflow/Stage attribution and owner Skill Result references without owning technical execution state.

## Required boundaries

- preserve canonical Skill and SkillInvocation identities;
- technical attempt state and retry remain UPOS-04 concerns;
- Skill Result semantics remain UPOS-03-owned;
- no duplicate invocation or execution-attempt identity.

## Machine representation

- schema: `schemas/03/skills/skill-invocation-attribution.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `03_skills_system/SKILLS_OPERATING_MODEL.md`
- `03_skills_system/SKILL_LIFECYCLE.md`
