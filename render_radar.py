import cv2, numpy as np, math
from time import sleep

height, width = (800, 800)
center = (width//2, height//2)
radius, theta = 400, 0

def r2d(radian):
    return radian / math.pi * 180

def d2r(degree):
    return degree / 180 * math.pi

#Polar to cartesian conversion
def p2c(r, theta):
    return (r * math.cos(d2r(theta))), (r * math.sin(d2r(theta)))

#Polar to cartesian conversion in integer
def p2c_int(r, theta):
    return int(r * math.cos(d2r(theta))), int(r * math.sin(d2r(theta)))

#Cartesian to polar
def c2p(x,y):
    theta = 0;
    if x > 0 and y > 0: #Quadrant I
        theta = 0;
    elif x < 0: #Quadrant II,III
        theta = 180;
    elif x > 0 and y < 0: #Quadrant IV
        theta = 360;
    theta += r2d(math.atan(y/x))
    return (math.sqrt(x**2 + y**2), theta)

#This function will create our backdrop
def base_canvas():
    mat = np.zeros((height, width, 3), dtype='uint8')
    cv2.line(mat, (0,height//2), (width-1, height//2), (255,255,255))
    cv2.line(mat, (width//2,0), (width//2, height-1), (255,255,255))
    cv2.circle(mat, center, 100, (255,255,255))
    cv2.circle(mat, center, 200, (255,255,255))
    cv2.circle(mat, center, 300, (255,255,255))
    cv2.circle(mat, center, 400, (255,255,255))
    return mat

def mimic_360_radar():
    while True:
        for theta in range(0,359,5):
            mat = base_canvas()
            x,y = p2c_int(400,theta)
            cv2.line(mat, center, (x+width//2, y+height//2), (0,255,0), 3)
            cv2.imshow("Radar", mat)
            cv2.waitKey(15)

def mimic_front_radar():
    while True:
        for theta in range(180, 360, 5):
            theta = abs(theta)
            mat = base_canvas()
            x,y = p2c_int(400, theta)
            cv2.line(mat, center, (x+width//2, y+height//2), (0,255,0), 3)
            cv2.imshow("Radar", mat)
            cv2.waitKey(15)

        for theta in range(360, 180, -5):
            theta = abs(theta)
            mat = base_canvas()
            x,y = p2c_int(400, theta)
            cv2.line(mat, center, (x+width//2, y+height//2), (0,255,0), 3)
            cv2.imshow("Radar", mat)
            cv2.waitKey(15)

mimic_front_radar()
