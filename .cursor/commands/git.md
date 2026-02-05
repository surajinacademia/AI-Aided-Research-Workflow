# Git - Complete GitHub Workflow

**Repository:** https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Primary Command (What /git does)
```bash
git status && git add . && git commit -m "Update: $(date '+%Y-%m-%d %H:%M')" && git push
```
**Default behavior:** Shows status, then automatically:
- Stages all changes (`git add .`)
- Commits with timestamp: `"Update: YYYY-MM-DD HH:MM"`
- Pushes to GitHub (no prompts)

### Manual Three-Step Process
```bash
git add .
git commit -m "describe your changes here"
git push
```

## Utility Commands

### Check Status Only
```bash
git status
```
Shows what files changed without committing.

### Check Ignored Files
```bash
git status --ignored
```
Shows files that won't be committed (in .gitignore).

### View Recent Commits
```bash
git log --oneline -5
```
