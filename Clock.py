import cv2
import argparse
import numpy as np
import time

SIZE = (640,640,3)
CENTER = (SIZE[0]//2-1, SIZE[1]//2-1)

def time_now():
    #Access with
    #tm_hour
    #tm_min
    #tm_sec
    return time.localtime(time.time())

print(ORIGIN)

mat = np.zeros((640,640,3), dtype=np.uint8)

cv2.imshow("Clock", mat)
cv2.waitKey(0)
