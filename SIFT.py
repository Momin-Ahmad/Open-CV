import numpy as np
import cv2


img = cv2.imread('10.png')
#cv2.imshow('image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('imaage', gray)


sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create(nfeatures=15000)
kp = surf.detect(gray,None)

img = cv2.drawKeypoints(gray,kp,img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image' , 600,600)
cv2.imshow('image', img)
