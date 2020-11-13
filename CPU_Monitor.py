import cv2
import numpy
import subprocess

CMD = "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq"
RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)

while True:
    backdrop = numpy.zeros((640,640,3), dtype='uint8')
    cv2.namedWindow("CPU Monitor")
    frequencies = subprocess.getoutput(CMD).split('\n')
    for i in range(len(frequencies)):
        frequencies[i] = int(frequencies[i]) // 1000 * 1000
        cv2.putText(backdrop, str(frequencies[i]), (45,80+40*i), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow("CPU Monitor", backdrop)
    key = cv2.waitKey(100) & 0xFF
    if key == ord("q"):
        exit(0)
    pass

