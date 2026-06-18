"""
Chemoattraction Model — Schematic (Matplotlib)
===============================================
Stage: Prototyping / Python workflow
Best for: Living next to your simulation code, parametric figures,
          fast iteration, instant feedback.

Run:
    python3 schematic.py

Writes ``../outputs/matplotlib_output.pdf`` (non-interactive; no display).

Tip: Add the line below for full LaTeX math rendering (requires LaTeX installed):
    matplotlib.rcParams['text.usetex'] = True
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ── Optional: enable full LaTeX rendering (comment out if LaTeX not installed) ─
# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['font.family'] = 'serif'

# ── Model parameters (change these and re-run — figure updates automatically) ─
KAPPA   = 0.01    # steering coupling strength
SIGMA   = 0.1     # angular noise std dev
R_C     = 3.0     # sensing radius (cell diameters)
LAMBDA_ = 3.0     # chemoattractant decay length

# ── Figure setup ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#f0f4ff')
ax.set_facecolor('#f0f4ff')

# ── Title (uses model parameters) ─────────────────────────────────────────────
ax.text(6.0, 7.65,
        f'Chemoattraction Model  '
        f'($\\kappa$={KAPPA}, $\\sigma$={SIGMA}, $r_c$={R_C})',
        ha='center', va='center', fontsize=13, fontweight='bold', color='#1e1e1e')

# ── Concentration gradient halo ───────────────────────────────────────────────
for radius, alpha in zip([4.0, 3.2, 2.4, 1.6, 0.8], [0.05, 0.09, 0.14, 0.20, 0.30]):
    halo = Ellipse((9.5, 4.0), width=radius * 2.0, height=radius * 1.4,
                   facecolor='#f59e0b', alpha=alpha, zorder=1)
    ax.add_patch(halo)

# ── Source cell ───────────────────────────────────────────────────────────────
ax.add_patch(Circle((9.5, 4.0), 0.6,
                    facecolor='#ffd8a8', edgecolor='#f59e0b', linewidth=2.5, zorder=5))
ax.text(9.5, 4.0,  'Source\n(VEGF)', ha='center', va='center',
        fontsize=9, fontweight='bold', color='#92400e', zorder=6)
ax.text(9.5, 3.2,  'Secreting cell', ha='center', fontsize=8,
        color='#92400e', style='italic')

# Gradient direction label
ax.annotate('', xy=(7.6, 4.3), xytext=(5.4, 4.7),
            arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.8, linestyle='dashed'))
ax.text(5.8, 5.0, '[C] concentration gradient $\\nabla C$',
        ha='center', fontsize=9, color='#92400e',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='#fff3bf',
                  edgecolor='#f59e0b', alpha=0.9))

# ── Sensing cell i ────────────────────────────────────────────────────────────
ax.add_patch(Ellipse((2.5, 4.0), width=1.6, height=1.3,
                     facecolor='#a5d8ff', edgecolor='#4a9eed',
                     linewidth=2.5, zorder=5))
ax.text(2.5, 4.0, r'Cell $i$', ha='center', va='center',
        fontsize=12, fontweight='bold', color='#1e3a5f', zorder=6)

# Receptors on right edge
for y_off in [-0.22, 0.0, 0.22]:
    ax.add_patch(FancyBboxPatch(
        (3.27, 4.0 + y_off - 0.08), 0.30, 0.16,
        boxstyle='round,pad=0.02',
        facecolor='#ef4444', edgecolor='#b91c1c', linewidth=1, zorder=6))
ax.text(3.65, 4.0, 'Receptors\n(VEGFR)', ha='left', va='center',
        fontsize=8.5, color='#b91c1c')

# Sensing radius dashed ring
ax.add_patch(Circle((2.5, 4.0), R_C * 0.73,   # scaled to figure coords
                    fill=False, edgecolor='#4a9eed',
                    linewidth=1.3, linestyle='--', alpha=0.5, zorder=3))
ax.text(2.5, 1.55, f'$r_c$ = {R_C} (sensing radius)',
        ha='center', fontsize=8.5, color='#2563eb', style='italic')

# ── Intracellular cascade box ─────────────────────────────────────────────────
ax.add_patch(FancyBboxPatch(
    (4.3, 1.5), 3.0, 1.1, boxstyle='round,pad=0.15',
    facecolor='#d0bfff', edgecolor='#8b5cf6', linewidth=2, zorder=5))
ax.text(5.8, 2.05, 'Intracellular Signal Cascade',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color='#4c1d95', zorder=6)
ax.text(5.8, 1.72, 'PI3K / Rac1 / actin polarization',
        ha='center', va='center', fontsize=8, color='#5b21b6', zorder=6)

# Arrow: receptor → cascade
ax.annotate('', xy=(5.2, 2.6), xytext=(3.6, 3.6),
            arrowprops=dict(arrowstyle='->', color='#8b5cf6', lw=2.0))
ax.text(4.1, 3.0, 'GPCR /\nRTK signal', ha='center', va='center',
        fontsize=8.5, color='#8b5cf6',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#ede9fe',
                  edgecolor='#8b5cf6', alpha=0.85))

# ── Heading update box ────────────────────────────────────────────────────────
ax.add_patch(FancyBboxPatch(
    (4.4, 5.1), 2.8, 0.85, boxstyle='round,pad=0.15',
    facecolor='#b2f2bb', edgecolor='#22c55e', linewidth=2, zorder=5))
ax.text(5.8, 5.525, r'$\theta_i$ heading update',
        ha='center', va='center', fontsize=10,
        fontweight='bold', color='#14532d', zorder=6)

# Arrow: cascade → heading update
ax.annotate('', xy=(5.8, 5.1), xytext=(5.8, 2.6),
            arrowprops=dict(arrowstyle='->', color='#22c55e', lw=2.2))
ax.text(6.35, 3.85,
        f'$\\kappa \\cdot \\sin(\\phi_{{\\nabla}} - \\theta_i)$\n'
        f'$\\kappa$ = {KAPPA}',
        ha='left', va='center', fontsize=9, color='#166534',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#d1fae5',
                  edgecolor='#22c55e', alpha=0.9))

# Arrow: directed migration
ax.annotate('', xy=(8.7, 4.0), xytext=(6.4, 5.4),
            arrowprops=dict(arrowstyle='->', color='#22c55e', lw=2.8))
ax.text(7.8, 5.0, 'Directed\nmigration', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color='#14532d',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='#d1fae5',
                  edgecolor='#22c55e', alpha=0.85))

# ── Angular noise box ─────────────────────────────────────────────────────────
ax.add_patch(FancyBboxPatch(
    (0.3, 5.3), 2.3, 0.75, boxstyle='round,pad=0.12',
    facecolor='#ffc9c9', edgecolor='#ef4444', linewidth=1.8, zorder=5))
ax.text(1.45, 5.675,
        f'$\\eta_i \\sim \\mathcal{{N}}(0,\\,{SIGMA}^2)$',
        ha='center', va='center', fontsize=10, color='#7f1d1d', zorder=6)

ax.annotate('', xy=(5.0, 5.45), xytext=(2.6, 5.6),
            arrowprops=dict(arrowstyle='->', color='#ef4444',
                            lw=1.8, linestyle='dashed'))
ax.text(3.7, 5.85, 'angular noise', ha='center', fontsize=8, color='#ef4444')

# ── Equation footer ───────────────────────────────────────────────────────────
ax.add_patch(FancyBboxPatch(
    (0.3, 0.1), 11.4, 0.95, boxstyle='round,pad=0.15',
    facecolor='white', edgecolor='#9ca3af', linewidth=1.3, alpha=0.95))
ax.text(6.0, 0.575,
        r'$\theta_i(t+1) = \theta_i(t) + \eta_i'
        r'+ \kappa\,\sin(\phi_{\nabla C_i} - \theta_i)'
        r'\quad (\mathrm{mod}\;2\pi)$',
        ha='center', va='center', fontsize=12, color='#1e1e1e')

# ── Stage label ───────────────────────────────────────────────────────────────
ax.text(0.35, 7.65, 'Stage 2 — Prototyping / Python Workflow',
        ha='left', fontsize=9, color='#6b7280', style='italic')

# ── Save ──────────────────────────────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'matplotlib_output.pdf')
plt.savefig(out_path, format='pdf', bbox_inches='tight', facecolor='#f0f4ff')
print(f"Saved → {out_path}")
plt.close(fig)
