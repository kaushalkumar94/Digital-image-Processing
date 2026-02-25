import cv2
img = cv2.imread(
    r"D:\CODING\DIP\LAB4\Sample images\Fig0304(a)(breast_digital_Xray).tif",
    cv2.IMREAD_GRAYSCALE
)
if img is None:
    print("Image not found!")
    exit()

image2 = 255 - img
cv2.imwrite(
    r"D:\CODING\DIP\LAB4\image2.tif",
    image2
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Image2 (Inverted)", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()