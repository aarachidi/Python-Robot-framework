from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar, StringVar
from decimal import Decimal

class TestClass(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    #ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        
        #Variable à retourner
        self.result = {}
        self.root = Tk()
        self.x = 100
        self.y = 10
        self.root.geometry("600x400")
    
    def createLabel(self, text=""):
        label = Label(self.root, text=text)
        label.place(x=self.x,y=self.y)
        self.y = self.y + 20

    def createEntry(self, name="", max='0', min='0'):

        varEntry = StringVar()
        entry1 = Entry(self.root, textvariable = varEntry)
        entry1.place(x=self.x,y=self.y)
        if(Decimal(max) != 0 and Decimal(min) != 0):
            label1 = Label(self.root, text="min "+min)
            label1.place(x=self.x-40,y=self.y)
            label1 = Label(self.root, text="max "+max)
            label1.place(x=self.x+130,y=self.y)
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry, max=int(max), min=int(min), entry=entry1, nm=name: \
                self.eventHandlerEntry(varEntry, max, min, entry, nm ))
        self.result[name] = ""
        self.y = self.y + 30

    def eventHandlerEntry(self, element, max, min, entry, name):
        if(element.get() is "" and (max != 0 or min != 0)):
            entry.configure({"background": "red"})
        elif(max != 0 or min != 0):
            if(Decimal(element.get()) < min or Decimal(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        self.result[name] = element.get()

    def show(self):
        self.root.mainloop()

