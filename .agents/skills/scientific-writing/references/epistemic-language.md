# Epistemic Language Guide for Simulation-Based Science

Match certainty to what the evidence actually supports. The key distinction: what your model/data *directly shows* vs. what you *infer* from it.


## Confidence Hierarchy

| Level | Language | When to use |
|-------|----------|-------------|
| **Strong** | "demonstrates", "shows" | Direct, unambiguous measurement or model result |
| **Confident** | "indicates", "reveals" | Slightly softer, still well-supported |
| **Moderate** | "suggests", "is consistent with" | Model reproduces observation but alternatives not ruled out. Most mechanistic claims belong here |
| **Hypothesis-testing** | "supports the hypothesis that" | Testing a specific idea and data aligns |
| **Speculative** | "may", "might", "could" | Extrapolating beyond data |
| **Explicitly open** | "is consistent with but does not rule out" | Acknowledging alternative explanations |


## The Core Discipline

A model that *reproduces* an observation doesn't *explain* it — it's *consistent with* one explanation. Be careful with causal language.

- Too strong: "This shows cells compact the gel"
- Correct: "This is consistent with cell-driven compaction"
- Also correct: "This suggests compaction is cell-mediated"


## Common Traps

- Saying "proves" — almost never appropriate in science
- Saying "shows" when you mean "suggests" — very common, reviewers notice
- Conflating correlation/reproduction with causation/mechanism

**Rule of thumb**: if a skeptic could reasonably propose an alternative interpretation, use "suggests" or "is consistent with," not "shows."


## Simulation-Specific Epistemic Rules

Simulations encode assumptions and show consequences. When a simulation matches an experiment, what you've shown is: *"IF these assumptions are true, THEN this outcome follows."* The match itself doesn't validate the assumptions.

### Reproducing an experimental trend

- "Our model **reproduces** the observed compaction dynamics" — neutral, accurate
- "This **suggests** that [mechanism X] may be sufficient to explain the observation"
- NOT: "This **shows** that cells compact via mechanism X"

### Proposing a mechanistic interpretation

- "The results are **consistent with** a picture in which..."
- "This behavior **can be explained by**..." (not "is explained by")
- "One interpretation is that..." — explicitly flagging it as interpretation

### Making predictions beyond the experiment

- "The model **predicts** that..." — strong and good, it's testable
- "We **expect** that..." with a caveat about what assumptions this rests on


## Separating Result from Interpretation

Always distinguish:

1. **What the simulation does** — "the model exhibits a percolation transition at cell density N" — state confidently
2. **What it means for biology** — "this transition *may correspond to* the experimentally observed onset of bulk compaction" — hedge appropriately


## Inline Model Limitations

Rather than burying caveats in a limitations section, weave them into claims:

- "Within the assumptions of our model, this suggests..."
- "To the extent that our coarse-grained representation captures the relevant physics..."
- "Although our model does not account for [X], the qualitative agreement suggests..."

This *strengthens* credibility — it shows understanding of what the model can and cannot do.


## The Practical Test

Before writing any claim, ask: *"Does my simulation assume this, or derive this?"*

If the model assumes cells exert contractile forces and then shows compaction — you cannot say the simulation explains *why* cells compact. You can say it shows that contractile forces *are sufficient* to produce the observed compaction pattern.

**Key distinction**: simulations typically demonstrate **sufficiency**, not **necessity**.


## Example Rewrite

**Weak:** "The simulation shows that cell-cell communication drives collective compaction."

**Strong:** "The simulation demonstrates that a contact-dependent force transmission rule is sufficient to reproduce the collective compaction observed experimentally, suggesting cell-cell mechanical coupling as a plausible mechanism."

The second version makes the same scientific point but is defensible, precise, and won't trigger reviewer objections.
