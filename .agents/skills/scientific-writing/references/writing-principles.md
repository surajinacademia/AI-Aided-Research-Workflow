# Scientific Writing Principles

## Contents

- [Author's Voice and Style](#authors-voice-and-style)
- [1. Clarity](#1-clarity)
- [2. Conciseness](#2-conciseness)
- [3. Accuracy](#3-accuracy)
- [4. Objectivity](#4-objectivity)
- [5. Consistency](#5-consistency)
- [6. Logical Organization](#6-logical-organization)
- [Revision Checklist](#revision-checklist)


## Overview

Effective scientific writing requires mastering fundamental principles that ensure clarity, precision, and impact. Unlike creative or narrative writing, scientific writing prioritizes accuracy, conciseness, and objectivity. This guide covers the core principles that distinguish good scientific writing from poor writing and provides practical strategies for improvement.


## Author's Voice and Style
- **Concise and direct**: Avoid verbosity, to the point, clear and direct. Coherent structure and flow.
- **Descriptive precision**: Use specific, quantitative language
- **Physics-grounded**: Frame biological phenomena using physics principles
- **Clear logic**: Maintain tight connection between observations, models, and conclusions

### Active Voice and Clarity
- Prefer active voice: "Cells form networks" not "Networks are formed by cells"
- Remove unnecessary qualifiers ("very", "quite", "rather", "crucial" etc.)
- Use parallel structure in lists and comparisons
- Avoid nominalization: "We analyzed" not "We performed an analysis of"


### Sentence Structure

- Keep sentences focused (avoid >25 words)
- Use parallel structure in lists
- Ensure each sentence connects logically to the previous one
- Remove redundant phrases


### 1. Clarity

**Definition:** Writing that is immediately understandable to the intended audience without ambiguity or confusion.

#### Strategies for Clarity

**Use precise, unambiguous language:**

**Define technical terms and symbols at first use:**
```
"We define the compaction parameter psi = 1 - A/A_0, where A is the current gel
area and A_0 is the initial area."
```

**Maintain logical flow within and between paragraphs:**
- Each paragraph should have one main idea
- Topic sentence introduces the paragraph's focus
- Supporting sentences develop that focus
- Transition sentences connect paragraphs

**Use active voice when it improves clarity:**
```
Passive (less clear): "The network was constructed by placing nodes uniformly."
Active (clearer): "We constructed the network by placing nodes uniformly."
```

However, passive voice is acceptable in Methods when the action is more important than the actor:
```
"Cells were placed randomly within the circular domain using Poisson disk sampling."
```


### 2. Conciseness

**Definition:** Expressing ideas in the fewest words necessary without sacrificing clarity or completeness.


**Avoid throat-clearing phrases:**
```
Wordy: "It is interesting to note that the results of our simulation demonstrate that..."
Concise: "Our simulations demonstrate that..." or "The results show that..."
```

**The key question:** Can any word be removed without losing meaning or precision? If yes, remove it.

### 3. Accuracy

**Definition:** Precise, correct representation of data, methods, and interpretations.


**Report exact values with appropriate precision:**
```
Poor: "The compaction was about 50%."
Better: "The compaction parameter was psi = 0.47 +/- 0.03 (ensemble average over 20 realizations)."
```

**Match precision to measurement capability:**
```
Inappropriate: "The critical cell gap was 103.247 um" (implies false precision)
Appropriate: "The critical cell gap was approximately 100 um"
```

**Use consistent terminology throughout:**
```
Inconsistent: Introduction calls it "cell density," Model calls it "cell
concentration," Results call it "cell number density."

Consistent: Use "cell density rho" throughout, defined once in the Model section.
```

**Distinguish observations from interpretations:**
```
Observation: "The compaction parameter decreased sharply at d = d_c [Fig. 2(a)]."
Interpretation: "This sharp transition coincides with the percolation threshold,
suggesting that collective cell connectivity drives gel compaction."
```

**Be specific about uncertainty:**
```
Vague: "There may be some finite-size effects."
Specific: "Finite-size effects shift the critical cell gap by approximately 5%
for system sizes R < 500 um."
```

**Verify all numbers:**
- Check that numbers in text match figures
- Verify parameter values are consistent between Model and Results
- Confirm ensemble sizes and averaging procedures
- Double-check all equations for sign errors and dimensions

#### Common Accuracy Problems

**Overgeneralization:**
```
Poor: "Cell networks always undergo percolation-driven compaction."
Better: "In our simulations, gel compaction coincided with the percolation threshold
of the cell connectivity network for all coordination numbers z > 3.5."
```

**Unwarranted causal claims:**
```
Poor: "Buckling causes the percolation transition."
Better: "Fiber buckling enables large local deformations that facilitate the
sharp compaction transition coinciding with the percolation threshold."
```

**Imprecise numerical descriptions:**
```
Vague: "Many simulations were run."
Precise: "We performed 20 independent realizations for each cell density."
```

## Additional Key Principles

### 4. Objectivity

**Definition:** Presenting information impartially without bias, exaggeration, or unsupported opinion.

**Strategies:**

**Present results without bias:**
```
Biased: "As expected, our superior model captured the transition perfectly."
Objective: "The model reproduces the sharp compaction transition observed
experimentally [2], with the critical cell gap within 10% of the measured value."
```

**Acknowledge conflicting evidence:**
```
"Our finding of a sharp percolation-driven transition contrasts with the gradual
compaction predicted by continuum models [3], likely because continuum approaches
average out the discrete cell connectivity that drives the transition."
```

**Avoid emotional or evaluative language:**
```
Subjective: "The results were striking and remarkable."
Objective: "The compaction parameter exhibited a sharp transition at the
percolation threshold [Fig. 2]."
```

**Distinguish fact from speculation:**
```
"The observed coincidence of the compaction and percolation transitions suggests
that collective cell connectivity, rather than individual cell traction, is the
primary mechanism driving gel compaction."
(Uses "suggests" and "primary" to indicate interpretation.)
```

### 5. Consistency

**Maintain consistency throughout the manuscript:**

**Terminology:**
- Use the same term for the same concept (don't alternate between "cell spacing," "cell gap," and "intercellular distance")
- Define abbreviations at first use and use consistently
- Use standard notation for physical quantities

**Notation:**
- Same symbol for the same quantity ($d$ for cell gap everywhere, not $d$ sometimes and $\ell$ other times)
- Consistent subscript/superscript conventions
- Units attached consistently

**Tense:**
- Past tense for your specific simulation results
- Present tense for established physical facts and model description
- See detailed tense guide in SKILL.md

**Style:**
- Follow journal guidelines consistently
- Citation format (all numbered [1])
- Figure labeling (a), (b), (c) throughout

### 6. Logical Organization

**Create a clear "red thread" through the manuscript:**

**Paragraph structure:**
1. Topic sentence (main idea)
2. Supporting sentences (evidence, equations, data)
3. Concluding/transition sentence (link to next idea)

**Section flow:**
- Each section builds logically on the previous
- Physical questions raised in Introduction are answered in Results
- Model decisions are justified by the physics they capture

**Signposting:**
```
"First, we examine how the coordination number affects the compaction transition..."
"Next, we investigate the role of fiber buckling..."
"Finally, we compare the percolation-driven model with local traction models..."
```

**Parallelism:**
```
Not parallel: "We studied (1) the percolation threshold, (2) how compaction
depends on cell density, and (3) dynamics of network formation."

Parallel: "We studied (1) the percolation threshold, (2) the density dependence
of compaction, and (3) the dynamics of network formation."
```

## Revision Checklist

### Content Level

- [ ] Does every sentence add value?
- [ ] Are physical claims supported by simulation data?
- [ ] Is the logic clear and sound?
- [ ] Are interpretations warranted by results?

### Paragraph Level

- [ ] Does each paragraph have one main idea?
- [ ] Are paragraphs in logical order?
- [ ] Are transitions smooth?
- [ ] Is there a clear "red thread"?

### Sentence Level

- [ ] Are sentences clear and concise?
- [ ] Is sentence structure varied?
- [ ] Are there no dangling modifiers?
- [ ] Do subjects and verbs agree?

### Word Level

- [ ] Is word choice precise?
- [ ] Are technical terms and symbols defined?
- [ ] Is terminology consistent throughout?
- [ ] Are abbreviations necessary and defined?
- [ ] Are numbers formatted correctly?

### Grammar and Mechanics

- [ ] Is verb tense correct and consistent?
- [ ] Are commas used correctly?
- [ ] Do pronouns agree with antecedents?
- [ ] Is punctuation correct?
- [ ] Are all equations dimensionally consistent?
