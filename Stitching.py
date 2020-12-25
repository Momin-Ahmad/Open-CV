import cv2
import numpy as np

dim = (1200,500)

one = cv2.imread('Frames4/3.png', cv2.IMREAD_COLOR)
#one = cv2.resize(one, dim, interpolation = cv2.INTER_AREA)
two = cv2.imread('Frames4/5.png', cv2.IMREAD_COLOR)
#two = cv2.resize(two, dim, interpolation = cv2.INTER_AREA)
three = cv2.imread('Frames4/7.png', cv2.IMREAD_COLOR)
#three = cv2.resize(three, dim, interpolation = cv2.INTER_AREA)

images = []
images.append(one)
images.append(two)
images.append(three)

stitcher = cv2.Stitcher.create()
ret, pano = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.namedWindow('Panorama',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Panorama', 1000,600)
    cv2.imshow('Panorama', pano)
    cv2.imwrite('Final_Stitched.png', pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during stitching")
