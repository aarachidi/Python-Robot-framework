** Settings ***
Documentation     How to use a custom Python Dialogs.
Library           implement.py

*** Variables ***

*** Keywords ***
Custom Dialogs
    [Arguments]    ${expected}
    ${users2} =	test
    Should Be True   ${users2}[0]>=1
    Should Be True   ${users2}[1]==True
    Should Be True   ${users2}[2]>=0.3


*** Test Cases ***
test Function 
    Custom Dialogs      achraf
