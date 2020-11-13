#!/usr/bin/python3
import cv2
import numpy as np
from flask import Flask, make_response, redirect, Response
from io import BytesIO
import threading
import time

app = Flask(__name__)

lock = threading.Lock()
# lock.release()
cap = cv2.VideoCapture(0)
frame = None
stop = False


def update_frame():
    global frame
    while not stop:
        # if not lock.locked():
        _, frame = cap.read()
            # time.sleep(33)
    return

thread = threading.Thread(target=update_frame)
thread.start()


@app.route("/snapshot")
def snapshot():
    # cap = cv2.VideoCapture(0)
    lock.acquire()
    ret, img = cap.read()
    lock.release()
    encoded_img = np.array(cv2.imencode('.jpg', img)[1])
    resp = make_response(bytes(encoded_img), 200)
    resp.headers['Content-Type'] = 'image/jpeg'
    return resp


@app.route('/snapshot2')
def snapsnot2():
    # cap = cv2.VideoCapture(0)
    lock.acquire()
    ret, img = cap.read()
    lock.release()
    encoded_img = np.array(cv2.imencode('.jpg', img)[1])
    with BytesIO() as f:
        f.write(encoded_img)
        f.seek(0)
        return (f.read(), 200,)


def convertToJpeg(img):
    return bytes(np.array(cv2.imencode('.jpg', img)[1]))


def gen():
    while True:
        img = frame
        yield (b'--frame\r\n' +
            b'Content-Type: image/jpeg\r\n\r\n' +
            convertToJpeg(img) +
            b'\r\n')


@app.route('/stream')
def stream():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host="0.0.0.0", port=8888)
stop = True
thread.join()
exit()
