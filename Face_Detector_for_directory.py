#!/usr/bin/python3
import cv2
import argparse
import os

'''
Usage:
python3 Face_Detector -d DIRECTORY
'''

keep_count, remove_count = 0,0
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_frontalface_default.xml')

#------------------------------------------------------------
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True, help="")
args = vars(ap.parse_args())

#Setting up the path for our directory
directory = args["directory"]
directory = directory + ("/" if directory[-1] != "/" else "")

print(directory)
#------------------------------------------------------------

file_list = sorted([x for x in os.listdir(directory) if ".jpg" in x or ".jpeg" in x])

# f = open(directory+'del_list.txt', "w")

for pic in file_list:
    if (keep_count + remove_count) % 10 == 0:
        print("Processed: %d/%d" % ((keep_count + remove_count), len(file_list)))
    filename = pic
    pic = directory + pic
    frame = cv2.imread(pic)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    if faces is ():
        try:
            os.rename(pic, directory+"noface_%d.jpg" % remove_count)
            print("[%d]\tRemoved:\t" % (keep_count + remove_count) + pic)
        except:
            # print("Cannot rename {pic}, probably removed.".format(pic=pic))
            print(f"Cannot rename {pic}, probably removed.")

        # f.write(pic)
        # f.write('\r\n')
        remove_count += 1

    else:
        print("[%d]\tKept:\t" % (keep_count + remove_count) + pic)
        keep_count += 1

    pass

print("Amount Processed:\t%d" % (keep_count + remove_count))
print("Amount Kept:\t\t%d" % keep_count)
print("Amount Removed:\t\t%d" % remove_count)
# f.close()
