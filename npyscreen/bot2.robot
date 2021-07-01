** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     MyTestApp.py         WITH NAME    UserMesures
Library     EasiiDialogs.py         WITH NAME    UserMesures2
Metadata         --name    Dialogs


*** Keywords ***

Label
    [Arguments]    @{expected}
    IF      '${mode}' =='command'    
    ${instance}     Get library instance     UserMesures
    ELSE
    ${instance}     Get library instance     UserMesures2
    END
    Call Method     ${instance}         createLabel      @{expected}

Input
    [Arguments]    @{expected}
    IF      '${mode}' =='command'    
    ${instance}     Get library instance     UserMesures
    ELSE
    ${instance}     Get library instance     UserMesures2
    END
    Call Method     ${instance}         createEntry      @{expected}

show
    [Arguments]    @{expected}
    IF      '${mode}' =='command'    
    ${instance}     Get library instance     UserMesures
    ELSE
    ${instance}     Get library instance     UserMesures2
    END
    Call Method     ${instance}         show      @{expected}
    ${result} =    Call Method     ${instance}         getResult      @{expected}     

*** Test Cases ***
test Function  
    Input      input1 
    Label      test
    Input      input2
    show  
