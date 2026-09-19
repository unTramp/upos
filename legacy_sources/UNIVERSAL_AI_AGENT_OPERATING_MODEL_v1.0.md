# Universal AI Agent Operating Model v1.0

**Document type:** Normative AI Team Governance & Execution Standard  
**Version:** 1.0  
**Status:** Proposed baseline  
**Normativity:** NORMATIVE  
**Scope:** AI-assisted product and software development across arbitrary projects  
**Companion standards:**  
- `UNIVERSAL_PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.md`
- `UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v1.md`

**Primary audience:** founders, product owners, engineering leads, AI platform owners, developers, reviewers, QA, security, DevOps/SRE, AI coding agents, orchestrators  
**Purpose:** Define how a virtual AI-assisted product and engineering organization is structured, governed, coordinated, reviewed, measured, and continuously improved.

---

# 0. Executive model

This document defines a universal operating model for AI agents working on software and product projects.

It does **not** define one specific agent framework.

It defines the organizational and engineering contracts that any implementation should satisfy.

The intended system is:

```text
HUMAN GOVERNANCE
        │
        ▼
PROJECT DOCUMENTATION / SOURCE OF TRUTH
        │
        ▼
PROJECT AGENT MANIFEST
        │
        ▼
ORCHESTRATOR
        │
        ├── selects workflow
        ├── classifies risk
        ├── assembles context
        ├── assigns agents
        └── tracks gates
        │
        ▼
SPECIALIST AGENTS
        │
        ├── Product
        ├── Domain / Architecture
        ├── UX / Design
        ├── Engineering
        ├── Reviewer
        ├── QA
        ├── Security
        ├── Documentation Guardian
        └── Merge Controller
        │
        ▼
SKILLS + WORKFLOWS + POLICIES
        │
        ▼
BRANCH / COMMITS / PR
        │
        ▼
INDEPENDENT VERIFICATION
        │
        ▼
MERGE GATE
        │
        ▼
HUMAN APPROVAL WHERE REQUIRED
        │
        ▼
MERGE / RELEASE
        │
        ▼
LEARNING → PROJECT MEMORY → IMPROVED FUTURE EXECUTION
```

The system is designed around one core idea:

> **AI agents should behave like a governed engineering organization, not like several chatbots talking to each other.**

---

# 1. Relationship to the Documentation Operating Model

The Documentation Operating Model defines:

```text
where project truth lives
which document owns which type of truth
how decisions are preserved
how plans differ from contracts
how canonical knowledge is governed
```

The AI Agent Operating Model defines:

```text
who may act on that truth
how work is delegated
how context is assembled
how changes are implemented
how they are independently verified
who can approve or merge
how learnings become future rules
```

The two models are intentionally decoupled.

The AI Agent Operating Model MUST NOT depend on hard-coded repository paths such as:

```text
docs/03_architecture/MASTER_ARCHITECTURE_v1.4.md
```

Instead it depends on abstract sources:

```text
Product Source of Truth
Domain Source of Truth
Architecture Source of Truth
UX Source of Truth
Design System Source of Truth
Engineering Source of Truth
Security Source of Truth
Current Plan
Decision Records
```

A project-specific manifest resolves these abstract sources to concrete paths.

---

# 2. Project Agent Manifest

Every project adopting this model SHOULD provide:

```text
.ai/PROJECT_AGENT_MANIFEST.md
```

or an equivalent machine-readable manifest.

Its purpose is to bind the universal agent model to the current project.

Recommended content:

```markdown
# Project Agent Manifest

Project:
<name>

Repository:
<repo>

Primary branch:
main

Product Source of Truth:
<path>

Domain Source of Truth:
<path>

Architecture Source of Truth:
<path>

UX Source of Truth:
<path>

Design System Source of Truth:
<path>

Engineering Source of Truth:
<path>

API/Data Source of Truth:
<path>

Security Source of Truth:
<path>

Quality Source of Truth:
<path>

Current Active Plan:
<path>

Decision Records:
<path>

Build commands:
...

Test commands:
...

Lint commands:
...

E2E commands:
...

Protected paths:
...

Sensitive domains:
...

Human approval required for:
...

Merge policy:
...
```

The manifest is the primary adapter between universal agent rules and a specific project.

---

# 3. Foundational principles

## 3.1 Human governance

The system exists to assist human-directed product development.

Humans retain final authority over critical product, architectural, security, financial, destructive, and production-impacting decisions unless explicit policy delegates limited authority.

---

## 3.2 Separation of duties

Creation and verification are distinct responsibilities.

Default rule:

```text
Implementer ≠ Final Reviewer
```

For higher-risk changes:

```text
Implementer ≠ Reviewer ≠ Merge Controller
```

The same underlying model may technically power several roles, but role instructions, context, authority, and evaluation must remain separated.

---

## 3.3 Source of Truth before inference

Agents MUST check relevant canonical project documentation before inventing or inferring project semantics.

---

## 3.4 No silent invention

Agents MUST NOT silently invent:

```text
domain entities
domain states
business rules
permissions
routes
API contracts
database fields
metrics
feature flags
design-system components
security policy
deployment policy
```

If a required concept is missing:

```text
UNKNOWN
TBD
OWNER DECISION REQUIRED
```

is preferable to fabricated certainty.

---

## 3.5 Evidence before approval

A change is not considered correct because an agent claims it is correct.

Approval requires evidence appropriate to risk:

```text
build
lint
tests
type checks
screenshots
visual regression
accessibility checks
security review
QA validation
migration verification
documentation reconciliation
```

---

## 3.6 Least privilege

Each agent receives the minimum authority required for its role.

---

## 3.7 Small coherent changes

The system prefers reviewable, logically coherent changes over broad multi-purpose modifications.

---

## 3.8 One PR, one intention

A Pull Request SHOULD represent one coherent outcome.

---

## 3.9 One commit, one logical change

A commit SHOULD represent one independent logical step, not one keystroke and not a giant unrelated bundle.

---

## 3.10 No opportunistic refactoring by default

Agents MUST NOT perform unrelated cleanup merely because they noticed it during implementation.

Create a separate follow-up task or PR.

---

## 3.11 Risk-based governance

Not all changes require the same workflow.

A typo and an authorization redesign must not pass through identical gates.

---

## 3.12 Organizational learning over hidden memory

Important learning must become durable project memory:

```text
decision
standard
test
skill
guardrail
runbook
specification
```

The system should not rely on an agent privately “remembering” previous work.

---

# 4. Core terminology

## Agent

A role-bound AI worker operating under explicit scope, authority, context, tools, skills, and output contracts.

## Skill

A reusable procedure an agent can perform.

Examples:

```text
create ADR
review PR
classify risk
generate test plan
audit architecture
```

## Workflow

A coordinated sequence of agents and skills used to complete a class of work.

Examples:

```text
bug fix
new feature
architecture change
database migration
```

## Orchestrator

The role responsible for classifying work, selecting workflow, assembling context, assigning agents, and tracking gates.

## Guardrail

A rule preventing or blocking unsafe, unauthorized, or invalid actions.

## Gate

A condition that must be satisfied before workflow progression.

## Handoff

A structured transfer of responsibility and context between agents.

## Project Memory

Durable knowledge stored in project-controlled artifacts.

## Run

One execution instance of an agent or workflow.

## Evidence

Material proving that a required quality condition was checked.

---

# 5. Universal Agent Contract

Every production-grade agent SHOULD have a contract.

Template:

```markdown
# Agent — <Name>

## Identity
<role>

## Mission
<one clear responsibility>

## Owns
<decisions/results this role owns>

## Scope
<allowed problem space>

## Non-scope
<areas explicitly outside authority>

## Required sources
<canonical project sources>

## Optional sources
<additional context>

## Tools
<available tools>

## Permissions
<read/write/review/merge/etc>

## Skills
<allowed reusable skills>

## Inputs
<input contract>

## Process
<required working procedure>

## Outputs
<output contract>

## Quality gates
<what must pass>

## Escalation
<when to stop and escalate>

## Handoffs
<who receives output>

## Prohibited behavior
<explicit constraints>
```

---

# 6. Agent identity is not enough

The following is insufficient:

```text
You are a senior software architect.
```

A production agent must also know:

```text
what it owns
what it does not own
which project truth it must read
what it may change
what it may not change
what output format is required
when it must escalate
```

Role titles alone do not provide governance.

---

# 7. Universal role families

Projects MAY instantiate only the roles they need.

Recommended role families:

```text
Orchestrator
Product
Domain / Architecture
UX / Product Design
Design System
Implementer
Reviewer
QA
Security
Data / Analytics
DevOps / SRE
Documentation Guardian
Merge Controller
```

Optional specialists:

```text
Database
Performance
Accessibility
AI/ML
Mobile Platform
Frontend Platform
Backend Platform
Release Manager
Incident Commander
```

