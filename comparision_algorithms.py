# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:52:51 2020

@author: mkhat
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(num=None, figsize=(80, 80), dpi=100, facecolor='w', edgecolor='k')
my_image=cv2.imread('CA1.jpg',cv2.IMREAD_ANYCOLOR)





image1=blurImg = cv2.blur(my_image,(2,2)) 
image2=blurImg = cv2.blur(my_image,(5,5))  
image3=blurImg = cv2.blur(my_image,(10,10))  
image4=blurImg = cv2.blur(my_image,(15,15))  
image5=blurImg = cv2.blur(my_image,(20,20))  
image6=blurImg = cv2.blur(my_image,(25,25))  
image7=blurImg = cv2.blur(my_image,(50,50)) 


def find_shape(my_image):
    
    grey_image=cv2.cvtColor(my_image,cv2.IMREAD_GRAYSCALE)   
    rows,col,_=grey_image.shape
    print(type(rows))
    print(type((col)))
    return rows,col
#Normalized Variance 

def variance(frame,rows,cols):
    
    mean_1=np.mean(frame)                                  #Variance (Groen et al., 1985; Yeo et al., 1993)
    
    return  (1.0/(rows*cols*np.mean(frame)))*((np.sum(frame[:,:]-np.mean(frame))**2))         



def variance_array(my_image,image1,image2,image3,image4,image5,image6):
    array1=[]
    rows,cols=find_shape(my_image)
    array1.append(variance(cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(variance(cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY),rows,cols))
    return array1
y_variance=variance_array(my_image,image1,image2,image3,image4,image5,image6)


def canny_array(my_image,image1,image2,image3,image4,image5,image6):
    array2=[]
    rows,cols=find_shape(my_image)
    array2.append(np.sum(cv2.Canny(my_image,100, 200)))
    array2.append(np.sum(cv2.Canny(image1,100, 200)))
    array2.append(np.sum(cv2.Canny(image2,100, 200)))
    array2.append(np.sum(cv2.Canny(image3,100, 200)))
    array2.append(np.sum(cv2.Canny(image4,100, 200)))
    array2.append(np.sum(cv2.Canny(image5,100, 200)))
    array2.append(np.sum(cv2.Canny(image6,100, 200)))
    array2.append(np.sum(cv2.Canny(image7,100, 200)))
    return array2
y_canny=canny_array(my_image,image1,image2,image3,image4,image5,image6)

def laplacian_array(my_image,image1,image2,image3,image4,image5,image6):
    array2=[]
    rows,cols=find_shape(my_image)
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    array2.append(np.sum(cv2.Laplacian(cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()))
    return array2
y_laplacian=laplacian_array(my_image,image1,image2,image3,image4,image5,image6)


def brenner(frame,row,col):
    temp=frame
    for i in range(row-10):
        for j in range(col):
            temp[i,j]=frame[i,j]-frame[i+10,j]
    
    return np.sum(temp)
    

def brenner_array(my_image,image1,image2,image3,image4,image5,image6):
    array1=[]
    rows,cols=find_shape(my_image)
    array1.append(brenner(cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY),rows,cols))
    array1.append(brenner(cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY),rows,cols))
    return array1

y_brenner=brenner_array(my_image,image1,image2,image3,image4,image5,image6)
x=range(1,9)


fig=plt.figure()

plt.imshow(cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY))
plt.xlabel('ORIGINAL IMAGE ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur1 ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur2  ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur3 ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur4 ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur5 ')
fig=plt.figure()
plt.imshow(cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur6 ')

plt.imshow(cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY))
plt.xlabel('blur7 ')
fig=plt.figure()
plt.plot(x,y_variance)
plt.xlabel('Normalized_Variance')
fig=plt.figure()
plt.plot(x,y_laplacian)
plt.xlabel('Power of laplacian')
fig=plt.figure()
plt.plot(x,y_canny)
plt.xlabel('Canny Edge Detector')
fig=plt.figure()
plt.plot(x,y_brenner)
plt.xlabel('brenner gradient')
cv2.waitKey(0)
cv2.destroyAllWindows()