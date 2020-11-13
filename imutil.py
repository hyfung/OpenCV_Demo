import numpy as np
import cv2
import math

def new_grayscale_frame(w,h):
    return np.zeros((h,w), dtype="uint8")

def new_bgr_frame(w,h):
    return np.zeros((h,w,3), dtype="uint8")

def new_unit_frame(w,h, value=1):
    return np.ones(h,w, dtype='uint8') * value

def d2r(d):
    return d * math.pi / 180

def r2d(r):
    return r / math.pi * 180

def translate(image, x, y):
    M = np.float32([[1,0,x], [0,1,y]])
    res = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return res

def rotate(image, center = None, scale = 0):
    h, w = image.shape[:2]
    if center is None:
        center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, degree, scale)
    res = cv2.warpAffine(image, M, (w,h))
    return res

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    h, w = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = height/float(h)
        dim = (int(w * r), height)
        
    if height is None:
        r = width/float(w)
        dim = (int(h * r), width)

    return cv2.resize(image, dim, interpolation = inter)

def horizontal_flip(image):
    return cv2.flip(image, 1)

def vertical_flip(image):
    return cv2.flip(image, 0)

def both_flip(image):
    return cv2.flip(image, -1)

def crop_image(image, x, y, w, h):
    return image[x:x+w, y,y+h]

def add(img_a, img_b):
    return cv2.add(img_a, img_b)

def subtract(img_a, img_b):
    return cv2.subtract(img_a, img_b)

def bitwise_and(img_a, img_b):
    return cv2.bitwise_and(img_a, img_b)

def bitwise_or(img_a, img_b):
    return cv2.bitwise_or(img_a, img_b)

def bitwise_xor(img_a, img_b):
    return cv2.bitwise_xor(img_a, img_b)

def bitwise_not(img_a):
    return cv2.bitwise_not(img_a)

def split(image):
    (b,g,r) = cv2.split(image)
    return (b,g,r)

#Combine 3 Grayscale mat into RGB
def merge(b,g,r):
    return cv2.merge([b,g,r])

'''
cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
'''

'''
cv2.calcHist(image, channel = [0,1,2], mask = MAT, histSize = 256, ranges = [0,256])
cv2.equalizeHist()
'''

