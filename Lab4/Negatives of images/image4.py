import cv2
import numpy as np

img = np.zeros((100,100), dtype=np.uint8)

rows = [(0,20),(20,80),(80,100)]
cols = [(0,20),(20,80),(80,100)]

pattern = [
    [255,0,255],
    [0,None,0],
    [255,0,255]
]

# outer blocks
for i in range(3):
    for j in range(3):

        r1,r2 = rows[i]
        c1,c2 = cols[j]

        if pattern[i][j] is not None:
            img[r1:r2 , c1:c2] = pattern[i][j]


# center X pattern
center = np.zeros((60,60), dtype=np.uint8)

for i in range(60):
    for j in range(60):

        if j < i and j < (59-i):
            center[i,j] = 255
        elif j > i and j > (59-i):
            center[i,j] = 255

img[20:80 , 20:80] = center


inverted_img = 255 - img

cv2.imwrite("image4.png", img)
cv2.imwrite("inverted_image4.png", inverted_img)

cv2.imshow("Original", img)
cv2.imshow("Inverted", inverted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()