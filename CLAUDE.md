# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Overview

This is a framework for AI-aided research using **context engineering** to guide AI agents for coding, data analysis, image analysis, and scientific computing. The repository demonstrates how to move beyond simple prompting to sophisticated agent-based workflows using rules, skills, MCPs (Model Context Protocol), and subagents.

**Repository:** https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Core Philosophy

Provide the right structure, rules, and tools so AI agents work autonomously and reliably on complex research tasks. The framework synchronizes AI configurations across IDEs (Cursor, VS Code, etc.) using structured directories for rules, agents, skills, and commands.

---

## Project Structure

### Key Directories

- **`.cursor/`** - Primary AI configuration for Cursor IDE
  - `rules/` - Mandatory rules for AI behavior (4 rule files)
  - `agents/` - Specialized subagents (literature-review)
  - `commands/` - Command shortcuts (git, airulez)
  - `skills/` - Workflow capabilities (scientific-writing)

- **`.claude/`** - Claude Code-specific configurations
  - `workflows/` - Workflow documentation for Claude Code
  - `skills/` - Claude-specific skills

- **`.agent/`** - Generic agent rules
  - `rules/` - Rule files for cross-IDE compatibility

- **`Data_analysis/`** - Example datasets and data analysis workflows
- **`Image_analysis/`** - 23 sample microscopy images for testing
- **`deep_stuff/`** - Miscellaneous content (e.g., rules of life)
- **`scripts/`** - Utility scripts (e.g., cursor-mdc-frontmatter.py)
- **`workflow.ipynb`** / **`workflow.py`** - Main workflow notebook (synced via jupytext)

### Important Files

- **`README.md`** - Complete framework documentation
- **`Resources.md`** - Links, resources, and recommendations
- **`.mcp.json`** - MCP server configuration (ai-rulez, github)

---

## Rules

Rules are non-negotiable guidelines that govern AI behavior. All rules are in `.cursor/rules/`:

### 1. `rules.mdc` (Priority: **critical**)

**Core expertise:**
- Data Analysis: Exploratory analysis, statistical analysis, data visualization
- Image Analysis: Microscopy image processing, segmentation, quantification
- Quantitative Analysis: Numerical computation, PDEs, ODEs, mathematical modeling
- AI Agents & MCPs: Model Context Protocol integration, agent workflows, context engineering

**Non-negotiable principles:**
- Provide concise, clear explanations
- Ask questions; don't make assumptions
- Prioritize readable, editable, reproducible, simple, modular code
- Write concise, technical responses

**Mandatory delegation to literature review workflow:**
When user asks ANY of these questions, IMMEDIATELY delegate:
- **Cursor IDE:** Use `@literature-review` agent
- **Claude Code:** Use `general-purpose` agent with literature review prompt (see Agents and Workflows section)

Trigger phrases:
- "How does [X] work" in biological/physical systems
- "What is [mechanism/process]" related to cell biology
- Requests for citations, literature references, or papers
- Questions about experimental findings or measurements
- Equations or mathematical models from literature
- Topics: cell adhesion, actomyosin, RhoA, E-cadherin, cortical flows, myosin
- ODEs/PDEs in biological modeling
- "What does the literature say about..."

**DO NOT answer from memory. ALWAYS delegate to literature review workflow.**

### 2. `python-coding-standards.mdc` (Priority: **high**)

**Core principles:**
- **Style**: Follow PEP 8
- **Execution**: Keep silent - minimize print statements
- **Performance**: Use vectorized operations (numpy/pandas) over loops
- **Functions**: Analysis returns data only; plots accept `ax` argument
- **Simplicity**: Write inline code for one-off logic; functions for reuse

**Critical rules:**
- ⚠️ **CRITICAL**: Edit `.py` files only, NOT `.ipynb` (notebooks sync via jupytext)
- **NEVER** create plots inside analysis functions
- **ALL** plot functions MUST accept `ax` argument
- Use matplotlib only (no seaborn)
- Save plots as SVG in `figures/` folder
- Use minimalist "science" style for plots

**Standard plotting setup:**
```python
import matplotlib.pyplot as plt
import minimalist

minimalist.use_style("science")
plt.rcParams.update({'figure.facecolor': 'none', 'axes.facecolor': 'none'})
text_width = 510/72.27  # LaTeX text width in inches
```

