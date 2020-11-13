import cv2, numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
#Commenting Eyes detection reduces frame time
# eye_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_eye.xml')

blurness = 1

cv2.namedWindow("Capture")

def on_blur_trackbar(val):
    global blurness
    blurness = 2*val+1

cv2.createTrackbar("Blurness", "Capture", 0, 50, on_blur_trackbar)

while True:
    ret, img = cap.read()
    
    img = cv2.blur(img, (blurness,blurness))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    '''
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
            # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    '''

    img = cv2.flip(img, 1)
    cv2.imshow("Capture", img)
    cv2.waitKey(33)

cv2.destroyAllWindows()
