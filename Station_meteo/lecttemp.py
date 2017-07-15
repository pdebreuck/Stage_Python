import sys
import Adafruit_DHT
import time


Pin = 2

fd = open("/home/pi/Documents/TempWeb/counter.txt","r")
number = int(fd.readline())
fd.close()

fd = open("/home/pi/Documents/TempWeb/counter.txt","w")
fd.write('{:010d}\n'.format(number+1))
fd.close()

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 ,Pin)

temp = '{0:0.1f} *C'.format(temperature)
hum = '{0:0.1f}%'.format(humidity)
str  = time.strftime("%H:%M %a %d %b %Y") + '\t' + temp +'\t' + hum +'\n'

fd = open("/home/pi/Documents/TempWeb/log.txt","a")
fd.write(str)
fd.close()


