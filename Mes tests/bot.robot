** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     UserMeasure.py         WITH NAME    UserMesures
*** Variables ***
${numbers}    

*** Keywords ***
UserMes
    UserMesures.show
    ${valide Result}=  UserMesures.getValidResult
    ${Invalide Result}=  UserMesures.getInvalidResult

*** Test Cases ***
Do Test
    UserMes