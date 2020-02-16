#!/usr/bin/env python
import cv2
import pytesseract
import numpy as np

img = cv2.imread("./data/text1.jpg",0)
cv2.imshow("input",img)
cv2.waitKey(0)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("input",img)
cv2.waitKey(0)


# kernel = np.array([[0,1,0],[0,1,0],[0,1,0]],np.uint8)
kernel = np.ones((3),np.uint8)
img = cv2.erode(img,kernel,iterations = 1)

cv2.imshow("input",img)
cv2.waitKey(0)


text = pytesseract.image_to_string(img,config='--psm 11')
print(text)