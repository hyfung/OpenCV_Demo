#!/usr/bin/python3
import cv2
import argparse
import numpy as np
import imutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,)
args = vars(ap.parse_args())
mat = cv2.imread(args["image"])
mat = imutil.resize(mat, height=640)

origin = mat

mat = cv2.GaussianBlur(mat, (5,5), 1)
mat = cv2.cvtColor(mat, cv2.COLOR_BGR2HSV)

mat_hsv = cv2.split(mat)

# dst_up = np.hstack([cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY), mat_hsv[0]] )
# dst_down = np.hstack([mat_hsv[1], mat_hsv[2]])
# dst = np.vstack([dst_up, dst_down])


cv2.imshow("H", mat_hsv[0])
cv2.imshow("S", mat_hsv[1])
cv2.imshow("V", mat_hsv[2])

# cv2.imshow("dst", dst)
cv2.imshow("original", mat)
cv2.waitKey(0)
