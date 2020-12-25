import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray, rgb2hsv
from skimage import io
from skimage import data
from skimage.feature import register_translation
from skimage.feature.register_translation import _upsampled_dft
from scipy.ndimage import fourier_shift
import os.path
import cv2


path_string = os.getcwd()
fileNumber = str(2).zfill(5)
fileName = path_string + "/frames/scene" + fileNumber + ".png"
file_exist_array = []
first_flag = 0
import os.path
for i in range(1350):
    fileNumber = str(i).zfill(5)
    fileName = path_string + "/frames/scene" + fileNumber + ".png"
    if os.path.isfile(fileName):
        #print (fileName)
        file_exist_array.append(i)
#for i2 in range(10):
for i2 in range(len(file_exist_array)-1):
    fileNumber1 = str(file_exist_array[i2]).zfill(5)
    fileName1 = path_string + "/frames/scene" + fileNumber1 + ".png"
    fileNumber2 = str(file_exist_array[i2+1]).zfill(5)
    fileName2 = path_string + "/frames/scene" + fileNumber2 + ".png"
    #image = data.camera()
    im = io.imread(fileName1)
    im2 = io.imread(fileName2)
    image = rgb2gray(im)
    offset_image = rgb2gray(im2)

    # pixel precision first
    shift, error, diffphase = register_translation(image, offset_image)
    ni0 = int(shift[0])
    ni = int(np.abs(shift[1]))
    print("offset x, ys = ", ni0, ", ", ni)
    px = np.size(im,0)
    py = np.size(im, 1)
    new_area = im2[:,0:ni,:]
    if first_flag == 0:   
        img3 = cv2.hconcat([new_area, im])
        first_flag = 1
    else:
        img3 = cv2.hconcat([new_area, img3])
io.imsave('temp.tif', img3, compress=0)
