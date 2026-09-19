# UI Kit Web Specification v1.2

**ID:** DS-STD-003  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System / UI Engineering  
**Version:** 1.2.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** UI Kit information architecture, registry rendering, preview, export, or static-build contract changes  
**Supersedes:** —  
**Related:** DS-STD-001, DS-STD-002, DS-STD-004


# 0. Responsibility

Defines how design-system knowledge becomes a living, navigable web interface.

It does NOT redefine:

- object lifecycle;
- token semantics;
- UX Constitution;
- feature behavior;
- quality-report ownership.

---

# 1. Registry-driven requirement

UI Kit SHOULD consume canonical `REGISTRY.json`.

Registry drives:

- inventory;
- navigation;
- search;
- status;
- version;
- relationships;
- deprecation;
- traceability links;
- freshness;
- parity.

Metadata is authored once.

---

# 2. Information architecture

```text
Overview / Atlas
Foundations
Primitives
Components
Patterns
Page Grammars
Deprecated
Resources
```

Screens/Flows MAY appear as **reference consumers** through links to Product/UX specs, but their canonical contracts are not owned by the Design System module.

Optional:

```text
Benchmark Screens
```

as a visual-reference section.

---

# 3. Atlas

Atlas displays:

```text
Name
Contract version
Object lifecycle
Freshness/parity signal if useful
Mini real specimen
Short purpose
```

It is visual navigation.

---

# 4. Search

Search should index:

- name;
- aliases;
- ID;
- purpose;
- tags;
- tokens;
- status;
- related objects.

---

# 5. Filters

Recommended:

```text
Type
Lifecycle status
Platform
Mode
Tag
Implemented only
Deprecated
```

---

# 6. Object detail page

Recommended:

```text
Header
Visual Spec
Live Preview
States
Variants
Modes / Environments
Responsive
Anatomy
Content Priority
Tokens
Interactions
Accessibility
Localization
Do / Don't
Development
Changelog
Related Objects
Used In
Traceability
```

Hide irrelevant sections.

---

# 7. Header

Show:

```text
Name
Registry ID
Contract version
Object lifecycle
Owner
Type
Platforms
Purpose
Design principle
Parity
Last reviewed / freshness
```

Document lifecycle need not be visually prominent unless viewing the raw spec.

---

# 8. Design / Development

Recommended:

```text
[ Design ] [ Development ]
```

Design:

- board;
- states;
- anatomy;
- responsive;
- tokens.

Development:

- import;
- public API;
- events;
- source;
- story;
- tests;
- implementation notes.

---

# 9. Live preview controls

Only approved contract concepts:

```text
State
Variant
Mode
Viewport
Locale
Direction
Fixture
```

Do not expose every internal prop.

---

# 10. Environment toolbar

Typical:

```text
375
430
768
1024
1440
Custom
LTR / RTL
Light / Dark
Reduced motion
Density mode
```

Only if product actually supports them.

---

# 11. Tokens

Display values from real token source.

Do not manually duplicate resolved values where generation is possible.

---

# 12. Accessibility

Show:

- keyboard;
- focus;
- semantics;
- contrast;
- target size;
- overlay behavior;
- reduced motion.

Automated check result may supplement, not replace, contract.

---

# 13. Localization

For multilingual products:

- locale switch;
- pseudo-locale;
- RTL preview;
- long-text fixture.

---

# 14. Related / traceability

Display registry relations:

```text
Uses
Used by
Related
Do not confuse with
Replacement
Feature specs
Decision refs
Tests
Telemetry/evidence
```

---

# 15. Reference implementation

Preferred:

```text
React
TypeScript
Storybook
MDX
real design tokens
real components
static build
```

Not mandatory.

Alternative tools are acceptable if contract is met.

---

# 16. Stories / fixtures

Use deterministic, safe fixtures.

Use same fixtures where possible for:

- stories;
- docs;
- screenshots;
- component tests.

No production secrets/private user data.

---

# 17. Static export

Required for a mature UI Kit:

```text
ui-kit-static/
├── index.html
└── assets/
```

Recommended command:

```text
pnpm ui-kit:build
```

---

# 18. Package export

Recommended:

```text
pnpm ui-kit:package
```

Output:

```text
<project>-ui-kit-<ds-version>.zip
```

---

# 19. Hosting

May be:

- `/ui-kit`;
- internal hostname;
- GitHub Pages;
- Vercel/Netlify;
- S3/CDN;
- local static server.

---

# 20. Security / privacy

Never expose:

- secrets;
- real tokens;
- private user records;
- confidential media;
- unreleased sensitive material.

---

# 21. UI Kit accessibility

UI Kit itself SHOULD meet WCAG 2.2 AA.

Boards require textual equivalents for critical rules.

---

# 22. CI

Recommended:

```text
typecheck
lint
component tests
UI Kit build
a11y checks
visual regression
static export
```

Broken UI Kit build is a documentation-system regression.

---

# 23. First milestone

Minimum useful UI Kit:

```text
Atlas
Search
Design System Profile
Foundations
Buttons/Inputs/Chips
3–5 core Components
2–3 core Patterns
Page Grammar examples
Static build
```

---

# 24. Acceptance

```text
[ ] registry drives inventory
[ ] Atlas exists
[ ] navigation semantic
[ ] search works
[ ] version/lifecycle shown from registry
[ ] important objects link board + spec + implementation
[ ] preview uses actual code where possible
[ ] supported environments inspectable
[ ] deprecated objects separated
[ ] static build works
[ ] no sensitive production data
[ ] documentation accessible
[ ] no local lifecycle/token redefinitions
```

---

# 25. Final rule

> **HTML is the experience. Registry + specs are the durable structured source. Boards preserve visual intent. Code preserves implementation truth.**