**Docstring format:**
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
```

### 3. `Image-analysis.mdc` (Priority: **high**)

**Always prioritize MCP tools over custom code:**
- MCPs are GPU-accelerated and tested
- Only write scripts when explicitly requested
- Use Python packages for tasks MCPs don't cover

**Cellpose MCP Tools:**

Segmentation:
```python
mcp__cellpose__segment_cells_2d({
    "image_path": "cells.tif",
    "model_type": "cyto3",  # or "nuclei", "cpsam"
    "diameter": 30  # 0 = auto-estimate
})
```

Models: `cyto`/`cyto2`/`cyto3` (general cells), `nuclei` (nuclei only), `cpsam` (most accurate)

Image restoration tools:
- `denoise_image` - Remove noise
- `deblur_image` - Restore blur
- `upsample_image` - Super-resolution
- `restore_and_segment` - Combined pipeline

**Python packages (when MCPs don't cover needs):**
- `scikit-image`: regionprops, gaussian, threshold_otsu, morphology operations
- `scipy.ndimage`: gaussian_filter, label
- `aicsimageio`: Read microscopy formats (ND2, CZI, etc.)

### 4. `project-repo.mdc` (Priority: **high**)

Quick reference for repository structure and navigation.

---

## Agents and Workflows

This repository supports both **Cursor IDE** (custom agents) and **Claude Code** (built-in agents + workflows).

### Cursor IDE Custom Agents

**Located:** `.cursor/agents/literature-review.md`

Cursor IDE uses custom agent definitions. The `literature-review` agent is a specialized subagent for Cursor that handles literature research tasks.

**For Cursor users only:** Invoke using `@literature-review` in Cursor IDE.

### Claude Code Built-in Agents

Claude Code has these built-in agent types (invoked via `Task` tool):
- **`general-purpose`** - Research, file searches, and multi-step tasks
- **`Explore`** - Fast codebase exploration (thoroughness: "quick", "medium", "very thorough")
- **`Plan`** - Software architecture and implementation planning
- **`Bash`** - Command execution specialist

**For Claude Code users:** You cannot create custom agent types. Instead, use the `general-purpose` agent with detailed prompts for specialized tasks.

### Literature Review Workflow for Claude Code

**Located:** `.claude/workflows/literature-review.md`

**Purpose:** Expert literature research using Claude Code's `general-purpose` agent

**When to invoke:** IMMEDIATELY and PROACTIVELY when user asks about:
1. Mechanisms or findings from papers
2. Citations or literature references
3. "How does X work" in biological/physical systems
4. Experimental methods or measurements
5. Equations or mathematical models from literature
6. Topics: cell adhesion, actomyosin, RhoA, E-cadherin, cortical flows
7. ODEs/PDEs in biology
8. "What does the literature say about..."

**DO NOT answer from memory. ALWAYS delegate to the general-purpose agent.**

**Delegation format:**
```python
Task(
  subagent_type="general-purpose",
  description="Literature search",
  prompt="""You are an expert literature research specialist in theoretical physics,
            experimental biophysics, bioengineering and computational biology.

            Search for information about: [USER'S QUESTION]

            Follow this systematic search strategy:
            1. Search local literature in 'literature/' folder using Grep and Read
            2. Search project documentation (Notes.md, module docs)
            3. If available, search Zotero library using MCP tools
            4. Use web search for recent papers or to fill gaps

            Structure your answer as:
            1. Direct Answer - Clear, concise response
            2. Detailed Explanation - Biological/physical context
            3. Evidence from Literature - Specific findings with citations
            4. Cross-Paper Synthesis - How sources relate/differ
            5. Key Equations/Methods - Mathematical expressions
            6. Further Reading - Specific files or papers

            Citation format:
            - In-text: Author et al. (Year) found that...
            - With title: Arslan et al. (2024) "Adhesion-induced..."
            - File ref: See literature/Arslan et al. - 2024 - ...md
            - Quotes: > "Quote text" - Author et al. (Year)

            Quality: Comprehensive, specific, critical, contextual, precise"""
)
```

**Search strategy:**
1. Parse query for key concepts
2. Search local literature (`literature/` folder) using Grep
3. Search project documentation (Notes.md, module docs)
4. Search Zotero library (if MCP configured)
5. Web search if gaps remain

**Output format:**
1. Direct Answer
2. Detailed Explanation (biological/physical context)
3. Evidence from Literature (with citations)
4. Cross-Paper Synthesis
5. Key Equations/Methods
6. Further Reading

**See `.claude/workflows/literature-review.md` for complete documentation.**

---

## Commands

Commands are shortcuts for common workflows. Invoke using `/command-name`.

### /git - Complete GitHub Workflow

**Located:** `.cursor/commands/git.md`

**Usage:**
- `/git quick` - Quick commit and push for small updates
- `/git new feature: description` - Detailed workflow with proposed commit message
- `/git` - Agent decides based on last commit date and change size

**Quick workflow:** (small updates within 2 days)
1. Pull first and show remote changes
2. Stage all changes: `git add .`
3. Commit with short message (timestamp or user-provided text)
4. Show what will be pushed, then push

**Detailed workflow:** (significant changes)
1. Pull first and show remote changes
2. Run `git status` and `git diff`
3. Propose commit message (conventional commits style)
4. Ask user to confirm or edit
5. Stage, commit, show changes, then push

**Standard practices:**
- Always pull before pushing
- Use conventional commits: `feat:`, `fix:`, `docs:`, `chore:`
- Show incoming/outgoing changes before push
- Never commit sensitive files

---

## Skills

Skills provide workflow-specific capabilities tuned to research domains.

### scientific-writing

**Located:** `.cursor/skills/scientific-writing/`

**Purpose:** Creates concise, structured scientific documents with LaTeX equations, integrated figures, and clear technical writing

---

## MCP Servers

Model Context Protocol servers provide specialized capabilities. Configured in `.mcp.json`:

### Available MCPs

| MCP | Capabilities |
|-----|--------------|
| `napari-mcp` | Interactive image visualization and analysis |
| `cellpose-mcp` | Cell segmentation and quantification |
| `github` | GitHub operations (configured in .mcp.json) |
| `ai-rulez` | AI governance tool (configured in .mcp.json) |

### Other MCPs (referenced in rules)

- `fmcp` - Mathematical plotting (matplotlib, numpy, sympy)
- `sympy-mcp` - Symbolic mathematics and calculus
- `zotero-mcp` - Zotero library access for literature management
- `data-forge` - Data manipulation and analysis
- `notion-mcp` - Notion workspace integration

---

## Development Workflow

### Working with Jupyter Notebooks

This repo uses **jupytext** to sync `.ipynb` and `.py` files.

**CRITICAL:** Always edit the `.py` file, NEVER edit the `.ipynb` file directly.

The `.py` file uses percent format with cell markers:
```python
# %% [markdown]
# ## Section Title

