** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     UserMeasure.py         WITH NAME    UserMesures
*** Variables ***
${numbers}    

*** Keywords ***
UserMes
    UserMesures.show
    ${a}=  UserMesures.getResult

*** Test Cases ***
Do Test
    UserMes