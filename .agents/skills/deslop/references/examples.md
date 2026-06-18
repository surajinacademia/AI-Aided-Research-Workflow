# Before/After Examples

## Example 1: Throat-Clearing + Binary Contrast (Scientific)

**Before:**
> "Here's the thing: modeling compaction in collagen gels is hard. Not because the physics is complex. Because the biology is complex. Let that sink in."

**After:**
> "Collagen gel compaction resists simple mechanical models. The fiber network mechanics are tractable. The cell behavior — traction forces that vary with gel stiffness, protrusion length, and neighbor contacts — is not."

**Changes:** Removed opener, binary contrast structure, and emphasis crutch. Named the specific biological variables that make the problem hard.

---

## Example 2: Filler + "Despite These Challenges" (Discussion Section)

**Before:**
> "It's worth noting that these findings have important implications for how we navigate the challenges of understanding compaction mechanisms moving forward. Despite these challenges, this work contributes meaningfully to the growing body of literature, highlighting the need for continued evaluation and underscoring the importance of robust mechanistic models."

**After:**
> "If individual cells compact only their local neighborhood, then global compaction should scale smoothly with density. A sharp threshold requires a mechanism that is collective — force transmission through a spanning network, not a sum of independent contributions."

**Changes:** Replaced filler transition, vague declarative, "despite these challenges" formula, and two superficial participle phrases with the specific mechanistic implication of the findings.

---

## Example 3: Grandiose Stakes + Landscape (Introduction)

**Before:**
> "In today's rapidly evolving mechanobiology landscape, cell-matrix interactions have fundamentally reshaped how we think about tissue mechanics. This paradigm shift has far-reaching implications for our understanding of disease."

**After:**
> "Fibroblasts embedded in collagen generate contractile forces that remodel the surrounding matrix. In freely floating gels, this remodeling is collective: isolated cells produce cannot produce large compaction, but a connected multicellular network can contract the gel by more than 80%."

**Changes:** Eliminated "landscape," "paradigm shift," "fundamentally," and the vague stakes claim. Replaced with a concrete contrast showing why collective behavior matters.

---

## Example 4: Passive Voice + False Agency (Results Section)

**Before:**
> "It was observed that compaction increased sharply below the critical cell gap. The percolation probability naturally emerged as the controlling parameter. These results arose from our analysis of 50 independent simulation ensembles."

**After:**
> "We measured a sharp increase in compaction below the critical cell gap $d_c \approx 8\sigma$. The percolation probability curve peaks at the same gap, matching the compaction transition to within one bin width. We confirmed this agreement across 50 independent ensembles."

**Changes:** Named the actor ("we"). Replaced false agency ("percolation probability naturally emerged," "results arose") with specific claims and a number.

---

## Example 5: Self-Posed Rhetorical Question (Blog Post / Talk Abstract)

**Before:**
> "What if I told you that most collagen gel compaction models miss the key physics? The result? Wrong predictions. The worst part? Nobody checks whether the transition is sharp or smooth. Here's why that matters:"

**After:**
> "Most continuum models of collagen gel compaction predict smooth, monotonic contraction as cell density increases. Doha et al. (2022) measured a sharp threshold instead: gels with 1.5 million cells/ml compacted by 80%, while gels at 1 million cells/ml barely moved."

**Changes:** Removed rhetorical setup and three self-posed questions. Replaced with a specific experimental contrast the reader can evaluate.

---

## Example 6: "Serves As" + Superficial Participle Analysis (Abstract)

**Before:**
> "The percolation framework serves as a foundational conceptual tool for understanding collagen gel compaction, contributing to our mechanistic understanding and underscoring the importance of network connectivity in driving collective cell behavior."

**After:**
> "The percolation framework identifies a geometric threshold: once the cell network spans the gel, contractile forces transmit system-wide and compaction is substantial. Below this threshold, cells deform only local matrix neighborhoods, and global area does not change."

**Changes:** Replaced "serves as a foundational conceptual tool" with what the framework actually predicts. Replaced two participle phrases with the specific mechanism.

---

## Example 7: Narrator Distance + Vague Declarative (Discussion Section)

**Before:**
> "Nobody designed collagen gel compaction to exhibit a sharp transition. The reasons are physical. This is genuinely complex, and the implications are significant."

**After:**
> "The sharp transition emerges from geometry, not biochemistry. Cells connect to neighbors within protrusion range $\lambda_c$. As density crosses the percolation threshold, a spanning cluster first appears and force can transmit across the gel for the first time."

**Changes:** Replaced narrator distance with the specific physical mechanism. Replaced two vague declaratives with the causal chain.

---

## Example 8: Listicle in a Trench Coat (Discussion Section)

**Before:**
> "The first limitation of our model is the assumption of 2D geometry. The second limitation is the use of a fixed cell connection length. The third limitation is the neglect of active cell migration during compaction."

