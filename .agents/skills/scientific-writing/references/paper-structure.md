# Paper Structure and Paragraph Templates

Effective patterns for scientific writing in computational biophysics, arranged by structural level.


## Manuscript Structure

- Introduction — broad context, problem statement, summary of findings
- Model / Theory
- Methods / Simulation Details
- Results (often merged with Discussion)
- Conclusion / Summary
- Appendix
- Supplemental Material


## Section Content Guide

**Abstract**: Single flowing paragraph, ~150 words (PRL) or ~250 words (PRE). No citations, no labeled subsections. State problem, approach, key result, and significance.

**Introduction**: Broad context → specific problem → gap in understanding → our approach → summary of key findings. End with a roadmap paragraph.

**Model / Theory**: Force laws as display equations. System geometry, boundary conditions, parameter values with physical justification. Network construction algorithm. Equation of motion for dynamics.

**Results and Discussion** (combined): Quantitative results referenced to figures. Physical interpretation alongside data. Phase transition analysis: order parameters, critical thresholds, scaling behavior, data collapse. Compare with experiment (Doha et al. 2022).

**Conclusion**: Summarize key findings (not repeat abstract). Physical implications. Limitations and future directions.

**Format targets**: PRL ~3500 words, PRE 6000–10000 words.


## Paragraph Templates

### Results Paragraph
**Structure**: Topic (Test) → Method → Observation (Quantified) → Support → Interpretation

### Methods Paragraph
**Structure**: Model Component → Assumptions → Implementation → Justification

### Discussion Paragraph
**Structure**: Key Finding → Mechanism → Context/Literature → Implications


### Stating Results
**Pattern**: Observation + Quantification + Interpretation

- **Weak**: "Compaction changes with density."
- **Strong**: "Compaction exhibits a sharp transition at $p_c = 8.0\sigma \approx 100\,\mu\mathrm{m}$, coinciding with the percolation threshold, demonstrating that macroscopic behavior emerges from network topology."


### Transitions
- **Logic**: "Having established X, we next examine Y..."
- **Contrast**: "Unlike purely elastic matrices..."
- **Causality**: "As cells approach the threshold..."


## Domain-Specific Patterns

### Physics Framing
**Pattern**: Physical Concept → Biological Context

- **Percolation**: "Below threshold, cells form finite clusters; above $p_c$, a system-spanning cluster emerges."
- **Phase Transition**: "The sharp change at $p_c$ is analogous to second-order phase transitions, with connectivity as the order parameter."


## Citation and Reference Management

For full citation guidance and LaTeX usage, see `references/citation-styles.md`.

**APS Numbered Style** — in-text format:
```
Several studies have demonstrated this effect [1].
The results were reported by Doha et al. [2], and later confirmed [3,4].
```
