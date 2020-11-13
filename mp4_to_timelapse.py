import cv2
import argparse
import numpy
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="The input filename, must end with .mp4")
ap.add_argument("-o", "--output", required=True, help="The output filename, must end with .avi")
ap.add_argument("-r", "--ratio", required=False, help="This option specifies how many frames to skip for each video", default=30, type=float)
ap.add_argument("-s", "--scale", required=False, help="This option allows you to downsize the video, must be less than 1", default=1, type=float)
ap.add_argument("-d", "--display", required=False, help="If enabled, will display the procses too", default=False, type=bool)
args = vars(ap.parse_args())

input_name = args['input']
output_name = args['output']
ratio = args['ratio']

print("[*]Opening video: %s" % input_name)
print("[*]Preparing output stream: %s" % output_name)

#This is our video stream
cap = cv2.VideoCapture(input_name)

if (cap.isOpened()== False): 
  print("[*]Error opening video stream or file")
  print("[*]Exiting with code -1")
  exit(-1)

ret, img = cap.read()
height, width, channels = img.shape
target_width, target_height = int(width*args['scale']), int(height*args['scale'])
# width = cap.get(3)
# height = cap.get(4)

print("[*]Source Dimension:\t{},{}".format(width, height))
print("[*]Target Dimension:\t{},{}".format(target_width, target_height))

out = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc('M','J','P','G'), 30, (target_width, target_height))

count = 0

start = time.time()
while(cap.isOpened()):
    ret, frame = cap.read()

    if count % ratio == 0:
        frame = cv2.resize(frame, (target_width, target_height))
        out.write(frame)
        if args['display']:
            cv2.imshow('frame', frame)
            cv2.waitKey(1)

    if count % 500 == 0:
        elapsed = time.time() - start
        print("[*]Frame handled: %d, FPS: %d" % (count, count/elapsed))
    
    count += 1
    
    if frame is None:
        break
end = time.time()

print("[*]Job completed in {} seconds".format(int(end - start)))
print("[*]Done, exiting...")
