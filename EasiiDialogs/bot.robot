** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     EasiiDialogs.py         WITH NAME    UserMesures
Metadata         --name    Dialogs
*** Variables ***
${numbers}    

*** Keywords ***
Label
    [Arguments]    @{expected}
    UserMesures.createLabel  @{expected}
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
    [Arguments]      @{expected}
    UserMesures.show        @{expected}
    ${a}=    UserMesures.getResult     

*** Test Cases ***
test Function 
    Label    name:        achraf
    Label    mot de passe
    Entry       input1     17      12   12   10  
    Entry       input2      
    Entry with regex Expression        input3      ^start
    show        Main Interface