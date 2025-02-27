'''
Author: curran.wu
Date: 2022-04-29 20:59:42
LastEditors: curran.wu
LastEditTime: 2022-04-29 22:22:22
FilePath: \digital_image_processing\Chapter03\curran32\image_reverse.py
Description: reverse the images
            grayLevel : [0, L - 1]
            s = L - 1 - r

Copyright (c) 2022 by curran.wu, All Rights Reserved. 
'''
import cv2
import numpy as np

img = cv2.imread('Chapter03/pic/Fig0304(a)(breast_digital_Xray).tif', 0)
reversed_image = 255 - img

cv2.imshow('src image', img)
cv2.imshow('reverved image', reversed_image)
cv2.waitKey(0)
