#!/usr/bin/python3
import cv2, argparse, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=False, help="")
ap.add_argument("-s", "--src", help="Index of video source", type=int, default=0)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['src'])

ret, frame = cap.read()
print(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
cap.release()

CONV_FILTER = np.array([[1,0], [0,1]])