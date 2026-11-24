#!/usr/bin/env python3
"""Integrity + fresh-project inheritance tests; --host also probes native discovery.
No model invocation, telemetry installation or external repository mutations.
"""
from pathlib import Path
import hashlib
import json
import selectors
import subprocess
import sys
import tempfile
import time
from init_repo_skills import ROOT, inherit, initialize


def integrity(root):
    bundle = root / '.agents' / 'skills'
    manifest = json.loads((bundle / 'manifest.json').read_text())
    assert set(manifest['skills']) == {'caveman', 'ponytail'}
    for name, skill in manifest['skills'].items():
        actual = {str(p.relative_to(bundle / name)) for p in (bundle / name).rglob('*') if p.is_file()}
        assert actual == set(skill['files']), (name, 'incomplete or extra files')
        for rel, expected in skill['files'].items():
            data = (bundle / name / rel).read_bytes()
            assert hashlib.sha256(data).hexdigest() == expected['installed_sha256'], (name, rel)
        text = (bundle / name / 'SKILL.md').read_text()
        assert f'name: {name}' in text and 'description:' in text
        assert skill['files']['SKILL.md']['upstream_sha256'] == skill['files']['SKILL.md']['installed_sha256']
    return bundle


def discover(roots):
    process = subprocess.Popen(['codex', 'app-server'], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, bufsize=1)
    try:
        def request(i, method, params):
            process.stdin.write(json.dumps({'id': i, 'method': method, 'params': params}) + '\n')
            process.stdin.flush()
            selector = selectors.DefaultSelector()
            selector.register(process.stdout, selectors.EVENT_READ)
            deadline = time.monotonic() + 25
            try:
                while time.monotonic() < deadline:
                    if selector.select(1):
                        line = process.stdout.readline()
                        if not line:
                            raise RuntimeError('app-server exited')
                        message = json.loads(line)
                        if message.get('id') == i:
                            assert 'error' not in message, 'native RPC error'
                            return message['result']
                raise TimeoutError(method)
            finally:
                selector.close()
        request(1, 'initialize', {'clientInfo': {'name': 'handoff-skills-check', 'version': '1'}})
        response = request(2, 'skills/list', {'cwds': [str(p) for p in roots], 'forceReload': True})
        assert len(response['data']) == len(roots)
        for entry in response['data']:
            assert not entry.get('errors'), 'native skill parse errors'
            wanted = {s['name']: s for s in entry['skills'] if s['name'] in ('caveman', 'ponytail')}
            assert set(wanted) == {'caveman', 'ponytail'}
            for name, skill in wanted.items():
                expected = Path(entry['cwd']) / '.agents' / 'skills' / name / 'SKILL.md'
                assert skill['enabled'] and skill['scope'] == 'repo'
                assert Path(skill['path']).resolve() == expected.resolve()
                assert expected.read_text().startswith('---\n')
        print('PASS: native skills/list discovers enabled repo skills without parse errors in source and fresh project; discovered paths readable.')
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()


def main():
    integrity(ROOT)
    with tempfile.TemporaryDirectory(prefix='handoff-skills-') as folder:
        fresh = Path(folder)
        subprocess.run(['git', 'init', '-q', str(fresh)], check=True)
        (fresh / 'README.md').write_text('Existing initial README\n')
        initialize(fresh)
        assert (fresh / 'README.md').read_text() == 'Existing initial README\n'
        original = (fresh / 'AGENTS.md').read_bytes()
        assert original == (ROOT / 'templates' / 'AGENTS.md').read_bytes()
        assert '每次新会话必须主动读取' in original.decode()
        assert '只有用户明确禁用' in original.decode()
        assert '加载失败' in original.decode()
        assert (fresh / 'PROJECT_CONTEXT.md').exists()
        assert (fresh / 'docs' / 'handoff' / 'README.md').exists()
        try:
            initialize(fresh)
        except FileExistsError:
            pass
        else:
            raise AssertionError('must refuse reinitializing an existing project')
        integrity(fresh)
        try:
            inherit(fresh)
        except FileExistsError:
            pass
        else:
            raise AssertionError('must not overwrite existing skills')
        assert (fresh / 'AGENTS.md').read_bytes() == original
        skill = fresh / '.agents' / 'skills' / 'ponytail' / 'SKILL.md'
        skill.write_text('damaged fixture')
        try:
            integrity(fresh)
        except AssertionError:
            pass
        else:
            raise AssertionError('must reject damaged vendored content')
        skill.write_bytes((ROOT / '.agents' / 'skills' / 'ponytail' / 'SKILL.md').read_bytes())
        with tempfile.TemporaryDirectory(prefix='handoff-disabled-') as disabled_folder:
            disabled = Path(disabled_folder)
            subprocess.run(['git', 'init', '-q', str(disabled)], check=True)
            initialize(disabled, disable_skills=True)
            assert not (disabled / '.agents' / 'skills').exists()
            assert '--disable-skills' in (disabled / 'PROJECT_CONTEXT.md').read_text()
            assert (disabled / 'AGENTS.md').read_bytes() == original
        print('PASS: default new-project skills, full hashes, per-session policy, explicit opt-out record, no-overwrite, preserved guidance, corruption rejection.')
        if '--host' in sys.argv:
            print(subprocess.check_output(['codex', '--version'], text=True).strip())
            discover([ROOT, fresh])


if __name__ == '__main__':
    main()
