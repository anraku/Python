#coding: utf-8
from __future__ import division
import sys
if len(sys.argv) < 2:
	print "Image not found"
	sys.exit(0)
movie_path = sys.argv[1]

import cv2
import os
import shutil

def main():
	cascade_path = "lbpcascade_animeface.xml"
	face_cascade = cv2.CascadeClassifier(cascade_path)

	video = cv2.VideoCapture(movie_path)

	fps = video.get(cv2.CAP_PROP_FPS)
	end = video.get(cv2.CAP_PROP_FRAME_COUNT)

	#画像を保存するディレクトリを作成
	path = os.path.splitext(movie_path)
	dir_path = path[0] + '_face'
	if os.path.isdir(dir_path):
		shutil.rmtree(dir_path)
	os.mkdir(dir_path)

	frame_count = 0
	i = 0
	while video.isOpened():
		frame_count = frame_count + 1
		progress_phase = 0
		progress = (frame_count / end) * 100
		if progress > progress_phase:
			progress_phase = int(progress)
			sys.stdout.write("\r%d" % progress + "%¥n")
    		sys.stdout.flush()

		success, frame = video.read()
		if not success:
			break

		if frame_count%10 is 0:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			face = face_cascade.detectMultiScale(gray, 1.1, 3)
			if len(face) > 0:
				for rect in face:
					#顔だけ切り出して保存
					x = rect[0]
					y = rect[1]
					width = rect[2]
					height = rect[3]
					dst = frame[y:y+height, x:x+width]
					new_image_path = dir_path + '/' + "image"+str(i) + ".jpg";
					print new_image_path
					cv2.imwrite(new_image_path, dst)
					i += 1

if __name__ == '__main__':
	main()