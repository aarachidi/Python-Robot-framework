** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     Dialogs
Library     OperatingSystem
Metadata         --name    Dialogs
*** Variables ***
${numbers}    

*** Keywords ***
init
    ${files} =	  List Files In Directory  	.	 EasiiDialogs.py	     absolute
    Log    ${files}[0]
    Import Library       ${files}[0]       WITH NAME     UserMesures
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
Style
    [Arguments]    @{expected}
    UserMesures.changePolice  @{expected}
show
    [Arguments]      @{expected}
    UserMesures.show        @{expected}
    ${a}=    UserMesures.getResult 
Del init    
    UserMesures.close
*** Test Cases ***
test Function
    Pause Execution
    init
    Style       mincho       15
    Label    name:        achraf
    Label    mot de passe
    Entry       input1     17      12   12   10  
    Entry       input2      
    Entry with regex Expression        input3      ^start
    show        Main Interface
    Del init