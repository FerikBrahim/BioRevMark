# ICRAMI-Biometric-Watermarking

**ICRAMI-Biometric-Watermarking** is a research-oriented Python framework implementing a
**blind, reversible, and biometric-driven medical image watermarking system**.
The project accompanies the research paper:

> *A Unified Biometric and Reversible Watermarking Framework for Secure Medical Image Authentication*

The framework integrates orientation-guided fingerprint feature extraction with
lightweight encryption and transform-domain watermarking to ensure **image integrity,
patient authentication, and privacy preservation** in telemedicine environments.

---

##  Key Features

- **Orientation-guided I-BSIF** fingerprint feature extraction  
- **FlexenTech permutation-based encryption** for biometric templates  
- **Blind and reversible watermarking** using Lifting Wavelet Transform (LWT)  
- **Adaptive spread-spectrum embedding** in mid-frequency subbands  
- **Robustness against signal-processing and geometric attacks**  
- **Low computational overhead**, suitable for real-time clinical workflows  

---

##  System Overview

1. Fingerprint images are processed using orientation-adaptive I-BSIF to generate
   compact, rotation-invariant binary feature vectors.
2. Biometric features are secured using FlexenTech lightweight permutation encryption.
3. The encrypted biometric watermark is embedded into medical images using
   spread-spectrum modulation in LWT subbands.
4. Blind extraction recovers the biometric watermark without access to the original image.
5. Exact reversibility is guaranteed through integer-to-integer LWT operations.

---

##  Repository Structure

```text
ICRAMI-Biometric-Watermarking/
│
├── data/
│   ├── medical_images/
│   │   ├── ct/
│   │   ├── mri/
│   │   ├── xray/
│   │   └── README.md
│   ├── fingerprints/
│   │   └── README.md
│
├── notebooks/
│   ├── 01_I-BSIF_Feature_Extraction.ipynb
│   ├── 02_FlexenTech_Analysis.ipynb
│   ├── 03_Watermark_Embedding.ipynb
│   ├── 04_Robustness_Tests.ipynb
│   └── 05_Results_Visualization.ipynb
│
├── src/
│   ├── features/
│   ├── encryption/
│   ├── watermarking/
│   └── evaluation/
│
├── README.md
└── LICENSE
