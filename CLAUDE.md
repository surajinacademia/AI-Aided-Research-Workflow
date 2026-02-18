# Project Rules

## Agent Expertise
- Data analysis, image analysis, quantitative modeling, AI agents & MCPs

## Core Principles
- Test ALL code before responding (debug until working)
- Style: readable, modular, reproducible, simple
- Save: results → CSV, plots → SVG
- Concise, technical responses
- Ask questions > make assumptions
- Explain when necessary, code when sufficient

## Image Analysis
- **Use MCP tools first** (Cellpose MCP, napari-mcp) → custom code only if insufficient
- MCPs are GPU-accelerated and tested — only write scripts when explicitly requested
- Extract quantitative metrics + visual validation
- Models: `cyto`/`cyto2`/`cyto3` (general cells), `nuclei` (nuclei only), `cpsam` (most accurate)
- Key params: `model_type`, `diameter`, `flow_threshold`, `cellprob_threshold`, `channels`
- Restoration: `denoise_image`, `deblur_image`, `upsample_image`, `restore_and_segment`
- Utilities: `estimate_cell_diameter`, `load_image_info`, `segment_cells_batch`, `list_available_models`
- Python fallback: scikit-image (`regionprops`, filters, morphology), scipy.ndimage

## Data Analysis
- Stack: pandas, numpy, scipy, matplotlib
- Workflow: EDA → statistical analysis → visualization
- Document analysis steps

## Mathematical Modeling
- Tools: sympy-mcp (symbolic math), fmcp (mathematical plotting)
- Workflow: solve symbolically → LaTeX documentation → vectorized numerical implementation

## Python Coding Standards
- Follow PEP 8
- Silent execution (minimize print statements)
- Use vectorized operations (numpy/pandas) over loops
- Analysis functions return data only — no plots inside
- Plot functions accept `ax` argument
- Matplotlib only (no seaborn), save as SVG in `figures/`
- Jupyter: edit `.py` files only, NOT `.ipynb` — notebooks sync via jupytext
- Jupyter cells: use `# %%` markers, 5-line spacing between cells
- Inline logic for one-off operations; functions only for reuse
- Docstrings: simple format with Parameters and Returns

## Project Structure
- `Data_analysis/` — datasets and data analysis workflows
- `Image_analysis/` — sample microscopy images for testing
- `deep_stuff/` — miscellaneous (rules of life, etc.)
- `workflow.ipynb` — workflow notebook
