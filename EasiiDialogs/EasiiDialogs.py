from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar, StringVar
import re

class EasiiDialogs(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    #ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        
        #Variable à retourner
        self.result = {}
        self.root = Tk()
        self.x = 100
        self.y = 10
        self.root.geometry("300x300")
        #Set interface in front
        self.root.attributes("-topmost", True)
    
    def createLabel(self, text=""):
        label = Label(self.root, text=text)
        label.place(x=self.x,y=self.y)
        self.y = self.y + 20

    def createEntry(self, name="", max='0', min='0'):

        varEntry = StringVar()
        entry1 = Entry(self.root, textvariable = varEntry)
        entry1.place(x=self.x,y=self.y)

        if isinstance(min , float) :
            min = float(min)
        else :
            min = int(min)

        if isinstance(max , float) :
            max = float(max)
        else :
            max = int(max)

        if(max != 0 or min != 0):
            label1 = Label(self.root, text=str(min))
            label1.place(x=self.x-40,y=self.y)
            label1 = Label(self.root, text=str(max))
            label1.place(x=self.x+130,y=self.y)
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry, max=int(max), min=int(min), entry=entry1, nm=name: \
                self.eventHandlerEntry(varEntry, max, min, entry, nm ))
        self.result[name] = ""
        self.y = self.y + 30

    def createEntryWithRegex(self, name="", RegexExpress=""):

        varEntry = StringVar()
        entry1 = Entry(self.root, textvariable = varEntry)
        entry1.place(x=self.x,y=self.y)
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry,  entry=entry1, nm=name + " : ", RegexExp=RegexExpress: \
                self.eventHandlerEntryWithRegex(varEntry, entry, nm , RegexExp))
        self.result[name] = ""
        self.y = self.y + 30

    def createButton(self, text=""):
        button = Button(self.root, text=text, bg= "#1ED454")
        button.place(x=self.x,y=self.y)
        button.bind('<Button-1>', self.eventHandlerButton)
        self.y = self.y + 20

    def eventHandlerButton(self, event):
        #print(event.widget['text'])
        self.root.quit()
        return "ace"
    
    def eventHandlerEntry(self, element, max, min, entry, name):
        if((element.get() == "") and (max != 0 or min != 0)):
            entry.configure({"background": "red"})
        elif(max != 0 or min != 0):
            if(float(element.get()) < min or float(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        self.result[name] = element.get()

    def eventHandlerEntryWithRegex(self, element, entry, name, RegexExp):
        x = re.search(RegexExp, element.get())
        if x:
            entry.configure({"background": "green"})
        else:
            entry.configure({"background": "red"})
        self.result[name] = element.get()

    def show(self):
        self.root.mainloop()

    def getResult(self):
        return self.result