---

# 8. Orchestrator

## Mission

Coordinate work without becoming the default implementer.

## Responsibilities

```text
understand request
classify change
identify affected domains
resolve sources of truth
determine required workflow
determine risk class
assemble context
delegate tasks
track dependencies
collect outputs
resolve process conflicts
enforce gates
escalate when authority boundary is reached
```

## Must not

```text
silently override specialist authority
approve its own high-risk implementation
invent missing project semantics
skip required gates for speed
```

---

# 9. Product Agent

Owns:

```text
user problem
user job
scope
non-goals
feature intent
acceptance intent
product-level trade-offs
```

May create:

```text
Product Spec
PDR
Scope clarification
Acceptance criteria
```

Must not independently redefine architecture, security, or domain ownership.

---

# 10. Domain / Architecture Agent

Owns:

```text
domain model
lifecycles
ownership boundaries
module/service boundaries
integration architecture
architectural constraints
```

May create:

```text
Architecture Impact Report
RFC
ADR
Domain proposal
Migration architecture
```

Must not silently change product scope.

---

# 11. UX / Product Design Agent

Owns:

```text
information architecture
user flows
interaction grammar
content hierarchy
feedback
error recovery
responsive behavior
accessibility intent
```

Must respect canonical domain semantics.

It may change presentation of a status.

It may not invent a new domain status.

---

# 12. Design System Agent

Owns:

```text
tokens
primitives
components
patterns
page grammars
design-system lifecycle
visual consistency
```

Must search existing system before creating new reusable objects.

---

# 13. Implementer Agent

Owns execution of an approved plan.

Responsibilities:

```text
understand plan
inspect existing implementation
modify code
write/update tests
maintain scope
create logical commits
run required checks
prepare implementation evidence
open/update PR
```

Must not:

```text
expand scope without approval
self-approve final review
silently alter domain semantics
silently skip tests
```

---

# 14. Reviewer Agent

Reviewer is independent from implementation.

Mission:

> Find reasons the change should not be merged yet.

Review dimensions may include:

```text
scope
correctness
architecture
domain semantics
security
data integrity
concurrency
error handling
testing
performance
UX
accessibility
documentation
maintainability
```

Reviewer should only evaluate dimensions relevant to the change.

---

# 15. QA Agent

QA validates behavior against:

```text
acceptance criteria
feature spec
bug reproduction
risk model
user scenarios
```

QA is not equivalent to running the test suite.

QA asks:

```text
Does the behavior actually satisfy the intended contract?
What edge cases may fail?
What regression paths are exposed?
```

---

# 16. Security Agent

Security is a conditional specialist.

Automatically consider Security review when changes involve:

```text
authentication
authorization
billing/payment
PII
secrets
file upload
external integrations
data deletion
permissions
admin functions
AI tool execution
production infrastructure
```

Security MAY block merge for unresolved security findings.

---

# 17. Documentation Guardian

Mission:

> Prevent documentation from drifting away from shipped behavior.

Checks:

```text
Did product behavior change?
Did domain semantics change?
Did architecture change?
Did API/data contract change?
Did UX contract change?
Did design system change?
Did operations change?
Is an ADR/PDR/DDR/SDR required?
```

For significant changes, Documentation Guardian SHOULD verify canonical docs before merge.

---

# 18. Merge Controller

Merge Controller does not implement.

It evaluates readiness.

Checks:

```text
scope coherent?
required reviewers passed?
CI passed?
QA passed?
security passed or N/A?
documentation reconciled?
unresolved blocking comments?
branch current?
required human approval present?
```

Output:

```text
READY_TO_MERGE
NOT_READY
BLOCKED
```

---

# 19. Skills model

Skills SHOULD be reusable across projects.

Recommended universal skill categories:

```text
classification
planning
analysis
specification
implementation
verification
governance
operations
```

---

# 20. Skill contract

Template:

```markdown
# Skill — <Name>

## Purpose

## Inputs

## Preconditions

## Required sources

## Procedure

## Outputs

## Quality criteria

## Failure modes

## Escalation

## Applicable roles

## Applicable risk classes
```

---

# 21. Example universal skills

Recommended starter library:

```text
classify-change
assemble-context
analyze-impact
create-feature-spec
create-rfc
create-adr
create-pdr
create-ddr
create-implementation-plan
reproduce-bug
write-regression-test
implement-change
create-atomic-commit
review-diff
review-architecture
review-security
run-qa-validation
reconcile-documentation
assess-merge-readiness
prepare-release
analyze-incident
capture-learning
```

---

# 22. Workflow contract

Each workflow SHOULD define:

```text
trigger
entry conditions
risk classes
required agents
required skills
required documents
steps
parallelizable steps
quality gates
human gates
exit conditions
failure path
```

---

# 23. Change classification

Universal baseline:

```text
C0 — MICRO
C1 — SMALL
C2 — STANDARD FEATURE
C3 — CROSS-CUTTING
C4 — ARCHITECTURAL
C5 — HIGH-RISK
```

Projects MAY define stricter rules.

---

# 24. C0 — Micro

Examples:

```text
typo
copy correction
small spacing correction
simple documentation fix
trivial isolated null guard
```

Typical workflow:

```text
Implement
→ local check
→ lightweight review
→ merge gate
```

Human approval may be optional depending on project policy.

---

# 25. C1 — Small

Examples:

```text
isolated bug
small component behavior adjustment
minor API validation fix
```

Typical:

```text
Plan
→ Implement
→ Independent Review
→ QA/lightweight validation
→ Merge Gate
```

---

# 26. C2 — Standard Feature

Examples:

```text
new ordinary capability
new workflow within existing architecture
new UI backed by existing domain
```

Typical:

```text
Feature Spec
→ Impact Analysis
→ Implementation Plan
→ Implementer
→ Reviewer
→ QA
→ Documentation Guardian
→ Merge Controller
```

---

# 27. C3 — Cross-cutting

Examples:

```text
frontend + backend + DB
multiple bounded contexts
large shared component migration
```

Typical:

```text
Product
→ Architecture Impact
→ Implementation Plan
→ Parallel implementation where safe
→ Reviewer
→ Integration QA
→ Docs
→ Merge Gate
```

Human review SHOULD be strongly considered.

---

# 28. C4 — Architectural

Examples:

```text
new service
new canonical storage owner
major routing architecture
new multi-tenancy model
new eventing model
```

Required:

```text
RFC
Architecture review
Human approval
ADR
Implementation Plan
Independent Review
QA
Documentation reconciliation
```

---

# 29. C5 — High-risk

Examples:

```text
auth
authorization
billing
money movement
destructive data changes
privacy/retention
secrets
production migration
security boundary
irreversible AI action
```

Required:

```text
specialist review
human approval
rollback strategy
strong evidence
enhanced QA
```

AI-only merge SHOULD be prohibited by default.

---

# 30. Risk override rule

A small diff can still be high risk.

Example:

```text
one-line authorization condition
```

may be C5.

Classification is based on impact, not line count.

---

# 31. Context assembly

Agents SHOULD receive minimal sufficient context.

Context selection should consider:

```text
task
role
affected domain
risk
source-of-truth ownership
recent relevant decisions
relevant code
relevant tests
```

Avoid sending every project document to every agent.

---

# 32. Context assembly order

Recommended:

```text
1. task / issue
2. project manifest
3. relevant source of truth
4. relevant specification
5. relevant decisions
6. relevant implementation
7. relevant tests
8. current plan
```

---

# 33. Context budget principle

Prefer:

```text
high relevance
high authority
high freshness
```

over maximal context volume.

Too much context can reduce reliability.

---

# 34. Memory model

Distinguish:

```text
SESSION CONTEXT
temporary working information

PROJECT MEMORY
durable repository-controlled knowledge

ORGANIZATIONAL LEARNING
new rules extracted from repeated outcomes
```

---

# 35. Project memory sources

Examples:

```text
Product Principles
Domain Model
Architecture
Feature Specs
ADRs/PDRs/DDRs/SDRs
Engineering Standards
Design System
Tests
Runbooks
Learnings
Postmortems
```

---

# 36. Learning is not hidden model training

Default system learning SHOULD happen through durable artifacts.

Example:

```text
Reviewer finds repeated race condition
↓
Engineering Standard updated
↓
test pattern added
↓
skill updated
↓
future agent receives new rule
```

This is controlled organizational learning.

---

# 37. Learning promotion model

After:

```text
incident
escaped defect
repeated review finding
failed migration
repeated UX inconsistency
```

ask:

```text
Was this systemic?
```

If yes, promote learning into one or more:

```text
Test
Guardrail
Engineering Standard
Design System rule
ADR
Skill update
Workflow update
Runbook
```

---

# 38. Permissions model

