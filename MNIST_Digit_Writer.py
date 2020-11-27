import numpy as np
import cv2

draw = False
mat = np.zeros((28,28), dtype=np.uint8)

def mouse_cb(event, x, y, flags, param):
    """Mouse callback function to modify the mat"""
    global draw
    global mat

    if event == cv2.EVENT_LBUTTONDOWN:        
        draw = True
        print('drawing')

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        print('stop drawing')
        print(mat)

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            print(x,y)
            mat[y][x] = 255

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        mat = np.zeros((28,28), dtype=np.uint8)
        print("Mat cleared")
    

cv2.namedWindow('Drawboard')
cv2.setMouseCallback("Drawboard", mouse_cb)

while True:
    cv2.imshow('Drawboard', mat)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
