** Settings ***
Documentation     How to use a custom Python Dialogs.
Library           script.py

*** Variables ***
@{numbers}    1    2    3
&{function1}       type=createEntry    name=variable1     x=40    y=30      max=10   min=2
&{function2}       type=createEntry    name=variable2     x=140    y=130
&{function3}       type=createImage     name=Img        x=150    y=150   path=easii-ic.png
*** Keywords ***
Custome Dialog
    [Documentation]     This keyword make a custom dialog depending on 
    ...                 the input.              
    ...                 The variables passed to the keyword must be dictionaries.\n
    ...                 There is three types of widgets :\n
    ...                 -----createEntry  for user's input\n
    ...                 Example :\n
    ...                 &{example1}       type=createEntry(required)    name=variable1(required)     x=40    y=30      max=10   min=2\n
    ...                 Custome Dialog   ${example1}\n
    ...                 -----createImage  to insert images\n
    ...                 Example :\n
    ...                 &{example2}       type=createImage(required)     name=Img(required)        x=150    y=150   path=example.png(required)\n
    ...                 Custome Dialog   ${example2}
    ...                 -----createButton  to insert button\n
    ...                 Example :\n
    ...                 &{example3}       type=createButton(required)     name=Bt(required)        x=150    y=150   text=validate(required)\n
    ...                 Custome Dialog   ${example3}
    [Arguments]    @{expected}
    ${a}=   test    ${expected}


*** Test Cases ***
test Function 
    Custome Dialog   ${function1}   ${function2}    ${function3}