Potential permission set:

```text
READ_REPO
READ_DOCS
WRITE_DOCS
WRITE_CODE
CREATE_BRANCH
COMMIT
PUSH
OPEN_PR
COMMENT_PR
REQUEST_CHANGES
APPROVE_PR
MERGE_PR
CREATE_RELEASE
DEPLOY_STAGING
DEPLOY_PRODUCTION
RUN_DB_MIGRATION
MODIFY_SECRETS
MODIFY_INFRA
```

---

# 39. Default role permission philosophy

## Orchestrator

```text
READ
PLAN
ASSIGN
TRACK
```

No automatic production deployment.

## Implementer

```text
WRITE_CODE
CREATE_BRANCH
COMMIT
PUSH
OPEN_PR
```

No final self-approval.

## Reviewer

```text
READ
COMMENT
REQUEST_CHANGES
APPROVE
```

No implementation by default.

## QA

```text
READ
RUN_TESTS
COMMENT
BLOCK_ON_FAILURE
```

## Merge Controller

```text
READ
ASSESS_GATES
MERGE
```

Only within policy.

---

# 40. Human approval model

Recommended baseline:

```text
C0 → optional human approval
C1 → optional/organization policy
C2 → human merge initially recommended
C3 → human approval recommended
C4 → human approval mandatory
C5 → human approval mandatory
```

A project can be stricter.

---

# 41. Recommended adoption mode

At first:

```text
AI agents:
implement
review
test
prepare
mark READY_TO_MERGE

Human:
final merge
```

Later, low-risk classes may receive delegated auto-merge.

---

# 42. Planning model

C2+ changes SHOULD receive a written Change Plan before implementation.

Change Plan should include:

```text
goal
affected domains
source of truth
scope
non-scope
risk class
dependencies
implementation steps
expected tests
expected documentation updates
expected commits
rollback considerations
```

---

# 43. Expected commits

Commit planning is indicative, not rigid.

Example:

```text
Task:
Fix expired reset token bug

Expected commits:

1. test(auth): reproduce expired reset token behavior
2. fix(auth): reject expired reset tokens
3. docs(auth): clarify reset-token expiration contract
```

---

# 44. Git operating principles

## 44.1 No direct push to protected main

Normal changes SHOULD use branches and PRs.

## 44.2 One branch per coherent task

Recommended:

```text
feat/<ticket>-<slug>
fix/<ticket>-<slug>
docs/<ticket>-<slug>
chore/<ticket>-<slug>
```

Exact convention is project-specific.

---

# 45. Atomic logical commits

A commit SHOULD:

```text
have one reason
have one logical intent
avoid unrelated cleanup
be understandable independently
be revertable where practical
keep repository coherent where practical
```

Atomic does not mean tiny.

---

# 46. Bad commit granularity

Avoid:

```text
create file
add import
rename variable
fix lint
change padding
```

as five separate commits when they are one logical change.

---

# 47. Bad oversized commit

Avoid:

```text
feat: implement everything
```

containing:

```text
new schema
new API
new UI
refactor auth
update design system
unrelated cleanup
```

---

# 48. Commit categories

Recommended Conventional Commit-like semantics:

```text
feat
fix
test
docs
refactor
perf
chore
build
ci
```

Projects may adapt.

---

# 49. Commit message contract

Recommended:

```text
<type>(<scope>): <imperative summary>
```

Optional body:

```text
why
important trade-off
migration implication
```

---

# 50. Bug-fix commit strategy

For non-trivial bugs, prefer:

```text
test: reproduce failure
fix: correct failure
```

where practical.

This creates review evidence.

---

# 51. Review-fix commits

Reviewer feedback may result in additional logical commits.

Avoid one commit per comment.

Group related corrections.

---

# 52. PR operating model

A PR is a coherent review unit.

Rule:

> **One PR = one reviewable intention.**

---

# 53. Good PR

Example:

```text
feat: add release planning
```

with commits:

```text
feat(release): add release plan model
feat(release): persist release plan
feat(release): expose API
feat(release): add planning UI
test(release): cover validation
docs(release): document workflow
```

All commits serve one outcome.

---

# 54. Bad PR

Avoid:

```text
Add release planning
Fix auth bug
Refactor sidebar
Upgrade framework
Rename analytics events
```

in one PR.

---

# 55. PR size policy

Do not use a universal hard limit such as “maximum 200 lines”.

Instead:

```text
Can the reviewer understand one intention?
Can risk be assessed in one mental context?
Can the PR be split without breaking safety?
```

Large PRs SHOULD trigger a split review.

---

# 56. PR description contract

Recommended:

```markdown
## Why

## What

## Scope

## Non-scope

## Risk class

## Architecture/domain impact

## API/data impact

## UX/design impact

## Security/privacy impact

## Test evidence

## QA evidence

## Documentation

## Rollback

## Known limitations
```

---

# 57. Creation loop

The creation loop is:

```text
Plan
→ Implement
→ Test locally
→ Commit
→ Continue
→ Open/Update PR
```

---

# 58. Verification loop

Verification is independent:

```text
Review
→ QA
→ Security if required
→ Documentation reconciliation
→ Merge readiness
```

Creation and verification SHOULD NOT collapse into one self-check.

---

# 59. Self-check

Implementer MUST self-check before review.

Self-check is not independent approval.

Typical:

```text
build
lint
targeted tests
diff review
scope review
```

---

# 60. Independent review protocol

Reviewer SHOULD inspect:

```text
task
spec
diff
relevant architecture
tests
evidence
```

Reviewer MUST NOT assume passing CI proves correctness.

---

# 61. Review finding severity

Recommended:

```text
BLOCKING
must be resolved before merge

MAJOR
significant issue; normally resolve before merge

MINOR
non-blocking improvement

NIT
optional polish
```

---

# 62. Review output contract

Example:

```text
REVIEW RESULT

Scope:
PASS

Correctness:
PASS

Architecture:
PASS

Domain semantics:
PASS

Security:
N/A

Testing:
FAIL

Documentation:
PASS

Findings:
1 BLOCKING

Verdict:
CHANGES_REQUIRED
```

---

# 63. Reviewer independence

Reviewer SHOULD NOT silently fix its own findings in the same review role.

Default:

```text
Reviewer finds
→ Implementer fixes
→ Reviewer re-reviews
```

This preserves separation of duties.

---

# 64. QA protocol

QA SHOULD derive tests from:

```text
acceptance criteria
risk
user flows
negative paths
regression paths
```

not solely from implementation details.

---

# 65. QA dimensions

Potential:

```text
happy path
negative path
boundary conditions
permissions
state transitions
error recovery
concurrency
responsive behavior
accessibility
backward compatibility
```

Use relevant subset.

---

# 66. Documentation gate

For C2+ changes, verify:

```text
Product docs affected?
Domain docs affected?
Architecture docs affected?
Feature spec affected?
UX docs affected?
Design system affected?
API/data contract affected?
Operations affected?
Decision record required?
```

---

# 67. Architecture gate

Trigger when:

```text
module boundary changes
new service
new persistence owner
new cross-domain dependency
new event
new external integration
```

Architecture Agent may require RFC/ADR.

---

# 68. Security gate

Trigger when sensitive domains are affected.

Security gate may require:

```text
threat review
permission review
secret review
data-flow review
rollback
audit evidence
```

---

# 69. Database migration gate

For schema/data migrations require where relevant:

```text
migration plan
backward compatibility
data verification
rollback or forward-fix
locking/performance analysis
backup/recovery consideration
```

---

# 70. Merge readiness

Merge Controller evaluates gates, not implementation aesthetics.

Possible result:

```text
READY_TO_MERGE
NOT_READY
BLOCKED_BY_HUMAN_DECISION
```

---

# 71. Merge authority

Projects SHOULD define merge authority by risk.

Example:

```text
C0: automated merge allowed
C1: automated merge allowed after gates
C2: human merge initially
C3: human approval
C4: human approval mandatory
C5: human approval mandatory
```

---

# 72. Merge strategy

Project-specific Git standard should define:

```text
merge commit
squash
rebase merge
```

This universal model recommends preserving meaningful logical history.

Do not blindly squash carefully structured commits if that history has review value.

---

# 73. Handoff protocol

Agents SHOULD exchange structured handoffs.

Template:

```text
HANDOFF

From:
<agent>

To:
<agent>

Task:
...

Context:
...

Canonical sources:
...

Decisions already made:
...

Constraints:
...

Open questions:
...

Expected output:
...

Authority:
...

Do not:
...
```

---

# 74. Handoff context minimization

Do not pass entire chat transcripts unless necessary.

Prefer:

```text
structured summary
canonical links
open decisions
required evidence
```

---

# 75. Guardrails

Universal guardrail examples:

