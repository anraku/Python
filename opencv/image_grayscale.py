import numpy as numpy
import cv2

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
