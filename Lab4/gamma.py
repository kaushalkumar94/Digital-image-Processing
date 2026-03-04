import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# GAMMA TRANSFORMATION
def gamma_transform(image, gamma):

    # Normalize image
    norm = image.astype(np.float32) / 255.0

    # Apply gamma
    gamma_img = np.power(norm, gamma)

    # Back to 0-255
    gamma_img = gamma_img * 255

    return np.uint8(gamma_img)



folder = r"D:\CODING\DIP\LAB4\Sample images"

images = [
    "cameraman.tif",
    "lena_gray_512.tif",
    "peppers_gray.tif",
    "rice.jpg"
]


gamma_value = .5   # Change gamma here if needed


plt.figure(figsize=(12,10))

plot_index = 1


for name in images:

    path = os.path.join(folder, name)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Cannot load:", name)
        continue


    gamma_img = gamma_transform(img, gamma_value)


    # Save image
    save_name = f"gamma_{gamma_value}_{name}"

    cv2.imwrite(os.path.join(folder, save_name), gamma_img)


    # Original
    plt.subplot(4,2,plot_index)
    plt.imshow(img, cmap='gray')
    plt.title(f"Original : {name}")
    plt.axis('off')

    plot_index += 1


    # Gamma Image
    plt.subplot(4,2,plot_index)
    plt.imshow(gamma_img, cmap='gray')
    plt.title(f"Gamma = {gamma_value}")
    plt.axis('off')

    plot_index += 1


plt.tight_layout()
plt.show()