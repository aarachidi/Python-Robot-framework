** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     EasiiDialogs.py         WITH NAME    UserMesures
*** Variables ***
${numbers}    

*** Keywords ***
Label
    [Arguments]    @{expected}
    UserMesures.createLabel  ${expected}
Entry
    [Arguments]    @{expected}
    UserMesures.createEntry  @{expected}
Entry with regix Expression
    [Arguments]    @{expected}
    UserMesures.createEntryWithRegix  @{expected}
Button
    [Arguments]    @{expected}
    UserMesures.createButton  @{expected}
show
    UserMesures.show
    ${a}=    UserMesures.getResult

*** Test Cases ***
test Function 
    Entry with regix Expression    b    start.$
    Button  validate
    show