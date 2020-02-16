#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin = 12
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)

p.start(7.5)
user_input = float(input("Enter the duty cycle "))

while not(user_input == 1000):
    user_input = float(input("Enter the duty cycle "))
    p.ChangeDutyCycle(user_input)  # turn towards 90 degree

p.stop()
GPIO.cleanup()