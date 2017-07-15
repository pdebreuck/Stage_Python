import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as md

fd = open("log.txt",'r')
lines = fd.readlines()
lines= lines[:]
t = []
dates=[]
for x in range(len(lines)):
	val = lines[x].split('\t')
	temp = val[1].strip(' *C')
	t.append(float(temp))
	
	timestr = val[0]
	d = datetime.strptime(timestr,"%H:%M %a %d %b %Y")
	date = matplotlib.dates.date2num(d)
	dates.append(date)

plt.plot_date(dates, t,marker='None',color='r',linestyle='-')
plt.ylim([0,30])

plt.xlabel('Temps')
plt.ylabel('Temperature (*C)')
plt.title('Temperature')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("test.png",transparent=True)
