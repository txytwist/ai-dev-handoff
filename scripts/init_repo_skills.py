#!/usr/bin/env python3
"""New-project initialization with default skill inheritance; never overwrite files."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


NEXT_TASK_TEMPLATE = """# NEXT_TASK

## 当前状态
PLANNED

## PR或分支
尚未创建

## 验证结果
尚未运行

## 未测项
项目适用检查与真实使用尚未验证

## 下一步唯一任务
读取AGENTS.md与当前Issue/PR，确定并完成下一项批准任务。

## 阻塞
无；未确定的关键范围、数据及发布决定须用户确认。
"""


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


def initialize(destination, *, disable_skills=False):
    """Initialize a new Git project (an initial README is allowed).

    Existing projects must merge guidance separately; never silently replace it.
    """
    destination = Path(destination).resolve()
    actual = subprocess.check_output(['git', '-C', str(destination), 'rev-parse', '--show-toplevel'], text=True).strip()
    if Path(actual).resolve() != destination:
        raise ValueError('destination must be the Git repository root')
    if any(p.name not in ('.git', 'README.md') for p in destination.iterdir()):
        raise FileExistsError('new-project initialization refuses existing project files; merge manually')
    if not disable_skills:
        inherit(destination)
    (destination / 'AGENTS.md').write_bytes((ROOT / 'templates' / 'AGENTS.md').read_bytes())
    context = (ROOT / 'templates' / 'PROJECT_CONTEXT.md').read_text()
    if disable_skills:
        context += '\n## Explicit user Skill decision\nUser explicitly disabled both caveman and ponytail during initialization (--disable-skills). Skip until the user re-enables them.\n'
    (destination / 'PROJECT_CONTEXT.md').write_text(context)
    (destination / 'NEXT_TASK.md').write_text(NEXT_TASK_TEMPLATE)
    return destination


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', help='approved new project Git root; initial README allowed')
    parser.add_argument('--disable-skills', action='store_true', help='only when the user explicitly disabled both skills; records that decision')
    args = parser.parse_args()
    print('Initialized new project:', initialize(args.destination, disable_skills=args.disable_skills))
