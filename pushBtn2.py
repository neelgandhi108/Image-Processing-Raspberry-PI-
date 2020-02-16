
#!/usr/bin/env python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

pb1 = 10
GPIO.setup(pb1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


btn_state = 0
flag = 0
def Button1(pin):
	global btn_state
	flag = False

	if (GPIO.input(pin)) and (btn_state == 0):
		btn_state = 1
		time.sleep(0.03)
	elif (GPIO.input(pin)) and (btn_state == 1):
		btn_state = 2
	elif not(GPIO.input(pin)) and (btn_state == 2):
		btn_state = 3
		time.sleep(0.03)
	elif not(GPIO.input(pin)) and (btn_state == 3):
		btn_state = 0
		flag = True

	return flag

while True:
	clicked = Button1(pb1)
	if clicked:
		print("Button clicked")