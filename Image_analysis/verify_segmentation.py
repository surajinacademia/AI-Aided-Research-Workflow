"""
Verify Cellpose segmentation quality for img00.
Loads image and masks, computes region stats, and writes overlay + CSV.
"""
import numpy as np
import pandas as pd
from pathlib import Path
from skimage import io
from skimage.measure import regionprops
from skimage.segmentation import find_boundaries
import matplotlib.pyplot as plt

# Paths
BASE = Path(__file__).resolve().parent / "demo_images"
IMG_PATH = BASE / "img00.png"
MASK_PATH = BASE / "img00_masks.png"
OUT_DIR = Path(__file__).resolve().parent.parent / "figures"
OUT_DIR.mkdir(exist_ok=True)
CSV_PATH = OUT_DIR / "img00_segmentation_stats.csv"
OVERLAY_PATH = OUT_DIR / "img00_segmentation_overlay.png"
HIST_PATH = OUT_DIR / "img00_area_distribution.svg"


def load_masks_as_labels(path):
    """Load mask image and return integer label array (0 = background)."""
    m = io.imread(path)
    if m.ndim == 3:
        m = m[:, :, 0]
    return np.asarray(m, dtype=np.int32)


def main():
    img = io.imread(IMG_PATH)
    if img.ndim == 3:
        img_display = img
    else:
        img_display = np.stack([img] * 3, axis=-1)

    labels = load_masks_as_labels(MASK_PATH)
    n_cells = labels.max()
    props = regionprops(labels)

    areas = np.array([r.area for r in props])
    perims = np.array([r.perimeter for r in props])
    equiv_diam = np.array([r.equivalent_diameter for r in props])
    ecc = np.array([r.eccentricity for r in props])

    summary = {
        "n_cells": n_cells,
        "area_mean": float(areas.mean()),
        "area_std": float(areas.std()),
        "area_min": int(areas.min()),
        "area_max": int(areas.max()),
        "equiv_diameter_mean_px": float(equiv_diam.mean()),
        "perimeter_mean": float(perims.mean()),
        "eccentricity_mean": float(ecc.mean()),
    }

    rows = [
        {
            "label": r.label,
            "area": r.area,
            "perimeter": r.perimeter,
            "equivalent_diameter": r.equivalent_diameter,
            "eccentricity": r.eccentricity,
        }
        for r in props
    ]
    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(OUT_DIR / "img00_segmentation_summary.csv", index=False)

    boundaries = find_boundaries(labels, mode="thick")
    overlay = np.array(img_display, dtype=float) / max(255, img_display.max())
    overlay[boundaries] = [1, 0.2, 0.2]

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.imshow(overlay)
    ax.set_axis_off()
    ax.set_title(f"img00 — Cellpose masks (n={n_cells})")
    fig.tight_layout()
    fig.savefig(OVERLAY_PATH, dpi=150, bbox_inches="tight")
    plt.close()

    fig, ax = plt.subplots(1, 1, figsize=(5, 3.5))
    ax.hist(areas, bins=min(50, max(10, n_cells // 5)), color="steelblue", edgecolor="white")
    ax.axvline(areas.mean(), color="red", ls="--", label=f"mean = {areas.mean():.0f} px²")
    ax.set_xlabel("Cell area (px²)")
    ax.set_ylabel("Count")
    ax.set_title("Cell area distribution")
    ax.legend()
    fig.tight_layout()
    fig.savefig(HIST_PATH, bbox_inches="tight")
    plt.close()

    return summary


if __name__ == "__main__":
    summary = main()
