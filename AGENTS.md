# Project Manual

This is the Codex project instruction file. Keep repository guidance here and keep project skills under `.agents/skills/`.

## Agent Scope

- Work on AI-aided research workflows, data analysis, image analysis, quantitative modeling, agents, and MCPs.
- Keep responses concise and technical.
- Ask questions when a scientific or analysis assumption is ambiguous.
- Verify code before handing back results; debug until the requested workflow runs.

## Core Rules

- Keep code readable, modular, reproducible, and simple.
- Save tabular results as CSV or another structured format.
- Save publication-style figures to `figures/` as SVG unless raster output is explicitly required.
- Treat model parameters, thresholds, metadata, and random seeds as explicit, documented inputs.
- Do not add or maintain provider-specific rule files. This repository uses `AGENTS.md` plus `.agents/skills/`.

## Project Structure

| Path | Role |
| --- | --- |
| `data_analysis/` | Data analysis scripts, reports, and derived metrics |
| `Image_analysis/` | Sample microscopy images and image-analysis workflows |
| `Resources/` | Workflow resources and reference notes |
| `workflow.py` / `workflow.ipynb` | Main paired workflow notebook |
| `figures/` | Figure outputs |
| `.agents/skills/` | Codex project skills |

## Python Standards

- Follow PEP 8.
- Prefer vectorized NumPy/Pandas operations over loops.
- Keep execution quiet; avoid progress prints unless requested.
- Use functions for reusable logic and inline code for one-off transformations.
- Analysis functions return data only. Do not create plots inside analysis functions.
- Plotting functions accept an `ax` argument and return the axis.
- Use matplotlib for plots unless another library is required.
- File order: imports, configuration, functions, execution.
- Use docstrings with `Parameters` and `Returns` for public or reusable functions.

## Notebooks

- Edit the paired `.py` file with `# %%` cells, not raw `.ipynb`, unless there is a one-off reason.
- Keep cells readable and avoid noisy output.
- If an executed notebook changes, make sure the paired script still reflects the workflow.

## Data Analysis

- Default stack: pandas, numpy, scipy, matplotlib.
- Workflow: inspect data, clean data, analyze statistically, visualize, and save outputs.
- Use method chaining where it improves readability.
- Document enough steps that another researcher can reproduce the analysis.

## Image Analysis

- Prefer Cellpose MCP and napari MCP when available for segmentation and inspection.
- Use custom Python only when MCP tools do not cover the task or the user asks for code.
- For custom measurements, prefer scikit-image and scipy.ndimage.
- Always provide quantitative outputs and visual validation for segmentation workflows.

## Julia Standards

- Follow the Julia style guide and local conventions.
- Use `const` for globals that must not change.
- Avoid untyped globals in hot loops.
- Keep performance-critical code type-stable.
- Preallocate or broadcast where it avoids repeated allocation.
- Keep plotting separate from numerical routines.
- Pin `Project.toml` / `Manifest.toml` for reproducible Julia analyses when relevant.

## Skills

Project skills live under `.agents/skills/`:

| Skill | Purpose |
| --- | --- |
| `data-analysis` | Pandas-oriented analysis workflows |
| `deslop` | Tighten prose and remove filler |
| `figure-generation` | Figure style and script conventions |
| `scientific-artist` | Scientific schematic generation |
| `scientific-writing` | Scientific documents, equations, and captions |
| `skill-creator` | Authoring and packaging skills |

## MCPs

See `README.md` for the MCP table. Prefer enabled MCP tools for image analysis, symbolic math, plotting, and reference management when they fit the task.
