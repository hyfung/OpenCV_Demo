import cv2, numpy
import threading

cap = cv2.VideoCapture(0)

W, H = 640, 480

cap.set(3,W)
cap.set(4,H)

_, frame = cap.read()
stop = False

def update_frame():
    global frame
    while True:
        _, frame = cap.read()
        if stop:
            exit()
        

thread = threading.Thread(target=update_frame)
thread.start()

while True:
    cv2.imshow("Frame", frame)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        stop = True
        thread.join()
        break
