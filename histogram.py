import cv2
import numpy as np
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="")
# args = vars(ap.parse_args())
#image = cv2.imread(args["image"])

cap = cv2.VideoCapture(0)
ret, image = cap.read()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)

cv2.imshow("Histogram equalization", np.hstack([gray, eq]))

# # hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title("Histogram")
# plt.xlabel("Bins")
# plt.ylabel("Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# cv2.imshow("Original", image)
# plt.show()

cv2.waitKey(0)