```text
no direct push to protected main
no merge with failing required checks
no schema migration without migration plan
no permission change without security review
no domain state creation without domain approval
no global design-system component without registry check
no production deploy without policy gate
```

---

# 76. Guardrail types

```text
input guardrail
tool/action guardrail
output guardrail
workflow guardrail
merge guardrail
```

---

# 77. Escalation model

Agents MUST escalate when:

```text
canonical docs conflict
required truth missing
authority boundary reached
risk higher than assigned workflow
same review issue repeats
migration cannot be safely reversed
production impact unclear
security uncertainty unresolved
```

---

# 78. Escalation targets

Potential:

```text
Orchestrator
Product Owner
Architecture Owner
Security Owner
Human Project Owner
```

---

# 79. Failure and recovery

Workflow must define recovery.

Possible actions:

```text
retry
re-plan
reassign
split task
rollback
abort
human escalation
```

---

# 80. Retry policy

Do not loop indefinitely.

Example:

```text
2 failed implementation attempts
→ re-plan

3 review rejection cycles
→ human/lead escalation
```

Exact thresholds are project-specific.

---

# 81. Scope Guardian

May be a dedicated role or Reviewer dimension.

Checks:

```text
Does diff exceed requested scope?
Are unrelated refactors present?
Did implementation alter additional domains?
```

If yes:

```text
BLOCK
SPLIT FOLLOW-UP
```

---

# 82. Concurrency model

Parallel agents are allowed only when contracts and dependencies permit.

Safe pattern:

```text
approved domain/API contract
        ↓
   ┌────┴────┐
Backend    Frontend
   └────┬────┘
     Integration QA
```

Unsafe:

```text
Frontend invents API
Backend invents different API
```

---

# 83. Task isolation

Preferred:

```text
one task
→ one branch/worktree/sandbox
```

Benefits:

```text
less cross-task contamination
clear ownership
clean diff
easier rollback
```

---

# 84. Shared file collision

Orchestrator should detect parallel tasks modifying the same sensitive files.

Options:

```text
serialize
split ownership
create explicit shared contract first
```

---

# 85. Workflow — Micro Change

```text
Request
→ classify C0
→ Implementer
→ self-check
→ lightweight Reviewer
→ Merge Controller
→ merge/human policy
```

Artifacts:

```text
small commit
small PR if repository policy requires
```

---

# 86. Workflow — Bug Fix

```text
Bug report
→ classify
→ reproduce
→ regression test where practical
→ implementation plan
→ fix
→ atomic commits
→ Reviewer
→ QA
→ Docs if behavior contract changed
→ Merge Gate
```

---

# 87. Workflow — New Feature

```text
Request
→ Product clarification
→ Feature Spec
→ Domain/Architecture impact
→ UX impact
→ risk classification
→ implementation plan
→ Implementer
→ Reviewer
→ QA
→ Security conditional
→ Documentation Guardian
→ Merge Controller
→ Human gate
```

---

# 88. Workflow — UI Change

```text
Request
→ UX intent
→ design-system check
→ implementation
→ visual evidence
→ accessibility check
→ Reviewer
→ QA
→ Docs gate
```

---

# 89. Workflow — Design System Change

```text
Need
→ search registry
→ reuse/extend/create decision
→ Design System review
→ component/pattern spec
→ implementation
→ stories/tests
→ visual QA
→ deprecation/migration if needed
```

---

# 90. Workflow — Architecture Change

```text
Problem
→ RFC
→ alternatives
→ architecture review
→ human approval
→ ADR
→ migration plan
→ implementation
→ independent review
→ QA
→ documentation reconciliation
```

---

# 91. Workflow — API Change

```text
Need
→ contract impact
→ backward compatibility
→ versioning
→ implementation
→ contract tests
→ consumer review
→ documentation
```

---

# 92. Workflow — Database Migration

```text
Need
→ data impact
→ migration plan
→ compatibility strategy
→ backup/recovery consideration
→ migration implementation
→ verification
→ rollback/forward-fix
→ human gate according to risk
```

---

# 93. Workflow — Security Change

```text
Request
→ threat analysis
→ security design
→ human approval where required
→ implementation
→ security review
→ QA
→ audit evidence
```

---

# 94. Workflow — Refactor

Refactor must define:

```text
behavior preserved
reason
scope
tests proving preservation
```

Do not mix broad refactor with feature change unless necessary.

---

# 95. Workflow — Dependency Upgrade

```text
dependency analysis
→ changelog/breaking review
→ upgrade
→ build/tests
→ regression review
→ security implications
→ merge
```

---

# 96. Workflow — Hotfix

Hotfix is optimized for recovery, not for skipping safety.

Typical:

```text
incident
→ minimal fix
→ focused validation
→ expedited review
→ human approval
→ release
→ post-merge/post-incident follow-up
```

Technical debt created by emergency shortcuts must be recorded.

---

# 97. Workflow — Documentation Change

```text
change
→ canonical ownership check
→ update
→ link validation
→ contradiction check
→ docs review
```

No code gate needed unless generated docs or behavior is involved.

---

# 98. Workflow — Release

```text
release candidate
→ CI
→ migration checks
→ release notes
→ security/ops gates
→ human approval
→ deploy
→ verification
→ rollback if needed
```

---

# 99. Observability model

Every agent/workflow run SHOULD emit structured telemetry where practical.

Fields:

```text
run_id
workflow_id
task_id
project
agent
role
skill
risk_class
started_at
finished_at
status
handoffs
tools_used
files_touched
commits_created
PR
test_results
review_findings
retries
escalations
final_outcome
cost/tokens if available
```

---

# 100. Dashboard-ready metrics

Potential metrics:

```text
tasks completed
tasks blocked
PR lead time
review cycles
first-pass review rate
QA failure rate
rework rate
revert rate
escaped defects
scope violations
architecture violations
security findings
documentation drift
agent utilization
cost per task
cost per merged PR
```

---

# 101. Do not optimize for activity

Avoid primary metrics:

```text
lines of code
number of commits
number of PRs
number of messages
```

These can be gamed and encourage bad behavior.

---

# 102. Quality metrics

Prefer:

```text
first-pass acceptance
escaped defects
rework
review severity
production regressions
mean time to recovery
architecture violations
documentation drift
```

---

# 103. Agent performance

Performance tracking may be useful, but avoid simplistic composite scores initially.

Prefer factual signals:

```text
review findings caught
rework requested
tasks completed
blocked/escalated tasks
QA failures
escaped defects associated with change
```

---

# 104. Agent learning record

Optional durable artifact:

```text
.ai/learnings/
```

A learning record may include:

```text
problem
evidence
root cause
new rule
affected skill
affected workflow
new test/guardrail
```

After promotion, the learning may be archived because the permanent rule now lives elsewhere.

---

# 105. Skill evolution

Skills SHOULD evolve when repeated execution reveals a better procedure.

Example:

```text
Old skill:
implement-change

New rule:
Before editing shared schema, inspect all consumers.

Reason:
Repeated breaking changes.
```

Version skills where behavior materially changes.

---

# 106. Workflow evolution

Workflow changes should be evidence-driven.

Example:

```text
Repeated production bugs after dependency upgrades
→ add targeted compatibility review gate
```

---

# 107. Agent contract evolution

Agent roles may be updated when:

```text
authority ambiguous
responsibility overlap discovered
handoffs repeatedly fail
agent repeatedly exceeds scope
```

---

# 108. Model/provider independence

Universal agent contracts SHOULD avoid dependence on one model provider.

The project may map roles to different models.

Example:

```text
fast low-cost model → C0 classification
strong reasoning model → architecture review
code-capable model → implementation
```

Provider selection is implementation detail.

---

# 109. Tool independence

The model should work with:

```text
GitHub
GitLab
Bitbucket
local Git
CI vendors
different agent runtimes
```

Tool-specific adapters implement the universal contracts.

---

# 110. Safety around secrets

Agents SHOULD NOT receive unrestricted secret access by default.

Use:

```text
scoped credentials
environment isolation
short-lived tokens
least privilege
audit trail
```

Secret modification should require explicit policy.

---

# 111. Production access

Default:

```text
development agents do not receive unrestricted production mutation access
```

Production actions should be delegated to controlled operations workflows.

---

# 112. Protected files

Project manifest MAY define:

```text
auth/
billing/
infra/
migrations/
security/
```

as sensitive paths requiring specialist review.

---

# 113. Definition of Ready — task

A C2+ task is ready for implementation when:

```text
[ ] user/product intent is clear
[ ] scope is explicit
[ ] non-scope is explicit
[ ] canonical sources identified
[ ] risk class assigned
[ ] affected domains known
[ ] architecture questions resolved enough
[ ] acceptance criteria exist
[ ] blocking decisions resolved
[ ] workflow selected
```

---

# 114. Definition of Ready — agent execution

