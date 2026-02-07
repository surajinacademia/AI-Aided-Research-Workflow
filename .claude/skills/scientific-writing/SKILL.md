<!--
🤖 AI-RULEZ :: GENERATED FILE — DO NOT EDIT DIRECTLY
Project: AI-Aided-Research-Workflow
Generated: 2026-02-05 12:14:59
Source: .ai-rulez/config.yaml
Target: /Users/suraj/Documents/AI-Aided-Research-Workflow/.claude/skills/scientific-writing/SKILL.md
Content: rules=4, sections=0, agents=1

WHAT IS AI-RULEZ
AI-Rulez is a directory-based AI governance tool. All configuration lives in
the .ai-rulez/ directory. This file is auto-generated from source files.

.AI-RULEZ FOLDER ORGANIZATION
Root content (always included):
  .ai-rulez/config.yaml    Main configuration (presets, profiles)
  .ai-rulez/rules/         Mandatory rules for AI assistants
  .ai-rulez/context/       Reference documentation
  .ai-rulez/skills/        Specialized AI prompts
  .ai-rulez/agents/        Agent definitions

Domain content (profile-specific):
  .ai-rulez/domains/{name}/rules/    Domain-specific rules
  .ai-rulez/domains/{name}/context/  Domain-specific documentation
  .ai-rulez/domains/{name}/skills/   Domain-specific AI prompts

Profiles in config.yaml control which domains are included.

INSTRUCTIONS FOR AI AGENTS
1. NEVER edit this file (/Users/suraj/Documents/AI-Aided-Research-Workflow/.claude/skills/scientific-writing/SKILL.md) - it is auto-generated

