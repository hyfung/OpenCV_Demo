import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="path to the video file", type=int, default=0)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['src'])

W,H = 640, 480
blur_radius = 1
bin_thresh = 0
bin_thresh_target = 0
C = 0
block_size = 11
cap.set(3,W)
cap.set(4,H)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

for i in range(0,4):
    cv2.namedWindow(titles[i])

def on_binthresh(val):
    global bin_thresh
    bin_thresh = val

def on_binthresh_target(val):
    global bin_thresh_target
    bin_thresh_target = val*255

def on_blocksize(val):
    global block_size
    block_size = val*2+3

def on_c(val):
    global C
    C = val

def on_blur(val):
    global blur_radius
    blur_radius = val*2+1

cv2.createTrackbar("Threshold", titles[1], 0, 255, on_binthresh)
cv2.createTrackbar("Target", titles[1], 0, 1, on_binthresh_target)
cv2.createTrackbar("Blocksize", titles[1], 0, 20, on_blocksize)
cv2.createTrackbar("C", titles[1], 0, 20, on_c)
cv2.createTrackbar("Blur", titles[0], 0, 25, on_blur)

while True:
    ret, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img,blur_radius)

    ret,th1 = cv2.threshold(img,bin_thresh,bin_thresh_target,cv2.THRESH_BINARY)

    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,block_size,C)

    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,block_size,C)


    images = [img, th1, th2, th3]

    for i in range(0,4):
        cv2.imshow(titles[i], images[i])

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
