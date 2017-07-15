from Tkinter import *
import Adafruit_DHT
import itertools

class Interface(Frame):
    
    
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=500, height=400, **kwargs)
        #self.pack(fill=BOTH)
        
        #widgets
        self.m1 = Label(self,text="Bonjour!",font=("Helvetica", 16),borderwidth=2)
        self.m1.grid(column=0,row=0,padx=100,pady=10)
        
        self.m2 = Label(self,text="Ceci est une station meteo!",font=("Helvetica", 16))
        self.m2.grid(column=0,row=1,padx=100,pady=10)
        
        self.bouton_cliquer = Button(self, text="Temp", fg="red",
                command=self.click)
        self.bouton_cliquer.grid(column = 2, row = 1)
        
        
        
        circle = Canvas(self,relief=RAISED)
        circle.create_oval(5, 5, 100-5, 100-5, fill="red")
        # frame.grid()
        circle.grid(row=0, column=1)
        
        
        circle.bind("<Button-1>", self.click)
        
    def click(self,event):
        self.m3 = Label(self,text="Tu as clicque sur le bouton",font=("Helvetica", 16),borderwidth=2)
        self.m3.grid(column=1,row=1,padx=100,pady=10)
    
        


root = Tk()
root.title("Station meteo")
interface = Interface(root)
interface.pack()
interface.mainloop()
interface.destroy()
