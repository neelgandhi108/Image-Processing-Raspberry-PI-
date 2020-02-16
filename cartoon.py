#!/usr/bin/env python

import numpy as np 
import cv2

img = cv2.imread("./data/sachin.jpeg")
img = cv2.bilateralFilter(img,3,75,75)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# gray = cv2.GaussianBlur(gray,(3,3),0)

edge = 255-cv2.Canny(gray,100,120)

blured = cv2.bilateralFilter(img,9,75,75)

output = cv2.bitwise_and(blured,blured,mask=edge)

# cv2.imshow("laplacian",laplacian)
# cv2.imshow("edge",edge)
# cv2.imshow("gray",gray)
cv2.imshow("input.jpeg",img)
cv2.imwrite("input.jpeg",img)
cv2.imshow("output.jpeg",output)
cv2.imwrite("output.jpeg",output)
cv2.waitKey(0)