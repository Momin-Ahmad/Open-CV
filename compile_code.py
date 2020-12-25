import cv2
import numpy as np
import serial
import matplotlib.pyplot as plt 
import os
import shutil
import glob
import time

ser = serial.Serial('COM11', baudrate = 9600, timeout = 1)
cap = cv2.VideoCapture(0)
total_horizontal_strip_steps=500000  #to be used in horizontal and vertical functions
total_vertical_strip_steps=500000
def optimal_focus():
     
    while cap.isOpened():
        _, frame = cap.read()
        edges_current = 0
        edges_previous = 0
        frame_count = 0
        direction = True
        edges  =np.sum(cv2.Laplacian(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var())
        
        if frame_count==60:
            edges_current = np.sum(edges)
            edges_previous = int(edges_previous)
            edges_current = int(edges_current)
            print(edges_previous, "  ", edges_current)
        if (edges_current-edges_previous>=100000)and direction:
            ser.write(b'4')
            print(edges_current-edges_previous)
            print('move down')
        elif (edges_current-edges_previous<-100000)and direction:
            ser.write(b'6')
            direction = False
            print(edges_current-edges_previous)
            print('move up')
        elif (edges_current-edges_previous>=100000)and not(direction):
            ser.write(b'6')
            print(edges_current-edges_previous)
            print('move up')
        elif (edges_current-edges_previous<-100000)and not(direction):
            ser.write(b'4')
            direction  = True
            print(edges_current-edges_previous)
            print('move down')
        frame_count = 0
        edges_previous = edges_current

        cv2.namedWindow('frames',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frames', 600,600)
        cv2.imshow('frames', frame)
        cv2.namedWindow('edges',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('edges', 600,600)
        cv2.imshow('edges', edges)

    frame_count=frame_count+1
    cv2.destroyAllWindows()
    cap.release()

# def reset_position_xy():
    
            
    
def horizontal_strip_with_framecapture(direction):
    pic_number = 0
    new_patch_iteration = 50  #again to be manually determined =like how many motors steps required to go to new patch for frame capturing 

        
    #code block for complete strip image capturing    
    for i in range(total_horizontal_strip_steps):
        _, frame1=cap.read()
        
        #cv2.waitKey(500)             #deley for some milli second to get static frame before writing 
        time.sleep(0.5)
        
        cv2.imwrite(os.path.join('some path','/'+str(pic_number)),frame1)
        pic_number=pic_number+1
        for j in range(new_patch_iteration):
            cv2.imshow('current_strip',frame1)
            #cv2.waitKey(500)
            time.sleep(0.5)
            if direction=='left_4':
                ser.write(b'4')
            else:
                ser.write(b'6')
            i=i+new_patch_iteration
            
        
        
        

def vertical_move_fornewstrip_horizontal():
    new_patch_vertical=50 #again to be manually determined =like how many steps for vertical to get in front of new strip 
    for j in range(new_patch_vertical):
            ser.write(b'2')


def scan_slide():
    #First Bring xy axis to initial position.it is in top right position
    total_iterations = 0
 #   reset_position_xy()
    scan_complete = False
    total_sets = 10  #predefined in the rectangular slide 
    for i in range(total_sets):
        optimal_focus()
        #Now use left x
        direction = 'left_4'
        horizontal_strip_with_framecapture(direction)
        vertical_move_fornewstrip_horizontal()   #vertical always in down direction
        optimal_focus()
        #Now use right  x
        direction = 'right_6'
        horizontal_strip_with_framecapture(direction)  
        vertical_move_fornewstrip_horizontal()  #vertical always in down direction
        
        
        
        



print('WELCOME TO AUTOMATIC PROGRAM')

while(True):
    
    input_command=input('Please enter Function Command')
    ''' s for scan
    4 and 6 for move y axis left or right
    8 and 4 move x axis left or right
    also commands for micro and full stepping 
    '''
    
    if input_command == '0':
        ser.write(b'0')
    elif input_command == '1':
        ser.write(b'1')
    elif input_command == '3':
        ser.write(b'3')
    elif input_command == '5':
        ser.write(b'5')
    elif input_command == '2':
        ser.write(b'2')
    elif input_command == '8':
        ser.write(b'8')
    elif input_command == '4':
        ser.write(b'4')
    elif input_command == '6':
        ser.write(b'6')
    elif input_command == '7':
        ser.write(b'7')
    elif input_command == '9':
        ser.write(b'9')
    elif input_command == 's':
        scan_slide()
    elif input_command == 'focus':
        optimal_focus()
    else:
        print('Invalid Input!')
        
    
    
    
    
    


