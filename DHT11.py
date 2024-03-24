import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2

for i in range(10):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temperature={:.1f}*C Humidity={:.1f}%".format(temperature, humidity))
    time.sleep(3)
