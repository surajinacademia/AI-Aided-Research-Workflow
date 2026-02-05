---
priority: high
description: Biological image analysis using Cellpose MCP and Python packages
---

# Biological Image Analysis

## Priority: Use MCP Tools First

**Always prioritize Cellpose MCP over custom code:**

- MCPs are GPU-accelerated and tested
- Only write scripts when explicitly requested
- Use Python packages for tasks MCPs don't cover

## Cellpose MCP Tools

**Segmentation:**

```python
# Server: "user-cellpose"
CallMcpTool("user-cellpose", "segment_cells_2d",
            {"image_path": "cells.tif",
             "model_type": "cyto3",  # or "nuclei", "cpsam"
             "diameter": 30})  # 0 = auto-estimate
```

**Models:** `cyto`/`cyto2`/`cyto3` (general cells), `nuclei` (nuclei only), `cpsam` (most accurate)

**Key parameters:** `model_type`, `diameter`, `flow_threshold`, `cellprob_threshold`, `channels`

**Image restoration:**

- `denoise_image` - Remove noise
- `deblur_image` - Restore blur
- `upsample_image` - Super-resolution
- `restore_and_segment` - Combined pipeline

**Utilities:** `estimate_cell_diameter`, `load_image_info`, `segment_cells_batch`, `list_available_models`

## Python Packages

**Use when MCPs don't cover your needs:**

### scikit-image

```python
from skimage.measure import regionprops
from skimage.filters import gaussian, threshold_otsu
from skimage.morphology import opening, closing

# Measure cells after segmentation
props = regionprops(masks)
for r in props:
    area, perimeter, eccentricity = r.area, r.perimeter, r.eccentricity
```

**Common functions:** `regionprops`, `gaussian`, `median`, `threshold_otsu`, morphology operations

### scipy.ndimage

```python
from scipy.ndimage import gaussian_filter, label

smoothed = gaussian_filter(image, sigma=2)
labeled, n = label(binary_mask)
```

### aicsimageio

```python
from aicsimageio import AICSImage

# Load proprietary formats (ND2, CZI, LIF, LSM)
img = AICSImage("data.nd2")
data = img.get_image_data("CZYX")
``` 

## Quick Reference

**When to use MCPs:**

- Cell/nuclei segmentation
- Denoise, deblur, upsample
- Batch processing

**When to write code:**

- Measurements (regionprops)
- Statistical analysis
- Custom filters
- Data aggregation
