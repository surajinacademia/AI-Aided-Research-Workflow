# Git - Complete GitHub Workflow

**Repository:** https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Command Parameters

User can type after `/git` to provide hints or descriptions:
- `/git quick` or `/git small update` → Use quick workflow
- `/git new feature: add user auth` → Use detailed workflow with that description
- `/git` alone → Agent decides based on last commit date and change size

## How to Choose Workflow

1. **Prefer user hint:** If user says "quick" / "small" / "just push" → quick workflow. If they say "significant" / "new feature" / "big change" or give a description → detailed workflow.
2. **If no clear hint:** Run `git status` and `git log -1 --format=%ci` to check last commit date. If last commit was within 2 days AND change set is small (few files, small diff) → quick workflow. Otherwise → detailed workflow.
3. **Default:** When in doubt, use detailed workflow (propose message and ask) to avoid vague commits.

## Quick Workflow (Small / Recent Updates)

**When to use:** 
- Changes are limited and last commit was within 2 days
- User says "quick", "small update", "just sync", etc.
- Typo fixes, config tweaks, small edits, daily sync

**Steps:**
1. Run `git status` (and optionally `git diff --stat` to confirm scope)
2. Stage all changes: `git add .`
3. Commit with short message:
   - If user provided text after `/git`, use that
   - Otherwise use timestamp: `Update: YYYY-MM-DD HH:MM`
4. Push: `git push`

**No confirmation step** - keep it fast for small changes.

## Detailed Workflow (Significant Changes / New Features)

**When to use:**
- New features, large refactors, or many files changed
- User says "significant", "new feature", "release", or provides description
- Last commit is older than 2 days and change set is non-trivial
- Multi-file changes that you'd want to read in `git log` later

**Steps:**
1. Run `git status` and `git diff` (or `git diff --staged` after temporary `git add .`) to see what changed
2. **Propose a commit message:**
   - If user provided description after `/git` (e.g., `/git add auth and dashboard`), use that as basis
   - Otherwise, draft a short descriptive message following conventional commits style:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `docs:` for documentation
     - `chore:` for maintenance
   - Example: "feat: add user authentication and dashboard"
3. **Ask the user:** "I'll use this commit message: `<proposed message>`. Confirm or edit?"
4. **Only after user confirms** (or provides an edit):
   - Stage: `git add .`
   - Commit: `git commit -m "confirmed message"`
   - Push: `git push`

## Standard Git Practices

### Commit Message Format
- Use short subject line (≤72 chars)
- Optional body for explaining "why" (separate with blank line)
- Conventional commits: `feat:`, `fix:`, `docs:`, `chore:` for clarity

### Pull Before Push
- Before pushing, check if branch is behind remote: `git status`
- If branch is ahead AND behind remote, run: `git pull --rebase`
- Then push to avoid unnecessary merge commits

### What Not to Commit
- Check `git status --short` before staging
- Don't stage sensitive files (secrets, `.env`, credentials)
- Don't stage large data files or build artifacts
- Rely on `.gitignore` for automatic exclusion

## Utility Commands

### Check Status Only
```bash
git status
```
Shows what files changed without committing.

### Check Last Commit Date
```bash
git log -1 --format=%ci
```
Shows when the last commit was made (helps decide workflow).

### Check Ignored Files
```bash
git status --ignored
```
Shows files that won't be committed (in .gitignore).

### View Recent Commits
```bash
git log --oneline -5
```
Shows last 5 commits with short messages.

### Stash Changes
```bash
git stash        # Save uncommitted work
git stash pop    # Restore stashed work
```
Use when switching branches with uncommitted changes.
