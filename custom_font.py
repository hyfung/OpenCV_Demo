import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((640,640,3), dtype='uint8')
img[:] = (255,255,255)

text = "*01552988019074*"

fontPath = "/usr/share/fonts/Code39_Regular.ttf"

font = ImageFont.truetype(fontPath, 40)

imgPil = Image.fromarray(img)

draw = ImageDraw.Draw(imgPil)
draw.text((30,30), text, font=font, fill=(0,0,0))

img = np.array(imgPil)

cv2.imshow('img', img)
cv2.waitKey()