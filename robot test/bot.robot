** Settings ***
Documentation     How to use a custom Python Dialogs.
Library           script.py

*** Variables ***
@{numbers}    1    2    3
&{function1}       type=createEntry    name=variable1     x=40    y=30      max=10   min=2
&{function2}       type=createEntry    name=variable2     x=140    y=130
*** Keywords ***
Print arguments
    [Arguments]    @{expected}
    ${a}=   test    ${expected}


*** Test Cases ***
test Function 
    Print arguments  ${function1}   ${function2}