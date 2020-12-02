import cv2
import numpy
import math

cv2.namedWindow('mat')

cv2.createTrackbar('pts', 'mat', 0, 255, lambda _: None)
cv2.createTrackbar('offset', 'mat', 0, 72, lambda _: None)
cv2.createTrackbar('radius', 'mat', 0, 50, lambda _: None)
cv2.createTrackbar('spread', 'mat', 0, 300, lambda _: None)


def main():
    origin = (300, 300)
    radius = 100
    
    while True:
        points = []
        radius = cv2.getTrackbarPos('spread', 'mat')

        num_steps = cv2.getTrackbarPos('pts', 'mat') + 1

        for step in range(0,num_steps):
            deg = 360 / num_steps * step + cv2.getTrackbarPos('offset', 'mat') * 5
            rad = math.radians(deg)
            points.append((int(origin[0] + radius * math.sin(rad)),int(origin[1] + radius * math.cos(rad))))
        
        mat = numpy.zeros((600,600,1))

        circle_rad = cv2.getTrackbarPos('radius', 'mat') * 4

        [cv2.circle(mat, point, circle_rad, (255,255,0), 1) for point in points]

        cv2.imshow('mat', mat)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
