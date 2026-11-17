# Autonomous AI runner — responsibilities and operational limits

A text prompt or ZIP cannot maintain a running background process after the hosting agent session expires. “Nonstop” means **the active runner** continues selecting and executing tasks without human routine confirmations. The `.ai/` state and `START_HERE.md` allow immediate resumption after interruption.

## Typical single-run startup

```bash
python scripts/agent_state.py init
python scripts/agent_state.py next
python scripts/agent_state.py start P0-001
```

The coding agent must then actually implement and test, commit source changes, write truthful evidence JSON, call `complete` with an actual commit and evidence, and call `next` for following task automatically. State helper does not write plugin source code, run tests or launch other AI agents by itself.

## Evidence example SCHEMA ONLY (not a pass certificate)

```json
{
  "task_id": "P0-001",
  "result": "pending",
  "command": "actual command here",
  "environment": "local machine / WP / WC / PHP versions",
  "timestamp_utc": null,
  "assertions_run": false,
  "test_ids": [],
  "stdout_log": "real log path",
  "summary": "real results, no fabricated claims"
}
```

## Single-writer contract

The orchestration agent owns `.ai/state.json` and `.ai/tasks.json` writes. Other specialized agents contribute patches and evidence but may not independently mark gates as done. For true parallel workers implement cross-platform file locking/transactions before concurrently modifying state; run one writer by default.

## Blockers

Vendor plugin license, marketplace account/QIT credentials or external network access may block specific verification. Record exact prerequisites, do not invent verification, continue unrelated tasks and eventually produce the best completed artifact possible. Do not busy-spin over blocked tasks.
