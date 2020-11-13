#!/usr/bin/python3
import cv2, numpy as np
from io import BytesIO

cap = cv2.VideoCapture(0)

ret, img = cap.read()
# cv2.imwrite('test.jpg', img)
cap.release()

encoded_img = np.array(cv2.imencode('.jpg', img)[1])

# print(encoded_img.tostring())

f = BytesIO()
f.write(encoded_img)
f.seek(0)
print(f.read())