
from EasiiDialogs import EasiiDialogs
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
import re

application = QtWidgets.QApplication([""])


def init():
    myObj = EasiiDialogs()
    return myObj
def appVal():
    return application