An agent run is ready when:

```text
[ ] role selected
[ ] input contract present
[ ] context assembled
[ ] permissions sufficient
[ ] tools available
[ ] expected output known
[ ] escalation path known
```

---

# 115. Definition of Done — implementation

```text
[ ] scoped behavior implemented
[ ] no unrelated changes
[ ] relevant tests pass
[ ] build/lint/type checks pass as required
[ ] commits are logical
[ ] implementation evidence recorded
[ ] PR prepared
```

---

# 116. Definition of Done — PR

```text
[ ] coherent intention
[ ] required review passed
[ ] QA passed where required
[ ] security passed where required
[ ] documentation reconciled
[ ] no blocking findings
[ ] merge policy satisfied
[ ] rollback/migration known where required
```

---

# 117. Definition of Done — workflow

```text
[ ] intended outcome achieved
[ ] required gates passed
[ ] project truth updated
[ ] decisions recorded
[ ] telemetry captured
[ ] systemic learning promoted if needed
```

---

# 118. Recommended repository structure

```text
.ai/
├── README.md
├── PROJECT_AGENT_MANIFEST.md
│
├── agents/
│   ├── orchestrator.md
│   ├── product.md
│   ├── domain-architect.md
│   ├── ux.md
│   ├── design-system.md
│   ├── implementer.md
│   ├── reviewer.md
│   ├── qa.md
│   ├── security.md
│   ├── documentation-guardian.md
│   └── merge-controller.md
│
├── skills/
│   ├── classify-change.md
│   ├── assemble-context.md
│   ├── analyze-impact.md
│   ├── create-feature-spec.md
│   ├── create-rfc.md
│   ├── create-adr.md
│   ├── create-implementation-plan.md
│   ├── reproduce-bug.md
│   ├── implement-change.md
│   ├── create-atomic-commit.md
│   ├── review-diff.md
│   ├── qa-validation.md
│   ├── reconcile-documentation.md
│   └── assess-merge-readiness.md
│
├── workflows/
│   ├── micro-change.md
│   ├── bug-fix.md
│   ├── new-feature.md
│   ├── ui-change.md
│   ├── design-system-change.md
│   ├── architecture-change.md
│   ├── api-change.md
│   ├── database-migration.md
│   ├── security-change.md
│   ├── dependency-upgrade.md
│   ├── refactor.md
│   ├── hotfix.md
│   └── release.md
│
├── policies/
│   ├── risk-classification.md
│   ├── permissions.md
│   ├── human-approval.md
│   ├── git-policy.md
│   ├── context-policy.md
│   ├── review-policy.md
│   └── merge-policy.md
│
├── templates/
│   ├── agent-contract.md
│   ├── skill.md
│   ├── workflow.md
│   ├── handoff.md
│   ├── review-result.md
│   ├── change-plan.md
│   └── project-agent-manifest.md
│
└── learnings/
```

Projects MAY simplify this structure.

---

# 119. Maturity model

## Level 0 — Single Agent

One coding agent, human manually supervises everything.

## Level 1 — Role Profiles

Separate implementer/reviewer/product roles exist as reusable instructions.

## Level 2 — Governed Workflows

Risk classes, skills, workflows, and gates are documented.

## Level 3 — Orchestrated Team

Orchestrator selects agents and workflows.

## Level 4 — Automated Verification

CI, review, QA, documentation, and merge gates are integrated.

## Level 5 — Controlled Autonomy

Low-risk changes may complete automatically under policy.

## Level 6 — Learning Organization

Telemetry and repeated failures automatically drive proposed changes to skills, rules, tests, and workflows.

Do not jump directly to Level 6.

---

# 120. Recommended adoption sequence

## Stage 1 — Documentation foundation

Adopt project documentation Source of Truth.

## Stage 2 — Project Agent Manifest

Map canonical sources, commands, protected areas, and approval rules.

## Stage 3 — Three roles

Start with:

```text
Orchestrator
Implementer
Reviewer
```

Human remains QA/merge authority.

## Stage 4 — Add QA and Documentation Guardian

Introduce independent behavioral validation and documentation consistency.

## Stage 5 — Add specialist agents

Architecture, UX, Security, Design System as project complexity requires.

## Stage 6 — Formal workflows

Bug Fix, New Feature, Architecture Change, etc.

## Stage 7 — Telemetry

Track runs and workflow outcomes.

## Stage 8 — Limited autonomous merge

Only after reliability evidence exists.

---

# 121. Recommended first implementation

Do not begin by writing 20 agents.

Start with:

```text
.ai/PROJECT_AGENT_MANIFEST.md

.ai/agents/
    orchestrator.md
    implementer.md
    reviewer.md
    qa.md
    documentation-guardian.md

.ai/skills/
    classify-change.md
    create-implementation-plan.md
    implement-change.md
    review-diff.md
    qa-validation.md
    reconcile-documentation.md

.ai/workflows/
    micro-change.md
    bug-fix.md
    new-feature.md

.ai/policies/
    risk-classification.md
    git-policy.md
    review-policy.md
    human-approval.md
```

This is enough to validate the architecture.

---

# 122. Universal Orchestrator algorithm

Conceptual procedure:

```text
1. Receive request.
2. Resolve project manifest.
3. Identify relevant canonical sources.
4. Determine requested outcome.
5. Classify change C0–C5.
6. Determine affected domains.
7. Select workflow.
8. Determine required agents.
9. Determine required human gates.
10. Assemble context for first agent.
11. Execute workflow.
12. Track outputs and evidence.
13. If conflict → resolve by authority or escalate.
14. If gate fails → return to responsible role.
15. If all gates pass → Merge Controller.
16. If human approval required → wait for approval.
17. Finalize.
18. Capture learning if systemic issue discovered.
```

---

# 123. Authority conflict resolution

When agents disagree:

```text
Product scope → Product authority
Domain lifecycle → Domain authority
Architecture boundary → Architecture authority
UX interaction grammar → UX authority
Design component contract → Design System authority
Security constraints → Security authority
Implementation mechanics → Engineering authority
Merge readiness → Merge Controller under policy
```

Human owner may override according to project governance.

---

# 124. Security veto

A Security Agent MAY block a change within security scope even if Product prefers otherwise.

The human owner may still make an explicit risk acceptance decision where organizational policy permits.

Such overrides should be recorded.

---

# 125. Architecture veto

Architecture Agent MAY block changes violating canonical architecture until:

```text
architecture changed through RFC/ADR
or implementation conforms
```

It should not block based merely on personal preference.

---

# 126. Reviewer veto

Reviewer can block for concrete quality findings.

Reviewer should cite evidence and required correction.

Avoid vague:

```text
I don't like this approach.
```

Prefer:

```text
BLOCKING:
This bypasses authorization contract SEC-AUTH-004.
```

---

# 127. Human override

Human override SHOULD be explicit.

Record:

```text
decision
reason
risk accepted
owner
date
follow-up if any
```

Avoid silent bypass of governance.

---

# 128. Agent output discipline

Agents should produce structured outputs rather than free-form commentary where workflows depend on them.

Examples:

```text
Change Classification
Implementation Plan
Review Result
QA Result
Merge Readiness
```

---

# 129. Change Classification output

```text
CHANGE CLASSIFICATION

Class:
C2

Reason:
New feature inside existing architecture.

Affected:
Frontend
Backend
API
Docs

Specialists:
Architecture review not required
Security not required

Workflow:
New Feature

Human gate:
Merge approval
```

---

# 130. Implementation Plan output

```text
IMPLEMENTATION PLAN

Goal:
...

Source of Truth:
...

Scope:
...

Non-scope:
...

Steps:
1.
2.
3.

Tests:
...

Expected commits:
...

Docs:
...

Risks:
...
```

---

# 131. Review Result output

```text
REVIEW RESULT

Verdict:
APPROVABLE / CHANGES_REQUIRED / BLOCKED

Scope:
PASS/FAIL

Correctness:
PASS/FAIL

Architecture:
PASS/FAIL/N/A

Security:
PASS/FAIL/N/A

Testing:
PASS/FAIL

Documentation:
PASS/FAIL

Findings:
...
```

---

# 132. QA Result output

```text
QA RESULT

Verdict:
PASS / FAIL / BLOCKED

Acceptance criteria:
...

Scenarios executed:
...

Failures:
...

Regression risk:
...

Evidence:
...
```

---

# 133. Merge Readiness output

```text
MERGE READINESS

Status:
READY_TO_MERGE / NOT_READY / BLOCKED

Required checks:
...

Missing:
...

Human approval:
REQUIRED / PRESENT / NOT_REQUIRED
```

---

# 134. Change review feedback loop

```text
Reviewer finding
→ Implementer fix
→ relevant tests
→ commit
→ re-review
```

