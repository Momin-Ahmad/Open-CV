import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray, rgb2hsv
from skimage import io
from skimage import data
#from skimage.feature import register_translation
from skimage.registration import phase_cross_correlation
#from skimage.feature.register_translation import _upsampled_dft
from skimage.registration._phase_cross_correlation import _upsampled_dft
from scipy.ndimage import fourier_shift
import os.path
import cv2

first_flag = 0

path_string = os.getcwd()
#fileName1 = path_string + "/Frames4/0" + ".png"
#fileName2 = path_string + "/Frames4/5" + ".png"
#fileName1 = "scene00421.png"
fileName1 = "i1.jpeg"
#fileName2 = "scene00391.png"
fileName2 = "i2.jpeg"

im = io.imread(fileName1)
im2 = io.imread(fileName2)
image = rgb2gray(im)
offset_image = rgb2gray(im2)

# pixel precision first
shift, error, diffphase = phase_cross_correlation(image, offset_image)
ni0 = int(np.abs(shift[0]))
ni = int(np.abs(shift[1]))
print("offset x, ys = ", ni0, ", ", ni)
print("offset x, ys = ", shift[0], ", ", shift[1])
px = np.size(im,0)
py = np.size(im, 1)
#new_area = im2[:,0:ni,:]
#new_area1 = im[0:ni0,:,:]
#zero_line = np.zeros((abs(int(shift[1])), im2.shape[1], 3), dtype=np.uint8)
#zero_line = np.zeros((im2.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
#zero_line1 = np.zeros((new_area1.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
#zero_line = np.zeros((342, 1920, 3), dtype=np.uint8)
#new_area1[:,:,:]=[0,0,0]
#cv2.imshow('bob', zero_line)
if first_flag == 0:   
    #img3 = cv2.hconcat([new_area, im])
    #img3 = cv2.vconcat([zero_line, im2])
    if (shift[0]>=0 and shift[1]>=0):
        print('case 1')
        new_area1 = im[0:ni0,:,:]
        zero_line = np.zeros((im2.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
        zero_line1 = np.zeros((new_area1.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
        im2_temp = cv2.hconcat([zero_line, im2])
        new_area1_temp = cv2.hconcat([new_area1, zero_line1])
        img3 = cv2.vconcat([new_area1_temp, im2_temp])
        first_flag = 1
    if (shift[0]<=0 and shift[1]>=0):
        print('case 2')
        new_area = im[:,0:ni,:]
        zero_line = np.zeros((abs(int(shift[0])), im2.shape[1], 3), dtype=np.uint8)
        zero_line1 = np.zeros((abs(int(shift[0])), new_area.shape[1], 3), dtype=np.uint8)
        im2_temp = cv2.vconcat([im2, zero_line])
        new_area_temp = cv2.vconcat([zero_line1, new_area])
        img3 = cv2.hconcat([new_area_temp, im2_temp])
        first_flag = 1
    if (shift[0]<=0 and shift[1]<=0):
        print('case 3')
        new_area1 = im2[0:ni0,:,:]
        zero_line = np.zeros((im2.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
        zero_line1 = np.zeros((new_area1.shape[0], abs(int(shift[1])), 3), dtype=np.uint8)
        im_temp = cv2.hconcat([zero_line, im])
        new_area1_temp = cv2.hconcat([new_area1, zero_line1])
        img3 = cv2.vconcat([new_area1_temp, im_temp])
        first_flag = 1
    if (shift[0]>=0 and shift[1]<=0):
        print('case 4')
        new_area = im2[:,0:ni,:]
        zero_line = np.zeros((abs(int(shift[0])), im2.shape[1], 3), dtype=np.uint8)
        zero_line1 = np.zeros((abs(int(shift[0])), new_area.shape[1], 3), dtype=np.uint8)
        im_temp = cv2.vconcat([im, zero_line])
        new_area_temp = cv2.vconcat([zero_line1, new_area])
        img3 = cv2.hconcat([new_area_temp, im_temp])
        first_flag = 1
else:
    img3 = cv2.hconcat([new_area, img3])
io.imsave('temp.tif', img3, compress=0)
#cv2.imshow('bob', img3)
#io.imsave('new.tif', new_area, compress=0)
#io.imsave('new1.tif', new_area1, compress=0)
