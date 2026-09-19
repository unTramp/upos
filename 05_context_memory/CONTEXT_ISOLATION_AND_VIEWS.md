# Context Isolation & Views

**ID:** UPOS-05-CIV-001  
**Type:** ISOLATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-002 Agent Organization


## 1. Context View

A Context View is a bounded projection of eligible Context for one consumer/purpose.

A View may differ by:

```text
Role
authority scope reference
Workflow Stage
Skill
Agent Run
permissions
independence constraints
Change Class / Concern
```

Seeing information never grants authority over its fact scope.

## 2. Role-aware examples

### Product
Intent, requirements, constraints, relevant evidence/decisions.

### Architecture
Product intent + Domain contracts + current architecture + relevant decisions/evidence.

### Implementer
Approved plan + applicable contracts + implementation surface + tests.

### Reviewer
Authoritative requirements/contracts + diff + relevant tests/evidence + decisions.

### QA
Expected behavior + acceptance/risk scenarios + testable change, not merely producer narrative.

### Merge Controller
Structured gate/readiness evidence, not full implementation reasoning.

### Human decision-maker
Focused decision packet with canonical sources/options/evidence/risks/conflicts.

## 3. Reviewer independence

Critical invariant:

```text
producer context
!= reviewer authoritative context
```

Reviewer MUST NOT automatically inherit:

- Implementer scratch reasoning;
- private chain-of-thought;
- unverified assumptions;
- self-approval claims;
- producer-only Run Working Memory.

Reviewer independently receives required authoritative sources.

Producer notes MAY be included only when explicitly relevant and labeled as producer-provided, non-independent material.

## 4. Same underlying model/provider

The same base model/provider may power different Roles only when UPOS-002 logical separation is preserved.

Module 05 supports this by keeping Context Requests/Bundles and working memory scoped separately per Role/Run.

## 5. QA independence

QA SHOULD begin from expected behavior/contracts and risks.

Implementation details can be supplemental, not the sole basis of the QA View.

## 6. Cross-project isolation

Default invariant:

```text
Project A Context
MUST NOT leak into
Project B Context
```

Cross-project/federated knowledge requires an explicit authorized mechanism.

Project identity/mappings remain UPOS-011; access grants remain UPOS-010.

## 7. Cross-task isolation

Task Working Memory from Task A MUST NOT automatically become Context for Task B.

Permitted reuse requires one of:

- governed canonical project knowledge;
- explicit governed reusable artifact;
- validated historical evidence relevant to current scope;
- explicit authorized source reference.

## 8. Sensitive Context isolation

UPOS-005 applies minimum-necessary inclusion/redaction/reference-only constraints returned by UPOS-010.

It does not define access policy.

## 9. Context contamination detection

Detected wrong-project/wrong-version/private-memory/producer-bias contamination makes affected material ineligible and may invalidate the Bundle.
