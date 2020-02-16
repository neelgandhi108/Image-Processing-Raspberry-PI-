#!/usr/bin/env python

import numpy as np
import cv2

gray = cv2.imread("./data/page.jpg",0)
# Checking the input shape
print(gray.shape)

# Since the image is so big we need to resize the image
gray = cv2.resize(gray,(0,0),fx=0.2,fy=0.2,
	interpolation=cv2.INTER_CUBIC)
print(gray.shape)

# Simple thresholding
thList = [cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,
cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV]

cv2.imshow("image.jpg",gray)
# cv2.imwrite("./data/image.jpg",gray)
for i,mode in enumerate(thList):
	ret,thresh = cv2.threshold(gray,120,255,mode)
	cv2.imshow("thresholded%d.jpg"%i,thresh)
	# cv2.imwrite("./data/thresholded%d.jpg"%i,thresh)
	cv2.waitKey(0)

cv2.namedWindow("output",cv2.WINDOW_NORMAL)
# This is used to resize only the output window and not the original image matrix.
cv2.resizeWindow("output",800,800)
cv2.imshow("output",gray)
cv2.waitKey(0)

print("All these were simple thresholding methods ...")
print("For our problem statement we need something better")

ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray,255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C
	,cv2.THRESH_BINARY,15,5)

cv2.imshow("simple binary thresholded",thresh1)
cv2.imshow("adaptive thresholded ",th2)
cv2.waitKey(0)





