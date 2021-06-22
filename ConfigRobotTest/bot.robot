** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     TestClass.py         WITH NAME    class1
*** Variables ***
${numbers}    

*** Keywords ***
Label
    [Arguments]    @{expected}
    class1.createLabel  ${expected}
Entry
    [Arguments]    @{expected}
    class1.createEntry  @{expected}
Button
    [Arguments]    @{expected}
    class1.createButton  @{expected}
show
    class1.show
    ${a}=    class1.getResult

*** Test Cases ***
test Function 
    Label  achraf
    Label   Oussama
    Entry  a   10    2
    Button  validate
    show