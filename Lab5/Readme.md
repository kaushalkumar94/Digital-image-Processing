# Digital Image Processing - Lab 5

This repository contains implementations of various **Spatial and Frequency Domain Filtering** techniques using Python, OpenCV, and NumPy.

---

## Folder Structure

```
Lab5/
|-- sample images used/     # Input images
|-- output results/         # Output images
|-- spatial_domain_filtering.ipynb  # Main notebook
```

---

## Experiments Performed

---

### 1. Spatial Domain Filtering

**Filters Applied:**
- Mean Filter
- Median Filter
- Max Filter
- Min Filter

**Kernel Sizes:**
- 3x3, 5x5, 7x7, 9x9, 11x11

**Observations:**
- Mean filter smooths the image but blurs edges
- Median filter preserves edges better
- Max filter enhances bright regions
- Min filter enhances dark regions
- Larger kernel size results in more smoothing

---

### 2. Repeated Filtering and Saturation

**Process:**
- Extracted a 16x16 patch from the Lena image
- Applied filters repeatedly
- Measured difference between iterations

**Observations:**
- Mean filter leads to a uniform image over time
- Median filter preserves structure for longer
- Saturation occurs when the difference between iterations approaches zero

---

### 3. Sharpening Filters

**Filters Applied:**
- Laplacian Filter
- Unsharp Masking
- High-Boost Filtering

**Observations:**
- Laplacian enhances edges but increases noise
- Unsharp masking provides balanced sharpening
- High-boost filtering provides stronger enhancement

---

### 4. Frequency Domain Filtering

**Filters Implemented:**
- Ideal Low Pass / High Pass (ILPF / IHPF)
- Butterworth Low Pass / High Pass (BLPF / BHPF)
- Gaussian Low Pass / High Pass (GLPF / GHPF)

**Parameters:**
- Cutoff Frequency (D0) = 10
- Butterworth Order (n) = 2

**Observations:**
- ILPF causes ringing artifacts
- BLPF provides a smoother transition
- GLPF gives the best visual smoothing
- High pass filters enhance edges

---

### 5. PCB Image Analysis (Low Pass Filters)

**Filters Applied:**
- ILPF
- BLPF
- GLPF

**Parameters:**
- D0 = 10
- n = 1

**Observations:**
- ILPF causes excessive blur and artifacts
- BLPF provides moderate smoothing
- GLPF performs best among the low pass filters tested

---

## Key Concepts

- Spatial filtering operates directly on pixel values
- Frequency domain filtering works using the Fourier Transform
- Cutoff frequency controls the strength of filtering
- Gaussian filters are preferred due to their smooth frequency transition

---

## Conclusion

- Spatial and frequency domain filtering techniques were successfully implemented
- Gaussian filters provided the best overall performance
- Proper selection of kernel size and cutoff frequency is crucial
- PCB images require careful filtering to preserve fine details

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Sample Outputs

Add your output images here from the `output results/` folder.

---

## Author

**Kaushal Kumar**  
B.Tech CSE | UIET Panjab University  
Aspiring Data Scientist
