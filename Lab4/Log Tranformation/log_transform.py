import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def log_transform(image):

    image = image.astype(np.float32)

    c = 255 / np.log(1 + np.max(image))

    log_image = c * np.log(1 + image)

    return np.array(log_image, dtype=np.uint8)



folder = r"D:\CODING\DIP\LAB4\Sample images"

images = [
    "cameraman.tif",
    "lena_gray_512.tif",
    "peppers_gray.tif",
    "rice.jpg"
]


plt.figure(figsize=(12,10))

plot_index = 1


for name in images:

    path = os.path.join(folder, name)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Cannot load:", name)
        continue


    log_img = log_transform(img)


    # Save Output
    save_name = f"log_{name}"
    cv2.imwrite(os.path.join(folder, save_name), log_img)


    # Original Image
    plt.subplot(4,2,plot_index)
    plt.imshow(img, cmap='gray')
    plt.title(f"Original : {name}")
    plt.axis('off')

    plot_index += 1


    # Log Image
    plt.subplot(4,2,plot_index)
    plt.imshow(log_img, cmap='gray')
    plt.title(f"Log Transform : {name}")
    plt.axis('off')

    plot_index += 1


plt.tight_layout()
plt.show()