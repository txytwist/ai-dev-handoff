#!/usr/bin/env python3
"""Explicit, optional skill inheritance. Never overwrite project guidance or skills."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def inherit(destination):
    destination = Path(destination).resolve()
    actual = subprocess.check_output(['git', '-C', str(destination), 'rev-parse', '--show-toplevel'], text=True).strip()
    if Path(actual).resolve() != destination:
        raise ValueError('destination must be the Git repository root')
    target = destination / '.agents' / 'skills'
    if (destination / '.agents').is_symlink() or target.exists() or target.is_symlink():
        raise FileExistsError('refusing to overwrite existing skills or follow a symlink')
    shutil.copytree(ROOT / '.agents' / 'skills', target)
    return target


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 scripts/init_repo_skills.py <approved project repository root>')
    print('Copied pinned skills and licenses:', inherit(sys.argv[1]))
