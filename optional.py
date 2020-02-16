#!/usr/bin/env python

import numpy as np 
import cv2

gray = cv2.imread("./data/chess.jpg",0)

gray = cv2.GaussianBlur(gray,(3,3),0)

laplacian = cv2.Laplacian(gray,cv2.CV_64F)
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
theta = np.arctan(sobely/(sobelx+0.0001))/np.pi


cv2.imshow("laplacian",laplacian/255)
cv2.imshow("sobel X",sobelx/255)
cv2.imshow("sobel y",sobely/255)
cv2.imshow("sobel theta",theta)
cv2.imshow("gray",gray)
cv2.waitKey(0)