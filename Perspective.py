#!/usr/bin/env python

import numpy as np 
import cv2

img = cv2.imread("./data/NYTimeSquare.jpg")
print(img.shape)
img = cv2.resize(img,(0,0),fx=0.25,fy=0.25,interpolation=cv2.INTER_CUBIC)

img2 = cv2.imread("./data/kostech.jpg")
mask = np.ones(img2.shape)

rows,cols,ch = img2.shape

pts1 = np.float32([[0,0],[cols,0],[cols,rows],[0,rows]])
pts2 = np.float32([[275,88],[398,32],[406,146],[274,190]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img2,M,(img.shape[1],img.shape[0]))
Maskdst = cv2.warpPerspective(mask,M,(img.shape[1],img.shape[0]))
mask = 255 - Maskdst[:,:,0].astype(np.uint8)*255
img = cv2.bitwise_and(img,img,mask=mask)

output = img + dst

cv2.imshow("output",output)
cv2.imwrite("output.jpg",output)
cv2.waitKey(0)