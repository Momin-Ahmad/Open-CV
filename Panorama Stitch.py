import cv2
import numpy as np
import glob
from os import listdir
from os.path import isfile, join
import re

dim = (1500,1000)

#images = [cv2.imread(file) for file in glob.glob("Frames/*.JPG")]


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


mypath = 'Frames5'
onlyfiles = sorted_alphanumeric([ f for f in listdir(mypath) if isfile(join(mypath,f)) ])
#images = np.empty(len(onlyfiles), dtype=object)
strips = []
j=1
for i in range(len(onlyfiles)):
    if i%5==0 or i==len(onlyfiles):
        images=[]
        for n in range(j, i):
            images.append(cv2.imread(join(mypath, onlyfiles[n])))

        stitcher = cv2.Stitcher.create()
        ret, pano = stitcher.stitch(images)
        strips.append(pano)
        j = i + 1

del strips[0]

if ret==cv2.STITCHER_OK:
    #cv2.namedWindow('Panorama 1',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Panorama 1', 600,600)
    cv2.imshow('Panorama 1', strips[0])
    cv2.imshow('Panorama 2', strips[1])
    cv2.imshow('Panorama 3', strips[2])
    cv2.imwrite('1.png', strips[1]) 
    #cv2.waitKey()
    #cv2.destroyAllWindows()
else:
    print("Error during stitching")

stitcher = cv2.Stitcher.create()
ret, pano = stitcher.stitch(strips)

if ret==cv2.STITCHER_OK:
    #cv2.namedWindow('Panorama 1',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Panorama 1', 600,600)
    cv2.imshow('Panorama_microscope', pano)
    cv2.imwrite('Panorama_microscope.png', pano) 
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during stitching")
