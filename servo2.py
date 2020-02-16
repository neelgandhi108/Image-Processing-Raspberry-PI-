#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def deg2duty(degree):
	min_val = 2
	max_val = 11

	duty = min_val + ((degree/180.0)*(max_val - min_val))

	return duty


GPIO.setmode(GPIO.BOARD)

pin = 12
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)


p.start(deg2duty(90))
user_input = float(input("Enter degree "))

while not(user_input == 1000):
    user_input = float(input("Enter degree "))
    p.ChangeDutyCycle(deg2duty(user_input))  # turn towards 90 degree

p.stop()
GPIO.cleanup()