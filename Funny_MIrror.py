import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
ret,img = cap.read()
for i in range(100000000):
	ret,img = cap.read()
	h,w = img.shape[:2]
	y,x = np.meshgrid(np.arange(0,h),np.arange(0,w))
	x = x.T
	y = y.T

	mode = 1

	if mode == 1:
		omega = 2*np.pi/(h/10.0)
		x = x + 3*np.sin(y*omega)
	else:
		omega = 2*np.pi/(w/10.0)
		y = y + 3*np.sin(x*omega)

	funnyMirror1 = cv2.remap(img,x.astype(np.float32),y.astype(np.float32),interpolation=cv2.INTER_LINEAR)

	cv2.imshow("output",funnyMirror1)
	cv2.waitKey(1)
