# START_HERE — persistent execution resume pointer

**Template only — not evidence of development.** Never overwrite an existing verified `START_HERE.md`.

Product: WPEssential Cart Rules Inspector for WooCommerce

Phase: `P0` (initial only)
Next task: `P0-001` (initial only)
Status: NOT STARTED
Last verified commit: None
Last executable test: None

## Agent startup sequence
1. Read Master and START_AGENT in full.
2. Inspect repository/gits status, compare actual source with state, recover current phase.
3. Initialize `.ai/tasks.json`/`.ai/state.json` from templates only if missing.
4. Pick next unblocked dependency-safe task. Implement, test, fix, record evidence, commit. Repeat without routine confirmation while runner active.
5. On forced termination update this file with exact phase/next task/command/blocker so next runner invocation resumes.

## Current blockers
None known yet; not equivalent to having executed all tests.

## Release gates
P0 pending; P1 pending; P2 pending; P3 pending; P4 pending.
