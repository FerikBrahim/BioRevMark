import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Helper to add a box with text
def add_box(ax, text, xy, boxstyle="round,pad=0.3", **kwargs):
    box = FancyBboxPatch((xy[0]-0.4, xy[1]-0.2), 0.8, 0.4,
                         boxstyle=boxstyle, mutation_scale=0.02*72,
                         linewidth=1, **kwargs)
    ax.add_patch(box)
    ax.text(xy[0], xy[1], text, ha='center', va='center', fontsize=9)
    return box

# Helper to add an arrow
def add_arrow(ax, xy_from, xy_to, **kwargs):
    arrow = FancyArrowPatch(xy_from, xy_to, arrowstyle='->', mutation_scale=10, linewidth=1, **kwargs)
    ax.add_patch(arrow)
    return arrow

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 6)
ax.axis('off')

# Define coordinates for boxes
coords = {
    "Fingerprint": (0, 5),
    "BSIF": (2, 5),
    "FV": (4, 5),
    "Encrypt": (6, 5),
    "W_enc": (8, 5),
    "Medical": (0, 1),
    "LWT": (2, 1),
    "Select": (4, 1),
    "Spread": (6, 3),
    "Inverse": (7, 1),
    "Watermarked": (8.5, 1)
}

# Add boxes
add_box(ax, "Fingerprint\nImage", coords["Fingerprint"])
add_box(ax, "BSIF Feature\nExtraction", coords["BSIF"])
add_box(ax, "Feature Vector\n(FV)", coords["FV"])
add_box(ax, "Flexentech\nEncryption", coords["Encrypt"])
add_box(ax, "Encrypted\nWatermark\nBits (W_enc)", coords["W_enc"])

add_box(ax, "Medical\nImage", coords["Medical"])
add_box(ax, "LWT\nDecomposition", coords["LWT"])
add_box(ax, "Select LH &\nHL Coefficients", coords["Select"])

add_box(ax, "Spread Spectrum\nEmbedding\n(α, PN with K)", coords["Spread"])
add_box(ax, "Inverse\nLWT", coords["Inverse"])
add_box(ax, "Watermarked\nMedical Image", coords["Watermarked"])

# Add arrows for upper branch
add_arrow(ax, coords["Fingerprint"], coords["BSIF"])
add_arrow(ax, coords["BSIF"], coords["FV"])
add_arrow(ax, coords["FV"], coords["Encrypt"])
add_arrow(ax, coords["Encrypt"], coords["W_enc"])

# Add arrows for lower branch
add_arrow(ax, coords["Medical"], coords["LWT"])
add_arrow(ax, coords["LWT"], coords["Select"])

# Connect branches to Spread
add_arrow(ax, coords["W_enc"], coords["Spread"])
add_arrow(ax, coords["Select"], coords["Spread"])

# From Spread to Inverse to Watermarked
add_arrow(ax, coords["Spread"], coords["Inverse"])
add_arrow(ax, coords["Inverse"], coords["Watermarked"])

plt.tight_layout()
plt.show()