**After:**
> "Our 2D quasi-planar approximation holds because the gel diameter is roughly four times its height, but it cannot capture the out-of-plane fiber reorientation that contributes to axial compaction. We also fix the protrusion length $\lambda_c$ throughout the simulation, whereas cells in experiment extend and retract protrusions dynamically as the gel contracts."

**Changes:** Replaced the numbered listicle with woven prose. Combined related points and added specificity about why the approximations matter.

---

## Example 9: One-Point Dilution (Discussion Section)

**Before:**
> "Network percolation matters. In fact, percolation is the most underappreciated concept in mechanobiology. When a cell network percolates, it transmits forces. Force transmission leads to compaction. Compaction changes matrix density. Changing matrix density changes cell behavior. The lesson? Think about percolation. Non-percolating networks cannot compact gels."

**After:**
> "Network percolation sets the compaction threshold. When we rescaled compaction curves from simulations with different $\lambda_c$ values by the critical gap $d_c(\lambda_c)$, all curves collapsed onto a single master curve — a signature of percolation universality."

**Changes:** Eight sentences restating one point became two sentences with the specific evidence (data collapse) that demonstrates the claim.

---

## Example 10: Historical Analogy Stacking (General / Talk)

**Before:**
> "Percolation explains traffic jams. Percolation explains power grid failures. Percolation explains forest fires. Percolation explains epidemic spread. Every collective threshold phenomenon follows the same pattern."

**After:**
> "Percolation describes the threshold at which a random network first spans its domain. In collagen compaction, the spanning cluster is the cell connectivity network; the control parameter is cell gap rather than bond probability."

**Changes:** One concrete application examined in depth instead of four analogies. Named the specific mapping between the abstract theory and the physical system.

---

## Example 11: Anaphora Abuse (Grant Narrative)

**Before:**
> "We will develop a minimal mechanical model of collagen gel compaction. We will validate this model against existing experimental data. We will extend the model to include active cell migration. We will compare predictions to new experiments. We will disseminate our findings through open-source simulation code."

**After:**
> "We will develop and validate an agent-based network model of fibroblast-driven collagen gel compaction against the Doha et al. (2022) dataset, then release the Julia simulation code with documentation and reproduce scripts for all figures."

**Changes:** Collapsed five anaphoric sentences into one that names specific methods, datasets, and deliverables.

---

## Example 12: Dramatic Fragmentation (General / Introduction)

**Before:**
> "Connectivity. Contractility. Geometry. You need all three. That's it. That's the mechanism."

**After:**
> "Compaction requires three ingredients: cell contractility, cell-cell connectivity, and enough cells to form a spanning network."

**Changes:** Single sentence. No performative emphasis.

---

## Example 13: False Vulnerability + Meta-Commentary (Blog Post / Perspective)

**Before:**
> "And yes, since we're being honest: I've run plenty of simulations where the compaction curve looked sharp and I convinced myself it was percolation. I want to explore why that inference is so tempting. In this post, I'll walk you through what I've learned."

**After:**
> "A sharp compaction curve is necessary but not sufficient evidence for percolation. I ran simulations with a purely linear traction model and got curves that looked equally sharp at finite system size. The test that distinguished them was data collapse under rescaling by $\lambda_c$."

**Changes:** Replaced false vulnerability with a specific methodological admission. Cut the meta-commentary. Stated the diagnostic instead of announcing it.

---

## Example 14: "It's Worth Noting" + Invented Concept Label (Results Section)

**Before:**
> "It's worth noting that this creates what might be called the 'connectivity-compaction feedback loop': as the gel compacts, cell-cell distances decrease, enabling new connections, which drive further compaction, reflecting broader trends in the tension between local and global mechanics."

**After:**
> "Compaction feeds back on connectivity. As the gel contracts, cell-cell distances decrease, bringing previously isolated cells within protrusion range $\lambda_c$ and enabling new connections. This positive feedback steepens the compaction curve near the critical gap."

**Changes:** Cut the filler transition and invented concept label. Replaced the superficial participle analysis with the specific mechanism (feedback via decreased cell gap).

---

## Example 15: "Imagine a World" + Patronizing Analogy (General / Talk)

**Before:**
> "Imagine a world where every cell in a gel could talk to its neighbors. Think of it like a telephone network: you wouldn't expect to reach someone without a connected path. That's the promise of the percolation picture. Let's unpack why this matters."

**After:**
> "Force transmission through the gel requires a continuous mechanical path from cell to boundary. Below the percolation threshold, no such path exists and cells deform only local matrix. Doha et al. (2022) showed that adding inert beads — which cannot generate force but can relay it — shifts the critical cell gap upward, directly confirming the path-dependence."

**Changes:** Removed the "imagine" opener, the telephone analogy (which adds nothing), and the pedagogical "let's unpack." Replaced with a specific experimental test of the claim.
