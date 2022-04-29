'''
Author: curran.wu
Date: 2022-04-29 22:25:16
LastEditors: curran.wu
LastEditTime: 2022-04-29 22:44:49
FilePath: \digital_image_processing\Chapter03\curran32\log_transform.py
Description: s = c * log(1 + r)

Copyright (c) 2022 by curran.wu, All Rights Reserved. 
'''

import cv2
import numpy as np
import math

def logTransform(c, img):
    h, w = img.shape[0], img.shape[1]
    
    new_img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.log(1.0 + img[i, j]))
    
    # the range of cv2.imshow() for double type must be 0.0 - 1.0 
    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)/255

    return new_img

if __name__ == '__main__':
    img = cv2.imread('Chapter03/pic/Fig0305(a)(DFT_no_log).tif', 0)
    log_img = logTransform(1, img)
    cv2.imshow('src_img', img)
    cv2.imshow('log_img', log_img)
    cv2.waitKey(0)
