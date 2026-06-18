# AI Pattern Removal for Scientific Prose

Distilled from the `deslop` skill for manuscript writing. For the full catalog covering blog posts, newsletters, and general prose, see that skill.

Apply these checks before delivering any drafted or revised manuscript prose.

---

## Quick Checks

Run through every item before finishing a revision pass:

- Passive voice? Find the actor, make them the subject. Exception: methods where the action matters more than the actor.
- Throat-clearing opener? ("It is worth noting that...", "It is interesting to observe that...", "Our simulations show that...") Cut to the claim.
- Filler transition? ("It's worth noting", "Importantly", "Notably", "Interestingly") Delete. Connect the ideas directly.
- "Despite these challenges..." formula? Rewrite. State what the limitation actually is and why it matters.
- Vague declarative? ("The implications are significant", "The reasons are physical") Name the specific implication or reason.
- False agency? ("The results emerged from...", "The transition naturally appeared") Name the actor: "We measured...", "The transition coincides with..."
- Superficial participle analysis? ("...highlighting the importance of...", "...underscoring the role of...", "...reflecting broader trends in...") Cut the participle; state what it actually shows.
- Invented concept label? ("the connectivity paradox", "the percolation trap") Name the mechanism directly instead.
- "Serves as"? Replace with "is" or a specific verb.
- Listicle in a trench coat? ("The first limitation... The second limitation... The third limitation...") Weave into prose; connect the points.
- Anaphora? (Five consecutive sentences starting "We will...") Collapse into one sentence naming methods, datasets, and deliverables.
- Grandiose stakes? ("fundamentally reshape how we think about...") Scale the claim to what the data actually shows.
- "Landscape" / "paradigm shift" / "ecosystem"? Replace with the specific field, model, or system.
- Em dash for dramatic pause? Remove. Use a comma, parenthetical, or period.
- Three consecutive sentences the same length? Break one.
- Same point restated across multiple sentences with no new content? Cut to the single clearest version.

---

## Scoring

Rate 1–10 on each dimension before submitting a draft:

| Dimension | Question for manuscript prose |
|-----------|-------------------------------|
| Directness | Does each sentence make a claim, or does it announce that a claim is coming? |
| Rhythm | Do sentence lengths vary, or is every sentence the same weight? |
| Trust | Does the prose treat the reader as a physicist, or does it explain things they already know? |
| Authenticity | Does it sound like a specific physicist wrote it, or like a language model approximating one? |
| Density | Can any sentence be removed without losing content? |

Below 35/50: revise before delivering.

---

## Domain Examples

Selected from the `deslop` skill's full examples file. These cover the patterns most common in biophysics manuscript writing.

### Throat-Clearing + Binary Contrast

**Before:**
> "Here's the thing: modeling compaction in collagen gels is hard. Not because the physics is complex. Because the biology is complex. Let that sink in."

**After:**
> "Collagen gel compaction resists simple mechanical models. The fiber network mechanics are tractable. The cell behavior — traction forces that vary with gel stiffness, protrusion length, and neighbor contacts — is not."

---

### Filler + "Despite These Challenges"

**Before:**
> "It's worth noting that these findings have important implications for how we navigate the challenges of understanding compaction mechanisms moving forward. Despite these challenges, this work contributes meaningfully to the growing body of literature, highlighting the need for continued evaluation and underscoring the importance of robust mechanistic models."

**After:**
> "If individual cells compact only their local neighborhood, then global compaction should scale smoothly with density. A sharp threshold requires a mechanism that is collective — force transmission through a spanning network, not a sum of independent contributions."

---

### Passive Voice + False Agency

**Before:**
> "It was observed that compaction increased sharply below the critical cell gap. The percolation probability naturally emerged as the controlling parameter. These results arose from our analysis of 50 independent simulation ensembles."

**After:**
> "We measured a sharp increase in compaction below the critical cell gap $d_c \approx 8\sigma$. The percolation probability curve peaks at the same gap, matching the compaction transition to within one bin width. We confirmed this agreement across 50 independent ensembles."

---

### "Serves As" + Superficial Participle Analysis

**Before:**
> "The percolation framework serves as a foundational conceptual tool for understanding collagen gel compaction, contributing to our mechanistic understanding and underscoring the importance of network connectivity in driving collective cell behavior."

**After:**
> "The percolation framework identifies a geometric threshold: once the cell network spans the gel, contractile forces transmit system-wide and compaction is substantial. Below this threshold, cells deform only local matrix neighborhoods, and global area does not change."

---

### Listicle in a Trench Coat

**Before:**
> "The first limitation of our model is the assumption of 2D geometry. The second limitation is the use of a fixed cell connection length. The third limitation is the neglect of active cell migration during compaction."

**After:**
> "Our 2D quasi-planar approximation holds because the gel diameter is roughly four times its height, but it cannot capture the out-of-plane fiber reorientation that contributes to axial compaction. We also fix the protrusion length $\lambda_c$ throughout the simulation, whereas cells in experiment extend and retract protrusions dynamically as the gel contracts."

---

### "It's Worth Noting" + Invented Concept Label

**Before:**
> "It's worth noting that this creates what might be called the 'connectivity-compaction feedback loop': as the gel compacts, cell-cell distances decrease, enabling new connections, which drive further compaction, reflecting broader trends in the tension between local and global mechanics."

**After:**
> "Compaction feeds back on connectivity. As the gel contracts, cell-cell distances decrease, bringing previously isolated cells within protrusion range $\lambda_c$ and enabling new connections. This positive feedback steepens the compaction curve near the critical gap."

---

### Grandiose Stakes + Landscape

**Before:**
> "In today's rapidly evolving mechanobiology landscape, cell-matrix interactions have fundamentally reshaped how we think about tissue mechanics. This paradigm shift has far-reaching implications for our understanding of disease."

**After:**
> "Fibroblasts embedded in collagen generate contractile forces that remodel the surrounding matrix. In freely floating gels, this remodeling is collective: isolated cells produce no lasting compaction, but a connected multicellular network can contract the gel by more than 80%."

---

### One-Point Dilution

**Before:**
> "Network percolation matters. In fact, percolation is the most underappreciated concept in mechanobiology. When a cell network percolates, it transmits forces. Force transmission leads to compaction. Compaction changes matrix density. Changing matrix density changes cell behavior. The lesson? Think about percolation. Non-percolating networks cannot compact gels."

**After:**
> "Network percolation sets the compaction threshold. When we rescaled compaction curves from simulations with different $\lambda_c$ values by the critical gap $d_c(\lambda_c)$, all curves collapsed onto a single master curve — a signature of percolation universality."
