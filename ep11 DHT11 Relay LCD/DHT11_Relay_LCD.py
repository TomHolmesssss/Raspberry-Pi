import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import lcdlib

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay = 22
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, True)

lcd = lcdlib.lcd()
lcd.lcd_clear()

flag = 0

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        text_temp = "Temp: {:.1f}-C".format(temperature)
        text_humid = "Humid: {:.1f}%".format(humidity)
        lcd.lcd_clear()
        lcd.lcd_display_string(text_temp, 1)
        lcd.lcd_display_string(text_humid, 2)
        if temperature >= 30 and flag == 0:
            GPIO.output(relay, False)
            flag = 1
        elif temperature < 30 and flag == 1:
            GPIO.output(relay, True)
            flag = 0
    time.sleep(10)
