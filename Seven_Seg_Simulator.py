#!/usr/bin/python3

import cv2, numpy as np, math
import threading, time

clock = 0
stop = False

lock = threading.Lock()
RED = (0,0,255)
GREEN = (0,255,0)
GRAY = (128,128,128)

def originToDiagonal(x,y,N=5):
    return ((x-N,y-N),(x+N,y+N))

def incrementClock():
    global clock
    while True:
        lock.acquire()
        if stop:
            exit(1)
        clock += 1
        lock.release()
        print("t: ", clock)
        time.sleep(1)

class CircularButton():
    def __init__(self, x, y, r = 5, color = (255,255,255)):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.colorOn = (0,0,255)
        self.colorOff = (0,255,0)
        self.state = True

    def inRange(self, x, y):
        return math.sqrt((self.x-x)**2 + (self.y-y)**2) <= self.r

    def getColor(self):
        if self.state:
            return self.colorOn
        else:
            return self.colorOff

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

def mouse_cb(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(0,8):
            if buttons[i].inRange(x,y):
                if states[i] == 0:
                    states[i] = 1
                else:
                    states[i] = 0

buttons = []
states = [1,1,1,1,1,1,1,1]
SEGMENT = ["DP", "G", "F", "E", "D", "C", "B", "A"]
ANCHOR = [(85,70), (230,70), (85,195), (230,195), (85,320), (230,320)]

A = ((85, 70), (230,70))
B = ((230,70),(230,195))
C = ((230,195),(230,320))
D = ((85, 320), (230,320))
E = ((85, 320), (85, 195))
F = ((85,70), (85,195))
G = ((85, 195), (230,195))
DP = (270,315)

for i in range(0,8):
    buttons.append(CircularButton(40+60*i, 600, 20))

print(buttons)

t = threading.Thread(target=incrementClock, args=())
t.start()

while True:
    mat = np.zeros((640,640,3), dtype="uint8")
    cv2.line(mat, (0,500), (639,500), (0,255,0), 1)

    counter = 0
    for button in buttons:
        cv2.circle(img=mat, center=(button.x, button.y), radius=button.r, color=GREEN if states[counter] else GRAY, thickness=-5)
        cv2.circle(mat, (button.x, button.y), button.r, (180,180,180), 2)
        cv2.putText(mat, SEGMENT[counter], (button.x-10, button.y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
        # cv2.rectangle(img=mat, pt1=coord, pt2=(coord[0]+BUTTON_SIZE, coord[1]+BUTTON_SIZE), color=(255,255,255), thickness=-5)
        counter += 1

    val = (states[0] <<  7| states[1] << 6 | states[2] << 5| states[3] << 4| states[4] << 3| states[5] << 2| states[6] << 1| states[7])

    cv2.putText(mat, '%X' % val, (435,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
    # cv2.putText(mat, str(hex(~val)), (435,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)


    if states[7]:
        cv2.line(mat, A[0], A[1], (0,0,255), 10)
    if states[6]:
        cv2.line(mat, B[0], B[1], (0,0,255), 10)
    if states[5]:
        cv2.line(mat, C[0], C[1], (0,0,255), 10)
    if states[4]:
        cv2.line(mat, D[0], D[1], (0,0,255), 10)
    if states[3]:
        cv2.line(mat, E[0], E[1], (0,0,255), 10)
    if states[2]:
        cv2.line(mat, F[0], F[1], (0,0,255), 10)
    if states[1]:
        cv2.line(mat, G[0], G[1], (0,0,255), 10)
    if states[0]:
        cv2.circle(mat, DP, 10, (0,0,255), -1)

    for i in ANCHOR:
        # cv2.circle(img=mat, center=i, radius=10, color=(0,0,0), thickness=-1)
        cv2.rectangle(mat, originToDiagonal(i[0],i[1],10)[0], originToDiagonal(i[0],i[1],10)[1], color=(0,0,0), thickness=-1)

    cv2.namedWindow("Mat")
    cv2.setMouseCallback("Mat", mouse_cb)
    cv2.imshow("Mat", mat)
    key = cv2.waitKey(100) & 0xFF
    if key == ord("q"):
        stop = True
        exit(1)
    for i in range(0,8):
        if key == i+190:
            states[i] = ~states[i] + 2
    lock.acquire()
    print(clock)
    lock.release()

