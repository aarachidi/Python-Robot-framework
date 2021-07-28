** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     OperatingSystem
Library     test.py
*** Variables *** 

*** Keywords ***
init
    ${obj1} =      test.init
    ${app} =       test.appVal
    Set Global Variable   ${obj}    ${obj1}
    Call Method    ${obj}       setApp     ${app}

Label
    [Arguments]    @{expected}
    Call Method    ${obj}      createLabel     @{expected}

Entry
    [Arguments]    @{expected}
    Call Method    ${obj}      createEntry  @{expected}


Entry with regex Expression
    [Arguments]    @{expected}
    Call Method    ${obj}      createEntryWithRegex  @{expected}


Button
    [Arguments]    @{expected}
    UserMesures.createButton  @{expected}


show
    [Arguments]      @{expected}
    Call Method    ${obj}      sh        @{expected}
    ${a}=    Call Method    ${obj}       getResult 


    