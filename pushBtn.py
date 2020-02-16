#!/usr/bin/env python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

pb1 = 10

GPIO.setup(pb1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
print("Reading button")

push = 0
while True: # Run forever
    if GPIO.input(pb1) == GPIO.HIGH:
        push+=1
        print("Button pressed %d times"%push)