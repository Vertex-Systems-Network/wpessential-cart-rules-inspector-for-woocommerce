# How to use this ZIP (repository setup)

1. **Extract** the AI Development Prompt Package ZIP. It is NOT a WordPress-installable plugin.
2. **Create/open the GitHub repository** `wpessential-cart-rules-inspector` (or existing project repo).
3. **Upload both root instruction Markdown files plus ALL companion subfolders/files**, preserving hidden `.ai` and the folder structure. Do not overwrite existing real progress/state.
4. Connect a coding agent with repo source write, build/test and Git permissions. If using a runner with continuous task mode, enable that mode; the ZIP alone cannot run tasks in the background.
5. Instruct agent: “Read Master and START_AGENT completely, inspect repository, recover AI state, select next unblocked task, implement/test/fix/commit and automatically continue while runtime active. Do not ask for routine confirmations.”
6. Agent starts with `python scripts/agent_state.py init` and `python scripts/agent_state.py next`, checks exact task and continues through only P0–P4. If files are stored under a `Companion_Files/` wrapper, copy the **contents** into the repository root according to Master Section 4 before running scripts.
7. Completion outputs: **two real plugin ZIP files**, Free `readme.txt`, Free/Pro `README.md`, functional Blueprints, test evidence, adapter coverage report, WordPress.org Free submission pack and Woo Marketplace Pro reviewer pack.

Avoid placing this prompt package ZIP itself in WordPress **Plugins → Add New**. Do not treat a template Blueprint as a tested site, or an unverified adapter as supported.
