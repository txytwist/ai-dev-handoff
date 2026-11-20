#!/usr/bin/env python3
"""Read-only audit of tracked files and all locally reachable Git blobs.
Does not print matching values, rewrite history, or inspect GitHub attachments.
Exit 1: heuristic content findings; exit 2: incomplete audit; exit 0: no findings.
Metadata identities always require owner review regardless of exit code.
"""
from pathlib import Path
import re
import subprocess
import sys
from validate import PATTERNS, ROOT


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def findings(data):
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return None
    # This exact line defines a detector, not imported private project data.
    text = re.sub(r"^    'unrelated private project': r'.*',$", '', text, flags=re.M)
    checks = dict(PATTERNS)
    checks['email in file'] = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    checks['local absolute path'] = r'/(?:workspace|home|Users|root)/[^\s<>]+'
    return [label for label, pattern in checks.items() if re.search(pattern, text)]


def main():
    if git('rev-parse', '--is-shallow-repository').strip() != b'false':
        print('INCOMPLETE: shallow history; fetch full authorized history before assessment.')
        return 2
    hits = []
    skipped = 0
    tracked = git('ls-files', '-z').decode().split('\0')
    tracked = [name for name in tracked if name]
    for name in tracked:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            print('INCOMPLETE: non-regular tracked file; inspect privately.')
            return 2
        result = findings(path.read_bytes())
        if result is None:
            skipped += 1
        elif result:
            hits.append(('tracked', name, result))
    # --all covers local branches and fetched remote refs, not deleted/unfetched refs.
    objects = git('rev-list', '--objects', '--all').splitlines()
    blobs = 0
    for item in objects:
        oid = item.split(b' ', 1)[0].decode()
        if git('cat-file', '-t', oid).strip() != b'blob':
            continue
        blobs += 1
        result = findings(git('cat-file', 'blob', oid))
        if result is None:
            skipped += 1
        elif result:
            hits.append(('history blob', oid, result))
    commits = git('rev-list', '--all').splitlines()
    identities = set()
    for oid in commits:
        metadata = git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', oid.decode())
        identities.add(metadata.strip())
        # Scan commit messages too; author identities are summarized separately.
        result = findings(git('show', '-s', '--format=%B', oid.decode()))
        if result:
            hits.append(('commit message', oid.decode(), result))
    print(f'AUDITED: {len(tracked)} tracked files; {blobs} unique reachable blobs; {len(commits)} commits; {skipped} non-UTF8 scans skipped.')
    print(f'OWNER REVIEW: {len(identities)} distinct author/committer identity combinations in Git metadata (names/emails not echoed).')
    print('Scope: local --all refs only; no deleted/unfetched refs, GitHub comments/attachments/logs/artifacts; heuristic scan is not a security certification.')
    print('Detector-definition line for unrelated-project pattern is excluded as a known signature, not a credential.')
    for source, location, labels in hits:
        print(f'REVIEW: {source} {location}: {", ".join(labels)} (values withheld)')
    if hits:
        return 1
    print('NO CONTENT PATTERN FINDINGS; metadata and unscanned surfaces still require owner review.')
    return 2 if skipped else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (subprocess.CalledProcessError, OSError) as error:
        print(f'INCOMPLETE: {type(error).__name__}; inspect privately, do not publish raw error data.')
        sys.exit(2)
