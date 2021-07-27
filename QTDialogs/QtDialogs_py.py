import sys
from tkinter.constants import SE
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt


class myMessageBox(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super(myMessageBox, self).__init__(parent)
    def show(self, message):
        self.setIcon(QtWidgets.QMessageBox.Information)
        self.setTextFormat(Qt.RichText)
        self.setText("<h1>"+message+"</h1>")
        self.setWindowTitle("Pause Test")
        self.exec_()

class PassFailDialog(myMessageBox):
    def __init__(self, parent=None):
        super(PassFailDialog, self).__init__(parent)
        self.passed = self.addButton("Pass", QtWidgets.QMessageBox.ActionRole)
        self.Failed = self.addButton("Fail", QtWidgets.QMessageBox.ActionRole)

    def result(self):
        if self.clickedButton() == self.passed:
            return True
        else:
            return False

class InputDialog(QtWidgets.QInputDialog):
    def __init__(self,message, default="",  parent=None):
        super(InputDialog, self).__init__(parent)
        self.message = message
        self.default = default
    def show(self):
        input, done = self.getText(self, 'Robot framework', self.message, QtWidgets.QLineEdit.Normal,self.default) 
        return input, done

class SelectionDialog(QtWidgets.QWidget):
    def __init__(self, message, choice,  parent=None):
        super(SelectionDialog, self).__init__(parent)
        self.setWindowTitle(message)
        self.listWidget = QtWidgets.QListWidget()
        for value in choice:
            QtWidgets.QListWidgetItem(value, self.listWidget)
        
        #List of option
        window_layout = QtWidgets.QVBoxLayout(self)
        window_layout.addWidget(self.listWidget)

        #Buttons
        self.okB = QtWidgets.QPushButton("Ok")
        self.okB.clicked.connect(self.okFunction)
        self.cancelB = QtWidgets.QPushButton("Cancel")
        self.cancelB.clicked.connect(self.close)
        hbox = QtWidgets.QGridLayout()
        hbox.addWidget(self.okB, 0, 0)
        hbox.addWidget(self.cancelB, 0, 3)

        window_layout.addLayout(hbox)
        self.setLayout(window_layout)

        self.result = None
    
    def okFunction(self):
        li = self.listWidget.selectedItems()
        if len(li) > 0:
            for item in li:
                self.result = item.text()
            self.close()

class SelectionsDialog(SelectionDialog):
    def __init__(self, message, choice,  parent=None):
        super(SelectionsDialog, self).__init__(message, choice, parent)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    def okFunction(self):
        li = self.listWidget.selectedItems()
        if len(li) > 0:
            self.result = []
            for item in li:
                self.result.append(item.text())
            self.close()














