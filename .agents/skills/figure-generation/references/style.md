## Minimalist Science Style

Publication-ready Matplotlib style: custom warm–cool palette, square layouts, LaTeX-compatible sizing.

### Core Principles

- Minimal clutter: thin axes, inward ticks, no grid, frameless legends.
- Sizes from LaTeX text width (510 pt); consistent color system across line/scatter/heatmap.

### Typography

- **Main font**: `CMU Sans Serif` for all text.
- **Math text**: Computer Modern via Matplotlib’s `mathtext` (no LaTeX engine required).
- **Colors and sizes**:
  - Text color: **black**
  - **Base font size** (body text): **10 pt**
  - **Axis labels** (`axes.labelsize`): **12 pt**
  - **Tick labels** (`xtick.labelsize`, `ytick.labelsize`): **10 pt**
  - **Legend text** (`legend.fontsize`, `legend.title_fontsize`): **10 pt**
- **Unicode minus disabled** (`axes.unicode_minus: False`) to avoid missing glyphs with this font.

### Geometry & Figure Sizing

- Text width: 510 pt ≈ 7.06". Width constants: `FW` (full), `FW_2` (half), `FW_3` (third), `FW_4` (quarter). Default aspect square; vector export (PDF/SVG).

### Legends & Utilities

- Frameless legend; `ax.legend(labelcolor="linecolor")` or `minimalist.color_legend_text(ax)` to match line colors.  
- `remove_all_clipping(fig)` to allow artists to extend beyond axes.


### LaTeX Integration

- Two-column: e.g. 6.75" text width, 3.25" column. Use `\columnwidth` or `\textwidth` in `\includegraphics`. In Python, match with `figsize=(3.25, 3.25)` (single column) or `minimalist.figsize(6.75/7.06, aspect_ratio=0.5)` (wide).

### Axes & Ticks

- **Spines**: All four visible; linewidth 0.65; facecolor none. **Ticks**: inward, majors only, 10 pt labels, black.

### Color System

- **Qualitative** (`axes.prop_cycle` / `BASE_COLORS`): `#AB3019`, `#FE7002`, `#F4B43E`, `#86B4C4`, `#00768C`, `#003547` (warm→cool). Use for lines, scatter, legends (~6 series).
- **Colormaps**: diverging `pride` (default), sequential `inferno`, continuous `minimalist`/`minimalist_r` from `BASE_COLORS`. API: `minimalist.get_cmap('diverging'|'sequential'|'qualitative')`.



