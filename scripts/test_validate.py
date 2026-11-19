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
    with (root / 'README.md').open('a') as handle:
        handle.write('\n[broken](missing-file.md)\n')
    path = root / 'templates/TASK_TEMPLATE.md'
    path.write_text(path.read_text().replace('## Evidence', '## Removed'))
    (root / 'fixture.md').write_text('ghp_' + 'A' * 30)
    errors, _ = validate(root)
    for expected in ['missing: SECURITY.md', 'broken/escaping link', 'missing field Evidence', 'possible GitHub token']:
        assert any(expected in error for error in errors), expected
print('PASS: clean fixture accepted; missing file, broken link, missing field and synthetic token rejected; temporary fixture removed.')
