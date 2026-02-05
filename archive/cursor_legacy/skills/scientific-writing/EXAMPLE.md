# Viscoelastic Response of Adherent Cells to Substrate Stiffness

## Summary

We measured mechanical properties of fibroblasts on substrates with stiffness ranging from 1 to 100 kPa using atomic force microscopy (AFM). Cell stiffness increased 3.2-fold across this range, with a sharp transition at 10 kPa. The timescale of viscoelastic relaxation decreased from 45 s on soft substrates to 12 s on stiff substrates, indicating mechanoadaptation through cytoskeletal reorganization.

## Methods

Cells were cultured on polyacrylamide gels with controlled stiffness (1, 10, 100 kPa, measured by AFM calibration). After 24 h, we performed force-indentation measurements using a spherical probe (R = 5 μm) at constant velocity (1 μm/s). Force-relaxation curves were fit to:

$$
\begin{equation}
F(t) = F_0 + F_1 e^{-t/\tau}
\end{equation}
$$

where $\tau$ is the characteristic relaxation time.

## Results

### Substrate Stiffness Modulates Cell Mechanics

Cell stiffness, quantified by the apparent Young's modulus $E_{\text{cell}}$, increased from 2.3 ± 0.3 kPa on soft substrates to 7.4 ± 0.9 kPa on stiff substrates (Figure 1A). The transition occurred sharply between 1 and 10 kPa, suggesting a threshold response.

![Cell stiffness vs substrate stiffness](figures/stiffness_correlation.svg)
**Figure 1.** Mechanosensitive stiffening of adherent fibroblasts. **(A)** Cell stiffness increases 3.2-fold from soft to stiff substrates, with sharp transition at 10 kPa (n = 45 cells per condition). **(B)** Relaxation time decreases with substrate stiffness, indicating faster stress relaxation on stiff substrates.

### Viscoelastic Relaxation Accelerates on Stiff Substrates

Relaxation time $\tau$ decreased from 45 ± 8 s (soft) to 12 ± 3 s (stiff), a 3.8-fold reduction (Figure 1B, p < 0.001). This indicates cells on stiff substrates reorganize cytoskeletal elements more rapidly under load.

### Cytoskeletal Disruption Eliminates Stiffness Dependence

Treatment with 1 μM latrunculin A (actin depolymerization) reduced $E_{\text{cell}}$ to 0.8 ± 0.2 kPa across all substrate stiffnesses (Figure 2), confirming that mechanoadaptation requires intact actin cytoskeleton.

![Effect of cytoskeletal disruption](figures/latrunculin_treatment.svg)
**Figure 2.** Actin depolymerization abolishes mechanosensitive stiffening. Latrunculin A treatment reduces cell stiffness to uniform baseline across all substrate conditions (gray bars, n = 30 cells per condition, ***p < 0.001).

## Discussion

Fibroblasts exhibit substrate stiffness-dependent mechanical properties with a sharp transition near 10 kPa, matching physiological tissue stiffness ranges. The coupled increase in stiffness and decrease in relaxation time suggests active cytoskeletal reinforcement. Future work should examine focal adhesion dynamics and RhoA signaling during this transition to identify molecular mechanisms.

## References

1. Discher et al. (2005) Science 310: 1139-1143
2. Yeung et al. (2005) Cell Motil. Cytoskeleton 60: 24-34
