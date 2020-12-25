import cv2
import numpy as np
import sys
import glob
import time

cap = cv2.VideoCapture("Video.3GP")
count = 0
while cap.isOpened():
    cap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite('Frames\\frame%d.jpg' %count, frame)
        cv2.imshow('frame', frame)

    count = count + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

time.sleep(1)

images = [cv2.imread(file) for file in glob.glob("Frames/*.jpg")]
 
stitcher = cv2.Stitcher.create()
ret, pano = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.namedWindow('Panorama 1',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Panorama 1', 600,600)
    cv2.imshow('Panorama 1', pano)
    cv2.imwrite('Stitched.jpg', pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during stitching")



cap.release()
cv2.destroyAllWindows()
