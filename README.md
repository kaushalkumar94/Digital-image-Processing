# Digital Image Processing Labs

A collection of lab assignments for the Digital Image Processing course, implemented using MATLAB and Python (OpenCV, NumPy, Matplotlib).

**Author:** Kaushal Kumar — B.Tech CSE, UIET Panjab University

---

## Labs Overview

### Lab 1 — Introduction to MATLAB
Getting started with MATLAB for image processing: basic syntax, image I/O, and display.

---

### Lab 2 — Spatial Resolution & Bit Depth
- Custom downscaling and upscaling using averaging and bilinear interpolation
- MSE-based comparison between custom and OpenCV implementations
- Right-shift and 1-bit MSB extraction from grayscale images

**Sample images:** `Rose 1024x1024.tif`, `lena_gray_512.tif`, `Skull 374x452.tif`

---

### Lab 3 — Histograms & Pattern Images
- Histogram plotting and analysis of grayscale images
- Working with pattern images: checkerboard, horizontal, and vertical stripes

**Sample images:** `3. BATMAN.jpg`, `checkerboard_16x16.png`, `horizontal_16x16.png`, `vertical_16x16.png`

---

### Lab 4 — Intensity Transformations
- **Bit Plane Slicing** — decomposing images into 8 bit planes
- **Contrast Stretching** — linear normalization to full intensity range
- **Gamma Transformation** — power-law brightness correction
- **Histogram Equalization** — automatic contrast enhancement via CDF mapping
- **Log Transformation** — compressing high dynamic range images
- **Image Negatives** — pixel inversion for enhanced visual inspection

---

### Lab 5 — Spatial & Frequency Domain Filtering
- **Spatial filters:** Mean, Median, Max, Min (kernel sizes 3×3 to 11×11)
- **Sharpening:** Laplacian, Unsharp Masking, High-Boost Filtering
- **Frequency domain filters:** Ideal, Butterworth, and Gaussian Low/High Pass filters
- Repeated filtering and saturation analysis on image patches
- PCB image analysis using low-pass filters

---

## Tech Stack

| Tool | Usage |
|------|-------|
| MATLAB | Lab 1 |
| Python | Labs 2–5 |
| OpenCV | Image I/O, resizing, filtering |
| NumPy | Array operations |
| Matplotlib | Visualization |
| Jupyter Notebook | Lab 5 |

---

## References
- *Digital Image Processing* — Gonzalez & Woods, 4th Edition
- [OpenCV Documentation](https://docs.opencv.org)
- [NumPy Documentation](https://numpy.org/doc)
