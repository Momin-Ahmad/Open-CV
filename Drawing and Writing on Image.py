import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Juggernaut.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (500,500), (255,255,255), 15)
cv2.rectangle(img, (0,0), (1000, 1000), (255,0,0), 15)
cv2.circle(img, (500,500), 200, (0,255,0), -1)

pts = np.array([[100,50], [200,300], [700, 200], [500, 100]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255) ,3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Momo Bobo', (500,500), font, 5, (200,255,255), 5, cv2.LINE_AA)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
