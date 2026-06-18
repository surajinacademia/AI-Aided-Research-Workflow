---
name: "figure-generation"
description: "Generate, update, and modify publication figures for the multicellular compaction project. Handles jupytext .py/.ipynb pairing, minimalist science style, LaTeX sizing, SVG output, and compaction_analysis/compaction_plotting imports. Use when: editing figure scripts, adding panels, fixing axes/colors/legends, styling error bars, saving figures, or creating new figure scripts."
---

# Figure Generation

## Critical Rules

- **Edit `.py` only, never `.ipynb`** — jupytext syncs from `.py`. Scripts: `scripts/fig*.py` (and `scripts/SI/` for supplementary); cells `# %%` / `# %% [markdown]`, 5 blank lines between cells.
- **Separation of concerns**: Analysis returns data only (arrays/DataFrames), no `plt`. Plot functions take `ax` and only draw; they never load data or do heavy analysis.
- **API shape**: High-level plots are `plot_*(ax, dataframes..., base_params, **options)`; they never create `fig, ax`. Caller owns `fig, ax = plt.subplots(...)`, `plt.savefig(...)`, then `plt.show()`.

## Setup Block

After imports in every figure script (`__file__` is the script under `scripts/`):

```python
import os, sys
import matplotlib.pyplot as plt
import minimalist

minimalist.use_style("science")
plt.rcParams.update({'figure.facecolor': 'none', 'axes.facecolor': 'none', 'savefig.facecolor': 'none'})
text_width = 510 / 72.27
fw, fw_2, fw_3, fw_4 = text_width, 0.5 * text_width, 0.33 * text_width, 0.25 * text_width
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(repo_root, 'scripts', 'src'))
data_dir = os.path.join(repo_root, 'results')
sim_data_dir = os.path.join(data_dir, 'data', 'simulation', 'simulation_analysis')
sim_frames_dir = os.path.join(data_dir, 'data', 'simulation', 'sim_frames')
exp_data_dir = os.path.join(data_dir, 'data', 'experiment')
plot_dir = os.path.join(data_dir, 'plots', 'publication')
```

## Style (single source of truth)

- **Sizing**: `fw`–`fw_4` from setup; default aspect square; `minimalist.figsize(fraction, aspect_ratio=)` for non-square.
- **Colors**: `colors` from setup (warm→cool palette). Colormaps: `pride`, `inferno`, `minimalist`. See [STYLE.md](references/STYLE.md).
- **Error bars**: marker + vertical line + caps; **no filled bands**.
- **Legends**: `ax.legend(labelcolor="linecolor")` then `minimalist.color_legend_text(ax)`.
- **Layout**: `constrained_layout=True`; never `tight_layout()`. Axes limits/ticks encode physics (e.g. fixed cell-gap ranges for compaction); equal aspect for network/spatial plots.

## Modules & data

```python
from compaction_analysis import load_arrow_data, compaction_fit, compaction_derivative
from compaction_plotting import draw_matrix, draw_cell_edges, draw_cell_nodes, draw_alpha_shape_and_compaction, plot_network
```

- Data: `.arrow` → `load_arrow_data(path)`; processed → `pd.read_csv(path)`.
- `draw_matrix(df, ax, df_initial=None, traction=None, linewidth=0.5)` — `traction=(lambda_m, cell_size)` for orange edges.
- `plot_network(df, ax, box_size, style="matrix_network", initial_df=None, traction=None, alpha_shape=1.0)`.

## Saving

```python
plt.savefig(os.path.join(plot_dir, 'fig_X_panel_name.svg'), bbox_inches='tight')
plt.show()
```

SVG by default; `savefig` before `show()`.

## References

- [figure-scripts-map.md](references/figure-scripts-map.md) — panels, data sources, output paths
- [STYLE.md](references/STYLE.md) — typography, color system, colormaps, LaTeX
