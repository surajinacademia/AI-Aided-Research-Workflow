# Git - Complete GitHub Workflow

**Repository:** https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Primary Command (What /git does)
```bash
git status && \
if [ $(git diff --cached --numstat | wc -l) -gt 10 ] || [ $(git diff --numstat | wc -l) -gt 10 ]; then \
  read -p "📝 Enter commit message: " msg && git add . && git commit -m "$msg" && git push; \
else \
  git add . && git commit -m "Update: $(date '+%Y-%m-%d %H:%M')" && git push; \
fi
```
**Smart mode:** Shows status, then:
- If 10+ files changed → prompts for custom message
- If fewer files → auto-commits with timestamp

## Alternative Commands

### Always Auto-Commit with Timestamp
```bash
git status && git add . && git commit -m "Update: $(date '+%Y-%m-%d %H:%M')" && git push
```

### Always Prompt for Message
```bash
git status && read -p "Enter commit message: " msg && git add . && git commit -m "$msg" && git push
```

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
Shows last 5 commits.
