#!/usr/bin/env python

import numpy as np 
import cv2

gray = cv2.imread("./data/chess.jpg",0)

# kernel = np.ones((3,3),np.float32)
sobel_kernel_x = np.array([[1,0,-1],[2,0,-2],[1,0,-1]],np.float32)
sobel_kernel_y = sobel_kernel_x.T
Laplacian_kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]],np.float32)
AvgBlurring = np.ones((5,5),np.float32)/25

output = cv2.filter2D(gray,-1,sobel_kernel_x)
# cv2.imwrite("input.jpg",gray)
cv2.imshow("output",output)
# cv2.imwrite("Laplacian_kernel.jpg",output)
cv2.waitKey(0)