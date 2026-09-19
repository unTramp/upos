#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 tools/verify_frozen_baseline.py

if [[ ! -d .git ]]; then
  git init
fi

git branch -M main
git add .

if git diff --cached --quiet; then
  echo "Nothing staged; repository may already be initialized."
else
  git commit -m "chore(repo): establish U-POS v1 canonical baseline"
fi

if ! git rev-parse v1.0.0 >/dev/null 2>&1; then
  git tag -a v1.0.0 -m "U-POS v1 modular architecture baseline"
fi

echo
printf '%s
' "Local baseline ready."   "Next: create an empty private GitHub repository, add it as origin, then:"   "  git push -u origin main"   "  git push origin v1.0.0"
