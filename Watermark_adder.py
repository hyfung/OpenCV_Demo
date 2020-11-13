import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="The input filename, must end with .mp4")
# ap.add_argument("-o", "--output", required=True, help="The output filename, must end with .avi")
# ap.add_argument("-r", "--ratio", required=False, help="This option specifies how many frames to skip for each video", default=30, type=float)
# ap.add_argument("-s", "--scale", required=False, help="This option allows you to downsize the video, must be less than 1", default=1, type=float)
# ap.add_argument("-d", "--display", required=False, help="If enabled, will display the procses too", default=False, type=bool)
args = vars(ap.parse_args())

frame = cv2.imread(args['input'])

target_w, target_h = frame.shape[:2]

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(frame,"Jerry FUNG",(0,target_h//2), font, 8,(0,255,0),3,cv2.LINE_AA)
cv2.putText(frame,"Jerry FUNG",(0,target_h//4), font, 8,(0,255,0),3,cv2.LINE_AA)
cv2.putText(frame,"Jerry FUNG",(0,3*target_h//4), font, 8,(0,255,0),3,cv2.LINE_AA)

cv2.imshow("Watermark", frame)
cv2.waitKey()
