#!/usr/bin/env python

import numpy as np
import cv2

gray = cv2.imread("./data/arrow.jpg",0)
# Checking the input shape
print(gray.shape)

cv2.imshow("inputTh",gray)
# cv2.imwrite("inputTh.jpg",gray)

ret,thresh1 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,5)

blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("binaryTh",thresh1)
# cv2.imwrite("binaryTh.jpg",thresh1)
cv2.imshow("adaptiveTh",th2)
# cv2.imwrite("adaptiveTh.jpg",th2)
cv2.imshow("OtsuTh",th3)
# cv2.imwrite("OtsuTh.jpg",th3)
cv2.waitKey(0)