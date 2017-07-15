import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as md
import re

fd = open("log.txt",'r')
lines = fd.readlines()
lines= lines[:]
t = []
dates=[]
for x in range(len(lines)):
	val = lines[x].split('\t')
	non_decimal = re.compile(r'[^\d.]+')
	temp = non_decimal.sub('', val[2])
	t.append(float(temp))
	
	timestr = val[0]
	d = datetime.strptime(timestr,"%H:%M %a %d %b %Y")
	date = matplotlib.dates.date2num(d)
	dates.append(date)

plt.plot_date(dates, t,marker='None',color='b',linestyle='-')
plt.ylim([10,100])

plt.xlabel('Temps')
plt.ylabel('Humidite (%%)')
plt.title('Humidite')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("hum.png",transparent=True)

