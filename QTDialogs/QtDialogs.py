import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from QtDialogs_py import InputDialog, PassFailDialog, SelectionDialog, SelectionsDialog, myMessageBox

def pause_execution(message='Test execution paused. Press OK to continue.'):
    """Pauses test execution until user clicks `Ok` button.

    `message` is the message shown in the dialog.
    """
    application = QtWidgets.QApplication(sys.argv)
    myObj = myMessageBox()
    myObj.show(message)

def execute_manual_step(message):
    application = QtWidgets.QApplication(sys.argv)
    myObj = PassFailDialog()
    myObj.show(message)
    if not myObj.result():
        raise AssertionError("Test failed")

def get_value_from_user(message, default_value=''):
    application = QtWidgets.QApplication(sys.argv)
    myobj = InputDialog(message="put a value", default= default_value)
    result, stat = myobj.show()
    if not stat:
        raise RuntimeError('No value provided by user')
    return result

def get_selection_from_user(message, *values):
    application = QtWidgets.QApplication(sys.argv)
    myobj = SelectionDialog(message, values)
    myobj.show()
    application.exec_()
    if myobj.result == None:
        raise RuntimeError('No value provided by user')
    return myobj.result


def get_selections_from_user(message, *values):
    application = QtWidgets.QApplication(sys.argv)
    myobj = SelectionsDialog(message, values)
    myobj.show()
    application.exec_()
    if myobj.result == None:
        raise RuntimeError('No value provided by user')
    return myobj.result

        