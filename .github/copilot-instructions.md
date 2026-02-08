# AI-Aided-Research-Workflow

## Rules

### image-analysis

**Priority:** high

## Priority: Use MCP Tools First

**Always prioritize Cellpose MCP over custom code:**

- MCPs are GPU-accelerated and tested
- Only write scripts when explicitly requested
- Use Python packages for tasks MCPs don't cover

## Cellpose MCP Tools

**Segmentation:**

```python
CallMcpTool("user-cellpose", "segment_cells_2d",
            {"image_path": "cells.tif",
             "model_type": "cyto3",  # or "nuclei", "cpsam"
             "diameter": 30})  # 0 = auto-estimate
```

**Models:** `cyto`/`cyto2`/`cyto3` (general cells), `nuclei` (nuclei only), `cpsam` (most accurate)

**Key parameters:** `model_type`, `diameter`, `flow_threshold`, `cellprob_threshold`, `channels`

**Image restoration:**

- `denoise_image` - Remove noise
- `deblur_image` - Restore blur
- `upsample_image` - Super-resolution
- `restore_and_segment` - Combined pipeline

**Utilities:** `estimate_cell_diameter`, `load_image_info`, `segment_cells_batch`, `list_available_models`

## Python Packages

**Use when MCPs don't cover your needs:**

### scikit-image

```python
from skimage.measure import regionprops
from skimage.filters import gaussian, threshold_otsu
from skimage.morphology import opening, closing

props = regionprops(masks)
for r in props:
    area, perimeter, eccentricity = r.area, r.perimeter, r.eccentricity
```

**Common functions:** `regionprops`, `gaussian`, `median`, `threshold_otsu`, morphology operations

### scipy.ndimage

```python
from scipy.ndimage import gaussian_filter, label

smoothed = gaussian_filter(image, sigma=2)
labeled, n = label(binary_mask)
```

### aicsimageio

```python
from aicsimageio import AICSImage

img = AICSImage("data.nd2")
data = img.get_image_data("CZYX")
``` 

## Quick Reference

**When to use MCPs:**

- Cell/nuclei segmentation
- Denoise, deblur, upsample
- Batch processing

**When to write code:**

- Measurements (regionprops)
- Statistical analysis
- Custom filters
- Data aggregation

### project-repo

**Priority:** high

This project demonstrates context engineering for AI-aided research workflows.

**📖 Full documentation:** See `README.md` for complete information about this framework.

## Project Structure Quick Reference

Key locations in this repository:

