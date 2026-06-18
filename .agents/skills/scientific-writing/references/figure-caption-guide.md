# Figure Caption Best Practices

A guide to writing clear, well-structured figure captions, based on analysis of published examples—including those in Dallon et al. (2014), Arruda et al. (Sci. Adv.), Peng et al. (2025), and detailed captions from contemporary biophysics papers such as Zakharov et al. (2021) found in `examples/Zakharov et al. - 2021 - Clots reveal anomalous elastic.md`. These references demonstrate conventions for multi-panel description, quantitative detail, and effective scientific communication in figure captions.


## Anatomy of a Good Caption

Every caption follows the same skeleton:

| Component | What it does | Example |
|-----------|-------------|---------|
| **Title sentence** | Describes *what* the figure shows (not conclusions) | "Active network model of plasma clots" |
| **Panel descriptions** | Systematic (A), (B), (C) walk-through, 1-2 sentences each | "(A) Microscopic image of PRP clot and a clot approximation by a 2D elastic network model..." |
| **Visual encoding** | Map symbols/colors/lines to data | "squares indicate experimental values, solid line indicates simulations" |
| **Scale & units** | Scale bars, axis units | "Scale bars, 10 um (5 um for insets)" |
| **Parameters** | Collected in one block at end | "Parameter values: E^f/E^b = 50, lambda_c = 1.04, alpha = 2.4 kPa^-1" |
| **Sample sizes** | Replicates, donors, runs | "n = 50 simulations per data point", "four donors" |


## Six Principles

1. **Title = What, not Why.** Describe the figure's content, not its interpretation.
   - Good: "Compaction and percolation probability as a function of cell gap"
   - Bad: "Sharp transition in compaction is due to percolation phase transition"

2. **Describe, don't interpret.** The caption says what is plotted and what the reader should see. Mechanistic arguments go in the main text.
   - Good: "At small cell gap (d = 5.0 sigma), cells form a system-spanning network and the gel compacts by ~80%."
   - Bad: "cells form percolating network that transfer contractile forces throughout the matrix from one end to the other and drive substantial gel compaction"

3. **Uniform panel coverage.** Each panel gets similar depth of treatment. Don't write a paragraph for (b) and a clause for (d).

4. **Self-contained.** A reader scanning figures should understand the plot without reading the paper. Define symbols, identify data sources, specify what curves represent.

5. **Parameters at the end.** Collect all parameter values into a single sentence or block at the caption's end. Don't scatter them throughout panel descriptions.

6. **Concise.** Each sentence serves exactly one purpose. No run-on descriptions. No redundancy. A good caption for a 4-panel figure is typically 5-8 sentences.


## Deconstructed Examples

### Peng et al. (2025), Fig. 2 — Strong example

> **Critical spacing threshold governs collective cell behavior and tissue condensation.** (A) Experimental data from Doha et al. revealing a sharp phase transition in tissue compaction when cell spacing falls below the critical threshold of 79 to 160 um. (B and C) Our model predictions (red lines) accurately capture this threshold behavior, with cell spacing normalized by nominal radius (10 um). The transition corresponds precisely to the distance at which myosin motor polarization dramatically increases, while motor density remains relatively constant. (D) Mechanistic basis: cells below critical spacing generate overlapping zones of strain-stiffened ECM, creating tension bands that enable mechanical communication. (E) Quantification of ECM fiber alignment shows dramatic reduction with increased cell spacing. Parameter values: E^f/E^b = 50, lambda_c = 1.04, alpha = 2.4 kPa^-1, beta = 2.5 kPa^-1, rho_0 = 1 kPa, K = 0.833 kPa, mu = 0.385 kPa.

**What makes it work:**
- Title is descriptive but carries the main message
- Each panel described in order with consistent depth
- Parameters collected in final sentence
- Quantitative where needed (79-160 um threshold)

### Arruda et al. (Sci. Adv.), Fig. 2 — Strong example

> **Effect of fibrin cross-linking on shear stiffness regimes of passive PPP clots.** (A) Microscopy images of cross-linked (PPP) and uncross-linked (PPP + T101) clots. Scale bars, 10 um (5 um for insets). (B) Schematic of bent fibrin fiber showing protofibril structure. (C) Shear modulus of cross-linked and uncross-linked clots show a highly nonlinear dependence on applied stress in both experiments (squares, four donors) and simulations (lines). (D) Increasing the average coordination number leads to higher shear moduli and reduces the critical strain at which the network transitions to a stiffer regime.

