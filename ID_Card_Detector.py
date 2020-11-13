import cv2, argparse, numpy as np

W,H = 640,480

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="Index of video source", type=int, default=0)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['src'])

cap.set(4, W)
cap.set(3, H)

cv2.namedWindow("Frame")
cv2.namedWindow("Cropped")


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ret, thresh_H = cv2.threshold(hsv[:,:,0], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, thresh_S = cv2.threshold(hsv[:,:,1], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(thresh_H + thresh_S, kernel, iterations = 1)
    cv2.imshow('dilation', dilation)

    (_, contours, hierarchy) = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('thresh', thresh_H + thresh_S)

    cv2.imshow("Frame", frame)
    # cv2.imshow("Cropped", frame)
    cv2.waitKey(33)

cap.release()
