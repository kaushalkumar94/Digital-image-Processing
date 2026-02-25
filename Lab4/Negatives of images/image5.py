import cv2
import numpy as np

img = np.zeros((64,64), dtype=np.uint8)



points_1x1 = [(2,2),(2,6),(2,10),(2,14),(2,18)]

for r,c in points_1x1:
    img[r:r+1 , c:c+1] = 255


points_2x2 = [(8,2),(8,8),(8,14),(8,20)]

for r,c in points_2x2:
    img[r:r+2 , c:c+2] = 255


points_3x3 = [(16,2),(16,10),(16,18)]

for r,c in points_3x3:
    img[r:r+3 , c:c+3] = 255


points_h = [(26,2),(30,2),(34,2)]

for r,c in points_h:
    img[r:r+1 , c:c+3] = 255

points_v = [(26,20),(26,24),(26,28)]

for r,c in points_v:
    img[r:r+3 , c:c+1] = 255

cv2.imwrite("subparts.png", img)



image2 = 255 - img

cv2.imwrite("subparts_inverted.png", image2)


# Display
cv2.imshow("Original", img)
cv2.imshow("Inverted", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()