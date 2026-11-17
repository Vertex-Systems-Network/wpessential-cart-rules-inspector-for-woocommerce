# WPEssential Cart Rules Inspector — AI Development Prompt Package

This is **not a functional WordPress plugin ZIP**. It contains an AI-Native development contract, a one-shot launcher, initial task/memory templates, rule/UI registries, WordPress Playground Blueprint templates, and executable starter scripts. Real Free and Pro plugin source/ZIP files are expected as **outputs** of development.

## Setup in GitHub

1. Extract the **AI Development Prompt Package** ZIP.
2. Upload the **entire extracted folder contents** to your project repository, retaining `.ai`, `docs`, `scripts`, `playground`, `templates` and the two root markdown instruction files.
3. Do not overwrite existing source code or a real `.ai/state.json` / `START_HERE.md` if already under active development.
4. Connect your coding agent with repository read/write/build/test permissions.
5. Send the contents of `WPEssential_Cart_Rules_Inspector_START_AGENT.md` or tell the agent: **Read both project instruction files completely; inspect repo; recover task state; implement the next unblocked task; test, repair, commit and automatically continue without routine human confirmation while the runner is active.**

## Initial files

- `WPEssential_Cart_Rules_Inspector_AI_Native_Master_Development_Prompt.md` — full contract.
- `WPEssential_Cart_Rules_Inspector_START_AGENT.md` — agent startup/resume instructions.
- `START_HERE_TEMPLATE.md` — human-readable resume state, copied only if no real state exists.
- `.ai/state.template.json` and `.ai/tasks.template.json` — not actual progress.
- `BACKLOG_TEMPLATE.md`, `DECISIONS_TEMPLATE.md` — planning scaffolds.
- `docs/UI_SCREEN_INVENTORY.json` — screen ownership and implementation acceptance.
- `docs/REQUIREMENTS_REGISTRY.json` — feature/test IDs.
- `docs/ACCEPTANCE_TEST_MATRIX.md` — test cases initially unexecuted.
- `docs/COMPATIBILITY_MATRIX_TEMPLATE.md` — third-party test truthfulness.
- `playground/blueprints/` — schema-oriented base, Free, Pro and optional third-party compatibility templates.
- `scripts/` — runnable Blueprint validator, bundler and documentation generator.
- `templates/release/product-docs.example.json` — deliberately unreleasable, planned-feature manifest.

## Initial commands (structural only)

```bash
python scripts/validate_blueprints.py
python scripts/build_playground_bundles.py --base-only --out dist/playground
```

The second command packages a baseline WooCommerce Blueprint; **it does not run WordPress**. Run the actual Playground separately, capture screenshots and test logs.

## After actual plugins are developed

```bash
python scripts/build_playground_bundles.py \
  --free dist/wpessential-cart-rules-inspector.zip \
  --pro dist/wpessential-cart-rules-inspector-pro.zip \
  --out dist/playground
```

This will refuse nonexistent or malformed plugin ZIPs. The optimized Composer autoload file must be inside each real plugin archive.

Before release, create real `release_approved:true` metadata with proven commits/tests/version requirements; `scripts/generate_readmes.py` then generates docs. It rejects incomplete test metadata and unreleased manifests.

## Safety note

The word **nonstop** describes repeated task scheduling during an active coding-agent runtime. Neither a prompt nor a ZIP can keep a closed/expired chat executing in the background. Persistent memory is used for automatic resumption in a new active runner.
