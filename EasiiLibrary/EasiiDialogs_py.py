
from EasiiDialogs import EasiiDialogs, InputDialog, PassFailDialog, SelectionDialog, SelectionsDialog, myMessageBox
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

def pause_execution(message='Test execution paused. Press OK to continue.'):
    """Pauses test execution until user clicks `Ok` button.

    `message` is the message shown in the dialog.
    """
    myObj = myMessageBox()
    myObj.show(message)

def execute_manual_step(message, default_error = "Test failed"):
    myObj = PassFailDialog()
    myObj.show(message)
    if not myObj.result():
        raise AssertionError(default_error)

def get_value_from_user(message = "Value :", default_value=''):
    myobj = InputDialog(message, default= default_value)
    result, stat = myobj.show()
    if not stat:
        raise RuntimeError('No value provided by user')
    return result

def get_selection_from_user(message, *values):
    myobj = SelectionDialog(message, values)
    myobj.show()
    application.exec_()
    if myobj.result == None:
        raise RuntimeError('No value provided by user')
    return myobj.result


def get_selections_from_user(message, *values):
    myobj = SelectionsDialog(message, values)
    myobj.show()
    application.exec_()
    if myobj.result == None:
        raise RuntimeError('No value provided by user')
    return myobj.result

