#!/bin/python

from Tkinter import *
import Adafruit_DHT
import itertools

class Interface(Frame):
    
    
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=1000, height=1000, **kwargs)
        #self.pack(fill=BOTH)
        
        #widgets
        
        
        fd = open('/home/pi/Documents/TempWeb/counter.txt','r')
        num = int(fd.readline())
        fd.close()
        
        min = num - 40
        if min<0:
            min = 0
        
        fd = open("/home/pi/Documents/TempWeb/log.txt","r")
        tabel = ""
        for line in itertools.islice(fd, min, num + 1):
            print(line)
            tabel = tabel + line
        print(tabel)
        fd.close()
        self.tbl = Label(self, text=tabel)
        self.tbl.grid(column=0,row=1)
        
        self.ti = Label(self, text="Historique des mesures",font=('Helvetica',16))
        self.ti.grid(column=0,row=0)
        
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.grid(column=2,row=0)
        
        self.bouton_cliquer = Button(self, text="Refresh", command=Refresh)
        self.bouton_cliquer.grid(column = 0, row = 2)
        
        
        self.img = PhotoImage(file="test.png")
        self.graphe = Label(self, image = self.img,padx=10,pady=10)
        self.graphe.grid(column=1,row=1)
        
        self.top = Buttons(self)
        self.top.grid(column=1,row=0)
        
        self.a = Actual(self)
        self.a.grid(column=1,row=2)
        
    
    def clic(self):     
        
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 ,2)
        temp = '{0:0.1f} *C'.format(temperature)
        self.m2["text"] = "Temperature: " +temp
        
class Buttons(Frame):
       
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=1000, height=1000, **kwargs)
        #self.pack(fill=BOTH)
        

        self.bHum = Button(self, text="humidite",
                command=graphHum)
        self.bHum.grid(column = 0, row = 0)
        
        self.bTemp = Button(self, text="temperature",
                command=graphTemp)
        self.bTemp.grid(column = 1, row = 0)
        
class Actual(Frame):
    
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=1000, height=1000, **kwargs)
        #self.pack(fill=BOTH)
        
        self.bHum = Button(self, text="humidite", command=lHum,justify=LEFT)
        self.bHum.grid(column = 0, row = 0)
        
        self.bTemp = Button(self, text="temperature", command=lTemp,justify=LEFT)
        self.bTemp.grid(column = 0, row = 1)
        
        self.t1 = Label(self, text="L'humidite est de: ",justify=LEFT)
        self.t1.grid(column=1,row=0)
        
        self.t2 = Label(self, text="La temperature est de: ",justify=LEFT)
        self.t2.grid(column=1,row=1)

def Refresh():
    fd = open('/home/pi/Documents/TempWeb/counter.txt','r')
    num = int(fd.readline())
    fd.close()
        
    min = num - 40
    if min<0:
        min = 0
        
    fd = open("/home/pi/Documents/TempWeb/log.txt","r")
    tabel = ""
    for line in itertools.islice(fd, min, num + 1):
        print(line)
        tabel = tabel + line
    print(tabel)
    fd.close()
    interface.tbl = Label(interface, text=tabel)
    interface.tbl.grid(column=0,row=1)    

def graphHum():
    execfile("graph2.py")
    interface.img = PhotoImage(file="hum.png")
    interface.graphe = Label(interface, image = interface.img,padx=10,pady=10)
    interface.graphe.grid(column=1,row=1)

def graphTemp():
    execfile("graph.py")
    interface.img = PhotoImage(file="test.png")
    interface.graphe = Label(interface, image = interface.img,padx=10,pady=10)
    interface.graphe.grid(column=1,row=1)

def lHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 ,2)
    temp = '{0:0.1f} %'.format(humidity)
    interface.a.t1["text"] = "L'humidite est de: " +temp

def lTemp():
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 ,2)
        temp = '{0:0.1f} *C'.format(temperature)
        interface.a.t2["text"] = "Temperature: " +temp



root = Tk()
interface = Interface(root)
interface.pack()
interface.mainloop()
interface.destroy()
