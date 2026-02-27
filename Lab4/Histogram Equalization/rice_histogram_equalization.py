#get the histogram of image using custom function then equalize it too

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(image):

    hist = np.zeros(256, dtype=int)

    for pixel in image.flatten():
        hist[pixel] += 1

    return hist


def histogram_equalization(image):

    height, width = image.shape
    total_pixels = height * width

    hist = [0]*256

    for i in range(height):
        for j in range(width):
            hist[image[i,j]] += 1


    pdf = [h/total_pixels for h in hist]


    cdf = [0]*256
    cdf[0] = pdf[0]

    for i in range(1,256):
        cdf[i] = cdf[i-1] + pdf[i]


    equalization_map = [int(c*255) for c in cdf]


    equalized = np.zeros_like(image)

    for i in range(height):
        for j in range(width):

            equalized[i,j] = equalization_map[image[i,j]]

    return equalized



img = cv2.imread(
    r"D:\CODING\DIP\LAB4\Sample images\rice.jpg",
    cv2.IMREAD_GRAYSCALE
)


equalized_img = histogram_equalization(img)



hist_original = histogram(img)
hist_equalized = histogram(equalized_img)



plt.figure(figsize=(12,8))


# Original Image
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')


# Equalized Image
plt.subplot(2,2,2)
plt.imshow(equalized_img, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')


# Original Histogram
plt.subplot(2,2,3)
plt.bar(range(256), hist_original)
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")


# Equalized Histogram
plt.subplot(2,2,4)
plt.bar(range(256), hist_equalized)
plt.title("Equalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")


plt.tight_layout()
plt.show()
