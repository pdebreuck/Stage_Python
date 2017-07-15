import sys
import Adafruit_DHT
import time

Pin = 2

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 ,Pin)

temp = '{0:0.1f} *C'.format(temperature)
hum = '{0:0.1f}%'.format(humidity)
date  = time.strftime("%H:%M %a %d %b %Y")
print(date)
print(temp)


