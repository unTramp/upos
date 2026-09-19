# Security Policy Standard

**ID:** UPOS-10-SPS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Policy reference model

UPOS-010 evaluates versioned Security Policy through:

```text
security_policy_ref
security_policy_version
```

`security_policy_ref` resolves to the governed canonical project/security source under UPOS-01 ownership rules.

UPOS-010 does not introduce a second global `security_policy_id` or independent policy database.

## 2. Policy content interface

A Security Policy may define:

```text
applicability
subject classes/attributes
resource classes/scopes
capability/action rules
default behavior
conditions
required authority refs
required approvals
SoD constraints
protected-action classifications
secret/sensitive-data controls
production/elevated access controls
exception eligibility
expiry/revalidation behavior
audit requirements
telemetry/audit sensitivity classifications where applicable
telemetry/audit redaction directives where applicable
telemetry/audit access constraints where applicable
telemetry/audit retention constraints where applicable
```


## 2.1 Observability security-handling interface

Where Security/Privacy policy constrains telemetry or audit material, UPOS-010 may expose policy-scoped handling references/directives without creating new global policy identities:

```text
security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

These values express security constraints only. UPOS-008 owns Event/Trace/storage/projection/retention mechanics under those constraints; UPOS-011 binds concrete storage/access/redaction/retention enforcement.

## 3. Canonicality

If applicable active normative Security sources conflict:

```text
DO NOT GUESS
→ BLOCKED / POLICY_CONFLICT
→ resolve canonical owner through UPOS-01 governance
```

## 4. Policy precedence

A more specific rule may refine a broader rule only where upstream security policy permits refinement and no stronger security rule is weakened.

UPOS-010 does not invent a universal numeric policy precedence system beyond canonical source resolution + explicit policy specificity/deny rules.

## 5. Deny-over-allow

Where the canonical policy defines explicit deny precedence for overlapping rules, that rule is honored.

Absent such a declared combination rule, conflicting applicable rules are `POLICY_CONFLICT`, not guessed.

## 6. Versioning

Every Permission Decision MUST record the exact `security_policy_ref` and `security_policy_version` used.

Material changes to authorization semantics require policy version change under the owning documentation/security governance.

## 7. Decision reproducibility

A decision should be explainable from:

```text
subject refs
execution scope
capability/action
resource/scope
policy ref/version
grant state
approval/authority refs
exception refs
security context refs
time
```

External provider state may prevent byte-identical replay, but the rule path and reason must remain attributable.