2. ALWAYS edit files in .ai-rulez/ instead:
   - Add/modify rules: .ai-rulez/rules/*.md
   - Add/modify context: .ai-rulez/context/*.md
   - Update config: .ai-rulez/config.yaml
   - Domain-specific: .ai-rulez/domains/{name}/rules/*.md

3. PREFER using the MCP Server (if available):
   Command: npx -y ai-rulez@latest mcp
   Provides safe CRUD tools for reading and modifying .ai-rulez/ content

4. After making changes: ai-rulez generate

5. Complete workflow:
   a. Edit source files in .ai-rulez/
   b. Run: ai-rulez generate
   c. Commit both .ai-rulez/ and generated files

Documentation: https://github.com/Goldziher/ai-rulez
-->

---
description: Creates concise, structured scientific documents with LaTeX equations, integrated figures, and clear technical writing. Use when documenting results, writing research summaries, or creating technical reports.
name: scientific-writing
priority: high
---

# Scientific Writing

Creates publication-quality markdown documents with mathematical rigor and visual clarity.

## Core Principles

1. **Concision**: Every sentence must earn its place
2. **Structure**: Logical flow with clear hierarchies
3. **Precision**: Technical accuracy over verbosity
4. **Integration**: Seamlessly embed figures and equations
5. **Clarity**: Complex ideas expressed simply

---

## Document Structure

### Standard Template

```markdown
# [Descriptive Title]

## Summary
[2-3 sentences: what was done, key finding, significance]

## Methods
[Essential details only - enough to reproduce]

## Results
[Observations → Data → Interpretation]

### [Subsection 1]
[Finding with supporting figure/equation]

### [Subsection 2]
[Finding with supporting figure/equation]

## Discussion
[Implications, limitations, future directions - 1 paragraph max]
```

### Section Guidelines

**Summary (3-5 lines)**
- First sentence: what you investigated
- Second sentence: how you investigated it
- Third sentence: what you found
- NO background or motivation

**Methods (minimal)**
- Only non-standard procedures
- Reference standard protocols by name
- Use lists for clarity

**Results (core content)**
- Lead with observation, follow with data
- One finding per subsection
- Figure/equation immediately after relevant text
- NO speculation (save for Discussion)

**Discussion (1 paragraph)**
- Interpret in broader context
- State limitations explicitly
- Suggest next steps

---

## Writing Style Rules

### Concision Tactics

**Before (wordy)**:
> The results that we obtained from the experiment clearly demonstrate that there is a significant increase in the fluorescence intensity.

**After (concise)**:
> Fluorescence intensity increased 3.2-fold (p < 0.001).

**Common eliminations**:
- ❌ "It is important to note that..."
- ❌ "The results clearly demonstrate..."
- ❌ "As can be seen from the figure..."
- ❌ "In order to..." → ✅ "To..."
- ❌ "Due to the fact that..." → ✅ "Because..."

### Active Voice

- ✅ "We measured force using AFM"
- ❌ "Force was measured using AFM"
- ✅ "Cells exhibited biphasic dynamics"
- ❌ "Biphasic dynamics were exhibited by cells"

### Precision

**Vague**: "The protein concentration was high"
**Precise**: "Protein concentration was 2.5 mg/mL"

**Vague**: "Cells responded quickly"
**Precise**: "Cells responded within 30 s"

---

## LaTeX Equations

### Inline Math

Use `$...$` for inline equations:

```markdown
The diffusion coefficient $D = 0.43 \pm 0.05 \, \mu\text{m}^2/\text{s}$ indicates...
```

### Display Math

Use `$$` with `\begin{}` and `\end{}` for block equations:

```markdown
The force balance is described by:

$$
\begin{equation}
F_{\text{total}} = F_{\text{spring}} + F_{\text{drag}} = kx + \gamma \frac{dx}{dt}
\end{equation}
$$

where $k$ is the spring constant and $\gamma$ is the drag coefficient.
```

### Equation Environments

**Common environments**:
- `equation` - Single numbered equation
- `align` - Multiple aligned equations
- `split` - Split long equations across lines

**Examples**:

```markdown
$$
\begin{align}
\sigma_{xx} &= E \epsilon_{xx} \\
\sigma_{yy} &= E \epsilon_{yy}
\end{align}
$$
```

### Equation Style

**Good practices**:
- Define all variables immediately after equation
- Use `\text{}` for words in equations: $F_{\text{max}}$
- Use proper spacing: `\,` for thin space (units)
- Use `equation` environment for automatic numbering

**Example**:

```markdown
The relationship between stress $\sigma$ and strain $\epsilon$ follows:

$$
\begin{equation}
\sigma = E \epsilon
\end{equation}
$$

where $E = 5 \pm 0.3$ kPa is the Young's modulus.
```

---

## Figure Integration

### Workflow

1. **Generate figure during analysis** (follow python-coding-standards)
2. **Save as SVG** in `figures/` folder
3. **Reference immediately** after relevant text
4. **Caption format**: statement of finding, not description

### Figure Template

```markdown
Force increased linearly with deformation up to 20% strain, then plateaued (Figure 1).

![Force-deformation relationship](figures/force_vs_strain.svg)
**Figure 1.** Linear stress-strain response transitions to plateau regime at ε > 0.2.
```

### Caption Guidelines

**Bad (descriptive)**:
> Figure 1. A plot showing force on the y-axis and deformation on the x-axis.

**Good (interpretive)**:
> Figure 1. Force increases linearly with deformation until strain exceeds 0.2.

**Best (finding)**:
> Figure 1. Biphasic mechanical response reveals strain-stiffening at ε > 0.2.

### Multiple Panels

For multi-panel figures:

```markdown
![Analysis overview](figures/analysis_overview.svg)
**Figure 2.** Cell morphology changes with substrate stiffness. **(A)** Representative images on soft (1 kPa), medium (10 kPa), and stiff (100 kPa) substrates. **(B)** Quantification shows area increases 2.5-fold from soft to stiff. **(C)** Aspect ratio decreases with stiffness (p < 0.001, n = 150 cells per condition).
```

---

## Data Presentation

### Tables (use sparingly)

Only when comparing multiple conditions across multiple metrics:

```markdown
| Condition | Spring Constant (pN/nm) | Relaxation Time (s) | n |
|-----------|------------------------|---------------------|---|
| Control   | 12.3 ± 1.2            | 45 ± 8             | 23 |
| Drug A    | 8.7 ± 0.9*            | 67 ± 12*           | 21 |
| Drug B    | 15.1 ± 1.8            | 38 ± 6             | 19 |

*p < 0.05 vs. control
```

**Table caption**: Place above table, descriptive

### Inline Data

For single comparisons, embed in text:

> Treatment increased velocity from 0.23 ± 0.03 to 0.41 ± 0.05 μm/s (p < 0.001, n = 45).

---

## Common Patterns

### Introducing Analysis

**Pattern**: Goal → Approach → Key result

> To determine whether force depends on loading rate, we performed constant-velocity indentation at speeds from 0.1 to 10 μm/s. Peak force scaled linearly with velocity (Figure 3A), consistent with viscoelastic behavior.

### Quantitative Results

**Pattern**: Observation → Measurement → Statistics

> Cells on stiff substrates adopted elongated morphologies. Aspect ratio increased from 1.8 ± 0.2 (soft) to 3.4 ± 0.4 (stiff), a 1.9-fold change (p < 0.001, n = 120 cells, Figure 2B).

### Model Validation

**Pattern**: Model → Prediction → Test → Result

> If force transmission is primarily via focal adhesions, disrupting integrin binding should reduce traction forces. We treated cells with RGD peptide and measured a 73% reduction in traction stress (Figure 4), confirming integrin-mediated adhesion.

---

## Checklist

Before finalizing document:

- [ ] Summary states finding in 3 sentences
- [ ] No sentence exceeds 25 words
- [ ] All equations defined immediately after appearance
- [ ] Figures referenced in text before appearing
- [ ] Figure captions state findings, not descriptions
- [ ] NO phrases: "clearly", "obviously", "it is important to note"
- [ ] NO repetition between sections
- [ ] Methods include only non-standard details
- [ ] Discussion is ≤ 1 paragraph
- [ ] All data includes uncertainty and sample size
- [ ] Active voice used throughout

---

## Quick Reference

### Numbers and Units

- Use ± for uncertainty: `5.2 ± 0.3 kPa`
- Thin space before units: `10 \, \mu\text{m}`
- Scientific notation for extremes: $3.2 \times 10^{-6}$
- Significant figures match precision

### Common Abbreviations

First use: full term (abbreviation)
> Atomic force microscopy (AFM) measurements revealed...

Subsequent: abbreviation only
> AFM images showed...

### References

Inline citation:
> Previous studies^[1,2]^ demonstrated...

End of document:
```markdown
## References

1. Smith et al. (2023) Nature 612: 123-130
2. Jones et al. (2022) Science 378: 456-460
```

---

## Anti-Patterns

### Avoid Redundancy

**Bad**:
> Figure 1 shows the force-distance curve. As can be seen in Figure 1, force increases with distance. The figure clearly demonstrates that...

**Good**:
> Force increased linearly with distance (Figure 1).

### Avoid Throat-Clearing

**Bad**:
> It is important to note that our results suggest that it may be possible that cells potentially exhibit...

**Good**:
> Cells exhibit viscoelastic behavior.

### Avoid Over-Qualification

**Bad**:
> The data appear to suggest that there might be a possible trend toward increased stiffness.

**Good**:
> Stiffness increased 1.8-fold (p = 0.03).

---

## Example Document

See EXAMPLE.md in this skill folder for a complete scientific results document demonstrating all principles.


## Rules

### image-analysis
**Priority:** high

# Biological Image Analysis

## Priority: Use MCP Tools First

**Always prioritize Cellpose MCP over custom code:**

- MCPs are GPU-accelerated and tested
- Only write scripts when explicitly requested
- Use Python packages for tasks MCPs don't cover

## Cellpose MCP Tools

**Segmentation:**

```python
# Server: "user-cellpose"
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

# Measure cells after segmentation
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

# Load proprietary formats (ND2, CZI, LIF, LSM)
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

# AI Research Workflow - Navigation Guide

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

# Python Coding Standards

## Core Principles

- **Style**: Follow PEP 8
- **Execution**: Keep silent - minimize print statements
- **Performance**: Use vectorized operations (numpy/pandas) over loops
- **Functions**: Analysis returns data only; plots accept `ax` argument
- **Simplicity**: Write inline code for one-off logic; functions for reuse


## Jupyter Notebooks

**⚠️ CRITICAL: Edit `.py` files only, NOT `.ipynb`**

```python
# %% [markdown]
# # Analysis Title

# %%
# Code cells use # %%
data = pd.read_csv('data.csv')

# %%
# Maintain 5-line spacing between cells
result = analyze(data)
```

Notebooks sync automatically via jupytext.

## Analysis vs Plotting

**NEVER create plots inside analysis functions:**

```python
# ❌ BAD: Analysis creates plot
def run_simulation():
    history = compute_dynamics()
    plt.plot(history)  # DON'T DO THIS
    return history

# ✅ GOOD: Analysis returns data
def run_simulation():
    """Compute dynamics and return history."""
    return compute_dynamics()

# Plot in separate cell
history = run_simulation()
fig, ax = plt.subplots()
ax.plot(history)
plt.show()
```

## Plot Functions

**All plot functions MUST accept axes:**

```python
# ❌ BAD: Creates own figure
def plot_data(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    plt.savefig('plot.png')

# ✅ GOOD: Accepts axes argument
def plot_data(data, ax):
    """Plot data on provided axes."""
    ax.plot(data)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    return ax

# Caller controls figure
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

# Publication figure widths
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
# ❌ BAD: Over-abstracted
def normalize(img):
    return (img - img.min()) / (img.max() - img.min())

for q in quadrants:
    result = normalize(q)

# ✅ GOOD: Inline for one-off
for q in quadrants:
    result = (q - q.min()) / (q.max() - q.min())
```

**Silent execution with inline comments:**

```python
# ❌ BAD: Noisy output
print("Processing...")
for i, f in enumerate(files):
    print(f"File {i+1}/{len(files)}")
    process(f)

# ✅ GOOD: Silent with comments
for f in files:
    # Normalize → filter → threshold
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
# Use vectorized operations
df['result'] = df['x'] * df['y']  # Not: df.apply(lambda row: row['x'] * row['y'])

# Method chaining for readability
result = (df
    .query('value > 0')
    .groupby('category')
    .agg({'value': ['mean', 'std']})
    .reset_index()
)

# Save as CSV
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

# Main rule for the project

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

# Project Architecture

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


