from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar, StringVar
from PIL import Image, ImageTk
import json

#Variable à retourner
result = {}

class MyFirstGUI:

    def __init__(self, master, widgetArray):
        self.master = master
        self.X=300
        self.Y=5
        master.geometry("600x400")
        self.attr1 = False
        master.title("A simple GUI")
        
        for i in widgetArray:
            self.createLabel(text=i["name"])
            self.Y = self.Y + 30
            #func = getattr(MyFirstGUI, i['type'])
            #func(self, **i)

    def createLabel(self, text=""):
        label = Label(self.master, text=text)
        label.place(x=self.X,y=self.Y)

    def createEntry(self, name="", max='0', min='0', x='0', y='0'):

        varEntry = StringVar()
        entry1 = Entry(self.master, textvariable = varEntry)
        entry1.place(x=int(x),y=int(y))
        if(int(max) != 0 and int(min) != 0):
            label1 = Label(self.master, text="min "+min)
            label1.place(x=int(x)-40,y=int(y))
            label1 = Label(self.master, text="max "+max)
            label1.place(x=int(x)+130,y=int(y))
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry, max=int(max), min=int(min), entry=entry1, nm=name: \
                self.eventHandlerEntry(varEntry, max, min, entry, nm ))
        result[name] = ""


    def createButton(self, text="", name="", x='0', y='0'):
        button = Button(self.master, text=text, bg= "#1ED454")
        button.place(x=int(x),y=int(y))
        button.bind('<Button-1>', self.eventHandlerButton)

    def createImage(self, path="", x='0', y='0', name=""):
        self.img2 = ImageTk.PhotoImage(file = path)
        self.labelEntr = Label(self.master, image=self.img2)
        self.labelEntr.place(x=int(x) , y=int(y))

    def eventHandlerEntry(self, element, max, min, entry, name):
        if(element.get() is "" and (max != 0 or min != 0)):
            entry.configure({"background": "red"})
        elif(max != 0 or min != 0):
            if(int(element.get()) < min or int(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        result[name] = element.get()

    
    def eventHandlerButton(self, event):
        #print(event.widget['text'])
        self.master.quit()

        
def test():
    f = open('data.json',)
    data = json.load(f)
    f.close()
    root = Tk()
    my_gui = MyFirstGUI(root, data['composant'])
    root.mainloop()
    

test()
#print(locals()["test"](arra))