import cv2
import numpy as np

# Bitwise Operations
image = cv2.imread("../data/road.png")
height, width, depth = image.shape

M = np.ones([height, width, depth], dtype="uint8") * 100

added = cv2.add(image, M)

cv2.imshow("added", added)
cv2.waitKey()
cv2.destroyAllWindows()

subtracted = cv2.subtract(M, image)
M = np.ones(image.shape, dtype="uint8") * 75

# Image Blending
img1 = cv2.imread("../data/road.png")
print(img1.shape)

cap = cv2.VideoCapture("../data/city/trm.169.007.avi")
_, img2 = cap.read()
cap.release()

# images have to be of the same size to be added, so we resize them

img1 = cv2.resize(img1, (300, 400))
img2 = cv2.resize(img2, (300, 400))

# blend the images
result = cv2.addWeighted(img1, 0.25, img2, 0.75, 0)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
