import cv2, argparse
import numpy as np
import time

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="path to the video file", type=int, default=0)
args = vars(ap.parse_args())

blurVal = 1
WVal = 16
HVal = 0

def time_to_string() -> str:
    #20180914_234000
    return str(time.strftime('%Y%m%d_%H%M%S'))

def time_to_string_human() -> str:
    #2020-01-01 23:40:00
    return str(time.strftime('%Y-%m-%d %H:%M:%S'))

def on_blur_trackbar(val) -> None:
    global blurVal
    blurVal = 2*val+1

def on_W_trackbar(val) -> None:
    global WVal
    WVal = val

def on_H_trackbar(val) -> None:
    global HVal
    HVal = val

W = 640
H = 480
R = 60

cv2.namedWindow("Frame")
cv2.namedWindow("Gray")
cv2.createTrackbar("Blurness", "Frame", 0, 50, on_blur_trackbar)
cv2.createTrackbar("Height", "Frame", 0, H, on_H_trackbar)
cv2.createTrackbar("Width", "Frame", 0, W, on_W_trackbar)

cap = cv2.VideoCapture(args['src'])

out = cv2.VideoWriter('/home/jerry/'+str(time.strftime('%Y%m%d'))+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (W,H))

cap.set(3,W)
cap.set(4,H)
# cap.set(3,640)
# cap.set(4,480)

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame,(W,H))
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,time_to_string_human(),(WVal,HVal), font, 0.5,(0,255,0),1,cv2.LINE_AA)
    out.write(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('Gray', gray)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
