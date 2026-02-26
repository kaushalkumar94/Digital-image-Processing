import cv2
import numpy as np
import matplotlib.pyplot as plt


# -------- LOAD IMAGE --------
path = r"D:\CODING\DIP\LAB4\Sample images\lena_gray_512.tif"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found")
    exit()


# -------- CONTRAST STRETCHING --------
def contrast_stretch(image):

    rmin = np.min(image)
    rmax = np.max(image)

    stretched = (image - rmin) / (rmax - rmin)

    stretched = stretched * 255

    return stretched.astype(np.uint8)



stretched_img = contrast_stretch(img)


# -------- SAVE OUTPUT --------
cv2.imwrite(
r"D:\CODING\DIP\LAB4\Sample images\lena_contrast_stretch.tif",
stretched_img
)


# -------- SHOW IN ONE FRAME --------
plt.figure(figsize=(10,5))


plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.axis('off')


plt.subplot(1,2,2)
plt.imshow(stretched_img,cmap='gray')
plt.title("Contrast Stretched")
plt.axis('off')


plt.tight_layout()
plt.show()