# Python program to create a table
   
from tkinter import *
import json
from PIL import Image, ImageTk


class UserMeasure(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        self.root = Tk()
        self.root.geometry("+250+50")
        self.header = []
        self.gridRow = 10
        self.gridColumn = 0

        #data
        data = self.loadJson("data.json")
        keys = data.keys()
        self.result = {}
        self.invalidInput = {}
        self.validInput = {}
        self.MaxValues = {}
        self.MinValues = {}

        # code for creating table
        self.createImage("easii-ic.png")
        self.writeHeader(data[list(keys)[0]])
        for key in keys:
            self.writeContent(data[key])
        self.createSpace(1)
        self.createButton("Validate")
        self.createSpace(2)


        col_count, row_count = self.root.grid_size()

        for col in range(col_count):
            self.root.grid_columnconfigure(col, minsize=20)

        for row in range(row_count):
            self.root.grid_rowconfigure(row, minsize=20)
    
    def createSpace(self, nbrSpace):
        for i in range(nbrSpace) :
            lb = Label(self.root, text="\n")
            lb.grid(row=i, column=0)
            self.gridRow += 1

    def createImage(self, path=""):
        self.img2 = ImageTk.PhotoImage(file = path)
        self.labelEntr = Label(self.root, image=self.img2)
        self.labelEntr.place(x=0, y=0, relwidth=1, relheight=0.3)

    def createButton(self, text):
        button = Button(self.root, text=text, bg= "#1ED454")
        button.grid(row=self.gridRow, column=2)
        button.bind('<Button-1>', self.eventHandlerButton)
    
    def eventHandlerButton(self, event):
        self.root.quit()



    def writeContent(self, data):
        if isinstance(data, list) != True:
            print("erreur")
        else:
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
        self.validInput[name] = {}
        self.invalidInput[name] = {}
        self.MaxValues[name] = {}
        self.MinValues[name] = {}
        for li in data:
            varV = StringVar()
            self.valV = Entry(self.root, textvariable = varV, borderwidth=1, relief="ridge", width=25)
            self.valV.grid(row=self.gridRow, column=self.gridColumn)
            self.gridColumn += 1
            
            lb = Label(self.root, text=li['unit'], borderwidth=1, relief="ridge", width=15)
            lb.grid(row=self.gridRow, column=self.gridColumn)
            self.gridColumn += 1

            varV.trace("w", lambda name, index, mode, \
            varV=varV, max=li['max'], min=li['min'], entry=self.valV, nm=name, type=li['unit']: \
                self.eventHandlerEntry(varV, max, min, entry, nm , type))
            self.validInput[name][li['unit']] = ""
            self.invalidInput[name][li['unit']] = ""
            self.MaxValues[name][li['unit']] = li['max']
            self.MinValues[name][li['unit']] = li['min']



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
            if(float(element.get()) < min or float(element.get()) > max):
                entry.configure({"background": "red"})
                self.invalidInput[name][type]= element.get()
                if type in self.validInput[name].keys():
                    self.validInput[name].pop(type)
            else:
                entry.configure({"background": "green"})
                self.validInput[name][type]= element.get()
                if type in self.invalidInput[name].keys():
                    self.invalidInput[name].pop(type)
                 

    def writeHeader(self, data, colum=0):
        li = data[0].keys()
        for element in li:
            if not isinstance(data[0][element], list) and element != "color":
                self.header.append(Label(self.root, text=element, borderwidth=1, relief="ridge", width=20))
                self.header[colum].grid(row=self.gridRow, column=colum)
                colum += 1
        self.gridRow += 1

    def show(self):
        self.root.mainloop()

    def getValidResult(self):
        for element in list(self.validInput):
            li = list(self.validInput[element])
            if(len(li) == 0):
                self.validInput.pop(element)
        return self.validInput

    def getInvalidResult(self):
        for element in list(self.invalidInput):
            li = list(self.invalidInput[element])
            if(len(li) == 0):
                self.invalidInput.pop(element)
        return self.invalidInput

    def getMaxValues(self):
        return self.MaxValues

    def getMinValues(self):
        return self.MinValues

    def loadJson(self, path):
        f = open(path,)
        data = json.load(f)
        f.close()
        return data
