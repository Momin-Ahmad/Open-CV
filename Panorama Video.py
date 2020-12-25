import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('200122163326.MP4')
count = 0
while cap.isOpened():
    cap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite('Frames6\\%d.bmp' %count, frame)
        cv2.imshow('frame', frame)

    count = count + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
