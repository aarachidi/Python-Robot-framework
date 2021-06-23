** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     UserMeasure.py         WITH NAME    UserMesures
*** Variables ***
${numbers}    

*** Keywords ***
UserMes
    UserMesures.show
    ${valid Result}=  UserMesures.getValidResult
    ${Invalid Result}=  UserMesures.getInvalidResult

*** Test Cases ***
Do Test
    UserMes