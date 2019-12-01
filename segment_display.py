import wiringpi
import time
from threading import Thread
from config import digits

class LED_Module:
	def __init__(self):
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(16,1)
		wiringpi.pinMode(21,1)
		wiringpi.pinMode(20,1)

	def set_screen(self,text):
		for x in text[::-1]:
			wiringpi.digitalWrite(16, 0)
			wiringpi.shiftOut(20, 21, wiringpi.MSBFIRST, digits[x])
			wiringpi.digitalWrite(16, 1)
			#time.sleep(0.05)
