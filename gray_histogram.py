#!/usr/bin/python3
from matplotlib import pyplot as plt
import argparse
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="")
# args = vars(ap.parse_args())
#image = cv2.imread(args["image"])

while True:

    cap = cv2.VideoCapture(0)
    ret, image = cap.read()


    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    hist = cv2.calcHist([image], [0], None, [256], [0,256])

    plt.figure()
    plt.title("Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    
    
    cv2.imshow("Original", image)
    plt.show(33)
    cv2.waitKey(33)