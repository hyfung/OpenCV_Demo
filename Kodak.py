import cv2
import numpy as np
import time

def time_to_string():
    #20180914_234000
    return str(time.strftime('%Y%m%d_%H%M%S'))

def time_to_string_human():
    #20180914_234000
    return str(time.strftime('%Y-%m-%d %H:%M:%S'))

cap = cv2.VideoCapture(1)
cap.set(3,1920)
cap.set(4,1080)
# cap.set(3,640)
# cap.set(4,480)

while(True):
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,time_to_string_human(),(0,20), font, 0.5,(0,255,0),1,cv2.LINE_AA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('gray', gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
