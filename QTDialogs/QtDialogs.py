import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from QtDialogs_py import myMessageBox

def pause_execution(message='Test execution paused. Press OK to continue.'):
    """Pauses test execution until user clicks `Ok` button.

    `message` is the message shown in the dialog.
    """
    myObj = myMessageBox()
    myObj.show(message)