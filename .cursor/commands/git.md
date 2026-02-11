# Git - GitHub Workflow

**Repo:** https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Parameters

- `/git` → Auto: infer message from diff, commit & push (no confirmation).
- `/git confirm` or `/git ask` → Propose message, wait for confirmation, then commit & push.
- `/git <text>` → Use `<text>` as commit message, then commit & push.

## Workflow

1. **Pull:** `git fetch` then `git status`. If behind: `git pull --rebase`, show incoming (e.g. `git log HEAD@{1}..HEAD --oneline`).
2. **Inspect:** `git status`, `git diff --stat`, and enough `git diff` to summarize. Write one short conventional-commit message (feat/fix/docs/chore, ≤72 chars). If user gave text after `/git`, use that.
3. **Confirm only if** user said "confirm" or "ask": "I'll use: `<message>`. Confirm or edit?" — then wait. Otherwise skip.
4. **Submit:** `git add .`, `git commit -m "..."`, show `git log origin/<branch>..HEAD --oneline`, then `git push`.

**Don't commit:** secrets, `.env`, large data, build artifacts. Use `.gitignore`.

## Utilities

- Status: `git status` | Last commit: `git log -1 --format=%ci` | Ignored: `git status --ignored` | Recent: `git log --oneline -5` | Stash: `git stash` / `git stash pop`
