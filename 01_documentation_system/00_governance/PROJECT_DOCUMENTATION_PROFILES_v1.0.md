# Project Documentation Profiles v1.0

**ID:** DOC-REF-002  
**Type:** REFERENCE  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** LIVING  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Project maturity/type profiles change  
**Supersedes:** —  
**Related:** DOC-STD-001, DOC-REF-001


# 1. Principle

Not every project needs every document.

Choose documentation by:

- risk;
- complexity;
- team size;
- regulatory burden;
- lifecycle;
- integration surface;
- operational criticality;
- AI usage;
- UI complexity.

---

# 2. Starter / MVP

Minimum useful set:

```text
README.md
docs/README.md
PRODUCT_VISION.md
SCOPE.md
MASTER_ARCHITECTURE.md
FEATURE_SPECS.md
UX_CONSTITUTION.md
ENGINEERING_PRINCIPLES.md
API_DATA.md
TESTING.md
ACTIVE_PLAN.md
DECISIONS/
LOCAL_SETUP.md
```

Add Design System when reusable UI begins to emerge.

---

# 3. Production product

Add:

```text
DOMAIN_MODEL.md
DESIGN_SYSTEM/
API_CONTRACTS.md
DATA_MODEL.md
SECURITY_MODEL.md
ANALYTICS_STRATEGY.md
DEPLOYMENT.md
ROLLBACK.md
INCIDENT_RESPONSE.md
RUNBOOKS/
ACCESSIBILITY_TESTING.md
OBSERVABILITY.md
DATA_MIGRATIONS.md
```

---

# 4. Complex / enterprise / regulated

Add:

```text
requirement IDs
formal traceability
compliance mapping
data lineage
retention
access reviews
change approvals
evidence retention
DR testing
vendor risk
formal threat modeling
formal RFC process
document manifest
CI documentation integrity
```

---

# 5. Mobile app profile

Emphasize:

- app lifecycle;
- navigation/deep links;
- offline/cache;
- OS permissions;
- device/OS support;
- app-store release;
- background tasks;
- local storage;
- accessibility on target devices.

---

# 6. SaaS profile

Emphasize:

- tenancy;
- auth/authz;
- billing;
- roles;
- audit;
- export/delete;
- environment strategy;
- migrations;
- observability.

---

# 7. API / platform profile

Emphasize:

- API contracts;
- versioning;
- rate limits;
- idempotency;
- events;
- SDKs;
- deprecation;
- examples;
- compatibility guarantees.

---

# 8. AI product profile

Emphasize:

- AI system overview;
- provider/model boundaries;
- context assembly;
- human approval;
- provenance;
- evals;
- safety;
- degraded mode;
- prompt contracts;
- AI telemetry;
- privacy/data minimization.

---

# 9. Internal tool profile

Emphasize:

- permissions;
- operational impact;
- audit;
- data correctness;
- destructive actions;
- runbooks;
- admin override rules.

---

# 10. High-UI-complexity product profile

Add early:

```text
UX_CONSTITUTION
INFORMATION_ARCHITECTURE
NAVIGATION_MODEL
CONTENT_DESIGN
DESIGN_SYSTEM_OPERATING_MODEL
DESIGN_HANDOFF_STANDARD
REGISTRY.json
UI KIT WEB
VISUAL_REGRESSION
```

---

# 11. Low-UI API/backend profile

Design System MAY be minimal or absent.

Do not create UI governance merely to fill a folder.
