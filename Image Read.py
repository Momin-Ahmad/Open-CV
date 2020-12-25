import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Juggernaut.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
