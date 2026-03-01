import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# POWER LAW TRANSFORMATION
def gamma_transform(image, alpha):

    image = image.astype(np.float32) / 255.0

    gamma_img = np.power(image, alpha)

    gamma_img = gamma_img * 255

    return np.uint8(gamma_img)



folder = r"D:\CODING\DIP\LAB4\Sample images"

images = [
    "cameraman.tif",
    "lena_gray_512.tif",
    "peppers_gray.tif",
    "rice.jpg"
]


alphas = [0.5, 1, 2]


plt.figure(figsize=(14,12))

plot_index = 1



for name in images:

    path = os.path.join(folder, name)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Cannot load:", name)
        continue


    # Original
    plt.subplot(4,4,plot_index)
    plt.imshow(img, cmap='gray')
    plt.title(f"Original : {name}")
    plt.axis('off')

    plot_index += 1


    # Gamma comparisons
    for alpha in alphas:

        gamma_img = gamma_transform(img, alpha)

        # Save output
        save_name = f"gamma_{alpha}_{name}"
        cv2.imwrite(os.path.join(folder, save_name), gamma_img)


        plt.subplot(4,4,plot_index)
        plt.imshow(gamma_img, cmap='gray')
        plt.title(f"α = {alpha}")
        plt.axis('off')

        plot_index += 1



plt.tight_layout()
plt.show()