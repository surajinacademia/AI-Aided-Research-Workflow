# Matplotlib Advanced Patterns — Publication Stage (Python Pipeline)

Multi-panel, simulation-coupled figures for journal submission when the pipeline stays in Python.

## GridSpec multi-panel layout

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(18, 14), facecolor=C_BG)
fig.suptitle(
    "Model Title\nSubtitle with key aspects",
    fontsize=17, fontweight="bold", y=0.98
)
gs = GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.38,
              left=0.06, right=0.97, top=0.93, bottom=0.04)

ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])
# ...
ax_table = fig.add_subplot(gs[2, :])  # full-width panel
```

## Panel background helper

```python
def panel_bg(ax, color=C_PANEL, alpha=0.35, label=None, label_color=C_TEXT):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_visible(False)
    rect = FancyBboxPatch((0, 0), 1, 1, transform=ax.transAxes,
                          boxstyle="round,pad=0.02", linewidth=1.2,
                          edgecolor="#aaaaaa", facecolor=color, alpha=alpha,
                          zorder=0, clip_on=False)
    ax.add_patch(rect)
    if label:
        ax.text(0.03, 0.97, label, transform=ax.transAxes,
                fontsize=11, fontweight="bold", color=label_color, va="top", ha="left")
```

Label each panel: `"A  |  Panel title"`, `"B  |  Panel title"`, etc.

## Simulation-coupled panels

Panels that compute real physics, not placeholder data.

### Bessel field profile (K0)

```python
from scipy.special import k0, k1

r = np.linspace(0.05, 8, 500)
for lam, ls, lbl in [(1.0, "-", r"$\lambda = 1$"), (2.0, "--", r"$\lambda = 2$")]:
    C = k0(r / lam)
    C /= C[0]  # normalize
    ax.plot(r, C, ls=ls, lw=2, label=lbl)

# Annotate asymptotic regimes
ax.annotate(r"near field: $K_0 \sim -\ln(r/\lambda)$", xy=(0.4, 0.85), fontsize=7.5)
ax.annotate(r"far field: $K_0 \sim e^{-r/\lambda}$", xy=(5, 0.18), fontsize=7.5)
```

### 2D concentration field heatmap

```python
src = np.array([[5, 5], [7, 3], [6, 7]])  # source cell positions
X, Y = np.meshgrid(np.linspace(0, 10, 200), np.linspace(0, 10, 200))
Cfield = np.zeros_like(X)
for sj in src:
    d = np.sqrt((X - sj[0])**2 + (Y - sj[1])**2) + 1e-9
    Cfield += k0(d / lam)

im = ax.contourf(X, Y, Cfield, levels=30, cmap="YlOrRd", alpha=0.9)
ax.contour(X, Y, Cfield, levels=10, colors="white", linewidths=0.4, alpha=0.4)
fig.colorbar(im, ax=ax, shrink=0.85, label="C(r)", pad=0.02)
```

### Gradient arrow at a cell position

Compute the actual gradient from K1:

```python
# Gradient at cell i from all sources
gx = np.sum([(ci[0]-sj[0]) / (np.linalg.norm(ci-sj)+1e-9)**2 *
             (-k1(np.linalg.norm(ci-sj)/lam)/lam) for sj in src])
gy = np.sum([(ci[1]-sj[1]) / (np.linalg.norm(ci-sj)+1e-9)**2 *
             (-k1(np.linalg.norm(ci-sj)/lam)/lam) for sj in src])
gn = np.sqrt(gx**2 + gy**2) + 1e-9
ax.annotate("", xy=(ci[0]-gx/gn*1.4, ci[1]-gy/gn*1.4), xytext=ci,
            arrowprops=dict(arrowstyle="->", color=C_GRAD, lw=2.5))
```

### Monte Carlo cell simulation

```python
np.random.seed(42)
N, T = 40, 300
pos   = np.random.uniform(1, 9, (N, 2))
theta = np.random.uniform(0, 2*np.pi, N)

