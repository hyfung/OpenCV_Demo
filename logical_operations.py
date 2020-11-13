import numpy as np
import cv2, time

cap = cv2.VideoCapture(0)

RET, FRAME = cap.read()
FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    xor = cv2.bitwise_xor(frame,FRAME)

    and_ = cv2.bitwise_and(frame,FRAME)

    or_ = cv2.bitwise_or(frame, FRAME)

    cv2.imshow("xor", xor)
    cv2.imshow("and", and_)
    cv2.imshow("or", or_)

    if cv2.waitKey(33) & 0xFF == ord('x'):
        RET, FRAME = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
