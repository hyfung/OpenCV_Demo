import cv2
import qrcode
import time
from io import BytesIO
import numpy as np

def main():
    while True:
        time_str = str(int(time.time()))
        with BytesIO() as f:
            qrcode.make(time_str).save(f)
            f = np.asarray(bytearray(f.getvalue()), dtype='uint8')
            img = cv2.imdecode(f, 1)
            cv2.imshow("img", img)
            if cv2.waitKey(33) & 0xFF == ord('q'):
                break
        time.sleep(1)

if __name__ == "__main__":
    main()
