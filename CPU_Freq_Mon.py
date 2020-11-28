import cv2
import numpy
import math
import time
import subprocess



target = (300,200)

center = (300,300)
axes = (100,100)
angle = 180
startAngle = 0 + 60
endAngle = 180 - 60
color = (255,255,255)
thickness = 3

def hsv2rgb(val, min, max):
    # val = 
    pixel = np.array([val, 255, 255], dtype=uint8)
    pixel = cv2.cvtColor(pixel, cv2.COLOR_HSV2BGR)


class Gauge():
    WHITE = (255,255,255)

    def __init__(self, center, length, theta, thickness=3):
        self.center = center
        self.length = length
        #self.theta = theta
        self.minTheta = -theta
        self.maxTheta = theta
        self.interval = 2*theta
        
        self.val = 0 #Val: from 0 to 100
        self.needleThickness = 1
        self.gaugeThickness = 2
        pass

    def get_color(self):
        RED = 255 if self.val < 50 else 255 - int(self.val/50*255)
        GREEN = int(self.val/50 * 255) if self.val < 50 else 255
        return (0,GREEN,RED)

    def val_to_theta(self):
        return (self.val-50)/50 * self.maxTheta

    def draw_on(self, img):
        cv2.line(img,
            self.center,
            (
                int(self.center[0]
                    +self.length*math.sin(math.radians(self.val_to_theta()))
                    ),
                int(self.center[1]
                    -self.length*math.cos(math.radians(self.val_to_theta())))
                    ),
            self.get_color(),
            self.needleThickness
            )
        cv2.ellipse(img, self.center, (self.length, self.length), 270, self.minTheta, self.maxTheta, self.WHITE, self.gaugeThickness)
        cv2.circle(img, self.center, 4, (128,128,128), -1)
        
gauges = [
        Gauge((100,150), 100, 30),
        Gauge((250,150), 100, 30),
        Gauge((400,150), 100, 30),
        Gauge((550,150), 100, 30),
        Gauge((700,150), 100, 30),
        Gauge((850,150), 100, 30),
        Gauge((1000,150), 100, 30),
        Gauge((1150,150), 100, 30),
        ]

while True:
    img = numpy.zeros((250,1400,3), dtype='uint8')
    cv2.putText(img, "CPU Frequency Monitor", (10,25), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 1, cv2.LINE_AA, False)
    cv2.putText(img, "Core 0", (70, 190), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, "Core 1", (220,190), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, "Core 2", (370,190), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, "Core 3", (520,190), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 255), 1, cv2.LINE_AA, False)
    
    frequencies = subprocess.getoutput('cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq').split('\n')[:4]
    for i in range(len(frequencies)):
        frequencies[i] = int(int(frequencies[i]) / 3100000 * 100)
    for i in range(len(frequencies)):
        gauges[i].val = frequencies[i]
    for gauge in gauges:
        gauge.draw_on(img)
    cv2.imshow('CPU Frequency Monitor', img)
    key = cv2.waitKey(100)
    print(frequencies)
    if key & 0xFF == ord('q'):
        exit(0)
    
        # time.sleep(0.05)

# while True:
#     i = 0
#     for theta in range(-30,31):
#         RED = int(255 - i/60*255)
#         GREEN = int(i/60*255)
#         img = numpy.zeros((640,640,3), dtype='uint8')
#         cv2.ellipse(img, center, axes,
#                    angle, startAngle, endAngle, color, thickness)
#         #cv2.line(img, center, target, (0,255,0), thickness)
#         cv2.line(img, center, (int(300+100*math.sin(math.radians(theta))), int(300-100*math.cos(math.radians(theta)))), (0,GREEN,RED), thickness)
#         cv2.putText(img, str(theta), (257,164), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                  (255,255,255), 1, cv2.LINE_AA, False)
#         cv2.imshow("Test", img)
#         if cv2.waitKey(50) & 0xFF == ord('q'):
#             exit(0)
#         i += 1

