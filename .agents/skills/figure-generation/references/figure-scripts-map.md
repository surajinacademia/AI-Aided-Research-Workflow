# Figure Scripts Map

## fig1_model.py

**Purpose**: Model description figures — network visualizations, force curves, penalty energy diagrams.

**Output directory**: `results/plots/publication/`

| Panel | Output file | Description |
|-------|-------------|-------------|
| 1a | `fig_1a_matrix_network.svg` | Matrix fiber network (circular gel) |
| 1a | `fig_1a_cell_network.svg` | Cell-cell contractile network only |
| 1a | `fig_1a_cell_matrix_network.svg` | Combined cell + matrix network |
| 1b | `fig_1b_matrix_interaction.svg` | Matrix fiber force-extension curve (buckle vs. linear) |
| 1c | `fig_1c_cell_force.svg` | Cell-cell contractile force vs. distance |
| SI | `SI_1_fiber_length_histogram.svg` | Matrix coordination number + fiber length distributions |
| SI | `SI_1_cell_coordination_number_histogram.svg` | Cell degree + cell-cell distance distributions |
| SI | `SI_1_penalty_energy_and_total_energy.svg` | Penalty energy vs. triangle orientation J |
| SI | `SI_two_cell_comparison.png` | Two-cell system comparison across matrix variants |
| SI | `SI_two_cell_traction_comparison.svg` | Two-cell traction comparison (with/without connection) |

**Key data sources**:
- Single-frame `.arrow` files from `sim_frames/cell_matrix_network_model/`
- Two-cell comparison frames from `sim_frames/two_cell/matrix_properties/` and `sim_frames/two_cell/traction/`

**Key functions used**: `draw_matrix`, `draw_cell_edges`, `draw_cell_nodes`, `draw_alpha_shape_and_compaction`, `load_arrow_data` (from compaction_plotting and compaction_analysis)

---

## fig2_compaction_transition.py

**Purpose**: Compaction transition figures — compaction vs. cell gap, percolation probability, comparison with Doha et al. (2022) experiment.

**Output directory**: `results/plots/`

**Key data sources**:
- `simulation_analysis/compaction_analysis.csv` → loaded via `calculate_compaction(pd.read_csv(...))`
- `simulation_analysis/cell_percolation_analysis.csv`
- `data/experiment/exp_comp_vs_cellgap.csv`

**Key functions used**: `calculate_compaction`, `compaction_cell_gap_fit`, `compaction_vs_cell_gap`, `compaction_vs_cell_gap_exp`, `compute_derivative`, `fit_compaction_tanh`

---

## Adding a New Figure Script

Use SKILL.md setup block and conventions. Copy header + setup from an existing `fig*.py`; name outputs `fig_X_panel_description.svg` in `results/plots/publication/`.
