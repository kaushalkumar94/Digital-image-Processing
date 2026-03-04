import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def gamma_transform(image, gamma):

    norm = image.astype(np.float32) / 255.0

    gamma_img = np.power(norm, gamma)

    gamma_img = gamma_img * 255

    return np.uint8(gamma_img)



folder = r"D:\CODING\DIP\LAB4\Sample images"

images = [
    "cameraman.tif",
    "lena_gray_512.tif",
    "peppers_gray.tif",
    "rice.jpg"
]


gamma_values = [0.3, 0.5, 1, 1.5, 2.5]


plt.figure(figsize=(18,12))

plot_index = 1

rows = len(images)
cols = len(gamma_values) + 1   # +1 for Original


for name in images:

    path = os.path.join(folder, name)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Cannot load:", name)
        continue


    # Original Image
    plt.subplot(rows, cols, plot_index)

    plt.imshow(img, cmap='gray')
    plt.title(f"Original\n{name}")
    plt.axis('off')

    plot_index += 1


    # Gamma Images
    for gamma in gamma_values:

        gamma_img = gamma_transform(img, gamma)


        # Save Output
        save_name = f"gamma_{gamma}_{name}"

        cv2.imwrite(os.path.join(folder, save_name), gamma_img)


        plt.subplot(rows, cols, plot_index)

        plt.imshow(gamma_img, cmap='gray')

        plt.title(f"γ = {gamma}")

        plt.axis('off')

        plot_index += 1


plt.tight_layout()
plt.show()