# %%
# Code cell
data = pd.read_csv('data.csv')
```

Notebooks sync automatically when you open the `.ipynb` file.

### Data Analysis Workflow

1. Use pandas, numpy, scipy for analysis
2. Analysis functions return data only (no plots)
3. Plot functions accept `ax` argument
4. Save results as CSV, plots as SVG in `figures/`
5. Use vectorized operations (avoid loops)
6. Silent execution (minimal print statements)

### Image Analysis Workflow

1. **Prefer MCP tools:** Use cellpose-mcp for segmentation
2. **Validate results:** Use napari-mcp for interactive visualization
3. **Extract metrics:** Use scikit-image for quantification (regionprops)
4. **Document steps:** Save intermediate results and parameters
5. **Custom code only when needed:** Write scripts only if MCPs don't cover the task

### Mathematical Modeling Workflow

1. Use sympy-mcp for symbolic mathematics
2. Generate LaTeX equations for documentation
3. Solve systems symbolically before numerical implementation
4. Use vectorized operations for performance
5. Save equations and derivations in project documentation

---

## Common Tasks

### Running Tests

No test framework is currently configured in this repository.

### Committing Changes

Use `/git` command for guided commit workflow (see Commands section).

### Updating AI Rules

**NOTE:** The ai-rulez system has been removed. To update rules:

1. Edit files in `.cursor/rules/`, `.cursor/agents/`, `.cursor/commands/`, or `.cursor/skills/`
2. Run `python scripts/cursor-mdc-frontmatter.py` to update frontmatter
3. Commit changes with descriptive message

### Adding New Configuration

- **Rules:** Add `.mdc` file to `.cursor/rules/`
- **Agents:** Add `.md` file to `.cursor/agents/`
- **Commands:** Add `.md` file to `.cursor/commands/`
- **Skills:** Add directory with `SKILL.md` to `.cursor/skills/`

---

## Important Notes

1. **Notebook editing:** ALWAYS edit `.py` files, not `.ipynb` files
2. **Literature queries:** ALWAYS delegate to literature review workflow:
   - Cursor: Use `@literature-review` agent
   - Claude Code: Use `general-purpose` agent with literature prompt
3. **Image analysis:** Prefer MCP tools over custom implementations
4. **Plotting:** Analysis functions never create plots; plot functions accept `ax` argument
5. **Execution:** Keep code silent - minimize print statements
6. **Git workflow:** Always pull before pushing, show changes before committing
7. **Agents:** Cursor supports custom agents; Claude Code uses built-in agents only

---

## Additional Resources

See `Resources.md` for:
- Cursor documentation and tutorials
- Model Context Protocol information
- MCP server directory
- Cursor rules examples
- Free student resources for AI tools

---

## Contact

**Author:** Suraj Kumar Sahu
**GitHub:** [@surajinacademia](https://github.com/surajinacademia)
**Email:** ssahu2@ucmerced.edu
**Affiliation:** University of California, Merced

**License:** MIT License - Free for use, modification, and distribution with attribution
