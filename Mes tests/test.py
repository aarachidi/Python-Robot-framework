# Python program to create a table
   
from tkinter import *
import json
from decimal import Decimal
from PIL import Image, ImageTk
#Variable à retourner
result = {}

class Table:
      
    def __init__(self,root, data):
        self.root = root
        self.root.geometry("800x800")
        self.header = []
        self.gridRow = 0
        self.gridColumn = 0
        #create Space
        #self.createSpace(10)
        # code for creating table
        self.createImage("easii-ic.png")
        self.createSpace(10)
        self.writeHeader(data)
        self.writeContent(data)
    
    def createSpace(self, nbrSpace):
        for i in range(nbrSpace) :
            lb = Label(self.root, text=" ")
            lb.grid(row=i, column=0)
            self.gridRow += 1

    def createImage(self, path=""):
        self.img2 = ImageTk.PhotoImage(file = path)
        self.labelEntr = Label(self.root, image=self.img2)
        self.labelEntr.place(x=0, y=0, relwidth=1, relheight=0.3)

    #def createButton(self):


    def writeContent(self, data):
        for li in data:
            keys = li.keys()
            self.gridColumn = 0
            for key in keys:
                if(isinstance(li[key], list)):
                    self.writeInputs(li[key], li['name'])
                else:
                    self.writeLabels(key, li)
            self.gridRow += 1

    def writeInputs(self, data, name):
        result[name] = {}
        for li in data:
            varV = StringVar()
            self.valV = Entry(self.root, textvariable = varV, borderwidth=1, relief="ridge", width=25)
            self.valV.grid(row=self.gridRow, column=self.gridColumn)
            self.gridColumn += 1

            varV.trace("w", lambda name, index, mode, \
            varV=varV, max=li['max'], min=li['min'], entry=self.valV, nm=name, type=li['unit']: \
                self.eventHandlerEntry(varV, max, min, entry, nm , type))
            result[name][li['unit']] = ""



    def writeLabels(self, key, data):
        if key != "color":
            if key == "location":
                lb = Label(self.root, text=data[key], bg=data["color"], borderwidth=1, relief="ridge", width=20)
            else:
                lb = Label(self.root, text=data[key], borderwidth=1, relief="ridge", width=20)
            lb.grid(row=self.gridRow, column=self.gridColumn)
            self.gridColumn += 1


    def eventHandlerEntry(self, element, max, min, entry, name, type):
        if(element.get() is "" and (max != 0 or min != 0)):
            entry.configure({"background": "red"})
        elif(max != 0 or min != 0):
            if(Decimal(element.get()) < min or Decimal(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        result[name][type]= element.get()  

    def writeHeader(self, data, colum=0):
        li = data[0].keys()
        for element in li:
            if isinstance(data[0][element], list):
                for dt in data[0][element]:
                    self.header.append(Label(self.root, text=dt["unit"], borderwidth=1, relief="ridge", width=20))
                    self.header[colum].grid(row=self.gridRow, column=colum)
                    colum += 1
            elif element != "color":
                self.header.append(Label(self.root, text=element, borderwidth=1, relief="ridge", width=20))
                self.header[colum].grid(row=self.gridRow, column=colum)
                colum += 1
        self.header.append(Label(self.root, text="Résult", borderwidth=1, relief="ridge", width=20))
        self.header[colum].grid(row=self.gridRow, column=colum)
        self.gridRow += 1


  
def test():
    f = open('data copy.json',)
    data = json.load(f)
    f.close()
    root = Tk()
    my_gui = Table(root, data['composant'])
    root.mainloop()
test()
   
