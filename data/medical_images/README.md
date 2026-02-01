# Medical Image Datasets

This directory contains representative medical images used to evaluate the proposed
biometric-based reversible watermarking framework. The datasets span multiple imaging
modalities and anatomical regions to ensure robustness, generalizability, and clinical
relevance.

## Modalities

### 📂 ct/
Computed Tomography (CT) images, primarily brain scans, used to evaluate watermark
imperceptibility and robustness in high-contrast anatomical structures.

Typical characteristics:
- Resolution: 512 × 512
- Grayscale
- High structural detail

Representative sources:
- Kaggle CT-to-MRI CycleGAN Dataset
- Brain tumor CT images

---

### 📂 mri/
Magnetic Resonance Imaging (MRI) scans used to assess performance under complex soft-tissue
textures and varying intensity distributions.

Typical characteristics:
- Resolution: 512 × 512
- Grayscale
- High intra-class variability

Representative sources:
- Brain MRI datasets
- Skeletal MRI from HBFMID

---

### 📂 xray/
X-ray radiographs used to evaluate robustness in low-contrast and noisy imaging conditions,
which are common in clinical environments.

Typical characteristics:
- Variable resolution
- Grayscale
- Low contrast with structural overlap

Representative sources:
- NIH Chest X-ray14 Dataset
- Human Bone Fractures Multi-modal Image Dataset (HBFMID)

---

## Usage Notes

- Images in this repository are provided **for research and reproducibility purposes only**.
- All datasets originate from publicly available sources.
- No patient-identifiable metadata is included.
- Images may be resized or normalized during preprocessing.

For exact dataset sources and citations, refer to the **Experimental Setup** section of the
associated research paper.

