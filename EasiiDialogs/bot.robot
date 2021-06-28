** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     EasiiDialogs.py         WITH NAME    UserMesures
Metadata         --name    Dialogs
*** Variables ***
${numbers}    

*** Keywords ***
Label
    [Arguments]    @{expected}
    UserMesures.createLabel  ${expected}
Entry
    [Arguments]    @{expected}
    UserMesures.createEntry  @{expected}
Entry with regex Expression
    [Arguments]    @{expected}
    UserMesures.createEntryWithRegex  @{expected}
Button
    [Arguments]    @{expected}
    UserMesures.createButton  @{expected}
show
    UserMesures.show
    ${a}=    UserMesures.getResult

*** Test Cases ***
test Function 
    Entry    test    3   4
    Entry with regex Expression    b    start.$
    Button  validate
    show