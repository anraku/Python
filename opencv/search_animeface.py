import sys
if len(sys.argv) < 2:
	print "Image not found"
	sys.exit(0)

import cv2
import numpy as np

cascade_path = "lbpcascade_animeface.xml"

image_path = sys.argv[1]

face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread(image_path, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.1, 3)

if len(face) > 0:
	for rect in face:
		cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
else:
	print "no face"

cv2.imwrite('detected_anime.jpg', img)

