'''
Author: curran.wu
Date: 2022-04-30 06:27:39
LastEditors: curran.wu
LastEditTime: 2022-04-30 06:37:23
FilePath: \digital_image_processing\Chapter03\curran32\constrast_stretch.py
Description: 
    A = min[f(x, y)]
    B = max[f(x, y)]
    then g(x, y) = F(f(x, y)) and max(g(x, y)) = 255
Copyright (c) 2022 by curran.wu, All Rights Reserved. 
'''
import cv2
import numpy as np
import math

def contrastStretchTransform(img):
    [h, w, d] = img.shape
    new_img = np.zeros((h, w, d), dtype=np.float32)
    A = img.min()
    B = img.max()
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = 255.0 / (B - A) * (img[i, j, k] - A) + 0.5
    
    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    return new_img

if __name__ == '__main__':
    img = cv2.imread('Chapter03/pic/beizi.png', 1)
    contrast_img = contrastStretchTransform(img)
    cv2.imshow('src img', img)
    cv2.imshow('contrast img', contrast_img)
    cv2.waitKey(0)