Do not bypass with “reviewer also fixes” by default.

---

# 135. Oversized PR handling

If a PR becomes too broad:

```text
pause
→ identify independent intentions
→ split safely
→ preserve dependency order
```

Do not force split if it creates an invalid intermediate system.

---

# 136. Scope expansion handling

When implementation discovers necessary extra work:

```text
stop
→ classify discovered work
→ decide:
   required for current task?
   follow-up?
   architecture issue?
```

No silent expansion.

---

# 137. Unplanned architecture discovery

If implementation reveals architecture contradiction:

```text
Implementer
→ Orchestrator
→ Architecture Agent
→ RFC/ADR if needed
```

Do not resolve architecture through incidental code.

---

# 138. Unplanned product ambiguity

If behavior requirement is ambiguous:

```text
Implementer
→ Orchestrator
→ Product Agent / Human
```

Do not guess irreversible semantics.

---

# 139. Unplanned security concern

Immediately escalate to Security workflow.

---

# 140. Documentation drift detection

Signals:

```text
code implements undocumented state
spec references removed endpoint
architecture diagram conflicts with runtime
design system docs reference deprecated component
```

Documentation Guardian should create reconciliation tasks.

---

# 141. Agent sandbox hygiene

At task start:

```text
sync base
create isolated branch/worktree
record baseline
```

At completion:

```text
ensure clean working tree
push commits
link PR
```

---

# 142. Branch lifetime

Branches should be short-lived where practical.

Long-lived branches increase integration risk.

---

# 143. Stacked PRs

Allowed when a feature safely decomposes into dependent review units.

Each stacked PR must clearly declare dependency.

---

# 144. Feature flags

Use when needed to separate deployment from release.

Agent must distinguish:

```text
code merged
feature deployed
feature enabled
feature released
```

---

# 145. Rollback thinking

For C3+ changes, implementation plan SHOULD consider:

```text
How do we undo this?
```

For C4/C5 it is generally required.

---

# 146. Dependency graph awareness

Orchestrator should model task dependencies.

Example:

```text
Domain contract
→ API contract
→ Backend
→ Frontend
→ Integration QA
```

Parallelize only independent nodes.

---

# 147. Cost awareness

Agent orchestration should avoid using expensive specialists unnecessarily.

Risk classification and role routing should control cost.

Do not run every agent on every task.

---

# 148. Latency awareness

For low-risk changes:

```text
short workflow
```

For high-risk:

```text
stronger verification
```

Governance should be proportional.

---

# 149. Human attention as scarce resource

Human review should focus on:

```text
critical decisions
high-risk changes
ambiguous product semantics
architecture
security
production
```

Low-risk mechanical work may gradually become autonomous.

---

# 150. Agent communication rule

Agents should communicate through artifacts and structured handoffs, not informal long debates.

The project artifacts remain the durable memory.

---

# 151. Decision preservation

Significant outcomes should become:

```text
ADR
PDR
DDR
SDR
spec update
standard update
```

Chat transcripts are not canonical memory.

---

# 152. No circular authority

Avoid:

```text
Agent A approves B
Agent B approves A
```

when both participated in implementation.

Approval paths should remain independent enough to provide real verification.

---

# 153. Independent model diversity

Optional advanced pattern:

Use different models/providers for implementation and review to reduce correlated failure.

This is optional, not required by the model.

---

# 154. Review freshness

If new commits arrive after approval, policy should determine whether approval remains valid.

High-risk projects should require review of latest state.

---

# 155. Merge queue compatibility

If repository supports merge queue, Merge Controller may submit approved PRs into the queue instead of merging directly.

---

# 156. CI as evidence provider

CI does not own decisions.

CI provides evidence:

```text
tests passed
build passed
lint passed
security scanner result
```

Merge Controller interprets these according to policy.

---

# 157. Agent-specific test ownership

Implementer:

```text
creates/updates relevant tests
```

Reviewer:

```text
checks whether tests are sufficient
```

QA:

```text
validates behavior independently
```

---

# 158. Test integrity

Agents MUST NOT weaken tests simply to make CI pass unless the contract intentionally changed and documentation supports it.

---

# 159. Snapshot integrity

Agents MUST NOT blindly update snapshots without reviewing why output changed.

---

# 160. Security scanner integrity

Agents MUST NOT suppress security warnings without documented rationale.

---

# 161. Linter suppression

New suppressions require justification when they weaken project standards.

---

# 162. Technical debt creation

If a temporary compromise is necessary, create explicit debt record or issue.

Do not hide temporary shortcuts.

---

# 163. Technical debt review

Repeated debt in one area may indicate:

```text
architecture problem
skill problem
workflow problem
```

Feed this into learning loop.

---

# 164. Post-merge verification

For meaningful changes:

```text
verify target branch
verify CI
verify deployment if applicable
verify migration if applicable
```

---

# 165. Post-merge learning trigger

After:

```text
rollback
hotfix
incident
unexpected QA failure
three+ review cycles
```

evaluate whether a systemic learning exists.

---

# 166. Incident integration

Incident workflow should feed:

```text
postmortem
runbook update
test
guardrail
agent skill
architecture decision
```

---

# 167. Dashboard model

Future dashboard may show:

```text
Active tasks
Agents currently working
Workflow stage
Blocked tasks
PRs awaiting review
QA queue
Merge queue
Recent failures
Agent utilization
Lead time
Review cycles
Cost
```

The operating model SHOULD define telemetry before dashboard implementation.

---

# 168. Agent workload

Do not interpret “utilization” like human employee utilization.

Agent capacity is primarily constrained by:

```text
tool concurrency
cost
rate limits
dependencies
review bottlenecks
human gates
```

Dashboard should represent flow, not pseudo-human busyness.

---

# 169. Workflow bottleneck analysis

Useful signals:

```text
implementation fast, review slow
QA repeated failures
many human escalations
architecture review backlog
```

Use to improve process.

---

# 170. Maturity gates for autonomy

Do not grant auto-merge because agents “seem good”.

Require evidence:

```text
low defect escape rate
stable first-pass review
reliable test coverage
low rollback rate
good scope discipline
```

---

# 171. Autonomy expansion

Expand gradually:

```text
docs-only
→ C0 code
→ selected C1
→ selected C2
```

Keep C4/C5 human-gated by default.

---

# 172. Project-specific overrides

A project may override universal defaults.

Example:

```text
all production code requires human merge
```

Project manifest/policies MUST make override explicit.

---

# 173. Universal vs project-specific rules

Universal:

```text
separation of duties
evidence before approval
risk classification
source-of-truth behavior
```

Project-specific:

```text
exact branch names
exact test commands
exact protected paths
exact human approval thresholds
```

---

# 174. Agent manifests should be versioned

Material changes to project agent configuration should be reviewed.

Examples:

```text
allow auto-merge for C1
grant production deploy permission
change Security gate triggers
```

These are governance changes.

---

# 175. Governance change workflow

Changes to the Agent Operating Model itself should use an RFC-like process when significant.

Examples:

```text
new autonomous merge authority
new production permissions
removing independent review
```

---

# 176. Universal starter agent set

For most projects start with:

```text
Orchestrator
Implementer
Reviewer
QA
Documentation Guardian
```

Human handles:

```text
Product
Architecture
Security
Merge
```

Then progressively specialize.

---

# 177. Universal full agent set

For mature projects:

```text
Orchestrator
Product
Domain
Architecture
UX
Design System
Frontend
Backend
Database
Reviewer
QA
Security
Data/Analytics
DevOps/SRE
Documentation Guardian
Merge Controller
Release Manager
```

Do not instantiate roles without workload.

---

# 178. Agent composition

One actual runtime agent may carry multiple compatible roles in small projects.

Example:

```text
Product + UX
Domain + Architecture
QA + Documentation Guardian
```

Avoid combining:

```text
Implementer + Final Reviewer
```

for significant work.

---

# 179. Universal policy files

Recommended:

```text
risk-classification.md
permissions.md
human-approval.md
git-policy.md
review-policy.md
merge-policy.md
context-policy.md
security-gates.md
```

---

# 180. AI Agent README

`.ai/README.md` should explain:

```text
what this directory contains
how agents are invoked
which file is project manifest
which policies are authoritative
how workflows are selected
```

---

# 181. Compatibility with AGENTS.md / tool-specific files

Tool-specific entry files SHOULD be thin adapters.

Example:

```text
AGENTS.md
→ read .ai/PROJECT_AGENT_MANIFEST.md
→ read relevant agent contract
→ follow project documentation source of truth
```

Avoid maintaining full duplicate instructions in multiple tool-specific files.

---

# 182. Universal file naming

Recommended:

```text
kebab-case.md
```

or project standard.

More important than style:

```text
stable predictable naming
one canonical file
```

---

# 183. Agent contract versioning

