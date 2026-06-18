# Excalidraw Patterns — Drafting Stage

## MCP tool usage (preferred method)

Call `read_me` before first use in a session to get the element format reference:

```
mcp__claude_ai_Excalidraw__read_me()
```

Create a view with elements:

```
mcp__claude_ai_Excalidraw__create_view(elements=[...])
```

Save state for later editing:

```
mcp__claude_ai_Excalidraw__save_checkpoint(name="schematic-v1")
mcp__claude_ai_Excalidraw__read_checkpoint(name="schematic-v1")
```

## Color palette

Use consistent colors across Excalidraw, Matplotlib, and TikZ:

| Role | Hex | Excalidraw name |
|------|-----|-----------------|
| Cell i | `#d0bfff` | light violet |
| Cell j / source | `#b2f2bb` | light green |
| Gradient | `#8b5cf6` | violet |
| Field / concentration | `#f59e0b` | amber |
| Torque / noise | `#ef4444` | red |
| Update / result | `#06b6d4` | cyan |
| Panel background | `#dbe4ff` | light blue |
| Text | `#1e1e1e` | near-black |

## Layout conventions

- Place source/target cells on the right, sensing cells on the left (gradient flows left-to-right).
- Signal cascade boxes below, heading update boxes above.
- Equation summary at the bottom spanning full width.
- Use proper variable names on all labels: "Cell i", not "Cell 1"; use Greek letters where possible (Excalidraw supports unicode: theta, kappa, sigma, eta, phi, nabla).

## Unicode math for Excalidraw text

Excalidraw does not render LaTeX. Use unicode equivalents:

| Symbol | Unicode |
|--------|---------|
| theta | `θ` |
| kappa | `κ` |
| sigma | `σ` |
| eta | `η` |
| phi | `φ` |
| nabla | `∇` |
| subscript i | `ᵢ` |
| subscript j | `ⱼ` |
| in [-1,1] | `∈ [-1, +1]` |
| sim | `~` |
| N(0, sigma^2) | `𝒩(0, σ²)` |

Example label: `θᵢ(t+1) = [θᵢ(t) + ηᵢ + κ·sin(φ∇C - θᵢ)] mod 2π`

## Element positioning

- Background rectangle: `x=10, y=10, width=920, height=580`
- Title: centered at top, `fontSize=22`
- Cells: ellipses with `width ~120, height ~100`
- Arrows: use `type: "arrow"` with `startBinding` and `endBinding` for connected elements
- Annotation boxes: `type: "rectangle"` with `roundness: {type: 3}`, small `fontSize=13`

## Feedback loop

After creating the initial view:
1. User can edit directly in Excalidraw (drag, resize, recolor)
2. Save checkpoint after user edits
3. Read checkpoint to get updated state
4. Iterate based on feedback
