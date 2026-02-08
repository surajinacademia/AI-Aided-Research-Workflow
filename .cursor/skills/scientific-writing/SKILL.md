---
name: scientific-writing
priority: high
description: Creates concise, structured scientific documents with LaTeX equations, integrated figures, and clear technical writing. Use when documenting results, writing research summaries, or creating technical reports.
---

# Scientific Writing

Creates publication-quality markdown documents with mathematical rigor and visual clarity.

## Core Principles

1. **Concision**: Every sentence must earn its place
2. **Structure**: Logical flow with clear hierarchies
3. **Precision**: Technical accuracy over verbosity
4. **Integration**: Seamlessly embed figures and equations
5. **Clarity**: Complex ideas expressed simply

---

## Document Structure

### Standard Template

```markdown
# [Descriptive Title]

## Summary
[2-3 sentences: what was done, key finding, significance]

## Methods
[Essential details only - enough to reproduce]

## Results
[Observations → Data → Interpretation]

### [Subsection 1]
[Finding with supporting figure/equation]

### [Subsection 2]
[Finding with supporting figure/equation]

## Discussion
[Implications, limitations, future directions - 1 paragraph max]
```

### Section Guidelines

**Summary (3-5 lines)**
- First sentence: what you investigated
- Second sentence: how you investigated it
- Third sentence: what you found
- NO background or motivation

**Methods (minimal)**
- Only non-standard procedures
- Reference standard protocols by name
- Use lists for clarity

**Results (core content)**
- Lead with observation, follow with data
- One finding per subsection
- Figure/equation immediately after relevant text
- NO speculation (save for Discussion)

**Discussion (1 paragraph)**
- Interpret in broader context
- State limitations explicitly
- Suggest next steps

---

## Writing Style Rules

### Concision Tactics

**Before (wordy)**:
> The results that we obtained from the experiment clearly demonstrate that there is a significant increase in the fluorescence intensity.

**After (concise)**:
> Fluorescence intensity increased 3.2-fold (p < 0.001).

**Common eliminations**:
- ❌ "It is important to note that..."
- ❌ "The results clearly demonstrate..."
- ❌ "As can be seen from the figure..."
- ❌ "In order to..." → ✅ "To..."
- ❌ "Due to the fact that..." → ✅ "Because..."

### Active Voice

- ✅ "We measured force using AFM"
- ❌ "Force was measured using AFM"
- ✅ "Cells exhibited biphasic dynamics"
- ❌ "Biphasic dynamics were exhibited by cells"

### Precision

**Vague**: "The protein concentration was high"
**Precise**: "Protein concentration was 2.5 mg/mL"

**Vague**: "Cells responded quickly"
**Precise**: "Cells responded within 30 s"

---

## LaTeX Equations

### Inline Math

Use `$...$` for inline equations:

```markdown
The diffusion coefficient $D = 0.43 \pm 0.05 \, \mu\text{m}^2/\text{s}$ indicates...
```

### Display Math

Use `$$` with `\begin{}` and `\end{}` for block equations:

```markdown
The force balance is described by:

$$
\begin{equation}
F_{\text{total}} = F_{\text{spring}} + F_{\text{drag}} = kx + \gamma \frac{dx}{dt}
\end{equation}
$$

where $k$ is the spring constant and $\gamma$ is the drag coefficient.
```

### Equation Environments

**Common environments**:
- `equation` - Single numbered equation
- `align` - Multiple aligned equations
- `split` - Split long equations across lines

**Examples**:

```markdown
$$
\begin{align}
\sigma_{xx} &= E \epsilon_{xx} \\
\sigma_{yy} &= E \epsilon_{yy}
\end{align}
$$
```

### Equation Style

**Good practices**:
- Define all variables immediately after equation
- Use `\text{}` for words in equations: $F_{\text{max}}$
- Use proper spacing: `\,` for thin space (units)
- Use `equation` environment for automatic numbering

**Example**:

```markdown
The relationship between stress $\sigma$ and strain $\epsilon$ follows:

$$
\begin{equation}
\sigma = E \epsilon
\end{equation}
$$

where $E = 5 \pm 0.3$ kPa is the Young's modulus.
```

---

## Figure Integration

### Workflow

1. **Generate figure during analysis** (follow python-coding-standards)
2. **Save as SVG** in `figures/` folder
3. **Reference immediately** after relevant text
4. **Caption format**: statement of finding, not description

### Figure Template

