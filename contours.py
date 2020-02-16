#!/usr/bin/env python
import cv2
import numpy as np 

img = cv2.imread("oreo.jpg")
cv2.imshow("oreo",img)
cv2.waitKey(0)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue= np.array([90,60,50])
upper_blue = np.array([140,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

edges = cv2.Canny(mask,70,200)

cnts,_ = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
centroids = []
biscuits = 0

for cnt in cnts:
	cv2.drawContours(img,[cnt],-1,(0,255,0),3)
	area = cv2.contourArea(cnt)
	x,y,w,h = cv2.boundingRect(cnt)
	rect_area = w*h
	extent = float(area)/rect_area
	print(extent)
	cx = x+w//2
	cy = y+h//2
	center = (cx,cy)
	if not(center in centroids):
		centroids.append(center)
		if extent > 0.7:
			biscuits+=1

	cv2.imshow("oreo",img)
	cv2.waitKey(0)

print("number of biscuits = ",biscuits)



cv2.imshow("Frame",mask)
cv2.waitKey(0)

cv2.imshow("Frame",edges)
cv2.waitKey(0)

cv2.imshow("oreo",img)
cv2.waitKey(0)

