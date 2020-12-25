import numpy as np
import cv2

img1 = cv2.imread('left.JPG')
img2 = cv2.imread('right.JPG')

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#Brute Force Matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

matches = sorted(matches, key=lambda x:x.distance)
#for m in matches:
#    print(m.distance)

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[0:300], None)

cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img1' , 1000,600)
cv2.imshow('img1', img1)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img2' , 1000,600)
cv2.imshow('img2', img2)
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.resizeWindow('result' , 1000,600)
cv2.imshow('result', matching_result)
cv2.imwrite('Feature_Matching_BF', matching_result)
