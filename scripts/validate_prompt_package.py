#!/usr/bin/env python3
"""Validate the prompt-package contract, not WooCommerce plugin behavior."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
master_candidates=[ROOT/'WPEssential_Cart_Rules_Inspector_AI_Native_Master_Development_Prompt.md',ROOT.parent/'WPEssential_Cart_Rules_Inspector_AI_Native_Master_Development_Prompt.md']
master=next((p for p in master_candidates if p.exists()),None)
assert master is not None, 'master missing'
s=master.read_text(encoding='utf-8')
for i in range(20):
    assert re.search(rf'^## {i}\. ',s,re.M),f'Missing required Master section {i}'
assert s.count('### PHASE P')==5
ui=json.loads((ROOT/'docs/UI_SCREEN_INVENTORY.json').read_text(encoding='utf-8'))
assert len(ui)==18 and len({u['id'] for u in ui})==18
assert all(u['id'] in s for u in ui)
req=json.loads((ROOT/'docs/REQUIREMENTS_REGISTRY.json').read_text(encoding='utf-8'))
assert len(req)>=140 and len({x['id'] for x in req})==len(req)
assert all(x['status']=='planned' and x['verified_evidence'] is None for x in req)
all_tasks=json.loads((ROOT/'.ai/tasks.template.json').read_text(encoding='utf-8'))['tasks']
assert len(all_tasks)>=180
mapping={t['id']:t for t in all_tasks}
assert len(mapping)==len(all_tasks)
assert set(t['phase'] for t in all_tasks)==set(('P0','P1','P2','P3','P4'))
assert all(t['status']=='pending' for t in all_tasks)
for task in all_tasks:
    assert all(dep in mapping for dep in task['dependencies']),task['id']
state={}
# Cycle-detection using Kahn topological pass.
remaining={k:set(t['dependencies']) for k,t in mapping.items()}
resolved=set()
while remaining:
    ready={k for k,deps in remaining.items() if deps<=resolved}
    assert ready, f'Task dependency cycle: {list(remaining)[:10]}'
    resolved|=ready
    remaining={k:deps for k,deps in remaining.items() if k not in ready}
for f in ['scripts/agent_state.py','scripts/build_playground_bundles.py','scripts/validate_blueprints.py','scripts/generate_readmes.py','playground/blueprints/free/blueprint.json','playground/blueprints/pro/blueprint.json','templates/release/product-docs.example.json']:
    assert (ROOT/f).is_file(),f
print(f'PACKAGE STRUCTURE PASS: master sections 0–19, 5 phases, {len(ui)} screens, {len(req)} requirements/test cases, {len(all_tasks)} pending acyclic tasks')
print('This test does not run WooCommerce, WordPress Playground or marketplace checks.')
