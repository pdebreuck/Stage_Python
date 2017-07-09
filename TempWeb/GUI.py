from tkinter import *

class Interface(Frame):
    
    
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=1000, height=1000, **kwargs)
        #self.pack(fill=BOTH)
        
        #widgets
        self.message = Label(self, text="Cliquez sur 'Temp' pour mesurer la temperature",width=50,height=5)
        self.message.grid(column=2,row=0)
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.grid(column=0,row=0)
        
        self.bouton_cliquer = Button(self, text="Temp", fg="red",
                command=self.clic)
        self.bouton_cliquer.grid(column = 2, row = 1)
        
        self.m2 = Label(self, text="La temperature est - ",width=50,height=5)
        self.m2.grid(column=2,row=2)
    
    def clic(self):     
        
        self.m2["text"] = "La temperature est 25"



root = Tk()
interface = Interface(root)
interface.pack()
interface.mainloop()
interface.destroy()
