from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar, StringVar, END
import re
from tkinter.constants import TRUE

class EasiiDialogs(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    #ROBOT_LIBRARY_SCOPE = 'SUITE'
    def __init__(self):
        
        #Variable à retourner
        self.result = {}
        self.root = Tk()
        self.gridRow = 4
        self.gridColumn = 0
        self.buttonExiste = False
        #Set interface in front
        self.root.attributes("-topmost", True)
        #Bind enter with button
        self.root.bind('<Return>', self.eventHandlerButton)

        col_count, row_count = self.root.grid_size()
        for col in range(col_count):
            self.root.grid_columnconfigure(col, minsize=20)

        for row in range(row_count):
            self.root.grid_rowconfigure(row, minsize=20)

    def createSpace(self, nbrSpace):
        for i in range(nbrSpace) :
            lb = Label(self.root, text="\n")
            lb.grid(row=self.gridRow, column=8)
            self.gridRow += 1

    
    def createLabel(self, text="", value="", width=25):
        if value != "" :
            column = 2
            justif = 'e'
            label = Label(self.root, text=value, width=width, anchor='w')
            label.grid(row=self.gridRow, column=3)
        else:
            column = 3
            justif = 'w'
        label = Label(self.root, text=text, width=width, anchor=justif)
        label.grid(row=self.gridRow, column=column)
        self.gridRow += 1
        

    def createEntry(self, name="", max='0', min='0', default="0", width=25, name_width= 25):

        varEntry = StringVar(value=default)
        entry1 = Entry(self.root, textvariable = varEntry, width= width)
        entry1.grid(row=self.gridRow, column=3, sticky ="w")

        if isinstance(min , float) :
            min = float(min)
        else :
            min = int(min)

        if isinstance(max , float) :
            max = float(max)
        else :
            max = int(max)

        nameEntry = Label(self.root, text=name, width= name_width, anchor='e')
        nameEntry.grid(row=self.gridRow, column=2)

        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry, max=int(max), min=int(min), entry=entry1, nm=name: \
                self.eventHandlerEntry(varEntry, max, min, entry, nm ))
        self.result[name] = ""
        self.gridRow += 1
        entry1.bind("<FocusIn>", self.selectEntry)

    def createEntryWithRegex(self, name="", RegexExpress="", width=25, name_width= 25):

        varEntry = StringVar()
        entry1 = Entry(self.root, textvariable = varEntry, width= width)
        entry1.grid(row=self.gridRow, column=3, sticky ="w")
        nameEntry = Label(self.root, text=name, width= name_width, anchor='e')
        nameEntry.grid(row=self.gridRow, column=2)
        varEntry.trace("w", lambda name, index, mode, \
            varEntry=varEntry,  entry=entry1, nm=name, RegexExp=RegexExpress: \
                self.eventHandlerEntryWithRegex(varEntry, entry, nm , RegexExp))
        self.result[name] = ""
        self.gridRow += 1
        entry1.bind("<FocusIn>", self.selectEntry)

    def createButton(self, text=""):
        button = Button(self.root, text=text, bg= "#1ED454")
        button.grid(row=self.gridRow + 3, column=3)
        button.bind('<Button-1>', self.eventHandlerButton)
        self.buttonExiste = TRUE
        self.gridRow += 3

    def eventHandlerButton(self, event):
        #print(event.widget['text'])
        self.root.quit()
    
    def eventHandlerEntry(self, element, max, min, entry, name):
        if((element.get() == "")):
            entry.configure({"background": "white"})
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
        if(element.get() == ""):
            entry.configure({"background": "white"})
        self.result[name] = element.get()

    def show(self, name):
        #Create button if not existe
        if self.buttonExiste == False:
            self.createButton("Validate")
        self.createSpace(5)
        col_count, row_count = self.root.grid_size()
        for col in range(col_count):
            self.root.grid_columnconfigure(col, minsize=20)

        for row in range(row_count):
            self.root.grid_rowconfigure(row, minsize=20)
        self.root.title(name)
        self.root.mainloop()

    def getResult(self):
        return self.result

    def selectEntry(self, event):
        event.widget.selection_range(0, END)
