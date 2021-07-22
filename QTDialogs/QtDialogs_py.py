import sys
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








