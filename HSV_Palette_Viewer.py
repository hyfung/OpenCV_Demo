import numpy as np
import cv2

cv2.namedWindow("Viewer")

h = 0
s = 0
v = 0

def r_track(val):
    global h
    h = val

def g_track(val):
    global s
    s = val

def b_track(val):
    global v
    v = val

cv2.createTrackbar("H", "Viewer", 0, 255, r_track)
cv2.createTrackbar("S", "Viewer", 0, 255, g_track)
cv2.createTrackbar("V", "Viewer", 0, 255, b_track)

# for i in range(60):
while True:
    # h,s,v = 255,255,255    
    img = np.zeros((200,200,3), dtype='uint8')
    cv2.rectangle(img, (0,0), (199,199), (h,s,v), -1)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow("Viewer", img)
    print(h, img[0][0][2], img[0][0][1],)
    #print(img[0][0][0],img[0][0][1],img[0][0][2],)
    #print(h,s,v,)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        exit(0)
