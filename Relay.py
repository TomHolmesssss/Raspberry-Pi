import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay = 2
GPIO.setup(relay, GPIO.OUT)

for i in range(10):
	GPIO.output(relay, True)
	time.sleep(5)
	GPIO.output(relay, False)
	time.sleep(5)
