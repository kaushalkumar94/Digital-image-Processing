import cv2
import numpy as np

img = np.zeros((100, 100), dtype=np.uint8)

rows = [(0,20), (20,80), (80,100)]
cols = [(0,20), (20,80), (80,100)]

pattern = [
    [0,255,0],
    [255,0,255],
    [0,255,0]
]

for i in range(3):
    for j in range(3):

        r1, r2 = rows[i]
        c1, c2 = cols[j]

        # CENTER BLOCK (random 8-bit)
        if i == 1 and j == 1:

            img[r1:r2, c1:c2] = np.random.randint(
                0, 256,
                (r2-r1, c2-c1),
                dtype=np.uint8
            )
        else:
            img[r1:r2, c1:c2] = pattern[i][j]



image2 = 255 - img


# Save Images
cv2.imwrite("image_random_center.png", img)
cv2.imwrite("image_random_center_inverted.png", image2)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Inverted Image", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()