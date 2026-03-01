import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# -------- IMAGE PATH --------
path = r"D:\CODING\DIP\LAB4\Sample images\note.tif"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found")
    exit()


# -------- BIT PLANE SLICING --------
bit_planes = []

for i in range(8):

    # Extract ith bit
    plane = (img >> i) & 1

    # Scale to 0-255 for visualization
    plane = plane * 255

    bit_planes.append(plane.astype(np.uint8))


# -------- SAVE BIT PLANES --------
folder = r"D:\CODING\DIP\LAB4\Sample images"

for i, plane in enumerate(bit_planes):

    cv2.imwrite(os.path.join(folder,f"bit_plane_{i}.tif"), plane)



# -------- DISPLAY IN ONE FRAME --------
plt.figure(figsize=(12,8))


# Original Image
plt.subplot(3,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')


# Bit Planes
for i in range(8):

    plt.subplot(3,3,i+2)

    plt.imshow(bit_planes[i], cmap='gray')

    plt.title(f"Bit Plane {i}")

    plt.axis('off')


plt.tight_layout()
plt.show()