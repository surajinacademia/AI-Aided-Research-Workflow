"""
Chemoattraction-Based Cell Migration Model — Matplotlib figure
Visualises the secreted-field model from the physics document:
  C(r) = (c0/2pi Dc) sum_j K0(|r-rj|/lambda)
  tau_i = sin(phi_nablaC - theta_i)
  theta_i(t+1) = [theta_i(t) + eta_i + kappa*tau_i] mod 2pi

6-panel publication figure:
  A — K0 Bessel field profile
  B — 2D concentration field heatmap
  C — Sine coupling geometry
  D — Heading update schematic
  E — Monte Carlo simulation (N=40, T=300)
  F — kappa/sigma phase diagram
  G — Comparison table (full-width)
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch, Arc
from matplotlib.gridspec import GridSpec
from scipy.special import k0, k1

# ── colour palette ────────────────────────────────────────────────────────────
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
C_MUT     = "#555555"

fig = plt.figure(figsize=(18, 14), facecolor=C_BG)
fig.suptitle(
    "Chemoattraction-Based Cell Migration Model\n"
    "Secreted Chemoattractant Field  |  Gradient Sensing  |  Heading Update",
    fontsize=17, fontweight="bold", color=C_TEXT, y=0.98
)

gs = GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.38,
              left=0.06, right=0.97, top=0.93, bottom=0.04)

# ── helper ────────────────────────────────────────────────────────────────────
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
                fontsize=11, fontweight="bold", color=label_color,
                va="top", ha="left")

def arr(ax, x0, y0, x1, y1, color="#333", lw=1.6, hw=0.018, hl=0.025, **kw):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f"->,head_width={hw},head_length={hl}",
                                color=color, lw=lw), **kw)

# ═══════════════════════════════════════════════════════════════════════════════
# Panel A — K0 Bessel field profile
# ═══════════════════════════════════════════════════════════════════════════════
ax_field = fig.add_subplot(gs[0, 0])
panel_bg(ax_field, "#fff3bf", 0.5, "A  |  Chemoattractant field  C(r)", "#92400e")

r = np.linspace(0.05, 8, 500)
for lam, ls, lbl in [(1.0, "-", r"$\lambda$ = 1"), (2.0, "--", r"$\lambda$ = 2"), (4.0, ":", r"$\lambda$ = 4")]:
    C = k0(r / lam)
    C /= C[0]
    ax_field.plot(r, C, ls=ls, lw=2, label=lbl)

ax_field.set_xlabel("distance  r  (cell diameters)", fontsize=9)
ax_field.set_ylabel("C(r) / C(0)", fontsize=9)
ax_field.set_title(r"$K_0(r/\lambda)$ — field from one source cell", fontsize=9, pad=4)
ax_field.legend(fontsize=8, loc="upper right")
ax_field.set_xlim(0, 8); ax_field.set_ylim(0, 1.05)
ax_field.tick_params(labelsize=8)
ax_field.axvline(2, color="#aaaaaa", lw=0.8, ls="--", alpha=0.6)
ax_field.text(2.05, 0.5, r"r = $\lambda$", fontsize=8, color="#777")

# near-field annotation
ax_field.annotate("near field\n"+r"$K_0 \sim -\ln(r/\lambda)$", xy=(0.4, 0.85), fontsize=7.5,
                  color="#92400e", ha="left")
ax_field.annotate("far field\n"+r"$K_0 \sim e^{-r/\lambda}$", xy=(5, 0.18), fontsize=7.5,
                  color="#4a9eed", ha="left")

# ═══════════════════════════════════════════════════════════════════════════════
# Panel B — 2D concentration field heatmap
# ═══════════════════════════════════════════════════════════════════════════════
ax_map = fig.add_subplot(gs[0, 1])
panel_bg(ax_map, "#fff3bf", 0.5, "B  |  2D field from 3 source cells", "#92400e")

lam = 2.5
# source cell positions
src = np.array([[5, 5], [7, 3], [6, 7]], dtype=float)
xg = np.linspace(0, 10, 200)
yg = np.linspace(0, 10, 200)
X, Y = np.meshgrid(xg, yg)
Cfield = np.zeros_like(X)
for sj in src:
    d = np.sqrt((X - sj[0])**2 + (Y - sj[1])**2) + 1e-9
    Cfield += k0(d / lam)

im = ax_map.contourf(X, Y, Cfield, levels=30, cmap="YlOrRd", alpha=0.9)
ax_map.contour(X, Y, Cfield, levels=10, colors="white", linewidths=0.4, alpha=0.4)
fig.colorbar(im, ax=ax_map, shrink=0.85, label="C(r)", pad=0.02)

for sj in src:
    ax_map.plot(*sj, "o", ms=10, color=C_CELL_J, mec="#22c55e", mew=2, zorder=5)
    ax_map.text(sj[0]+0.15, sj[1]+0.15, "j", fontsize=9, color="#15803d", fontweight="bold")

# sensing cell i
ci = np.array([2.5, 5.0])
ax_map.plot(*ci, "o", ms=12, color=C_CELL_I, mec="#8b5cf6", mew=2.5, zorder=6)
ax_map.text(ci[0]+0.15, ci[1]+0.15, "i", fontsize=9, color="#5b21b6", fontweight="bold")

# gradient arrow at cell i
gx = np.sum([(ci[0]-sj[0]) / (np.linalg.norm(ci-sj)+1e-9)**2 *
             (-k1(np.linalg.norm(ci-sj)/lam)/lam) for sj in src])
gy = np.sum([(ci[1]-sj[1]) / (np.linalg.norm(ci-sj)+1e-9)**2 *
             (-k1(np.linalg.norm(ci-sj)/lam)/lam) for sj in src])
gn = np.sqrt(gx**2+gy**2)+1e-9
ax_map.annotate("", xy=(ci[0]-gx/gn*1.4, ci[1]-gy/gn*1.4),
                xytext=(ci[0], ci[1]),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.3",
                                color=C_GRAD, lw=2.5))
ax_map.text(ci[0]-gx/gn*1.6-0.3, ci[1]-gy/gn*1.6+0.15,
            r"$\nabla C$", fontsize=10, color=C_GRAD, fontweight="bold")

ax_map.set_xlim(0, 10); ax_map.set_ylim(0, 10)
ax_map.set_aspect("equal"); ax_map.tick_params(labelsize=8)
ax_map.set_xlabel("x  (cell diameters)", fontsize=9)
ax_map.set_ylabel("y  (cell diameters)", fontsize=9)
ax_map.set_title("Concentration field & gradient at cell i", fontsize=9, pad=4)

# sensing radius circle
circ = Circle(ci, radius=3.0, fill=False, ec="#8b5cf6", lw=1.2,
              ls="--", alpha=0.7)
ax_map.add_patch(circ)
ax_map.text(ci[0]+3.05, ci[1], r"$r_c$", fontsize=8, color="#8b5cf6")

# ═══════════════════════════════════════════════════════════════════════════════
# Panel C — Sine coupling geometry
# ═══════════════════════════════════════════════════════════════════════════════
ax_sine = fig.add_subplot(gs[0, 2])
panel_bg(ax_sine, "#ffc9c9", 0.3, "C  |  Sine torque geometry", "#991b1b")

theta_vals = np.linspace(-np.pi, np.pi, 400)
ax_sine.plot(np.degrees(theta_vals), np.sin(theta_vals),
             color=C_TORQUE, lw=2.5, label=r"$\tau = \sin(\phi_{\nabla C} - \theta_i)$")
ax_sine.axhline(0, color="#aaa", lw=0.8)
ax_sine.axvline(0, color="#aaa", lw=0.8)
ax_sine.fill_between(np.degrees(theta_vals), np.sin(theta_vals), 0,
                     where=np.sin(theta_vals) > 0, alpha=0.18, color="#22c55e",
                     label="turn left (CCW)")
ax_sine.fill_between(np.degrees(theta_vals), np.sin(theta_vals), 0,
                     where=np.sin(theta_vals) < 0, alpha=0.18, color="#ef4444",
                     label="turn right (CW)")

for ang, lbl, col in [(90, r"$+\pi/2$"+"\nmax left", "#15803d"),
                       (-90, r"$-\pi/2$"+"\nmax right", "#991b1b"),
                       (0, "0\nno steer", "#555"),
                       (180, r"$\pi$"+"\nno steer", "#555")]:
    ax_sine.axvline(ang, color=col, lw=0.9, ls=":", alpha=0.7)
    ax_sine.text(ang+3, 0.72 if col != "#555" else -0.88,
                 lbl, fontsize=7, color=col, ha="left")

ax_sine.set_xlabel(r"$\phi_{\nabla C} - \theta_i$  (degrees)", fontsize=9)
ax_sine.set_ylabel(r"torque  $\tau_i$", fontsize=9)
ax_sine.set_title(r"$\tau_i \in [-1, +1]$  always", fontsize=9, pad=4)
ax_sine.set_xlim(-185, 185); ax_sine.set_ylim(-1.2, 1.2)
ax_sine.legend(fontsize=7.5, loc="lower right")
ax_sine.tick_params(labelsize=8)

# ═══════════════════════════════════════════════════════════════════════════════
# Panel D — Heading update schematic
# ═══════════════════════════════════════════════════════════════════════════════
ax_upd = fig.add_subplot(gs[1, 0])
panel_bg(ax_upd, "#c3fae8", 0.45, "D  |  Heading update schematic", "#0e7490")
ax_upd.set_xlim(0, 10); ax_upd.set_ylim(0, 10)
ax_upd.set_aspect("equal")
ax_upd.axis("off")

# cell body
cell = Circle((5, 5), 1.6, color=C_CELL_I, ec="#8b5cf6", lw=2.5, zorder=3)
ax_upd.add_patch(cell)
ax_upd.text(5, 5, "i", ha="center", va="center", fontsize=14,
            fontweight="bold", color="#5b21b6", zorder=4)

theta_i = np.radians(30)
phi_grad = np.radians(80)
noise    = np.radians(15)
theta_new = theta_i + noise + 0.4*np.sin(phi_grad - theta_i)

L = 2.6
# current heading
ax_upd.annotate("", xy=(5+L*np.cos(theta_i), 5+L*np.sin(theta_i)),
                xytext=(5, 5),
                arrowprops=dict(arrowstyle="->,head_width=0.22,head_length=0.28",
                                color="#555", lw=2))
ax_upd.text(5+L*np.cos(theta_i)+0.15, 5+L*np.sin(theta_i)+0.15,
            r"$\theta_i(t)$", fontsize=9.5, color="#555")

# gradient direction
Lg = 3.0
ax_upd.annotate("", xy=(5+Lg*np.cos(phi_grad), 5+Lg*np.sin(phi_grad)),
                xytext=(5, 5),
                arrowprops=dict(arrowstyle="->,head_width=0.22,head_length=0.28",
                                color=C_GRAD, lw=2.5))
ax_upd.text(5+Lg*np.cos(phi_grad)+0.05, 5+Lg*np.sin(phi_grad)+0.18,
            r"$\phi_{\nabla C}$", fontsize=9.5, color=C_GRAD, fontweight="bold")

# new heading
ax_upd.annotate("", xy=(5+L*np.cos(theta_new), 5+L*np.sin(theta_new)),
                xytext=(5, 5),
                arrowprops=dict(arrowstyle="->,head_width=0.22,head_length=0.28",
                                color=C_UPDATE, lw=2.5))
ax_upd.text(5+L*np.cos(theta_new)+0.12, 5+L*np.sin(theta_new)+0.05,
            r"$\theta_i(t+1)$", fontsize=9.5, color=C_UPDATE, fontweight="bold")

# arc showing torque
arc = Arc((5, 5), 4, 4, angle=0,
          theta1=np.degrees(theta_i), theta2=np.degrees(phi_grad),
          color=C_TORQUE, lw=2, ls="--")
ax_upd.add_patch(arc)
mid = (theta_i + phi_grad) / 2
ax_upd.text(5+2.3*np.cos(mid), 5+2.3*np.sin(mid),
            r"$\kappa \cdot \sin(\Delta\phi)$", fontsize=8.5, color=C_TORQUE,
            ha="center", fontweight="bold")

ax_upd.set_title("Single timestep heading update", fontsize=9, pad=4)

# equation box
eq_str = (r"$\theta_i(t+1) = [ \theta_i(t)  +  \eta_i  +  \kappa \cdot \sin(\phi_{\nabla C} - \theta_i) ] \mod 2\pi$" + "\n"
          r"$\eta_i \sim \mathcal{N}(0, \sigma^2)$   |   $\kappa$ = coupling strength   |   $\tau_i \in [-1,+1]$")
ax_upd.text(5, 0.4, eq_str, ha="center", va="bottom", fontsize=8,
            color=C_TEXT, style="italic",
            bbox=dict(boxstyle="round,pad=0.4", fc="#ffffffcc", ec="#aaa", lw=0.8))

# ═══════════════════════════════════════════════════════════════════════════════
# Panel E — Monte Carlo simulation of N cells
# ═══════════════════════════════════════════════════════════════════════════════
np.random.seed(42)
N   = 40
T   = 300
lam = 3.0
kap = 0.18
sig = 0.35
rc  = 3.5
spd = 0.15

pos   = np.random.uniform(1, 9, (N, 2))
theta = np.random.uniform(0, 2*np.pi, N)

traj = [pos.copy()]
for _ in range(T):
    new_theta = theta.copy()
    for i in range(N):
        gx_i, gy_i = 0.0, 0.0
        for j in range(N):
            if j == i: continue
            dx = pos[j, 0] - pos[i, 0]
            dy = pos[j, 1] - pos[i, 1]
            d  = np.sqrt(dx*dx + dy*dy) + 1e-9
            if d > rc or d < 0.1: continue
            w   = k1(d / lam) / lam
            gx_i += -w * (-dx / d)
            gy_i += -w * (-dy / d)
        phi = np.arctan2(gy_i, gx_i) if (gx_i != 0 or gy_i != 0) else theta[i]
        tau = np.sin(phi - theta[i])
        new_theta[i] = (theta[i] + np.random.normal(0, sig) + kap * tau) % (2*np.pi)
    theta = new_theta
    pos[:, 0] = np.clip(pos[:, 0] + spd * np.cos(theta), 0.5, 9.5)
    pos[:, 1] = np.clip(pos[:, 1] + spd * np.sin(theta), 0.5, 9.5)
    traj.append(pos.copy())

ax_sim = fig.add_subplot(gs[1, 1])
panel_bg(ax_sim, "#e5dbff", 0.35, "E  |  Simulation  (N=40, T=300 steps)", "#5b21b6")
ax_sim.set_xlim(0.3, 9.7); ax_sim.set_ylim(0.3, 9.7)
ax_sim.set_aspect("equal")

# draw trajectories (thin, faded)
step_skip = 10
for i in range(N):
    xs = [traj[t][i, 0] for t in range(0, T+1, step_skip)]
    ys = [traj[t][i, 1] for t in range(0, T+1, step_skip)]
    ax_sim.plot(xs, ys, "-", lw=0.6, color="#999999", alpha=0.4)

# final positions with heading arrows
for i in range(N):
    ax_sim.plot(pos[i, 0], pos[i, 1], "o", ms=7,
                color=C_CELL_I, mec="#8b5cf6", mew=1.2, zorder=4)
    ax_sim.annotate("", xy=(pos[i,0]+0.35*np.cos(theta[i]),
                              pos[i,1]+0.35*np.sin(theta[i])),
                    xytext=(pos[i,0], pos[i,1]),
                    arrowprops=dict(arrowstyle="->,head_width=0.12,head_length=0.14",
                                    color="#5b21b6", lw=1.2), zorder=5)

ax_sim.set_xlabel("x  (cell diameters)", fontsize=9)
ax_sim.set_ylabel("y  (cell diameters)", fontsize=9)
ax_sim.set_title(r"$\kappa$={}, $\sigma$={}, $\lambda$={}, $r_c$={}".format(kap, sig, lam, rc),
                 fontsize=8.5, pad=4)
ax_sim.tick_params(labelsize=8)

# ═══════════════════════════════════════════════════════════════════════════════
# Panel F — kappa/sigma phase diagram
# ═══════════════════════════════════════════════════════════════════════════════
np.random.seed(7)
N2  = 30
T2  = 200
kappas = np.linspace(0.02, 0.8, 18)
sigmas = np.linspace(0.05, 1.2, 18)
order_mat = np.zeros((len(sigmas), len(kappas)))

for ki, k in enumerate(kappas):
    for si, s in enumerate(sigmas):
        th = np.random.uniform(0, 2*np.pi, N2)
        p  = np.random.uniform(1, 9, (N2, 2))
        for _ in range(T2):
            nt = th.copy()
            for i in range(N2):
                gx2, gy2 = 0.0, 0.0
                for j in range(N2):
                    if j == i: continue
                    dx2 = p[j,0]-p[i,0]; dy2 = p[j,1]-p[i,1]
                    d2  = np.sqrt(dx2*dx2+dy2*dy2)+1e-9
                    if d2 > 3.5 or d2 < 0.1: continue
                    w2 = k1(d2/3.0)/3.0
                    gx2 -= -w2*(-dx2/d2); gy2 -= -w2*(-dy2/d2)
                phi2 = np.arctan2(gy2, gx2) if (gx2!=0 or gy2!=0) else th[i]
                nt[i] = (th[i]+np.random.normal(0,s)+k*np.sin(phi2-th[i]))%(2*np.pi)
            th = nt
            p[:,0] = np.clip(p[:,0]+0.15*np.cos(th),0.5,9.5)
            p[:,1] = np.clip(p[:,1]+0.15*np.sin(th),0.5,9.5)
        order_mat[si, ki] = np.abs(np.mean(np.exp(1j*th)))

ax_phase = fig.add_subplot(gs[1, 2])
panel_bg(ax_phase, "#fff3bf", 0.4, r"F  |  Order parameter  $|\langle e^{i\theta}\rangle|$", "#92400e")
pm = ax_phase.contourf(kappas, sigmas, order_mat, levels=20, cmap="RdYlGn")
fig.colorbar(pm, ax=ax_phase, shrink=0.85, label=r"order  $\psi$", pad=0.02)
ax_phase.contour(kappas, sigmas, order_mat, levels=[0.3, 0.6],
                 colors=["white", "cyan"], linewidths=[1.2, 1.2])
ax_phase.set_xlabel(r"$\kappa$  (coupling strength)", fontsize=9)
ax_phase.set_ylabel(r"$\sigma$  (noise std dev)", fontsize=9)
ax_phase.set_title(r"Phase diagram  $\kappa/\sigma$ controls coherence", fontsize=9, pad=4)
ax_phase.tick_params(labelsize=8)
ax_phase.text(0.62, 0.9, "coherent\nalignment", transform=ax_phase.transAxes,
              fontsize=8, color="white", fontweight="bold", ha="center")
ax_phase.text(0.15, 0.15, "random\nwalk", transform=ax_phase.transAxes,
              fontsize=8, color="white", fontweight="bold", ha="center")

# ═══════════════════════════════════════════════════════════════════════════════
# Panel G — Comparison table
# ═══════════════════════════════════════════════════════════════════════════════
ax_tab = fig.add_subplot(gs[2, :])
panel_bg(ax_tab, "#f8f9fa", 0.6, "", "#1e1e1e")
ax_tab.axis("off")

rows = [
    ["Aspect", "Canonical neighbor-torque  (current)", "Secreted-field model  (proposed)"],
    ["Torque expression",
     r"$\tau_i = \sum_j \sin(\theta_{ij} - \theta_i) / d_{ij}^\nu$",
     r"$\tau_i = \sin(\phi_{\nabla C} - \theta_i)$"],
    ["Torque range",
     "Unbounded — grows with neighbor count",
     r"Always $\in [-1, +1]$  density-independent"],
    ["Physical origin",
     r"Ad hoc exponent $\nu$  (no mechanistic basis)",
     r"$K_1(r/\lambda)$ from 2D diffusion-degradation PDE"],
    ["What cell i processes",
     "Each neighbor j separately (per-pair sine)",
     r"Aggregate gradient $\nabla C_i$  (single sine)"],
    ["Interpretation",
     "Geometry-directed positional alignment",
     "True gradient chemotaxis"],
    ["Free parameters",
     r"$\kappa$,  $\nu$,  $r_c$",
     r"$\kappa$,  $\lambda$  (or $\gamma$),  $r_c$"],
    ["Network formation",
     "Requires CIL to suppress Keller-Segel clustering",
     "Same — CIL still needed  (structure unchanged)"],
]

col_widths = [0.22, 0.39, 0.39]
col_x      = [0.01, 0.23, 0.62]
row_h      = 0.095
y0         = 0.97

for ri, row in enumerate(rows):
    y = y0 - ri * row_h
    bg = "#1e3a5f" if ri == 0 else ("#ffc9c9" if ri % 2 == 1 else "#e5dbff")
    fc = "white" if ri == 0 else C_TEXT
    fw = "bold" if ri == 0 else "normal"
    for ci, (cell_txt, cx, cw) in enumerate(zip(row, col_x, col_widths)):
        rect = FancyBboxPatch((cx, y - row_h + 0.005), cw - 0.005, row_h - 0.008,
                              transform=ax_tab.transAxes,
                              boxstyle="round,pad=0.005", linewidth=0.5,
                              edgecolor="#aaa", facecolor=bg, alpha=0.9,
                              clip_on=False)
        ax_tab.add_patch(rect)
        ax_tab.text(cx + 0.008, y - row_h / 2, cell_txt,
                    transform=ax_tab.transAxes,
                    fontsize=8.5, color=fc, fontweight=fw, va="center")

ax_tab.text(0.5, 0.005, "G  |  Canonical vs Secreted-field model comparison",
            transform=ax_tab.transAxes, fontsize=10, fontweight="bold",
            color="#1e3a5f", ha="center", va="bottom")

plt.tight_layout()
plt.show()
