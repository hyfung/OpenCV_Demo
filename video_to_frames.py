#!/usr/bin/python3
import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', type=str, required=True)
parser.add_argument('-r', '--rate', type=int, default=30)
args = parser.parse_args()

def leftpad(input):
    return '0' * (7 - len(str(input))) + str(input)

def main():
    filename = args.file
    cap = cv2.VideoCapture(args.file)

    ret, frame = cap.read()
    counter = 0
    fn_cnt = 0
    while ret:
        ret, frame = cap.read()
        if (counter % args.rate) == 0:
            cv2.imwrite(leftpad(fn_cnt) + '.jpg', frame)
            fn_cnt += 1
        counter += 1
    pass

if __name__ == '__main__':
    main()
