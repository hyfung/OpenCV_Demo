import cv2, argparse
import numpy as np
import time

class rectangle():
    def __init__(self, x, y, w, h):
        pass
   

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="path to the video file", type=int, default=0)
ap.add_argument("-f", "--file", help="file name to save to", type=str)
args = vars(ap.parse_args())

blurVal = 1
WVal = 0
HVal = 0

def time_to_string():
    """
    Returns a string of current time suitable for filenames
    20180914_234000
    """
    return str(time.strftime('%Y%m%d_%H%M%S'))

def time_to_string_human():
    """
    Returns a human readible string of current time
    2018-09-14 23:40:00
    """
    return str(time.strftime('%Y-%m-%d %H:%M:%S'))

W = 1280
H = 720
R = 60

cv2.namedWindow("Frame")
cap = cv2.VideoCapture(args['src'])

cap.set(3,640)
cap.set(4,480)

_, last = cap.read()
last = cv2.cvtColor(last, cv2.COLOR_BGR2GRAY)

while(True):
    ret, frame = cap.read()
    frame = cv2.blur(frame, (blurVal,blurVal))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Frame',cv2.absdiff(gray,last))
    last = gray
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