Material role changes may use:

```text
Version: 2
```

Minor wording changes do not require a new major contract version.

---

# 184. Skill versioning

Version when procedure materially changes.

---

# 185. Workflow versioning

Version when required gates or sequence materially changes.

---

# 186. Telemetry retention

Projects should define retention and privacy rules for agent traces, especially if traces include source code, secrets, customer data, or prompts.

---

# 187. Sensitive context policy

Agents should receive sensitive context only when required by role.

---

# 188. Secret redaction

Project tooling SHOULD redact secrets from traces and handoffs.

---

# 189. Auditability

For critical workflows, preserve:

```text
who/which agent acted
what changed
which evidence passed
who approved
what was merged
```

---

# 190. Reproducibility

Where practical, a future reviewer should be able to reconstruct:

```text
task
context
plan
commits
review
QA
merge decision
```

---

# 191. Agent hallucination handling

If agent claims a project fact without source:

```text
Reviewer or Orchestrator should request source.
```

Unsupported project claims should not become canonical.

---

# 192. Missing Source of Truth

If no source exists:

```text
mark missing
identify owner
create proposal
do not silently canonize assumption
```

---

# 193. Stale Source of Truth

If source conflicts with runtime evidence:

```text
raise documentation drift
do not automatically treat code as canonical
resolve ownership
```

---

# 194. Feature lifecycle integration

Agent workflow status is separate from product feature lifecycle.

Do not reuse enums.

---

# 195. Agent lifecycle

Possible:

```text
DRAFT
ACTIVE
DEPRECATED
DISABLED
```

This is agent configuration lifecycle, not task status.

---

# 196. Task lifecycle

Suggested:

```text
NEW
CLASSIFIED
PLANNED
IN_PROGRESS
IN_REVIEW
IN_QA
READY_TO_MERGE
BLOCKED
DONE
CANCELLED
```

---

# 197. PR lifecycle

Use Git platform states plus internal gate state.

---

# 198. Agent run lifecycle

Suggested:

```text
QUEUED
RUNNING
WAITING
FAILED
SUCCEEDED
ESCALATED
CANCELLED
```

---

# 199. Workflow state machine

Each workflow should have explicit legal transitions if automation depends on it.

---

# 200. No hidden background authority

Agents must not continue making project decisions outside explicit tasks/workflows.

---

# 201. Human pause points

Long workflows should surface meaningful pause points:

```text
spec approval
architecture decision
high-risk migration
merge approval
production release
```

---

# 202. Plan change protocol

If implementation plan materially changes:

```text
update plan
record reason
reclassify risk if necessary
```

---

# 203. Reclassification

A C1 task may become C4 after discovery.

Orchestrator must allow upward reclassification.

Downward reclassification should require evidence.

---

# 204. Risk inheritance

If any critical sub-change is C5, whole PR may need C5 workflow even if most changes are low-risk.

---

# 205. Change decomposition

Orchestrator should split work by coherent ownership and dependency, not arbitrary file count.

---

# 206. Multi-agent code ownership

Parallel implementers should have clear file/domain ownership during a task.

---

# 207. Shared contract first

Before parallel implementation across boundaries, define:

```text
API contract
event contract
domain interface
design component contract
```

---

# 208. Reviewer context independence

Reviewer should not receive implementation chain-of-thought.

Reviewer receives:

```text
task
spec
diff
tests
evidence
```

This encourages independent analysis.

---

# 209. QA context independence

QA should not be biased only by implementation details.

It should begin from expected behavior.

---

# 210. Merge Controller context

Merge Controller does not need full implementation reasoning.

It needs structured evidence and gate status.

---

# 211. Product Owner context

Human owner should receive concise decision packets for high-risk approvals.

Example:

```text
Decision needed
Options
Trade-offs
Recommendation
Risks
Reversibility
```

---

# 212. Decision packet

Template:

```markdown
# Decision Required

## Question

## Why now

## Option A

## Option B

## Trade-offs

## Risk

## Reversibility

## Recommended next step

## Decision owner
```

---

# 213. Do not fake consensus

If agents disagree materially, surface disagreement.

Do not synthesize a false “everyone agrees” summary.

---

# 214. Conflict resolution by authority

Use:

```text
scope ownership
canonical documentation
risk policy
human governance
```

not majority vote between agents.

---

# 215. Majority voting

May be useful for narrow evaluation tasks, but MUST NOT replace authority model for product governance.

---

# 216. Agent confidence

Agents may report uncertainty, but confidence values SHOULD NOT be treated as objective probability without calibration.

Prefer concrete missing evidence.

---

# 217. Evidence hierarchy

Strong:

```text
passing reproducible test
canonical contract
runtime trace
verified screenshot
```

Weak:

```text
agent intuition
```

---

# 218. Change evidence bundle

For C2+ PRs, optional bundle:

```text
plan
commits
test output
review result
QA result
docs result
security result
merge readiness
```

---

# 219. Artifact retention

Projects should define which agent-generated artifacts remain permanently.

Recommended durable:

```text
specs
decisions
PR review
tests
important reports
```

Temporary:

```text
intermediate scratch plans
raw deliberation
```

---

# 220. Privacy of reasoning

Agent workflows should not depend on storing hidden model reasoning.

Store decisions, evidence, and concise rationale instead.

---

# 221. Universal anti-patterns

## 221.1 Agent swarm without ownership

Many agents discussing one task with no decision rights.

## 221.2 Self-approval

Implementer declares own PR production-ready.

## 221.3 Every task runs every agent

Expensive and slow.

## 221.4 Giant context dump

All docs sent to all agents.

## 221.5 Prompt duplication

Same rules copied into 15 agent files.

## 221.6 Hidden project memory

Important decision exists only in chat.

## 221.7 Activity metrics

Optimizing commits/LOC rather than quality.

## 221.8 AI-created architecture by accident

Implementation agent introduces new system boundary without review.

## 221.9 Fake review

Reviewer says “looks good” without structured evidence.

## 221.10 Git history as keystroke log

One commit per trivial action.

---

# 222. Governance health checks

Periodically review:

```text
Are agents respecting scope?
Are reviews finding real issues?
Are workflows over-heavy?
Are human gates too frequent?
Are docs drifting?
Are repeated failures becoming learnings?
Are agents using deprecated skills?
Are permissions too broad?
```

---

# 223. Quarterly / milestone review

For mature projects:

```text
agent contracts
workflow performance
risk classification
merge policy
security gates
learning backlog
telemetry quality
```

---

# 224. Universal adoption checklist

```text
[ ] Documentation Source of Truth exists
[ ] Project Agent Manifest exists
[ ] Risk classification exists
[ ] Human approval policy exists
[ ] Implementer and Reviewer separated
[ ] Git policy exists
[ ] Review output structured
[ ] QA workflow exists
[ ] Documentation Guardian exists
[ ] Merge readiness defined
[ ] Learning loop exists
[ ] Telemetry schema defined
```

---

# 225. Minimal viable agent system

For an individual developer:

```text
Human
│
├── Orchestrator Agent
├── Implementer Agent
├── Reviewer Agent
└── QA/Docs Agent
```

Human merges.

This already captures most value.

---

# 226. Intermediate agent system

```text
Human Product Owner
        │
Orchestrator
├── Product
├── Architecture
├── UX
├── Implementer
├── Reviewer
├── QA
├── Documentation Guardian
└── Merge Controller
```

---

# 227. Advanced agent system

Add:

```text
Security
Data
SRE
Release
Performance
Accessibility
multiple parallel implementers
automated merge for low risk
```

Only after simpler model proves reliable.

---

# 228. Final operating model

The target is:

```text
PROJECT TRUTH
        ↓
PROJECT MANIFEST
        ↓
TASK
        ↓
ORCHESTRATOR
        ↓
CLASSIFY RISK
        ↓
SELECT WORKFLOW
        ↓
ASSEMBLE CONTEXT
        ↓
ASSIGN SPECIALISTS
        ↓
PLAN
        ↓
IMPLEMENT
        ↓
ATOMIC COMMITS
        ↓
PULL REQUEST
        ↓
INDEPENDENT REVIEW
        ↓
QA
        ↓
SECURITY / ARCHITECTURE / DOCS GATES
        ↓
MERGE CONTROLLER
        ↓
HUMAN GATE IF REQUIRED
        ↓
MERGE / RELEASE
        ↓
OBSERVE
        ↓
LEARN
        ↓
UPDATE PROJECT MEMORY / SKILLS / WORKFLOWS
```

---

# Appendix A — Project Agent Manifest template

