'''
Author: curran.wu
Date: 2022-04-30 06:43:06
LastEditors: curran.wu
LastEditTime: 2022-04-30 06:47:41
FilePath: \digital_image_processing\Chapter03\curran32\slice_transform.py
Description: 

Copyright (c) 2022 by curran.wu, All Rights Reserved. 
'''

from pickletools import uint8
import cv2
import numpy as np
import math

def sliceTransform(img):
    [h, w] = img.shape
    new_img = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if 150 <= img[i, j] <= 230:
                new_img[i, j] = 255
            else:
                new_img[i, j] = 0
    
    return new_img

if __name__ == '__main__':
    img = cv2.imread('Chapter03/pic/Fig0312(a)(kidney).tif', 0)
    slice_img = sliceTransform(img)
    cv2.imshow('source img', img)
    cv2.imshow('slice img', slice_img)
    cv2.waitKey(0)