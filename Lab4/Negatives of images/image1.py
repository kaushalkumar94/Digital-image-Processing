import cv2
import numpy as np

# Create black image (100x100)
img = np.zeros((100, 100), dtype=np.uint8)

# Define regions
rows = [(0,20), (20,80), (80,100)]
cols = [(0,20), (20,80), (80,100)]

# Pattern matrix
# 0 = Black , 255 = White
pattern = [
    [0,   255, 0],
    [255, 0,   255],
    [0,   255, 0]
]

# Fill image
for i in range(3):
    for j in range(3):
        r1, r2 = rows[i]
        c1, c2 = cols[j]
        img[r1:r2, c1:c2] = pattern[i][j]

# Save image
cv2.imwrite("image1.png", img)

# Display image
cv2.imshow("image1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Invert image
inverted_img = 255 - img

# Save inverted image
cv2.imwrite("image1_inverted.png", inverted_img)

# Display
cv2.imshow("Inverted Image", inverted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

