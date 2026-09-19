# GitHub Bootstrap — U-POS v1.0.0

## 1. Create the remote repository

Recommended repository name: `upos`.

Create it as **Private** and do not initialize it with README, license, or .gitignore because this directory already contains them.

With GitHub CLI:

```bash
gh auth login
gh repo create unTramp/upos --private --source=. --remote=origin
```

Or create an empty private repository in the GitHub UI and then add the returned remote URL.

## 2. Establish the canonical baseline

From repository root:

```bash
python3 tools/verify_frozen_baseline.py

git init
git branch -M main
git add .
git commit -m "chore(repo): establish U-POS v1 canonical baseline"
git tag -a v1.0.0 -m "U-POS v1 modular architecture baseline"
```

Then push:

```bash
git push -u origin main
git push origin v1.0.0
```

## 3. Create GitHub Release

Attach the original `UPOS_v1_FINAL.zip` as a release asset rather than committing the ZIP into Git history:

```bash
gh release create v1.0.0 /path/to/UPOS_v1_FINAL.zip \
  --title "U-POS v1.0.0 — Modular Architecture Baseline" \
  --notes "Frozen U-POS v1 modular architecture baseline. See audit/releases/v1.0.0/UPOS_V1_FREEZE_MANIFEST.md."
```

## 4. Protect `main`

Recommended initial repository ruleset:

- Require pull requests before merge.
- Require the `Baseline Integrity` status check.
- Require branches to be up to date before merging once multiple contributors/agents are active.
- Block force pushes to `main`.
- Block branch deletion for `main`.
- Prefer linear, reviewable changes; use the repository's Engineering Governance rules for commit/PR semantics.

If you are the only human maintainer, do **not** require an external human approval count that would make your own repository impossible to merge. Add mandatory reviewer approvals later when a real second reviewer or governed review bot exists.

## 5. Start Phase 2

Only after `v1.0.0` exists on `main`:

```bash
git switch -c feat/schema-registry-v1
```

The first implementation phase should add machine-readable schemas/interfaces without modifying frozen module semantics.
