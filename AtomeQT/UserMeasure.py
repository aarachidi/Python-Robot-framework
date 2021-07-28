# Python program to create a table
import json
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap


class UserMeasure(QtWidgets.QWidget):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, parent=None):

        super(UserMeasure, self).__init__(parent)
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.header = []
        self.gridRow = 10
        self.gridColumn = 0

        self.grid.setSpacing(20)
        self.createSpace(1)
        #data
        data = self.loadJson("data.json")
        keys = data.keys()
        self.result = {}
        self.invalidInput = {}
        self.validInput = {}
        self.MaxValues = {}
        self.MinValues = {}

        self.writeHeader(data[list(keys)[0]])
        for key in keys:
            self.writeContent(data[key])
        self.createSpace(1)
        self.createButton("Validate")
        self.createSpace(1)

    
    def createSpace(self, nbrSpace):
        for i in range(nbrSpace) :
            for j in range(7):
                label = QtWidgets.QLabel("\n", self)
                label.setMargin(10)
                self.grid.addWidget(label, self.gridRow, j)
            self.gridRow += 1

    def createImage(self, path="", width = 0, height = 0):
        pixmap = QPixmap(path)
        if width == 0 and height == 0:
            pixmap2 = pixmap.scaled(int(pixmap.width()/4), int(pixmap.height()/4))
        else:
            pixmap2 = pixmap.scaled(int(width), int(height))
        label = QtWidgets.QLabel(self)
        label.setPixmap(pixmap2)
        self.grid.addWidget(label, self.gridRow, 3, 1, 6)
        self.gridRow += 4

    def createButton(self, text):
        button  =QtWidgets.QPushButton(text, self)
        button.setStyleSheet("background-color : #1ED454")
        self.grid.addWidget(button, self.gridRow + 3, 3)

        button.clicked.connect(self.eventHandlerButton)
        self.gridRow += 4
    
    def eventHandlerButton(self, event):
        self.close()



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
                mi = li["min"], na = name, u= li['unit'] : self.eventHandlerEntry(entry, ma, mi, na, u))
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


    def eventHandlerEntry(self, element, max, min, name, type):
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

    def sh(self, name):
        self.createSpace(1)
        self.setWindowTitle(name)
        self.show()
        self.activateWindow()

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

application = QtWidgets.QApplication(sys.argv)
obj = UserMeasure()
obj.sh("test")
application.exec_()
