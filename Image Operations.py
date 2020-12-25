import numpy as np
import cv2

img = cv2.imread('Juggernaut.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)

img[100:150, 100:150] = [255,255,255]

img_part = img[370:670, 500:800]
img[0:300, 0:300] = img_part

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllwindows()
