
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
import re, json

class EasiiDialogs(QtWidgets.QWidget):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, parent=None):
        super(EasiiDialogs, self).__init__(parent)
        self.grid = QtWidgets.QGridLayout()

        #Input's results
        self.result = {}

        #Initialize 
        self.gridRow = 4
        self.gridColumn = 0
        self.buttonExiste = False

        self.grid.setSpacing(20)
        self.createSpace(1)

    #Bind enter with button
    def keyPressEvent(self, event):
        if event.key() == 16777220 :
            self.eventHandlerButton()
    
    def createTable(self, path):
        self.header = []

        #data
        data = self.loadJson(path)
        keys = data.keys()
        self.invalidInput = {}
        self.validInput = {}
        self.MaxValues = {}
        self.MinValues = {}

        self.writeHeader(data[list(keys)[0]])
        for key in keys:
            self.writeContent(data[key])
    
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

            entry1 = QtWidgets.QLineEdit(self)
            entry1.mousePressEvent = lambda _, entry=entry1 : entry.selectAll()
            entry1.textChanged.connect(lambda _ , entry=entry1, ma=li['max'], \
                mi = li["min"], na = name, u= li['unit'] : self.eventHandlerEntryComplex(entry, ma, mi, na, u))
            self.grid.addWidget(entry1, self.gridRow, self.gridColumn)
            self.gridColumn += 1

            lb = QtWidgets.QLabel(li['unit'], self)
            self.grid.addWidget(lb, self.gridRow, self.gridColumn)
            self.gridColumn += 1

            self.validInput[name][li['unit']] = ""
            self.invalidInput[name][li['unit']] = ""
            self.MaxValues[name][li['unit']] = li['max']
            self.MinValues[name][li['unit']] = li['min']
    
    def writeLabels(self, key, data):
        if key != "color":
            if key == "location":
                label = QtWidgets.QLabel(data[key], self)
                label.setStyleSheet('background-color : '+ data["color"])
            else:
                label = QtWidgets.QLabel(data[key], self)
            self.grid.addWidget(label, self.gridRow, self.gridColumn)
            self.gridColumn += 1
    
    def eventHandlerEntryComplex(self, element, max, min, name, type):
        if((element.text() == "")):
            element.setStyleSheet("background-color : white")
        elif(max != 0 or min != 0):
            try:
                if(float(element.text()) < min or float(element.text()) > max):
                    element.setStyleSheet("background-color : red")
                    self.invalidInput[name][type]= element.text()
                    if type in self.validInput[name].keys():
                        self.validInput[name].pop(type)
                else:
                    element.setStyleSheet("background-color : green")
                    self.validInput[name][type]= element.text()
                    if type in self.invalidInput[name].keys():
                        self.invalidInput[name].pop(type)
            except:
                element.setStyleSheet("background-color : red")
                self.invalidInput[name][type]= element.text()
                if type in self.validInput[name].keys():
                    self.validInput[name].pop(type)
    
    def writeHeader(self, data, colum=0):
        li = data[0].keys()
        for element in li:
            if not isinstance(data[0][element], list) and element != "color":
                label = QtWidgets.QLabel(element, self)
                self.grid.addWidget(label, self.gridRow, colum)
                colum += 1
        self.gridRow += 1
    


    #Create empty grids for space
    def createSpace(self, nbrSpace):
        for i in range(nbrSpace) :
            for j in range(7):
                label = QtWidgets.QLabel("\n", self)
                label.setMargin(10)
                self.grid.addWidget(label, self.gridRow, j)
            self.gridRow += 1

    
    def createLabel(self, text="", value="", width=25):
        if value != "" :
            column = 2
            justif = Qt.AlignRight
            label = QtWidgets.QLabel(value, self)
            self.grid.addWidget(label, self.gridRow, 3)
            label.setAlignment(Qt.AlignLeft)
        else:
            column = 3
            justif = Qt.AlignLeft
        label = QtWidgets.QLabel(text, self)
        label.setAlignment(justif)
        self.grid.addWidget(label, self.gridRow, column)
        self.gridRow += 1
        
    
    def createImage(self, path, width = 0, height = 0):
        pixmap = QPixmap(path)
        if width == 0 and height == 0:
            pixmap2 = pixmap.scaled(int(pixmap.width()/4), int(pixmap.height()/4))
        else:
            pixmap2 = pixmap.scaled(int(width), int(height))
        label = QtWidgets.QLabel(self)
        label.setPixmap(pixmap2)
        self.grid.addWidget(label, self.gridRow, 3, 1, 6)
        self.gridRow += 4

    #If you want to use the attributs default, width and name_width you need to use also the min and max attributs
    def createEntry(self, name="", max='0', min='0', default="0", width=25, name_width= 25):

        
        entry1 = QtWidgets.QLineEdit(self)
        entry1.setAlignment(Qt.AlignLeft)
        entry1.setText(default)
        self.grid.addWidget(entry1, self.gridRow, 3)

        if isinstance(min , float) :
            min = float(min)
        else :
            min = int(min)

        if isinstance(max , float) :
            max = float(max)
        else :
            max = int(max)

        label = QtWidgets.QLabel(name, self)
        self.grid.addWidget(label, self.gridRow, 2)
        label.setAlignment(Qt.AlignRight)

        entry1.textChanged.connect(lambda _ , entry=entry1, ma=max, \
                mi = min, na = name : self.eventHandlerEntry(entry, ma, mi, na))
        entry1.mousePressEvent = lambda _, entry=entry1 : entry.selectAll()
        self.result[name] = default
        self.gridRow += 1

    def createEntryWithRegex(self, name="", RegexExpress="", width=25, name_width= 25):


        entry1 = QtWidgets.QLineEdit(self)
        entry1.setAlignment(Qt.AlignLeft)
        self.grid.addWidget(entry1, self.gridRow, 3)

        label = QtWidgets.QLabel(name, self)
        self.grid.addWidget(label, self.gridRow, 2)
        label.setAlignment(Qt.AlignRight)

        entry1.textChanged.connect(lambda: self.eventHandlerEntryWithRegex(entry1, name, RegexExpress))
        entry1.mousePressEvent = lambda _ : entry1.selectAll()

        self.result[name] = ""
        self.gridRow += 1

    def createButton(self, text=""):

        button  =QtWidgets.QPushButton(text, self)
        button.setStyleSheet("background-color : #1ED454")
        self.grid.addWidget(button, self.gridRow + 3, 3)

        button.clicked.connect(self.eventHandlerButton)
        self.buttonExiste = True
        self.gridRow += 4

    #Results are sent when button is clicked
    def eventHandlerButton(self):
        self.close()
    
    def eventHandlerEntry(self, element, max, min, name):
        if((element.text() == "")):
            element.setStyleSheet("background-color : white")
        elif(max != 0 or min != 0):
            try:
                if(float(element.text()) < min or float(element.text()) > max):
                    element.setStyleSheet("background-color : red")
                else:
                    element.setStyleSheet("background-color : green")
            except:
                element.setStyleSheet("background-color : red")
        self.result[name] = element.text()

    def eventHandlerEntryWithRegex(self, element, name, RegexExp):
        x = re.search(RegexExp, element.text())
        if x:
            element.setStyleSheet("background-color : green")
        else:
            element.setStyleSheet("background-color : red")
        if(element.text() == ""):
            element.setStyleSheet("background-color : white")
        self.result[name] = element.text()
    
    def setApp(self, app):
        self.application = app

    def sh(self, name):
        #Create button if not existe
        if self.buttonExiste == False:
            self.createButton("Validate")
        self.createSpace(1)
        self.setLayout(self.grid)
        self.setWindowTitle(name)
        self.show()
        self.activateWindow()
        self.application.exec_()

    #Return results
    def getResult(self):
        return self.result
    
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


# application = QtWidgets.QApplication(sys.argv)
# a = EasiiDialogs()
# a.setApp(application)
# a.createImage("qrcode001.jpg", 200, 200)
# a.createEntry(name="input1", max=12, min=10, default="10")
# a.createEntry(name="input2", max=12, min=10)
# a.createEntryWithRegex(name="input3", RegexExpress="start.")
# a.createLabel(text="Name: ", value="value")
# a.sh("EasiiDialog with QT")