# Project Documentation Catalog v1.0

**ID:** DOC-REF-001  
**Type:** REFERENCE  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** LIVING  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** A new canonical documentation class/layer is introduced  
**Supersedes:** —  
**Related:** DOC-STD-001


# Purpose

This catalog answers:

> What kinds of project documentation may exist, who owns them, and when are they warranted?

It is not a command to create every file.

---

# 1. Governance

Typical:

```text
docs/README.md
SOURCE_OF_TRUTH.md
DOCUMENTATION_OPERATING_MODEL.md
DOCS_AS_CODE_STANDARD.md
GLOSSARY.md
DOCUMENT_MANIFEST.json
TRACEABILITY.md
```

Create when:

- project has multiple active document classes;
- multiple contributors/AI agents need precedence;
- documentation drift becomes costly.

---

# 2. Product

Typical:

```text
PRODUCT_VISION.md
PRODUCT_PRINCIPLES.md
USER_PROBLEMS_JTBD.md
PERSONAS.md
SCOPE.md
SUCCESS_CRITERIA.md
BUSINESS_RULES.md
```

Owner:

```text
Product
```

Purpose:

- why product exists;
- who it serves;
- outcomes;
- product boundaries.

---

# 3. Domain

Typical:

```text
DOMAIN_MODEL.md
DOMAIN_GLOSSARY.md
ENTITY_CATALOG.md
LIFECYCLES.md
OWNERSHIP_BOUNDARIES.md
INVARIANTS.md
```

Owner:

```text
Domain / Architecture
```

Purpose:

- canonical meaning independent of UI/database.

---

# 4. Architecture

Typical:

```text
MASTER_ARCHITECTURE.md
SYSTEM_CONTEXT.md
CONTAINER_VIEW.md
COMPONENT_VIEW.md
DATA_FLOW.md
TRUST_BOUNDARIES.md
NON_FUNCTIONAL_REQUIREMENTS.md
```

Architecture decisions live under Decision History.

---

# 5. Product / Feature Contracts

Typical feature folder:

```text
feature/
├── PRODUCT_SPEC.md
├── UX_FLOW.md
├── API_CONTRACT.md
├── TEST_MATRIX.md
└── assets/
```

Small features MAY use one file.

Feature spec owns feature behavior, not global architecture.

---

# 6. UX / Experience

Typical:

```text
UX_CONSTITUTION.md
INFORMATION_ARCHITECTURE.md
NAVIGATION_MODEL.md
USER_FLOWS.md
CONTENT_DESIGN.md
ACCESSIBILITY_UX.md
research/
```

UX owns:

- experience principles;
- navigation semantics;
- information hierarchy;
- user-flow intent;
- product language.

UX does not own backend/domain truth.

---

# 7. Design System

Canonical module:

```text
DESIGN_SYSTEM_OPERATING_MODEL.md
DESIGN_HANDOFF_STANDARD.md
UI_KIT_WEB_SPECIFICATION.md
DESIGN_SYSTEM_PROFILE.md
REGISTRY.json
CHANGELOG.md
foundations/
primitives/
components/
patterns/
page-grammars/
boards/
implemented/
deprecated/
```

Design System owns reusable visual/interaction language.

It does not own whole product flows or temporary migration plans.

---

# 8. Engineering

Typical:

```text
ENGINEERING_PRINCIPLES.md
CODEBASE_GUIDE.md
FRONTEND_ARCHITECTURE.md
BACKEND_ARCHITECTURE.md
STATE_MANAGEMENT.md
ERROR_HANDLING.md
CONCURRENCY_IDEMPOTENCY.md
JOBS_WORKERS.md
STORAGE_MEDIA.md
INTEGRATIONS.md
OBSERVABILITY.md
PERFORMANCE.md
coding-standards/
```

---

# 9. Data / API / Integration

Typical:

```text
DATA_MODEL.md
DATABASE_SCHEMA.md
API_CONTRACTS.md
EVENT_CONTRACTS.md
DATA_MIGRATIONS.md
RETENTION.md
IMPORT_EXPORT.md
API_VERSIONING.md
```

Prefer generated OpenAPI/DB diagrams where appropriate, with human context separately.

---

# 10. AI

Create only when AI materially affects product/system.

Typical:

```text
AI_SYSTEM_OVERVIEW.md
AI_PRINCIPLES.md
MODEL_PROVIDER_BOUNDARIES.md
PROMPT_CONTRACTS.md
CONTEXT_ASSEMBLY.md
HUMAN_APPROVAL.md
EVALS.md
SAFETY_GUARDRAILS.md
AI_TELEMETRY.md
```

---

# 11. Security / Privacy

Typical:

```text
SECURITY_MODEL.md
THREAT_MODEL.md
AUTHENTICATION.md
AUTHORIZATION.md
SECRETS.md
PRIVACY.md
DATA_CLASSIFICATION.md
AUDIT_LOGGING.md
compliance/
```

---

# 12. Quality / Testing

Typical:

```text
QUALITY_STRATEGY.md
TESTING_STANDARD.md
TEST_PYRAMID.md
E2E.md
ACCESSIBILITY_TESTING.md
PERFORMANCE_TESTING.md
VISUAL_REGRESSION.md
TEST_DATA.md
DEFINITION_OF_DONE.md
reports/
evidence/
```

Reports/evidence are not design-system truth.

---

# 13. Analytics / Telemetry

Typical:

```text
ANALYTICS_STRATEGY.md
EVENT_TAXONOMY.md
METRIC_CATALOG.md
KPI_DEFINITIONS.md
EXPERIMENTATION.md
ATTRIBUTION.md
DATA_QUALITY.md
```

---

# 14. Operations / Release

Typical:

```text
ENVIRONMENTS.md
DEPLOYMENT.md
RELEASE_PROCESS.md
ROLLBACK.md
BACKUP_RESTORE.md
INCIDENT_RESPONSE.md
SLO_SLI.md
ON_CALL.md
runbooks/
```

Runbooks should be tested.

---

# 15. Decisions

Typical:

```text
architecture/ADR-...
product/PDR-...
design/DDR-...
security/SDR-...
rfcs/
```

Preserve why.

---

# 16. Plans / Current Execution

Typical:

```text
ACTIVE_PLAN.md
migrations/
redesign/
rollout/
completed/
```

Plans are temporary.

---

# 17. Onboarding / Contribution

Typical:

```text
START_HERE.md
LOCAL_SETUP.md
REPOSITORY_TOUR.md
FIRST_PR.md
AI_AGENT_GUIDE.md
TROUBLESHOOTING.md
```

---

# 18. Reference

Typical:

```text
ROUTES.md
ENV_VARS.md
ERROR_CODES.md
FEATURE_FLAGS.md
THIRD_PARTY_SERVICES.md
COMMANDS.md
```

---

# 19. Archive

Archive:

- superseded architecture;
- completed plans;
- historical audits;
- old design-system versions;
- retired specs.

Archive preserves context but is not active instruction.