**What makes it work:**
- Title names the independent variable (cross-linking) and the dependent variable (shear stiffness)
- Visual encodings explicit: "squares" = experiments, "lines" = simulations
- Scale bars stated
- Sample size: "four donors"


## Bad Example: 
**Sharp Transition in Collagen gel compaction as a function of cell gap is due to percolation phase transition in fibroblast multicellular network.** a) Simulation snapshots for three different starting cell densities, cell gaps($d/\sigma$) showing initial (top) and final (bottom) configurations. (b) Compaction $\phi = 1 - A_f/A_0$ versus cell gap $d/\sigma$ comparing experiment(red, n = 6), simulation (orange, n = 5). At large cell gap ($d/\sigma = 12.0$), cells remain isolated resulting in negligible compaction gel compaction. At intermediate gap ($d = 8.0\sigma$) close to the maximum distance within with the cells can form cell-cell connection in our simulation $\lambda_c = 8.0\sigma$, cells show formation  multicellular networks though not system spanning, that upon contraction cause slight compaction of the gel. At small cell gap ($d = 5.0\sigma$), cells form percolating network that transfer contrtile forces trhoguhout the matrix from one end to the other and drive substantial gel compaction reductin gel size almost 80%. This is further validated by plotting the derivatives of compaction and percolation probability in (d) showing that compaction transition conicides with with the percolation threshold. (c) Varying the connection length $\lambda_c$ systematically shifts the critical cell gap for compaction transition as upon rescaling by $\lambda_c$ confirms that the transition is controlled by the dimensionless ratio $d/\lambda_c$, characteristic of percolation transtion threhold in the cell network. Initial disk radius $R_0 = 50 \sigma$ in simulation. Matrix fiber stiffness is $k_{gel} = 1$ and active contractile force for cell connection with $k_{cell} = k_{gel}$. Experiment done with 3T3 fibroblasts in 2 mg/ml collagen gels with disk radius $1 mm$ and thickness $500 \mu m$. As experimental 3D densities differ from 2D densities, we take cell gap parameter to compare simulation and experiment, as the length scale reflects key mechanobiological properties long range cell-cell communication in cell-ECM system.

The current caption has these issues:

| Problem | Example from current caption |
|---------|-----|
| **Title argues a conclusion** | "Sharp Transition in Collagen gel compaction... is due to percolation phase transition" |
| **Interpretation mixed with description** | "cells form percolating network that transfer contractile forces throughout the matrix from one end to the other" |
| **Uneven panel coverage** | (a) gets 1 clause; (b) gets a full paragraph with 3 mechanistic scenarios; (d) is buried inside (b) |
| **Parameters scattered** | R_0, k_gel, k_cell, sigma appear mid-sentence in different locations |
| **Typos** | "contrtile", "trhoguhout", "reductin", "conicides", "threhold" |
| **Experimental methods in caption** | "3T3 fibroblasts in 2 mg/ml collagen gels with disk radius 1 mm and thickness 500 um" belongs in Methods |
| **Too long** | Reads like a results paragraph, not a figure description |


## Rewritten Fig. 2 Caption

> **Compaction transition in cell-matrix networks coincides with percolation threshold.** (a) Simulation snapshots showing initial (top) and final (bottom) configurations at three cell gaps: $d = 12.0\sigma$ (isolated cells, no compaction), $d = 8.0\sigma$ (partial network, slight compaction), and $d = 5.0\sigma$ (percolating network, $\sim$80\% compaction). (b) Compaction $\phi = 1 - A/A_0$ versus cell gap $d/\sigma$ for experiment (red, $n = 6$) and simulation (orange, $n = 5$), with percolation probability $P(d)$ (gray, right axis). Solid curves are hyperbolic tangent fits. Star marks the critical cell gap. (c) Varying the connection length $\lambda_c$ shifts the compaction curve; rescaling by $\lambda_c$ (inset) collapses the data, confirming the transition is controlled by $d/\lambda_c$. Shaded region marks $d < \lambda_c$. (d) Derivatives of compaction $-\mathrm{d}\phi/\mathrm{d}(d/\sigma)$ and percolation probability $-\mathrm{d}P/\mathrm{d}(d/\sigma)$ both peak at the same critical cell gap. Simulation parameters: $R_0 = 50\sigma$, $k_{\text{gel}} = 1.0$, $k_{\text{cell}} = 1.0$, $z = 3.9$, non-crossing topology. Experimental data corresponds to measured compaction of gel after 72 hrs from initial setting~\cite{Doha2022}.