- **ai-rulez/rules/** - AI guidance (see main rules for complete listing)
- **ai-rulez/agents/** - Specialized agents (e.g., literature-review)
- **ai-rulez/mcp/** - MCPs (e.g., napari-mcp, cellpose-mcp)
- **Data_analysis/** - Example datasets and data analysis workflows
- **Image_analysis/** - 23 sample microscopy images for testing
- **deep_stuff/** - Random stuff like rules of life, etc.
- **workflow.ipynb** - Workflow notebook

### python-coding-standards

**Priority:** high

## Core Principles

- **Style**: Follow PEP 8
- **Execution**: Keep silent - minimize print statements
- **Performance**: Use vectorized operations (numpy/pandas) over loops
- **Functions**: Analysis returns data only; plots accept `ax` argument
- **Simplicity**: Write inline code for one-off logic; functions for reuse

## Jupyter Notebooks

**⚠️ CRITICAL: Edit `.py` files only, NOT `.ipynb`**

```python
# # Analysis Title

# Code cells use # %%
data = pd.read_csv('data.csv')

# Maintain 5-line spacing between cells
result = analyze(data)
```

Notebooks sync automatically via jupytext.

## Analysis vs Plotting

**NEVER create plots inside analysis functions:**

```python
def run_simulation():
    history = compute_dynamics()
    plt.plot(history)  # DON'T DO THIS
    return history

def run_simulation():
    """Compute dynamics and return history."""
    return compute_dynamics()

history = run_simulation()
fig, ax = plt.subplots()
ax.plot(history)
plt.show()
```

## Plot Functions

**All plot functions MUST accept axes:**

```python
def plot_data(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    plt.savefig('plot.png')

def plot_data(data, ax):
    """Plot data on provided axes."""
    ax.plot(data)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    return ax

fig, ax = plt.subplots(figsize=(8, 6))
plot_data(data, ax)
plt.savefig('plot.svg')
plt.show()
```

## Plotting Configuration

**Standard setup:**

```python
import matplotlib.pyplot as plt
import minimalist

minimalist.use_style("science")
plt.rcParams.update({'figure.facecolor': 'none', 'axes.facecolor': 'none'})

text_width = 510/72.27  # LaTeX text width in inches
```

**Standards:**

- Use matplotlib only (no seaborn)
- Save as SVG for vector graphics
- Save in `figures/` folder
- Use minimalist "science" style

## Code Style

**Inline logic for one-off operations:**

```python
def normalize(img):
    return (img - img.min()) / (img.max() - img.min())

for q in quadrants:
    result = normalize(q)

for q in quadrants:
    result = (q - q.min()) / (q.max() - q.min())
```

**Silent execution with inline comments:**

```python
print("Processing...")
for i, f in enumerate(files):
    print(f"File {i+1}/{len(files)}")
    process(f)

for f in files:
    process(f)
```

## Docstrings

**Simple format with Parameters and Returns:**

```python
def analyze_data(df, threshold=0.5):
    """
    Analyze dataframe and compute metrics.

    Parameters:
    - df: pandas DataFrame with columns ['x', 'y', 'z']
    - threshold: cutoff value for filtering (default 0.5)

    Returns:
    - dict with keys 'mean', 'std', 'count'
    """
    filtered = df[df['x'] > threshold]
    return {
        'mean': filtered['y'].mean(),
        'std': filtered['y'].std(),
        'count': len(filtered)
    }
```

## Data Analysis

**Pandas best practices:**

```python
df['result'] = df['x'] * df['y']  # Not: df.apply(lambda row: row['x'] * row['y'])

result = (df
    .query('value > 0')
    .groupby('category')
    .agg({'value': ['mean', 'std']})
    .reset_index()
)

result.to_csv('output.csv', index=False)
```

## Quick Checklist

Before committing:

- [ ] Analysis functions return data (no plots inside)
- [ ] Plot functions accept `ax` argument
- [ ] Jupyter: edited `.py` not `.ipynb`
- [ ] Silent execution (minimal prints)
- [ ] Docstrings with Parameters/Returns
- [ ] Inline logic for one-off operations
- [ ] File order: imports → config → functions → execution

### rules

**Priority:** critical

The agent is an expert in:
- **Data Analysis**: Exploratory data analysis, statistical analysis, data visualization
- **Image Analysis**: Microscopy image processing, segmentation, quantification
- **Quantitative Analysis**: Numerical computation, PDEs, ODEs, and mathematical modeling
- **AI Agents & MCPs**: Model Context Protocol integration, agent workflows, context engineering

## Core: Non-negotiable Rules

- Provide concise, clear explanations
- Ask questions; don't make assumptions
- Prioritize readable, editable, reproducible, simple, modular code
- Write concise, technical responses

## Data Analysis
- Use pandas, numpy, scipy, matplotlib for analysis and visualization

## Image Analysis Expertise

**Tools and Integration:**
- **napari-mcp**: Interactive image visualization and analysis
- **cellpose-mcp**: Cell segmentation and quantification
- Prioritize MCP tools over custom implementations
- Extract quantitative metrics and validate results visually
- Document analysis steps

**Mathematical Tools:**
- Use sympy-mcp for calculus, algebra, differential equations
- Use fmcp for mathematical plotting (matplotlib, numpy)
- Generate LaTeX equations for documentation
- Solve systems symbolically before numerical implementation
- Vectorized operations for performance

**Workflow:**
- Save results as CSV, plots as SVG
- Only write custom scripts when explicitly requested
- Validate results with custom code when needed

## Location of important files

- **Rules** 
  - `rules.md`: Main rule file with project-wide standards and expert domains
  - project-repo.md: Repository structure documentation and navigation guide for AI agents
  - python-coding-standards.md: Python coding patterns, best practices, and visualization standards
  - image-analysis.md: Image analysis workflow patterns and MCP tool prioritization

- **Commands** 
  - `git.md`: Git workflow: quick commit & push, manual workflows, and status checking
  - `airulez.md`: AI-Rulez workflow: generate and commit with default message.

- **Agents** 
  - `literature-review.md`: Expert literature research for biophysics and cell mechanics, semantic searches across local papers, Zotero library, and web sources

- **MCPs** 
  - `napari-mcp.md`: Interactive image visualization and analysis
  - `cellpose.md`: Cell segmentation and quantification
  - `fmcp.md`: Mathematical plotting (matplotlib, numpy, sympy)
  - `sympy-mcp.md`: Symbolic mathematics and calculus
  - `claude-scientific-skills.md`: Scientific computing capabilities
  - `data-forge.md`: Data manipulation and analysis
  - `notion.md`: Notion workspace integration
  - `zotero.md`: Zotero library access for literature management
  - `cursor-ide-browser.md`: Browser automation for testing

## Context

### architecture

This project follows a modular architecture with clear separation of concerns.

## Directory Structure

- **cmd/**: Command-line interface and entry points
- **internal/**: Private application code
- **pkg/**: Public library code
- **tests/**: Test files and fixtures

## Key Principles

- Dependency injection for better testability
- Interface-based design for flexibility
- Clear separation between business logic and infrastructure

### git

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

