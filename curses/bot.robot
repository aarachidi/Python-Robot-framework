** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     CurseDialog.py         WITH NAME    UserMesures
Metadata         --name    Dialogs
*** Variables ***
${numbers}    

*** Keywords ***

Entry
    [Arguments]    @{expected}
    UserMesures.createInput  @{expected}

show
    UserMesures.show       
    ${a}=    UserMesures.getResult     

*** Test Cases ***
test Function2 
    Entry       input1      in      
    Entry       input2      in1    
    Entry       input3      in2   
    show   
