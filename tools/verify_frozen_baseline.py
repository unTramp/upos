#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "00_system" / "FROZEN_BASELINE.sha256"
COUNTS = ROOT / "00_system" / "MODULE_FILE_COUNTS.json"
FROZEN_SCOPES = [
    "01_documentation_system",
    "02_agent_organization",
    "03_skills_system",
    "04_workflow_engine",
    "05_context_memory",
    "06_engineering_governance",
    "07_quality_system",
    "08_observability",
    "09_learning_system",
    "10_security_permissions",
    "11_project_adapter",
    "legacy_sources",
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

expected = {}
for raw in MANIFEST.read_text(encoding='utf-8').splitlines():
    if not raw.strip():
        continue
    digest, rel = raw.split('  ', 1)
    expected[rel] = digest

actual_files = set()
for scope in FROZEN_SCOPES:
    base = ROOT / scope
    if not base.exists():
        print(f'ERROR missing frozen scope: {scope}')
        sys.exit(1)
    for path in base.rglob('*'):
        if path.is_file():
            actual_files.add(path.relative_to(ROOT).as_posix())

errors = []
expected_files = set(expected)
for rel in sorted(expected_files - actual_files):
    errors.append(f'missing: {rel}')
for rel in sorted(actual_files - expected_files):
    errors.append(f'unexpected frozen-scope file: {rel}')
for rel in sorted(expected_files & actual_files):
    got = sha256(ROOT / rel)
    if got != expected[rel]:
        errors.append(f'hash mismatch: {rel}\n  expected {expected[rel]}\n  actual   {got}')

expected_counts = json.loads(COUNTS.read_text(encoding='utf-8'))
for scope, want in expected_counts.items():
    got = sum(1 for p in (ROOT/scope).rglob('*') if p.is_file())
    if got != want:
        errors.append(f'file-count mismatch: {scope}: expected {want}, actual {got}')

if errors:
    print('U-POS frozen baseline verification: FAIL')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print(f'U-POS frozen baseline verification: PASS ({len(expected)} files verified)')
