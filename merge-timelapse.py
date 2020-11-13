import os
import cv2
import numpy as np

files = [x for x in sorted(os.listdir()) if ".jpg" in x]

width, height, ret = cv2.imread(files[0]).shape


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (height,width))
# out = cv2.VideoWriter('output.avi',cv2.CV_FOURCEE('',), 30.0, (height,width))

for file in files:
    print(file)
    frame = cv2.imread(file)
    out.write(frame)

    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
