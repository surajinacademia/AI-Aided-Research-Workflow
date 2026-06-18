# Matplotlib Patterns — Prototyping Stage

## LaTeX math setup (required)

```python
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
```

## Color palette convention

Define all colors as named constants at script top:

```python
C_BG      = "#f8f9fa"
C_CELL_I  = "#d0bfff"
C_CELL_J  = "#b2f2bb"
C_BORDER  = "#1e1e1e"
C_GRAD    = "#8b5cf6"
C_FIELD   = "#f59e0b"
C_TORQUE  = "#ef4444"
C_UPDATE  = "#06b6d4"
C_PANEL   = "#dbe4ff"
C_TEXT    = "#1e1e1e"
```

## Model parameters as named constants

```python
KAPPA   = 0.01    # steering coupling strength
SIGMA   = 0.1     # angular noise std dev
R_C     = 3.0     # sensing radius (cell diameters)
LAMBDA_ = 3.0     # chemoattractant decay length
```

Use these in titles and annotations:

```python
ax.text(6.0, 7.65,
        f'Chemoattraction Model  '
        f'($\\kappa$={KAPPA}, $\\sigma$={SIGMA}, $r_c$={R_C})',
        ha='center', fontsize=13, fontweight='bold')
```

## Arrow helper

```python
def arr(ax, x0, y0, x1, y1, color="#333", lw=1.6, hw=0.018, hl=0.025, **kw):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f"->,head_width={hw},head_length={hl}",
                                color=color, lw=lw), **kw)
```

## Common patches

```python
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, FancyArrowPatch, Arc

# Cell body
ax.add_patch(Ellipse((cx, cy), width=1.6, height=1.3,
                     facecolor='#a5d8ff', edgecolor='#4a9eed', linewidth=2.5))

# Rounded box (for equation panels, cascade boxes)
ax.add_patch(FancyBboxPatch(
    (x, y), width, height, boxstyle='round,pad=0.15',
    facecolor='#d0bfff', edgecolor='#8b5cf6', linewidth=2))

# Dashed sensing radius ring
ax.add_patch(Circle((cx, cy), radius,
                    fill=False, edgecolor='#4a9eed',
                    linewidth=1.3, linestyle='--', alpha=0.5))
```

## Equation rendering in annotations

```python
# Inline LaTeX in text
ax.text(x, y, r'$\theta_i(t+1) = \theta_i(t) + \eta_i + \kappa\,\sin(\phi_{\nabla C_i} - \theta_i)$',
        fontsize=12, ha='center')

# Equation box at bottom of figure
ax.add_patch(FancyBboxPatch((0.3, 0.1), 11.4, 0.95,
             boxstyle='round,pad=0.15', facecolor='white', edgecolor='#9ca3af'))
ax.text(6.0, 0.575, r'$\theta_i(t+1) = ...$', ha='center', fontsize=12)
```

## Gradient halo pattern

Concentric ellipses with increasing opacity:

```python
for radius, alpha in zip([4.0, 3.2, 2.4, 1.6, 0.8],
                         [0.05, 0.09, 0.14, 0.20, 0.30]):
    halo = Ellipse((cx, cy), width=radius*2.0, height=radius*1.4,
                   facecolor='#f59e0b', alpha=alpha, zorder=1)
    ax.add_patch(halo)
```

## Save convention

```python
out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(out_dir, exist_ok=True)
plt.savefig(os.path.join(out_dir, 'figure_name.pdf'),
            format='pdf', bbox_inches='tight', facecolor=C_BG)
plt.close(fig)
```
