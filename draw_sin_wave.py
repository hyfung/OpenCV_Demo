import math, cv2, numpy as np

t = 0

frame = np.ones((600,800,3), dtype='uint8') * 255
cv2.line(frame, (0,300), (799,300), (255,255,255))
cv2.imshow("Main", frame)
# cv2.waitKey()

thickness = 1
while t < 800:
    # frame = np.zeros((600,600,3), dtype='uint8')
    cv2.circle(frame, (t, int(300 + 200 * math.sin((t-120) * math.pi / 180))),thickness, (0,0,255), -1)
    cv2.circle(frame, (t, int(300 + 200 * math.sin(t) * math.pi / 180))),thickness, (0,255,0), -1)
    cv2.circle(frame, (t, int(300 + 200 * math.sin((t+120) * math.pi / 180))),thickness, (255,0,0), -1)
    # r = 128 + 255 * math.sin((t-120) * math.pi / 180)
    # g = 128 + 255 * math.sin((t) * math.pi / 180)
    # b = 128 + 255 * math.sin((t+120) * math.pi / 180)
    # cv2.rectangle(frame, (0,0), (275,275), (b,g,r), -1)
    # cv2.rectangle(frame, (275,0), (300,100), (b,0,0), -1)
    # cv2.rectangle(frame, (275,100), (300,200), (0,g,0), -1)
    # cv2.rectangle(frame, (275,200), (300,300), (0,0,r), -1)
    cv2.imshow("rect", frame)
    t += 1
    cv2.waitKey(10)
