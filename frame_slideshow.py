#!/usr/bin/python3
import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-d', '--dir', type=str, required=True)
args = parser.parse_args()

image_dir = args.dir
cv2.namedWindow("Lapse")

def main():    
    frame_names = [x for x in os.listdir(image_dir) if x.endswith('.jpg') or x.endswith('.png')]
    cv2.createTrackbar("Frame", "Lapse", 0, len(frame_names)-1, lambda x: None)
    frames = list()

    for frame_name in frame_names:
        mat = cv2.imread(args.dir + frame_name)
        frames.append(mat)

    while True:
        index = cv2.getTrackbarPos("Frame", "Lapse")
        cv2.imshow(frames, "Lapse")
        if cv2.waitKey(100) & 0xFF == ord('q'):
            exit(0)

if __name__ == '__main__':
    main()
