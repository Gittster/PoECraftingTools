# Data source

Files in this directory are vendored snapshots of generated Path of Exile game data, not written by us.

| File | Source | Fetched | Notes |
|---|---|---|---|
| `essences.json` | https://repoe-fork.github.io/essences.json | 2026-07-30 | Maps each essence to its guaranteed mod id per item class, item level restriction, tier, and corruption-only flag. |

Generator/source code: https://github.com/repoe-fork/repoe (runs PyPoE against the game client).

This is a snapshot, not a live feed. It goes stale on game patches that change essence mods or add new ones. Re-fetch manually and update the date above when refreshing.
