import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()

#image = cv2.imread("test.jpg")

#Output datatype: fp64
#Black-to-White: Positive
#White-to-Black: Negative
    lap = cv2.Laplacian(image, cv2.CV_64F)

#Convert fp64 to uint8
    lap = np.uint8(np.absolute(lap))

#Show the result matrix
    cv2.imshow("Laplacian", lap)
    cv2.waitKey(33)

