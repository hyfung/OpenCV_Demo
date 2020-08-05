import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("Window")
cv2.createTrackbar("Modulus", "Window", 0,5, lambda x: None)

color_mode = True

mapping = {
    1: 255,
    2: 128,
    4: 64,
    8: 32,
    16: 16,
    32: 8,
    }

while True:
    ret, img = cap.read()

    if not color_mode:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img %= 2**cv2.getTrackbarPos("Modulus", "Window")
    img *= mapping[2**cv2.getTrackbarPos("Modulus", "Window")]
    cv2.imshow("Window", img)

    key = cv2.waitKey(33) & 0xFF

    print(key)

    if key == ord('c'):
        color_mode = not color_mode
    elif key == ord('a'):
        pos = cv2.getTrackbarPos("Modulus", "Window")
        cv2.setTrackbarPos("Modulus", "Window", pos-1)
    elif key == ord('d'):
        pos = cv2.getTrackbarPos("Modulus", "Window")
        cv2.setTrackbarPos("Modulus", "Window", pos+1)
    elif key == ord('q'):
        cv2.destroyAllWindows()
        exit(1)
