#!/usr/bin/env python

import numpy as np 
import cv2

img = cv2.imread("./data/saltpep.jpeg",0)

avg_blur = cv2.blur(img,(5,5))
gaussian_blur = cv2.GaussianBlur(img,(5,5),0)
bilatera_blur = cv2.bilateralFilter(img,5,75,75)
median_blur = cv2.medianBlur(img,5)

cv2.imshow("input",img)
cv2.imwrite("avg_blur.jpg",avg_blur)
cv2.imwrite("gaussian_blur.jpg",gaussian_blur)
cv2.imwrite("bilatera_blur.jpg",bilatera_blur)
cv2.imwrite("median_blur.jpg",median_blur)
cv2.waitKey(0)