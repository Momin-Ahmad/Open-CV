import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'H264')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('momo.avi', fourcc, 20.0, (1280,720))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame=cv2.resize(frame, (1280,720))
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
