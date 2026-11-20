#!/usr/bin/env python3
"""Exercise meaningful failure paths without altering the project."""
from pathlib import Path
import shutil
import tempfile
from validate import ROOT, validate

with tempfile.TemporaryDirectory() as folder:
    root = Path(folder) / 'fixture'
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    assert not validate(root)[0], 'clean fixture must pass'
    (root / 'SECURITY.md').unlink()
    (root / '.github/workflows/docs.yml').unlink()
    with (root / 'README.md').open('a') as handle:
        handle.write('\n[broken](missing-file.md)\n')
    path = root / 'templates/TASK_TEMPLATE.md'
    path.write_text(path.read_text().replace('## Evidence', '## Removed'))
    (root / 'fixture.md').write_text('ghp_' + 'A' * 30)
    with (root / 'START_HERE.md').open('a') as handle:
        handle.write('\nFor internal testing\n')
    errors, _ = validate(root)
    for expected in ['missing: SECURITY.md', 'missing: .github/workflows/docs.yml', 'broken/escaping link', 'missing field Evidence', 'possible GitHub token', 'stale private-preview onboarding']:
        assert any(expected in error for error in errors), expected
print('PASS: clean fixture accepted; missing file/workflow, broken link, missing field and synthetic token and stale private onboarding rejected; temporary fixture removed.')

from privacy_audit import findings
assert 'GitHub token' in findings(('ghp_' + 'B' * 30).encode())
assert 'email in file' in findings(('tester' + '@' + 'example.invalid').encode())
assert findings(b'\xff\xfe') is None
assert findings(b'ordinary documentation') == []
print('PASS: privacy scanner detects synthetic token/email; flags non-UTF8 as unscanned; accepts ordinary text.')
