from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar, StringVar
from PIL import Image, ImageTk

#Variable à retourner
result = {}

class MyFirstGUI:

    def __init__(self, master, widgetArray):
        self.master = master
        master.geometry("600x400")
        self.attr1 = False
        master.title("A simple GUI")
        
        for i in widgetArray:
            func = getattr(MyFirstGUI, i['type'])
            func(self, **i)

    def createLabel(self, text="", x="0", y="0", type=""):
        label = Label(self.master, text=text)
        label.place(x=int(x),y=int(y))

    def createEntry(self, name="", max='0', min='0', x='0', y='0', type=""):

        varEntry = StringVar()
        entry1 = Entry(self.master, textvariable = varEntry)
        entry1.place(x=int(x),y=int(y))
        if(int(max) != 0 and int(min) != 0):
            label1 = Label(self.master, text="min"+min)
            label1.place(x=int(x)-40,y=int(y))
            label1 = Label(self.master, text="max"+max)
            label1.place(x=int(x)+130,y=int(y))
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry, max=int(max), min=int(min), entry=entry1, nm=name: \
                self.eventHandlerEntry(varEntry, max, min, entry, nm ))
        result[name] = ""


    def createButton(self, text="", name="", x='0', y='0', type=""):
        button = Button(self.master, text=text, bg= "#1ED454")
        button.place(x=int(x),y=int(y))

    def createImage(self, path="", x='0', y='0', name="", type=""):
        self.img2 = ImageTk.PhotoImage(file = path)
        self.labelEntr = Label(self.master, image=self.img2)
        self.labelEntr.place(x=int(x) , y=int(y))

    def eventHandlerEntry(self, element, max, min, entry, name):
        if(element.get() is ""):
            entry.configure({"background": "red"})
        elif(max != 0 and min != 0):
            if(int(element.get()) < min or int(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        result[name] = element.get()

        
def test(ar):
    root = Tk()
    arr = [
        {
            'type' : 'createEntry',
            'name' : 'variable1',
            'x' : 40,
            'y' : 30,
            'max' : 10,
            'min' : 2
        },
        {
            'type' : 'createButton',
            'name' : 'variable2',
            'text' : 'no',
            'x'    : 500,
            'y'    : 300
        },
        {
            'type' : 'createEntry',
            'x' : 40,
            'y' : 130,
            'max' : 100,
            'min' : 50
        },
        {
            'type' : 'createImage',
            'name'  :  'image',
            'x' :   150,
            'y' :   130,
            'path' : 'easii-ic.png'
        }
    ] 
    my_gui = MyFirstGUI(root, ar)
    root.mainloop()
    return result

#test()

#arra = [1, 2]
#tes = "test"
#print(locals()["test"](arra))