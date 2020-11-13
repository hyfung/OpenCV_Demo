import cv2
import numpy

RED = (0,255,0)
ox,oy=300,300
axe1 = 200
axe2 = 200
start_angle = 0
end_angle = 360
rotation = 0

def axe1_cb(val):
    global axe1
    axe1 = val

def axe2_cb(val):
    global axe2
    axe2 = val

def start_angle_cb(val):
    global start_angle
    start_angle = val

def end_angle_cb(val):
    global end_angle
    end_angle = val

def rotation_cb(val):
    global rotation
    rotation = val


cv2.namedWindow('img')

cv2.createTrackbar("Axis 1", "img", axe1, 200, axe1_cb)
cv2.createTrackbar("Axis 2", "img", axe2, 200, axe2_cb)
cv2.createTrackbar("Start Angle", "img", start_angle, 360, start_angle_cb)
cv2.createTrackbar("End Angle", "img", end_angle, 360, end_angle_cb)
cv2.createTrackbar("Rotation", "img", rotation, 360, rotation_cb)

while True:
    img = numpy.zeros((640,640,3), dtype='uint8')
    cv2.ellipse(img, (ox,oy), (axe1,axe2), rotation, start_angle, end_angle, RED, thickness=1, lineType=8, shift=0)
    cv2.imshow('img', img)
    cv2.waitKey(33)