import cv2
import numpy as np
import serial

ser = serial.Serial('COM11', baudrate = 9600, timeout = 1)
cap = cv2.VideoCapture(1)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('momo.avi',fourcc, 20.0, (640,480))

edges_current = 0
edges_previous = 0
frame_count = 0
count = 0
direction = True
while cap.isOpened():
    #cap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
    ret, frame = cap.read()
    #if ret == True:
        #cv2.imwrite('Frames3\\frame%d.jpg' %count, frame)
        #cv2.imshow('frame', frame)
        #out.write(frame)

    #edges  = cv2.Canny(frame, 100, 200)
    edges = cv2.Laplacian(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), cv2.CV_64F)
    
    if frame_count==60:
        edges_current = np.sum(edges)
        edges_previous = int(edges_previous)
        edges_current = int(edges_current)
        print(edges_previous, "  ", edges_current)
        if (edges_current-edges_previous>=10)and direction:
            ser.write(b'4')
            print(edges_current-edges_previous)
            print('move down')
        elif (edges_current-edges_previous<-10)and direction:
            ser.write(b'6')
            direction = False
            print(edges_current-edges_previous)
            print('move up')
        elif (edges_current-edges_previous>=10)and not(direction):
            ser.write(b'6')
            print(edges_current-edges_previous)
            print('move up')
        elif (edges_current-edges_previous<-10)and not(direction):
            ser.write(b'4')
            direction  = True
            print(edges_current-edges_previous)
            print('move down')
        frame_count = 0
        edges_previous = edges_current
    
    
    cv2.namedWindow('frames',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frames', 600,600)
    cv2.imshow('frames', frame)
    #cv2.namedWindow('edges',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('edges', 600,600)
    #cv2.imshow('edges', edges)
    
    count = count + 1
    frame_count=frame_count+1

    k= cv2.waitKey(5) & 0xFF

    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
