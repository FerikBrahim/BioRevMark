# Fingerprint Dataset

This directory contains fingerprint images used for biometric feature extraction and
authentication within the proposed watermarking framework.

## Dataset Description

Fingerprint samples are used exclusively to:
- Extract compact biometric signatures using the Improved BSIF (I-BSIF) operator
- Evaluate rotation invariance, robustness, and authentication accuracy
- Generate encrypted biometric watermarks

Representative dataset:
- **FVC2002 DB3**
  - Sensor: Precise Biometrics 100 SC
  - Resolution: 300 × 300 pixels
  - DPI: 500
  - Grayscale images

## Preprocessing

Before feature extraction, fingerprint images undergo:
- Grayscale normalization
- Block-wise orientation estimation (16 × 16)
- Orientation-adaptive BSIF filtering

Only **binary feature vectors** are retained after processing. Raw fingerprint images are
never embedded directly into medical images, ensuring privacy preservation.

## Privacy and Ethics

- All fingerprint data originates from publicly available benchmark datasets.
- No personal identity information is stored or inferred.
- The framework embeds **encrypted biometric features**, not raw biometric images.

## Important Note

Fingerprint images are **not distributed** with this repository by default.
Users should download the dataset independently from the official source and place
the images in this directory following the expected structure.

Refer to the project README for setup instructions.

