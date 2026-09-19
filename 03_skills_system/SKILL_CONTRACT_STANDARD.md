# Skill Contract Standard

**ID:** UPOS-03-SCS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/SKILL_CONTRACT_TEMPLATE.md


## 1. Requirement

Every production-grade universal Skill MUST have a versioned Skill Contract.

## 2. Mandatory fields

A Skill Contract MUST contain:

```text
Identity
Purpose
Category
Scope
Non-scope

Inputs
Outputs

Preconditions
Postconditions where meaningful

Required Source Classes
Optional Source Classes

Required Context Interface
Tool Interface Requirements
Permission Interface Requirements

Applicable Roles
Applicable Work/Risk Constraints by reference

Procedure
Procedural Invariants

Quality Criteria
Validation Requirements

Failure Modes
Escalation Conditions

Dependencies
Composition Rules

Prohibited Behavior

Lifecycle
Version

Related Skills
Replacement / Supersession if applicable
```

## 3. Identity

Minimum identity:

- stable `skill_id`;
- canonical name;
- version;
- lifecycle status;
- primary category.

`skill_id` SHOULD remain stable across compatible versions.

## 4. Inputs and outputs

Inputs and outputs MUST describe semantic data, not a specific provider prompt format.

Inputs SHOULD identify whether a value is:

- required;
- optional;
- canonical-context reference;
- evidence reference;
- task-local material.

Outputs MUST define the expected Skill Result class.

## 5. Source classes

A Skill MUST declare required canonical Source Classes when its correctness depends on project truth.

It MUST NOT hard-code repository paths.

Example:

```text
Required Source Classes:
- Product Contract
- Architecture Contract
- relevant Decision Records
```

Physical resolution is external.

## 6. Context interface

The contract may state required context characteristics.

It MUST NOT define:

- retrieval algorithm;
- authority weighting;
- context budget;
- freshness algorithm;
- memory policy.

Those belong to UPOS-005.

## 7. Tool interface

Tool requirements MUST normally be capability-based, e.g.:

```text
repository-read
repository-write
diff-inspection
test-execution
search
document-write
```

Concrete tool/provider binding belongs to UPOS-011.

## 8. Permission interface

A Skill may declare required permission capabilities.

It MUST NOT grant them.

Example:

```text
create-atomic-commit requires a commit-capable interface
```

Who may receive that permission and under what repository policy is external.

## 9. Applicable roles

`Applicable Roles` means the Skill is semantically compatible with those Roles.

It does not alter Role authority.

## 10. Work/risk constraints

A Skill may reference externally owned work/risk constraints.

It MUST NOT redefine canonical C0–C5 semantics or Workflow consequences.

## 11. Procedure

Procedure is the bounded reusable method owned by the Skill.

It SHOULD be:

- ordered only where order is intrinsic to the capability;
- small enough to evaluate;
- independent of full multi-role orchestration.

## 12. Quality criteria

Quality criteria define what correct execution of the Skill means at the Skill Contract level.

They MUST avoid replacing downstream Quality verdict semantics.

## 13. Failure and escalation

Skill-specific failures include:

- missing required semantic input;
- violated precondition;
- ambiguous result;
- inability to satisfy output contract;
- detected boundary breach;
- unavailable required interface.

The Skill MUST escalate rather than invent missing authority or canonical project truth.

## 14. Dependencies

Dependencies MUST use explicit relationships defined by `SKILL_DEPENDENCY_AND_COMPOSITION.md`.

## 15. Lifecycle/version

Every Skill Definition MUST declare lifecycle and version under the Module 03 lifecycle/versioning standards.
