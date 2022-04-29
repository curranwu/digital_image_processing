'''
Author: curran.wu
Date: 2022-04-29 22:45:56
LastEditors: curran.wu
LastEditTime: 2022-04-30 06:24:35
FilePath: \digital_image_processing\Chapter03\curran32\gamma_transform.py
Description: 

Copyright (c) 2022 by curran.wu, All Rights Reserved. 
'''

import cv2
import numpy as np
import math

def gammaTransform(c, gamma, img):
    h, w = img.shape[0], img.shape[1]
    new_img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.pow(img[i, j], gamma))

    # the range of cv2.imshow() for double type must be 0.0 - 1.0 
    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)/255
    return new_img

def benchGammaTransform(c, gamma, image):
    # 彩色图像
    """
    h, w, d = image.shape[0], image.shape[1], image.shape[2]
    new_img = np.zeros((h, w, d), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = c*math.pow(image[i, j, k], gamma)

    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    print(new_img)
    new_img = cv2.convertScaleAbs(new_img)
    print(new_img)
    """

    # 灰度图
    h, w = image.shape[0], image.shape[1]
    new_img = np.zeros((h, w), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * math.pow(image[i, j], gamma)
    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)

    return new_img
if __name__ == '__main__':
    img = cv2.imread('Chapter03/pic/Fig0307(a)(intensity_ramp).tif', 0)
    gamma_img = gammaTransform(1, 3.0, img)
    gamma_img_bench = benchGammaTransform(1, 3.0, img)
    cv2.imshow('src_img', img)
    cv2.imshow('gamma_img', gamma_img)
    cv2.imshow('gamma_img_bench', gamma_img_bench)
    cv2.waitKey(0)