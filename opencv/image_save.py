#coding: utf-8

import numpy as np
import cv2

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('result', img)

# key入力を受け付ける
key = cv2.waitKey(0)

if key == 27: #escの処理
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite('grayscale_image.png', img)
	cv2.destroyAllWindows()

