# Docs-as-Code Standard v1.0

**ID:** DOC-STD-002  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance / Engineering  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Documentation tooling, manifest, metadata, or integrity pipeline changes  
**Supersedes:** —  
**Related:** DOC-STD-001


# 1. Purpose

Define how project documentation is stored, indexed, validated, generated, and reviewed.

---

# 2. Repository-first default

Normative and living documentation SHOULD be:

- Markdown/MDX/structured text;
- version controlled;
- reviewed in PR;
- linkable;
- searchable;
- consumable by humans and AI agents.

Binary artifacts MAY accompany docs when they serve evidence or visual contracts.

---

# 3. Metadata header

Important docs SHOULD expose:

```text
ID
Type
Status
Normativity
Owner
Version
Lifetime
Created
Last reviewed
Review trigger
Supersedes
Related
```

Trivial guides MAY use reduced metadata.

---

# 4. IDs

Suggested prefixes:

```text
DOC
PROD
DOM
ARCH
SPEC
UX
DS
ENG
API
DATA
AI
SEC
QA
AN
OPS
ADR
PDR
DDR
SDR
RFC
PLAN
RUN
REF
```

IDs MUST be unique within a project when used.

---

# 5. Naming

Good:

```text
AUTHORIZATION.md
MASTER_ARCHITECTURE.md
CONTENT_DESIGN.md
DESIGN_HANDOFF_STANDARD.md
RELEASE_PROCESS.md
```

Bad:

```text
notes-final-v2.md
misc.md
important.md
new-final.md
```

Do not use `final` as lifecycle/version metadata.

---

# 6. Date naming

Use date prefixes for snapshots/reports:

```text
2026-09-19-performance-audit.md
```

Do not date-prefix timeless active standards by default.

---

# 7. Diagrams

Every diagram must answer a question.

Recommended maintainable formats:

```text
Mermaid flowchart
sequenceDiagram
stateDiagram-v2
erDiagram
```

Keep textual explanation.

A diagram is not self-explanatory documentation.

---

# 8. Screenshot policy

Use screenshots for:

- visual design contracts;
- visual QA evidence;
- UX audit evidence;
- operational instructions when stable.

Do not use screenshots as the sole behavioral source.

Important screenshots SHOULD include:

- version/baseline;
- environment/viewport where relevant.

---

# 9. Generated docs

Generated files MUST state:

```text
GENERATED FILE
Source: ...
Command: ...
Do not edit manually.
```

Generated artifacts SHOULD be regenerated, not patched.

---

# 10. Document manifest

Larger projects SHOULD maintain machine-readable:

```text
docs/DOCUMENT_MANIFEST.json
```

The manifest may drive:

- docs index;
- ownership checks;
- freshness checks;
- search;
- AI-agent retrieval;
- CI integrity.

Use `DOCUMENT_MANIFEST_SCHEMA_v1.0.json`.

---

# 11. CI integrity checks

Useful checks:

```text
broken internal links
missing required metadata
duplicate document IDs
invalid status/type/lifetime
ACTIVE doc superseded by another ACTIVE doc
missing owner
overdue review
orphaned canonical spec
invalid supersession link
deprecated API still referenced
missing changelog for breaking change
missing manifest entry
```

Only automate checks that provide real value.

---

# 12. Freshness automation

Freshness MUST NOT mutate semantic document status.

Example:

```text
Status: ACTIVE
Freshness: STALE_REVIEW_REQUIRED
```

Review dates/triggers may generate warnings.

---

# 13. Machine-generated index

`docs/README.md` MAY be partially generated from manifest.

Human-curated orientation SHOULD remain.

---

# 14. Changelogs

Use separate changelogs for separate scopes.

Examples:

```text
root CHANGELOG
→ product releases

design-system/CHANGELOG
→ design-system releases

API_CHANGELOG
→ breaking API contract changes
```

Do not mix unrelated scopes.

---

# 15. Link policy

Prefer repository-relative links for docs.

External links SHOULD have stable ownership where possible.

Broken links SHOULD fail/warn CI for normative docs.

---

# 16. Code ↔ docs references

Specs MAY expose:

```text
Implementation refs
Test refs
Telemetry refs
Decision refs
```

Do not hardcode volatile line numbers as permanent architecture truth.

---

# 17. Tool neutrality

The standard does not require a particular static-site generator.

Possible:

- GitHub Markdown;
- Docusaurus;
- MkDocs;
- Astro;
- Next.js;
- Storybook for Design System;
- custom docs portal.

Source truth remains in canonical docs/registries.

---

# 18. AI readability

Avoid:

- critical meaning encoded only in images;
- inconsistent headings;
- ambiguous status terms;
- unmarked historical content;
- hidden precedence.

Prefer:

- explicit metadata;
- stable headings;
- canonical links;
- machine-readable manifests;
- textual alternatives for visual artifacts.

---

# 19. Quality gate

For normative docs:

```text
[ ] purpose clear
[ ] owner clear
[ ] scope clear
[ ] out-of-scope clear
[ ] status clear
[ ] lifetime clear
[ ] terms defined
[ ] canonical links correct
[ ] temporary details excluded
[ ] conflicts resolved
[ ] acceptance/testability present where relevant
```
