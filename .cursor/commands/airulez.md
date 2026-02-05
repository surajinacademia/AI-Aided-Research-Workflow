# ai-rulez - Generate and Commit

**Use after editing anything under `.ai-rulez/`** so all presets stay in sync and changes are committed.

## When to use

- You edited `.ai-rulez/rules/`, `context/`, `skills/`, `agents/`, or `config.yaml`
- You want to regenerate tool outputs and commit in one step

## Steps

1. **Generate** (from repo root):
   ```bash
   uvx ai-rulez generate
   ```

2. **Stage** both source and generated files:
   - `.ai-rulez/` (entire directory)
   - `CLAUDE.md`
   - `.cursor/rules/`
   - `.github/copilot-instructions.md`
   - `.agent/rules/`

   ```bash
   git add .ai-rulez/ CLAUDE.md .cursor/rules/ .github/copilot-instructions.md .agent/rules/
   ```

3. **Commit** with a clear message:
   - If the user provided text after `/airulez` (e.g. `/airulez add image rule`), use that in the message.
   - Otherwise use: `docs: update AI rules (ai-rulez generate)`

   ```bash
   git commit -m "docs: update AI rules (ai-rulez generate)"
   ```

4. **Do not push** unless the user asks. After committing, say what was committed and remind them they can push when ready.

## Command parameters

- `/airulez` — Generate and commit with default message.
- `/airulez <hint>` — Generate and commit; use hint in the commit message (e.g. `/airulez add Python style rule` → `docs: add Python style rule (ai-rulez generate)`).

## Notes

- Never edit generated files (CLAUDE.md, .cursor/rules/*.mdc, etc.) by hand; edit only under `.ai-rulez/`.
- If `uvx ai-rulez generate` fails, report the error and do not commit.
