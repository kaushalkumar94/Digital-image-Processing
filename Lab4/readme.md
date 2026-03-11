# Digital Image Processing — Lab Manual

This document covers the theoretical concepts behind the fundamental image processing techniques implemented in this repository.

---

## Table of Contents

1. [Bit Plane Slicing](#1-bit-plane-slicing)
2. [Contrast Stretching](#2-contrast-stretching)
3. [Gamma Transformation](#3-gamma-transformation)
4. [Histogram Equalization](#4-histogram-equalization)
5. [Log Transformation](#5-log-transformation)
6. [Negative of an Image](#6-negative-of-an-image)

---

## 1. Bit Plane Slicing

A digital image is stored as a matrix of pixel values, where each pixel is represented by an 8-bit binary number ranging from 0 to 255. Bit plane slicing is the process of decomposing this image into its 8 individual bit layers, called bit planes.

Each bit plane isolates a single bit position across all pixels in the image. The most significant bit (MSB), which is bit plane 7, contributes the most to the overall appearance of the image and contains the dominant structural information. As we move towards lower-order planes, the contribution to visual quality decreases, and the lower planes (0, 1, 2) often resemble random noise.

This technique is useful in image compression, because the higher-order bit planes can often reconstruct a visually acceptable version of the original image on their own, allowing the lower planes to be discarded without significant perceptual loss. It is also used in watermarking, where information is hidden in the least significant bit planes without visibly affecting the image.

---

## 2. Contrast Stretching

Contrast stretching, also called normalization, is a simple image enhancement technique that improves the contrast of an image by expanding its pixel intensity range to span the full available range, typically 0 to 255.

Many real-world images suffer from poor contrast due to limitations in the imaging sensor or lighting conditions. In such images, the pixel intensities are confined to a narrow range, making the image appear dull or washed out. Contrast stretching addresses this by linearly remapping the minimum intensity value to 0 and the maximum intensity value to 255, with all intermediate values scaled proportionally.

The key idea is that the relative differences between pixel values are preserved — only the scale changes. This makes it a linear transformation, unlike histogram equalization which is non-linear. Contrast stretching works best when the image has a few dominant intensity values clustered in a narrow range, and it is particularly effective when the minimum and maximum pixel values are well-defined and not influenced by extreme outliers.

---

## 3. Gamma Transformation

Gamma transformation, also known as power-law transformation, is a non-linear intensity mapping technique used to correct the brightness of an image. It is defined by the relationship where the output intensity is proportional to the input intensity raised to the power of gamma (y).

When gamma is less than 1, the transformation maps darker input values to a wider range of output values, effectively brightening the image and bringing out detail in the shadows. When gamma is greater than 1, the opposite occurs — brighter regions are compressed, and the image appears darker. When gamma equals 1, the transformation is linear and produces no change.

This concept originates from the non-linear response of display devices such as CRT monitors and cameras, which do not reproduce intensity in a perfectly linear manner. Gamma correction is applied to compensate for this hardware behavior. In image processing, gamma transformation is widely used in medical imaging, satellite imagery, and any application where precise control over the tonal range of an image is required.

Different gamma values are applied to observe their effect on the same image, demonstrating how the technique can be tuned to brighten underexposed images or reduce glare in overexposed ones.

---

## 4. Histogram Equalization

A histogram of a grayscale image is a graphical representation that shows the frequency of each intensity value (0 to 255) across all pixels. It gives a global view of the tonal distribution in the image — whether it is predominantly dark, bright, or well-balanced.

Histogram equalization is an automatic contrast enhancement technique that redistributes pixel intensities so that the output histogram is approximately uniform, meaning all intensity levels are used with roughly equal frequency. This is achieved through a mathematical mapping derived from the cumulative distribution function (CDF) of the original histogram.

The process involves three steps. First, the histogram is computed to find how often each intensity value appears. Second, the cumulative distribution function is calculated by summing up the histogram values progressively. Third, each original pixel value is remapped to a new value using the CDF, scaled to the full intensity range.

The result is an image with enhanced global contrast where previously compressed intensity ranges are stretched out. Histogram equalization is especially effective for images that are overall too dark or too bright, and is widely applied in medical imaging, satellite image analysis, and document scanning. However, it can sometimes over-enhance noise or produce unnatural-looking results when the image already has a well-balanced histogram.

---

## 5. Log Transformation

Log transformation is a non-linear intensity transformation that applies the mathematical logarithm function to each pixel value in the image. It maps a narrow range of low-intensity values in the input to a wider range in the output, effectively brightening dark regions while compressing bright ones.

The transformation uses a scaling constant to ensure that the output values are normalized to the standard 0–255 range. This constant is derived from the maximum pixel value in the image so that the transformation adapts to the content of each specific image.

Log transformation is particularly useful when an image has a very wide dynamic range — meaning it contains both very dark and very bright regions simultaneously. In such cases, simply displaying the image would cause the dark details to be invisible. A practical and common application is visualizing the Fourier spectrum of an image, where the magnitude values span several orders of magnitude. Applying the log transform compresses this range into a displayable scale, making the frequency components visible.

The key characteristic of log transformation is that it is most sensitive at low intensity values, where small differences in input produce large differences in output. At higher intensities, the transformation becomes less sensitive, compressing the bright end of the spectrum.

---

## 6. Negative of an Image

The negative of an image is produced by inverting all pixel intensity values. For an 8-bit grayscale image, this means subtracting each pixel value from 255, so that dark pixels become bright and bright pixels become dark. The result is visually similar to a photographic negative.

This is one of the simplest point operations in image processing, where the output at each pixel depends only on the input at that same pixel, with no consideration of neighboring values.

The negative transformation is particularly valuable in medical imaging. For example, when examining digital X-rays or mammograms, certain subtle features — such as small calcifications or lesions — may be easier to detect against a dark background than a bright one. By inverting the image, radiologists can inspect the same content from a different visual perspective, potentially improving diagnostic accuracy.

It is also used in photographic art and document processing, where inverting the image can improve readability of certain types of content or produce visual effects.

---

## References

- *Digital Image Processing* — Rafael C. Gonzalez & Richard E. Woods (4th Edition)
- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
