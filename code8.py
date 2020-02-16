#!/usr/bin/env python
import cv2
import numpy as np
from webcam import *
import RPi.GPIO as GPIO
import time

# Define which type of numbering we will be using is the physical numbering
GPIO.setmode(GPIO.BOARD)


#define pin tags
pin1 = 11

# Configure GPIO pins as input or Output pins
GPIO.setup(pin1,GPIO.OUT)


cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    frame = get_image(url)
    # _, frame = cap.read()

    roi = frame[:200,:200,:]

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    mask = th3.astype(np.uint8)
    image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(roi,roi, mask= mask)
    cnt = contours[0]
    epsilon = 0.03*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    res = cv2.drawContours(res, [approx], 0, (0,255,0), 3)
    
    if approx.shape[0] > 9:
        GPIO.output(pin1,True)
    else:
        GPIO.output(pin1,False)

    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
GPIO.cleanup()

