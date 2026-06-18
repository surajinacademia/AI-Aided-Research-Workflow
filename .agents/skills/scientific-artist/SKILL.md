---
name: "scientific-artist"
description: "Generate scientifically accurate visual output from descriptions of scientific concepts or models. Use for sketches, figures, schematics, diagrams, publication graphics, Excalidraw drafts, Matplotlib figures, or TikZ output."
---

# Scientific Artist

Generate scientifically accurate visual output from a description of a scientific concept or model.

## Workflow

1. Read the user's description. Identify: equations, variables, spatial relationships, physical processes.
2. Ask which tool stage to use (or infer from context — see selection table below).
3. At publishing stage, disambiguate Matplotlib Advanced vs. TikZ if unclear.
4. Generate output following the accuracy and style rules below.
5. Present output for user feedback; iterate.

## Tool selection

| User signal | Stage | Tool |
|-------------|-------|------|
| "sketch", "draft", "quick diagram", "for a talk" | Drafting | Excalidraw MCP |
| "figure", "prototype", "next to my code", "iterate" | Prototyping | Matplotlib |
| "paper", "journal", "publication", "submit" | Publishing | Matplotlib Advanced **or** TikZ — ask if unclear |
| Ambiguous | — | Ask the user |

## Scientific accuracy rules

These are non-negotiable across all stages:

- All labels and annotations use LaTeX math symbols.
- Model parameters are named constants at the top of the script, never magic numbers.
- Equations must match the actual model: correct variable names, subscripts, operator precedence.
- Arrow directions and spatial layout reflect physical meaning (gradients toward sources, torque arcs show rotation, sensing radii to scale).
- At publication stage: parameters from simulation output, not hardcoded.

## Stage-specific guidance

### Excalidraw (drafting)

Use the Excalidraw MCP tools (`create_view`, `save_checkpoint`). Call `read_me` before first use.

- Correct topology: right components connected to right components.
- Proper variable names on all labels (e.g., "Cell i", not "Cell 1").
- Physically meaningful spatial arrangement from the start.
- No equations required, but variable names must be correct.
- See `references/excalidraw-patterns.md` for MCP usage and layout conventions.

### Matplotlib (prototyping)

- Enable full LaTeX: `matplotlib.rcParams['text.usetex'] = True` and `font.family = 'serif'`.
- Parameters as named constants at script top.
- Plot functions accept `ax` argument (project convention).
- Save as PDF/SVG to `figures/` or `outputs/`.
- See `references/matplotlib-patterns.md` for style patterns and helpers.

### Matplotlib Advanced (publishing — Python pipeline)

- GridSpec multi-panel layouts with labeled panels (A, B, C...).
- Simulation-coupled panels: run real physics to generate data (Bessel functions, Monte Carlo, phase diagrams).
- Comparison tables via FancyBboxPatch.
- `panel_bg` helper for consistent panel styling.
- See `references/matplotlib-advanced-patterns.md` for multi-panel and simulation patterns.

### TikZ (publishing — LaTeX)

- Native LaTeX math via amsmath/amssymb.
- Reusable `\tikzset` styles for cells, boxes, arrows.
- Relative positioning via TikZ libraries.
- Compile with `pdflatex` for vector PDF.
- See `references/tikz-patterns.md` for style definitions and patterns.

## Examples

Working examples in `examples/`:

| File | What it demonstrates |
|------|---------------------|
| `schematic-matplotlib.py` | Single-panel schematic with LaTeX math, named parameters, color palette |
| `schematic-advanced-matplotlib.py` | 6-panel simulation-coupled figure: K0 field, 2D heatmap, sine torque, heading update, Monte Carlo, phase diagram, comparison table |
| `chemoattraction-model-plan.md` | Example "plan" input — the physics document that drove the advanced figure |
| `schematic-tikz.tex` | Publication-ready TikZ schematic with reusable styles |
