import sys
from tkinter import Entry
from tkinter.constants import END
from robot.libraries.dialogs_py import MessageDialog, PassFailDialog, InputDialog, SelectionDialog


class MyMessageDialog(MessageDialog):
    def __init__(self, message):
        super().__init__(message)
        self.bind('<Return>', self.eventHandlerButton)

    def eventHandlerButton(self, event):
        self._close()

class MySelectionDialog(SelectionDialog):
    def __init__(self, message, values):
        super().__init__(message, values)
        self.bind('<Return>', self.eventHandlerButton)

    def eventHandlerButton(self, event):
        self._close()


class MyInputDialog(InputDialog):
    def __init__(self, message, default_value):
        super().__init__(message, default_value)
        self.bind('<Return>', self.eventHandlerButton)

    def eventHandlerButton(self, event):
        self._close()



def  pause_execution(message='Test execution paused. Press OK to continue.'):
    MyMessageDialog(message).show()


def get_value_from_user(message, default_value=''):
    """Pauses test execution and asks user to input a value.

    `message` is the instruction shown in the dialog and `default_value` is
    the possible default value shown in the input field. Selecting 'Cancel'
    fails the keyword.
    """
    return _validate_user_input(MyInputDialog(message, default_value))

def get_selection_from_user(message, *values):
    """Pauses test execution and asks user to select a value.

    `message` is the instruction shown in the dialog and `values` are
    the options given to the user. Selecting 'Cancel' fails the keyword.
    """
    return _validate_user_input(MySelectionDialog(message, values))


def _validate_user_input(dialog):
    value = dialog.show()
    if value is None:
        raise RuntimeError('No value provided by user')
    return value

        
        
