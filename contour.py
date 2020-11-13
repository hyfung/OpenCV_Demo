import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="path to the video file", type=int, default=0)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['src'])
cap.set(3,640)
cap.set(4,480)

while True:
    #Get image feed
    ret, im = cap.read()

    #Convert to a gray image
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    imgray = cv2.GaussianBlur(imgray, (5,5), 0)
    imgray = cv2.Canny(imgray, 30, 150)

    #Convert to binary image
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)

    #Find contour from binary image
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        M = cv2.moments(c)

        #
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.circle(im, (x,y), 3, (127,0,0), 2)
        cv2.circle(im, (x+w,y), 3, (127,0,0), 2)
        cv2.circle(im, (x,y+h), 3, (127,0,0), 2)
        cv2.circle(im, (x+w,y+h), 3, (127,0,0), 2)

        # new = im[x:x+w,y:y+h]

        # cv2.imshow("new", new)
        # cv2.waitKey(0)

        #
        #Box is an array with 4 coordinates
        box = cv2.minAreaRect(c)
        box = np.int0(cv2.boxPoints(box))
        cv2.drawContours(im, [box], -1, (0,0,255), 2)

        #
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        cv2.circle(im, (int(x), int(y)), int(radius), (255,0,0), 2)

        # #
        # ellipse = cv2.fitEllipse(c)
        # cv2.ellipse(im, ellipse, (127,0,0), 2)

        try:
            cX = int(M['m10']/M['m00'])
            cY = int(M['m01']/M['m00'])
            cv2.circle(im, (cX,cY), 10, (1,227,254), -1)
        except ZeroDivisionError:
            pass


    #Draw contour on color image
    # cv2.drawContours(im, contours, -1, (0,255,0), 3)
    # cv2.drawContours(imgray, contours, -1, (255,255,255), 2)

    cv2.imshow('im2', im2)
    cv2.imshow('gray', imgray)
    cv2.imshow('im', im)

    # for contour in contours:
    #     print(contour)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
