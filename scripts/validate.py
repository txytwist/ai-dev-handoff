#!/usr/bin/env python3
"""Offline documentation checks. Standard library only; no network calls."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = '''README.md README.zh-CN.md START_HERE.md CHATGPT_SETUP.md CODEX_SETUP.md AGENTS.md templates/PROJECT_CONTEXT.md templates/AGENTS.md templates/TASK_TEMPLATE.md templates/HANDOFF_TEMPLATE.md templates/REVIEW_TEMPLATE.md docs/workflow.md docs/mobile-quickstart.md examples/complete-cycle.md .github/ISSUE_TEMPLATE/task.md .github/pull_request_template.md CONTRIBUTING.md SECURITY.md LICENSE_PENDING.md .gitignore docs/tasks/README.md docs/handoff/README.md docs/tasks/phase1-mvp.md docs/handoff/phase1-mvp.md docs/portable-starter.md docs/mobile-acceptance.md docs/tasks/review-round1.md docs/handoff/review-round1.md .github/workflows/docs.yml scripts/validate.py scripts/test_validate.py docs/external-ai-test.md docs/public-beta.md docs/tasks/public-beta.md docs/handoff/public-beta.md .github/ISSUE_TEMPLATE/beta-feedback.md scripts/privacy_audit.py docs/mobile-simulation.md scripts/check_mobile.mjs docs/tasks/public-beta-mobile-ux.md docs/handoff/public-beta-mobile-ux.md'''.split()
STATES = 'PLANNED APPROVED IN_PROGRESS REVIEW CHANGES_REQUESTED ACCEPTED'.split()
COMMON = ['Status', 'Repository and refs', 'Source and approval', 'Acceptance criteria', 'Evidence', 'Next action']
TEMPLATES = ['templates/TASK_TEMPLATE.md', 'templates/HANDOFF_TEMPLATE.md', 'templates/REVIEW_TEMPLATE.md', '.github/ISSUE_TEMPLATE/task.md', '.github/pull_request_template.md']
PATTERNS = {
    'private key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'GitHub token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b',
    'API key': r'\bsk-[A-Za-z0-9_-]{20,}\b',
    'IPv4 literal': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    'credential assignment': r'(?i)\b(?:password|api_key|access_token)\s*[:=]\s*[\x22\x27]?[A-Za-z0-9/+_-]{12,}',
    'unrelated private project': r'proxy-maintenance|Twist Monitor',
}

def validate(root):
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'missing: {name}')
    markdown = sorted(root.rglob('*.md'))
    markdown = [p for p in markdown if '.git' not in p.relative_to(root).parts]
    links = 0
    for path in markdown:
        text = path.read_text(encoding='utf-8')
        # Inline links/images and reference definitions. Ignore fenced examples.
        body = re.sub(r'```.*?```', '', text, flags=re.S)
        targets = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', body)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', body, re.M)
        for raw in targets:
            target = raw.strip().split()[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            links += 1
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():
                errors.append(f'{path.relative_to(root)}: broken/escaping link {target}')
    for name in TEMPLATES:
        path = root / name
        if not path.exists():
            continue
        headings = set(re.findall(r'^## (.+)$', path.read_text(), re.M))
        for field in COMMON:
            if field not in headings:
                errors.append(f'{name}: missing field {field}')
    for name in ['docs/workflow.md', 'CHATGPT_SETUP.md', 'templates/AGENTS.md']:
        path = root / name
        if path.exists():
            for state in STATES:
                if state not in path.read_text():
                    errors.append(f'{name}: missing state {state}')
    # Current guides must not send public readers back to the former private preview.
    # Historical tasks/handoffs are intentionally outside this guard.
    active_guides = ['README.md', 'README.zh-CN.md', 'START_HERE.md', 'CHATGPT_SETUP.md',
                     'docs/portable-starter.md', 'docs/public-beta.md', 'docs/external-ai-test.md']
    stale = r'Private at the last verified|For internal testing|仍(?:为|是)?\s*Private|所有者在授权范围内提供.*全文'
    for name in active_guides:
        path = root / name
        if path.exists() and re.search(stale, path.read_text(), re.I):
            errors.append(f'{name}: stale private-preview onboarding')
    scanned = 0
    for path in sorted(root.rglob('*')):
        if not path.is_file() or '.git' in path.relative_to(root).parts or path.suffix not in ('.md', '.yml', '.yaml'):
            continue
        scanned += 1
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, path.read_text(encoding='utf-8')):
                # Never echo a possible credential.
                errors.append(f'{path.relative_to(root)}: possible {label}; inspect privately')
                break
    return errors, (len(markdown), links, scanned)

if __name__ == '__main__':
    errors, counts = validate(ROOT)
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print(f'PASS: {len(REQUIRED)} required files; {counts[0]} Markdown files; {counts[1]} local links; shared template fields; states; {counts[2]} files scanned for common sensitive patterns.')
    print('Limits: no external URLs, iPhone UI, platform permissions, anchor fragments or exhaustive secret detection verified.')
