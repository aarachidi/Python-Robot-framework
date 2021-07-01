** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     MyTestApp.py         WITH NAME    UserMesures
Metadata         --name    Dialogs


*** Keywords ***

Label
    [Arguments]    @{expected}
    UserMesures.createLabel  @{expected}

Input
    [Arguments]    @{expected}
    UserMesures.createSimpleInput  @{expected}



show
    UserMesures.show 
    ${a}=    UserMesures.getResult          

*** Test Cases ***
test Function  
    Input      input1    i1
    Label      test
    show  
