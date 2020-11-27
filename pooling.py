#!/usr/bin/python3
import cv2, numpy as np
import argparse

POOL_DIM = 4

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--continuous", required=False, action='store_true')
ap.add_argument("-f", "--file", required=False, help="")
ap.add_argument("-s", "--src", help="Index of video source", type=int, default=0)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['src'])

#Capturing a frame from camera
ret, frame = cap.read()
print(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
cap.release()

H,W = frame.shape[:2]

assert(H % POOL_DIM == 0)
assert(W % POOL_DIM == 0)

X_count = int(H / POOL_DIM)
Y_count = int(W / POOL_DIM)

print(X_count)
print(Y_count)

dst = np.zeros((X_count,Y_count), dtype="uint8")

#Pooling function, takes in a 2x2 array and return
def max_pooling_atomic(x):
    return max(x.flatten())

def max_pooling(mat):
    global dst
    for i in range(0,X_count):
        for j in range(0, Y_count):
            dst[i,j] = max_pooling_atomic(mat[i*POOL_DIM:i*POOL_DIM+1, j*POOL_DIM:j*POOL_DIM+1])

def avg_pooling_atomic(x):
    return max(x.flatten())

def avg_pooling(x):
    global dst
    for i in range(0,X_count):
        for j in range(0, Y_count):
            dst[i,j] = max_pooling_atomic(mat[i*2:i*2+1, j*2:j*2+1])


def main():
    global dst
    if args['continuous']:
        cap = cv2.VideoCapture(args['src'])
        while True:
            dst = np.zeros((X_count,Y_count), dtype="uint8")
            ret, frame = cap.read()

            max_pooling(frame)

            cv2.imshow("result", dst)
            cv2.waitKey(33)
        return
        
    max_pooling(frame)
    print(dst)
    cv2.imshow("result", dst)
    cv2.waitKey()

if __name__ == '__main__'
    main()