```markdown
Force increased linearly with deformation up to 20% strain, then plateaued (Figure 1).

![Force-deformation relationship](figures/force_vs_strain.svg)
**Figure 1.** Linear stress-strain response transitions to plateau regime at ε > 0.2.
```

### Caption Guidelines

**Bad (descriptive)**:
> Figure 1. A plot showing force on the y-axis and deformation on the x-axis.

**Good (interpretive)**:
> Figure 1. Force increases linearly with deformation until strain exceeds 0.2.

**Best (finding)**:
> Figure 1. Biphasic mechanical response reveals strain-stiffening at ε > 0.2.

### Multiple Panels

For multi-panel figures:

```markdown
![Analysis overview](figures/analysis_overview.svg)
**Figure 2.** Cell morphology changes with substrate stiffness. **(A)** Representative images on soft (1 kPa), medium (10 kPa), and stiff (100 kPa) substrates. **(B)** Quantification shows area increases 2.5-fold from soft to stiff. **(C)** Aspect ratio decreases with stiffness (p < 0.001, n = 150 cells per condition).
```

---

## Data Presentation

### Tables (use sparingly)

Only when comparing multiple conditions across multiple metrics:

```markdown
| Condition | Spring Constant (pN/nm) | Relaxation Time (s) | n |
|-----------|------------------------|---------------------|---|
| Control   | 12.3 ± 1.2            | 45 ± 8             | 23 |
| Drug A    | 8.7 ± 0.9*            | 67 ± 12*           | 21 |
| Drug B    | 15.1 ± 1.8            | 38 ± 6             | 19 |

*p < 0.05 vs. control
```

**Table caption**: Place above table, descriptive

### Inline Data

For single comparisons, embed in text:

> Treatment increased velocity from 0.23 ± 0.03 to 0.41 ± 0.05 μm/s (p < 0.001, n = 45).

---

## Common Patterns

### Introducing Analysis

**Pattern**: Goal → Approach → Key result

> To determine whether force depends on loading rate, we performed constant-velocity indentation at speeds from 0.1 to 10 μm/s. Peak force scaled linearly with velocity (Figure 3A), consistent with viscoelastic behavior.

### Quantitative Results

**Pattern**: Observation → Measurement → Statistics

> Cells on stiff substrates adopted elongated morphologies. Aspect ratio increased from 1.8 ± 0.2 (soft) to 3.4 ± 0.4 (stiff), a 1.9-fold change (p < 0.001, n = 120 cells, Figure 2B).

### Model Validation

**Pattern**: Model → Prediction → Test → Result

> If force transmission is primarily via focal adhesions, disrupting integrin binding should reduce traction forces. We treated cells with RGD peptide and measured a 73% reduction in traction stress (Figure 4), confirming integrin-mediated adhesion.

---

## Checklist

Before finalizing document:

- [ ] Summary states finding in 3 sentences
- [ ] No sentence exceeds 25 words
- [ ] All equations defined immediately after appearance
- [ ] Figures referenced in text before appearing
- [ ] Figure captions state findings, not descriptions
- [ ] NO phrases: "clearly", "obviously", "it is important to note"
- [ ] NO repetition between sections
- [ ] Methods include only non-standard details
- [ ] Discussion is ≤ 1 paragraph
- [ ] All data includes uncertainty and sample size
- [ ] Active voice used throughout

---

## Quick Reference

### Numbers and Units

- Use ± for uncertainty: `5.2 ± 0.3 kPa`
- Thin space before units: `10 \, \mu\text{m}`
- Scientific notation for extremes: $3.2 \times 10^{-6}$
- Significant figures match precision

### Common Abbreviations

First use: full term (abbreviation)
> Atomic force microscopy (AFM) measurements revealed...

Subsequent: abbreviation only
> AFM images showed...

### References

Inline citation:
> Previous studies^[1,2]^ demonstrated...

End of document:
```markdown
## References

1. Smith et al. (2023) Nature 612: 123-130
2. Jones et al. (2022) Science 378: 456-460
```

---

## Anti-Patterns

### Avoid Redundancy

**Bad**:
> Figure 1 shows the force-distance curve. As can be seen in Figure 1, force increases with distance. The figure clearly demonstrates that...

**Good**:
> Force increased linearly with distance (Figure 1).

### Avoid Throat-Clearing

**Bad**:
> It is important to note that our results suggest that it may be possible that cells potentially exhibit...

**Good**:
> Cells exhibit viscoelastic behavior.

### Avoid Over-Qualification

**Bad**:
> The data appear to suggest that there might be a possible trend toward increased stiffness.

**Good**:
> Stiffness increased 1.8-fold (p = 0.03).

---
 