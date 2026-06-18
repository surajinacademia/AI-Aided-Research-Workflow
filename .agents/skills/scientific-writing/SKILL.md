---
name: "scientific-writing"
description: "Scientific writing assistant for biophysics and soft matter manuscripts. Writes, edits, and revises LaTeX research papers for physics journals (PRL, PRE, Biophysical Journal, Soft Matter). Uses IMRAD structure with combined Results and Discussion. Handles figure captions, LaTeX equations (revtex4-2), numbered APS citations, and terminology consistency. Use when: writing or editing paper sections, drafting figure captions, formatting equations, checking terminology, revising prose, responding to reviewer comments, or any task involving the manuscript."
---

# Scientific Writing Assistant

## Overview

Edit and improve the LaTeX manuscript at:
`Percolation-Driven Compaction of Cell-Matrix Networks/paper/main.tex`

Bibliography: `Percolation-Driven Compaction of Cell-Matrix Networks/paper/references.bib`


## Writing Process

Follow a two-stage process:

1. **Outline**: List key points and logical flow for the section
2. **Draft**: Convert outline into full, flowing paragraphs

Always write in complete paragraphs with flowing prose. Never leave bullet points or outlines in the final manuscript. Every paragraph must have a topic sentence, supporting evidence, and a transition to the next idea.


## Author's Voice

- **Concise and direct** — avoid verbosity, get to the point
- **Physics-grounded** — frame biological phenomena using physics principles
- **Active voice** — "Cells form networks" not "Networks are formed by cells"
- **Quantitative** — specific values, not vague descriptions

Remove unnecessary qualifiers ("very", "quite", "rather", "crucial").
Avoid nominalization: "We analyzed" not "We performed an analysis of".
Avoid throat-clearing: "Our simulations show that..." not "It is interesting to note that the results of our simulation demonstrate that..."

Apply AI pattern checks before delivering any prose — see `references/deslop-scientific.md`.

**Epistemic language** — match certainty to evidence (see `references/epistemic-language.md` for full guide):
- **Strong** ("demonstrates", "shows") — only for direct, unambiguous results
- **Moderate** ("suggests", "is consistent with") — most mechanistic claims belong here
- **Speculative** ("may", "could") — extrapolating beyond data
- Simulations demonstrate **sufficiency**, not necessity. A model that reproduces an observation is *consistent with* an explanation, not proof of it
- Separate what the simulation *does* (state confidently) from what it *means for biology* (hedge appropriately)
- Weave model limitations into claims: "Within the assumptions of our model, this suggests..."


## Section Quick Reference

For section structure, paragraph templates, and format targets by journal, see `references/paper-structure.md`.


## Verb Tense

| Section | Tense | Example |
|---------|-------|---------|
| Model description | Present | "The network consists of..." |
| Simulation procedure | Past | "We performed 20 realizations..." |
| Established facts | Present | "Collagen gels exhibit strain-stiffening..." |
| Specific results | Past | "The compaction parameter decreased sharply..." |
| Interpretation | Present | "This coincidence suggests that..." |
| Figure references | Present | "Figure 2 shows..." |


## Figure Captions

See `references/figure-caption-guide.md` for the six principles, deconstructed examples, a bad-caption case study, and a rewritten model caption.


## Equations and LaTeX

- Use `$$..$$` for mathematical symbols and short inline equations
- Use display equations (`\begin{equation}`) for key force laws, equations of motion, and definitions
- Number all important equations for cross-referencing
- Use `revtex4-2` document class with `\bibliography{references}`
- APS numbered citations: `[1]`, `[2]`, `[3,4]`
- Multi-panel figures labeled (a), (b), (c)


## Reference Index

Load these files as needed based on the task:

| Task | File to load |
|------|-------------|
| Improving prose quality, revision | `references/writing-principles.md` |
| Removing AI patterns from prose | `references/deslop-scientific.md` |
| Structuring sections, paragraph templates | `references/paper-structure.md` |
| Writing figure captions | `references/figure-caption-guide.md` |
| Formatting citations, bibliography | `references/citation-styles.md` |
| Epistemic language, hedging, causal claims | `references/epistemic-language.md` |
| Need writing style exemplar | `references/examples/doha-2022.md`, `references/examples/peng-2025.md`, or `references/examples/zakharov-2021.md` |

**Example papers** (in `references/examples/`):
- `doha-2022.md` — Primary experimental reference (Doha et al. 2022, disorder-to-order transition)
- `peng-2025.md` — Writing style reference (Peng et al. 2025, fiber recruitment phase transition)
- `zakharov-2021.md` — Writing style reference (Zakharov et al. 2021, clot elasticity)


## Quick Editing Checklist

- [ ] First sentence states the main point clearly
- [ ] Results are quantified with specific values
- [ ] Active voice; subject performs the action
- [ ] Sentences connect logically; smooth transitions
- [ ] Physical/mechanistic interpretation is clear
- [ ] Technical terms defined on first use
- [ ] Parameter values consistent between Model and Results
- [ ] Equation formatting correct (proper LaTeX syntax)
