** Settings ***
Documentation     How to use a custom Python Dialogs.
Library           implement.py

*** Variables ***

*** Keywords ***
Custom Dialogs
    ${users2} =	test
    Should Be True   ${users2}[0]==True
    Should Be True   ${users2}[1]>=0.3

*** Test Cases ***
test Function 
    Custom Dialogs