```markdown
# Project Agent Manifest

**Status:** ACTIVE
**Owner:** Project Governance

## Project

Name:
Repository:
Primary branch:

## Sources of Truth

Product:
Domain:
Architecture:
Feature Specs:
UX:
Design System:
Engineering:
API/Data:
AI:
Security:
Quality:
Operations:
Current Plan:
Decision Records:

## Commands

Install:
Build:
Lint:
Typecheck:
Unit:
Integration:
E2E:
Accessibility:
Visual:
Security:

## Git

Protected branches:
Branch naming:
Commit convention:
Merge strategy:

## Risk-sensitive areas

- auth
- authorization
- billing
- secrets
- migrations
- production infrastructure

## Human approval

Required for:
- C4
- C5
- production deploy
- destructive migration

## Protected paths

...

## Agent runtime notes

...
```

---

# Appendix B — Agent Contract template

```markdown
# Agent — <Name>

**Version:** 1
**Status:** ACTIVE

## Identity

## Mission

## Owns

## Scope

## Non-scope

## Required sources

## Tools

## Permissions

## Skills

## Inputs

## Procedure

## Outputs

## Quality gates

## Escalation

## Handoffs

## Prohibited behavior
```

---

# Appendix C — Skill template

```markdown
# Skill — <Name>

**Version:** 1
**Status:** ACTIVE

## Purpose

## Inputs

## Preconditions

## Sources

## Procedure

1.
2.
3.

## Outputs

## Quality criteria

## Failure modes

## Escalation

## Roles
```

---

# Appendix D — Workflow template

```markdown
# Workflow — <Name>

**Version:** 1
**Status:** ACTIVE

## Trigger

## Applicable risk classes

## Entry conditions

## Required roles

## Required skills

## Required sources

## Steps

1.
2.
3.

## Parallel steps

## Gates

## Human approvals

## Failure handling

## Completion criteria

## Telemetry
```

---

# Appendix E — Change Plan template

```markdown
# Change Plan — <Task>

## Goal

## Risk class

## Source of Truth

## Affected domains

## Scope

## Non-scope

## Implementation steps

## Tests

## Expected commits

## Documentation

## Security

## Rollback

## Open questions
```

---

# Appendix F — Handoff template

```markdown
# Handoff

From:
To:

## Task

## Context

## Canonical sources

## Decisions already made

## Constraints

## Open questions

## Expected output

## Authority

## Prohibited changes
```

---

# Appendix G — Review Result template

```markdown
# Review Result

**Verdict:** APPROVABLE / CHANGES_REQUIRED / BLOCKED

## Scope
PASS / FAIL

## Correctness
PASS / FAIL

## Architecture
PASS / FAIL / N/A

## Domain semantics
PASS / FAIL / N/A

## Security
PASS / FAIL / N/A

## Testing
PASS / FAIL

## UX / Accessibility
PASS / FAIL / N/A

## Documentation
PASS / FAIL

## Findings

### BLOCKING

### MAJOR

### MINOR

### NIT
```

---

# Appendix H — QA Result template

```markdown
# QA Result

**Verdict:** PASS / FAIL / BLOCKED

## Acceptance criteria

## Scenarios executed

## Negative scenarios

## Regression coverage

## Failures

## Evidence

## Residual risk
```

---

# Appendix I — Merge Readiness template

```markdown
# Merge Readiness

**Status:** READY_TO_MERGE / NOT_READY / BLOCKED

## CI

## Review

## QA

## Security

## Architecture

## Documentation

## Branch status

## Human approval

## Missing requirements
```

---

# Appendix J — Risk Classification Matrix

| Class | Typical scope | Review | QA | Specialist | Human |
|---|---|---|---|---|---|
| C0 | Micro | light | optional | no | optional |
| C1 | Small | required | light | conditional | policy |
| C2 | Feature | required | required | conditional | recommended initially |
| C3 | Cross-cutting | required | integration | architecture | recommended |
| C4 | Architectural | architecture + review | required | yes | mandatory |
| C5 | High-risk | enhanced | enhanced | security/domain | mandatory |

---

# Appendix K — Permission Matrix example

| Role | Code | Docs | Commit | PR | Approve | Merge | Prod |
|---|---:|---:|---:|---:|---:|---:|---:|
| Orchestrator | No | Limited | No | No | No | No | No |
| Implementer | Yes | Yes | Yes | Yes | No | No | No |
| Reviewer | No | Comment | No | Review | Yes | No | No |
| QA | No | Evidence | No | Comment | No | No | No |
| Docs Guardian | No | Yes | No | Comment | No | No | No |
| Merge Controller | No | No | No | Read | No | Policy | No |
| Security | No | Security docs | No | Review | Block | No | No |
| Human Owner | Policy | Policy | Policy | Policy | Yes | Yes | Policy |

---

# Appendix L — Git Policy starter

```markdown
# Git Policy

## Protected branches

No direct push to main.

## Branches

One coherent task per branch.

## Commits

One logical change per commit.

Avoid unrelated cleanup.

Use clear messages.

## Pull Requests

One coherent intention per PR.

## Review

Author cannot be sole final reviewer.

## Merge

All required gates must pass.
```

---

# Appendix M — Review Policy starter

```markdown
# Review Policy

## Reviewer objective

Find blocking correctness, architecture, security, scope, testing, and documentation issues.

## Severity

BLOCKING
MAJOR
MINOR
NIT

## Independence

Reviewer does not silently implement its own findings.

## Evidence

Every blocking finding should include concrete rationale.
```

---

# Appendix N — Human Approval Policy starter

```markdown
# Human Approval Policy

Mandatory:
- C4
- C5
- production deployment
- irreversible migration
- security policy change
- billing/money change
- destructive data policy

Initially recommended:
- C2
- C3

Optional:
- C0
- selected C1
```

---

# Appendix O — Example New Feature workflow

```text
User Request
↓
Orchestrator
↓
C2 classification
↓
Product Agent
→ Feature Spec
↓
Architecture Agent
→ Impact: no architecture change
↓
UX Agent
→ Flow
↓
Implementation Plan
↓
Implementer
→ logical commits
↓
PR
↓
Reviewer
↓
QA
↓
Documentation Guardian
↓
Merge Controller
↓
Human Merge
↓
Post-merge validation
↓
Learning capture if needed
```

---

# Appendix P — Example Bug Fix workflow

```text
Bug
↓
Orchestrator
↓
C1
↓
Implementer
→ reproduce
→ regression test
→ fix
↓
Reviewer
↓
QA
↓
Merge Controller
↓
Merge
```

---

# Appendix Q — Example Architecture Change workflow

```text
Request
↓
Orchestrator
↓
C4
↓
Architecture RFC
↓
Product + Architecture + Security review as relevant
↓
Human decision
↓
ADR
↓
Migration Plan
↓
Implementation
↓
Independent Review
↓
QA
↓
Docs
↓
Merge Gate
↓
Human Merge
```

---

# Appendix R — Learning Record template

```markdown
# Learning — <Title>

## Trigger

## Evidence

## Root cause

## Why systemic

## New rule

## Updated skill

## Updated workflow

## New test / guardrail

## Owner

## Status
```

---

# Appendix S — Telemetry schema starter

```json
{
  "run_id": "...",
  "workflow_id": "...",
  "task_id": "...",
  "project": "...",
  "agent": "...",
  "role": "...",
  "skill": "...",
  "risk_class": "C2",
  "status": "SUCCEEDED",
  "handoffs": [],
  "tools": [],
  "files_touched": [],
  "commits": [],
  "tests": [],
  "review_findings": [],
  "retries": 0,
  "escalations": [],
  "outcome": "READY_TO_MERGE"
}
```

---

# Appendix T — Adoption directive for an existing project

```text
Adopt UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md.

Do not build full automation immediately.

Phase 1:
- create .ai/PROJECT_AGENT_MANIFEST.md
- map Source of Truth
- define risk-sensitive areas
- define test/build commands
- define human approval requirements

Phase 2:
Create:
- Orchestrator
- Implementer
- Reviewer
- QA
- Documentation Guardian

Phase 3:
Create:
- risk classification
- git policy
- review policy
- human approval policy

Phase 4:
Create workflows:
- micro change
- bug fix
- new feature

Phase 5:
Run manually through real tasks.

Phase 6:
Measure failure/rework.

Phase 7:
Add specialist agents only when justified.

Phase 8:
Automate orchestration and low-risk merge only after evidence supports it.
```

---

# Final principles

## 1

> Project truth is external to the agent.

## 2

> Authority must be explicit.

## 3

> Implementation and verification should be separated.

## 4

> Risk determines process depth.

## 5

> Commits represent logical change; PRs represent coherent intention.

## 6

> Evidence, not agent confidence, drives approval.

## 7

> Important learning must become durable project memory.

## 8

> Agents should specialize through contracts, not vague personas.

## 9

> Automation should grow only after the governed workflow proves reliable.

## 10

> The objective is not maximum autonomy. The objective is safe, scalable, explainable execution.
