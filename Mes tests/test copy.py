# Python program to create a table
   
from tkinter import *
import json
from decimal import Decimal
#Variable à retourner
result = {}

class Table:
      
    def __init__(self,root, data, rows, columns):
        root.geometry("800x800")
        
        # code for creating table
        self.label1 = Label(root, text="Name")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(root, text="Location")
        self.label2.grid(row=0, column=1)
        self.label3 = Label(root, text="Value(R)")
        self.label3.grid(row=0, column=2)
        self.label4 = Label(root, text="Value(V)")
        self.label4.grid(row=0, column=3)
        self.label5 = Label(root, text="Result")
        self.label5.grid(row=0, column=4)
        i = 10
        for dt in data:
            self.Name = Label(root, text=dt['name'] )
            self.Name.grid(row=i, column=0)
            self.loc = Label(root, text=dt['location'], bg=dt['color'])
            self.loc.grid(row=i, column=1)
            varOhm = StringVar()
            self.valOhm = Entry(root, textvariable = varOhm)
            self.valOhm.grid(row=i, column=2)
            varOhm.trace("w", lambda name, index, mode, \
            varOhm=varOhm, max=dt['ValueOhm']*1.2, min=dt['ValueOhm']*0.8, entry=self.valOhm, nm=dt['name'], type="Ohm": \
                self.eventHandlerEntry(varOhm, max, min, entry, nm , type))

            varV = StringVar()
            self.valV = Entry(root, textvariable = varV)
            self.valV.grid(row=i, column=3)
            self.result = Label(root, text="")
            self.result.grid(row=i, column=4)
            varV.trace("w", lambda name, index, mode, \
            varV=varV, max=dt['ValueT']*1.05, min=dt['ValueT']*0.95, entry=self.valV, nm=dt['name'], type="V": \
                self.eventHandlerEntry(varV, max, min, entry, nm , type))
            types = {"Ohm" : "", "V": ""}
            result[dt['name']] = types
            i += 1


    def eventHandlerEntry(self, element, max, min, entry, name, type):
        if(element.get() is "" and (max != 0 or min != 0)):
            entry.configure({"background": "red"})
        elif(max != 0 or min != 0):
            if(Decimal(element.get()) < min or Decimal(element.get()) > max):
                entry.configure({"background": "red"})
            else:
                entry.configure({"background": "green"})
        result[name][type]= element.get()  

        

  
def test():
    f = open('data.json',)
    data = json.load(f)
    f.close()
    total_rows = len(data['composant'])
    total_columns = 5
    root = Tk()
    my_gui = Table(root, data['composant'], total_rows, total_columns)
    root.mainloop()
test()
   