traj = [pos.copy()]
for _ in range(T):
    new_theta = theta.copy()
    for i in range(N):
        # compute gradient at cell i from neighbors within rc
        # ... (K1-based gradient computation)
        phi = np.arctan2(gy_i, gx_i) if (gx_i != 0 or gy_i != 0) else theta[i]
        tau = np.sin(phi - theta[i])
        new_theta[i] = (theta[i] + np.random.normal(0, sig) + kap * tau) % (2*np.pi)
    theta = new_theta
    pos += spd * np.column_stack([np.cos(theta), np.sin(theta)])
    pos = np.clip(pos, 0.5, 9.5)
    traj.append(pos.copy())
```

Plot trajectories and final positions with heading arrows.

### Phase diagram (kappa/sigma sweep)

```python
kappas = np.linspace(0.02, 0.8, 18)
sigmas = np.linspace(0.05, 1.2, 18)
order_mat = np.zeros((len(sigmas), len(kappas)))

for ki, k in enumerate(kappas):
    for si, s in enumerate(sigmas):
        # run short simulation, compute order parameter
        order_mat[si, ki] = np.abs(np.mean(np.exp(1j * theta_final)))

ax.contourf(kappas, sigmas, order_mat, levels=20, cmap="RdYlGn")
ax.contour(kappas, sigmas, order_mat, levels=[0.3, 0.6],
           colors=["white", "cyan"], linewidths=1.2)
```

## Comparison table via patches

```python
rows = [
    ["Aspect", "Model A", "Model B"],
    ["Expression", r"$\tau = \sum \sin(\theta_{ij})/d^\nu$", r"$\tau = \sin(\phi_{\nabla C} - \theta_i)$"],
    # ...
]
col_widths = [0.22, 0.39, 0.39]
col_x      = [0.01, 0.23, 0.62]
row_h      = 0.095

for ri, row in enumerate(rows):
    y = 0.97 - ri * row_h
    bg = "#1e3a5f" if ri == 0 else ("#ffc9c9" if ri % 2 == 1 else "#e5dbff")
    fc = "white" if ri == 0 else C_TEXT
    for ci, (txt, cx, cw) in enumerate(zip(row, col_x, col_widths)):
        rect = FancyBboxPatch((cx, y - row_h + 0.005), cw - 0.005, row_h - 0.008,
                              transform=ax.transAxes,
                              boxstyle="round,pad=0.005", linewidth=0.5,
                              edgecolor="#aaa", facecolor=bg, alpha=0.9, clip_on=False)
        ax.add_patch(rect)
        ax.text(cx + 0.008, y - row_h / 2, txt, transform=ax.transAxes,
                fontsize=8.5, color=fc, fontweight="bold" if ri == 0 else "normal", va="center")
```

## Heading update vector diagram

Show current heading, gradient direction, and new heading as arrows from cell center, with arc showing torque:

```python
from matplotlib.patches import Arc

theta_i = np.radians(30)    # current heading
phi_grad = np.radians(80)   # gradient direction

# Current heading arrow (gray)
ax.annotate("", xy=(cx+L*np.cos(theta_i), cy+L*np.sin(theta_i)), xytext=(cx, cy),
            arrowprops=dict(arrowstyle="->", color="#555", lw=2))
ax.text(..., r"$\theta_i(t)$", ...)

# Gradient arrow (purple)
ax.annotate("", xy=(cx+Lg*np.cos(phi_grad), cy+Lg*np.sin(phi_grad)), xytext=(cx, cy),
            arrowprops=dict(arrowstyle="->", color=C_GRAD, lw=2.5))

# Torque arc between them
arc = Arc((cx, cy), 4, 4, angle=0,
          theta1=np.degrees(theta_i), theta2=np.degrees(phi_grad),
          color=C_TORQUE, lw=2, ls="--")
ax.add_patch(arc)
```
